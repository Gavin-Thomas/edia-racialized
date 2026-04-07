# QA Report: fulltext_screening_decisions.csv (QA Agent 2 -- Independent)

**Date:** 2026-04-01
**File:** `fulltext_screening_decisions.csv`
**Total records:** 153

---

## 1. COUNT CHECK -- FAIL

| Category | Count |
|----------|-------|
| MAP | 44 |
| UNCERTAIN | 109 |
| **Total** | **153** |

**Arbiter logic for MAP records:**
- All 44 MAP records have `arbiter_needed=No` -- PASS

**Arbiter logic for mismatching R1/R2:**
- 44 records have mismatching R1 and R2 decisions (both reviewers present, different decisions)
- All 44 have `arbiter_needed=Yes` -- PASS

**NOTE:** 34 UNCERTAIN records have both reviewers agreeing (both = UNCERTAIN) with `arbiter_needed=No`. This is correct behavior (no mismatch). 31 UNCERTAIN records have only a single reviewer (all with decision = UNCERTAIN, arbiter_needed=No). This is acceptable for single-reviewer records but raises a question about whether single-reviewer UNCERTAIN records should proceed to arbiter review regardless.

**Overall:** PASS on arbiter logic. Counts are internally consistent.

---

## 2. DUPLICATE CHECK -- PASS

- **Duplicate PMIDs:** 0
- **Duplicate titles:** 0
- **Note:** 13 records have empty/missing PMIDs (these are non-PubMed sourced studies with internal IDs). No two of these share the same title.

---

## 3. MISSING STUDIES CHECK -- FAIL

4 of 13 known MAP PMIDs are **MISSING** from the consolidated file:

| PMID | Description | Found in batch file | Status |
|------|-------------|---------------------|--------|
| 38445382 | oxytocin MDD McGill | batch23_reconciled.csv | **MISSING from consolidated** |
| 36325158 | buprenorphine TRD CAMH | batch27_reconciled.csv | **MISSING from consolidated** |
| 34637343 | PRC-063 ADHD UBC | batch31_reconciled.csv | **MISSING from consolidated** |
| 40135470 | mirtazapine insomnia Quebec | batch33_reconciled.csv | **MISSING from consolidated** |

**9 of 13 known PMIDs were found** in the consolidated file (all classified as UNCERTAIN, requiring arbiter review):

| PMID | Description | Final Decision |
|------|-------------|----------------|
| 29182037 | DRD4 methylphenidate Montreal | UNCERTAIN |
| 36519188 | OPTIMA BUP/NX | UNCERTAIN |
| 35324094 | quetiapine XR MDD Toronto | UNCERTAIN |
| 40587145 | ambroxol PD dementia | UNCERTAIN |
| 29959765 | STOP-PD psychotic depression | UNCERTAIN |
| 40133524 | escitalopram AD agitation | UNCERTAIN |
| 28234436 | clozapine switching CAMH | UNCERTAIN |
| 40875536 | AID-ME antidepressant AI | UNCERTAIN |
| 41218611 | semaglutide MDD Toronto | UNCERTAIN |

**Action required:** Investigate why PMIDs 38445382, 36325158, 34637343, and 40135470 were dropped during consolidation. All four exist in their respective batch reconciled files and must be added to the consolidated file.

---

## 4. DECISION ACCURACY CHECK -- PASS

15 randomly-sampled UNCERTAIN records were verified (seed=42):

- **7 records** had genuinely different R1/R2 decisions (e.g., MAP vs OUT_OF_SCOPE), all correctly flagged with `arbiter_needed=Yes`. These are true disagreements, not label normalization artifacts.
- **3 records** had both reviewers agreeing as UNCERTAIN, with `arbiter_needed=No`. Correct.
- **4 records** had a single reviewer only (the other field is empty), classified as UNCERTAIN with `arbiter_needed=No`. Reasonable for single-reviewer records.
- **1 record** had an empty PMID (single reviewer, UNCERTAIN). Acceptable for non-PubMed sourced studies.

**No label normalization issues detected.** All mismatches represent genuine disagreements between reviewers (e.g., MAP vs OUT_OF_SCOPE, MAP vs UNCERTAIN). No cases of the same decision in different casing or formatting being treated as a mismatch.

---

## 5. ABSTRACT CHECK -- FAIL

- **MAP records with abstracts:** 37 / 44 (84.1%)
- **Threshold:** 90%
- **Result:** Below threshold

**MAP records missing abstracts (n=7):**

| PMID | Title (truncated) |
|------|-------------------|
| 6644 | A Decision-Support System to Personalize Antidepressant Treatment in MDD |
| 9392 | An interdisciplinary program for familiar faces with chronic pain... |
| 6643 | Five-factor personality and antidepressant response to iTBS for MDD |
| 6664 | Identifying biomarkers to predict treatment response to nabilone... |
| 6677 | SMILE: nitrous oxide for treatment-resistant depression |
| 9449 | Substance of choice impact on treatment retention... |
| 9383 | The Effects of an E-Mental Health Program and Job Coaching... |

All 7 records with missing abstracts have non-standard PMIDs (4-digit internal IDs), suggesting they are non-PubMed sourced studies. Abstracts may need to be retrieved manually from original sources.

---

## Summary

| Check | Result |
|-------|--------|
| 1. Count / Arbiter Logic | PASS |
| 2. Duplicate Check | PASS |
| 3. Missing Studies | **FAIL** -- 4 known PMIDs missing from consolidated file |
| 4. Decision Accuracy | PASS |
| 5. Abstract Presence | **FAIL** -- 84.1% (below 90% threshold) |

**Overall: FAIL (2 issues require resolution)**

### Priority Actions
1. **Critical:** Add the 4 missing studies (PMIDs 38445382, 36325158, 34637343, 40135470) from their batch files into the consolidated file.
2. **Moderate:** Retrieve abstracts for the 7 MAP records with missing abstracts (all non-PubMed sourced studies with internal IDs).
