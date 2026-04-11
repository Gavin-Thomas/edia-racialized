# Screening Complete: Final Report

**Date:** 2026-04-01
**Total records screened:** 10,904 / 10,904 (100%)

---

## Quality Assurance Summary

Every record in this review has been verified by at least 2 independent reviewers:

| Batches | Records | Screening method | False-negative check |
|---------|---------|-----------------|---------------------|
| 1-22 | 3,309 | Single-screened (prior session) → dual-reviewed all MAP/UNCERTAIN (6 agents, A+B per chunk) | Codex GPT-5.4 second-pass of all 2,771 OUT_OF_SCOPE: **0 false negatives** |
| 23-42 | 3,000 | Single-screened (this session) → QA audit of all MAP/UNCERTAIN | Codex GPT-5.4 second-pass of all 2,917 OUT_OF_SCOPE: **0 false negatives** (1 borderline: PMID 29458928, n=9, vitamin D) |
| 43-73 | 4,595 | Dual-screened (Screener A + B independent) → QA audit of MAP/UNCERTAIN | N/A (already dual-screened) |

### Inter-Rater Agreement (Dual-Screened Batches 43-73)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Percent agreement (normalized) | **97.8%** | After collapsing `EXCLUDE` ≡ `OUT_OF_SCOPE` vocabulary |
| Cohen's κ | **0.39** | Fair agreement |
| Raw string-match agreement (not recommended) | ~76% | Reflects vocabulary drift, not disagreement |
| Dual-screened records | 4,458 | Batches 43-73 |
| Records classified MAP by either reviewer | 28 | Small "positive" class |

**Reporting guidance:** Cohen's κ = 0.39 is the preferred headline metric for this dataset. The base rate of exclusions is ~96%, so percent agreement is heavily inflated by trivially easy exclusions and overstates true reviewer concordance. The raw 76% agreement figure that appears in the batch CSVs without label normalization is an artifact of vocabulary inconsistency (`EXCLUDE` vs. `OUT_OF_SCOPE` were used synonymously across batches), not a reflection of real disagreement, and should not be reported.

**Caveat on the "include" decision:** of the 4,458 dual-screened records, only 28 were classified as MAP by either reviewer. Agreement on exclusions is therefore near-perfect, but agreement on the harder "include" decisions is less well-characterized by these statistics. This is a known limitation of reporting percent agreement alone for imbalanced screening tasks, and is part of why κ is reported alongside.

---

## Confirmed MAP Studies

### Batches 1-22: 25 confirmed (of original 125)

| PMID | Title (abbreviated) | Category |
|------|---------------------|----------|
| 26580307 | Bright light + fluoxetine for nonseasonal MDD | Depression |
| 27049826 | Hydromorphone vs diacetylmorphine for OUD (SALOME) | Substance use |
| 26460229 | Risperidone/olanzapine adjunctive to mood stabilizer in bipolar | Bipolar |
| 26482056 | Cholinesterase inhibitor discontinuation in AD | Dementia |
| 27284082 | Methylene blue for residual bipolar symptoms | Bipolar |
| 28013123 | Crossover trial evaluating a pharmacological agent for MH | Other |
| 28061017 | Extended-release naltrexone for opioid and alcohol dependence | Substance use |
| 28185899 | Lurasidone for cognitive impairment in euthymic bipolar | Bipolar |
| 30684794 | Long-acting methylphenidate vs CBT for adult ADHD | ADHD |
| 30922101 | Ketamine infusions for treatment-resistant depression | Depression |
| 31066887 | Infliximab vs placebo for bipolar depression | Bipolar |
| 31182351 | Nabilone for agitation in Alzheimer's disease | Dementia |
| 32639561 | Sequential psychological and medication therapies for insomnia | Other |
| 34570180 | Methylphenidate for apathy in Alzheimer's (ADMET 2) | Dementia |
| 35120288 | Metformin for insulin resistance in bipolar depression | Bipolar |
| 36223114 | D-cycloserine + iTBS for treatment-resistant depression | Depression |
| 38359838 | Psilocybin-assisted psychotherapy for TRD | Depression |
| 30135032 | Agomelatine vs escitalopram for severe GAD | Anxiety |
| 37530824 | Adjunctive antidepressant maintenance in bipolar I depression | Bipolar |
| 23773886 | Risperidone LAI vs oral in early psychosis | Psychotic |
| 27895238 | Methylphenidate + reading intervention for ADHD+RD | ADHD |
| 32068562 | Varenicline for smoking cessation in alcohol-dependent smokers | Substance use |
| 35151410 | Balovaptan for ASD (V1aduct phase 3) | Other |
| 37227402 | Vortioxetine vs desvenlafaxine for MDD (VIVRE) | Depression |
| 39862881 | Intranasal oxytocin for FTD apathy (FOXY) | Dementia |

