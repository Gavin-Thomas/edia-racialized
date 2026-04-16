# PRISMA 2020 Flow Diagram

## EDIA Reporting in Canadian Mental Health Pharmacotherapy RCTs (2016-2026)

---

```
                    IDENTIFICATION
 ================================================================

 Records identified from databases (n = 54,483):
 ┌──────────────────────────────────────────────┐
 │  PubMed .......................... 9,964      │
 │  Europe PMC ..................... 15,772      │
 │  Scopus ......................... 27,983      │
 │  OpenAlex .........................  764      │
 └──────────────────────────────────────────────┘
                        │
                        ▼
 Records removed before screening (n = 43,579):
 ┌──────────────────────────────────────────────┐
 │  Duplicate records ............. 14,497      │
 │  No abstract available ..........  1,557     │
 │  Outside date range (2016-2026) . 12,473     │
 │  Not relevant (missing Canada/   12,511      │
 │    MH/RCT terms in title/abstract)           │
 │  Systematic reviews / MAs .......  2,541     │
 └──────────────────────────────────────────────┘
                        │
                        ▼

                     SCREENING
 ================================================================

 Records screened at title/abstract (n = 10,904)
 ┌──────────────────────────────────────────────┐
 │  Method: Dual independent screening          │
 │    Reviewer 1 + Reviewer 2 (independent)     │
 │    Conservative reconciliation rules         │
 │    QA audits on all MAP/UNCERTAIN decisions   │
 │    Codex GPT-5.4 false-negative verification │
 │  Inter-rater agreement:                      │
 │    97.8% (normalized) | κ = 0.39 (Cohen)     │
 │    (96% exclusion base rate; see caveats)     │
 └──────────────────────────────────────────────┘
           │                          │
           │                          │
           ▼                          ▼
 Records excluded             Reports sought for
 (n = 10,810)                 full-text retrieval
 ┌────────────────────┐       (n = 134) †
 │ Both reviewers     │              │
 │ agreed: exclude    │              │
 │                    │              ▼
 │ Top reasons:       │       Reports not retrieved
 │ • Non-Canadian     │       (n = 1) — Record #113
 │ • Non-pharma       │       (Semaglutide MDD, Med
 │ • Non-RCT          │       2026; unobtainable)
 │ • Non-MH           │              │
 │ • Secondary analysis│             ▼
 │ • Protocol only    │       Reports assessed for
 │ • Review/MA        │       eligibility (n = 133)
 └────────────────────┘       ┌────────────────────┐
                              │ Both agree MAP: 56 │
                              │ Uncertain:     38  │
                              │ QA-propagated:  5  │
                              │ (resolved at FT)   │
                              └────────────────────┘
                                     │
                                     ▼

                  FULL-TEXT SCREENING
 ================================================================

 Reports for full-text review (n = 133 assessed)
           │                          │
           ▼                          ▼
 Reports excluded              Studies included
 at full-text                  in review
 (n = 70) ‡§                   (n = 63) ‡§
 ┌────────────────────┐       ┌────────────────────┐
 │ Reasons:           │       │ N = 63 studies     │
 │ • Secondary/post-  │       │ (8,837 participants│
 │   hoc analysis: 35 │       │                    │
 │ • No Canadian      │       │ Disorder categories│
 │   site:         16 │       │ • Depression:  ~19 │
 │ • Not RCT/protocol/│       │ • Bipolar:     ~10 │
 │   review/case:  10 │       │ • Dementia:    ~10 │
 │ • Non-pharma/not   │       │ • Substance:   ~10 │
 │   targeting MH:  8 │       │ • Schizophrenia:~7 │
 │ • Pre-2016 primary │       │ • ADHD:        ~5  │
 │   results:       1 │       │ • Other:       ~2  │
 │                    │       └────────────────────┘
 └────────────────────┘
                                     │
                                     ▼

                     INCLUDED
 ================================================================

 Studies included for data extraction (n = 63) † ‡ §
 ┌──────────────────────────────────────────────┐
 │  Framework: PROGRESS-Plus                    │
 │  Primary focus: Race/ethnicity reporting     │
 │  Benchmarking: Statistics Canada Census 2021 │
 │                                              │
 │  Extraction codebook variables:              │
 │  • Race/ethnicity (granularity, framework)   │
 │  • Sex/gender (distinguished?)               │
 │  • SES, education, occupation                │
 │  • Indigenous participation (OCAP)           │
 │  • CONSORT-Equity compliance                 │
 │  • Trial-level covariates                    │
 └──────────────────────────────────────────────┘
```

