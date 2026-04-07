# Next Session Prompt — Full-Text Screening & Data Extraction

Copy everything below this line into a new Claude Code chat:

---

## Project Context

I'm running a scoping review on EDIA (Equity, Diversity, Inclusion, Accessibility) reporting in Canadian mental health pharmacotherapy RCTs (2016-2026). Title/abstract screening is 100% complete. I need to move to full-text screening and then data extraction.

## Key Files

Read these files first to understand the project:

1. `ACADEMIC_REVIEW.md` — full academic critique and methodology overview
2. `05_screening/PRISMA_2020_flow_diagram.md` — PRISMA flow with all numbers
3. `05_screening/fulltext_screening_decisions.csv` — **129 records for full-text review** (36 MAP + 93 UNCERTAIN), each with Reviewer 1 decision, Reviewer 2 decision, reasoning, and arbiter notes
4. `05_data_extraction/extraction_codebook.md` — PROGRESS-Plus coding manual for data extraction
5. `03_inclusion_exclusion/criteria.md` — inclusion/exclusion criteria
6. `02_research_question/research_question.md` — PICO framework and objectives

## What Needs to Happen

### Step 1: Full-Text Screening (resolve the 129 records)

For each of the 129 records in `fulltext_screening_decisions.csv`:

**36 MAP records** (both reviewers agreed include): Confirm they truly meet ALL inclusion criteria:
1. Interventional RCT (parallel, crossover, factorial, adaptive, pragmatic)
2. Participants with diagnosed mental disorders (DSM-5/ICD-10/11)
3. Pharmacological intervention TARGETING a mental disorder
4. At least one Canadian recruitment site or Canadian institutional PI leadership (co-author alone is NOT sufficient — need actual Canadian site)
5. Main trial results published 2016+ (NOT secondary analyses, post-hoc, protocols)
6. English

**93 UNCERTAIN records** (reviewers disagreed): Make a final include/exclude decision. Common reasons they're uncertain:
- Multinational trials where Canadian site involvement is unclear from abstract → look up ClinicalTrials.gov registration to check site locations
- Borderline pharmacological interventions (micronutrients, supplements, FMT) → apply strict pharma criterion
- Ambiguous primary vs secondary analysis status → check if a separate primary results paper exists
- D-cycloserine/other adjuncts to neurostimulation → primary intervention must be pharmacological

For each record, use web search to look up the full paper (by PMID on PubMed, or by DOI). Check:
- Was there actually a Canadian recruitment site? (check ClinicalTrials.gov NCT number for site list)
- Is this the primary results paper? (or a secondary/post-hoc analysis?)
- Does the intervention qualify as pharmacotherapy targeting the mental disorder?

### Step 2: Data Extraction (PROGRESS-Plus framework)

For each confirmed included study, extract data using the codebook in `05_data_extraction/extraction_codebook.md`. Key variables:

**Race/Ethnicity:** Was it reported? What categories? How granular? Framework used? Subgroup analyses?
**Sex/Gender:** Distinguished? Categories reported?
**Indigenous:** Participation reported? OCAP principles referenced?
**Other PROGRESS-Plus:** Place, occupation, education, SES, social capital, age, disability, SOGI
**Trial covariates:** Funder, sample size, disorder category, intervention, design
**CONSORT-Equity:** Compliance with equity reporting items
**Benchmarking:** Map reported race categories to Statistics Canada Census 2021 taxonomy

### Step 3: Update PRISMA Flow Diagram

Fill in the blanks in `05_screening/PRISMA_2020_flow_diagram.md`:
- Records excluded at full-text (with reasons)
- Studies included in review (final n)

## How to Execute

Use a team of parallel agents. For the full-text screening:

1. **Split the 129 records into chunks** (e.g., 4 agents handling ~32 records each)
2. **Each agent independently** looks up each paper via web search (PubMed, ClinicalTrials.gov) and makes an include/exclude decision with reasoning
3. **A reconciliation agent** compares decisions and resolves disagreements
4. **2 QA agents** independently verify the final decisions

For data extraction:
1. **Split included studies across agents** (5-8 studies per agent)
2. **Each agent** reads the paper and extracts PROGRESS-Plus variables per the codebook
3. **A QA agent** verifies extraction accuracy by spot-checking 20% of records

## Critical Rules

- **DO NOT fabricate data.** If you can't find information about a study, say so. Never invent reviewer decisions, extraction values, or paper details.
- **Be strict on inclusion criteria.** The prior session's screening was initially too lenient (125 MAP was reduced to 36 after rigorous dual-review). Common errors: counting secondary analyses as primary trials, accepting Canadian co-authors as Canadian sites, including non-pharmacological interventions.
- **Document everything.** Every decision needs reasoning. A peer reviewer will read these files.
- **Use conservative reconciliation.** When agents disagree, default to the more restrictive decision.
- **Double-check everything.** Run QA agents after every major step. The prior session caught major errors through QA that would have undermined the review.

## Output Files to Create

1. `05_screening/fulltext_screening_final.csv` — final include/exclude decisions for all 129 records with full-text screening reasoning
2. `05_data_extraction/extracted_data.csv` — PROGRESS-Plus extraction for all included studies
3. `05_screening/PRISMA_2020_flow_diagram.md` — updated with full-text numbers
4. `05_screening/SCREENING_COMPLETE.md` — updated final summary

## Quality Standard

Every decision in this review should be defensible to a peer reviewer at a Canadian health research journal (target: Canadian Journal of Psychiatry or BMC Medical Research Methodology). The methodology section of the manuscript will describe dual-independent screening with QA audits — the data must support that claim.
