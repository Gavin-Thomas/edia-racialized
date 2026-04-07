# Batch 3 Screening Reconciliation Summary

**Date:** 2026-03-30
**Extractors:** 3 independent reviewers
**Method:** Majority vote reconciliation with conservative tie-breaking

## Overall Results

| Metric | Count |
|---|---|
| Total abstracts screened | 150 |
| MAP (included) | 3 |
| OUT_OF_SCOPE (excluded) | 145 |
| UNCERTAIN (requires full-text) | 2 |
| CONFLICT (unresolved) | 0 |

## Agreement Statistics

| Metric | Value |
|---|---|
| Unanimous agreement (3/3) | 143 (95.3%) |
| Majority agreement (2/3) | 7 |
| Conservative resolution (3-way split) | 0 |
| Overall agreement rate (2/3+) | 100.0% |

## Reconciliation Rules Applied

1. **Majority vote:** 2+ extractors agree = final decision
2. **Conservative tie-breaking:** MAP + OUT_OF_SCOPE + UNCERTAIN = UNCERTAIN
3. **Conflict flag:** All 3 disagree with no applicable rule = CONFLICT

## Non-Unanimous Decisions

| ID | Title | Final | Votes | Notes |
|---|---|---|---|---|
| 27032628 | Effects of citalopram on neuropsychiatric symptoms in Alzhei... | OUT_OF_SCOPE | MAP/OUT_OF_SCOPE/OUT_OF_SCOPE | Majority rule (2v1); dissent: MAP |
| 27780334 | Efficacy of Vortioxetine on Cognitive Functioning in Working... | UNCERTAIN | UNCERTAIN/UNCERTAIN/OUT_OF_SCOPE | Majority rule (2v1); dissent: OUT_OF_SCOPE |
| 28473524 | A realist evaluation of patients' decisions to deprescribe i... | OUT_OF_SCOPE | OUT_OF_SCOPE/UNCERTAIN/OUT_OF_SCOPE | Majority rule (2v1); dissent: UNCERTAIN |
| 30952794 | INTREPAD: A randomized trial of naproxen to slow progress of... | OUT_OF_SCOPE | OUT_OF_SCOPE/OUT_OF_SCOPE/UNCERTAIN | Majority rule (2v1); dissent: UNCERTAIN |
| 31759333 | Single and repeated ketamine infusions for reduction of suic... | MAP | MAP/UNCERTAIN/MAP | Majority rule (2v1); dissent: UNCERTAIN |
| 33658952 | The Efficacy, Safety, and Tolerability of Probiotics on Depr... | OUT_OF_SCOPE | OUT_OF_SCOPE/UNCERTAIN/OUT_OF_SCOPE | Majority rule (2v1); dissent: UNCERTAIN |
| 33860185 | Acute and Sustained Reductions in Loss of Meaning and Suicid... | UNCERTAIN | UNCERTAIN/UNCERTAIN/OUT_OF_SCOPE | Majority rule (2v1); dissent: OUT_OF_SCOPE |

## MAP Decisions (Included Studies)

| ID | Title | Votes |
|---|---|---|
| 27556593 | Metformin for Treatment of Overweight Induced by Atypical Antipsychotic Medicati... | MAP/MAP/MAP |
| 31759333 | Single and repeated ketamine infusions for reduction of suicidal ideation in tre... | MAP/UNCERTAIN/MAP |
| 34570180 | Effect of Methylphenidate on Apathy in Patients With Alzheimer Disease: The ADME... | MAP/MAP/MAP |

## UNCERTAIN Decisions (Require Full-Text Review)

| ID | Title | Votes |
|---|---|---|
| 27780334 | Efficacy of Vortioxetine on Cognitive Functioning in Working Patients With Major... | UNCERTAIN/UNCERTAIN/OUT_OF_SCOPE |
| 33860185 | Acute and Sustained Reductions in Loss of Meaning and Suicidal Ideation Followin... | UNCERTAIN/UNCERTAIN/OUT_OF_SCOPE |

## Data Quality Notes

- Extractor 3 had a data entry error: IDs 29362209 and 29624206 were swapped. Both were OUT_OF_SCOPE decisions, so this did not affect the reconciled outcome. The swap was corrected during reconciliation.
