#!/usr/bin/env python3
"""
Fetch search results from the Scopus (Elsevier) API for a scoping review on
EDIA reporting in Canadian mental health pharmacotherapy RCTs.

API docs: https://dev.elsevier.com/documentation/ScopusSearchAPI.wadl
Requires an API key set via the SCOPUS_API_KEY environment variable.
Uses view=COMPLETE to retrieve abstracts; falls back to STANDARD if needed.
Implements date-based chunking if total results exceed 5000 (API limit).
"""

import csv
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL = "https://api.elsevier.com/content/search/scopus"

API_KEY = os.environ.get("SCOPUS_API_KEY")
if not API_KEY:
    print("ERROR: SCOPUS_API_KEY environment variable is not set.")
    print("  Set it with:  export SCOPUS_API_KEY=your_key_here")
    print("  Obtain a key at: https://dev.elsevier.com/")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "abstracts")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "scopus_results.csv")

PAGE_SIZE = 25  # Scopus max per page
RATE_LIMIT_SECONDS = 1.0
MAX_RETRIES = 3
INITIAL_BACKOFF = 2  # seconds, doubles on each retry
SCOPUS_MAX_RESULTS = 5000  # standard API key limit

# ---------------------------------------------------------------------------
# Search query blocks
# ---------------------------------------------------------------------------

BLOCK_MENTAL = (
    'TITLE-ABS-KEY("mental disorder" OR "mental illness" OR "mental health" '
    'OR psychiatr* OR psychopharmac* OR antidepressant* OR antipsychotic* '
    'OR anxiolytic* OR "mood stabilizer" OR neuroleptic* OR SSRI OR SNRI '
    'OR benzodiazepine* OR lithium OR depress* OR anxiety OR schizophren* '
    'OR psychosis OR bipolar OR mania OR "obsessive compulsive" OR OCD '
    'OR "post-traumatic stress" OR PTSD OR "attention deficit" OR ADHD '
    'OR "anorexia nervosa" OR bulimia OR "eating disorder" '
    'OR "substance use disorder" OR "substance abuse" '
    'OR "personality disorder" OR "autism spectrum" OR insomnia '
    'OR dementia OR Alzheimer*)'
)

BLOCK_RCT = (
    'TITLE-ABS-KEY(randomized OR randomised OR placebo '
    'OR "clinical trial" OR "controlled trial" OR randomly)'
)

BLOCK_CANADA = (
    '(AFFILCOUNTRY(Canada) OR TITLE-ABS-KEY(Canada OR Canadian '
    'OR Ontario OR Quebec OR "British Columbia" OR Alberta '
    'OR Manitoba OR Saskatchewan OR "Nova Scotia" '
    'OR Toronto OR Montreal OR Vancouver OR Ottawa '
    'OR Calgary OR Edmonton OR Winnipeg OR Halifax))'
)


def build_query(year_min=2000, year_max=None):
    """Build the full Scopus query, optionally restricting to a year range."""
    q = f"{BLOCK_MENTAL} AND {BLOCK_RCT} AND {BLOCK_CANADA}"
    if year_max is not None:
        # Inclusive year range for date-based chunking
        q += f" AND PUBYEAR > {year_min - 1} AND PUBYEAR < {year_max + 1}"
    else:
        q += f" AND PUBYEAR > {year_min - 1}"
    q += " AND LANGUAGE(english)"
    return q


# ---------------------------------------------------------------------------
# CSV columns
# ---------------------------------------------------------------------------

