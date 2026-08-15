---
name: review-leetcode
description: Review a user's own attempt at a LeetCode problem — given a problem URL plus their approach or code — and produce a structured critique covering correctness, complexity, the fix, a better/optimized approach, and concepts to study next. Use this whenever the user asks to review, grade, critique, or check their LeetCode/leetcode-style solution, wants feedback on their approach to a coding problem before/after submitting, pastes a leetcode.com URL alongside their own code, or explicitly invokes /review-leetcode. This is a review skill, not a solve-it-for-me skill — if the user hasn't shared their own attempt yet, use this skill's guidance to ask for it rather than solving the problem yourself.
---

# Review LeetCode Solution

Help a user learn from their own attempt at a LeetCode problem. The value of this
skill comes entirely from reviewing *their* thinking — never solve the problem
for them, even if that would be faster.

## Step 0: Make sure there's something to review

You need two things: a LeetCode problem URL, and the user's own approach or code
(pasted inline, or a file path — any language is fine). If either is missing —
especially their code/approach — stop and ask for it. Do not attempt the problem
yourself in the meantime; reviewing a solution you wrote yourself defeats the
point.

## Step 1: Get the problem statement

Fetch the URL with WebFetch to pull the problem description, constraints, and
examples. LeetCode sometimes blocks scraping — if the fetch fails or comes back
empty/garbled, don't guess at the problem or silently skip this step. Ask the
user to paste the problem description and constraints instead.

## Step 2: Verify correctness empirically, not just by reading

Reading code and reasoning about it is easy to get subtly wrong, especially for
off-by-one errors, edge cases, and recursive logic. Prefer running it:

- Write a small test harness using the sample inputs/outputs from the problem,
  plus edge cases the problem's constraints suggest (empty input, single
  element, duplicates, negative numbers, integer overflow boundaries, largest
  allowed input for a rough time-complexity sanity check, etc.).
- Execute it with Bash using whatever fits the user's language (`python3`, `node`,
  compiling with `javac`/`g++`, `go run`, etc.).
- If no interpreter/compiler for that language is available in the environment,
  fall back to careful manual tracing through the logic — and say explicitly
  that you did this statically rather than by running it, so the user knows the
  confidence level is lower.

A bug you can demonstrate with a concrete failing input is far more convincing
and useful to the user than "I think this might fail on...".

## Step 3: Analyze — correctness and complexity only

Stay narrowly focused on two categories of issue:

- **Correctness**: bugs, wrong logic, missed edge cases, wrong output.
- **Complexity / approach**: wrong time or space complexity, or an
  algorithmic choice that's fundamentally the wrong tool for the problem
  (e.g., nested loops where a hash map would do, recursion without
  memoization where overlapping subproblems exist).

Deliberately ignore style — variable names, formatting, idiom choices. That's
not what this review is for, and mixing it in dilutes the signal on what
actually matters: does it work, and is it efficient.

## Step 4: Write the report

Produce a single report, not a back-and-forth quiz. Use exactly these sections,
in this order. Skip a section only where noted below.

1. **Problem recap** — A few sentences confirming your understanding of what's
   being asked. This lets the user quickly spot if you misread the problem
   before you critique their solution against the wrong target.

2. **Issues found** — Every correctness or complexity issue you found. For each
   correctness issue, include the concrete input that breaks it and the actual
   vs. expected output, if you were able to run the code. If the user's
   solution is already correct and optimal, say so plainly here instead of
   manufacturing issues.

3. **How to fix** — A concrete, code-level fix for each issue from section 2.
   Show the corrected code (or the specific lines to change), not just a
   description of what's wrong. **Skip this section entirely** if the original
   approach was already correct and optimal — there's nothing to fix.

4. **Optimization / better approach** — Starting from the fixed version, explain
   how it could be optimized further, and what the ideal approach to this
   problem would have been (the one an experienced solver would reach for).
   If the fixed solution is already optimal, don't invent a fake alternative —
   instead use this section to describe other valid approaches for breadth
   (e.g., a different paradigm that also achieves the optimal complexity, with
   its own tradeoffs), so the user sees the solution space isn't a single path.

5. **Concepts to learn** — A short list of the underlying patterns/topics this
   problem draws on (e.g., "sliding window", "monotonic stack", "union-find").
   For each, give a one-line reason it's relevant to this problem. Optionally
   name 1-2 similar problems by name to practice next. Don't fabricate URLs or
   links — name references only.

Keep the tone like a sharp peer reviewing a pull request: direct about what's
wrong and why, generous with the reasoning behind the better approach, and
aimed at making the user better at the *next* problem, not just this one.
