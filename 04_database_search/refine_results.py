#!/usr/bin/env python3
"""
Refine deduplicated search results for the EDIA scoping review on
racialized reporting in Canadian mental health pharmacotherapy RCTs.

Input:  abstracts/combined_deduplicated.csv
Output: abstracts/top_100_cited.csv
        abstracts/refined_all.csv
        reports/search_log.md
"""

import csv
import os
import random
import sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ABSTRACTS_DIR = os.path.join(SCRIPT_DIR, "abstracts")
REPORTS_DIR = os.path.join(SCRIPT_DIR, "reports")

INPUT_FILE = os.path.join(ABSTRACTS_DIR, "combined_deduplicated.csv")
OUTPUT_ALL = os.path.join(ABSTRACTS_DIR, "refined_all.csv")
OUTPUT_TOP = os.path.join(ABSTRACTS_DIR, "stratified_sample_200.csv")
OUTPUT_LOG = os.path.join(REPORTS_DIR, "search_log.md")

YEAR_MIN = 2016
YEAR_MAX = datetime.now().year

EXPECTED_COLUMNS = [
    "pmid", "title", "authors", "journal", "year", "doi",
    "abstract", "sources", "europepmc_id", "openalex_id",
    "scopus_id", "cited_by_count",
]

# Per-database source CSV files (used for PRISMA counts)
SOURCE_FILES = {
    "PubMed": os.path.join(ABSTRACTS_DIR, "pubmed_results.csv"),
    "OpenAlex": os.path.join(ABSTRACTS_DIR, "openalex_results.csv"),
    "Europe PMC": os.path.join(ABSTRACTS_DIR, "europepmc_results.csv"),
    "Scopus": os.path.join(ABSTRACTS_DIR, "scopus_results.csv"),
}


# ── helpers ──────────────────────────────────────────────────────────────

def count_csv_rows(path):
    """Return the number of data rows in a CSV file, or None if missing."""
    if not os.path.isfile(path):
        return None
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        return sum(1 for _ in reader)


