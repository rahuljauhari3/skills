---
name: tailor-resume
description: Tailor a resume to a specific job description using a persistent, grounded record of the user's actual experience (an "experience bank"), producing a gap-analysis report and, on approval, a tailored one-page LaTeX resume plus compiled PDF. Use this whenever the user pastes or screenshots a job posting and wants help tailoring their resume, asks which resume bullets/sections to update for a specific role, wants to know what's missing from their resume for a job, or explicitly invokes /tailor-resume. Also use it the first time the user wants to set up their experience bank from a master resume or "everything I've ever done" document. This is a rewording/reordering/gap-surfacing skill grounded in the user's own real experience — it never invents work history, skills, or metrics that aren't grounded in something the user actually did.
---

# Tailor resume

Help the user tailor their resume to a specific job posting, without ever
inventing experience they don't have. The skill has two modes depending on
whether an `experience-bank.md` already exists at their configured path.

## Configuration

`<bank-dir>` is the folder holding everything this skill reads and writes.
Resolve it in this order, and do not ask the user if an earlier step succeeds:

1. Read `~/.claude/resume-bank-path.txt`. If it exists, its first line is
   `<bank-dir>`.
2. Otherwise, if the path is recorded in memory or earlier in the
   conversation, use that and write it to the file above for next time.
3. Otherwise, ask the user once, then write it to that file.

Keeping the path in a local file rather than in this skill is deliberate: the
skill is shareable and version controlled, the path is personal.

**Before doing anything else, read whichever of these exist:**

1. `<bank-dir>/resume-tailoring-instructions.md` — the user's standing rules on
   tone, layout, honesty guardrails, and output format. These override the
   generic guidance in this skill wherever they conflict.
2. `<bank-dir>/experience-bank.md` — the full record.
3. `<bank-dir>/bullet-pool.md` — the same material already rewritten as
   jargon-free STAR/XYZ bullets, tagged by theme. Draft from this pool first
   and fall back to the raw bank only when the pool has no bullet for a
   JD requirement.

Also check `<bank-dir>/applications/` for the most recent application folder:
its `.tex` is the starting template for the new one, and its gap-analysis
report shows what was asked and answered last time.

If `resume-tailoring-instructions.md` exists, it is the user's own standing
brief and it wins over anything generic in this skill. Do not re-ask for
preferences it already answers.

**The bank is a floor, not a ceiling.** It's an amalgamation of whatever the
user could remember or had written down at the time it was built or last
updated — not an exhaustive, audited record of everything they've ever done.
Treat "not in the bank" as "not yet captured," not as "didn't happen." This
assumption shapes both modes below: Mode A should keep growing the bank
opportunistically, and Mode B should surface suspected gaps generously rather
than only when very confident.

## Mode A: bootstrap or update the bank

Trigger this mode when `experience-bank.md` doesn't exist yet, or when the
user attaches a new/updated resume document on a run (even if the bank
already exists).

