# Review State

Last updated: 2026-04-16 10:02 MDT (Run 20)

## Completed

- Run 17 (2026-04-15): Major fixes — Vancouver renumbering of 31 references, n=21 denominator disclosure, supplementary citations S4–S6, 9th limitation added.
- Runs 18–19 (2026-04-15): Claimed "stable" but dash guardrail and line-numbering guardrail were never actually checked against docx XML.
- **Run 20 (2026-04-16)**: Dash elimination (78 occurrences → 0) and continuous line numbering added.
  - `generate_manuscript.py`: all 34 en + 44 em dashes replaced contextually.
  - Line numbering: `<w:lnNumType countBy=1 start=1 distance=360 restart=continuous/>` on main section sectPr only.
  - `manuscript.docx` regenerated; `word/*.xml` grepped for U+2013/U+2014 — zero confirmed.
  - XML well-formed (`xmllint --noout`).
  - LibreOffice PDF conversion succeeded; extracted text also has zero dashes.
  - Abstract 297/300 words; main text 4,792/5,000 words.

## In progress

None for this cycle.

## Open issues requiring attention

### Pending human action
1. Fill in corresponding author email (`generate_manuscript.py:504` placeholder `[corresponding author email]`).
2. Register protocol on OSF.
3. Verify grey-literature URLs (references 3, 6, 8, 13, 14, 28, 30, 31).
4. Prepare supplementary files S1–S6 for submission.
5. Update PRISMA-ScR checklist (S1) statuses to "Reported."
6. Decide whether to move Table 4 (Indigenous detail) and Figures 3–8 to supplementary.
7. Final print-format review of manuscript.docx in Word (LibreOffice rendering showed line numbers on title page; in Word this should respect sectPr #1 having no `lnNumType`. Spot-check in Word before submission).

### Carried-forward prose items (MEDIUM/LOW priority — judgment calls)
1. **Obj 2 Results gap (MEDIUM)**: Add 2–3 sentences in Results covering Census benchmarking preclusion (currently only in Discussion + Limitation 9).
2. **n=21 denominator path (MEDIUM)**: Explicitly trace 36 → 33 → 21 White% reporters.
3. **Sex/Gender Discussion redundancy (MEDIUM)**: Temporal race stats (46.2%→64.9%) repeated without new interpretation.
4. **Recommendation 3 (LOW-MEDIUM)**: Expand "ethics approval" to "Research Ethics Board (REB) approval."
5. **Indigenous reflexivity (LOW)**: One-line Limitations acknowledgment of no Indigenous community partnership.
6. **Limitations paragraph length (LOW)**: ~290 words in one paragraph; consider splitting.

### Newly-deferred this cycle
- Figure source audit (generate_figures.py) unchanged since Run 17; re-audit next cycle.
- Full parallel subagent sweep deferred to next cycle; focused fix this cycle.
- Verify that tables_and_figures.docx (separate companion document) is also dash-free — not audited this cycle.

## Decisions made autonomously (and why)

- **Atomic dash replacement in source, not docx**: Edited `generate_manuscript.py` (the authoritative generator) and regenerated the `.docx` rather than hand-patching XML, because the generator is the source of truth and future regenerations would otherwise reintroduce dashes. This complies with the task's "use the docx skill for docx edits" spirit (don't touch zipped XML for prose; edit the generator) while avoiding source/output drift.
- **Numeric ranges → " to "**: Chosen over " through " or parentheses because it is the most common replacement per modern English style guides, preserves readability in table cells, and matches the task's explicit example ("18–65" → "18 to 65").
- **Em-dash → context-appropriate punctuation**: Selected per-instance (comma for parenthetical asides, semicolon for independent-clause joins, parentheses for long embedded qualifiers, colon for heading-subtitle splits). Avoided blanket replacement to preserve prose quality.
- **Mann–Whitney → Mann-Whitney**: Hyphenated-proper-name convention; dash inside a proper name was the only remaining non-range en-dash after numeric ranges were handled.
- **Assessment of prior "stable" runs**: Runs 18 and 19 logs claimed zero statistical errors and passing checks. Those claims are not invalidated — but the dash audit described in the scheduled task ("After editing, unzip the .docx and grep every XML file inside `word/` for U+2013 and U+2014 to confirm zero remain") was apparently never executed against the XML. This was an omission, not a falsification. The stability counter resets with this cycle.
- **Stability counter reset**: Because this cycle introduced substantive changes, the "3 consecutive stable runs" countdown noted in the MANUSCRIPT_CHANGELOG resets. Recommend resuming the stability count after Run 20's changes are committed.
