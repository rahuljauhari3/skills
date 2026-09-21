#!/usr/bin/env python3
"""
keyword_match.py — compute JD-vs-resume keyword overlap, the way an ATS
keyword-matching pass does it.

Usage:
    python3 keyword_match.py --resume resume.txt --jd jd.txt [--top-n 40]

Or import and call `keyword_match(resume_text, jd_text, top_n=40)` directly
from another script — useful when the resume/JD text is already in memory
rather than in files.

This is a heuristic, not a semantic matcher: it extracts noun-ish / technical
terms from the JD (skipping common English stopwords), then checks which of
those terms show up anywhere in the resume text (case-insensitive substring
match, so "Kubernetes" matches "kubernetes" and "K8s" would NOT match
"Kubernetes" — different tokens are treated as different keywords on purpose,
since that's closer to how a real keyword scanner behaves).
"""

import argparse
import re
import sys
from collections import Counter

STOPWORDS = set("""
a an the and or but if then else for of to in on at by with without from
into onto over under again further once here there when where why how all
any both each few more most other some such no nor not only own same so
than too very s t can will just don should now is are was were be been
being have has had do does did having this that these those i you he she
it we they what which who whom as about above after before between
during through above below up down out off between during
you're you'll i'm we're they're it's don't doesn't isn't aren't
years experience preferred required strong excellent ability able
work team teams role position candidate candidates responsibilities
requirements qualifications plus join us our we're looking company
including etc using use used across various new build building
need needs needed experienced background strong solid deep proven
""".split())

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9+./#-]{1,}")


def extract_keywords(jd_text, top_n=40):
    tokens = TOKEN_RE.findall(jd_text)
    # Keep original casing for known acronyms/tech terms, but count case-insensitively
    counts = Counter()
    display = {}
    for tok in tokens:
        low = tok.lower()
        if low in STOPWORDS or len(low) < 2:
            continue
        if low.isdigit():
            continue
        counts[low] += 1
        # prefer a display form that looks "technical" (has a digit, uppercase, or symbol)
        if low not in display or any(c.isupper() or c.isdigit() for c in tok):
            display[low] = tok
    ranked = counts.most_common(top_n)
    return [display[low] for low, _ in ranked]


def keyword_match(resume_text, jd_text, top_n=40):
    keywords = extract_keywords(jd_text, top_n=top_n)
    resume_low = resume_text.lower()
    matched, not_matched = [], []
    for kw in keywords:
        if kw.lower() in resume_low:
            matched.append(kw)
        else:
            not_matched.append(kw)
    pct = round(100 * len(matched) / len(keywords), 1) if keywords else 0.0
    return {
        "top_keywords_considered": len(keywords),
        "matched": matched,
        "not_matched": not_matched,
        "match_percent": pct,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--resume", required=True, help="Path to resume text file")
    ap.add_argument("--jd", required=True, help="Path to job description text file")
    ap.add_argument("--top-n", type=int, default=40, help="How many top JD keywords to consider")
    args = ap.parse_args()

    with open(args.resume, "r", encoding="utf-8", errors="ignore") as f:
        resume_text = f.read()
    with open(args.jd, "r", encoding="utf-8", errors="ignore") as f:
        jd_text = f.read()

    result = keyword_match(resume_text, jd_text, top_n=args.top_n)

    print(f"Keyword match: {result['match_percent']}% "
          f"({len(result['matched'])} of {result['top_keywords_considered']} top JD keywords)\n")
    print("Matched:")
    for k in result["matched"]:
        print(f"  - {k}")
    print("\nNot matched:")
    for k in result["not_matched"]:
        print(f"  - {k}")


if __name__ == "__main__":
    sys.exit(main())