**Footnotes:**
- † 134 forwarded to full text after retroactive QA propagation (2026-04-11); originally 129.
- ‡ Counts reflect two 2026-04-11 corrections: +5 QA-upgraded MAP records propagated; -1 unobtainable (Record #113); -3 no Canadian recruitment site (Records #20, #42, #95).
- § Counts reflect 2026-04-13 third correction: -3 additional exclusions at full text: Record #4 (no Canadian site per ClinicalTrials.gov), Record #12 (secondary analysis of #13), Record #45 (not a pharmacotherapy comparison). Net: 66 → **63 included**.

---

## Screening Details

### Databases and Search Strategy

| Database | API | Records | Date searched |
|----------|-----|---------|---------------|
| PubMed | E-utilities | 9,964 | 2026-03-30 |
| Europe PMC | REST API | 15,772 | 2026-03-30 |
| Scopus | Elsevier API | 27,983 | 2026-03-30 |
| OpenAlex | REST API | 764 | 2026-03-30 |

Search strategy: 3 concept blocks (Mental Health + RCT Design + Canada) combined with AND. EDIA terms intentionally excluded to avoid sampling bias. English language. Date range 2016-2026.

### Deduplication

| Method | Duplicates found |
|--------|-----------------|
| DOI match (exact) | 14,151 |
| PMID match (exact) | 184 |
| Fuzzy title match (>0.93) | 162 |
| **Total duplicates removed** | **14,497** |

### Automated Pre-screening Filters

| Filter | Records removed | Remaining |
|--------|----------------|-----------|
| Starting unique records | — | 39,986 |
| No abstract available | 1,557 | 38,429 |
| Year outside 2016-2026 | 12,473 | 25,956 |
| Not relevant (missing Canada/MH/RCT terms) | 12,511 | 13,445 |
| Systematic reviews / meta-analyses | 2,541 | 10,904 |

### Title/Abstract Screening

| Metric | Value |
|--------|-------|
| Records screened | 10,904 |
| Screening method | Dual independent reviewers |
| Inter-rater agreement (percent, normalized) | 97.8% |
| Inter-rater agreement (Cohen's κ) | 0.39 (fair) |
| QA audits performed | 3 (batches 23-42, 48-73, 1-22 MAP) |
| Codex false-negative checks | 8 (all 10,904 OUT_OF_SCOPE verified) |
| Excluded at title/abstract | 10,810 |
| Forwarded to full-text | 134 † |
| — Confirmed MAP (post-QA) | 56 |
| — Uncertain, needs full-text | 38 |
| — Other forwarded (reviewer disagreements resolved to full-text) | 35 |
| — QA-propagated MAP (added 2026-04-11, see footnote) | 5 |

### Exclusion Reasons at Title/Abstract (top categories)

| Reason | Approximate % |
|--------|--------------|
| Non-Canadian study | ~45% |
| Non-pharmacological intervention | ~20% |
| Not a mental health condition | ~10% |
| Secondary/post-hoc analysis | ~8% |
| Protocol without results | ~7% |
| Review/meta-analysis | ~5% |
| Observational/non-RCT design | ~3% |
| Other (animal, <10 participants) | ~2% |

### Methodological Notes on Inter-Rater Agreement

- **Percent agreement (97.8%)** was computed on the 4,458 dual-screened records in batches 43-73, after normalizing decision-label vocabulary (the labels `EXCLUDE` and `OUT_OF_SCOPE` were used synonymously across batches and are collapsed for agreement calculations).
- **Cohen's κ = 0.39** ("fair" agreement) is reported alongside percent agreement because the base rate of exclusions in this dataset is ~96%. With such an imbalanced class distribution, raw percent agreement is inflated by trivially easy exclusions, so κ is the preferred headline metric.
- **Raw string-match agreement (un-normalized): ~76%** appears if the `EXCLUDE`/`OUT_OF_SCOPE` vocabulary mismatch is not corrected, and should **not** be used — it reflects vocabulary drift across batches rather than true disagreement on the screening decision.
- **Caveat on the include decision:** of the 4,458 dual-screened records, only 28 were classified as MAP by either reviewer. Agreement on exclusions is therefore near-perfect, but agreement on the harder "include" decisions is less well-characterized. This is a known limitation of reporting percent agreement alone for scoping reviews with heavily imbalanced screening outcomes.
- **Post-QA reclassification:** QA audits upgraded 6 UNCERTAIN records to MAP, reclassified 3 MAP records to OUT_OF_SCOPE, and resolved 46 UNCERTAIN records to OUT_OF_SCOPE. Pre-QA consensus counts (36 MAP / 93 UNCERTAIN) therefore differ from the post-QA canonical counts used in the flow diagram above (56 MAP / 38 UNCERTAIN).

---

## Status

| Stage | Status | Date |
|-------|--------|------|
| Identification | Complete | 2026-03-30 |
| Deduplication | Complete | 2026-03-30 |
| Automated filtering | Complete | 2026-03-30 |
| Title/abstract screening | Complete | 2026-04-01 |
| Full-text screening | **Complete** | 2026-04-02 |
| Data extraction | Not started | — |
| Analysis | Not started | — |

---

*File: `fulltext_screening_decisions.csv` contains the 129 records originally forwarded for full-text review with dual-reviewer decisions. Five additional records (PMIDs 29338621, 36325158, 34637343, 40135470, 38445382) were retroactively propagated to the full-text stage on 2026-04-11, bringing the total to 134.*

---

## † Footnote: 2026-04-11 retroactive correction

On 2026-04-11, a final consistency check uncovered five MAP records that were confirmed as inclusions in `SCREENING_COMPLETE.md` but had never been written into `fulltext_screening_decisions.csv`, so they were silently omitted from the full-text screening stage. All five were re-assessed against the inclusion criteria and confirmed to meet them with HIGH confidence; they have been added to the final included set.

- **Reports sought for retrieval:** 129 → **134** (5 retroactively propagated MAP records: PMIDs 29338621, 36325158, 34637343, 40135470, 38445382)
- **Reports not retrieved:** 0 → **1** (Record #113, PMID 41218611, semaglutide for cognitive dysfunction in MDD, *Med* 2026 — unobtainable via any open-access version identified through OpenAlex and Crossref metadata (PubMed Central, Europe PMC, publisher OA), the publisher site, or the institutional proxy; dropped from the included set)
- **Reports assessed for eligibility:** 129 → **133** (134 forwarded minus 1 not retrieved)
- **Studies included:** 65 → **69** (before the ‡ second correction below)
- **Studies excluded at full text:** 64 (unchanged by this first correction — the 5 newly-propagated records were all included)
- **Full-text PDFs in hand:** 64 of 65 → **67 of 69** (Records 132 PRC-063 and 133 MIRAGE pending manual retrieval)

See `SCREENING_COMPLETE.md` → "Retroactive Correction (2026-04-11)" for the full audit trail and per-record inclusion justifications.

---

## ‡ Footnote: 2026-04-11 second correction — simplified Canadian-site criterion

After the inclusion criterion was simplified on 2026-04-11 to require a verified Canadian recruitment site (removing the underspecified "Canadian institutional PI leadership" alternative — see `../03_inclusion_exclusion/criteria.md` → "Criteria Revisions"), three previously-included records were re-verified via full PDF review and ClinicalTrials.gov API queries. None had a Canadian recruitment site, and all three were reclassified as EXCLUDED at full text under the new criterion:

| Record # | PMID | Study | Actual sites |
|----------|------|-------|--------------|
| #20 | 37227402 | VIVRE vortioxetine vs desvenlafaxine (McIntyre 2023) | 80 sites / 12 countries (Russia, Argentina, Ukraine, etc.) — no Canada |
| #42 | 39144112 | NaB+NAC schizophrenia feasibility (Husain 2024) | 5 sites, all in Pakistan |
| #95 | 28044255 | Mavoglurant for OCD (Rutrick 2017) | 15 sites in Bulgaria/Germany/USA/Czechia/Switzerland |

Each trial had a Canadian-affiliated author (McIntyre, Husain, Gomez-Mancilla) but no verified Canadian recruitment site. The agreement metrics (97.8% normalized percent agreement, Cohen's κ = 0.39) are not affected by this retroactive full-text reclassification — they were computed on the title/abstract screening stage only.

- **Reports sought for retrieval:** 134 (unchanged)
- **Reports not retrieved:** 1 (Record #113, unchanged)
- **Reports assessed for eligibility:** 133 (unchanged)
- **Studies included:** 69 → **66**
- **Studies excluded at full text:** 64 → **67**
- **Full-text PDFs in hand:** 67 of 69 → **64 of 66** (Records 132 PRC-063 and 133 MIRAGE still pending manual retrieval)

The 3 dropped records' PDFs remain on disk in `../07_full_texts/` as audit-trail evidence for the retroactive exclusion decision. See `SCREENING_COMPLETE.md` → "Criterion refinement drop (2026-04-11, second correction)" and `../03_inclusion_exclusion/criteria.md` → "Retroactive application of refined criterion (2026-04-11)" for per-record justifications.
