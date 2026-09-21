---
name: scout-oss
description: Scout for open-source contribution opportunities across vllm, vllm-metal, mlx, transformers, tensorflow, opencv, pandas, and numpy. Surfaces good-first/help-wanted issues, docs/example gaps, and bugs-with-repro — then clones, reproduces, and confirms a candidate fix locally BEFORE recommending you open a PR. Use when the user wants to find something worth contributing to upstream.
argument-hint: "[repo name(s) to focus on, or blank for all] [optional: topic/area]"
---

# scout-oss

Find contribution opportunities worth your time, and **prove they're real and fixable before recommending a PR**. The user takes OSS contributions seriously: never recommend opening a PR for something that isn't verified, isn't still open, or is already claimed.

## Target repositories

| Key | Repo |
|-----|------|
| vllm | `vllm-project/vllm` |
| vllm-metal | `vllm-project/vllm-metal` (verify exact slug; may be a fork/branch effort) |
| mlx | `ml-explore/mlx` |
| transformers | `huggingface/transformers` |
| tensorflow | `tensorflow/tensorflow` |
| opencv | `opencv/opencv` |
| pandas | `pandas-dev/pandas` |
| numpy | `numpy/numpy` |

If `$ARGUMENTS` names specific repos, scope to those. Otherwise sweep all. If a topic/area is given (e.g. "quantization", "dataframe groupby"), bias issue search toward it.

## What counts as an opportunity

Only these three categories (the user chose them):
1. **Good-first / help-wanted issues** — maintainer-labeled, open for contributors.
2. **Docs & examples** — doc gaps, broken/outdated examples, incorrect docstrings. Low-risk, high-acceptance.
3. **Bugs with a clear repro** — open bug reports with reproduction steps but no merged fix.

Explicitly skip: feature requests requiring design buy-in, anything labeled `wontfix`/`stale`/`needs-design`, issues with an open linked PR, and issues assigned to someone else.

## Procedure

### Phase 1 — Discover (read-only, fast)
For each in-scope repo, use the GitHub API via `gh` (preferred) or WebFetch:

- `gh issue list -R <repo> --label "good first issue" --state open --limit 30`
- also try labels: `help wanted`, `good-first-issue`, `documentation`, `docs`, `Easy`, `contributions welcome` (label names vary per repo — list labels first with `gh label list -R <repo>` if unsure).
- For bugs: `--label bug` plus a body containing repro steps / a code block.

Collect candidates with: title, number, URL, labels, age, comment count, whether anyone is assigned, and whether a linked PR exists (`gh issue view <n> -R <repo> --json assignees,linkedBranches` and scan comments/timeline for "PR" links).

### Phase 2 — Filter & rank (no cloning yet)
Drop anything assigned, with an open PR, stale (no activity >12 months unless maintainer reaffirmed), or requiring design approval. Rank survivors by acceptance likelihood:
- Maintainer explicitly invited contributions / labeled good-first → high
- Clear scope, clear repro, recent activity → high
- Touches well-tested module → higher (easier to verify)
- Large surface area, ambiguous requirements → low

Present the **ranked shortlist** to the user and ask which to verify deeply (verification is expensive — don't clone all of them). Show ~5–10 candidates max with one-line rationale each.

### Phase 3 — Verify locally (the gate — this is the whole point)
For each candidate the user picks, do a **full clone-reproduce-confirm** pass in a scratch dir (e.g. under the OS temp dir, NOT the working directory):

1. **Clone** the repo (shallow is fine: `git clone --depth 50`), check out the default branch, and confirm the issue is reproducible against current `main` — if it's already fixed on main, report that and drop it.
2. **Set up** the minimal dev environment (use a venv / the repo's documented dev install; for C++/CUDA repos like tensorflow/opencv/vllm where a full build is impractical locally, say so explicitly and fall back to the strongest verification you *can* do — static analysis, reading the failing code path, running the specific affected unit test if buildable). Never pretend you built something you didn't.
3. **Reproduce** the bug / confirm the doc is wrong / confirm the example is broken. Capture the exact command and output as evidence.
4. **Draft a candidate fix** locally and confirm it: the repro now passes, and the repo's relevant tests/lint still pass (`pytest <affected tests>`, doctest, etc.). For docs, render/verify the corrected snippet actually runs.
5. **Re-check it's still unclaimed** right before recommending (issues move fast): re-query assignees + linked PRs.

### Phase 4 — Report
For each verified opportunity produce a short dossier:
- Issue link, repo, category, labels
- **Verification evidence**: env used, repro command + output, what the fix changes, test/lint results (or an honest statement of why full local build wasn't possible)
- Suggested PR scope + a draft of what the PR description would say
- A confidence level: "verified & ready", "verified but needs maintainer sign-off on approach", or "could not fully verify locally — do NOT PR yet"

**Do not open any PR.** Stop at the dossier. The user decides whether to proceed.

## Rules
- Honesty over output: if nothing passes the gate, say "no verified opportunities" — that's a valid, good result.
- Never recommend a PR you haven't reproduced and confirmed fixable, per the user's standard.
- Keep scratch clones out of the user's own project directories; clone into a temp dir and clean up when done.
- Prefer `gh` CLI; if not authenticated, tell the user to run `! gh auth login` and fall back to WebFetch on github.com for read-only discovery.
