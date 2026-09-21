---
name: ats-resume-check
description: Scan a resume the way an ATS (Applicant Tracking System) parser and a resume-scoring tool like BigInterview/ResumeAI would, scoring it across four categories — Readability, Credibility, ATS Fit, and Format — and returning a color-coded (Needs Work / Almost There / Good Work) report with an action-item list. Use this whenever the user shares a resume and asks for ATS feedback, an "ATS score," a "resume scan," to "grill" or stress-test their resume, to check it against a job description, or to know why they aren't getting callbacks. Also trigger on requests like "would this pass an ATS", "score my resume", "check my resume format/readability/credibility", or "match my resume to this JD" — even if the user doesn't name a specific tool.
---

# ATS Resume Check

Mimics how an ATS-style resume scanner (the kind built into platforms like BigInterview/ResumeAI) grades a resume. It does NOT rewrite the resume for you first — it grades what's actually on the page, the way a bot or a rushed recruiter would, then tells the user exactly what to fix.

## Why this framework

Real ATS platforms don't judge a resume holistically — they run independent, mechanical checks across a few axes and flag anything that fails, without caring how good the underlying work is. A resume with genuinely impressive experience can still fail on section order or bullet count. Being blunt and mechanical here is the whole point: it's what "grilling" the resume actually means. Don't soften scores because the content is impressive — a strong engineer with a resume that skips a section header the parser expects should hear about it.

## What you need before scoring

1. **The resume itself** — as text, or a file to read (see the `docx`/`pdf` skills if it's a Word doc or PDF; this skill only handles the scoring, not extraction).
2. **A target job title and/or job description**, if the user wants ATS Fit scored. Without one, score the other three categories in full and tell the user ATS Fit needs a job description or target title to be meaningful — don't fabricate one.

If the user only pastes a resume with no JD, proceed with Readability, Credibility, and Format, and ask for the JD only if they want the ATS Fit category too — don't block the whole scan on it.

## The four categories

Score each category as one of: **Good Work** (passes cleanly), **Almost There** (passes but has real gaps), or **Needs Work** (fails one or more hard checks). A category is only "Good Work" if every sub-check in it passes — one failed sub-check caps the whole category at "Almost There" at best, two or more caps it at "Needs Work."

Full checklists for each category are in `references/` — read the relevant one before scoring that category, since the sub-checks are specific and easy to under-check from memory alone.

1. **Readability** — `references/readability.md`. Section presence, section ORDER (this is a hard parser requirement, not a style preference), spelling/grammar, contact info completeness.
2. **Credibility** — `references/credibility.md`. Bullet count per role (2–6), whether bullets lead with quantified impact, parallel structure/tense, whether claims read as generic vs. specific and verifiable.
3. **ATS Fit** — `references/ats-fit.md`. Job title match, keyword overlap against the JD, skills/competency/education/experience-level match. Run `scripts/keyword_match.py` for the keyword overlap — don't eyeball this one, it's meant to be computed, not guessed.
4. **Format** — `references/format.md`. Font choice/size, margins, line spacing, bullet style, date format consistency, overall length.

## Output structure

Report back in this shape — it mirrors what the real scanning tools show, which is what makes the feedback actionable rather than a vague "make it better":

```
## ATS Scan Results

### Readability — [Good Work / Almost There / Needs Work]
- [sub-check]: [pass/fail + one-line reason]
...

### Credibility — [status]
...

### ATS Fit — [status] (or "Skipped — no job description provided")
- Keyword match: X% (Y of Z top keywords)
- Matched: [...]
- Not matched: [...]
...

### Format — [status]
...

## Top 3 things to fix first
1. ...
2. ...
3. ...
```

Order the "top 3" by how much they'd move the needle with an actual ATS parser or recruiter — a missing section header or wrong section order beats a font-size nitpick almost every time, because parsers can silently drop content they can't classify.

## After the scan

Offer — don't push — to actually fix the top issues in the resume file itself. If the user says yes, edit the resume directly (respecting whatever file skill applies: `docx` for Word docs, plain markdown otherwise) rather than just describing the fix in prose.
