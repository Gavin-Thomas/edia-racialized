# Search and Refinement Log

## EDIA Reporting in Canadian Mental Health Pharmacotherapy RCTs

**Date of search refinement:** 2026-03-30

## Database Search Results

| Database | Records Retrieved |
|----------|------------------:|
| PubMed | 9,964 |
| OpenAlex | 764 |
| Europe PMC | 15,772 |
| Scopus | 27,983 |
| **Combined total** | **54,483** |

## Deduplication and Filtering

- Records after deduplication: **39,986**
- Duplicates removed: 14,497
- Records removed (no abstract): 1,557
- Records removed (year outside 2016-2026): 12,473
- Records removed (not relevant - missing Canada/MH/RCT): 12,511
- Records removed (systematic reviews/meta-analyses): 2,541
- **Records after all filters: 10,904**
- Stratified random sample for extraction: 200

## PRISMA-Style Flow Diagram

```
IDENTIFICATION
============================================================
  PubMed: 9,964 records
  OpenAlex: 764 records
  Europe PMC: 15,772 records
  Scopus: 27,983 records
  Combined total: 54,483 records

              |
              v

DEDUPLICATION
============================================================
  Duplicates removed: 14,497
  Unique records: 39,986

              |
              v

SCREENING / FILTERING
============================================================
  Excluded - no abstract:                1,557
  Excluded - year outside 2016-2026:     12,473
  Excluded - not relevant (Canada+MH+RCT): 12,511
  Excluded - systematic reviews/MAs:       2,541
  Total excluded at filtering:            29,082

              |
              v

REFINED SET
============================================================
  Records eligible for screening: 10,904
  Stratified random sample for extraction: 200
```

## Output Files

| File | Description |
|------|-------------|
| `abstracts/refined_all.csv` | All eligible records after filtering, sorted by citations, with rank |
| `abstracts/top_100_cited.csv` | Stratified random sample (n=200) for data extraction |
| `reports/dedup_report.md` | Deduplication overlap statistics |
| `reports/search_log.md` | This log file |
