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
 Records removed before screening (n = 43,764):
 ┌──────────────────────────────────────────────┐
 │  Duplicate records ............. 14,497      │
 │  No abstract available ..........  4,152     │
 │  Outside date range (2016-2026) . 1,345      │
 │  Not relevant (missing Canada/   22,913      │
 │    MH/RCT terms in title/abstract)           │
 │  Systematic reviews / MAs .......   857      │
 └──────────────────────────────────────────────┘
                        │
                        ▼

                     SCREENING
 ================================================================

 Records screened at title/abstract (n = 10,719)
 ┌──────────────────────────────────────────────┐
 │  Method: Dual independent screening          │
 │    Reviewer 1 + Reviewer 2 (independent)     │
 │    Conservative reconciliation rules         │
 │    QA audits on all MAP/UNCERTAIN decisions   │
 │    Codex GPT-5.4 false-negative verification │
 │  Inter-rater agreement: 95.2%                │
 └──────────────────────────────────────────────┘
           │                          │
           ▼                          ▼
 Records excluded             Reports sought for
 (n = 10,590)                 full-text retrieval
 ┌────────────────────┐       (n = 129)
 │ Both reviewers     │              │
 │ agreed: exclude    │              │
 │                    │              ▼
 │ Top reasons:       │       Reports assessed for
 │ • Non-Canadian     │       eligibility (n = 129)
 │ • Non-pharma       │       ┌────────────────────┐
 │ • Non-RCT          │       │ Both agree MAP: 36 │
 │ • Non-MH           │       │ Uncertain:     93  │
 │ • Secondary analysis│      │ (needs arbiter)    │
 │ • Protocol only    │       └────────────────────┘
 │ • Review/MA        │              │
 └────────────────────┘              │
                                     ▼

                  FULL-TEXT SCREENING
 ================================================================

 Reports for full-text review (n = 129)
           │                          │
           ▼                          ▼
 Reports excluded              Studies included
 at full-text                  in review
 (n = 64)                      (n = 65)
 ┌────────────────────┐       ┌────────────────────┐
 │ Reasons:           │       │ Disorder categories│
 │ • Secondary/post-  │       │ (preliminary):     │
 │   hoc analysis: 34 │       │ • Depression:  ~20 │
 │ • No Canadian      │       │ • Bipolar:     ~10 │
 │   site/PI:      12 │       │ • Dementia:    ~10 │
 │ • Not RCT/protocol/│       │ • Substance:   ~10 │
 │   review/case:  10 │       │ • Schizophrenia:~7 │
 │ • Non-pharma/not   │       │ • ADHD:        ~5  │
 │   targeting MH:  7 │       │ • Other:       ~3  │
 │ • Pre-2016 primary │       └────────────────────┘
 │   results:       1 │
 └────────────────────┘
                                     │
                                     ▼

                     INCLUDED
 ================================================================

 Studies included for data extraction (n = 65)
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
| No abstract available | 4,152 | 35,834 |
| Year outside 2016-2026 | 1,345 | 34,489 |
| Not relevant (missing Canada/MH/RCT terms) | 22,913 | 11,576 |
| Systematic reviews / meta-analyses | 857 | 10,719 |

### Title/Abstract Screening

| Metric | Value |
|--------|-------|
| Records screened | 10,719 |
| Screening method | Dual independent reviewers |
| Inter-rater agreement | 95.2% |
| QA audits performed | 3 (batches 23-42, 48-73, 1-22 MAP) |
| Codex false-negative checks | 8 (all 10,904 OUT_OF_SCOPE verified) |
| Excluded at title/abstract | 10,590 |
| Forwarded to full-text | 129 |
| — Both reviewers agree include (MAP) | 36 |
| — Uncertain, needs arbiter | 93 |

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

*File: `fulltext_screening_decisions.csv` contains the 129 records for full-text review with dual-reviewer decisions.*
