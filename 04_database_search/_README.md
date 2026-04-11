# 04 Database Search

> Scripted, reproducible multi-database literature search, deduplication, and refinement pipeline.

## Purpose

This folder executes the formal literature search for the scoping review. All fetch, deduplication, and filtering steps are implemented as Python scripts using only the standard library, so the pipeline is reproducible with a plain Python 3.11+ install. Outputs are CSVs of records and a Markdown log, which feed directly into [`../05_screening/`](../05_screening/).

## Files in this folder

| File | Description |
|------|-------------|
| [`search_strategy.md`](search_strategy.md) | Full documented search strategy (concept blocks, database-specific translations, field tags, limits). |
| [`fetch_pubmed.py`](fetch_pubmed.py) | Queries NCBI E-utilities (esearch + efetch with history server) and writes `abstracts/pubmed_results.csv`. No API key required; respects NCBI rate limits. |
| [`fetch_europepmc.py`](fetch_europepmc.py) | Queries the Europe PMC REST API using `cursorMark` pagination (pageSize=1000) and writes `abstracts/europepmc_results.csv`. No API key required. |
| [`fetch_scopus.py`](fetch_scopus.py) | Queries the Elsevier Scopus Search API and writes `abstracts/scopus_results.csv`. **Requires `SCOPUS_API_KEY` environment variable.** |
| [`fetch_openalex.py`](fetch_openalex.py) | Queries OpenAlex in two passes (affiliation `institutions.country_code:CA` + text-based "Canada/Canadian") and writes `abstracts/openalex_results.csv`. No API key required. |
| [`deduplicate.py`](deduplicate.py) | Merges all four per-database CSVs into `abstracts/combined_deduplicated.csv`. Deduplication priority: DOI → PMID → fuzzy title match (SequenceMatcher ratio ≥ 0.93 + same year). Writes `reports/dedup_report.md`. |
| [`refine_results.py`](refine_results.py) | Applies year and relevance filters to the deduplicated set, produces `abstracts/refined_all.csv`, a stratified pilot sample `abstracts/stratified_sample_200.csv` (seed 42), and `reports/search_log.md`. |
| [`abstracts/`](abstracts/) | All raw and processed CSV outputs (per-database results, deduplicated, refined, stratified sample). |
| [`reports/`](reports/) | Search log and deduplication overlap report. |

## How to reproduce

### Requirements

- **Python 3.11+** (scripts use only the standard library: `urllib`, `csv`, `json`, `xml.etree`, `difflib`, `datetime`)
- For Scopus: **`SCOPUS_API_KEY`** environment variable (Elsevier Developer Portal)
- Optional dependencies (listed in [`../requirements.txt`](../requirements.txt)) can be installed with:

```bash
pip install -r requirements.txt
```

### Pipeline order

Run the four fetchers (any order; they are independent), then dedupe, then refine:

```bash
cd 04_database_search

# 1. Fetch from each database
python fetch_pubmed.py
python fetch_europepmc.py
python fetch_openalex.py
export SCOPUS_API_KEY=your_key_here
python fetch_scopus.py

# 2. Deduplicate across databases
python deduplicate.py

# 3. Apply year + relevance filters and write the refined set
python refine_results.py
```

Each script writes its output into `abstracts/` (per-database CSVs, deduplicated CSV, refined CSV, stratified sample) and `reports/` (dedup_report, search_log).

## Records retrieved (2026-03-30 run)

| Database | Records |
|----------|--------:|
| PubMed | 9,964 |
| Europe PMC | 15,772 |
| Scopus | 27,983 |
| OpenAlex | 764 |
| **Combined raw total** | **54,483** |

### Deduplication (details in [`reports/dedup_report.md`](reports/dedup_report.md))

- DOI matches: 14,151
- PMID matches: 184
- Fuzzy title matches: 162
- Duplicates removed: **14,497**
- Unique records after deduplication: **39,986**

### Refinement filters (applied by `refine_results.py`)

| Filter | Records removed |
|--------|---------------:|
| No abstract | 1,557 |
| Year outside 2016-2026 | 12,473 |
| Not relevant (missing Canada / mental-health / RCT tokens) | 12,511 |
| Systematic reviews / meta-analyses | 2,541 |
| **Records eligible for screening** | **10,904** |

A **stratified pilot sample** of 200 records (generated with `random.seed(42)`) is also emitted for calibration purposes; it was not used as the primary selection set.

## Key decisions / rationale

- **Four API-accessible databases only** (PubMed, Europe PMC, Scopus, OpenAlex): reproducibility requires programmatic access. PsycINFO and CINAHL lack public APIs. See [`../03_inclusion_exclusion/criteria.md`](../03_inclusion_exclusion/criteria.md) ("Database selection" section) for the full rationale.
- **Conservative fuzzy-match threshold (0.93)**: chosen because the domain is narrow (Canadian psychiatry RCTs), where similar-but-distinct titles are common and false merges must be avoided.
- **Two-pass OpenAlex**: combines institutional-affiliation filtering (`institutions.country_code:CA`) with text-based "Canada/Canadian" mentions, maximising recall for trials where Canadian affiliation metadata is incomplete.

## Data integrity notes

- The current `refined_all.csv` contains 10,918 rows while this folder's `search_log.md` reports 10,904. The 14-row discrepancy arises because the CSV and log were produced by separate pipeline runs. The **screening pipeline operated on 10,904 records** (confirmed by [`../05_screening/SCREENING_COMPLETE.md`](../05_screening/SCREENING_COMPLETE.md) and [`../05_screening/screening_progress.yaml`](../05_screening/screening_progress.yaml)). The 14 extra records were not screened and do not affect downstream results.
- Similarly, `combined_deduplicated.csv` has 40,006 rows vs. 39,986 reported. Same cause, same non-impact on downstream results.

## Outputs

| Output | Description | Consumer |
|--------|-------------|----------|
| `abstracts/refined_all.csv` | All eligible records (10,904) after filters, sorted by citation count, ranked | [`../05_screening/`](../05_screening/) |
| `abstracts/stratified_sample_200.csv` | Stratified pilot sample (n=200) | Calibration only |
| `reports/search_log.md` | Full PRISMA-style identification/screening counts | Manuscript methods |
| `reports/dedup_report.md` | Pairwise database overlap, match-method breakdown | Manuscript appendix |

## Links

- Documented strategy: [`search_strategy.md`](search_strategy.md) and project-level [`../Search_Strategies_Canadian_MH_RCTs.md`](../Search_Strategies_Canadian_MH_RCTs.md)
- Previous stage: [`../03_inclusion_exclusion/`](../03_inclusion_exclusion/)
- Next stage: [`../05_screening/`](../05_screening/)
- PRISMA flow diagram: [`../05_screening/PRISMA_2020_flow_diagram.md`](../05_screening/PRISMA_2020_flow_diagram.md)
