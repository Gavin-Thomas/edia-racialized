# Protocol Registration Statement

**Status**: NOT PRE-REGISTERED

This scoping review was NOT prospectively registered on PROSPERO, OSF
Registries, or any other protocol registration platform prior to its
initiation.

## Context

PROSPERO (International Prospective Register of Systematic Reviews) is
the primary registry for systematic reviews but has historically limited
scoping review registration. OSF Registries is an alternative that accepts
scoping review protocols, but was not used for this project.

## Implications

The absence of prospective registration means:

- Readers should be aware that methodological decisions could have been
  made or modified after work began. Every effort has been made to
  document decisions transparently in this repository, but the repository
  cannot substitute for a time-stamped public protocol.
- Any post-hoc adjustments to scope, inclusion criteria, search strategy,
  or analytic plan are documented in the respective stage READMEs and in
  `04_database_search/reports/search_log.md`.
- Readers should treat this work as a retrospectively documented scoping
  review rather than a prospectively registered one.

## Authorship context

This scoping review is a student-led independent project by a medical student at
the University of Calgary Cumming School of Medicine. It is not supervised by a
faculty principal investigator (PI) and does not have a Canadian senior author.
See `AUTHORS.md` for the full authorship statement. The absence of faculty
oversight, combined with the absence of formal pre-registration, should be
considered by readers when evaluating the review's methodology. Transparency
measures listed above are intended to compensate for both.

## Transparency measures in lieu of pre-registration

In the absence of a registered protocol, the following transparency
measures apply:

- **Full code availability**: All search scripts (`04_database_search/*.py`)
  and screening data are in this public repository under CC BY 4.0.
- **Documented inclusion/exclusion criteria**: See
  `03_inclusion_exclusion/criteria.md` for the full criteria, decision
  rules, and borderline-case handling.
- **Full screening audit trail**: Per-batch decisions in
  `05_screening/batch*_reconciled.csv`, QA audits and corrections in
  `05_screening/qa_audit_corrections.md` and `qa_consolidated_check*.md`,
  and the final authoritative report in `05_screening/SCREENING_COMPLETE.md`.
- **Numeric discrepancies and resolutions**: See
  `04_database_search/reports/search_log.md` for documented artifacts
  (289 empty-ID rows, 83 duplicate IDs) that were identified and
  reconciled rather than hidden.
- **Inter-rater agreement honestly reported**: Both raw string-match
  agreement (~76%, driven by vocabulary drift) and normalized agreement
  (97.8% with Cohen's κ = 0.39) are reported with methodological caveats
  in `05_screening/SCREENING_COMPLETE.md` and
  `05_screening/PRISMA_2020_flow_diagram.md`.

## Recommendation for future work

Subsequent reviews by this team, or derivative work using this dataset,
should be prospectively registered via:

- **PROSPERO** — https://www.crd.york.ac.uk/prospero/  (systematic reviews)
- **OSF Registries** — https://osf.io/registries/  (scoping reviews,
  protocols, and broader research plans)

## Reporting guideline compliance

While not pre-registered, this scoping review aims to comply with the
**PRISMA 2020** and **PRISMA-ScR** reporting guidelines. See
`05_screening/PRISMA_2020_flow_diagram.md` for the PRISMA flow diagram.
A PRISMA-ScR checklist will accompany the final manuscript submission.
