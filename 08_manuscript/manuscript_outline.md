# Manuscript Outline — PRISMA-ScR Format

**Working title:** Equity, Diversity, Inclusion, and Accessibility Reporting in Canadian Mental Health Pharmacotherapy Randomized Controlled Trials (2016-2026): A Scoping Review Using the PROGRESS-Plus Framework

**Target journals (in order of fit):**
1. BMJ Open
2. CMAJ Open
3. Canadian Journal of Psychiatry
4. Systematic Reviews

**Reporting guideline:** PRISMA-ScR (PRISMA Extension for Scoping Reviews)

---

## Title Page

- Title (as above)
- Authors: Gavin Thomas (University of Calgary Cumming School of Medicine) + collaborators
- Corresponding author
- Word count target: 3,500-4,500 (main text)
- Keywords: scoping review, equity, diversity, inclusion, PROGRESS-Plus, randomized controlled trial, mental health, pharmacotherapy, Canada, CONSORT-Equity, racialized groups, Indigenous

---

## Abstract (structured, ~350 words)

### Objective
To characterize the representation and reporting of equity, diversity, inclusion, and accessibility (EDIA) metrics in Canadian mental health pharmacotherapy RCTs published 2016-2026, with a focus on racialized groups and Indigenous peoples.

### Design
Scoping review following PRISMA-ScR guidelines.

### Data sources
PubMed, Europe PMC, Scopus, OpenAlex (searched March 2026).

### Eligibility criteria
Interventional RCTs of pharmacological agents targeting DSM-5/ICD-10 mental disorders, with at least one verified Canadian recruitment site, published 2016-2026 in English.

### Data extraction
PROGRESS-Plus framework (Place, Race/Ethnicity, Occupation, Gender/Sex, Religion, Education, Socioeconomic Status, Social Capital, plus Age, Disability, SOGI, Intersectionality). Indigenous-specific variables coded per TCPS2/OCAP principles. Dual extraction with Cohen's kappa > 0.86 for all key fields.

### Results
- 63 trials included (N=8,837 participants)
- Race/ethnicity reported in 57.1% of trials (36/63)
- Sex and gender explicitly distinguished in 6.3% (4/63)
- SOGI data in 3.2% (2/63)
- Indigenous participation documented in 11.1% (7/63), with 0% referencing OCAP principles
- Intersectional analysis: 0/63
- No trial achieved full CONSORT-Equity compliance

### Conclusions
Substantial gaps persist in EDIA reporting in Canadian mental health pharmacotherapy trials. [1-2 sentences on implications]

---

## 1. Introduction (~600 words)

### 1.1 Background
- Health equity in clinical research as a global priority
- Canada-specific policy landscape: CIHR SGBA+ (2019), TCPS2 Chapter 9 (2018), CIHR EDI requirements (2022)
- Known gaps in race/ethnicity reporting in clinical trials internationally (cite: Weng et al., 2021; Oh et al., 2015)
- Unique Canadian context: visible minority taxonomy (Statistics Canada), Indigenous self-determination framework (OCAP), francophone populations

### 1.2 Rationale
- No scoping review has systematically assessed PROGRESS-Plus EDIA reporting in Canadian mental health pharmacotherapy RCTs
- Previous reviews focused on US (NIH mandate-driven) or global samples — Canadian-specific data needed
- Pharmacotherapy trials specifically relevant because of known racial/ethnic differences in drug metabolism, dosing, and adverse effects

### 1.3 Objectives
Primary:
1. Determine the proportion of trials reporting participant race/ethnicity and characterize reporting completeness/granularity
2. Quantify the representation of racialized groups relative to Statistics Canada Census 2021 benchmarks
3. Identify trial-level factors associated with adequate vs. underrepresentation

Secondary:
1. Assess how race/ethnicity is incorporated into trial design/analysis
2. Characterize reporting of other PROGRESS-Plus variables
3. Evaluate Indigenous participation reporting and OCAP principles
4. Compare EDIA reporting pre-2020 vs. post-2020

---

## 2. Methods (~800 words)

### 2.1 Protocol and registration
- Not pre-registered (compensated by full code availability and transparent methodology)
- Protocol available at: [GitHub repo]
- PRISMA-ScR checklist in Supplementary Table S1

### 2.2 Eligibility criteria
- Inclusion: interventional RCTs, DSM-5/ICD-10 mental disorders, pharmacological interventions, verified Canadian recruitment site, 2016-2026, English
- Exclusion: observational studies, non-pharmacological only, no Canadian recruitment site, secondary analyses, protocols
- Key criterion refinement: simplified from "Canadian PI leadership" to "verified Canadian recruitment site" (2026-04-11) — documented with rationale

