---
name: pick-model
description: Decide which Claude model to use for a given coding task and how to route it (main session, /model, subagent, or workflow). Use when the user asks "which model should I use", wants to optimize cost vs. quality, or is about to kick off a task and hasn't specified a model.
---

# Pick Model

Help the user (or yourself) choose the right Claude model for a task, then route it the cheapest way that still hits the quality bar.

## Current models (2026)

| Model | ID | Best for | Relative cost |
|---|---|---|---|
| **Opus 4.8** | `claude-opus-4-8` | Hardest reasoning, architecture, tricky debugging, long-horizon agentic work, ambiguous specs | $$$ |
| **Sonnet 4.6** | `claude-sonnet-4-6` | Default workhorse: most coding, refactors, reviews, multi-file edits | $$ |
| **Haiku 4.5** | `claude-haiku-4-5-20251001` | High-volume, mechanical, well-specified: formatting, simple edits, grep/summarize, cheap parallel fan-out | $ |
| **Fable 5** | `claude-fable-5` | Latest-gen alternative when explicitly requested | varies |

When building AI *apps*, default to the latest, most capable models. This skill is about which model runs *your Claude Code work*.

## Decision table

Match the task to the lowest tier that clears the bar:

- **Reach for Opus** when: the problem is under-specified and needs judgment; a subtle bug resists first attempts; you're designing architecture or a migration plan; the task spans many steps where one wrong turn compounds; correctness matters more than speed/cost.
- **Default to Sonnet** when: it's normal coding — implement a feature, refactor, write tests, review a diff, edit across a few files. This is the right answer most of the time.
- **Drop to Haiku** when: the task is mechanical and fully specified — rename symbols, reformat, extract strings, summarize a file, first-pass search. Also ideal as the per-item worker in a large parallel fan-out.

Tie-breakers:
- Uncertain between two tiers → pick the higher one for a *one-shot* task, the lower one for anything you'll *repeat many times* (cost multiplies).
- Verification/adversarial-review steps → keep them on Sonnet or Opus even if the work being checked ran on Haiku.

## How to route it

1. **Whole session** — user wants everything on one model: tell them to run `/model` (or `/fast` for Opus with faster output on Opus 4.8/4.7/4.6).
2. **One-off delegated task** — spawn a subagent with `Agent(..., model: "opus"|"sonnet"|"haiku")`. Keep expensive tiers scoped to the hard part.
3. **Fan-out over many items** — use a Workflow: run cheap per-item stages on Haiku (`agent(..., {model: 'haiku'})`) and reserve Opus/Sonnet for synthesis or verification stages. Omit `model` to inherit the session model — usually correct.

Guidance for `effort`/thinking: raise reasoning effort on the hardest verify/design stages; keep it low for mechanical stages regardless of model.

## Output

When asked "which model," give a one-line recommendation + the routing command — not a survey. Example:

> Refactor across 5 files → **Sonnet** (`/model` to sonnet, or a subagent). Save Opus for the auth-flow redesign that's genuinely ambiguous.
