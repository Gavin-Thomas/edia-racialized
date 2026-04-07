# Batch 9 Reconciliation Summary

**Date:** 2026-03-30
**Records reconciled:** 150
**Sources:** ext1_b9.csv, ext2_b9.csv, ext3_b9.csv
**Method:** Majority vote (2/3 agree); three-way split marked UNCERTAIN

---

## Agreement Statistics

| Metric | Count | % |
|---|---|---|
| Unanimous (3/3) | 138 | 92.0% |
| Majority rule (2/3) | 10 | 6.7% |
| Three-way split (UNCERTAIN) | 2 | 1.3% |
| **Total** | **150** | **100%** |

**Inter-rater agreement rate (2+ concordant):** 98.7%

---

## Final Decision Distribution

| Decision | Count | % |
|---|---|---|
| OUT_OF_SCOPE | 140 | 93.3% |
| MAP | 5 | 3.3% |
| UNCERTAIN | 5 | 3.3% |
| **Total** | **150** | **100%** |

---

## Records Decided MAP (n=5)

| ID | Title | Vote | Notes |
|---|---|---|---|
| 28942807 | Metformin for Overweight Induced by Antipsychotics in Youth With ASD | 2/3 | ext1 voted UNCERTAIN |
| 29689693 | Vortioxetine improves symptomatic and functional outcomes in MDD | 2/3 | ext1 voted UNCERTAIN |
| 30684794 | Methylphenidate vs CBT for binge eating disorder | 2/3 | ext1 voted UNCERTAIN |
| 31682328 | Comorbid anxiety in late-life depression: venlafaxine treatment | 2/3 | ext1 voted UNCERTAIN |
| 33658605 | Peripheral inflammatory biomarkers define biotypes of bipolar depression | 2/3 | ext3 voted UNCERTAIN |

---

## Records Marked UNCERTAIN (n=5)

| ID | Title | Votes | Notes |
|---|---|---|---|
| 27529771 | Omega-3 for depressive symptoms in CAD patients | ext1=UNC, ext2=MAP, ext3=UNC | Majority UNCERTAIN |
| 30115553 | Adjunctive SAMe for non-remittent MDD | ext1=UNC, ext2=OOS, ext3=MAP | Three-way split |
| 30771856 | Vitamins B12/B6/Folic Acid in First-Episode Psychosis | ext1=UNC, ext2=OOS, ext3=MAP | Three-way split |
| 31658058 | Hydromethylthionine for cognitive decline in AD | ext1=UNC, ext2=UNC, ext3=MAP | Majority UNCERTAIN |
| 32212856 | Vortioxetine for age-related cognitive decline | 3/3 | Unanimous UNCERTAIN |

---

## Conflicts Resolved to OUT_OF_SCOPE (n=2)

| ID | Title | Votes | Notes |
|---|---|---|---|
| 31587995 | Escitalopram for agitation in AD (S-CitAD protocol) | ext1=OOS, ext2=UNC, ext3=OOS | Majority OUT_OF_SCOPE |
| 37489299 | Psilocybin for TRD (protocol) | ext1=OOS, ext2=MAP, ext3=OOS | Majority OUT_OF_SCOPE |
| 32217739 | Melatonin for postconcussive symptoms in children | ext1=OOS, ext2=OOS, ext3=MAP | Majority OUT_OF_SCOPE |

---

## Methodologist Action Required

The following 2 records had three-way splits and require manual adjudication:

1. **30115553** -- SAMe for MDD: ext1=UNCERTAIN, ext2=OUT_OF_SCOPE, ext3=MAP. Key question: is this Australian-only or does it include Canadian sites?
2. **30771856** -- B-vitamins in first-episode psychosis: ext1=UNCERTAIN, ext2=OUT_OF_SCOPE, ext3=MAP. Key question: appears Australian; verify Canadian site involvement.

The remaining 3 UNCERTAIN records were resolved by majority vote (2/3 agreed UNCERTAIN) and may also warrant review if borderline MAP decisions affect the scoping review yield.

---

## Output Files

- `batch9_reconciled.csv` -- 150 rows with columns: id, title, final_decision, category, vote_count, conflict_flag, reconciliation_notes
