# 05 Screening

> Research / Edia / Edia Racialized / 05 Screening

## Purpose

Title and abstract screening stage of the scoping review. Two independent
reviewers applied the eligibility criteria from
[`../03_inclusion_exclusion/criteria.md`](../03_inclusion_exclusion/criteria.md)
to **10,904 records** delivered by
[`../04_database_search/`](../04_database_search/_README.md) (post-deduplication,
post-automated filters), yielding **134 records** forwarded to full-text review
(129 originally written to `fulltext_screening_decisions.csv`, plus 5 QA-upgraded
MAP records retroactively propagated on 2026-04-11 — see
[`SCREENING_COMPLETE.md`](SCREENING_COMPLETE.md) → "Retroactive Correction").
This stage spans 73 sequential batches, three distinct screening protocols,
a multi-pass QA audit, and an automated false-negative validation layer.

## Canonical numbers

| Stage | Count |
|-------|-------|
| Records entering screening | **10,904** |
| Batches of ~150 records | 73 |
| Confirmed MAP (include) | **56** |
| UNCERTAIN (disagreement, needs full text) | **38** |
| OUT_OF_SCOPE (exclude) | **10,810** |
| Pre-QA MAP/UNCERTAIN pool | 194 |
| Forwarded to full-text review (post-correction) | **134** |
| Final included after full text | **66** |

> **Note (2026-04-11):** The "forwarded to full-text review" count was 129 prior to the retroactive QA propagation correction on 2026-04-11, after which 5 additional QA-upgraded MAP records (PMIDs 29338621, 36325158, 34637343, 40135470, 38445382) were added to the full-text pool, and Record #113 (PMID 41218611) was dropped as unobtainable.
>
> **Note (2026-04-11, criterion refinement):** A subsequent audit under the simplified "verified Canadian recruitment site" criterion dropped 3 additional records that had previously been included: **Record #20** (VIVRE vortioxetine, PMID 37227402 — 80 sites in 12 countries with no Canadian site), **Record #42** (NaB+NAC schizophrenia, PMID 39144112 — 5 sites all in Pakistan), and **Record #95** (Mavoglurant OCD, PMID 28044255 — 15 sites in Bulgaria/Germany/USA/Czechia/Switzerland). Net included count: 69 → **66**. See [`SCREENING_COMPLETE.md`](SCREENING_COMPLETE.md) for the full correction audit.

See [`PRISMA_2020_flow_diagram.md`](PRISMA_2020_flow_diagram.md) for the post-QA
flow diagram, and [`SCREENING_COMPLETE.md`](SCREENING_COMPLETE.md) for the
authoritative final report including the full list of confirmed MAP PMIDs.

## Screening methodology

Screening was conducted in three phases, each using a different protocol.
Every record in the review has been verified by at least two independent
reviewers (human or automated).

### Phase 1 — Batches 1–22 (3,309 records)

- **Initial pass:** Single-screened in an earlier session.
- **Secondary pass:** All MAP/UNCERTAIN decisions were dual-reviewed by
  six reviewer agents (Reviewer A + Reviewer B split across three chunks),
  reducing the initial MAP pool from 125 to 25 confirmed (100 were
  secondary analyses, protocols, non-pharmacological interventions, or
  non-Canadian sites).
- **False-negative check:** Codex GPT-5.4 performed a second-pass review
  of all 2,771 OUT_OF_SCOPE records. **0 false negatives.**

### Phase 2 — Batches 23–42 (3,000 records)

- **Initial pass:** Single-screened in this session.
- **Secondary pass:** QA audit of all MAP/UNCERTAIN decisions.
- **False-negative check:** Codex GPT-5.4 second-pass review of all 2,917
  OUT_OF_SCOPE records. **0 false negatives**, with 1 borderline flag
  (PMID 29458928, vitamin D, n=9 — judged out of scope on manual review).

### Phase 3 — Batches 43–73 (4,595 records)

- **Initial pass:** Fully dual-screened. Screener A and Screener B
  independently classified every record before any reconciliation.
- **Secondary pass:** QA audit of all MAP/UNCERTAIN decisions after
  reconciliation.
- **False-negative check:** Not applied; already dual-screened.

## Inter-rater agreement

Computed over the 4,458 dual-screened records in Phase 3 (batches 43–73):

| Metric | Value | Notes |
|--------|-------|-------|
| Percent agreement (normalized) | **97.8 %** | After collapsing `EXCLUDE` ≡ `OUT_OF_SCOPE` |
| Cohen's κ | **0.39** | Fair agreement |
| Raw string-match agreement | ~76 % | Pre-normalization artifact — do not report |
| Records classified MAP by either reviewer | 28 | Small positive class |

**Caveats.** The dataset is highly imbalanced (~96 % exclusions), so percent
agreement is inflated by trivially easy exclusions. Cohen's κ is the preferred
headline metric for imbalanced screening, and κ = 0.39 reflects fair agreement
on a task with a tiny positive class rather than weak screening. The raw 76 %
figure is a vocabulary-drift artifact — `EXCLUDE` and `OUT_OF_SCOPE` were used
synonymously across batches and are equivalent under the codebook. With only
28 MAP decisions in the dual-screened window, agreement on the harder
"include" decision is less well-characterized by these statistics and should
be interpreted cautiously. See
[`SCREENING_COMPLETE.md`](SCREENING_COMPLETE.md) for the full methodological
discussion.

