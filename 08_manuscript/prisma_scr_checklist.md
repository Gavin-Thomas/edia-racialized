# Supplementary Table S1 — PRISMA-ScR Checklist

**Review title:** Equity, Diversity, Inclusion, and Accessibility Reporting in Canadian Mental Health Pharmacotherapy Randomized Controlled Trials (2016-2026): A Scoping Review Using the PROGRESS-Plus Framework

**Reporting guideline:** PRISMA Extension for Scoping Reviews (PRISMA-ScR)
**Reference:** Tricco AC, Lillie E, Zarin W, et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation. *Ann Intern Med.* 2018;169(7):467–473. doi:10.7326/M18-0850

**Note:** Item wording reproduced verbatim from Tricco et al. 2018. Compliance status reflects the current stage of the project (manuscript in outline; extraction complete). Items are assessed as: **Reported** (content exists in the repository or manuscript outline), **Partially reported** (content exists but is incomplete or provisional), or **Not yet reported** (planned but not yet drafted for the manuscript).

---

## Checklist

| # | Section / Item label | PRISMA-ScR item (Tricco et al. 2018 — exact wording) | Manuscript location | Repository file(s) | Compliance status |
|---|----------------------|------------------------------------------------------|---------------------|--------------------|-------------------|
| **TITLE** | | | | | |
| 1 | Title | Identify the report as a scoping review. | Title page — working title includes "A Scoping Review Using the PROGRESS-Plus Framework" | `08_manuscript/manuscript_outline.md` (Title Page) | **Reported** |
| **ABSTRACT** | | | | | |
| 2 | Structured summary | Provide a structured summary that includes, as applicable, background, objectives, eligibility criteria, sources of evidence, charting methods, results, and conclusions relating to the review questions and objectives. | Abstract — structured under: Objective, Design, Data sources, Eligibility criteria, Data extraction, Results, Conclusions | `08_manuscript/manuscript_outline.md` (Abstract) | **Partially reported** — Results section contains placeholder text pending final manuscript drafting; all structural elements are present in the outline |
| **INTRODUCTION** | | | | | |
| 3 | Rationale | Describe the rationale for the review in the context of what is already known and what the review adds to existing knowledge. | Section 1.2 (Rationale) | `08_manuscript/manuscript_outline.md` §1.2; supporting literature in `01_literature_search/` | **Partially reported** — Rationale points are outlined; full narrative prose not yet drafted |
| 4 | Objectives | Provide an explicit statement of the questions and objectives being addressed with reference to their key elements (e.g., population or participants, concepts, and context) or other relevant key elements used to conceptualize the review questions and/or objectives. | Section 1.3 (Objectives) — primary and secondary objectives listed with PROGRESS-Plus population/concept/context framing | `08_manuscript/manuscript_outline.md` §1.3; `02_research_question/` | **Reported** — 3 primary and 4 secondary objectives stated; population (Canadian mental health pharmacotherapy RCTs), concept (EDIA reporting per PROGRESS-Plus), and context (2016–2026, post-CIHR SGBA+ era) are explicit |
| **METHODS** | | | | | |
| 5 | Protocol and registration | Indicate whether a review protocol exists; state if and where it can be accessed (e.g., a Web address); and if available, provide registration information including the registration number. | Section 2.1 (Protocol and registration) | `08_manuscript/manuscript_outline.md` §2.1; `PROTOCOL_REGISTRATION.md` | **Reported** — Not pre-registered; transparency statement with full rationale and compensating measures documented in `PROTOCOL_REGISTRATION.md`; protocol accessible via public GitHub repository |
| 6 | Eligibility criteria | Specify characteristics of the sources of evidence used as eligibility criteria (e.g., years considered, language, and publication status), and provide a rationale for the decisions made. | Section 2.2 (Eligibility criteria) | `08_manuscript/manuscript_outline.md` §2.2; `03_inclusion_exclusion/criteria.md` | **Reported** — Inclusion (RCT, DSM-5/ICD-10 mental disorder, pharmacological intervention, verified Canadian recruitment site, 2016–2026, English) and exclusion criteria with rationale and documented criterion revision (2026-04-11) |
| 7 | Information sources | Describe all information sources in the search (e.g., databases with dates of coverage and contact with authors of studies) and date last searched. | Section 2.3 (Information sources and search strategy) | `08_manuscript/manuscript_outline.md` §2.3; `04_database_search/_README.md`; `Search_Strategies_Canadian_MH_RCTs.md` | **Reported** — 4 databases (PubMed, Europe PMC, Scopus, OpenAlex), all searched 2026-03-30; API types and per-database record counts documented |
| 8 | Search | Present the full search strategy for at least one database, including any limits used, such that it could be repeated. | Section 2.3 / Supplementary Table S2 | `Search_Strategies_Canadian_MH_RCTs.md`; `04_database_search/*.py` | **Reported** — Full search strategies for all 4 databases in `Search_Strategies_Canadian_MH_RCTs.md`; complete reproducible Python scripts in `04_database_search/`; to be formatted as Supplementary Table S2 in the manuscript |
| 9 | Selection of sources of evidence | State the process for selecting sources of evidence (i.e., screening and eligibility) included in the scoping review. | Section 2.4 (Selection of sources of evidence) | `08_manuscript/manuscript_outline.md` §2.4; `05_screening/SCREENING_COMPLETE.md`; `05_screening/PRISMA_2020_flow_diagram.md` | **Reported** — Dual independent title/abstract screening (10,904 records), Cohen's κ = 0.39 with base-rate caveat; Codex GPT-5.4 false-negative validation; full-text screening process; all decision rules documented |
| 10 | Data charting process | Describe the methods of charting data from the included sources of evidence (e.g., calibrated forms or forms that have been tested by the team before their use, and whether data charting was done independently or in duplicate) and any processes for obtaining and confirming data from investigators. | Section 2.5 (Data charting process) | `08_manuscript/manuscript_outline.md` §2.5; `06_data_extraction/`; Pass 2 QC results in `06_data_extraction/extraction_summary.md` | **Reported** — PROGRESS-Plus framework, 50+ variables per study; AI-assisted extraction with human QA; Pass 2 QC on 30% of records (20/66); Cohen's κ 0.86–1.00 for 4 key fields; extraction codebook in Supplementary File S3 |
| 11 | Data items | List and define all variables for which data were sought and any assumptions made. | Section 2.6 (Data items) | `08_manuscript/manuscript_outline.md` §2.6; `06_data_extraction/` (codebook); Supplementary File S3 | **Partially reported** — Variable categories listed in manuscript outline (trial-level covariates, PROGRESS-Plus variables, Indigenous-specific variables, CONSORT-Equity compliance); full definitions and decision rules in extraction codebook — to be published as Supplementary File S3 |
| 12 | Critical appraisal of individual sources of evidence | If done, provide a rationale for conducting a critical appraisal of included sources of evidence; describe the methods used and how this information was used in any data synthesis (if applicable). | Methods / not applicable (N/A for scoping reviews) | — | **Not applicable** — Consistent with scoping review methodology, formal risk-of-bias or quality appraisal of individual studies was not conducted; the manuscript will state this explicitly per PRISMA-ScR guidance |
| **RESULTS** | | | | | |
| 13 | Selection of sources of evidence | Give numbers of sources of evidence screened, assessed for eligibility, and included in the review, with reasons for exclusions at each stage, ideally using a flow diagram. | Section 3.1 (Selection of sources of evidence) / Figure 1 | `05_screening/PRISMA_2020_flow_diagram.md` | **Reported** — PRISMA flow diagram drafted: 54,483 identified → 39,986 unique → 10,904 screened → 134 full-text → 63 included (flow diagram) / 66 included (final extraction, per 2026-04-13 third correction; see footnote §); exclusion reasons at each stage documented |
| 14 | Characteristics of sources of evidence | For each source of evidence, present characteristics for which data were charted and provide the citations. | Section 3.2 (Characteristics of included trials) / Table 1 | `06_data_extraction/extraction_summary.md`; `06_data_extraction/extracted_data.csv` | **Partially reported** — Trial characteristics summarized in `extraction_summary.md` (66 trials, N=9,598, multisite/international proportions, disorder categories, median sample size); Table 1 to be formatted in manuscript |
| 15 | Critical appraisal within sources of evidence | If done, present data on critical appraisal of included sources of evidence (see item 12). | — | — | **Not applicable** — No critical appraisal conducted (see item 12) |
| 16 | Results of individual sources of evidence | For each included source of evidence, present the relevant data that were charted that relate to the review questions and objectives. | Section 3.3–3.8 / Supplementary File S4 | `06_data_extraction/extracted_data.csv`; `06_data_extraction/extraction_summary.md` | **Partially reported** — Per-study extraction data in `extracted_data.csv` (66 rows × 75 columns); summarized in `extraction_summary.md`; per-study table to be formatted in manuscript and published as Supplementary File S4 |
| 17 | Synthesis of results | Summarize and/or present the charting results as they relate to the review questions and objectives. | Section 2.7 (Synthesis) / Sections 3.3–3.8 (Results) / Tables 2–4 | `08_manuscript/manuscript_outline.md` §2.7, §3.3–§3.8; `06_data_extraction/extraction_summary.md` | **Partially reported** — Analysis plan specified (descriptive statistics, temporal comparison pre/post-2020, Census benchmarking); key findings documented in `extraction_summary.md`; full narrative synthesis and tables not yet drafted |
| **DISCUSSION** | | | | | |
| 18 | Summary of evidence | Summarize the main results (including an overview of concepts, themes, and types of evidence available), link to the review questions and objectives, and consider the relevance to key groups. | Section 4.1 (Summary of evidence) | `08_manuscript/manuscript_outline.md` §4.1–§4.5 | **Partially reported** — Summary points outlined (race/ethnicity gap, sex/gender conflation, intersectionality absent, Indigenous governance absent); comparison with US/global literature planned in §4.2; full narrative not yet drafted |
| 19 | Limitations | Discuss the limitations of the scoping review process. | Section 4.6 (Limitations) | `08_manuscript/manuscript_outline.md` §4.6; `_README.md` (Known limitations) | **Reported** — 6 limitations explicitly enumerated: English-language only, 4-database API-only search, AI-assisted screening/extraction, not pre-registered, Cohen's κ = 0.39, unequal temporal comparison windows |
| 20 | Conclusions | Provide a general interpretation of the results with respect to the review questions and objectives, as well as potential implications and/or next steps for research, practice, or policy. | Section 5 (Conclusions) | `08_manuscript/manuscript_outline.md` §5 | **Partially reported** — Conclusions and policy implications outlined (CIHR mandatory PROGRESS-Plus reporting, Indigenous governance); full narrative not yet drafted |
| **FUNDING** | | | | | |
| 21 | Funding | Describe sources of funding for the included sources of evidence, as well as sources of funding for the scoping review. Describe the role of the funders of the scoping review. | Section 3.8 (Funder patterns) / Funding statement | `08_manuscript/manuscript_outline.md` §3.8; `_README.md` (Authorship and conflicts of interest) | **Partially reported** — Funder patterns of *included trials* described in §3.8 (CIHR, NIH, industry, etc.); funding of *this review*: self-funded, no institutional sponsor — to be stated explicitly in the manuscript funding statement |
| 22 | Competing interests | Provide a statement of any competing interests, or a statement that there are none. | Declarations section | `_README.md` (Authorship and conflicts of interest) | **Reported** — Conflicts of interest: none declared; independent student-led review with no faculty PI, no institutional sponsor, no industry ties; to be included in manuscript declarations |

