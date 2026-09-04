"""Update script for trending-claude-skills.

Runs on a cron via .github/workflows/update.yml every 15
minutes. Fetches the upstream data, diffs against data/items.json, rewrites
the README between sentinel markers, writes a new JSON snapshot. The
workflow then commits any diff with a message like
``feat: +N added, -M removed (timestamp)``.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx


DATA_FILE = Path("data/items.json")
README_FILE = Path("README.md")
TABLE_START = "<!-- TRACKER_TABLE_START -->"
TABLE_END = "<!-- TRACKER_TABLE_END -->"
LAST_UPDATED_RE = re.compile(r"^> ⏰ Last updated: .+$", re.MULTILINE)
ITEMS_BADGE_RE = re.compile(r"badge/Tracked_Items-\d+-brightgreen")


# === Data fetch =====================================================
# The default fetcher queries the GitHub Search API for repos matching a
# topic + recent push. Replace ``fetch_items`` if your tracker needs a
# different upstream.

GITHUB_QUERY = 'topic:claude-skills sort:updated-desc'
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
MAX_ITEMS = 50


def calculate_score(item: dict) -> float:
    """Calculate ranking score based on freshness (pushed_at/updated_at) and stars.
    Prioritizes recent activity (freshness) over all-time stars."""
    stars = item.get("stars", item.get("stargazers_count", 0))
    updated_str = item.get("updated_at", item.get("pushed_at", ""))

    score = float(stars)
    if updated_str:
        try:
            dt = datetime.fromisoformat(str(updated_str).replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            days_ago = max(0.0, (now - dt).total_seconds() / 86400.0)
            recency_boost = max(0.0, 100.0 - days_ago * 2.0)
            score += recency_boost * 10.0
        except (ValueError, TypeError):
            pass
    return score


def rank_items(items: list[dict]) -> list[dict]:
    """Sort items by calculated ranking score descending."""
    return sorted(items, key=calculate_score, reverse=True)


def fetch_items() -> list[dict]:
    """Return a list of current items. Each item must have an ``id``
    (stable identifier used for diffing) and the columns rendered in
    the table."""
    if not GITHUB_TOKEN:
        print("WARN: GITHUB_TOKEN not set; running with anonymous quota")
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    url = "https://api.github.com/search/repositories"
    params = {"q": GITHUB_QUERY, "sort": "updated", "order": "desc", "per_page": MAX_ITEMS}
    resp = httpx.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()
    out = []
    for r in resp.json().get("items", [])[:MAX_ITEMS]:
        out.append({
            "id": r["full_name"],
            "name": r["full_name"],
            "url": r["html_url"],
            "stars": r["stargazers_count"],
            "language": r.get("language") or "—",
            "description": (r.get("description") or "")[:120],
            "updated_at": r["pushed_at"],
        })
    return rank_items(out)


# === Diff + render ==================================================


def load_previous() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        return []


def diff_counts(old: list[dict], new: list[dict]) -> tuple[int, int]:
    old_ids = {i["id"] for i in old}
    new_ids = {i["id"] for i in new}
    return len(new_ids - old_ids), len(old_ids - new_ids)


def render_table(items: list[dict]) -> str:
    if not items:
        return "_No items in the upstream feed right now. Next check in 15 minutes._"
    rows = ["| # | Name | ⭐ | Lang | Updated | Description |",
            "|---|------|---|------|---------|-------------|"]
    for i, it in enumerate(items, 1):
        name = f"[{it['name']}]({it['url']})"
        desc = (it.get("description") or "").replace("|", "\\|")
        updated = it.get("updated_at", "")[:10]
        rows.append(f"| {i} | {name} | {it.get('stars', 0)} | {it.get('language', '—')} | {updated} | {desc} |")
    return "\n".join(rows)


def rewrite_readme(items: list[dict]) -> None:
    txt = README_FILE.read_text()

    table = render_table(items)
    section = f"{TABLE_START}\n{table}\n{TABLE_END}"
    pattern = re.compile(re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END), re.DOTALL)
    txt = pattern.sub(section, txt)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    txt = LAST_UPDATED_RE.sub(f"> ⏰ Last updated: {now}", txt)

    txt = ITEMS_BADGE_RE.sub(f"badge/Tracked_Items-{len(items)}-brightgreen", txt)

    README_FILE.write_text(txt)


def main() -> int:
    items = fetch_items()
    previous = load_previous()
    added, removed = diff_counts(previous, items)

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(items, indent=2, sort_keys=True))
    rewrite_readme(items)

    now_short = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    msg = f"feat: +{added} added, -{removed} removed ({now_short})"
    print(msg)

    # The workflow will commit only if there's a diff. Surface the message
    # via GITHUB_OUTPUT so the workflow can use it.
    gho = os.environ.get("GITHUB_OUTPUT")
    if gho:
        with open(gho, "a") as f:
            f.write(f"message={msg}\n")
            f.write(f"changed={'true' if (added or removed) else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
