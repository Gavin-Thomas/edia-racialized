# Inclusion/Exclusion Criteria

## Inclusion Criteria
- Interventional randomized clinical trials (parallel, crossover, factorial, adaptive, pragmatic designs)
- Participants with diagnosed or clinically significant mental disorders (DSM-5, ICD-10/11)
- Pharmacological interventions explicitly targeting a DSM-5 diagnosed mental disorder
- **Geographic / site**: At least one recruitment site in Canada (a Canadian recruitment site listed in the paper's methods, ClinicalTrials.gov registry, or supplementary material). Canadian co-authorship alone is NOT sufficient. Canadian senior authorship / PI leadership alone is NOT sufficient — the trial must have enrolled participants at a Canadian location.
  - Multicenter international trials eligible only if Canadian data (or a Canadian site) are explicitly reported
  - **Decision rule for multisite international trials**: If the paper reports that some participants were enrolled at a Canadian site (via author affiliation in the Methods section, a clearly listed Canadian site in the trial registration on ClinicalTrials.gov / EU CTR / WHO ICTRP, or a supplementary site table), include it. If no Canadian enrollment site can be verified, exclude — regardless of whether any author is Canadian-affiliated.
  - **Rationale**: This criterion is simpler and more defensible than inferring Canadian leadership from author affiliations. It aligns the scoping review's population focus (Canadian-recruited participants) with the equity analysis goal (EDIA reporting among Canadian trial participants).
- Main trial results published from 2016 onward (last 10 years)
- Published in English

## Exclusion Criteria
- Observational studies (cohort, case-control, cross-sectional)
- Case reports, small case series (<10 participants)
- Systematic reviews, meta-analyses, scoping reviews, narrative reviews
- Educational or health promotion interventions not targeting diagnosed mental disorders
- Non-pharmacological interventions (psychotherapy-only, neurostimulation-only, device-only)
- Trials conducted entirely outside Canada with no Canadian recruitment site (Canadian authorship alone does not confer eligibility)
- Laboratory, simulation, animal, or methodological trials
- Protocols, registry-only records, narrative reports, secondary analyses without primary results
- Conference abstracts without full publication

## Key Definitions
- **Mental disorders**: Conditions classified in the DSM-5 or ICD-10/11 (including depression, anxiety disorders, psychotic disorders, bipolar/mood disorders, OCD, PTSD, ADHD, eating disorders, substance use disorders, personality disorders, neurodevelopmental disorders, neurocognitive disorders/dementia, sleep-wake disorders)
- **Pharmacotherapy**: Any pharmacological agent used to prevent, treat, or manage a mental disorder (includes combination pharmacotherapy + psychotherapy trials if a pharmacological arm is present)
- **Canadian trial**: Trial with at least one Canadian recruitment site (a Canadian site listed in the paper's methods, ClinicalTrials.gov / EU CTR / WHO ICTRP registration, or supplementary site table). Canadian co-authorship or senior authorship alone is NOT sufficient — the trial must have enrolled participants at a Canadian location.
- **EDIA reporting**: Reporting of any PROGRESS-Plus framework variable:
  - **P**lace of residence
  - **R**ace/ethnicity/racialization
  - **O**ccupation
  - **G**ender/sex
  - **R**eligion
  - **E**ducation
  - **S**ocioeconomic status
  - **S**ocial capital
  - **Plus**: Age, Disability, Sexual orientation/gender identity (SOGI), Intersectional analyses

## Date Range Justification
The 2016-2026 window captures the period following major equity reporting policy milestones:
- 2015: NIH Policy on Inclusion revision
- 2017: ClinicalTrials.gov race/ethnicity results reporting requirement
- 2018: TCPS2 revision (strengthened Chapters 4 and 9)
- 2019: CIHR SGBA+ requirements implemented
- 2020+: Heightened global attention to racial equity in health research
- 2022: CIHR EDI grant requirements strengthened

## Scope Restriction: English-Language Only

The English-language restriction is a **scope restriction**, not merely a study limitation. Its impact is substantial:

- **Quebec represents ~23% of Canada's population** and operates a distinct mental health service system (the Act Respecting Mental Health Services, 2023 reforms). A meaningful proportion of Quebec-led RCTs are published primarily in French, particularly those funded by the FRQS (Fonds de recherche du Québec – Santé).
- French-language journals relevant to this review include *Santé mentale au Québec*, *Revue québécoise de psychologie*, and *La Revue canadienne de psychiatrie* (which publishes bilingual content).
- This restriction introduces **systematic geographic and demographic bias**: Quebec has a higher proportion of francophone racialized communities (particularly Haitian, North African, and Middle Eastern populations) with distinct EDIA reporting patterns not captured by English-language literature.

**Sensitivity analysis (planned):**
A targeted French-language PubMed/Érudit search on 10% of disorder categories (depression and substance use) will be conducted as a sensitivity check to estimate the exclusion rate. This will be reported as a supplementary table in the manuscript.

**Implications for generalizability:**
Findings from this review should be interpreted as reflecting primarily anglophone Canadian research institutions. Claims about "Canadian" RCT EDIA reporting should be qualified accordingly.

**Database selection — API-accessible sources only:**
This review uses four databases with programmatic API access (PubMed, Europe PMC, Scopus, OpenAlex), enabling reproducible, scriptable search execution. PsycINFO (Ovid) and CINAHL (EBSCOhost) were excluded because they lack public APIs and require manual institutional-portal queries, which would compromise pipeline reproducibility. For *pharmacotherapy* RCTs specifically, PsycINFO's unique yield beyond PubMed/Scopus is modest — its primary strength is psychotherapy and psychological assessment literature. The four selected databases collectively index the major biomedical and multidisciplinary literature where pharmacotherapy RCTs are published.

## Screening Scope

**Original plan:** Screen a stratified random sample of 200 records from the eligible set, consistent with rapid review methodology (Garritty et al., *BMJ Evidence-Based Medicine* 2021).

**Actual implementation:** All **10,904 eligible records** were screened at title/abstract level via dual independent review. This was feasible due to automated screening support. The stratified sample of 200 records (generated with `random.seed(42)` for reproducibility) was used as a pilot calibration set but is no longer the primary selection method.

**Result:** 134 records forwarded to full-text review (129 originally, plus 5 QA-upgraded MAP records retroactively propagated on 2026-04-11 — see [`../05_screening/SCREENING_COMPLETE.md`](../05_screening/SCREENING_COMPLETE.md) → "Retroactive Correction"); **69 studies** included for data extraction (67 full text obtained, 2 pending manual retrieval; Record #113 unobtainable and recorded as "Reports not retrieved" per PRISMA 2020). This comprehensive screening strengthens generalizability — findings reflect the full eligible Canadian RCT literature, not a sample.

## Criteria Revisions

**Criterion refinement (2026-04-11)**: The original protocol included "Canadian institutional PI leadership" as an alternative inclusion pathway alongside Canadian recruitment sites. This alternative was removed during audit review because (a) "institutional PI leadership" was not operationalized with specific rules (e.g., senior author vs. corresponding author vs. ClinicalTrials.gov Principal Investigator) and (b) the equity analysis focus is on Canadian-recruited participants, for which recruitment site is the relevant indicator. This change simplifies the criterion and improves reviewer defensibility. Previously included records are retained unless a re-evaluation shows they fail the new recruitment-site criterion — see the audit flag list in the R2 audit report for records that may warrant re-evaluation.
