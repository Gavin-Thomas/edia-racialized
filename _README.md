# EDIA Reporting in Canadian Mental Health Pharmacotherapy RCTs

> Scoping review of equity, diversity, inclusion, and accessibility (EDIA) reporting in Canadian mental health pharmacotherapy RCTs (2016-2026), with a focus on racialized groups and a distinct Indigenous analysis. Framework: **PROGRESS-Plus + CONSORT-Equity**.

## Project status

| Stage | Status | Date |
|-------|--------|------|
| Literature search (landscape) | Complete | 2026-03 |
| Research question | Complete | 2026-03 |
| Inclusion/exclusion criteria | Complete | 2026-03 |
| Database search (4 databases) | Complete | 2026-03-30 |
| Title/abstract screening (10,904 records) | Complete | 2026-04-01 |
| Full-text screening (134 records) | 67 of 69 complete; 2 pending formal full-text review (records #132, #133) | 2026-04-02 initial / 2026-04-11 retroactive +5 |
| Full-text retrieval (69 studies) | 67 of 69 obtained, 2 pending manual retrieval | 2026-04 |
| Data extraction | **Not started** | — |

**Headline numbers**: 54,483 raw records → 39,986 unique after deduplication → 10,904 after filters → 134 forwarded to full text → **69 included** (67 full text in hand, 2 pending manual retrieval).

> **Note (2026-04-11):** Counts above reflect a retroactive QA correction that propagated 5 previously-confirmed MAP records (PMIDs 29338621, 36325158, 34637343, 40135470, 38445382) into the included set, and dropped Record #113 (PMID 41218611, Semaglutide MDD, *Med* 2026) as unobtainable. Prior drafts of this README showed the pre-correction counts (129 forwarded / 65 included). See **Revision history** at the bottom of this file.

## Contents

- `01_literature_search/` — Landscape report and key references
- `02_research_question/` — PICO framework and objectives
- `03_inclusion_exclusion/` — Criteria with decision rules
- `04_database_search/` — Scripted fetch, deduplication, and refinement pipeline
- `05_screening/` — Batch reconciled CSVs, QA audits, PRISMA flow diagram, screening summary
- `06_data_extraction/` — PROGRESS-Plus extraction codebook *(renamed from `05_data_extraction`)*
- `07_full_texts/` — Retrieved full-text PDFs for included studies *(renamed from `06_full_texts`)*
- `project.yaml` — Project configuration and status
- `Search_Strategies_Canadian_MH_RCTs.md` — Detailed search strategies for all databases
- `NEXT_SESSION_PROMPT.md` — Instructions for full-text screening and data extraction
- `requirements.txt` — Python dependencies (currently only standard library is used)

Each stage folder has its own `_README.md` with the methodology, inputs, and outputs for that stage. Start there for detail; this page is the landing index.

## Quick reproducibility

### Requirements

- **Python 3.11+** — all scripts in `04_database_search/` use only the standard library (`urllib`, `csv`, `json`, `xml.etree`, `difflib`)
- **Scopus API key** — set `SCOPUS_API_KEY` in your environment for `fetch_scopus.py`
- Optional future deps can be added to `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Run the search pipeline

```bash
cd 04_database_search
python fetch_pubmed.py
python fetch_europepmc.py
python fetch_openalex.py
export SCOPUS_API_KEY=your_key_here
python fetch_scopus.py
python deduplicate.py
python refine_results.py
```

See [`04_database_search/_README.md`](04_database_search/_README.md) for full instructions, expected outputs, and per-database record counts.

## Key methodological facts

| Item | Value |
|------|-------|
| Review type | Scoping review |
| Date range | 2016-01-01 to 2026-03-30 |
| Databases | PubMed (9,964) / Europe PMC (15,772) / Scopus (27,983) / OpenAlex (764) |
| Framework | PROGRESS-Plus + CONSORT-Equity |
| Primary focus | Racialized groups (with distinct Indigenous analysis) |
| Screening | Dual independent review of all 10,904 eligible records |
| Inter-rater agreement (dual-screened batches 43-73, normalized) | **97.8%** |
| Cohen's κ (headline metric) | **0.39** (fair agreement) |
| Benchmarks | Statistics Canada Census 2021 (visible minority, Indigenous identity); CCHS Mental Health; CIHI Hospital Mental Health Database |

## Known limitations

- **English-language only**: a scope restriction, not just a limitation. Quebec represents ~23% of Canada's population and a meaningful proportion of Quebec-led RCTs publish primarily in French; French-language work is systematically excluded. A targeted French-language sensitivity search on two disorder categories (depression, substance use) is planned as a supplementary exclusion-rate estimate. See [`03_inclusion_exclusion/criteria.md`](03_inclusion_exclusion/criteria.md).
- **Four API-accessible databases only**: PsycINFO and CINAHL were excluded because they lack public APIs, which would break pipeline reproducibility. For pharmacotherapy RCTs their marginal yield beyond PubMed/Scopus is modest.
- **Cohen's κ = 0.39 (fair agreement)**: despite 97.8% normalized percent agreement, kappa is modest because the base rate of exclusions is ~96% and only 28 of 4,458 dual-screened records were classified as MAP by either reviewer. Agreement on the harder "include" decisions is therefore less well-characterized. See [`05_screening/SCREENING_COMPLETE.md`](05_screening/SCREENING_COMPLETE.md) for the full discussion.
- **Temporal comparison windows are unequal**: pre-2020 spans 4 years vs. 6-7 years post-2020. Comparisons must be reported as proportions within each period, not absolute counts; sensitivity analyses at 2018 (TCPS2) and 2022 (CIHR EDI) are planned.
- **Data extraction has not started**: findings described below the screening stage are provisional pending the extraction phase.

## AI-assisted screening disclosure

Title/abstract screening of all 10,904 eligible records was performed by Large Language Model (LLM) agents, specifically:

- **Batches 1-22**: Initial single-pass screening by an LLM, followed by a dual-review of all MAP/UNCERTAIN records, plus a Codex GPT-5.4 false-negative check on all OUT_OF_SCOPE records.
- **Batches 23-42**: Single-pass screening by an LLM plus a structured QA audit and Codex GPT-5.4 second-pass false-negative validation.
- **Batches 43-73**: Dual independent screening (Screener A and Screener B both LLM agents) with post-hoc reconciliation.

The use of LLM agents as screeners is a material methodological choice that readers should consider when interpreting the inter-rater agreement metrics (97.8% normalized, Cohen's κ = 0.39). QA audits with a separate LLM (Codex GPT-5.4) identified 0 false negatives across ~5,900 OUT_OF_SCOPE records. All screening decisions and reasoning are available per-batch in `05_screening/batch*_reconciled.csv`.

The extraction and analysis stages have not yet been executed; the decision of whether to use LLM, human, or hybrid screening for those stages has not been made.

See `05_screening/SCREENING_COMPLETE.md` for full methodology details including batch-level agreement calculations.

## Authorship and conflicts of interest

**Author**: Gavin Thomas, University of Calgary Cumming School of Medicine (MD Program).

This is an independent student-led scoping review. There is **no faculty PI, no
Canadian senior author, and no institutional sponsor** beyond the author's
affiliation with the University of Calgary.

**Conflicts of interest**: None declared.
**Funding**: None. Self-funded.

See [`AUTHORS.md`](AUTHORS.md) for the full authorship statement.

## License and registration

- **License**: [CC BY 4.0](LICENSE) — free to share and adapt with attribution.
- **Pre-registration**: **Not pre-registered.** See [`PROTOCOL_REGISTRATION.md`](PROTOCOL_REGISTRATION.md) for the full transparency statement and rationale.
- **Reporting guidelines**: PRISMA 2020 and PRISMA-ScR. See [`05_screening/PRISMA_2020_flow_diagram.md`](05_screening/PRISMA_2020_flow_diagram.md).

## Citation

```
Thomas, G. (2026). EDIA Reporting in Canadian Mental Health Pharmacotherapy
RCTs: A Scoping Review (2016–2026). GitHub repository.
https://github.com/Gavin-Thomas/edia-racialized
```

## Revision history

### 2026-04-11 — Retroactive QA propagation correction

A consistency check discovered that five records confirmed as MAP in `SCREENING_COMPLETE.md` had never been written into `fulltext_screening_decisions.csv`, and therefore never entered the full-text screening pipeline. A retroactive investigation confirmed that all five meet the inclusion criteria with HIGH confidence (Canadian-led RCTs of pharmacological interventions targeting mental disorders, published 2016–2025). All five were added to the final included set:

| Record # | PMID | Topic | Retrieval |
|----------|------|-------|-----------|
| 130 | 29338621 | CDP-choline sensory gating, schizophrenia (Aidelbaum 2018, *J Psychopharmacol*) | PDF retrieved |
| 131 | 36325158 | Low-dose buprenorphine augmentation for TRD (Lee 2022, *Biol Psychiatry Glob Open Sci*) | PDF retrieved (PMC9616305) |
| 132 | 34637343 | PRC-063 methylphenidate adolescent ADHD (Weiss 2021, *J Child Adolesc Psychopharmacol*) | Pending manual retrieval (SAGE hybrid OA) |
| 133 | 40135470 | Mirtazapine for chronic insomnia (MIRAGE, Nguyen 2025, *Age and Ageing*) | Pending manual retrieval (paywalled) |
| 134 | 38445382 | Intranasal oxytocin + IPT for MDD (Ellenbogen 2024, *Psychological Medicine*) | PDF retrieved (PMC11413360) |

At the same time, **Record #113** (PMID 41218611, semaglutide for cognitive dysfunction in MDD, *Med* 2026, DOI 10.1016/j.medj.2025.100916) was dropped from the included list: the full text could not be obtained via any open-access channel identified by OpenAlex and Crossref metadata (PubMed Central, Europe PMC, publisher OA), the publisher site, or the institutional proxy, and the study has been recorded as "Reports not retrieved" in the PRISMA 2020 flow diagram.

### Potential bias from dropping Record #113

The single "report not retrieved" (Record #113, PMID 41218611: "Semaglutide for cognitive dysfunction in major depressive disorder", McIntyre et al. 2026, *Med*) is a recent (2026) MDD pharmacotherapy trial. Its exclusion removes one paper from the depression disorder category (currently ~22% of included studies) and one very recent publication from the 2023-2026 temporal window. Given the small absolute impact (1 of 70 eligible studies = 1.4%), we do not expect this exclusion to materially bias the scoping review's conclusions about EDIA reporting trends. The decision to drop was operational (full text unobtainable through any open-access version identified via OpenAlex and Crossref metadata, the library proxy, or a direct request to the authors), not methodological.

**Net effect on counts:**

| Count | Pre-correction | Post-correction |
|-------|----------------|------------------|
| Records forwarded to full-text review | 129 | 134 |
| Records assessed for eligibility at full text | 129 | 133 (1 not retrieved) |
| Studies included | 65 | **69** |
| Full texts in hand | 64 of 65 | 67 of 69 |
| Pending manual retrieval | 1 (#113) | 2 (#132, #133) |

Affected files have been updated accordingly: `05_screening/SCREENING_COMPLETE.md`, `05_screening/PRISMA_2020_flow_diagram.md`, `05_screening/_README.md`, `03_inclusion_exclusion/_README.md`, `06_data_extraction/_README.md`, `07_full_texts/README.md`, `07_full_texts/ALL_69_LINKS.md` (renamed from `ALL_65_LINKS.md`), and `07_full_texts/PAYWALLED_LINKS.md`.
