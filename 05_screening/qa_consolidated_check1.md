# QA Report: fulltext_screening_decisions.csv

**Date:** 2026-04-01
**QA Agent:** QA Agent 1
**File under review:** `fulltext_screening_decisions.csv`

---

> ⚠️ **HISTORICAL SNAPSHOT — PRE-CORRECTION (2026-04-11)**
>
> This QA consolidated check describes the state of `fulltext_screening_decisions.csv` BEFORE the retroactive correction of 2026-04-11. The "5 missing MAP PMIDs" flagged as failures in this report were subsequently added to the included set (records 130-134 in the current CSV). See `SCREENING_COMPLETE.md` "Retroactive Correction" section and root `_README.md` "Revision history" for the post-correction resolution.
>
> Current canonical state (as of 2026-04-11):
> - 134 forwarded to full-text review (was 129 pre-correction)
> - 69 included in final review (was 65 pre-correction)
> - 67 of 69 full texts obtained
> - Record #113 (PMID 41218611) dropped from included set (unobtainable)

---

## CHECK 1: STRUCTURAL CHECK -- PASS (with note)

**Expected columns:** record_number, pmid, doi, title, authors, journal, year, abstract, reviewer_1_decision, reviewer_1_reasoning, reviewer_2_decision, reviewer_2_reasoning, final_decision, arbiter_needed, arbiter_notes

**Result:** All 15 expected columns are present and correctly named.

- **Row count:** 153 data rows (plus header)
- **Final decision breakdown:** 44 MAP, 109 UNCERTAIN
- **Reviewer 1 decisions:** 63 MAP, 67 UNCERTAIN, 4 OUT_OF_SCOPE, 19 blank
- **Reviewer 2 decisions:** 54 MAP, 52 UNCERTAIN, 20 OUT_OF_SCOPE, 27 blank
- **Arbiter needed:** 44 Yes, 109 No

**Note:** 46 records (30%) have only one reviewer decision present (19 with blank R1, 27 with blank R2). These appear to be records from batches where only one screening pass was available. Record numbering is 1-153 (re-numbered, not original batch record numbers).

---

## CHECK 2: DECISION LOGIC CHECK -- PASS

Tested all 153 records against the conservative decision rules:

| Rule | Expected | Violations |
|------|----------|------------|
| Both MAP -> MAP | MAP | 0 |
| Both OUT_OF_SCOPE -> should NOT be in file | excluded | 0 |
| MAP vs OUT_OF_SCOPE -> UNCERTAIN | UNCERTAIN | 0 |
| MAP vs UNCERTAIN -> UNCERTAIN | UNCERTAIN | 0 |
| UNCERTAIN vs OUT_OF_SCOPE -> should NOT be in file | excluded | 0 |

All 107 dual-reviewed records follow the conservative decision rules correctly. No OUT_OF_SCOPE final decisions exist in the file. No records that should have been excluded are present.

For the 46 single-reviewer records, the final decision matches the sole reviewer's decision (MAP or UNCERTAIN). This is acceptable behavior though it means these records have not been independently verified by a second reviewer.

---

## CHECK 3: CROSS-REFERENCE -- Reviewer 1 vs Source Files -- PASS (with caveats)

Checked 10 MAP records against their source batch files:

| PMID | Source File | R1 Match? |
|------|------------|-----------|
| 39415650 | batch46_screenerA.csv | MATCH (MAP) |
| 30684794 | batch1_22_reviewerA_chunk1.csv | MATCH (MAP, notes match with category prefix) |
| 26482056 | batch1_22_reviewerA_chunk1.csv | MATCH (MAP) |
| 28013123 | batch1_22_reviewerA_chunk1.csv | MATCH (MAP) |
| 34570180 | batch1_22_reviewerA_chunk1.csv | MATCH (MAP) |
| 30135032 | batch1_22_reviewerA_chunk2.csv | MATCH (MAP) |
| 23773886 | batch14_reviewer2.csv | Note: R1 sourced from reviewer2 file |
| 27895238 | batch15_reviewer2.csv | Note: R1 sourced from reviewer2 file |
| 37530824 | batch11_reviewer2.csv | Note: R1 sourced from reviewer2 file |
| 38153735 | batch23_reviewer2.csv | Note: R1 sourced from reviewer2 file |

