# screened_results.csv — Legacy / Stub File Notice

**Status:** LEGACY — retained for backward compatibility only.

## What this file is

`screened_results.csv` in this directory contains only 16 data rows (plus 1 header row = 17 total lines). It holds a small set of entries with columns:

```
id, title, final_decision, category, vote_count, conflict_flag, reconciliation_notes
```

This is **NOT** the authoritative output of the abstract-screening stage. The actual scoping review screened **10,904 records** over 73 batches.

## Why it exists

This CSV appears to be a stub or leftover from an earlier pipeline iteration. It is referenced by `screening_progress.yaml` (as `output_file`) so it has been retained in place rather than renamed or deleted.

## Where the real screening outputs live

For the canonical, full screening outputs see:

- **Per-batch screening CSVs** — see `batch_*_screened.csv` files in this directory
- **Aggregate / reconciled post-QA results** — see `fulltext_screening_decisions.csv` and `included_for_fulltext_review.csv`
- **Running totals and audit trail** — see `screening_progress.yaml`, `qa_audit_corrections.md`, and `SCREENING_COMPLETE.md`
- **PRISMA flow numbers** — see `PRISMA_2020_flow_diagram.md`

Post-QA totals (from `screening_progress.yaml`):

- Records screened: 10,904
- Confirmed MAP (Include): 56
- UNCERTAIN forwarded to full-text: 38
- Excluded: 10,810
- Total forwarded to full-text review: 134
- Included after full-text review: **69**

## Do not delete

This stub file is referenced by `screening_progress.yaml`. Deleting it may break tooling that resolves that reference. If the pipeline is refactored so `screening_progress.yaml` no longer needs this path, the CSV can then be safely removed.
