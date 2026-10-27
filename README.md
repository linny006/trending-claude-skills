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

> ⏰ Last updated: 2026-10-27 16:00 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Description |
|---|------|---|------|---------|-------------|
| 1 | [docsor1212/paper-rewriter](https://github.com/docsor1212/paper-rewriter) | 0 | Python | 2026-10-27 | paper-rewriter — Agent Skill (SKILL.md open format) |
| 2 | [JouberthAlves/off-template-skills](https://github.com/JouberthAlves/off-template-skills) | 1 | JavaScript | 2026-10-27 | Anti-AI-slop design skills for coding agents: a brief, real research and three directions before any code. |
| 3 | [linny006/trending-claude-skills](https://github.com/linny006/trending-claude-skills) | 133 | Python | 2026-10-27 | Auto-updated leaderboard of trending claude-skills and AI agent repos, refreshed every 15 minutes |
| 4 | [ohugonnot/claude-skills](https://github.com/ohugonnot/claude-skills) | 0 | Python | 2026-10-27 | Battle-tested Claude Code skills by Odilon Hugonnot: quality-gated feature delivery, senior review, issue/MR workflow, b |
| 5 | [sarojkjha/aaj-marketing-skills](https://github.com/sarojkjha/aaj-marketing-skills) | 1 | JavaScript | 2026-10-27 | The math layer for marketing agents: 73 skills, 62 with deterministic engines that return numbers and a verdict. Keep yo |
| 6 | [escoffier-labs/brigade](https://github.com/escoffier-labs/brigade) | 81 | Python | 2026-10-27 | Run coding agents anywhere and keep one record of the work, with tools and memory in sync across your harnesses. Local f |
| 7 | [IcyCreamDAS/shidi-skill](https://github.com/IcyCreamDAS/shidi-skill) | 14 | Python | 2026-10-27 | AI4S 科研 Agent 技能 \| AI-for-Science research workflow skill for coding agents: literature review · experiment design · fig |
| 8 | [CorvinLabs/CorvinOS](https://github.com/CorvinLabs/CorvinOS) | 22 | Python | 2026-10-27 | Self-hosted agentic OS — a Vibe-Engineering platform for Builders. Connect Claude Code Agent to Discord, Telegram, Whats |
| 9 | [jgoneit/jaekit](https://github.com/jgoneit/jaekit) | 0 | Python | 2026-10-27 | Spec turns requests into goal documents; Seal implements, verifies, and records completion. |
| 10 | [bonniegeng-max/video-digest](https://github.com/bonniegeng-max/video-digest) | 1 | Python | 2026-10-27 | video-digest 视频深读 · 把没时间看的 YouTube 视频提炼成中文结构化笔记：按主题成文、区分事实与观点、附原链接与时间戳可跳回。Turn long YouTube videos into structured Chine |
| 11 | [alejandroventaplay/ventaplay-wa-bridge](https://github.com/alejandroventaplay/ventaplay-wa-bridge) | 0 | TypeScript | 2026-10-27 | VentaPlay WA Bridge: tu WhatsApp conectado a Claude (MCP + skill), en tu computador. Respalda, filtra lo personal y llev |
| 12 | [zhuyansen/awesome-claude-seo-skills](https://github.com/zhuyansen/awesome-claude-seo-skills) | 10 | — | 2026-10-27 | Open-source Claude SEO skills, SEO MCP servers and GEO tools for coding agents. Each read and security-graded. EN + 中文. |
| 13 | [zhuyansen/awesome-claude-code-skills-collections](https://github.com/zhuyansen/awesome-claude-code-skills-collections) | 0 | — | 2026-10-27 | Collections of Claude Code skills: 781 repos that hold many skills, plugins or subagents. General collections, single-do |
| 14 | [surbhi-bhor/learnloop-skill](https://github.com/surbhi-bhor/learnloop-skill) | 0 | Python | 2026-10-27 | Turn what you learn in AI chats into Notion study notes, weak spots, practice and job-ready proof. Works with Claude, Co |
| 15 | [athola/claude-night-market](https://github.com/athola/claude-night-market) | 343 | Python | 2026-10-27 | 23 Claude Code plugins: TDD enforcement hooks, git/PR workflows, spec-driven development, code review, project lifecycle |
| 16 | [tylerwarner33/autodesk-claude-plugins](https://github.com/tylerwarner33/autodesk-claude-plugins) | 1 | Python | 2026-10-27 | Unofficial Claude plugin marketplace with skills for Autodesk development. Works in claude.ai, Claude Code, Claude Deskt |
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
