# Batch 2 Screening Reconciliation Summary

**Date:** 2026-03-30
**Methodology:** Independent triple screening with majority-vote reconciliation

## Results

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Screened** | 150 | 100% |
| MAP (included) | 1 | 0.7% |
| OUT_OF_SCOPE (excluded) | 145 | 96.7% |
| UNCERTAIN (needs review) | 4 | 2.7% |
| CONFLICT (unresolved) | 0 | 0.0% |

## Agreement Statistics

| Metric | Count | Rate |
|--------|-------|------|
| Full agreement (3/3) | 137 | 91.3% |
| Majority agreement (2/3) | 11 | 7.3% |
| **Overall agreement (2+ agree)** | **148** | **98.7%** |
| 3-way disagreement (resolved) | 2 | 1.3% |
| 3-way disagreement (unresolved) | 0 | 0.0% |

## Reconciliation Rules Applied

1. **Majority vote:** If 2 or more extractors agree, that decision is final.
2. **Conservative tie-break:** If 1 MAP + 1 OUT_OF_SCOPE + 1 UNCERTAIN, resolved as UNCERTAIN (conservative approach requiring further review).
3. **2 OUT_OF_SCOPE + 1 UNCERTAIN:** Resolved as OUT_OF_SCOPE (majority rule).
4. **Unresolvable conflicts:** Marked as CONFLICT for senior reviewer adjudication.

## Records Requiring Further Review

### UNCERTAIN Decisions (4 records)
- **27721184**: Liraglutide promotes improvements in objective measures of cognitive dysfunction... | Votes: E1=OUT_OF_SCOPE, E2=UNCERTAIN, E3=UNCERTAIN | Majority (2/3)
- **28381506**: A phase 3 trial of IV immunoglobulin for Alzheimer disease... | Votes: E1=UNCERTAIN, E2=MAP, E3=OUT_OF_SCOPE | 3-way split (MAP/OUT_OF_SCOPE/UNCERTAIN) -> UNCERTAIN (conservative)
- **32101271**: Effects of Antipsychotic Medication on Brain Structure in Patients With Major De... | Votes: E1=OUT_OF_SCOPE, E2=UNCERTAIN, E3=MAP | 3-way split (MAP/OUT_OF_SCOPE/UNCERTAIN) -> UNCERTAIN (conservative)
- **33103819**: A ketogenic drink improves cognition in mild cognitive impairment: Results of a ... | Votes: E1=MAP, E2=UNCERTAIN, E3=UNCERTAIN | Majority (2/3)

### CONFLICT Decisions (0 records)
- None

### Majority-Only Decisions (2/3 agreement, 11 records)
- **27721184**: UNCERTAIN | Votes: E1=OUT_OF_SCOPE, E2=UNCERTAIN, E3=UNCERTAIN | Majority (2/3)
- **28294985**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=OUT_OF_SCOPE, E3=UNCERTAIN | Majority (2/3)
- **29067316**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=UNCERTAIN, E3=OUT_OF_SCOPE | Majority (2/3)
- **30791895**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=OUT_OF_SCOPE, E3=UNCERTAIN | Majority (2/3)
- **30845817**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=OUT_OF_SCOPE, E3=UNCERTAIN | Majority (2/3)
- **31329216**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=UNCERTAIN, E3=OUT_OF_SCOPE | Majority (2/3)
- **31786030**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=OUT_OF_SCOPE, E3=UNCERTAIN | Majority (2/3)
- **33103819**: UNCERTAIN | Votes: E1=MAP, E2=UNCERTAIN, E3=UNCERTAIN | Majority (2/3)
- **35431912**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=OUT_OF_SCOPE, E3=UNCERTAIN | Majority (2/3)
- **36094645**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=MAP, E3=OUT_OF_SCOPE | Majority (2/3)
- **36740140**: OUT_OF_SCOPE | Votes: E1=OUT_OF_SCOPE, E2=UNCERTAIN, E3=OUT_OF_SCOPE | Majority (2/3)

## Output Files

- Reconciled CSV: `batch2_reconciled.csv`
- This summary: `batch2_summary.md`
