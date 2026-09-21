# ATS Fit checks

This is the category that actually requires a target — a job title and ideally a full job description (JD). Without a JD, don't fake this category; tell the user it's skipped and explain what you'd need.

## 1. Job title match
Compare the resume's most recent/current title (or a stated target title) against the JD's title. An exact or near-exact match (e.g., "Software Development Engineer" vs. "Software Engineer") passes; a distant match (e.g., "Data Analyst" resume against a "Machine Learning Engineer" JD) flags — not as a defect in the resume, but as a heads-up that the framing may need adjusting for this specific application.

## 2. Keyword matching — use the script, don't eyeball it
Run `scripts/keyword_match.py` with the resume text and JD text. It extracts the JD's significant terms (tools, frameworks, methodologies, nouns that aren't common English filler) and reports:
- Percentage of top JD keywords present in the resume
- List of matched keywords
- List of top keywords NOT found in the resume

A rough target: 50%+ of the JD's top keywords should appear somewhere in the resume (not necessarily verbatim in the same phrasing, but the core term). Below 50% is "Needs Work" for this sub-check; 50-70% is "Almost There"; above 70% is solid.

Report the not-matched list to the user honestly — but don't tell them to keyword-stuff bullets with terms that aren't true of their actual experience. If a keyword is legitimately missing from their background, say so rather than suggesting they add it anyway.

## 3. Skills / competency / education / experience-level match
- **Skills match**: does the resume's skills section cover the JD's required technical skills?
- **Competency match**: do the resume's demonstrated competencies (from bullet content, not just the skills list) align with what the JD emphasizes?
- **Education match**: does the resume's degree/field meet the JD's stated requirement (or exceed it)?
- **Experience level match**: does the years-of-experience or seniority implied by the resume match what the JD is asking for (e.g., don't flag a new grad's resume against an entry-level JD, but do flag a 10-year-experience resume framed for a senior JD if the resume undersells seniority, or a 1-year resume against a "5+ years required" JD)?

Each of these four is a single pass/fail judgment call based on reading both documents — there's no script for these, unlike the keyword count.