**Caveat:** For several records (PMIDs 23773886, 27895238, 37530824, 38153735), the "Reviewer 1" decision in the consolidated file appears to have been sourced from `batch{N}_reviewer2.csv` files rather than screenerA/reviewerA files. This suggests the reviewer labeling (R1 vs R2) may not consistently correspond to the same screening pass across batches. The decisions themselves are accurate.

---

## CHECK 4: CROSS-REFERENCE -- Reviewer 2 vs Source Files -- CONDITIONAL PASS

Checked 10 MAP records:

| PMID | Source File | R2 Match? | Notes |
|------|------------|-----------|-------|
| 41779422 | batch45_screenerB.csv | MATCH (MAP) | |
| 39415650 | batch46_screenerB.csv | MATCH (MAP) | |
| 30684794 | batch1_22_reviewerB_chunk1.csv | MATCH (MAP) | |
| 26482056 | batch1_22_reviewerB_chunk1.csv | MATCH (MAP) | |
| 28013123 | batch1_22_reviewerB_chunk1.csv | MATCH (MAP) | |
| 23773886 | batch14_reviewer2.csv | MATCH (MAP) | |
| 37530824 | batch11_reviewer2.csv | MATCH (MAP) | |
| 30135032 | batch12_reviewer2.csv | **MISMATCH** | Source=UNCERTAIN, Consolidated=MAP |
| 27895238 | batch15_reviewer2.csv | **MISMATCH** | Source=UNCERTAIN, Consolidated=MAP |
| 9392 | batch63_screenerB.csv | MATCH (MAP) | But reconciled says UNCERTAIN (A=EXCLUDE, B=MAP) |

**PMID 30135032 mismatch explained:** The batch12_reviewer2.csv shows UNCERTAIN, but a later dual-review (batch1_22_reviewerA_chunk2 and reviewerB_chunk2) both confirmed MAP. The consolidated file used the later, more authoritative dual-review decisions. This is acceptable.

**PMID 27895238 mismatch:** batch15_reviewer2 says UNCERTAIN, but the consolidated file shows R2=MAP. This may reflect a later review. Requires verification.

**PMID 9392 issue:** The batch63_reconciled.csv shows final_decision=UNCERTAIN (because screenerA=EXCLUDE, screenerB=MAP), but the consolidated file shows this record with only R2=MAP, no R1, and final_decision=MAP. This is an error -- the final decision should be UNCERTAIN per the conservative rules.

---

## CHECK 5: NO FABRICATION CHECK -- PASS

Spot-checked 5 records by comparing reasoning text in consolidated file against source batch files:

| PMID | R1 Reasoning | R2 Reasoning |
|------|-------------|-------------|
| 30684794 | Verbatim match (with category prefix added) | Verbatim match (with category prefix added) |
| 26482056 | Verbatim match (with category prefix) | Verbatim match (with category prefix) |
| 28013123 | Verbatim match (with category prefix) | Verbatim match (with category prefix) |
| 39415650 | Near-verbatim ("INCLUDED;" prefix added) | Category prefix + source notes |
| 30135032 | Category prefix + source notes (from reviewerA_chunk2) | Category prefix + source notes (from reviewerB_chunk2) |

**Pattern:** Reasoning text in the consolidated file consistently consists of a category prefix (e.g., "depression;", "eating_disorder;") prepended to the verbatim notes from the source batch files. No fabricated reasoning was detected.

---

## CHECK 6: COMPLETENESS CHECK -- FAIL

### Known MAP PMIDs (from task specification)