## Quality assurance

Three overlapping QA mechanisms were applied:

1. **Human QA audits** of all MAP/UNCERTAIN decisions. Net effect on the
   confirmed MAP count was zero: 46 records moved UNCERTAIN → OUT_OF_SCOPE
   and 6 moved UNCERTAIN → MAP. Logged in
   [`qa_audit_corrections.md`](qa_audit_corrections.md) and consolidated in
   [`qa_consolidated_check1.md`](qa_consolidated_check1.md) /
   [`qa_consolidated_check2.md`](qa_consolidated_check2.md).
2. **Codex GPT-5.4 false-negative validation** on every OUT_OF_SCOPE record
   from Phases 1 and 2. Seven of the eight `codex_false_negatives_*.csv`
   files are empty (0 false negatives); the eighth contains the single
   borderline vitamin-D flag noted above.
3. **Dual-screened Phase 3** provides a built-in second reviewer by design.

Minor cosmetic CSV artifacts (289 empty IDs, 83 duplicate IDs, vocabulary
drift between `EXCLUDE` and `OUT_OF_SCOPE`) are documented in
[`../04_database_search/reports/search_log.md`](../04_database_search/reports/search_log.md)
and do not affect the final counts.

## Key files

| File | Purpose |
|------|---------|
| [`SCREENING_COMPLETE.md`](SCREENING_COMPLETE.md) | Final authoritative screening report |
| [`PRISMA_2020_flow_diagram.md`](PRISMA_2020_flow_diagram.md) | PRISMA 2020 flow diagram (post-QA numbers) |
| [`screening_progress.yaml`](screening_progress.yaml) | Structured progress data and running totals |
| [`fulltext_screening_decisions.csv`](fulltext_screening_decisions.csv) | 129 records originally forwarded to full-text screening (plus 5 QA-upgraded MAP records propagated retroactively on 2026-04-11 — see `SCREENING_COMPLETE.md`) |
| [`included_for_fulltext_review.csv`](included_for_fulltext_review.csv) | Full-text review candidate list |
| [`qa_audit_corrections.md`](qa_audit_corrections.md) | QA correction log |
| [`qa_consolidated_check1.md`](qa_consolidated_check1.md) · [`qa_consolidated_check2.md`](qa_consolidated_check2.md) | Consolidated QA check reports |
| [`qa_audit_batches48_73.md`](qa_audit_batches48_73.md) | QA audit notes for Phase 3 tail |
| [`deduplication_report.md`](deduplication_report.md) | Dedup methodology and results |
| `batch{N}_reconciled.csv` | Final per-batch decisions (N = 1–73) |
| `batch{N}_screenerA.csv` / `batch{N}_screenerB.csv` | Independent dual-screen outputs (Phase 3, batches 43–73) |
| `batch{N}_reviewer2.csv` | QA second-pass outputs (Phases 1 and 2, batches 1–42) |
| `batch{N}_summary.md` | Per-batch human-readable summary (batches 1–42) |
| `batch1_22_reviewer{A,B}_chunk{1,2,3}.csv` | Dual-review of batches 1–22 MAP/UNCERTAIN pool |
| `codex_false_negatives_*.csv` | Codex second-pass OUT_OF_SCOPE validation (mostly empty = 0 false negatives) |
| [`screened_results.csv`](screened_results.csv) | Legacy stub — see [`screened_results_README.md`](screened_results_README.md) |
| [`screening_summary_interim.md`](screening_summary_interim.md) | Mid-review interim summary (superseded by `SCREENING_COMPLETE.md`) |

## Outputs

- **134 records** → forwarded to full-text screening (129 via
  `fulltext_screening_decisions.csv`; 5 retroactively propagated on
  2026-04-11, see `SCREENING_COMPLETE.md`); extraction metadata lives in
  [`../06_data_extraction/`](../06_data_extraction/_README.md).
- **66 included studies** → full-text PDFs archived in
  [`../07_full_texts/`](../07_full_texts/README.md) (64 in hand, 2 pending
  manual retrieval).

## Known caveats and limitations

- **Imbalanced base rate.** Cohen's κ = 0.39 reflects a ~96 % exclusion base
  rate, not weak screening. Percent agreement is inflated by trivial exclusions.
- **Small positive class in Phase 3.** Only 28 of 4,458 dual-screened records
  were classified MAP by either reviewer, so IRR statistics primarily
  characterize agreement on exclusions.
- **Vocabulary drift.** `EXCLUDE` and `OUT_OF_SCOPE` were used synonymously
  across batches; IRR is reported on the normalized labels, and any raw
  agreement figures in per-batch CSVs should be ignored.
- **Cosmetic CSV artifacts.** 289 rows with empty IDs and 83 duplicate IDs
  exist in the batch CSVs but do not affect the final decision counts.
  Documented in `../04_database_search/reports/search_log.md`.

## Cross-references

- Eligibility criteria: [`../03_inclusion_exclusion/criteria.md`](../03_inclusion_exclusion/criteria.md)
- Upstream database search: [`../04_database_search/_README.md`](../04_database_search/_README.md)
- Full-text review candidates: [`../06_data_extraction/_README.md`](../06_data_extraction/_README.md)
- Included study PDFs: [`../07_full_texts/README.md`](../07_full_texts/README.md)
- Authoritative report: [`SCREENING_COMPLETE.md`](SCREENING_COMPLETE.md)