CSV_COLUMNS = [
    "pmid", "title", "authors", "journal", "year", "doi",
    "abstract", "scopus_id", "citedby_count",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

USE_COMPLETE_VIEW = True  # will be toggled to False if COMPLETE fails


def _make_request(url, retry=0):
    """Send a GET request to Scopus and return parsed JSON.

    Retries up to MAX_RETRIES times with exponential backoff.
    """
    global USE_COMPLETE_VIEW

    req = urllib.request.Request(url)
    req.add_header("X-ELS-APIKey", API_KEY)
    req.add_header("Accept", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as exc:
        # If COMPLETE view is not allowed (403 or 401), fall back to STANDARD
        if exc.code in (401, 403) and USE_COMPLETE_VIEW and "view=COMPLETE" in url:
            print("  COMPLETE view not permitted. Falling back to STANDARD view.")
            print("  (Abstracts will NOT be available in STANDARD view.)")
            USE_COMPLETE_VIEW = False
            fallback_url = url.replace("view=COMPLETE", "view=STANDARD")
            return _make_request(fallback_url, retry=0)

        if retry < MAX_RETRIES:
            wait = INITIAL_BACKOFF * (2 ** retry)
            print(f"  HTTP {exc.code} error, retrying in {wait}s "
                  f"(attempt {retry + 1}/{MAX_RETRIES})...")
            time.sleep(wait)
            return _make_request(url, retry + 1)
        raise
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        if retry < MAX_RETRIES:
            wait = INITIAL_BACKOFF * (2 ** retry)
            print(f"  Request failed ({exc}), retrying in {wait}s "
                  f"(attempt {retry + 1}/{MAX_RETRIES})...")
            time.sleep(wait)
            return _make_request(url, retry + 1)
        raise


def _extract_record(entry):
    """Pull the fields we need from a single Scopus search result entry."""
    # scopus_id: dc:identifier is like "SCOPUS_ID:12345678"
    raw_id = entry.get("dc:identifier", "")
    scopus_id = raw_id.replace("SCOPUS_ID:", "")

    # year from prism:coverDate (YYYY-MM-DD)
    cover_date = entry.get("prism:coverDate", "")
    year = cover_date[:4] if len(cover_date) >= 4 else ""

    # Authors: prefer full author list from COMPLETE view, fall back to dc:creator
    authors = ""
    author_list = entry.get("author", [])
    if author_list and isinstance(author_list, list):
        names = []
        for auth in author_list:
            name = auth.get("authname", "") or auth.get("surname", "")
            if not name:
                name = auth.get("given-name", "")
            names.append(name)
        authors = "; ".join(n for n in names if n)
    if not authors:
        authors = entry.get("dc:creator", "")

    return {
        "pmid": entry.get("pubmed-id", ""),
        "title": entry.get("dc:title", ""),
        "authors": authors,
        "journal": entry.get("prism:publicationName", ""),
        "year": year,
        "doi": entry.get("prism:doi", ""),
        "abstract": entry.get("dc:description", ""),
        "scopus_id": scopus_id,
        "citedby_count": entry.get("citedby-count", ""),
    }


MAX_RECORDS_PER_QUERY = 5000  # We only need top-cited, not all 20k


def fetch_page(query, start=0, sort=None):
    """Fetch a single page of Scopus results."""
    view = "COMPLETE" if USE_COMPLETE_VIEW else "STANDARD"
    p = {
        "query": query,
        "start": start,
        "count": PAGE_SIZE,
        "view": view,
    }
    if sort:
        p["sort"] = sort
    params = urllib.parse.urlencode(p)
    url = f"{BASE_URL}?{params}"
    return _make_request(url)


def fetch_query(query, label="", sort=None, max_records=None):
    """Fetch pages for a given Scopus query. Returns list of records."""
    records = []
    prefix = f"[{label}] " if label else ""

    # First request to get total
    print(f"{prefix}Fetching page 1 (start=0)...")
    data = fetch_page(query, start=0, sort=sort)

    search_results = data.get("search-results", {})
    total = int(search_results.get("opensearch:totalResults", 0))
    print(f"{prefix}Total results: {total:,}")

    if total == 0:
        return records

    cap = min(total, SCOPUS_MAX_RESULTS)
    if max_records:
        cap = min(cap, max_records)

    if total > cap:
        print(f"{prefix}Will fetch top {cap:,} of {total:,} results")

    # Parse first page
    entries = search_results.get("entry", [])
    if entries and "error" in entries[0]:
        print(f"{prefix}No results: {entries[0].get('error', 'unknown error')}")
        return records

    for entry in entries:
        records.append(_extract_record(entry))

    print(f"{prefix}  Page 1: fetched {len(entries)} "
          f"(total so far: {len(records):,})")

    # Paginate through remaining results
    effective_total = cap
    page = 1
    while len(records) < effective_total:
        page += 1
        start = (page - 1) * PAGE_SIZE

        time.sleep(RATE_LIMIT_SECONDS)

        print(f"{prefix}Fetching page {page} (start={start})...")
        try:
            data = fetch_page(query, start=start, sort=sort)
        except Exception as e:
            print(f"{prefix}  Error on page {page}: {e}")
            print(f"{prefix}  Stopping pagination for this chunk.")
            break

        search_results = data.get("search-results", {})
        entries = search_results.get("entry", [])

        if not entries or (entries and "error" in entries[0]):
            print(f"{prefix}  No more entries. Done with chunk.")
            break

        for entry in entries:
            records.append(_extract_record(entry))

        print(f"{prefix}  Page {page}: fetched {len(entries)} "
              f"(total so far: {len(records):,})")

    return records


# ---------------------------------------------------------------------------
# Date-based chunking for large result sets
# ---------------------------------------------------------------------------

def get_total_for_query(query):
    """Quick count query -- fetch page 1 with count=1 to get total."""
    params = urllib.parse.urlencode({
        "query": query,
        "start": 0,
        "count": 1,
        "view": "STANDARD",
    })
    url = f"{BASE_URL}?{params}"
    data = _make_request(url)
    return int(data.get("search-results", {}).get("opensearch:totalResults", 0))


def fetch_with_chunking():
    """Fetch results sorted by citation count. Uses chunking only if needed."""
    full_query = build_query(year_min=2000)
    print(f"Query length: {len(full_query)} characters")
    print()

    # Check total first
    print("Checking total result count...")
    total = get_total_for_query(full_query)
    print(f"Total results across all years: {total:,}")
    print()

    time.sleep(RATE_LIMIT_SECONDS)

    if total <= SCOPUS_MAX_RESULTS:
        # Fetch all, sorted by citation count
        return fetch_query(full_query, sort="-citedby-count")

    # Need date-based chunking. Sort each chunk by citations descending.
    print(f"Results exceed {SCOPUS_MAX_RESULTS:,} limit. "
          f"Using year-based chunking (sorted by citations)...")
    print()

    all_records = []
    seen_scopus_ids = set()

    current_year = datetime.datetime.now().year
    year_ranges = []
    yr = 2000
    while yr <= current_year:
        yr_end = min(yr + 4, current_year)
        year_ranges.append((yr, yr_end))
        yr = yr_end + 1

    for yr_min, yr_max in year_ranges:
        chunk_query = build_query(year_min=yr_min, year_max=yr_max)
        label = f"{yr_min}-{yr_max}"

        chunk_total = get_total_for_query(chunk_query)
        print(f"Chunk {label}: {chunk_total:,} results")
        time.sleep(RATE_LIMIT_SECONDS)

        if chunk_total == 0:
            continue

        if chunk_total > SCOPUS_MAX_RESULTS:
            # Sub-chunk by individual years
            print(f"  Chunk {label} exceeds limit. Splitting by year...")
            for year in range(yr_min, yr_max + 1):
                sub_query = build_query(year_min=year, year_max=year)
                sub_total = get_total_for_query(sub_query)
                print(f"  Year {year}: {sub_total:,} results")
                time.sleep(RATE_LIMIT_SECONDS)

                if sub_total == 0:
                    continue

                chunk_records = fetch_query(
                    sub_query, label=str(year),
                    sort="-citedby-count",
                    max_records=min(sub_total, SCOPUS_MAX_RESULTS),
                )
                for rec in chunk_records:
                    sid = rec["scopus_id"]
                    if sid and sid not in seen_scopus_ids:
                        seen_scopus_ids.add(sid)
                        all_records.append(rec)
                    elif not sid:
                        all_records.append(rec)

                print(f"  Year {year}: unique total so far: {len(all_records):,}")
                print()
        else:
            chunk_records = fetch_query(
                chunk_query, label=label,
                sort="-citedby-count",
            )
            for rec in chunk_records:
                sid = rec["scopus_id"]
                if sid and sid not in seen_scopus_ids:
                    seen_scopus_ids.add(sid)
                    all_records.append(rec)
                elif not sid:
                    all_records.append(rec)

            print(f"Chunk {label}: unique total so far: {len(all_records):,}")
            print()

    return all_records


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_csv(records):
    """Write records to the output CSV file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(records)

    print(f"\nWrote {len(records):,} records to {OUTPUT_FILE}")


def print_summary(records):
    """Print a summary of the results."""
    unique_pmids = {r["pmid"] for r in records if r["pmid"]}
    with_abstract = sum(1 for r in records if r["abstract"])

    year_counts = {}
    for r in records:
        yr = r["year"] or "Unknown"
        year_counts[yr] = year_counts.get(yr, 0) + 1

    print(f"\nSummary:")
    print(f"  Total records:          {len(records):,}")
    print(f"  Unique PMIDs:           {len(unique_pmids):,}")
    print(f"  Records with abstracts: {with_abstract:,}")
    print(f"  Records without:        {len(records) - with_abstract:,}")
    if not USE_COMPLETE_VIEW:
        print(f"  NOTE: COMPLETE view was not available; abstracts are missing.")
    print(f"\n  Year distribution:")
    for yr in sorted(year_counts.keys()):
        print(f"    {yr}: {year_counts[yr]:,}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Scopus search for EDIA scoping review")
    print("=" * 50)
    print(f"API key: {API_KEY[:8]}...{API_KEY[-4:]}")
    print()

    records = fetch_with_chunking()

    if records:
        write_csv(records)
        print_summary(records)
    else:
        print("\nNo results found.")

    print("\nDone!")


if __name__ == "__main__":
    main()
