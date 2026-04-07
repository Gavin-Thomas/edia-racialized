# Data Extraction Codebook

## EDIA Reporting in Canadian Mental Health Pharmacotherapy RCTs

### Purpose
This codebook operationalizes the PROGRESS-Plus framework for extracting equity, diversity, inclusion, and accessibility (EDIA) reporting data from included randomized controlled trials. It provides decision rules for coding completeness, granularity, and quality of reporting for each variable.

---

## Key Definitions

### Racialized Groups
In this review, "racialized groups" refers to people who experience racialization — the social process by which racial meaning is ascribed to groups, creating hierarchies of difference. Race is understood as a **social construct** reflecting systems of power and categorization, not a biological variable.

In the Canadian context:
- **Racialized persons** includes those identified as visible minorities under the *Employment Equity Act* (i.e., non-Caucasian in race or non-white in colour, excluding Indigenous peoples)
- **Indigenous peoples** (First Nations, Inuit, and Metis) are discussed under a **distinct framework** of self-determination, sovereignty, and reconciliation — not subsumed under "racialized"
- This review extracts data on both racialized groups and Indigenous peoples, but analyzes them separately, consistent with CIHR and TCPS2 guidance

**Terminology note — "visible minority":** This term is used in extraction fields where it preserves fidelity to (a) trial-reported categories and (b) Statistics Canada benchmarking definitions under the *Employment Equity Act*. The term is contested: Statistics Canada (2022 consultation with the Commission on Official Languages) has proposed replacing "visible minority" with "racialized person" or "racialized group" in future census instruments. This review uses "racialized groups" as its primary term throughout, reserving "visible minority" only where Canadian legal/statistical definitions are directly invoked. When trials themselves use "visible minority," code `race_categories` verbatim and note this in `race_notes`.

### Adequate Reporting
A trial is coded as having "adequate" EDIA reporting for a given variable when:
1. The variable is explicitly named and defined
2. Participant-level data are presented (counts or proportions)
3. Categories are sufficiently granular (not just "White/non-White")

### Partial Reporting
A trial reports a variable partially when data are mentioned but:
- Only in aggregate (e.g., "diverse sample" without numbers)
- Using overly broad categories
- Reported at baseline but not in results

---

## PROGRESS-Plus Variables

### P — Place of Residence

| Field | Description |
|-------|-------------|
| `place_reported` | Yes / Partial / No |
| `place_detail` | Categories used (urban/rural/remote/Northern, province, postal code, etc.) |
| `place_notes` | Free text |

**Decision rules:**
- "Yes" = geographic distribution of participants reported with counts
- "Partial" = general statement (e.g., "urban academic centre") without participant-level data
- "No" = no geographic information about participants

### R — Race/Ethnicity/Racialization

| Field | Description |
|-------|-------------|
| `race_reported` | Yes / Partial / No |
| `race_categories` | Exact categories used (copy verbatim from paper) |
| `race_n_groups` | Number of racial/ethnic categories reported |
| `race_framework` | US-derived / Canadian Census / Self-identified / Other / Not stated |
| `race_granularity` | Granular (14+ groups, matching Statistics Canada visible minority taxonomy) / Moderate (5–13 groups) / Coarse (2–4 groups) / Binary (White/non-White) / Aggregate only |
| `race_subgroup_analysis` | Yes / No — were racial/ethnic subgroups analyzed for treatment effects? |
| `race_as_variable` | Covariate / Stratification / Subgroup / Descriptive only / Not used |
| `race_social_construct` | Yes / No — does the paper acknowledge race as a social construct? |
| `race_crosswalk` | Free text — mapping of trial-reported categories to Statistics Canada visible minority taxonomy for benchmarking (e.g., "Asian → South Asian + East Asian + Southeast Asian") |
| `race_notes` | Free text |

**Decision rules:**
- "Yes" = participant race/ethnicity reported with counts per category
- "Partial" = mentioned but no counts (e.g., "predominantly White") or only % without n
- "No" = no mention of race, ethnicity, or racialization
- Record **exact categories** as stated in the paper (do not reclassify)

**Granularity reference — Statistics Canada visible minority taxonomy (Census 2021):**
South Asian, Chinese, Black, Filipino, Arab, Latin American, Southeast Asian, West Asian, Korean, Japanese, Visible minority n.i.e., Multiple visible minorities. These 12 named groups + "Not a visible minority" + "Total" = 14 categories. Trials that report all named groups (or an equivalent level of specificity) are coded "Granular". See Statistics Canada Table 98-10-0347-01 for the full taxonomy.

**Note on US vs. Canadian frameworks:** Many included trials will report race/ethnicity using US OMB categories (White / Black or African American / Asian / American Indian or Alaska Native / Native Hawaiian or Pacific Islander / Other). Code `race_framework = "US-derived"` for these. Add a `race_crosswalk` free-text field noting which Statistics Canada categories the reported groups map to, to enable benchmarking.

