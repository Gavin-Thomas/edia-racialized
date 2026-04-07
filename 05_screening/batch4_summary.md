# Batch 4 Reconciliation Summary

## Overview
- **Date:** 2026-03-30
- **Reconciliation method:** Majority vote (2+ agree = final decision); ties with UNCERTAIN resolved conservatively; all-disagree = CONFLICT
- **Extractor coverage:**
  - Extractor 1: 75 abstracts screened
  - Extractor 2: 150 abstracts screened
  - Extractor 3: 149 abstracts screened

## ID Coverage
| Category | Count |
|----------|-------|
| Screened by all 3 extractors | 75 |
| Screened by 2 extractors | 74 |
| Screened by 1 extractor only | 1 |
| **Total unique abstracts** | **150** |

## Final Decisions
| Decision | Count | Percentage |
|----------|-------|------------|
| MAP (include) | 4 | 2.7% |
| OUT_OF_SCOPE (exclude) | 138 | 92.0% |
| UNCERTAIN (needs review) | 8 | 5.3% |
| CONFLICT (needs adjudication) | 0 | 0.0% |
| **Total** | **150** | **100%** |

## Agreement Statistics
| Metric | Count |
|--------|-------|
| Unanimous agreement (3/3 extractors) | 70 |
| Full agreement (2/2 extractors) | 68 |
| Majority vote resolved (2/3) | 5 |
| Single-extractor carry-forward | 1 |
| Conflicts requiring adjudication | 1 |
| **Agreement rate (among multi-extractor IDs)** | **92.6%** |

## Disagreements Requiring Attention

### Conflicts (all extractors disagreed or tied MAP vs OUT_OF_SCOPE)
- **36867173**: Antidepressant Augmentation versus Switch in Treatment-Resistant Geriatric Depre... | Tie between ext2,ext3: MAP, OUT_OF_SCOPE. Conservative: marked UNCERTAIN for methodologist review

### UNCERTAIN decisions (conservative tie-breaks and extractor uncertainty)
- **26746121**: Efficacy of Low-Dose Buspirone for Restricted and Repetitive Behavior in Young C... | Tie between ext2,ext3: UNCERTAIN, OUT_OF_SCOPE. Conservative approach: UNCERTAIN
- **27150464**: The Pharmacogenomics of Bipolar Disorder study (PGBD): identification of genes f... | Tie between ext2,ext3: UNCERTAIN, OUT_OF_SCOPE. Conservative approach: UNCERTAIN
- **28533148**: Repetitive transcranial magnetic stimulation of the right dorsal lateral prefron... | Tie between ext2,ext3: UNCERTAIN, OUT_OF_SCOPE. Conservative approach: UNCERTAIN
- **29407288**: GWAS-based machine learning approach to predict duloxetine response in major dep... | Majority vote: 2/3 UNCERTAIN. Dissent from ext3: OUT_OF_SCOPE
- **33636648**: Long-term effectiveness and safety of lemborexant in adults with insomnia disord... | Tie between ext2,ext3: MAP, UNCERTAIN. Conservative approach: UNCERTAIN
- **33643087**: Development and Evaluation of a Therapist Training Program for Psilocybin Therap... | Tie between ext2,ext3: UNCERTAIN, OUT_OF_SCOPE. Conservative approach: UNCERTAIN
- **33654400**: Efficacy of Vortioxetine on Anhedonia: Results from a Pooled Analysis of Short-T... | Majority vote: 2/3 UNCERTAIN. Dissent from ext3: OUT_OF_SCOPE
- **36867173**: Antidepressant Augmentation versus Switch in Treatment-Resistant Geriatric Depre... | Tie between ext2,ext3: MAP, OUT_OF_SCOPE. Conservative: marked UNCERTAIN for methodologist review

### MAP decisions (included for full-text review)
- **31429896**: Effect of Continuing Olanzapine vs Placebo on Relapse Among Patients With Psycho... | 2/2 MAP
- **32639561**: Effectiveness of Sequential Psychological and Medication Therapies for Insomnia ... | 2/2 MAP
- **35120288**: Treating Insulin Resistance With Metformin as a Strategy to Improve Clinical Out... | 2/2 MAP
- **37902726**: Exploratory Tau Biomarker Results From a Multiple Ascending-Dose Study of BIIB08... | 2/2 MAP

## Notes
- Extractor 1 screened only 75 of 150 abstracts (IDs 1-75 in the batch). The remaining 75 IDs were reconciled between Extractors 2 and 3 only.
- 1 ID (35964143) appeared only in Extractor 2 and was carried forward as-is (OUT_OF_SCOPE).
- Conservative approach applied to all ties involving UNCERTAIN: resolved as UNCERTAIN to avoid premature exclusion.
- All CONFLICT and UNCERTAIN items should be reviewed by the senior methodologist before finalizing.
