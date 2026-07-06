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

## License

MIT © Rahul Jauhari