### O — Occupation/Employment

| Field | Description |
|-------|-------------|
| `occupation_reported` | Yes / Partial / No |
| `occupation_detail` | Categories used |

### G — Gender/Sex

| Field | Description |
|-------|-------------|
| `sex_reported` | Yes / Partial / No |
| `sex_categories` | Categories used (Male/Female, M/F/Other, etc.) |
| `gender_reported` | Yes / Partial / No |
| `gender_categories` | Categories used (Man/Woman/Non-binary, etc.) |
| `sex_gender_distinguished` | Yes / No — does the paper distinguish sex from gender? |
| `sex_subgroup_analysis` | Yes / No |

**Decision rules:**
- Code sex and gender separately
- "Yes" for sex = biological sex reported with counts
- "Yes" for gender = gender identity reported with counts
- If paper uses "gender" but reports M/F only, code sex=Yes, gender=No, sex_gender_distinguished=No

### R — Religion/Culture

| Field | Description |
|-------|-------------|
| `religion_reported` | Yes / Partial / No |
| `religion_detail` | Categories used |

### E — Education

| Field | Description |
|-------|-------------|
| `education_reported` | Yes / Partial / No |
| `education_detail` | Categories used |

### S — Socioeconomic Status (SES)

| Field | Description |
|-------|-------------|
| `ses_reported` | Yes / Partial / No |
| `ses_indicators` | Income / Insurance / Housing / Deprivation index / Other |
| `ses_detail` | Categories used |

### S — Social Capital/Support

| Field | Description |
|-------|-------------|
| `social_capital_reported` | Yes / Partial / No |
| `social_capital_detail` | Measures used |

---

## PROGRESS "Plus" Variables

### Age

| Field | Description |
|-------|-------------|
| `age_reported` | Yes / Partial / No |
| `age_detail` | Mean/SD, range, categories |
| `age_subgroup_analysis` | Yes / No |

### Disability

| Field | Description |
|-------|-------------|
| `disability_reported` | Yes / Partial / No |
| `disability_type` | Physical / Intellectual / Sensory / Other |
| `disability_notes` | Free text |

### Sexual Orientation and Gender Identity (SOGI)

| Field | Description |
|-------|-------------|
| `sogi_reported` | Yes / Partial / No |
| `sogi_categories` | Categories used (2SLGBTQ+, heterosexual/homosexual/bisexual, etc.) |
| `sogi_notes` | Free text |

### Intersectionality

| Field | Description |
|-------|-------------|
| `intersectional_analysis` | Yes / No |
| `intersectional_detail` | Which variables were cross-tabulated (e.g., race x gender x SES) |

---

## Indigenous-Specific Variables

Consistent with TCPS2 Chapter 9 and OCAP (Ownership, Control, Access, Possession) principles. These fields are coded for **ALL** included trials, not just those with Indigenous participants. "Not reported" means Indigenous participation status is unknown (distinct from "No" = explicitly stated as none).

### Participation and Design

| Field | Description |
|-------|-------------|
| `indigenous_participation` | Yes / No / Not reported |
| `indigenous_groups_named` | First Nations / Inuit / Metis / Multiple / Not specified (select all that apply) |
| `indigenous_specific_trial` | Yes / No — was the trial designed specifically for/with Indigenous communities? |
| `indigenous_separate_reporting` | Yes / No — were Indigenous participant outcomes reported separately from racialized group data? |

### OCAP Principles — Control & Access

| Field | Description |
|-------|-------------|
| `indigenous_partnership` | Yes / No — explicit evidence of community partnership, community advisory board, or CBPR/CPAR approach |
| `indigenous_partnership_detail` | Free text — name the community body, council, or organization involved if stated |

### OCAP Principles — Ownership & Possession

| Field | Description |
|-------|-------------|
| `indigenous_data_ownership` | Yes / No — was the data ownership structure explicitly described (i.e., who holds rights to the data)? |
| `indigenous_governance_body` | Yes / No — was a named Indigenous governance body involved in data oversight or protocol approval? |

### Data Sovereignty (4-level ordinal)

| Field | Description |
|-------|-------------|
| `indigenous_data_sovereignty` | 0 = No mention / 1 = Statement only (e.g., brief data-sharing note) / 2 = Protocol referenced (e.g., OCAP, FNIGC data governance cited) / 3 = Full governance described (band council approval, data governance agreement, community benefit agreement documented) |
| `indigenous_data_sovereignty_detail` | Free text — describe the specific governance arrangement if coded 2 or 3 |

### General

| Field | Description |
|-------|-------------|
| `indigenous_notes` | Free text — any additional observations about Indigenous participation or data practices |

---

## Trial-Level Covariates