### 2.3 Information sources and search strategy
- 4 databases: PubMed, Europe PMC, Scopus, OpenAlex
- Search concepts: Mental Disorders AND RCT AND Canada
- EDIA terms intentionally excluded from search to avoid bias toward already-reporting trials
- Full search strategies in Supplementary Table S2
- All search code available: Python 3.11+, standard library only

### 2.4 Selection of sources of evidence
- Title/abstract screening: 10,904 records, dual independent review
- Cohen's kappa = 0.39 (fair; caveat: 96% exclusion base rate inflates percent agreement)
- Full-text screening: 134 records assessed, 63 included
- Codex GPT-5.4 false-negative validation: 0 false negatives across ~5,900 OUT_OF_SCOPE records

### 2.5 Data charting process
- PROGRESS-Plus framework with 50+ variables per study
- Extraction codebook with decision rules (Supplementary File S3)
- AI-assisted extraction by LLM agents with human QA
- Pass 2 QC: 20/63 records (32%) independently re-extracted; Cohen's kappa 0.86-1.00 for 4 key fields
- **QC coverage limitation:** The extraction codebook specifies 7 fields for inter-rater reliability testing. Pass 2 QC assessed 4 of these 7 fields (race_reported, sex_gender_distinguished, indigenous_participation, education_reported). Three fields were not independently verified: indigenous_data_sovereignty, ses_reported, and consort_equity_compliant. The 4 tested fields include the primary outcome (race_reported) and two high-priority secondary variables. The untested fields have lower expected variance (indigenous_data_sovereignty is 0 for all 63 included studies; ses_reported and consort_equity_compliant have straightforward coding rules). This partial coverage is acknowledged as a limitation.

### 2.6 Data items
- Trial-level covariates: PMID, year, journal, disorder category, intervention, sample size, design, sites, funder, registration
- PROGRESS-Plus variables (list all with codebook definitions in supplement)
- Indigenous-specific variables: participation, group naming, OCAP, data sovereignty (0-3 ordinal)
- CONSORT-Equity compliance (Yes/Partial/No)

### 2.7 Synthesis of results
- Descriptive statistics: counts and proportions for each PROGRESS-Plus variable
- Temporal comparison: pre-2020 vs. post-2020 (with sensitivity at 2018 TCPS2 and 2022 CIHR EDI cutpoints)
- Benchmarking: race/ethnicity data compared to Statistics Canada Census 2021 visible minority taxonomy
- No meta-analysis (scoping review)

---

## 3. Results (~1,200 words)

### 3.1 Selection of sources of evidence
- PRISMA-ScR flow diagram (Figure 1)
- 54,483 raw records -> 39,986 unique -> 10,904 eligible -> 134 full-text assessed -> 63 included

### 3.2 Characteristics of included trials
- Table 1: trial characteristics (year, journal, disorder category, design, sample size, sites, funder)
- 63 trials, N=8,837 participants
- Median sample size 60 (range 6-785)
- 60.6% multisite, 40.9% international
- Disorder categories: Depression (largest), Bipolar-Mood, Substance Use, Psychotic, Dementia, ADHD, Other

### 3.3 Race/ethnicity reporting (PRIMARY OUTCOME)
- **36/63 (57.1%) reported race/ethnicity**
- Race framework: US-derived (32% of reporters), Canadian Census (5%), Self-identified (varies), Not stated (39%)
- Race granularity: Binary/single-category (weakest) to 10-category (strongest)
- Race used analytically: 4.5% conducted subgroup analyses, 6.1% used as covariate
- 0% acknowledged race as a social construct
- 2 trials collected race/ethnicity but did not report it
- 1 pharmacogenomics trial did not collect race despite known population-level genetic variation

### 3.4 Sex and gender reporting
- Sex reported: 95.2% (60/63)
- Gender reported: 14.3% (9/63)
- **Sex/gender distinguished: 6.3%** (4/63, all published 2022-2025)
- Sex subgroup analysis: 12.7% (8/63)

### 3.5 Other PROGRESS-Plus variables
- Table 2: PROGRESS-Plus reporting rates (all variables)
- Education: 34.9% (22/63)
- SES/income: 28.6% (18/63)
- Employment/occupation: 14.3% (9/63)
- Disability: 41.3% (26/63)
- Religion: **0/63**
- Social capital: **3.2% (2/63)**
- SOGI: **3.2% (2/63)**
- Intersectional analysis: **0/63**

