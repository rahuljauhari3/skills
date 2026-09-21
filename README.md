# Rahul's Agent Skills

A collection of [agent skills](https://skills.sh) for Claude Code and other AI coding agents.

## Skills

| Skill | What it does |
|---|---|
| [`pick-model`](./skills/pick-model) | Decide which Claude model (Opus / Sonnet / Haiku) fits a task and how to route it (session, subagent, or workflow) for the best cost/quality tradeoff. |
| [`review-leetcode`](./skills/review-leetcode) | Review your own LeetCode attempt (problem URL + your code) — finds correctness/complexity issues, shows the fix, suggests the optimal approach, and lists concepts to study. |
| [`humanizer`](./skills/humanizer) | Rewrite AI-sounding text so it reads naturally without changing what it says. From [blader/humanizer](https://github.com/blader/humanizer). |
| [`tailor-resume`](./skills/tailor-resume) | Tailor a resume to a job description from a persistent "experience bank" of what you've actually done — gap analysis first, then a one-page LaTeX resume. Never invents experience. |

## Install

Install any skill straight from this repo — no registry account needed:

```bash
# a single skill, globally (user-level)
npx skills add rahuljauhari3/skills@pick-model -g

# or all skills in this repo
npx skills add rahuljauhari3/skills --all
```

Then use it in Claude Code with `/pick-model` (or let the agent invoke it automatically).

### Configuring `tailor-resume`

This one needs to know where your experience bank lives. Point it at a folder:

```bash
echo "/path/to/your/resume-folder" > ~/.claude/resume-bank-path.txt
```

The skill reads `experience-bank.md`, `bullet-pool.md`, and (optionally)
`resume-tailoring-instructions.md` from that folder, and writes each
application into `applications/<company>-<role>/`. If the file doesn't exist,
the skill asks once and creates it. The path stays local so it never ends up
in this repo.

## Guides

- [Track Claude Code usage with ccusage](./docs/ccusage-statusline.md) — set up a status line that shows session cost, daily total, and the rolling 5-hour reset countdown.
- [Auto-update Claude Code tooling on launch](./docs/cc-auto-update.md) — a `cc` shell wrapper that keeps Claude Code, ccusage, and skills current (throttled to once/day).

## License

MIT © Rahul Jauhari
