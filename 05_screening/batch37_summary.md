# Batch 37 Reconciliation Summary

**Date:** 2026-03-31
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
| OUT_OF_SCOPE | 145 | 96.7% |
| MAP | 1 | 0.7% |
| UNCERTAIN | 4 | 2.7% |

## Category Distribution

| Category | Count | % |
|----------|------:|--:|
| non-pharmacological | 49 | 32.7% |
| non-mental-health | 26 | 17.3% |
| observational | 23 | 15.3% |
| secondary_analysis | 17 | 11.3% |
| review/meta-analysis | 14 | 9.3% |
| protocol_only | 13 | 8.7% |
| non-canadian | 3 | 2.0% |
| psychotic | 2 | 1.3% |
| depression | 2 | 1.3% |
| other_mental_health | 1 | 0.7% |

## MAP Records (1)

| ID | Title | Category |
|----|-------|----------|
| 40875536 | Artificial Intelligence in Depression-Medication Enhancement (AID-ME): A Cluster Randomized Trial of a Deep-Learning-Enabled Clinical Decision Support System for Personalized Depression Treatment Selection and Management | depression |

**Details:** Canadian multicenter (9 sites) cluster randomized trial of an AI-enabled clinical decision support system guiding antidepressant selection for outpatient adults with moderate or greater severity MDD. The intervention guides pharmacological treatment (antidepressant prescribing); active-control clinicians received patient questionnaires and guideline training. Published 2025.

## UNCERTAIN Records Requiring Full-Text Review (4)

| ID | Title | Category | Reason |
|----|-------|----------|--------|
| 41233083 | Efficacy and safety of iclepertin for cognitive impairment associated with schizophrenia (CONNEX programme) | psychotic | Phase 3 multinational RCT (41 countries, 338 centres) of iclepertin (GlyT1 inhibitor) for CIAS. Pharmacological, mental disorder (schizophrenia). Canadian recruitment sites not confirmed from abstract alone. |
| 39463173 | Efficacy of vortioxetine versus desvenlafaxine in the treatment of functional impairment in patients with major depressive disorder: Results from the multinational VIVRE study | depression | Multinational RCT of vortioxetine vs desvenlafaxine for MDD with inadequate SSRI response. Pharmacological, mental disorder. Canadian sites not confirmed from abstract. |
| 39248107 | Neurophysiological effects of a combined treatment of lovastatin and minocycline in patients with fragile X syndrome: Ancillary results of the LOVAMIX randomized clinical trial | other_mental_health | Ancillary TMS neurophysiology results from LOVAmix RCT (NCT02680379) of lovastatin+minocycline for Fragile X syndrome. Pharmacological intervention for neurodevelopmental disorder. Unclear if this constitutes primary results; Canadian origin plausible but needs confirmation. |
| 38900958 | Randomized Laboratory Study of Single-Dose Cannabis, Dronabinol, and Placebo in Patients With Schizophrenia and Cannabis Use Disorder | psychotic | Double-dummy placebo-controlled trial of single-dose THC (oral dronabinol or smoked cannabis) in SCZ-CUD. Pharmacological; mental disorders (schizophrenia + CUD). Canadian sites not confirmed; laboratory study design may not meet standard clinical trial criteria. |

## Notes

- This batch (rows 5409-5558) contained a very high proportion of OUT_OF_SCOPE records (96.7%), dominated by non-pharmacological interventions (32.7%), non-mental-health topics (17.3%), and observational/non-RCT study designs (15.3%).
- The single MAP record is a Canadian cluster RCT that uses AI to guide antidepressant prescribing for MDD.
- All four UNCERTAIN records are pharmacological RCTs for mental disorders but require full-text review to confirm Canadian recruitment sites or to verify whether ancillary/laboratory study designs meet inclusion criteria.

## Files

- **Reconciled CSV:** `batch37_reconciled.csv`
- **Source rows:** 5409-5558 of `refined_all.csv`
