# Full Text Files — Status Summary

Last updated: 2026-04-11

## Current status: 64 of 66 full texts acquired

Of the **66 included studies**, **64 full texts are available locally** in this folder. **2 records remain pending manual retrieval:**

- **Record #132** — PRC-063 methylphenidate for adolescent ADHD (Weiss et al. 2021, *J Child Adolesc Psychopharmacol*, PMID 34637343, DOI 10.1089/cap.2021.0034). SAGE hybrid open access, currently blocked by Cloudflare on headless fetch. Try in a regular browser: <https://journals.sagepub.com/doi/pdf/10.1089/cap.2021.0034>
- **Record #133** — Mirtazapine for chronic insomnia (MIRAGE, Nguyen et al. 2025, *Age and Ageing*, PMID 40135470, DOI 10.1093/ageing/afaf050). Oxford Academic paywall. Try U Calgary EZproxy: <https://login.ezproxy.lib.ucalgary.ca/login?url=https://doi.org/10.1093/ageing/afaf050>, or email author Patrick V-Q Nguyen (CHUM Pharmacy).

**Record #113 dropped.** The prior "1 pending" study, Record #113 (Semaglutide for cognitive dysfunction in MDD, *Med* 2026, PMID 41218611, DOI 10.1016/j.medj.2025.100916) has been **dropped from the final included list** because its full text could not be obtained via any tested retrieval method. Per PRISMA 2020, it is now recorded under "Reports not retrieved" rather than "Studies included".

**Records #20, #42, and #95 dropped (2026-04-11, criterion refinement).** Under the simplified "verified Canadian recruitment site" criterion, three additional records were dropped after a targeted site-verification audit:
- **Record #20** — VIVRE vortioxetine (PMID 37227402): 80 sites across 12 countries, no Canadian site.
- **Record #42** — Sodium benzoate + N-acetylcysteine for schizophrenia (PMID 39144112): 5 sites, all in Pakistan.
- **Record #95** — Mavoglurant for SSRI-resistant OCD (PMID 28044255): 15 sites in Bulgaria, Germany, USA, Czechia, and Switzerland.

Their PDFs remain on disk as audit evidence but they are no longer in the included set. Net included count went from 69 → **66**. See [`../05_screening/PRISMA_2020_flow_diagram.md`](../05_screening/PRISMA_2020_flow_diagram.md) and [`../05_screening/SCREENING_COMPLETE.md`](../05_screening/SCREENING_COMPLETE.md) → "Retroactive Correction (2026-04-11)".

**Important:** PDFs and extracted full-text `.txt` files are kept locally and are **not committed to git** (see repository `.gitignore`). This README and the metadata file `ALL_66_LINKS.md` are the only artifacts tracked in version control.

For the authoritative, per-record full-text status (with links), see **`ALL_66_LINKS.md`**.

The older file `PAYWALLED_LINKS.md` is deprecated and retained only as a historical snapshot from 2026-04-03 (updated 2026-04-11 with the current pending list).

## How the 64 full texts were obtained

Full-text retrieval used OpenAlex and Crossref open-access metadata to identify publisher-hosted, PubMed Central (PMC), and Europe PMC copies of each study. For papers without a machine-retrievable open-access version, authors were contacted directly or institutional library access (U Calgary EZproxy) was used.

| Source | Approximate count | Notes |
|--------|-------------------|-------|
| PubMed Central / Europe PMC (open access) | ~30 | Fetched as `.txt` full text via NCBI E-utilities / Europe PMC REST |
| Publisher open-access HTML/PDF (gold/hybrid OA) | ~10 | Direct download where the journal offered free access |
| Other open-access copies identified via OpenAlex / Crossref metadata | ~18 | Author manuscripts, institutional repositories, and preprint/OA mirrors surfaced through OpenAlex `oa_url` and Crossref DOI resolution |
| Manually uploaded by user | ~10 | User-supplied PDFs (e.g., obtained through institutional library access) placed directly into this folder |
| Record #30 (corrected) | 1 | Previously the wrong PDF was downloaded; replaced with correct file |

Note: the counts above are approximate and reflect the retrieval workflow before the 2026-04-11 criterion-refinement drop of records #20, #42, and #95. Their PDFs remain on disk as audit evidence but are excluded from the analysable corpus; the net included local count is **64 unique records** (of the 66 included studies).

## Outstanding records

### Pending manual retrieval (2 records) — provisionally included

