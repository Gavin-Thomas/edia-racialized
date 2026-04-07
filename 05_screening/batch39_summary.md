# Batch 39 Reconciliation Summary

**Date:** 2026-04-01
**Method:** Majority vote (2+/3 agree). Three-way split marked UNCERTAIN.

## Extractor Coverage

| Extractor | Records |
|-----------|---------|
| Extractor 1 | 150 |
| Extractor 2 | 150 |
| Extractor 3 | 150 |
| **Unique IDs** | **150** |

## Agreement Statistics

| Metric | Count | % |
|--------|------:|--:|
| Unanimous (3/3) | 150 | 100.0% |
| Majority (2/3) | 0 | 0.0% |
| Uncertain (3-way split) | 0 | 0.0% |
| **Total** | **150** | **100%** |

## Decision Distribution

| Decision | Count | % |
|----------|------:|--:|
| OUT_OF_SCOPE | 149 | 99.3% |
| MAP | 0 | 0.0% |
| UNCERTAIN | 1 | 0.7% |

## Category Distribution

| Category | Count | % |
|----------|------:|--:|
| non-pharmacological | 55 | 36.7% |
| observational | 29 | 19.3% |
| review/meta-analysis | 25 | 16.7% |
| non-mental-health | 23 | 15.3% |
| non-canadian | 7 | 4.7% |
| protocol_only | 6 | 4.0% |
| secondary_analysis | 4 | 2.7% |
| substance_use | 1 | 0.7% |

## MAP Records (0)

None in this batch.

## UNCERTAIN Records Requiring Full-Text Review (1)

| ID | Title | Category | Reason |
|----|-------|----------|--------|
| (no PMID) | Probenecid as a pharmacotherapy for alcohol use disorder: A randomized placebo-controlled alcohol interaction trial | substance_use | Phase I/IIa RCT of probenecid (2g oral) for AUD (N=35). Randomized, double-blind, placebo-controlled, crossover trial. Pharmacological intervention targeting a mental disorder (AUD). Canadian site not confirmed from abstract; authors appear US-based (Brown University affiliations). Needs full-text to confirm Canadian recruitment sites. |

## Notes

- This batch (rows 5709-5858) contained an extremely high proportion of OUT_OF_SCOPE records (99.3%), with zero MAP records identified.
- The dominant exclusion category was non-pharmacological interventions (36.7%), reflecting a large number of psychotherapy, neurostimulation, exercise, and digital interventions that lacked a pharmacological component.
- Observational/non-RCT study designs (19.3%) and reviews/meta-analyses (16.7%) were also prominent exclusion categories.
- Non-mental-health topics (15.3%) included veterinary studies, cardiac/stroke research, geological studies, and other unrelated areas.
- The single UNCERTAIN record is a pharmacological RCT for AUD but requires full-text review to confirm Canadian recruitment sites.
- Several Canadian studies were identified but excluded as non-pharmacological (e.g., digital DBT in Toronto, psychoeducation for BD in Vancouver, museum visit in Montreal, care bundle in Alberta).

## Files

- **Reconciled CSV:** `batch39_reconciled.csv`
- **Source rows:** 5709-5858 of `refined_all.csv`
