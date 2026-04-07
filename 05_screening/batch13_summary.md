# Batch 13 Reconciliation Summary

**Date:** 2026-03-30
**Method:** Strict majority vote (2-of-3)
**Note:** Extractor 3 was identified as liberal (18 MAP, many low-confidence). Majority vote applied strictly -- if 2 of 3 voted OUT_OF_SCOPE, the final decision is OUT_OF_SCOPE regardless of the third extractor's MAP vote.

## Input Summary

| Source | Records | MAP | OUT_OF_SCOPE | UNCERTAIN |
|--------|---------|-----|--------------|-----------|
| Extractor 1 | 150 | 3 | 142 | 5 |
| Extractor 2 | 150 | 16 | 133 | 1 |
| Extractor 3 | 150 | 18 | 132 | 0 |

## Reconciled Output

- **Total records:** 150
- **Final MAP:** 12
- **Final OUT_OF_SCOPE:** 138
- **Unanimous agreement:** 130 (86.7%)
- **Conflicts resolved by majority vote:** 20 (13.3%)
  - Resolved as MAP: 9
  - Resolved as OUT_OF_SCOPE: 11

## Pairwise Agreement

| Pair | Agreement | Rate |
|------|-----------|------|
| Ext1 vs Ext2 | 136/150 | 90.7% |
| Ext1 vs Ext3 | 135/150 | 90.0% |
| Ext2 vs Ext3 | 139/150 | 92.7% |

## Extractor 3 Liberal Bias

Extractor 3 classified 18 records as MAP compared to 3 (Ext1) and 16 (Ext2). Of Ext3's 18 MAP votes, **6** were overruled to OUT_OF_SCOPE by majority vote.

### Ext3 MAP Overruled to OUT_OF_SCOPE

| ID | Title (truncated) |
|-----|-------------------|
| 26971071 | Cognitive Behavior Therapy for psychosis based Guided Self-help (CBTp-GSH) deliv... |
| 29387022 | Magnetic Seizure Therapy in Treatment-Resistant Schizophrenia: A Pilot Study. |
| 29581089 | Evaluation of an Internet-Based Behavioral Intervention to Improve Psychosocial ... |
| 32809030 | Magnetic Seizure Therapy for Suicidality in Treatment-Resistant Depression. |
| 37535357 | Efficacy of Telephone-Based Cognitive Behavioral Therapy for Weight Loss Disorde... |
| rank_1904 | Mindfulness-based intervention for female adolescents with chronic pain: A pilot... |

## UNCERTAIN Handling

Extractor 1 had 5 UNCERTAIN votes and Extractor 2 had 1 UNCERTAIN vote. UNCERTAIN votes were treated as non-MAP for majority purposes. Where no clear majority existed (e.g., 1 MAP + 1 OOS + 1 UNCERTAIN), the conservative default of OUT_OF_SCOPE was applied.

## All Conflicts

| ID | Final | Votes | Notes |
|----|-------|-------|-------|
| 26496015 | MAP | 2/3 | Ext1 voted UNCERTAIN (conf=0.40) |
| 26971071 | OUT_OF_SCOPE | 2/3 | Ext3 voted MAP (conf=0.30) |
| 27821210 | MAP | 2/3 | Ext1 voted UNCERTAIN (conf=0.40) |
| 28869006 | OUT_OF_SCOPE | 2/3 | Ext2 voted MAP (conf=0.35) |
| 29387022 | OUT_OF_SCOPE | 2/3 | Ext3 voted MAP (conf=0.35) |
| 29581089 | OUT_OF_SCOPE | 2/3 | Ext3 voted MAP (conf=0.25) |
| 29957477 | OUT_OF_SCOPE | 2/3 | Ext2 voted UNCERTAIN (conf=0.40) |
| 31344528 | OUT_OF_SCOPE | 2/3 | Ext2 voted MAP (conf=0.45) |
| 31555976 | OUT_OF_SCOPE | 2/3 | Ext2 voted MAP (conf=0.40) |
| 31721892 | MAP | 2/3 | Ext1 voted OUT_OF_SCOPE (conf=0.90) |
| 31969269 | OUT_OF_SCOPE | 2/3 | Ext2 voted MAP (conf=0.45) |
| 32809030 | OUT_OF_SCOPE | 2/3 | Ext3 voted MAP (conf=0.35) |
| 33092404 | MAP | 2/3 | Ext1 voted OUT_OF_SCOPE (conf=0.75) |
| 34782701 | MAP | 2/3 | Ext1 voted OUT_OF_SCOPE (conf=0.70) |
| 36151869 | MAP | 2/3 | Ext1 voted UNCERTAIN (conf=0.50) |
| 36516343 | MAP | 2/3 | Ext1 voted OUT_OF_SCOPE (conf=0.80) |
| 36529623 | MAP | 2/3 | Ext1 voted UNCERTAIN (conf=0.50) |
| 37535357 | OUT_OF_SCOPE | 2/3 | Ext3 voted MAP (conf=0.30) |
| 37795512 | MAP | 2/3 | Ext1 voted UNCERTAIN (conf=0.55) |
| rank_1904 | OUT_OF_SCOPE | 2/3 | Ext3 voted MAP (conf=0.30) |

---
*Reconciliation performed programmatically with strict 2-of-3 majority vote.*
