# trending-claude-skills

> Ranking de repos claude-skills e IA agente más trending, actualizado automáticamente cada 15 minutos

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · **Español** · [Português](./README_PT.md)

[![Stars](https://img.shields.io/github/stars/linny006/trending-claude-skills?style=for-the-badge&logo=github)](https://github.com/linny006/trending-claude-skills/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/trending-claude-skills?style=for-the-badge)](https://github.com/linny006/trending-claude-skills/commits)

---

Un tracker en vivo que consulta la GitHub Search API para encontrar repositorios de habilidades de agentes de IA creados y actualizados recientemente, los ordena por frescura y momentum (no por estrellas históricas) y publica un leaderboard en el README que se actualiza solo mediante GitHub Actions.

Esta lista se **actualiza automáticamente cada 15 minutos** con un cron de GitHub Actions. Cada commit refleja un cambio real en la fuente de datos: ítems nuevos añadidos, ítems expirados eliminados. Lo que ves es lo que hay.

---

Cada 15 minutos, un GitHub Action ejecuta `tracker.py`. Ese script:

1. Obtiene el estado más reciente desde la `GitHub Search API`.
2. Hace un diff contra `data/items.json` (el snapshot anterior).
3. Reescribe la tabla de arriba entre los marcadores `<!-- TRACKER_TABLE_* -->`.
4. Hace commit con `feat: +N added, -M removed (timestamp)` si hubo cambios.

Sin servicios externos. Sin APIs de pago. Solo una fuente de datos pública y un GitHub Action gratuito.

---

## 📋 Live data

Los datos en vivo están en el README en inglés

---

## 🔗 Related live trackers

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