### 3.6 Indigenous participation
- Documented in 11.1% (7/63 trials)
- Highest: OPTIMA trial (First Nations 16.9%, Metis 4.8%)
- Groups specifically named in only 2 trials
- **0% described OCAP principles or any Indigenous governance framework**
- **0% reported Indigenous outcomes separately**
- No trial was designed with/for Indigenous communities

### 3.7 CONSORT-Equity compliance
- Full compliance: 0/63
- Partial: 27.0% (17/63)
- None: 73.0% (46/63)

### 3.8 Funder patterns
- Table 3: EDIA reporting by funder type
- **31% of CIHR-funded trials** did not report race/ethnicity (5/16 CIHR-funded trials lack race reporting)
- NIH-funded trials more consistently reported race (driven by NIH inclusion policy)
- Industry-funded trials varied widely

---

## 4. Discussion (~1,000 words)

### 4.1 Summary of evidence
- Canadian mental health pharmacotherapy RCTs have substantial EDIA reporting gaps
- Race/ethnicity absent in >40% of trials
- Sex/gender conflated in >90%
- Intersectional analysis completely absent
- Indigenous governance absent despite documented participation

### 4.2 Comparison with existing literature
- Compare to US (Weng et al., Pub Med race reporting ~70-80% post-NIH mandate)
- Compare to global reviews (Oh et al., 2015; Khan et al., 2022)
- Canada-specific: lower race reporting than US, reflecting lack of mandatory reporting

### 4.3 Canadian policy implications
- CIHR SGBA+ (2019) has not translated to race reporting in trials
- TCPS2 Chapter 9 not operationalized — OCAP principles absent
- Recommendation: CIHR should mandate PROGRESS-Plus minimum reporting for funded trials
- Recommendation: Canadian trial registries should require demographic data fields

### 4.4 The sex/gender distinction
- 94% of trials conflate sex and gender
- Only post-2022 trials beginning to distinguish (temporal signal)
- CIHR SGBA+ specifically calls for this distinction — not being implemented

### 4.5 Indigenous data sovereignty
- 11.1% document Indigenous participation, 0% address OCAP
- The SALOME trial (30% Aboriginal) and OPTIMA trial (21.7% First Nations/Metis) serve highly Indigenous populations without Indigenous governance
- This is a gap in CIHR-funded research ethics, not just reporting

### 4.6 Limitations
1. English-language only (Quebec ~23% of Canada's population; francophone trials excluded)
2. Four API-accessible databases only (PsycINFO/CINAHL excluded for reproducibility)
3. AI-assisted screening and extraction (methodology disclosed, kappa reported)
4. Not pre-registered
5. Cohen's kappa for screening = 0.39 (fair; base rate caveat)
6. Temporal comparison windows unequal (pre-2020: 4 years; post-2020: 6-7 years)

---

## 5. Conclusions (~200 words)

- Substantial EDIA reporting gaps in Canadian mental health pharmacotherapy RCTs
- Intersectional analysis absent; religion absent; SOGI near-absent
- Indigenous governance absent despite documented participation
- Policy action needed: mandatory PROGRESS-Plus minimum reporting for CIHR-funded trials
- This review provides a baseline for monitoring improvements following policy changes

---

## Tables and Figures

### Figure 1: PRISMA-ScR flow diagram
(Already drafted in `05_screening/PRISMA_2020_flow_diagram.md`)

### Table 1: Characteristics of included trials (N=63)
Year, journal, disorder category, design, sample size, sites, international, funder

### Table 2: PROGRESS-Plus reporting rates
All variables with n (%) and 95% CI

### Table 3: Race/ethnicity reporting by funder type
CIHR vs NIH vs Industry vs Foundation vs Other

### Table 4: Indigenous participation and OCAP indicators
Per-study detail for 7 trials with documented Indigenous participation

### Supplementary materials
- S1: PRISMA-ScR checklist
- S2: Full search strategies for all 4 databases
- S3: Extraction codebook
- S4: Per-study extraction data (full CSV)
- S5: Pass 2 QC methodology and kappa statistics
- S6: Flagged records and resolution decisions

---

*Outline created 2026-04-13. Statistics updated 2026-04-13 to reflect 63-study final included set (Records #4, #12, #45 excluded). Based on extraction_summary.md and CHANGELOG.md.*
