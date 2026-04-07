# QA Audit Corrections — Batches 23-42

**Date:** 2026-04-01
**Auditor:** Independent QA agent (re-screened all MAP and UNCERTAIN decisions)
**Records audited:** 80 (all MAP and UNCERTAIN from batches 23-42)

## Summary

| Action | Count |
|--------|-------|
| CONFIRMED (original correct) | 25 |
| UPGRADED (UNCERTAIN → MAP) | 6 |
| RECLASSIFIED (MAP → OUT_OF_SCOPE) | 3 |
| DOWNGRADED (MAP → UNCERTAIN) | 3 |
| DOWNGRADED (UNCERTAIN → OUT_OF_SCOPE) | 46 |

## Corrections Applied

### UPGRADED to MAP (previously UNCERTAIN)

| Batch | PMID | Title | Reason |
|-------|------|-------|--------|
| 23 | 38445382 | Intranasal oxytocin augmenting psychotherapy for MDD | Canadian PI (Joober, McGill Montreal); pharma RCT; DSM MDD |
| 27 | 36325158 | Buprenorphine augmentation for treatment-resistant depression | CAMH Toronto site confirmed; N=85; pharma RCT |
| 27 | 29338621 | CDP-choline for sensory gating in schizophrenia | Canadian (Knott/Labelle, Ottawa); pilot RCT; primary results |
| 31 | 34637343 | PRC-063 methylphenidate for adolescent ADHD | Canadian PI (Weiss, UBC); Phase 3; N=354; primary results |
| 33 | 40135470 | Mirtazapine for chronic insomnia (MIRAGE) | Canadian (Quebec geriatric clinic); N=60; DSM-5 insomnia |
| 35 | 40133524 | Escitalopram for agitation in Alzheimer's dementia | Canadian co-PIs (Ismail Calgary, Burhan London ON); N=173 |

### RECLASSIFIED to OUT_OF_SCOPE (previously MAP)

| Batch | PMID | Title | Reason |
|-------|------|-------|--------|
| 23 | 38260793 | Ketamine for TRD: Edmonton community program | Literature review + case study, NOT an RCT |
| 23 | 32573396 | Bright light + fluoxetine QoL in MDD | Explicitly "secondary outcome data from" a prior RCT |
| 41 | 27613505 | Varenicline in non-smokers with schizophrenia (CAMH) | Only n=9 in schizophrenia group (<10 threshold) |

### DOWNGRADED to UNCERTAIN (previously MAP)

| Batch | PMID | Title | Reason |
|-------|------|-------|--------|
| 23 | 38153735 | Zolpidem vs behavioral therapy for insomnia | Mixed pharma/behavioral primary intervention |
| 33 | 37689680 | Vaporized cannabis for PTSD | Only n=5 completers; unable to analyze placebo effect |
| 33 | 36855791 | PARTNERs collaborative care for depression | Service delivery model, not direct pharmacotherapy |

### Key Patterns in UNCERTAIN → OUT_OF_SCOPE Downgrades (46 records)

1. **Secondary/post-hoc analyses** (18 records): Most common error. Studies reporting secondary outcomes, subgroup analyses, or pharmacogenetic analyses from previously published RCTs.
2. **Non-pharmacological primary intervention** (7): Neurostimulation, digital therapy, or care delivery models where drugs were incidental.
3. **No Canadian site** (5): Canadian co-author ≠ Canadian recruitment site.
4. **Not targeting a mental disorder** (6): Drug targeting side effects (weight gain, NDI) or non-DSM conditions (fibromyalgia, MS).
5. **Not an RCT** (5): Open-label, observational, or experimental paradigm studies.
6. **Protocol without results** (3): Design papers reporting planned methodology.
7. **Sample <10** (2): Case series below threshold.

## Impact on Running Totals

- MAP added: +6 (upgrades)
- MAP removed: -3 (reclassified) -3 (downgraded to uncertain)
- Net MAP change: 0
- UNCERTAIN removed: -6 (upgraded to MAP) -46 (downgraded to OUT_OF_SCOPE)
- UNCERTAIN added: +3 (downgraded from MAP)
- Net UNCERTAIN change: -49
- OUT_OF_SCOPE added: +3 (reclassified from MAP) +46 (downgraded from UNCERTAIN)
- Net OUT_OF_SCOPE change: +49
