<!--
SEO: trending claude skills
-->

<div align="center">

# Trending Claude Skills

Auto-updated leaderboard of trending claude-skills and AI agent repos, refreshed every 15 minutes

[![Stars](https://img.shields.io/github/stars/linny006/trending-claude-skills?style=for-the-badge&logo=github)](https://github.com/linny006/trending-claude-skills/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/trending-claude-skills?style=for-the-badge)](https://github.com/linny006/trending-claude-skills/commits)
[![Items](https://img.shields.io/badge/Tracked_Items-16-brightgreen?style=for-the-badge)](#)
[![Updated](https://img.shields.io/badge/Updates-every_15min-blue?style=for-the-badge)](#)

**⭐ Star this repo to bookmark — fresh data every 15 minutes**

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

</div>

---

## 💡 What is this?

A live tracker that queries GitHub Search API for recently created and updated AI coding-agent skill repositories, ranks them by freshness and momentum rather than all-time stars, and publishes a self-updating README leaderboard via GitHub Actions.

This list is **auto-updated every 15 minutes** by a GitHub Actions cron.
Each commit reflects a real change in the upstream data source — new items added,
expired items removed — so you can rely on what you see being current.

---

## 📋 Current Items

> ⏰ Last updated: 2026-10-27 12:00 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Description |
|---|------|---|------|---------|-------------|
| 1 | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | 966 | JavaScript | 2026-10-27 | An AI skill that turns books into animated, narrated, interactive web experiences |
| 2 | [AgamiAI/agami-core](https://github.com/AgamiAI/agami-core) | 29 | Python | 2026-10-27 | The trust layer between AI and your data. Turns your database schema - messy joins, undocumented tables,  into a governe |
| 3 | [rudderlabs/rudder-agent-skills](https://github.com/rudderlabs/rudder-agent-skills) | 19 | Python | 2026-10-27 | Claude Code plugin marketplace & agent skills for RudderStack — instrument events, design tracking plans & data graphs,  |
| 4 | [Jenesyx/arta-edit-studio](https://github.com/Jenesyx/arta-edit-studio) | 0 | Python | 2026-10-27 | Claude Code skills that turn talking-head videos into animated Instagram Reels — Farsi-first, no subtitles. \| ادیت ریلز  |
| 5 | [qadeer-ux/oh-my-codex-remix](https://github.com/qadeer-ux/oh-my-codex-remix) | 0 | HTML | 2026-10-27 | 🧠 Ultimate AI Coding Agent 2026: Supercharge Your Dev Workflow for Faster, Cleaner Code |
| 6 | [yanmeng0113-ctrl/eddyy-skill-orchestrator](https://github.com/yanmeng0113-ctrl/eddyy-skill-orchestrator) | 1 | Python | 2026-10-27 | Tiered orchestrator for chaining AI Skills & MCP tools: route card, locked anchors, cost/risk gates. 技能与MCP总控调度 |
| 7 | [yulmucoffee/artiboard](https://github.com/yulmucoffee/artiboard) | 19 | JavaScript | 2026-10-27 | A shared task board for people and their Claude agents, built as one claude.ai artifact. Views drawn by code, not tokens |
| 8 | [Mahashwetha/Job-search-email-system-claude](https://github.com/Mahashwetha/Job-search-email-system-claude) | 10 | Python | 2026-10-27 |   Automated daily job search pipeline — aggregates company tracking, sends styled HTML email digests, tailors resumes wi |
| 9 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 5316 | Python | 2026-10-27 | A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-repo |
| 10 | [exasol-labs/exasol-agent-skills](https://github.com/exasol-labs/exasol-agent-skills) | 10 | Shell | 2026-10-27 | Exasol skills for AI agents. Optimized for Claude Code and OpenAI Codex 🤖 |
| 11 | [Focus688/agent-security-skills](https://github.com/Focus688/agent-security-skills) | 1 | — | 2026-10-27 | 🛡️ Operational security skills for AI agent runtimes — safe installs, silent-failure detection, rollback. War-story driv |
| 12 | [nerdkim/im-a-korean-ai-in-seoul](https://github.com/nerdkim/im-a-korean-ai-in-seoul) | 0 | JavaScript | 2026-10-27 | Claude Code에서 Claude가 처음부터 한국어로 생각해 자연스러운 한국어를 쓰도록 한국어 작성 skill과 문체 검사 hook을 설치합니다. |
| 13 | [tonydzi/second-brain-starter-kit](https://github.com/tonydzi/second-brain-starter-kit) | 12 | Python | 2026-10-27 | A second brain for Claude Code and Codex that keeps receipts: skills as a plugin marketplace, opt-in persistent memory o |
| 14 | [lijishuang/skill-forge](https://github.com/lijishuang/skill-forge) | 1 | HTML | 2026-10-27 | Turn any SKILL.md into a working browser tool — generate adaptive UI and run skills with any OpenAI-compatible LLM. Chro |
| 15 | [adityash8/growth-skills](https://github.com/adityash8/growth-skills) | 0 | Python | 2026-10-27 | Evidence-first Agent Skills that connect growth strategy to verified execution. |
| 16 | [scrapall/scrapall-agent-skills](https://github.com/scrapall/scrapall-agent-skills) | 1 | — | 2026-10-27 | Scrapall agent skills: public social data from TikTok, Instagram, YouTube, Facebook, Reddit, X and more for Claude Code, |
<!-- TRACKER_TABLE_END -->

---

## 🔍 How it works

Every 15 minutes, a GitHub Action runs `tracker.py`. That script:

1. Fetches the latest state from `GitHub Search API`.
2. Diffs against `data/items.json` (the previous snapshot).
3. Rewrites the table above between the `<!-- TRACKER_TABLE_* -->` markers.
4. Commits `feat: +N added, -M removed (timestamp)` if anything changed.

No external services. No paid APIs. Just a public data source and a free GitHub Action.

---

## 🤝 Contributing

See `CONTRIBUTING.md` — usually you don't need to: the tracker keeps itself current.
If you spot a data-source bug or want to suggest a new column for the table, open
an issue.

---

## 🔗 Related live trackers

If you find this useful, you might also like these other auto-updated
trackers from the same maintainer — same mechanism, different upstream:

- [mcp-servers-live](https://github.com/linny006/mcp-servers-live) — Live index of newest MCP servers (`topic:mcp-server`)
- [cursor-rules-live](https://github.com/linny006/cursor-rules-live) — Newest Cursor rules and .cursorrules patterns (`topic:cursor-rules`)
- [claude-code-plugin-tracker](https://github.com/linny006/claude-code-plugin-tracker) — Claude Code plugins and hook configs (`topic:claude-code`)
- [llm-agents-radar](https://github.com/linny006/llm-agents-radar) — Newest LLM agent frameworks (`topic:llm-agent`)
- [rag-radar](https://github.com/linny006/rag-radar) — Newest RAG implementations and tools (`topic:rag`)
- [llm-eval-tracker](https://github.com/linny006/llm-eval-tracker) — Newest LLM evaluation tools and benchmarks (`topic:llm-eval`)
- [agent-framework-radar](https://github.com/linny006/agent-framework-radar) — Newest agent frameworks shipping on GitHub (`topic:agent-framework`)
- [vector-db-live](https://github.com/linny006/vector-db-live) — Newest vector DB projects and integrations (`topic:vector-database`)
- [llmops-radar](https://github.com/linny006/llmops-radar) — Newest LLMOps tooling (observability, deployment) (`topic:llmops`)
- [prompt-tools-live](https://github.com/linny006/prompt-tools-live) — Newest prompt-engineering tools and prompt repos (`topic:prompt-engineering`)
- [agent-eval-harness](https://github.com/linny006/agent-eval-harness) — Live benchmark of AI coding agents (`topic:llm-eval`)
- [skills-tracker](https://github.com/linny006/skills-tracker) — Tracking new GitHub 'skills' repos (`topic:agent-skills`)
- [awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) — Curated auto-updated awesome-list of AI agent skills (`topic:agent-skills`)

---

## 📜 License

MIT — see `LICENSE`.
