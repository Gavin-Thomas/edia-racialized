# Directory Map

Living map of the project. Updated whenever structure changes. Each automated session reads this first to orient.

Last updated: 2026-04-12

```
edia-racialized/
|
|-- _README.md                          # Project overview and entry point
|-- project.yaml                        # Structured project metadata (stages, counts, config)
|-- PROTOCOL_REGISTRATION.md            # Pre-registration transparency statement
|-- AUTHORS.md                          # Authorship and conflicts of interest
|-- NEXT_SESSION_PROMPT.md              # Handoff instructions (written pre-extraction)
|-- CHANGELOG.md                        # Session-by-session changelog (MUST read + append every session)
|-- DIRECTORY_MAP.md                    # This file
|-- LICENSE                             # CC BY 4.0
|-- Search_Strategies_Canadian_MH_RCTs.md  # Original search planning document
|-- .gitignore                          # Excludes PDFs, data files from git
|
|-- 01_literature_search/
|   |-- _README.md                      # Stage overview
|   |-- landscape_report.md             # Key studies, preliminary terms, gaps identified
|
|-- 02_research_question/
|   |-- _README.md                      # Stage overview
|   |-- research_question.md            # Full PCC framework, objectives, temporal analysis plan
|
|-- 03_inclusion_exclusion/
|   |-- _README.md                      # Stage overview
|   |-- criteria.md                     # AUTHORITATIVE inclusion/exclusion with decision rules
|                                       #   Key criterion: verified Canadian recruitment site
|
|-- 04_database_search/
|   |-- _README.md                      # Stage overview
|   |-- search_strategy.md              # Per-database search translations
|   |-- fetch_pubmed.py                 # PubMed E-utilities script
|   |-- fetch_europepmc.py              # Europe PMC REST API script
|   |-- fetch_scopus.py                 # Scopus API (requires SCOPUS_API_KEY)
|   |-- fetch_openalex.py               # OpenAlex two-pass script
|   |-- deduplicate.py                  # DOI/PMID/fuzzy title dedup
|   |-- refine_results.py               # Year and relevance filters
|   |-- abstracts/                      # Per-database CSVs, deduplicated, refined
|   |-- reports/                        # Dedup and search logs
|
|-- 05_screening/
|   |-- _README.md                      # Stage overview
|   |-- SCREENING_COMPLETE.md           # Final screening report (confirmed MAP list, kappa, counts)
|   |-- PRISMA_2020_flow_diagram.md     # PRISMA flow with counts and exclusion reasons
|   |-- fulltext_screening_decisions.csv  # AUTHORITATIVE per-record full-text decisions
|   |                                     #   134 rows. final_decision: INCLUDE(66)/EXCLUDE(67)/NOT_RETRIEVED(1)
|   |-- included_for_fulltext_review.csv  # Pre-QA pool (194 records, historical)
|   |-- qa_audit_corrections.md         # QA decision log
|   |-- qa_consolidated_check1.md       # QA report batch 1
|   |-- qa_consolidated_check2.md       # QA report batch 2
|   |-- batch{1-73}_reconciled.csv      # Per-batch final screening decisions
|   |-- batch{43-73}_screenerA.csv      # Phase 3 independent screen A
|   |-- batch{43-73}_screenerB.csv      # Phase 3 independent screen B
|   |-- codex_false_negatives_*.csv     # Codex OUT_OF_SCOPE validation (all empty = 0 FN)
|
|-- 06_data_extraction/
|   |-- _README.md                      # Stage overview
|   |-- extraction_codebook.md          # AUTHORITATIVE variable definitions and decision rules
|   |                                   #   50+ PROGRESS-Plus variables. Follow literally.
|   |-- extraction_tracker.csv          # Per-record extraction status tracking (created by automation)
|   |-- extracted_data.csv              # OUTPUT: one row per included study (created by automation)
|
|-- 07_full_texts/
|   |-- README.md                       # Retrieval status and methods
|   |-- ALL_66_LINKS.md                 # AUTHORITATIVE per-record full-text status with links
|   |-- PAYWALLED_LINKS.md             # DEPRECATED historical snapshot
|   |-- REMAINING_PROXY_URLS.md        # Proxy links (legacy)
|   |-- record_*.pdf                    # Full-text PDFs (44 files, not in git)
|   |-- record_*_fulltext.txt           # Extracted plain text from PMC (22 files, not in git)
|   |-- record_*_PMID_*.txt             # PubMed abstract stubs (27 files, metadata only)
|   |-- record_*_fulltext.xml           # XML full text (1 file: record_120)
|   |-- 132_methylphenidate_adhd.pdf    # Record #132 (non-standard naming)
|   |-- 133_miratzipine_insomnia.pdf    # Record #133 (non-standard naming)
|
|-- 08_manuscript/
|   |-- manuscript_outline.md           # PRISMA-ScR manuscript outline with section structure
```

## Key authoritative files (read these for ground truth)

| Purpose | File |
|---------|------|
| Inclusion criteria | `03_inclusion_exclusion/criteria.md` |
| Which records are INCLUDE/EXCLUDE | `05_screening/fulltext_screening_decisions.csv` |
| Variable definitions for extraction | `06_data_extraction/extraction_codebook.md` |
| Full-text retrieval status | `07_full_texts/ALL_66_LINKS.md` |
| What happened last | `CHANGELOG.md` |

## File format notes for full texts

- 22 records have `.txt` or `.xml` full text (from PMC) — read directly
- 44 records have PDF only — read with the Read tool (multimodal)
- 27 `_PMID_*.txt` files are abstract stubs only, NOT full text
- Records #132 and #133 use non-standard filenames (no `record_` prefix)
