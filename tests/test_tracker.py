import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from tracker import (
    calculate_score,
    rank_items,
    diff_counts,
    render_table,
    load_previous,
    rewrite_readme,
    fetch_items,
    DATA_FILE,
    README_FILE,
)


def test_calculate_score_freshness_prioritized():
    now = datetime.now(timezone.utc)
    recent_dt = (now - timedelta(hours=1)).isoformat()
    old_dt = (now - timedelta(days=200)).isoformat()

    recent_repo = {
        "name": "recent-repo",
        "stars": 10,
        "updated_at": recent_dt,
    }
    old_repo = {
        "name": "old-repo",
        "stars": 50,
        "updated_at": old_dt,
    }

    recent_score = calculate_score(recent_repo)
    old_score = calculate_score(old_repo)

    assert recent_score > old_score


def test_calculate_score_invalid_or_missing_date():
    repo_missing_date = {"name": "repo1", "stars": 25, "updated_at": ""}
    repo_bad_date = {"name": "repo2", "stars": 25, "updated_at": "invalid-date"}

    assert calculate_score(repo_missing_date) == 25.0
    assert calculate_score(repo_bad_date) == 25.0


def test_rank_items_sorting():
    now = datetime.now(timezone.utc)
    items = [
        {"name": "repo-old", "stars": 100, "updated_at": (now - timedelta(days=100)).isoformat()},
        {"name": "repo-fresh", "stars": 20, "updated_at": (now - timedelta(minutes=5)).isoformat()},
        {"name": "repo-mid", "stars": 30, "updated_at": (now - timedelta(days=1)).isoformat()},
    ]

    ranked = rank_items(items)
    ranked_names = [i["name"] for i in ranked]

    assert ranked_names[0] == "repo-fresh"
    assert ranked_names[1] == "repo-mid"
    assert ranked_names[2] == "repo-old"


def test_diff_counts():
    old = [{"id": "repo1"}, {"id": "repo2"}, {"id": "repo3"}]
    new = [{"id": "repo2"}, {"id": "repo3"}, {"id": "repo4"}, {"id": "repo5"}]

    added, removed = diff_counts(old, new)
    assert added == 2
    assert removed == 1


def test_render_table_empty():
    assert "No items in the upstream feed" in render_table([])


def test_render_table_content():
    items = [
        {
            "name": "owner/repo-one",
            "url": "https://github.com/owner/repo-one",
            "stars": 42,
            "language": "Python",
            "updated_at": "2026-08-12T12:00:00Z",
            "description": "Test description | with bar",
        }
    ]
    table = render_table(items)
    assert "| # | Name | ⭐ | Lang | Updated | Description |" in table
    assert "[owner/repo-one](https://github.com/owner/repo-one)" in table
    assert "with bar" in table
    assert "42" in table


def test_load_previous_nonexistent(tmp_path, monkeypatch):
    test_data = tmp_path / "data" / "items.json"
    monkeypatch.setattr("tracker.DATA_FILE", test_data)
    assert load_previous() == []


def test_load_previous_invalid_json(tmp_path, monkeypatch):
    test_data = tmp_path / "data" / "items.json"
    test_data.parent.mkdir(parents=True, exist_ok=True)
    test_data.write_text("invalid json")
    monkeypatch.setattr("tracker.DATA_FILE", test_data)
    assert load_previous() == []


def test_load_previous_valid(tmp_path, monkeypatch):
    test_data = tmp_path / "data" / "items.json"
    test_data.parent.mkdir(parents=True, exist_ok=True)
    items = [{"id": "repo1", "stars": 10}]
    test_data.write_text(json.dumps(items))
    monkeypatch.setattr("tracker.DATA_FILE", test_data)
    assert load_previous() == items


def test_rewrite_readme(tmp_path, monkeypatch):
    readme = tmp_path / "README.md"
    content = (
        "# Header\n\n"
        "> ⏰ Last updated: old\n\n"
        "badge/Tracked_Items-0-brightgreen\n\n"
        "<!-- TRACKER_TABLE_START -->\nold table\n<!-- TRACKER_TABLE_END -->"
    )
    readme.write_text(content)
    monkeypatch.setattr("tracker.README_FILE", readme)

    items = [
        {
            "name": "user/skill",
            "url": "https://github.com/user/skill",
            "stars": 5,
            "language": "Python",
            "updated_at": "2026-08-12T10:00:00Z",
            "description": "Skill desc",
        }
    ]
    rewrite_readme(items)

    updated_text = readme.read_text()
    assert "user/skill" in updated_text
    assert "badge/Tracked_Items-1-brightgreen" in updated_text
    assert "Last updated:" in updated_text


@patch("tracker.httpx.get")
def test_fetch_items(mock_get):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {
        "items": [
            {
                "full_name": "user/claude-skill",
                "html_url": "https://github.com/user/claude-skill",
                "stargazers_count": 15,
                "language": "Python",
                "description": "A great skill",
                "pushed_at": "2026-08-12T15:00:00Z",
            }
        ]
    }
    mock_get.return_value = mock_resp

    items = fetch_items()
    assert len(items) == 1
    assert items[0]["id"] == "user/claude-skill"
    assert items[0]["stars"] == 15