1. Read the attached document (.docx — use the `docx` skill to extract
   content if it's not already plain text).
2. Normalize it into `experience-bank.md` as **plain structured prose**
   mirroring whatever sections the source actually has (Education, Work
   Experience, Projects, Research Publications, Technical Skills, or whatever
   else is there — don't force a fixed section list). No tagging or metadata
   scheme: keep it as prose the model can read and reason about at match time,
   not a rigid schema that will go stale.
3. If `experience-bank.md` already exists, **merge and append** — add new
   entries, dedupe against what's already there, but never delete or
   overwrite an existing entry. The bank only ever grows. Point of comparison
   for dedup is meaning, not exact string match (a reworded version of an
   existing bullet is a duplicate, not a new entry).
4. Confirm to the user what was added/merged before moving on. If the user
   only wanted to update the bank (no job description given this run), stop
   here.

If there's no source document to build from and no bank exists, ask the user
to attach one — don't proceed to Mode B on a bank you'd have to invent.

## Mode B: tailor for a specific job application

Trigger this whenever the user provides a job description (pasted text or a
screenshot — read screenshots directly, don't transcribe them first as a
separate step) and the bank already exists.

### 1. Build the alignment map first — it drives everything else

Alignment to this specific JD is the first and foremost goal of this skill.
Before drafting anything, extract a checklist of every requirement,
responsibility, technology, and theme the JD names — this checklist, in the
JD's own language, is the target you're aligning to. Extract the company name
and role title while you're at it, for later file naming.

Only after the checklist exists, read the full `experience-bank.md` and mark
each checklist item as one of:

- **Covered** — a bank entry speaks to it directly.
- **Partially covered** — a bank entry is related but doesn't use the JD's
  language or doesn't emphasize the angle the JD cares about.
- **Not covered** — nothing in the bank speaks to it (a candidate for step 3).

Everything downstream (rewording, reordering, gap-surfacing) is organized
around this map, not the other way around — don't start from the resume's
existing structure and tweak it; start from what the JD is asking for.

### 2. Draft the report

Organize the report by resume section, but every suggestion in it should
trace back to a specific line on the alignment map:

- **Reword/re-emphasize**: for each "partially covered" item, don't just
  describe the direction ("emphasize the leadership angle") — actually draft
  1-2 candidate rewritten phrasings that pull in the JD's own terminology,
  grounded only in what the bank entry actually says. Brainstorm freely on
  phrasing; never brainstorm on substance the bank doesn't support.
- **Suggested new sections**, but only if the bank already contains enough
  real content to justify one (e.g. the bank mentions a certification in
  passing but there's no Certifications section yet). Never propose an empty
  section header with nothing to put in it — that's noise, not signal.
- **Reordering**: which bullets should move to the top within a section, and
  whether whole sections should be reordered (e.g. Projects before Education
  if the JD is project-heavy), driven by how many "covered" checklist items
  cluster in each section. Order is a free signal for a reviewer skimming in
  a few seconds — don't leave it as an afterthought.

By default every entry already in the bank goes into the tailored resume —
this skill reorders and rewords for relevance, it does not cut or omit for
length. The exception is a standing page limit in the user's own
`resume-tailoring-instructions.md`: if they have one, honor it, select the
strongest entries for this JD, and say in the report what you left out and
why. Absent such a rule, treat trimming as a separate explicit request.

### 3. Surface gaps, don't fabricate them

Every "not covered" checklist item is a suspected gap. Because the bank is
known to be incomplete (see above), lean toward surfacing these generously —
if the JD implies experience a person in adjacent roles plausibly has, ask
about it rather than silently dropping it for lack of confidence. Do not
silently invent a bullet for it, and don't silently ignore it either — that's
real signal the user should see. Phrase each as a direct, specific question
("the JD asks for X — is that something you've done that just isn't in the
bank yet?") and collect them as a **"suspected gaps"** list at the end of the
report, all together in one batch, so the user can confirm or reject them in
one pass rather than being interrupted mid-analysis for each one.

### 4. Save the report and JD

Determine the output folder: `<bank-dir>/applications/<company>-<role>/`. If
that folder already exists (a prior run for the same company + role), version
it instead of overwriting — `<company>-<role>-v2`, `-v3`, etc. Never touch a
previous attempt's folder.

Inside it, save:
- The job description itself (the pasted text, or a note of the screenshot
  source) — so the reasoning in the report can be reconstructed later even
  after the posting is taken down.
- The gap-analysis report as markdown.

Present the report to the user and stop here. Do not generate the resume yet.

### 5. On approval, generate the tailored resume

Once the user reviews the report and approves it (and tells you which
suspected gaps, if any, are real):

- Produce the tailored resume as **LaTeX** in the same application subfolder,
  applying the approved rewording, reordering, and any confirmed gap bullets.
  Copy the most recent application's `.tex` as the starting template. Then
  compile it with `pdflatex` and **look at the rendered page** before showing
  it to the user: confirm it is one page, that it fills the page rather than
  stopping short, and that no bullet ends in a two word orphan line. Iterate on
  spacing until all three hold. Never modify the user's master resume file or
  `experience-bank.md` as a side effect of generating this file.
- Add any confirmed gap bullets to `experience-bank.md` as well (merge/append,
  same rule as Mode A) — a confirmed gap is real experience the user has, so
  future applications should benefit from it too, not just this one.
