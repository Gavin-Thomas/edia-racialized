# Batch 38 Reconciliation Summary

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
| OUT_OF_SCOPE | 146 | 97.3% |
| MAP | 0 | 0.0% |
| UNCERTAIN | 4 | 2.7% |

## Category Distribution

| Category | Count | % |
|----------|------:|--:|
| non-pharmacological | 48 | 32.0% |
| observational | 25 | 16.7% |
| protocol_only | 21 | 14.0% |
| secondary_analysis | 18 | 12.0% |
| non-mental-health | 16 | 10.7% |
| non-canadian | 13 | 8.7% |
| review/meta-analysis | 5 | 3.3% |
| depression | 1 | 0.7% |
| psychotic | 1 | 0.7% |
| adhd | 1 | 0.7% |
| substance_use | 1 | 0.7% |

## MAP Records (0)

No records met all inclusion criteria in this batch.

## UNCERTAIN Records Requiring Full-Text Review (4)

| ID | Title | Category | Reason |
|----|-------|----------|--------|
| 33476774 | The primary care assessment and research of a telephone intervention for neuropsychiatric conditions with education and resources study: Design, rationale, and sample of the PARTNERs randomized controlled trial | depression | Canadian RCT of collaborative care for depression/anxiety/at-risk drinking in primary care using pharmacological treatment algorithms. Design paper with sample description; unclear if main results published separately. Needs full-text review to determine if primary results are available. |
| 35257622 | EEG Microstates in Early Phase Psychosis: The Effects of Acute Caffeine Consumption | psychotic | Canadian (Dalhousie, Nova Scotia) placebo-controlled randomized double-blind study of caffeine 200mg in early psychosis vs healthy controls. Pharmacological and mental disorder criteria met, but caffeine is not a standard pharmacotherapy targeting the mental disorder. Needs full-text review. |
| 28058589 | Assessment of effects of atomoxetine in adult patients with ADHD: consistency among three geographic regions in a response maintenance study | adhd | Multinational phase 3 RCT of atomoxetine for adult ADHD with US/Canada as one geographic region. Pharmacological intervention for mental disorder. Canadian recruitment sites not individually confirmed from abstract alone. |
| 30774343 | Depressed mood induction in early cigarette withdrawal is unaffected by acute monoamine precursor supplementation | substance_use | Canadian (CAMH Toronto) placebo-controlled crossover RCT of dietary supplement (tryptophan + tyrosine + blueberry antioxidants) during cigarette withdrawal. Targets depressed mood in smokers. Need full-text to verify if participants had diagnosed mental disorders or were otherwise healthy smokers. |

## Notes

- This batch (rows 5559-5708) contained no MAP records and a very high proportion of OUT_OF_SCOPE records (97.3%), dominated by non-pharmacological interventions (32.0%), observational/non-RCT study designs (16.7%), protocol-only publications (14.0%), and secondary analyses (12.0%).
- The four UNCERTAIN records are all potentially Canadian pharmacological studies for mental disorders but each has specific issues requiring full-text verification: (1) PARTNERs may be a design paper with results published elsewhere; (2) caffeine is not a standard pharmacotherapy for psychosis; (3) Canadian sites in the atomoxetine trial need confirmation; (4) monoamine precursor supplementation study may not involve participants with diagnosed mental disorders.

## Files

- **Reconciled CSV:** `batch38_reconciled.csv`
- **Source rows:** 5559-5708 of `refined_all.csv`
