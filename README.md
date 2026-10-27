<!--
SEO: trending claude skills
-->

<div align="center">

# Trending Claude Skills

Auto-updated leaderboard of trending claude-skills and AI agent repos, refreshed every 15 minutes

[![Stars](https://img.shields.io/github/stars/linny006/trending-claude-skills?style=for-the-badge&logo=github)](https://github.com/linny006/trending-claude-skills/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/trending-claude-skills?style=for-the-badge)](https://github.com/linny006/trending-claude-skills/commits)
[![Items](https://img.shields.io/badge/Tracked_Items-11-brightgreen?style=for-the-badge)](#)
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

> ⏰ Last updated: 2026-10-27 10:00 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Description |
|---|------|---|------|---------|-------------|
| 1 | [ommakes/Skills](https://github.com/ommakes/Skills) | 21 | TypeScript | 2026-10-27 | Skills for product design |
| 2 | [ZiChenWang114514/chemdraw-skill](https://github.com/ZiChenWang114514/chemdraw-skill) | 30 | Python | 2026-10-27 | ChemDraw Skill · AI 绘制可编辑化学结构式 — Editable ChemDraw structures for Claude Code, Codex & any AI agent: draw molecules, reb |
| 3 | [JMAILLY/claude-migration-skills](https://github.com/JMAILLY/claude-migration-skills) | 0 | — | 2026-10-27 | Claude Code plugin: skills for migrating and modernizing Dockerized, Makefile-driven web projects — Drupal 10→11, PHP/Do |
| 4 | [haiderfarooq3/paper-reel](https://github.com/haiderfarooq3/paper-reel) | 25 | JavaScript | 2026-10-27 | Claude Code skill: faceless 9:16 explainer reels in a cut-paper style. Voice-timed scenes, word-by-word captions. Free,  |
| 5 | [Melvynx/ai-maxxing-skills](https://github.com/Melvynx/ai-maxxing-skills) | 19 | HTML | 2026-10-27 | Skills Claude Code pour créer ton SaaS personnel (Cloudflare, Convex, Lumail, Stripe) : grill-me, audit-safety et plus.  |
| 6 | [ahmedrzzaa/coroot-agent-skills](https://github.com/ahmedrzzaa/coroot-agent-skills) | 1 | — | 2026-10-27 | Agent skills for investigating production systems with Coroot MCP: incident RCA, logs, traces, PromQL analytics and SLOs |
| 7 | [the911fund/skill-of-skills](https://github.com/the911fund/skill-of-skills) | 79 | Python | 2026-10-27 | The quality-ranked discovery engine for AI coding skills, plugins and MCP servers across Claude Code, Codex, Cursor, Win |
| 8 | [sampil/triz-skill](https://github.com/sampil/triz-skill) | 0 | Python | 2026-10-27 | TRIZ (Theory of Inventive Problem Solving) Agent Skill for Claude: contradiction matrix, 40 principles, ARIZ — for engin |
| 9 | [OpenLatch/saferskills](https://github.com/OpenLatch/saferskills) | 8 | Python | 2026-10-27 | Every AI skill, independently scanned. Public, open-source trust scoring for skills, MCP servers, hooks, and plugins acr |
| 10 | [Adityaraj0421/dalal-street-skills](https://github.com/Adityaraj0421/dalal-street-skills) | 4 | Python | 2026-10-27 | Claude skills for NSE & BSE: scan, plan, replay 10,000x and size every Indian trade, with STT, circuit bands, the 3:15 c |
| 11 | [shhadi/keenstone](https://github.com/shhadi/keenstone) | 1 | HTML | 2026-10-27 | 10 experts. 100 rules. Only what they agree on. Distill turns any problem into a ranked, actionable plan for Claude, Cod |
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
