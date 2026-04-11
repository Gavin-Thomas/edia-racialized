# Full Text Files — Status Summary

Last updated: 2026-04-11

## Current status: 67 of 69 full texts acquired

Of the **69 included studies**, **67 full texts are available locally** in this folder. **2 records remain pending manual retrieval:**

- **Record #132** — PRC-063 methylphenidate for adolescent ADHD (Weiss et al. 2021, *J Child Adolesc Psychopharmacol*, PMID 34637343, DOI 10.1089/cap.2021.0034). SAGE hybrid open access, currently blocked by Cloudflare on headless fetch. Try in a regular browser: <https://journals.sagepub.com/doi/pdf/10.1089/cap.2021.0034>
- **Record #133** — Mirtazapine for chronic insomnia (MIRAGE, Nguyen et al. 2025, *Age and Ageing*, PMID 40135470, DOI 10.1093/ageing/afaf050). Oxford Academic paywall. Try U Calgary EZproxy: <https://login.ezproxy.lib.ucalgary.ca/login?url=https://doi.org/10.1093/ageing/afaf050>, or email author Patrick V-Q Nguyen (CHUM Pharmacy).

**Record #113 dropped.** The prior "1 pending" study, Record #113 (Semaglutide for cognitive dysfunction in MDD, *Med* 2026, PMID 41218611, DOI 10.1016/j.medj.2025.100916) has been **dropped from the final included list** because its full text could not be obtained via any tested retrieval method. Per PRISMA 2020, it is now recorded under "Reports not retrieved" rather than "Studies included". See [`../05_screening/PRISMA_2020_flow_diagram.md`](../05_screening/PRISMA_2020_flow_diagram.md) and [`../05_screening/SCREENING_COMPLETE.md`](../05_screening/SCREENING_COMPLETE.md) → "Retroactive Correction (2026-04-11)".

**Important:** PDFs and extracted full-text `.txt` files are kept locally and are **not committed to git** (see repository `.gitignore`). This README and the metadata file `ALL_69_LINKS.md` are the only artifacts tracked in version control.

For the authoritative, per-record full-text status (with links), see **`ALL_69_LINKS.md`**.

The older file `PAYWALLED_LINKS.md` is deprecated and retained only as a historical snapshot from 2026-04-03 (updated 2026-04-11 with the current pending list).

## How the 67 full texts were obtained

Full-text retrieval used OpenAlex and Crossref open-access metadata to identify publisher-hosted, PubMed Central (PMC), and Europe PMC copies of each study. For papers without a machine-retrievable open-access version, authors were contacted directly or institutional library access (U Calgary EZproxy) was used.

| Source | Approximate count | Notes |
|--------|-------------------|-------|
| PubMed Central / Europe PMC (open access) | ~30 | Fetched as `.txt` full text via NCBI E-utilities / Europe PMC REST |
| Publisher open-access HTML/PDF (gold/hybrid OA) | ~10 | Direct download where the journal offered free access |
| Other open-access copies identified via OpenAlex / Crossref metadata | ~18 | Author manuscripts, institutional repositories, and preprint/OA mirrors surfaced through OpenAlex `oa_url` and Crossref DOI resolution |
| Manually uploaded by user | ~10 | User-supplied PDFs (e.g., obtained through institutional library access) placed directly into this folder |
| Record #30 (corrected) | 1 | Previously the wrong PDF was downloaded; replaced with correct file |

Note: the counts above are approximate and sum slightly higher than 67 because Record #30 was re-acquired; the net local count is 67 unique records.

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

### Dropped from included list (1 record)

- **Record #113** — Semaglutide for cognitive dysfunction in major depressive disorder
  - Journal: *Med* (Cell Press), 2026
  - PMID: 41218611
  - DOI: 10.1016/j.medj.2025.100916
  - Status: **Dropped from the final included list on 2026-04-11** — unobtainable via any open-access version identified through OpenAlex and Crossref metadata (PubMed Central, Europe PMC, publisher OA), the publisher site, or the institutional proxy. Recorded as "Reports not retrieved" in the PRISMA 2020 flow.

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

- `ALL_69_LINKS.md` — **authoritative** list of all 69 included records with current download status (renamed from `ALL_65_LINKS.md` on 2026-04-11)
- `PAYWALLED_LINKS.md` — DEPRECATED (historical snapshot from 2026-04-03, updated 2026-04-11 to reflect the current pending list)
- `REMAINING_PROXY_URLS.md` — proxy URLs for records previously needing institutional access