| Field | Description |
|-------|-------------|
| `pmid` | PubMed ID |
| `doi` | Digital Object Identifier |
| `first_author` | Last name of first author |
| `year` | Publication year |
| `journal` | Journal name |
| `disorder_category` | Depression / Anxiety-Trauma-OCD / Psychotic / Bipolar-Mood / Substance Use / ADHD / Dementia / Eating Disorder / Other |
| `intervention` | Drug name(s) and class |
| `comparator` | Placebo / Active comparator / Usual care |
| `sample_size` | Total N randomized |
| `trial_design` | Parallel / Crossover / Factorial / Adaptive / Other |
| `multisite` | Yes / No |
| `international` | Yes / No — sites in countries other than Canada |
| `canadian_sites_n` | Number of Canadian sites (if reported) |
| `canadian_sites_named` | City/province of Canadian sites |
| `funder` | Industry / CIHR / NIH / Other government / Foundation / Not reported |
| `registration` | ClinicalTrials.gov ID or other registry |
| `consent_language` | Languages of consent/study materials (if reported) |
| `cited_by_count` | Scopus citation count at time of search |
| `citations_per_year` | Normalized citation rate |

---

## Benchmarking Framework

Trial demographics will be compared to Canadian population benchmarks:

| Benchmark Source | Variables | Level |
|-----------------|-----------|-------|
| Statistics Canada Census 2021 (Table 98-10-0347-01) | Visible minority status | National + provincial |
| Statistics Canada Census 2021 (Table 98-10-0266-01) | Indigenous identity | National + provincial |
| CCHS Mental Health Component | Mental health service utilization by demographic group | National |
| CIHI Hospital Mental Health Database | Inpatient mental health demographics | Provincial |

**Benchmarking approach:**
- Compare at the **field level** (aggregate across all included trials), not per-trial pass/fail
- Use **provincial-level** benchmarks matched to trial site locations where possible
- Adjust for **disease-specific prevalence** using CCHS data where available
- Develop a **crosswalk table** mapping trial-reported categories to Census categories

---

## Coding Process

1. Two independent reviewers extract data from each included trial
2. Pilot calibration on **first 30 trials** (increased from 20; per CONSORT-Equity recommendation, Welch et al., *BMJ* 2019); calculate inter-rater agreement for key fields listed below
3. Resolve disagreements by consensus; involve third reviewer if unresolved
4. Target **kappa > 0.80** before proceeding to full extraction

**Kappa reporting requirements:**

| Field | Reporting requirement |
|-------|----------------------|
| `race_reported` | Overall kappa + category-specific agreement (% for Yes / Partial / No separately) |
| `race_granularity` | Overall kappa |
| `race_framework` | Overall kappa |
| `gender_reported` | Overall kappa |
| `sex_gender_distinguished` | Overall kappa |
| `indigenous_participation` | Overall kappa + category-specific for Yes / No / Not reported |
| `indigenous_data_sovereignty` | Weighted kappa (ordinal 0–3 scale) |

Rationale: Race/ethnicity and Indigenous participation fields have highly skewed marginal distributions (most trials will score "No" or "Partial"). Chance agreement inflates overall kappa in such cases; category-specific agreement prevents this artefact (Viera & Garrett, *American Family Physician* 2005).

**CONSORT-Equity alignment:**
This review uses CONSORT-Equity (Welch et al., *BMJ* 2019) as a supplementary reporting quality benchmark. For each included trial, code `consort_equity_compliant` (Yes / Partial / No) based on whether the trial reports:
- Sociodemographic characteristics of randomized participants (Item 15 extension)
- Equity-relevant subgroup analyses (Item 18 extension)
- Generalizability discussion with reference to equity (Item 21 extension)

| Field | Description |
|-------|-------------|
| `consort_equity_compliant` | Yes (all 3 items) / Partial (1–2 items) / No (0 items) |
| `consort_equity_notes` | Which specific items were present |

---

## Date Range Justification (2016-2026)

The 10-year window was selected based on the following policy milestones:

- **2015**: NIH Policy on Inclusion of Women and Minorities revised, strengthening requirements for demographic reporting in clinical trials
- **2016**: CONSORT 2010 extensions widely adopted; CONSORT-Equity extension in development
- **2017**: ClinicalTrials.gov began requiring race/ethnicity in results reporting
- **2018**: TCPS2 (Tri-Council Policy Statement) revised with strengthened Chapter 9 on Indigenous research and Chapter 4 on equity
- **2019**: CIHR Sex and Gender-Based Analysis Plus (SGBA+) requirements implemented for all funded research
- **2020+**: Heightened global attention to racial equity in health research following anti-Black racism reckoning
- **2022**: CIHR EDI requirements for grant applications strengthened

This window captures the period of most significant policy change in Canadian and international equity reporting standards. It ensures findings reflect current practice rather than historical norms.