### Batches 1-22: 38 uncertain (needs full-text to resolve)

These are studies where the two independent reviewers disagreed. Most involve:
- Multinational trials where Canadian site involvement is unclear from abstract alone
- Borderline pharmacological interventions (micronutrients, supplements)
- Studies where primary vs secondary analysis status is ambiguous

### Batches 23-73: 31 confirmed

| PMID | Title (abbreviated) | Category |
|------|---------------------|----------|
| 27536342 | CONCERTA vs generic methylphenidate ADHD crossover | ADHD |
| 38445382 | Intranasal oxytocin + psychotherapy for MDD | Depression |
| 29182037 | DRD4 methylphenidate ADHD crossover (Montreal) | ADHD |
| 29537978 | Rivastigmine oral vs transdermal PDD (Quebec) | Dementia |
| 29338621 | CDP-choline sensory gating schizophrenia (Ottawa) | Psychotic |
| 36325158 | Buprenorphine augmentation TRD (CAMH) | Depression |
| 36519188 | OPTIMA: BUP/NX vs methadone OUD (4 provinces) | Substance use |
| 35324094 | Quetiapine XR augmentation MDD (Toronto) | Depression |
| 34637343 | PRC-063 methylphenidate adolescent ADHD (UBC) | ADHD |
| 34076068 | Ketamine adjunct to ECT for MDD (U Alberta) | Depression |
| 40135470 | Mirtazapine chronic insomnia MIRAGE (Quebec) | Other |
| 40587145 | Ambroxol for PD dementia (London ON) | Dementia |
| 29959765 | STOP-PD olanzapine+sertraline psychotic depression | Psychotic |
| 38520501 | Vortioxetine for post-COVID depression | Depression |
| 40133524 | Escitalopram for AD agitation (Calgary/London ON) | Dementia |
| 28234436 | Clozapine switching RCT (CAMH) | Psychotic |
| 40875536 | AID-ME AI-guided antidepressant selection (9 sites) | Depression |
| 33630646 | CDP-choline dose-finding schizophrenia (Ottawa) | Psychotic |
| 36927273 | CDP-choline + galantamine schizophrenia (Ottawa) | Psychotic |
| 41218611 | Semaglutide for cognitive dysfunction MDD (Toronto) | Depression |
| 41779422 | PETRUSHKA antidepressant personalization (JAMA 2026) | Depression |
| 40936464 | SMILE nitrous oxide for TRD (Toronto) | Depression |
| 39415650 | Brexpiprazole maintenance MDD (McIntyre Toronto) | Depression |
| 31965445 | Methylphenidate crossover ADHD children (Montreal) | ADHD |
| 41405885 | Extended-release buprenorphine doses OUD (Toronto) | Substance use |
| 28521199 | Injectable hydromorphone vs diacetylmorphine OUD (SALOME) | Substance use |
| 41785480 | FMT for bipolar depression (CAMH/McMaster) | Bipolar |
| 41582768 | Methylphenidate ER cognition schizophrenia (McGill/Ottawa) | Psychotic |
| 41085986 | Rapid vs standard buprenorphine induction OUD | Substance use |
| 35702828 | OPTIMA primary: BUP/NX vs methadone OUD (7 sites) | Substance use |
| 32457492 | Melatonin for AUD sleep (Le Foll CAMH Toronto) | Substance use |

