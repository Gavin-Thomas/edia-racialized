# Manuscript Review Changelog
All changes made by the hourly review loop are logged here.
Format: ISO 8601 timestamp, section, change, rationale.

## [2026-04-16 10:02 MDT] Run 20 — Dash removal & line numbering

### Changed
- `08_manuscript/generate_manuscript.py`: Replaced all 34 en-dashes (U+2013) and 44 em-dashes (U+2014) with context-appropriate ASCII punctuation (comma, semicolon, colon, parentheses, "to" for numeric ranges). Previous runs 18–19 claimed stability but the dash check was never actually executed against the docx XML; 78 dashes were present throughout body text, headings, title page, table cells, and references.
- `08_manuscript/generate_manuscript.py`: Added continuous line numbering (`<w:lnNumType w:countBy="1" w:start="1" w:distance="360" w:restart="continuous"/>`) to the main manuscript sectPr, after the title page section break. Title page sectPr retains no `lnNumType` per spec.
- `08_manuscript/manuscript.docx`: Regenerated from source — zero en/em dashes confirmed across `word/document.xml`, `header1.xml`, `footer1.xml`, `styles.xml`, `numbering.xml`, `settings.xml`; line numbering present in main section only.
- `08_manuscript/manuscript_text.md`: Regenerated from source — zero dashes confirmed.

### Decisions made autonomously
- **Dash replacement strategy**: Numeric ranges (e.g., "44.9–68.6%", "6–785") became "X to Y"; prose em-dash asides became commas or parentheses; double em-dash parentheticals became commas or parentheses preserving meaning; headings with em-dash separators became colons ("Race/Ethnicity Reporting — Primary Outcome" → "Race/Ethnicity Reporting: Primary Outcome"); "sex–gender distinction" en-dash (not a range) became "sex/gender distinction" to match usage elsewhere in the manuscript.
- **Word count impact**: Abstract went from 296 to 297 words (still ≤300); main text went from 4,801 to 4,792 words (still ≤5,000). Net reduction on main text because the previous counter treated free-standing em-dashes as words.
- **Line numbering position/distance**: `w:distance="360"` twips (~0.25 inch) chosen as a conservative default that keeps line numbers visible without crowding body text at 3 cm left margin.
- **Mann–Whitney spelling**: "Mann–Whitney" (en-dash) normalized to "Mann-Whitney" (hyphen), consistent with standard hyphenated proper-name usage in statistics style guides.
- **Backup retention**: Kept the timestamped backup `manuscript.docx.bak-20260416-100230` (first since policy added); previous runs did not create backups, so no older backups to prune.

### Deferred
- Reverification of figure source code (generate_figures.py) — unchanged this cycle; figures remain as produced by Run 17.
- Running the full analysis pipeline end-to-end in a clean venv — out of scope for this cycle (dash/line-number fix was the priority violation).
- Full parallel subagent sweep (code-review / data-extraction / methodology / fact-check / figures / manuscript) — deferred to next cycle; this cycle focused on the concrete guardrail violation (78 dashes present) to restore basic submission readiness before next audit.

### Open items requiring human input
- Corresponding author email still a placeholder: `[corresponding author email]` (see `generate_manuscript.py:504`).
- Protocol registration on OSF pending (MANUSCRIPT_CHANGELOG carried-forward TODO 3).
- Grey-literature URL verification (refs 3, 6, 8, 13, 14, 28, 30, 31) pending.
- Six carried-forward MEDIUM/LOW prose items from Run 18–19 unchanged this cycle (Obj 2 results gap, n=21 denominator path, Sex/Gender discussion redundancy, Recommendation 3 REB naming, Indigenous reflexivity, Limitations paragraph length).
