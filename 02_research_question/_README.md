# 02 Research Question

> Formalization of the scoping review question using the PCC framework (Population, Concept, Context) per JBI scoping review methodology.

## Purpose

This folder holds the formalized research question and objectives for the scoping review. It translates the landscape gaps identified in [`../01_literature_search/`](../01_literature_search/) into a specific, answerable question using the PCC framework and articulates the primary and secondary objectives that guide every downstream stage (inclusion criteria, search strategy, data extraction).

## Files in this folder

| File | Description |
|------|-------------|
| [`research_question.md`](research_question.md) | Full research question, PCC breakdown, primary/secondary objectives, temporal-comparison analysis plan, sensitivity-analysis cutpoints, and terminology (racialized groups vs. Indigenous peoples). |

## Research question

> Among randomized controlled trials conducted in Canada evaluating pharmacological interventions to prevent, treat, or manage diagnosed mental disorders (2016-2026), what is the representation and reporting of EDIA-related metrics — with a focus on racialized groups — among participants, and how does representation vary across trials and disorders?

## PCC summary

| Element | Specification |
|---------|---------------|
| **P**opulation | RCTs evaluating pharmacological interventions for DSM-5/ICD-10 mental disorders with at least one verified Canadian recruitment site, published 2016-2026 in English |
| **C**oncept | EDIA reporting practices as defined by the PROGRESS-Plus framework — specifically race/ethnicity representation, sex/gender distinction, Indigenous participation and governance, and CONSORT-Equity compliance |
| **C**ontext | Canadian clinical trial infrastructure, benchmarked against Statistics Canada Census 2021 and compared across disorder categories, time periods (pre/post-2020), and trial characteristics (funder, multisite/single-site, sample size) |

## Objectives

**Primary**
1. Proportion of trials reporting participant race/ethnicity and the completeness/granularity of reporting.
2. Representation of racialized groups relative to Canadian population benchmarks (Statistics Canada Census 2021).
3. Trial-level factors associated with adequate vs. underrepresentation.

**Secondary**
1. How race/ethnicity is incorporated into trial design/analysis (descriptive / covariate / subgroup).
2. Reporting of other PROGRESS-Plus variables (sex/gender distinction, SES, education, Indigenous participation, disability, SOGI).
3. Whether Indigenous peoples' participation is reported distinctly from racialized groups (TCPS2/OCAP reference).
4. Pre/post-2020 temporal comparison with sensitivity cutpoints at **2018** (TCPS2 revision) and **2022** (CIHR EDI tightening).
5. Structural barriers/enablers to recruiting racialized groups as reported by trial authors.

## Key decisions / rationale

- **Racialized groups as primary framing** (not "race/ethnicity"): aligns with Canadian equity-research norms and the *Employment Equity Act* definition of visible minorities. "Race/ethnicity" is used only when reporting what individual trials themselves used.
- **Separate Indigenous analysis**: First Nations, Inuit, and Metis participation is analyzed under a distinct framework of self-determination and data sovereignty (TCPS2 Chapter 9, OCAP principles). Indigenous peoples are not subsumed under "racialized groups."
- **Temporal-comparison design**: the pre/post-2020 window is unequal (4 years vs. 6-7 years), so comparisons must be reported as proportions within each period, never absolute counts. Sensitivity analyses at 2018 and 2022 test robustness of the temporal signal.
- **Interrupted time series** (aspirational): with all 10,904 eligible records now screened, segmented regression may be feasible if the included sample (n=69) supports it.

## Outputs

This stage produces the operational inputs consumed downstream:

- The PCC framework and objectives are operationalized into inclusion/exclusion rules in [`../03_inclusion_exclusion/criteria.md`](../03_inclusion_exclusion/criteria.md).
- The PROGRESS-Plus variable list drives both the search-strategy concept blocks ([`../04_database_search/search_strategy.md`](../04_database_search/search_strategy.md)) and the data-extraction fields ([`../06_data_extraction/extraction_codebook.md`](../06_data_extraction/extraction_codebook.md)).
- The temporal-comparison design determines the year variable and sensitivity-analysis plan used at the analysis stage.

## Links

- Previous stage: [`../01_literature_search/`](../01_literature_search/)
- Next stage: [`../03_inclusion_exclusion/`](../03_inclusion_exclusion/)
- Downstream extraction codebook: [`../06_data_extraction/extraction_codebook.md`](../06_data_extraction/extraction_codebook.md)
