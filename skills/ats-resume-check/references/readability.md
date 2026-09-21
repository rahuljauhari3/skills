# Readability checks

An ATS parser reads a resume top-to-bottom and tries to classify each section by its header. If a section is missing, mislabeled, or out of the order the parser expects, it can misfile or drop that content entirely — the human reviewer never sees it. That's why "order" is a hard check here, not a style preference.

## 1. Sections present
Check for these, each as its own clearly labeled section:
- Contact Information (name, phone, email, and ideally a location and one professional link — LinkedIn/GitHub/portfolio)
- Education
- Experience (any of: Employment Experience, Professional Experience, Graduate Projects, Academic Projects, Selected Projects, Career History, Work History, Relevant Experience)
- Technical Skills or equivalent (Skills, Core Competencies, Technical Expertise, Software Proficiencies, IT Skills, Technical Capabilities, Technical Knowledge, Technical Abilities, Technology Skills)

Flag any of the four missing entirely.

## 2. Required order
The expected order is:
1. Contact Information
2. Education
3. Technical Skills (or equivalent)
4. Experience (or equivalent)

Anything after that (projects, certifications, publications) is fine in any order. Flag if Education comes after Experience, if Skills comes after Experience, or if Contact Information isn't first — these are the ones that trip up a parser's section classifier, not just a human reader's expectations.

## 3. Spelling & grammar
Flag actual misspellings, subject-verb agreement errors, and inconsistent capitalization of proper nouns (e.g., a tool name spelled two different ways). Don't flag stylistic choices (e.g., sentence fragments in bullets are standard resume style, not a grammar error).

## 4. Contact information completeness
Needs: full name, phone, email. Should have: location (city/state is enough — no need for a full address), and at least one professional link (LinkedIn, GitHub, portfolio). Flag if any of name/phone/email is missing; treat a missing link as a minor gap, not a hard fail.

## 5. Pronouns
Resumes should not contain personal pronouns (I, me, my) in bullet points — this is a resume-writing convention, not an ATS mechanic, but scanners check it and it reads as unpolished. Flag any bullet starting with "I" or containing "my."
