# Batch 40 Reconciliation Summary

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
| OUT_OF_SCOPE | 147 | 98.0% |
| MAP | 0 | 0.0% |
| UNCERTAIN | 3 | 2.0% |

## Category Distribution

| Category | Count | % |
|----------|------:|--:|
| non-pharmacological | 47 | 31.3% |
| protocol_only | 32 | 21.3% |
| non-mental-health | 24 | 16.0% |
| secondary_analysis | 17 | 11.3% |
| observational | 15 | 10.0% |
| review/meta-analysis | 8 | 5.3% |
| non-canadian | 4 | 2.7% |
| depression | 1 | 0.7% |
| anxiety_trauma_ocd | 1 | 0.7% |
| adhd | 1 | 0.7% |

## MAP Records (0)

No records met all inclusion criteria in this batch.

## UNCERTAIN Records Requiring Full-Text Review (3)

| ID | Title | Category | Reason |
|----|-------|----------|--------|
| 39470367 | Procognitive Effects of Adjunctive D-Cycloserine to Intermittent Theta-Burst Stimulation in Major Depressive Disorder | depression | Canadian RCT (Can J Psych, Calgary authors) of D-cycloserine (NMDA receptor agonist, 100 mg) as adjunct to iTBS for MDD (n=50). Pharmacological component targeting mental disorder with RCT results. Primary intervention is neurostimulation; need full-text to confirm if pharmacological adjunct qualifies. |
| 39316026 | Dietary counseling plus omega-3 supplementation in the treatment of generalized anxiety disorder: results of a randomized wait-list controlled pilot trial (the 'EASe-GAD Trial') | anxiety_trauma_ocd | Canadian RCT of dietary counseling + omega-3 supplementation for GAD in 50 women. Mental disorder (GAD), RCT with results. Need full-text to confirm if omega-3 supplement qualifies as pharmacological and to verify Canadian recruitment site. |
| 37672605 | A Randomized Three-Arm Double-Blind Placebo-Controlled Study of Homeopathic Treatment of Children and Youth with Attention-Deficit/Hyperactivity Disorder | adhd | Canadian (Toronto) 3-arm double-blind placebo-controlled RCT of homeopathic treatment for ADHD in children ages 6-16. Mental disorder (ADHD), RCT with results. Need full-text to determine if homeopathic medicines qualify as pharmacological intervention. |

## Notes

- This batch (rows 5859-6008) contained an exceptionally high proportion of OUT_OF_SCOPE records (98.0%), with no clear MAP records identified.
- The dominant exclusion reason was non-pharmacological interventions (31.3%), followed by protocol-only publications without results (21.3%) and non-mental-health topics (16.0%).
- The three UNCERTAIN records are all Canadian RCTs for mental disorders with results, but each raises questions about whether the intervention qualifies as pharmacological: D-cycloserine is adjunctive to neurostimulation, omega-3 supplementation is a nutraceutical, and homeopathic medicines are alternative medicine.
- Several Canadian studies were identified but excluded due to non-pharmacological interventions (e.g., digital health apps, CBT, mindfulness, Housing First, exercise programs, peer support).

## Files

- **Reconciled CSV:** `batch40_reconciled.csv`
- **Source rows:** 5859-6008 of `refined_all.csv`