Of 25 known confirmed MAP PMIDs provided:

- **21 found with correct MAP decision**
- **2 found but marked UNCERTAIN instead of MAP:**
  - PMID 41405885 (Extended-release buprenorphine doses OUD)
  - PMID 28521199 (Injectable hydromorphone vs diacetylmorphine OUD - SALOME)
- **2 completely missing from consolidated file:**
  - PMID 25999335 (Agomelatine adjunctive to mood stabilizer)
  - PMID 32380271 (Infliximab vs placebo for bipolar depression)

### SCREENING_COMPLETE.md confirmed MAP PMIDs

Of 56 confirmed MAP PMIDs listed in SCREENING_COMPLETE.md:

- **5 completely missing from consolidated file:**
  - PMID 29338621 (CDP-choline sensory gating schizophrenia, Ottawa)
  - PMID 36325158 (Buprenorphine augmentation TRD, CAMH)
  - PMID 34637343 (PRC-063 methylphenidate adolescent ADHD, UBC)
  - PMID 40135470 (Mirtazapine chronic insomnia MIRAGE, Quebec)
  - PMID 38445382 (Intranasal oxytocin + psychotherapy for MDD)

- **20 present but marked UNCERTAIN instead of MAP** (these were confirmed MAP in SCREENING_COMPLETE.md but appear as UNCERTAIN in the consolidated file):
  - PMID 27536342, 29182037, 29537978, 36519188, 35324094, 40587145, 29959765, 38520501, 40133524, 28234436, 40875536, 33630646, 36927273, 41218611, 41405885, 28521199, 41785480, 41582768, 41085986, 35702828

### Batch reconciled vs consolidated totals

- Total MAP/UNCERTAIN across all 73 batch reconciled files: **377**
- Total in consolidated file: **153**
- Difference: **224 records** not carried forward

This large gap is partially explained by the dual-review process (many initial MAP/UNCERTAIN were reclassified to OUT_OF_SCOPE on re-review). However, the 5 completely missing confirmed MAP records and 20 confirmed MAPs marked as UNCERTAIN represent genuine errors.

---

## OVERALL ASSESSMENT

| Check | Result |
|-------|--------|
| 1. Structural | **PASS** |
| 2. Decision Logic | **PASS** |
| 3. Cross-reference R1 | **PASS** (with caveats on reviewer labeling) |
| 4. Cross-reference R2 | **CONDITIONAL PASS** (1 incorrect final_decision for PMID 9392) |
| 5. No Fabrication | **PASS** |
| 6. Completeness | **FAIL** |

### Critical Issues Requiring Action

1. **5 confirmed MAP studies are completely missing** from the consolidated file (PMIDs: 29338621, 36325158, 34637343, 40135470, 38445382). These must be added.

2. **20 confirmed MAP studies are marked UNCERTAIN** instead of MAP. While the conservative screening logic may justify UNCERTAIN when reviewers disagreed, these have been confirmed as MAP in the SCREENING_COMPLETE.md final report. The consolidated file and the completion report are inconsistent.

3. **2 known MAP PMIDs missing** (25999335, 32380271). These were downgraded by dual-review but still show as MAP in batch5_reconciled.csv. Their status needs clarification.

4. **PMID 9392 (record 9392 from batch63):** Final decision is MAP but reconciled file says UNCERTAIN (screenerA=EXCLUDE, screenerB=MAP). Should be UNCERTAIN per conservative rules.

5. **46 records have only one reviewer** (30% of file). These have not been independently verified and should be flagged for priority second review.

### Recommendation

The consolidated file needs to be regenerated to:
- Add the 5 missing confirmed MAP records
- Reconcile the 20 UNCERTAIN vs confirmed-MAP discrepancies with SCREENING_COMPLETE.md
- Fix PMID 9392 from MAP to UNCERTAIN
- Clarify the status of PMIDs 25999335 and 32380271
