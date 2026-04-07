# Deduplication Report

Deduplication was performed during the database search stage (Stage 4) using a 3-tier
automated approach. This report summarizes results for PRISMA flow reporting.

| Metric | Count |
|--------|-------|
| Records identified (all databases, pre-deduplication) | 54,483 |
| Records removed — DOI-exact duplicates | 14,151 |
| Records removed — PMID-exact duplicates | 184 |
| Records removed — fuzzy title+year duplicates (>0.93 threshold) | 162 |
| Possible duplicates flagged for human review | 0 (best-match selection used) |
| Records after deduplication | 39,986 |
| Records removed — no abstract | 1,557 |
| Records removed — year outside 2016-2026 | 12,473 |
| Records removed — not relevant (missing Canada/MH/RCT terms) | 12,511 |
| Records removed — systematic reviews/meta-analyses | 2,541 |
| **Records proceeding to screening** | **10,904** |

## Database Breakdown (pre-deduplication)
| File | Format | Records |
|------|--------|---------|
| pubmed_results.csv | PubMed E-utilities XML→CSV | 9,964 |
| europepmc_results.csv | Europe PMC REST API JSON→CSV | 15,772 |
| openalex_results.csv | OpenAlex REST API JSON→CSV | 764 |
| scopus_results.csv | Scopus Search API JSON→CSV | 27,983 |

## Deduplication Method
- Pass 1: DOI-exact matching (case-insensitive, URL-prefix-normalized)
- Pass 2: PMID-exact matching
- Pass 3: Fuzzy title matching (SequenceMatcher ratio >0.93, same publication year, best-match selection)
- HTML artifacts stripped during processing

See `04_database_search/reports/dedup_report.md` for full pairwise overlap statistics.
