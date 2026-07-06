# Rahul's Agent Skills

A collection of [agent skills](https://skills.sh) for Claude Code and other AI coding agents.

## Skills

| Skill | What it does |
|---|---|
| [`pick-model`](./skills/pick-model) | Decide which Claude model (Opus / Sonnet / Haiku) fits a task and how to route it (session, subagent, or workflow) for the best cost/quality tradeoff. |

## Install

Install any skill straight from this repo — no registry account needed:

```bash
# a single skill, globally (user-level)
npx skills add rahuljauhari3/skills@pick-model -g

# or all skills in this repo
npx skills add rahuljauhari3/skills --all
```

Then use it in Claude Code with `/pick-model` (or let the agent invoke it automatically).

## Guides

- [Track Claude Code usage with ccusage](./docs/ccusage-statusline.md) — set up a status line that shows session cost, daily total, and the rolling 5-hour reset countdown.
- [Auto-update Claude Code tooling on launch](./docs/cc-auto-update.md) — a `cc` shell wrapper that keeps Claude Code, ccusage, and skills current (throttled to once/day).

## License

MIT © Rahul Jauhari
