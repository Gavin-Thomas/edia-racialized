# 06 Data Extraction

> PROGRESS-Plus data-extraction codebook and coding rules for the 69 included studies.

## Status

**NOT STARTED** (as of 2026-04-07, updated 2026-04-11). This folder currently contains only the extraction codebook. No extracted data yet exist. Extraction will begin once full-text PDFs for all **69 included studies** are finalized in [`../07_full_texts/`](../07_full_texts/). As of the latest project snapshot (2026-04-11), **67 of 69** full texts have been retrieved; 2 remain pending manual retrieval (Record #132 PRC-063 methylphenidate adolescent ADHD, and Record #133 MIRAGE mirtazapine for chronic insomnia). The former Record #113 (Semaglutide MDD) has been dropped from the included list as unobtainable — see [`../05_screening/SCREENING_COMPLETE.md`](../05_screening/SCREENING_COMPLETE.md) → "Retroactive Correction (2026-04-11)".

## Purpose

This folder holds the data-extraction template and coding rules that operationalize the PROGRESS-Plus framework for the 69 included studies. Its goal is to produce a clean, dual-reviewed, publication-ready dataset capturing the completeness and granularity of EDIA reporting for each included trial.

## Files in this folder

| File | Description |
|------|-------------|
| [`extraction_codebook.md`](extraction_codebook.md) | Full codebook: variable definitions, decision rules, Indigenous-specific fields (TCPS2/OCAP), trial-level covariates, benchmarking framework (Statistics Canada Census 2021), coding process, and the kappa-reporting plan. |

## Framework

**PROGRESS-Plus** (Place, Race/ethnicity, Occupation, Gender/sex, Religion, Education, Socioeconomic status, Social capital, + Age, Disability, SOGI, Intersectionality) — supplemented with **CONSORT-Equity** (Welch et al., *BMJ* 2017) as a reporting-quality benchmark.

## Variable groups

### Primary variables (central to the research question)

- `race_reported` (Yes / Partial / No)
- `race_categories` (verbatim from the paper)
- `race_framework` (US-derived / Canadian Census / Self-identified / Other / Not stated)
- `race_granularity` (Granular 14+ / Moderate 5-13 / Coarse 2-4 / Binary / Aggregate-only)
- `race_subgroup_analysis` (Yes / No)
- `race_as_variable` (Covariate / Stratification / Subgroup / Descriptive / Not used)
- `race_social_construct` (Yes / No)
- `race_crosswalk` (mapping of trial categories to Statistics Canada visible-minority taxonomy)

### Secondary PROGRESS-Plus variables

Sex vs. gender (distinguished), Indigenous participation (with a distinct field block), age, SES indicators, place of residence, education, religion, social capital, disability, sexual orientation and gender identity (SOGI), intersectional analysis.

### Indigenous-specific variables (TCPS2 Chapter 9 / OCAP)

Participation, groups named (First Nations / Inuit / Metis / Multiple), separate reporting, community partnership, data-ownership description, named governance body, and a 4-level ordinal **data-sovereignty** field (0 = no mention → 3 = full governance described).

### Trial-level covariates

PMID, DOI, first author, year, journal, disorder category, intervention/comparator, sample size, trial design, multisite flag, international flag, number and naming of Canadian sites, funder, registration ID, citation count, citations per year.

## Coding process

1. **Dual independent extraction** by two reviewers for every included trial.
2. **Pilot calibration** on the first 30 trials (increased from 20 per CONSORT-Equity recommendation, Welch et al. 2017).
3. **Inter-rater agreement** calculated per field; target **Cohen's κ ≥ 0.80** before proceeding to full extraction.
4. **Disagreement resolution** by consensus; third reviewer consulted if unresolved.
5. **Kappa reporting**: overall kappa plus category-specific agreement for skewed fields (e.g., `race_reported`, `indigenous_participation`), and **weighted kappa** for the ordinal `indigenous_data_sovereignty` field. Rationale: skewed marginal distributions inflate overall kappa via chance agreement (Viera & Garrett, *AFP* 2005).

## Benchmarking framework

Trial demographics are compared to Canadian population benchmarks at the field level (aggregated across trials), not per-trial pass/fail:

| Benchmark | Source |
|-----------|--------|
| Visible minority status (national + provincial) | Statistics Canada Census 2021, Table 98-10-0347-01 |
| Indigenous identity (national + provincial) | Statistics Canada Census 2021, Table 98-10-0266-01 |
| Mental health service utilization by demographic group | CCHS Mental Health Component |
| Inpatient mental health demographics | CIHI Hospital Mental Health Database |

## Outputs (planned)

| File | Purpose | Status |
|------|---------|--------|
| `extracted_data.csv` | Dual-reviewed, consensus-reconciled extraction of all 69 included studies across every PROGRESS-Plus and trial-level field | **Not yet created** |
| `extraction_kappa.md` | Field-level agreement statistics computed on the pilot calibration (first 30 trials) | Not yet created |
| `benchmark_crosswalk.csv` | Mapping of trial-reported race/ethnicity categories to Statistics Canada visible-minority taxonomy | Not yet created |

## Links

- Codebook: [`extraction_codebook.md`](extraction_codebook.md)
- Included full texts: [`../07_full_texts/`](../07_full_texts/)
- Screening results that produced the included set: [`../05_screening/SCREENING_COMPLETE.md`](../05_screening/SCREENING_COMPLETE.md)
- Research question driving variable selection: [`../02_research_question/research_question.md`](../02_research_question/research_question.md)
- CONSORT-Equity reference: Welch VA et al. *BMJ* 2017;359:j5085.