def safe_int(value, default=0):
    """Convert a value to int; return *default* on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def has_abstract(row):
    """Return True if the record has a non-empty abstract."""
    text = (row.get("abstract") or "").strip()
    return len(text) > 0


def year_in_range(row):
    """Return True if year parses to an int within [YEAR_MIN, YEAR_MAX]."""
    y = safe_int(row.get("year"), default=None)
    if y is None:
        return False
    return YEAR_MIN <= y <= YEAR_MAX


# ---------------------------------------------------------------------------
# Relevance filter: Canada + Mental Health + RCT
# Applied BEFORE citation ranking so top 100 are actually relevant
# ---------------------------------------------------------------------------

CANADA_TERMS = [
    "canada", "canadian", "canadians",
    "alberta", "british columbia", "manitoba", "new brunswick",
    "newfoundland", "labrador", "nova scotia", "ontario", "quebec",
    "saskatchewan", "prince edward island", "northwest territories",
    "nunavut", "yukon",
    "toronto", "montreal", "vancouver", "ottawa", "calgary", "edmonton",
    "winnipeg", "halifax", "hamilton", "mississauga", "saskatoon", "regina",
    "sherbrooke", "fredericton", "charlottetown", "whitehorse",
    "yellowknife", "iqaluit", "thunder bay", "quebec city", "kingston",
    "sudbury", "st. john", "london ontario", "victoria bc",
]

MENTAL_HEALTH_TERMS = [
    "mental disorder", "mental illness", "mental health", "psychiatr",
    "psychopharmac", "antidepressant", "antipsychotic", "anxiolytic",
    "mood stabiliz", "neuroleptic", "ssri", "snri", "benzodiazepine",
    "lithium", "depress", "major depressive", "dysthymi",
    "anxiety", "panic disorder", "social anxiety", "phobia",
    "generalized anxiety", "agoraphobia",
    "schizophren", "psychosis", "psychotic", "schizoaffective",
    "bipolar", "mania", "manic", "mood disorder",
    "obsessive compulsive", "ocd",
    "post-traumatic stress", "posttraumatic stress", "ptsd",
    "attention deficit", "adhd",
    "anorexia nervosa", "bulimia", "eating disorder", "binge eating",
    "substance use disorder", "substance abuse", "alcohol use disorder",
    "opioid use disorder", "drug dependence", "alcohol dependence",
    "personality disorder", "borderline personality",
    "autism spectrum", "autistic",
    "insomnia", "sleep disorder",
    "neurocognitive disorder", "dementia", "alzheimer",
    "neurodevelopmental", "adjustment disorder", "gambling disorder",
    "somatic symptom",
]

RCT_TERMS = [
    "randomized", "randomised", "placebo", "double-blind", "double blind",
    "single-blind", "single blind", "clinical trial", "controlled trial",
    "randomly", "random allocation", "random assignment",
    "crossover", "cross-over", "pragmatic trial", "adaptive trial",
    "n-of-1", "drug therapy",
]

# Negative filter: exclude systematic reviews, meta-analyses, etc.
EXCLUDE_TITLE_TERMS = [
    "systematic review", "meta-analysis", "meta analysis",
    "scoping review", "umbrella review", "rapid review",
    "narrative review", "integrative review", "literature review",
]


def is_review(row):
    """Return True if the record is a review/meta-analysis.

    Checks title first (primary signal). Also checks for explicit review-purpose
    language in the abstract to catch records where the review type is stated in
    the body but not the title (e.g., "Evidence synthesis on...", "An overview...").
    Abstract-only matching requires stronger anchoring phrases to avoid false
    positives on primary trials that *discuss* review methodology.
    """
    title = (row.get("title") or "").lower()
    if any(t in title for t in EXCLUDE_TITLE_TERMS):
        return True

    # Abstract-level check: look for explicit review-purpose declarations only
    abstract = (row.get("abstract") or "").lower()
    ABSTRACT_REVIEW_PHRASES = [
        "we conducted a systematic review",
        "we performed a systematic review",
        "we undertook a systematic review",
        "this systematic review",
        "this meta-analysis",
        "this scoping review",
        "we conducted a meta-analysis",
        "we performed a meta-analysis",
        "background: systematic review",
        "objective: systematic review",
        "purpose: systematic review",
    ]
    return any(phrase in abstract for phrase in ABSTRACT_REVIEW_PHRASES)


def is_relevant(row):
    """Return True if record mentions Canada + mental health + RCT terms.

    Canada detection: check title/abstract for Canada terms, OR check if
    the record's source databases include affiliation-based retrieval
    (Scopus uses AFFILCOUNTRY, PubMed uses [ad], Europe PMC uses AFF).
    Records from these databases that passed the original search are
    assumed to have a Canadian affiliation even if "Canada" isn't in the
    abstract text.
    """
    text = ((row.get("title") or "") + " " + (row.get("abstract") or "")).lower()
    has_mental = any(t in text for t in MENTAL_HEALTH_TERMS)
    has_rct = any(t in text for t in RCT_TERMS)

    # Canada: check text first
    has_canada = any(t in text for t in CANADA_TERMS)

    # If not in text, accept records that came from affiliation-based
    # database searches (Scopus/PubMed/Europe PMC all search affiliations)
    if not has_canada:
        sources = (row.get("sources") or "").lower()
        # Records found in Scopus or PubMed were retrieved via affiliation
        # fields (AFFILCOUNTRY, [ad]) so they have a Canadian connection
        if "scopus" in sources or "pubmed" in sources or "europe pmc" in sources:
            has_canada = True

    return has_canada and has_mental and has_rct


# ── main pipeline ────────────────────────────────────────────────────────

def main():
    # --- 0. Validate input ---
    if not os.path.isfile(INPUT_FILE):
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        print("Run the deduplication step first to produce combined_deduplicated.csv.")
        sys.exit(1)

    os.makedirs(REPORTS_DIR, exist_ok=True)

    # --- 1. Read deduplicated records ---
    print(f"Reading {INPUT_FILE} ...")
    with open(INPUT_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        all_records = list(reader)

    total_dedup = len(all_records)
    print(f"  Deduplicated records loaded: {total_dedup}")

    # --- 2. Filter: require abstract ---
    before_abstract = len(all_records)
    records = [r for r in all_records if has_abstract(r)]
    removed_no_abstract = before_abstract - len(records)
    print(f"  Removed (no abstract): {removed_no_abstract}")

    # --- 3. Filter: year range ---
    before_year = len(records)
    records = [r for r in records if year_in_range(r)]
    removed_year = before_year - len(records)
    print(f"  Removed (year outside {YEAR_MIN}-{YEAR_MAX}): {removed_year}")

    # --- 3b. Filter: relevance (Canada + mental health + RCT) ---
    before_relevance = len(records)
    records = [r for r in records if is_relevant(r)]
    removed_relevance = before_relevance - len(records)
    print(f"  Removed (not relevant - missing Canada/MH/RCT terms): {removed_relevance}")

    # --- 3c. Filter: exclude systematic reviews and meta-analyses ---
    before_sr = len(records)
    records = [r for r in records if not is_review(r)]
    removed_sr = before_sr - len(records)
    print(f"  Removed (systematic reviews/meta-analyses): {removed_sr}")

    total_after_filters = len(records)
    print(f"  Records after all filters: {total_after_filters}")

    # --- 4. Add citations_per_year ---
    current_year = datetime.now().year
    for r in records:
        cites = safe_int(r.get("cited_by_count"))
        pub_year = safe_int(r.get("year"), default=None)
        if pub_year and cites > 0:
            years_since = max(1, current_year - pub_year + 1)
            r["citations_per_year"] = str(round(cites / years_since, 1))
        else:
            r["citations_per_year"] = ""

    # --- 5. Sort by cited_by_count descending ---
    records.sort(key=lambda r: safe_int(r.get("cited_by_count")), reverse=True)

    # --- 6. Add rank (by citation count) ---
    for i, r in enumerate(records, start=1):
        r["rank"] = str(i)

    # --- 7. Stratified random sample of 200 ---
    # Stratify by time period and disorder category for representative sampling
    random.seed(42)  # reproducibility

    def get_time_stratum(row):
        y = safe_int(row.get("year"), default=2020)
        if y <= 2019:
            return "2016-2019"
        elif y <= 2022:
            return "2020-2022"
        else:
            return "2023-2026"

    def get_disorder_stratum(row):
        text = ((row.get("title") or "") + " " + (row.get("abstract") or "")).lower()
        if any(t in text for t in ["depress", "major depressive", "dysthymi", "postpartum depression"]):
            return "depression"
        if any(t in text for t in ["schizophren", "psychosis", "psychotic", "schizoaffective"]):
            return "psychotic"
        if any(t in text for t in ["anxiety", "panic disorder", "phobia", "generalized anxiety", "ocd", "obsessive compulsive", "ptsd", "post-traumatic"]):
            return "anxiety_trauma_ocd"
        if any(t in text for t in ["substance use", "substance abuse", "alcohol", "opioid", "drug dependence"]):
            return "substance_use"
        if any(t in text for t in ["bipolar", "mania", "manic", "mood disorder"]):
            return "bipolar_mood"
        if any(t in text for t in ["adhd", "attention deficit"]):
            return "adhd"
        if any(t in text for t in ["dementia", "alzheimer", "neurocognitive"]):
            return "dementia"
        return "other"

    # Assign stable integer indices before sampling so we can track membership
    # without relying on id() (which is memory-address-based and fragile).
    for i, r in enumerate(records):
        r["_idx"] = i

    # Build strata
    from collections import defaultdict
    strata = defaultdict(list)
    for r in records:
        key = (get_time_stratum(r), get_disorder_stratum(r))
        strata[key].append(r)

    # Proportional allocation with minimum 1 per non-empty stratum
    target_n = min(200, total_after_filters)
    sample = []
    stratum_counts = {}

    # First pass: allocate proportionally
    for key, recs in sorted(strata.items()):
        proportion = len(recs) / total_after_filters
        n_alloc = max(1, round(proportion * target_n))
        chosen = random.sample(recs, min(n_alloc, len(recs)))
        sample.extend(chosen)
        stratum_counts[key] = len(chosen)

    # If over target, trim randomly; if under, add more from largest strata.
    # Use _idx set for O(1) membership checks (avoids O(n²) dict comparisons).
    sample_idx_set = {r["_idx"] for r in sample}
    if len(sample) > target_n:
        sample = random.sample(sample, target_n)
        sample_idx_set = {r["_idx"] for r in sample}
    elif len(sample) < target_n:
        remaining = [r for r in records if r["_idx"] not in sample_idx_set]
        extra = random.sample(remaining, min(target_n - len(sample), len(remaining)))
        sample.extend(extra)
        sample_idx_set = {r["_idx"] for r in sample}

    # Sort sample by citations_per_year (not raw citations) to avoid temporal bias:
    # raw citation counts systematically favour older papers regardless of quality.
    # citations_per_year normalizes for time-in-print, giving recent trials a fair rank.
    # Falls back to raw cited_by_count for records missing citations_per_year.
    def _cpy_key(r):
        cpy = r.get("citations_per_year", "")
        try:
            return float(cpy)
        except (ValueError, TypeError):
            return 0.0

    sample.sort(key=_cpy_key, reverse=True)
    for i, r in enumerate(sample, start=1):
        r["sample_rank"] = str(i)

    # Flag in full set using stable _idx (not id() which is memory-address-based)
    for r in records:
        r["in_sample"] = "True" if r["_idx"] in sample_idx_set else "False"
    # Remove temporary index field before writing output
    for r in records:
        del r["_idx"]

    print(f"  Stratified sample: {len(sample)} records")
    print(f"  Strata breakdown:")
    for key in sorted(stratum_counts):
        total_in_stratum = len(strata[key])
        print(f"    {key[0]} / {key[1]}: {stratum_counts[key]} sampled / {total_in_stratum} available")

    # --- 8. Write refined_all.csv ---
    out_columns = EXPECTED_COLUMNS + ["citations_per_year", "rank", "in_sample"]
    print(f"\nWriting {OUTPUT_ALL} ({len(records)} records) ...")
    with open(OUTPUT_ALL, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)

    # --- 9. Write stratified sample CSV ---
    sample_columns = EXPECTED_COLUMNS + ["citations_per_year", "sample_rank"]
    print(f"Writing {OUTPUT_TOP} ({len(sample)} records) ...")
    with open(OUTPUT_TOP, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=sample_columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(sample)

    # --- 9. Gather per-database counts for PRISMA log ---
    db_counts = {}
    combined_total = 0
    for name, path in SOURCE_FILES.items():
        n = count_csv_rows(path)
        if n is not None:
            db_counts[name] = n
            combined_total += n

    # --- 10. Write search_log.md ---
    print(f"Writing {OUTPUT_LOG} ...")
    write_search_log(
        db_counts=db_counts,
        combined_total=combined_total,
        total_dedup=total_dedup,
        removed_no_abstract=removed_no_abstract,
        removed_year=removed_year,
        removed_relevance=removed_relevance,
        removed_sr=removed_sr,
        total_after_filters=total_after_filters,
        sample_count=len(sample),
    )

    # --- 11. Summary ---
    print("\n" + "=" * 60)
    print("REFINEMENT SUMMARY")
    print("=" * 60)
    for name, n in db_counts.items():
        print(f"  {name:20s} {n:>7,} records")
    if db_counts:
        print(f"  {'Combined (raw)':20s} {combined_total:>7,} records")
    print(f"  {'After deduplication':20s} {total_dedup:>7,} records")
    print(f"  {'Removed (no abstract)':20s} {removed_no_abstract:>7,}")
    print(f"  {'Removed (year filter)':20s} {removed_year:>7,}")
    print(f"  {'Removed (not relevant)':20s} {removed_relevance:>7,}")
    print(f"  {'Removed (reviews/MAs)':20s} {removed_sr:>7,}")
    print(f"  {'After all filters':20s} {total_after_filters:>7,} records")
    print(f"  {'Stratified sample':20s} {len(sample):>7,} records")
    print("=" * 60)
    print("Done.")


# ── PRISMA-style search log ─────────────────────────────────────────────

def write_search_log(
    db_counts,
    combined_total,
    total_dedup,
    removed_no_abstract,
    removed_year,
    removed_relevance,
    removed_sr,
    total_after_filters,
    sample_count,
):
    today = datetime.now().strftime("%Y-%m-%d")

    lines = []
    lines.append("# Search and Refinement Log")
    lines.append("")
    lines.append("## EDIA Reporting in Canadian Mental Health Pharmacotherapy RCTs")
    lines.append("")
    lines.append(f"**Date of search refinement:** {today}")
    lines.append("")

    # Per-database counts
    lines.append("## Database Search Results")
    lines.append("")
    lines.append("| Database | Records Retrieved |")
    lines.append("|----------|------------------:|")
    for name, n in db_counts.items():
        lines.append(f"| {name} | {n:,} |")
    if db_counts:
        lines.append(f"| **Combined total** | **{combined_total:,}** |")
    else:
        lines.append("| *(no source CSVs found)* | - |")
    lines.append("")

    # Dedup and filtering
    lines.append("## Deduplication and Filtering")
    lines.append("")
    lines.append(f"- Records after deduplication: **{total_dedup:,}**")
    duplicates_removed = combined_total - total_dedup if combined_total > 0 else 0
    if combined_total > 0:
        lines.append(f"- Duplicates removed: {duplicates_removed:,}")
    lines.append(f"- Records removed (no abstract): {removed_no_abstract:,}")
    lines.append(f"- Records removed (year outside {YEAR_MIN}-{YEAR_MAX}): {removed_year:,}")
    lines.append(f"- Records removed (not relevant - missing Canada/MH/RCT): {removed_relevance:,}")
    lines.append(f"- Records removed (systematic reviews/meta-analyses): {removed_sr:,}")
    lines.append(f"- **Records after all filters: {total_after_filters:,}**")
    lines.append(f"- Stratified random sample for extraction: {sample_count}")
    lines.append("")

    # PRISMA-style text flow diagram
    lines.append("## PRISMA-Style Flow Diagram")
    lines.append("")
    lines.append("```")
    lines.append("IDENTIFICATION")
    lines.append("=" * 60)
    for name, n in db_counts.items():
        lines.append(f"  {name}: {n:,} records")
    lines.append(f"  Combined total: {combined_total:,} records")
    lines.append("")
    lines.append("              |")
    lines.append("              v")
    lines.append("")
    lines.append("DEDUPLICATION")
    lines.append("=" * 60)
    if combined_total > 0:
        lines.append(f"  Duplicates removed: {duplicates_removed:,}")
    lines.append(f"  Unique records: {total_dedup:,}")
    lines.append("")
    lines.append("              |")
    lines.append("              v")
    lines.append("")
    lines.append("SCREENING / FILTERING")
    lines.append("=" * 60)
    lines.append(f"  Excluded - no abstract:                {removed_no_abstract:,}")
    lines.append(f"  Excluded - year outside {YEAR_MIN}-{YEAR_MAX}:     {removed_year:,}")
    lines.append(f"  Excluded - not relevant (Canada+MH+RCT): {removed_relevance:,}")
    lines.append(f"  Excluded - systematic reviews/MAs:       {removed_sr:,}")
    lines.append(f"  Total excluded at filtering:            {removed_no_abstract + removed_year + removed_relevance + removed_sr:,}")
    lines.append("")
    lines.append("              |")
    lines.append("              v")
    lines.append("")
    lines.append("REFINED SET")
    lines.append("=" * 60)
    lines.append(f"  Records eligible for screening: {total_after_filters:,}")
    lines.append(f"  Stratified random sample for extraction: {sample_count}")
    lines.append("```")
    lines.append("")

    # Output files
    lines.append("## Output Files")
    lines.append("")
    lines.append("| File | Description |")
    lines.append("|------|-------------|")
    lines.append("| `abstracts/refined_all.csv` | All eligible records after filtering, sorted by citations, with rank |")
    lines.append("| `abstracts/stratified_sample_200.csv` | Stratified random sample (n=200) for data extraction |")
    lines.append("| `reports/dedup_report.md` | Deduplication overlap statistics |")
    lines.append("| `reports/search_log.md` | This log file |")
    lines.append("")

    with open(OUTPUT_LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