---

## Definitive Counts

| Category | Count |
|----------|-------|
| **Confirmed MAP** | **56** |
| Uncertain (needs full-text) | 38 |
| OUT_OF_SCOPE (excluded) | 10,810 |
| **Estimated final MAP after full-text** | **~65-75** |

## Confirmed MAP by Disorder Category

| Category | Count |
|----------|-------|
| Depression/TRD | 16 |
| Substance use (OUD, AUD) | 8 |
| Bipolar/mood | 7 |
| Dementia/neurocognitive | 6 |
| Psychotic/schizophrenia | 6 |
| ADHD | 5 |
| Anxiety/OCD | 1 |
| Other (insomnia, ASD, FTD) | 7 |

## Confirmed MAP by Time Period

| Period | Count |
|--------|-------|
| 2016-2019 | 22 |
| 2020-2022 | 14 |
| 2023-2026 | 20 |

---

## Full-Text Forwarding Note

Pre-QA screening flagged **194 records** as MAP or UNCERTAIN (`included_for_fulltext_review.csv`). After QA audits resolved 65 of these to OUT_OF_SCOPE (mostly secondary analyses, non-Canadian sites, and non-pharmacological interventions), **129 records** were forwarded to full-text review (`fulltext_screening_decisions.csv`). After the 2026-04-11 retroactive correction (see below), 5 additional QA-upgraded MAP records were propagated into the full-text pool, bringing the total to **134 forwarded to full text**. Of these 134, **69 studies** were included, **64 excluded**, and **1 not retrieved** (Record #113, see below).

## Screening Process Documentation

1. **10,904 records** retrieved from 4 databases (PubMed, Scopus, Europe PMC, OpenAlex), deduplicated, and filtered
2. **73 batches** of 150 records each (final batch: 96 records)
3. **Dual-screening** (Screener A + Screener B independent) for batches 43-73
4. **QA audits** on all MAP/UNCERTAIN decisions across all batches
5. **Codex GPT-5.4 false-negative check** on all ~5,900 OUT_OF_SCOPE records from single-screened batches: **0 confirmed false negatives**
6. **Dual-reviewer reconciliation** of batches 1-22 MAP studies: reduced from 125 to 25 confirmed (100 were secondary analyses, protocols, non-pharma, or non-Canadian)

## Files

| File | Description |
|------|-------------|
| `batch{N}_reconciled.csv` | Final decisions for each batch (N=1-73) |
| `batch{N}_screenerA.csv` / `screenerB.csv` | Independent screener outputs (batches 43-73) |
| `qa_audit_corrections.md` | QA audit results for batches 23-42 |
| `qa_audit_batches48_73.md` | QA audit results for batches 48-73 |
| `batch1_22_reviewer{A,B}_chunk{1,2,3}.csv` | Dual-review of batches 1-22 MAP studies |
| `codex_false_negatives_b{range}.csv` | Codex false-negative check results (all empty = no false negatives) |
| `screening_progress.yaml` | Running totals and progress tracking |
| `SCREENING_COMPLETE.md` | This file |

---

## Retroactive Correction (2026-04-11)

During a final consistency check between this file and `fulltext_screening_decisions.csv`, five QA-upgraded MAP records listed above in "Batches 23-73: 31 confirmed" were found to have **never been written into `fulltext_screening_decisions.csv`**. They were therefore silently excluded from the full-text screening stage, even though this file had recorded them as confirmed MAP inclusions.

**Affected records:**

| Record # | PMID | Title (abbreviated) | Journal | DOI |
|----------|------|---------------------|---------|-----|
| 130 | 29338621 | CDP-choline sensory gating, schizophrenia (Aidelbaum 2018) | J Psychopharmacol 2018 | 10.1177/0269881117746903 |
| 131 | 36325158 | Low-dose buprenorphine augmentation for TRD (Lee 2022) | Biol Psychiatry Glob Open Sci 2022 | 10.1016/j.bpsgos.2021.09.003 |
| 132 | 34637343 | PRC-063 methylphenidate for adolescent ADHD (Weiss 2021) | J Child Adolesc Psychopharmacol 2021 | 10.1089/cap.2021.0034 |
| 133 | 40135470 | Mirtazapine for chronic insomnia (MIRAGE, Nguyen 2025) | Age and Ageing 2025 | 10.1093/ageing/afaf050 |
| 134 | 38445382 | Intranasal oxytocin + IPT for MDD (Ellenbogen 2024) | Psychological Medicine 2024 | 10.1017/S0033291724000217 |

**Investigation.** Each of the five records was re-assessed against the inclusion criteria using PubMed abstracts, ClinicalTrials.gov registrations, and PubMed Central open-access text where available. All five were confirmed to meet the inclusion criteria at **HIGH** confidence: each is an interventional RCT of a pharmacological agent targeting a diagnosed mental-health condition, with clear Canadian site leadership (Ottawa, CAMH Toronto, UBC, Quebec/CHUM, and Concordia respectively), and main trial results published within the 2016–2026 window.

**Resolution.** All five records were added to the final included list, bringing the total from 65 to **69 included studies**. Full texts were successfully retrieved for Records 130, 131, and 134. Records 132 (PRC-063, SAGE hybrid OA, blocked by Cloudflare on headless fetch) and 133 (MIRAGE, Oxford Academic paywall) remain **pending manual retrieval**.

#### Provisional status: Records #132 and #133

Records #132 (PMID 34637343, PRC-063 methylphenidate for adolescent ADHD) and #133 (PMID 40135470, MIRAGE mirtazapine for chronic insomnia) are currently listed as INCLUDE in `fulltext_screening_decisions.csv` based on HIGH-confidence abstract + ClinicalTrials.gov + QA-audit evidence. Their full-text PDFs are pending manual retrieval. Formal full-text review will be completed once the PDFs are obtained, and the inclusion decision may be revised at that time. Until then, these records should be treated as **provisionally included pending full-text review**.

**Record #113 dropped.** Simultaneously, Record #113 (PMID 41218611, semaglutide for cognitive dysfunction in MDD, *Med* 2026, DOI 10.1016/j.medj.2025.100916) was dropped from the final included list because its full text is unobtainable via every tested retrieval method — no open-access version could be identified via OpenAlex or Crossref metadata (Europe PMC / PubMed Central, publisher OA), and the publisher site and U Calgary institutional proxy both returned paywalls. In the PRISMA 2020 flow, Record #113 is now recorded under "Reports not retrieved" rather than "Studies included".

### Potential bias from dropping Record #113

The single "report not retrieved" (Record #113, PMID 41218611: "Semaglutide for cognitive dysfunction in major depressive disorder", McIntyre et al. 2026, *Med*) is a recent (2026) MDD pharmacotherapy trial. Its exclusion removes one paper from the depression disorder category (currently ~22% of included studies) and one very recent publication from the 2023-2026 temporal window. Given the small absolute impact (1 of 70 eligible studies = 1.4%), we do not expect this exclusion to materially bias the scoping review's conclusions about EDIA reporting trends. The decision to drop was operational (full text unobtainable through any open-access version identified via OpenAlex and Crossref metadata, the library proxy, or a direct request to the authors), not methodological.

**Net effect on counts.**

| Count | Pre-correction | Post-correction |
|-------|----------------|------------------|
| Confirmed MAP (final) | 56 | 56 (unchanged) |
| Forwarded to full-text review | 129 | **134** |
| Assessed for eligibility at full text | 129 | 133 |
| Studies included | 65 | **69** |
| Studies excluded at full text | 64 | 64 (unchanged) |
| Reports not retrieved | 0 | 1 (Record #113) |
| Full-text PDFs in hand | 64 of 65 | **67 of 69** (records 132 and 133 pending) |