> **Provisional status.** Records #132 and #133 are currently listed as INCLUDE in `../05_screening/fulltext_screening_decisions.csv` based on HIGH-confidence abstract + ClinicalTrials.gov + QA-audit evidence only. Their full-text PDFs are pending manual retrieval, and **formal full-text review has not yet been completed for these two records**. The inclusion decision may be revised once the PDFs are obtained. Until then, treat Records #132 and #133 as **provisionally included pending full-text review**.

- **Record #132** — PRC-063 methylphenidate for adolescent ADHD
  - Authors: Weiss et al., 2021
  - Journal: *Journal of Child and Adolescent Psychopharmacology*
  - PMID: 34637343
  - DOI: 10.1089/cap.2021.0034
  - Retrieval path: SAGE hybrid open access (CC-BY). Cloudflare blocks automated fetch. Open the publisher PDF link in a normal browser: <https://journals.sagepub.com/doi/pdf/10.1089/cap.2021.0034>

- **Record #133** — Mirtazapine for chronic insomnia (MIRAGE trial)
  - Authors: Nguyen et al., 2025
  - Journal: *Age and Ageing*
  - PMID: 40135470
  - DOI: 10.1093/ageing/afaf050
  - Retrieval path: paywalled on Oxford Academic. Try U Calgary EZproxy <https://login.ezproxy.lib.ucalgary.ca/login?url=https://doi.org/10.1093/ageing/afaf050>, or email corresponding author Patrick V-Q Nguyen (CHUM Pharmacy, Montreal).

### Dropped from included list (4 records)

- **Record #113** — Semaglutide for cognitive dysfunction in major depressive disorder
  - Journal: *Med* (Cell Press), 2026
  - PMID: 41218611
  - DOI: 10.1016/j.medj.2025.100916
  - Status: **Dropped from the final included list on 2026-04-11** — unobtainable via any open-access version identified through OpenAlex and Crossref metadata (PubMed Central, Europe PMC, publisher OA), the publisher site, or the institutional proxy. Recorded as "Reports not retrieved" in the PRISMA 2020 flow.

- **Record #20** — VIVRE: Vortioxetine vs. desvenlafaxine in MDD (partial SSRI response)
  - PMID: 37227402
  - DOI: 10.4088/jcp.23m14780
  - Status: **Dropped 2026-04-11 (criterion refinement)** — 80 sites in 12 countries with no Canadian recruitment site. PDF remains on disk as audit evidence.

- **Record #42** — Add-on sodium benzoate + N-acetylcysteine in early schizophrenia-spectrum disorder
  - PMID: 39144112
  - DOI: 10.1093/schizbullopen/sgae004
  - Status: **Dropped 2026-04-11 (criterion refinement)** — 5 sites all in Pakistan; no Canadian recruitment site. PDF remains on disk as audit evidence.

- **Record #95** — Mavoglurant augmentation in SSRI-resistant OCD
  - PMID: 28044255
  - DOI: 10.1007/s12325-016-0468-5
  - Status: **Dropped 2026-04-11 (criterion refinement)** — 15 sites in Bulgaria, Germany, USA, Czechia, and Switzerland; no Canadian recruitment site. PDF remains on disk as audit evidence.

## File naming conventions

Files in this folder generally follow one of these patterns:

- `record_<N>.pdf` — PDF for record `<N>` (manually uploaded or publisher download)
- `record_<N>_oa.pdf` — Open-access PDF identified via OpenAlex / Crossref metadata (author manuscript, institutional repository, or OA mirror)
- `record_<N>_<publisher>_oa.pdf` — Open-access PDF from a named publisher (e.g. `wiley_oa`, `jcp_oa`)
- `record_<N>_PMC<ID>.pdf` — PDF fetched from PubMed Central
- `record_<N>_PMID_<PMID>.txt` — PubMed abstract / metadata stub
- `record_<N>_PMC<ID>_fulltext.txt` — Extracted plain-text full text from PMC
- `record_<N>_fulltext.txt` — Generic extracted full text
- `record_<N>_extracted.pdf` — PDF derived/extracted from another source
- `record_<N>_corrected.pdf` — Replacement PDF after a prior incorrect download

## Related files in this folder

- `ALL_66_LINKS.md` — **authoritative** list of all 66 included records with current download status (renamed from `ALL_65_LINKS.md` → `ALL_69_LINKS.md` on 2026-04-11, then to `ALL_66_LINKS.md` later the same day after the criterion-refinement drop)
- `PAYWALLED_LINKS.md` — DEPRECATED (historical snapshot from 2026-04-03, updated 2026-04-11 to reflect the current pending list)
- `REMAINING_PROXY_URLS.md` — proxy URLs for records previously needing institutional access
