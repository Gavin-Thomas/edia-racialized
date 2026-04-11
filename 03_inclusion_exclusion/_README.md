# 03 Inclusion / Exclusion

> Pre-specified eligibility criteria and decision rules used to screen records and adjudicate borderline cases.

## Purpose

This folder holds the formal inclusion and exclusion criteria that operationalize the research question from [`../02_research_question/`](../02_research_question/). The criteria were fixed before screening began and were applied consistently at both title/abstract and full-text stages.

## Files in this folder

| File | Description |
|------|-------------|
| [`criteria.md`](criteria.md) | Full inclusion and exclusion criteria, PROGRESS-Plus operational definitions, date-range justification, English-only scope restriction with planned sensitivity analysis, database-selection rationale, and the revised screening scope (full population, not stratified sample). |

## Inclusion criteria (summary)

- **Design**: Interventional randomized clinical trials (parallel, crossover, factorial, adaptive, pragmatic).
- **Population**: Participants with diagnosed or clinically significant mental disorders (DSM-5, ICD-10/11).
- **Intervention**: Pharmacological intervention explicitly targeting a diagnosed mental disorder.
- **Location**: At least one Canadian recruitment site (listed in the paper's methods, ClinicalTrials.gov / EU CTR / WHO ICTRP registry, or a supplementary site table). Canadian co-authorship or senior authorship alone is NOT sufficient — the trial must have enrolled participants at a Canadian location. Multicentre international trials are eligible only if a Canadian site (or Canadian enrollment data) is explicitly reported.
- **Time**: Main trial results published from 2016 onward.
- **Language**: English.

## Exclusion criteria (summary)

- Observational designs (cohort, case-control, cross-sectional).
- Case reports or small case series (<10 participants).
- Reviews of any kind (systematic, meta-analysis, scoping, narrative).
- Non-pharmacological-only interventions (psychotherapy-only, neurostimulation-only, device-only).
- Trials fully outside Canada with no Canadian recruitment site (Canadian authorship alone does not confer eligibility).
- Laboratory, simulation, animal, methodological trials.
- Protocols, registry-only records, secondary analyses without primary results.
- Conference abstracts without full publication.

## Scope restrictions (important)

- **English-only**: This is a **scope restriction**, not just a limitation. Quebec represents ~23% of Canada's population and a meaningful proportion of Quebec-led RCTs are published primarily in French (e.g., *Santé mentale au Québec*, FRQS-funded work). The restriction introduces systematic geographic and demographic bias toward anglophone Canadian research institutions. A targeted French-language sensitivity search on two disorder categories (depression, substance use) is planned as a supplementary exclusion-rate estimate.
- **API-accessible databases only**: PsycINFO (Ovid) and CINAHL (EBSCOhost) were excluded because they lack programmatic APIs, which would break pipeline reproducibility. For pharmacotherapy RCTs specifically, PsycINFO's marginal yield beyond PubMed/Scopus is modest.

## Decision rule for borderline cases

Where eligibility was ambiguous (typical example: multicentre international trials where Canadian participation is mentioned but not quantified), reviewers were instructed to **promote to full-text review** rather than exclude at title/abstract. Final inclusion was then adjudicated at full text against the same criteria, with a third reviewer consulted if the two primary screeners disagreed.

## Date range (2016-2026)

Aligned with major equity-reporting policy milestones:
- 2015: NIH Policy on Inclusion revision
- 2017: ClinicalTrials.gov race/ethnicity results-reporting requirement
- 2018: TCPS2 revised (Chapters 4 and 9 strengthened)
- 2019: CIHR SGBA+ requirements implemented
- 2020+: Heightened global attention to racial equity in health research
- 2022: CIHR EDI grant requirements strengthened

## How these were applied during screening

- **Title/abstract screening** applied these criteria to all 10,904 eligible records via dual independent review. See [`../05_screening/`](../05_screening/) for batch CSVs, the PRISMA diagram, and inter-rater agreement statistics (97.8% normalized agreement, Cohen's κ=0.39).
- **Full-text screening** applied the same criteria to the 134 records forwarded from title/abstract (129 originally, plus 5 QA-upgraded MAP records retroactively propagated on 2026-04-11 — see [`../05_screening/SCREENING_COMPLETE.md`](../05_screening/SCREENING_COMPLETE.md) → "Retroactive Correction"). Final included set: **69 studies** (67 full text obtained, 2 pending manual retrieval; Record #113 dropped as unobtainable and recorded as "Reports not retrieved" in the PRISMA flow).
- **Original vs. actual screening scope**: the original protocol specified a stratified random sample of 200 records (rapid-review methodology, Garritty et al. 2021); the actual implementation screened the full eligible population of 10,904 via dual independent review. The n=200 stratified sample (seed 42) was retained as a pilot calibration set.

## Outputs

- Operationalized criteria used directly in [`../05_screening/`](../05_screening/).
- PROGRESS-Plus variable list reused in [`../06_data_extraction/extraction_codebook.md`](../06_data_extraction/extraction_codebook.md).

## Links

- Previous stage: [`../02_research_question/`](../02_research_question/)
- Next stage: [`../04_database_search/`](../04_database_search/)
- Screening application: [`../05_screening/`](../05_screening/)
- Extraction codebook: [`../06_data_extraction/extraction_codebook.md`](../06_data_extraction/extraction_codebook.md)
