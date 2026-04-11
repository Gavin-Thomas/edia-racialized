# Next Session Prompt — Finish Full-Text Review & Run Data Extraction

Hand this document to the next worker on the project (Claude Code session, another agent, or the human researcher). It reflects the state of the review as of 2026-04-11.

---

## 1. Current Status

- **Title/abstract screening:** Complete. 10,904 records screened, 134 forwarded to full-text review.
- **Full-text retrieval:** 64 of 66 PDFs in hand. Two records remain (see Task A).
- **Full-text screening:** Complete for the 64 retrieved records. Two records (132, 133) are provisional, pending PDF retrieval.
- **Data extraction:** NOT STARTED.
- **Provisional final included count:** 66 studies (subject to full-text review of the 2 pending PDFs).
- **Dropped from included set:**
  - Record #113 (Semaglutide for MDD) — unobtainable after exhaustive retrieval attempts.
  - Records #20 (VIVRE vortioxetine, PMID 37227402), #42 (NaB+NAC schizophrenia, PMID 39144112), and #95 (Mavoglurant OCD, PMID 28044255) — dropped 2026-04-11 under the simplified "verified Canadian recruitment site" criterion after site-verification audit found no Canadian recruitment site.

---

## 2. Immediate To-Do

### Task A — Retrieve the 2 pending PDFs

**Record #132: PRC-063 Methylphenidate for Adolescent ADHD**
- Authors: Weiss et al. 2021
- Journal: *Journal of Child and Adolescent Psychopharmacology*
- PMID: 34637343
- DOI: 10.1089/cap.2021.0034
- License: CC-BY hybrid open access on SAGE
- Retrieval path: https://journals.sagepub.com/doi/pdf/10.1089/cap.2021.0034
- If automated download is blocked by Cloudflare, open the URL in a browser and save the PDF manually.
- Save as: `07_full_texts/record_132.pdf`

**Record #133: MIRAGE Mirtazapine for Chronic Insomnia**
- Authors: Nguyen et al. 2025
- Journal: *Age and Ageing*
- PMID: 40135470
- DOI: 10.1093/ageing/afaf050
- Status: Paywalled (no OA copy located)
- Retrieval paths (in order of preference):
  1. University of Calgary library proxy: https://login.ezproxy.lib.ucalgary.ca/login?url=https://doi.org/10.1093/ageing/afaf050
  2. Direct request to corresponding author Patrick V-Q Nguyen, Pharmacy Dept., Centre Hospitalier de l'Université de Montréal (CHUM)
- Save as: `07_full_texts/record_133.pdf`

### Task B — Full-text review for records #132 and #133

Once each PDF is obtained:
1. Apply the inclusion criteria in `03_inclusion_exclusion/criteria.md`.
2. The load-bearing criterion is **verified Canadian recruitment site** (not merely Canadian co-authorship).
3. Record the decision in `05_screening/fulltext_screening_decisions.csv`, updating the `reviewer_1`, `reviewer_2`, `final_decision`, and `arbiter_notes` fields.
4. If either record is **excluded** after full-text review, revise the provisional included count downward (66 → 65 or 64) in every dependent file (see Task D).

### Task C — Data extraction

This is the main body of remaining work. Do not begin until Task A and Task B are settled — the included set must be frozen first.

1. **Read the codebook.** `06_data_extraction/extraction_codebook.md` is the single source of truth for variable definitions. Follow it literally.
2. **Framework:** PROGRESS-Plus.
3. **Key variable families:**
   - Race/ethnicity: reported? categories used? granularity? conceptual framework? subgroup analyses performed?
   - Sex and gender: distinguished from each other? category labels used?
   - Indigenous participation: reported? OCAP principles referenced?
   - Other PROGRESS-Plus axes: place, occupation, education, SES, social capital, age, disability, SOGI
   - Trial covariates: funder, sample size, disorder category, intervention, design, site count