---

## Compliance summary

| Status | Count | Items |
|--------|-------|-------|
| Reported | 10 | 1, 4, 5, 6, 7, 8, 9, 10, 19, 22 |
| Partially reported | 10 | 2, 3, 11, 13, 14, 16, 17, 18, 20, 21 |
| Not applicable | 2 | 12, 15 |
| Not yet reported | 0 | — |

> Note: All items classified as "Partially reported" reflect the current stage of the project (data extraction complete; manuscript in outline stage). No substantive gaps in the underlying methodology or data exist; partial status indicates that full prose has not yet been drafted. Items 12 and 15 (critical appraisal) are intentionally not applicable per PRISMA-ScR guidance for scoping reviews that do not conduct formal quality appraisal.

---

## Key repository files cross-reference

| Repository file | PRISMA-ScR items covered |
|-----------------|--------------------------|
| `_README.md` | 2, 7, 19, 21, 22 |
| `PROTOCOL_REGISTRATION.md` | 5 |
| `03_inclusion_exclusion/criteria.md` | 6, 9 |
| `04_database_search/_README.md` | 7, 8 |
| `Search_Strategies_Canadian_MH_RCTs.md` | 8 |
| `04_database_search/*.py` | 8 |
| `05_screening/SCREENING_COMPLETE.md` | 9, 13 |
| `05_screening/PRISMA_2020_flow_diagram.md` | 13 |
| `05_screening/batch*_reconciled.csv` | 9, 13 |
| `06_data_extraction/extracted_data.csv` | 14, 16, 17 |
| `06_data_extraction/extraction_summary.md` | 10, 14, 16, 17, 18 |
| `08_manuscript/manuscript_outline.md` | All items (planned sections) |

---

*File created 2026-04-13. Based on Tricco et al. 2018 (Ann Intern Med 169:467–473). To be submitted as Supplementary Table S1.*