4. **Benchmarking:** For every study that reports race/ethnicity, map its categories onto the Statistics Canada Census 2021 taxonomy and record discrepancies.
5. **Output file:** `06_data_extraction/extracted_data.csv` — one row per included study.
6. **Dual extraction:** Recommended. Run two independent extraction passes and target Cohen's κ > 0.80 on coded fields.
7. **Pilot first.** Extract the first 10 papers, review for consistency, calibrate the codebook or rubric if needed, then scale to the remaining studies.
8. **Parallelism note:** For a set this size (~64–66 studies), splitting across parallel sub-agents (5–8 studies per agent) is appropriate. Reconcile at the end.

### Task D — Update the PRISMA flow diagram

After Task B is complete and the included count is final:
- Update `05_screening/PRISMA_2020_flow_diagram.md` with the final included count and the full-text exclusion reasons with counts.
- Update `05_screening/SCREENING_COMPLETE.md` to match.
- If the included count changed, audit every other file that cites the number (66 appears in multiple places).

### Task E — Draft manuscript

Only begin once data extraction (Task C) is complete and reconciled.

- **Target journals (in preference order):** Canadian Journal of Psychiatry, BMC Medical Research Methodology, Systematic Reviews.
- **Reporting standard:** PRISMA-ScR (Scoping Reviews extension).
- **Required methodological disclosures:**
  - AI-assisted screening using Codex GPT-5.4 plus downstream LLM agents (describe the workflow and the human adjudication layer).
  - Simplified inclusion criterion: Canadian recruitment site only (the original PI-leadership clause was dropped — document this change).
- **Acknowledge limitations explicitly:**
  - English-language only.
  - Inter-rater agreement κ = 0.39 (fair); note that this is driven by an imbalanced base rate, not by noisy reviewers.
  - Not pre-registered.

---

## 3. Key Files Reference

| File | Purpose |
|---|---|
| `_README.md` | Project overview and entry point |
| `03_inclusion_exclusion/criteria.md` | Inclusion and exclusion criteria (authoritative) |
| `05_screening/SCREENING_COMPLETE.md` | Final title/abstract screening report |
| `05_screening/PRISMA_2020_flow_diagram.md` | PRISMA 2020 flow, pending final full-text numbers |
| `05_screening/fulltext_screening_decisions.csv` | Per-record full-text decisions |
| `06_data_extraction/extraction_codebook.md` | PROGRESS-Plus extraction codebook (authoritative) |
| `07_full_texts/ALL_66_LINKS.md` | Full-text retrieval status for all 66 records |
| `07_full_texts/README.md` | Retrieval log and notes |
| `PROTOCOL_REGISTRATION.md` | Transparency statement and protocol disclosures |

---

## 4. Critical Rules

1. **Do not fabricate.** If a paper does not report a variable, code it as unknown / not reported. Never invent values to fill a cell.
2. **Be strict on inclusion.** The Canadian recruitment site criterion must be verified in the paper itself or on ClinicalTrials.gov. A Canadian co-author alone is not sufficient.
3. **Document every decision.** Reviewers will read these files. Every non-obvious call needs a reason written down.
4. **Dual review where possible.** Independent passes catch errors that a single pass cannot.
5. **Verify after major steps.** Re-read what you wrote. Recount the rows. Cross-check dependent files when a number changes.

---

## 5. Current Numbers (as of 2026-04-11)

| Metric | Count |
|---|---|
| Records screened (title/abstract) | 10,904 |
| Forwarded to full-text | 134 |
| Included (provisional) | 66 |
| Full-text PDFs obtained | 64 |
| Full-text PDFs pending | 2 (records #132, #133) |
| Dropped (unobtainable) | 1 (record #113) |
| Dropped (no Canadian recruitment site, criterion refinement 2026-04-11) | 3 (records #20, #42, #95) |

---

## 6. Handoff Checklist

Before declaring the review complete, confirm:

- [ ] Records #132 and #133 PDFs retrieved and screened
- [ ] Final included count frozen and propagated to all dependent files
- [ ] PRISMA 2020 flow diagram updated with full-text exclusion reasons
- [ ] Data extraction complete for every included study
- [ ] Dual extraction reconciled; κ recorded
- [ ] Race/ethnicity categories benchmarked against Statistics Canada 2021 taxonomy
- [ ] Manuscript draft underway
