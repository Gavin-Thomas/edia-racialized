#!/usr/bin/env python3
"""
Fetch search results from Europe PMC REST API for a scoping review on
EDIA reporting in Canadian mental health pharmacotherapy RCTs.

API docs: https://europepmc.org/RestfulWebService
No API key required. Uses cursorMark pagination with pageSize=1000.
"""

import csv
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "abstracts")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "europepmc_results.csv")

PAGE_SIZE = 1000
RATE_LIMIT_SECONDS = 0.5
MAX_RETRIES = 3
INITIAL_BACKOFF = 2  # seconds, doubles on each retry

# ---------------------------------------------------------------------------
# Search query
# ---------------------------------------------------------------------------

# Europe PMC: TITLE_ABS supports wildcards (*) but MeSH_TERM is unreliable.
# Use comprehensive free-text terms to compensate.
BLOCK_MENTAL = (
    '(TITLE_ABS:psychiatr* OR TITLE_ABS:"mental illness" OR TITLE_ABS:"mental disorder" '
    'OR TITLE_ABS:"mental health" OR TITLE_ABS:psychopatholog* OR TITLE_ABS:psychopharmac* '
    'OR TITLE_ABS:antidepressant* OR TITLE_ABS:antipsychotic* OR TITLE_ABS:anxiolytic* '
    'OR TITLE_ABS:"mood stabiliz*" OR TITLE_ABS:neuroleptic* '
    'OR TITLE_ABS:SSRI OR TITLE_ABS:SNRI OR TITLE_ABS:benzodiazepine* OR TITLE_ABS:lithium '
    'OR TITLE_ABS:depress* OR TITLE_ABS:"major depressive" OR TITLE_ABS:dysthymi* '
    'OR TITLE_ABS:"postpartum depression" OR TITLE_ABS:"perinatal depression" '
    'OR TITLE_ABS:anxiety OR TITLE_ABS:"panic disorder" OR TITLE_ABS:"social anxiety" '
    'OR TITLE_ABS:phobia* OR TITLE_ABS:"generalized anxiety" OR TITLE_ABS:agoraphobia '
    'OR TITLE_ABS:schizophren* OR TITLE_ABS:psychosis OR TITLE_ABS:psychotic '
    'OR TITLE_ABS:schizoaffective '
    'OR TITLE_ABS:bipolar OR TITLE_ABS:mania OR TITLE_ABS:manic OR TITLE_ABS:"mood disorder" '
    'OR TITLE_ABS:"obsessive compulsive" OR TITLE_ABS:OCD '
    'OR TITLE_ABS:"post-traumatic stress" OR TITLE_ABS:"posttraumatic stress" OR TITLE_ABS:PTSD '
    'OR TITLE_ABS:"attention deficit" OR TITLE_ABS:ADHD '
    'OR TITLE_ABS:"anorexia nervosa" OR TITLE_ABS:bulimia OR TITLE_ABS:"eating disorder" '
    'OR TITLE_ABS:"binge eating" '
    'OR TITLE_ABS:"substance use disorder" OR TITLE_ABS:"substance abuse" '
    'OR TITLE_ABS:"alcohol use disorder" OR TITLE_ABS:"opioid use disorder" '
    'OR TITLE_ABS:"drug dependence" OR TITLE_ABS:"alcohol dependence" '
    'OR TITLE_ABS:"personality disorder" OR TITLE_ABS:"borderline personality" '
    'OR TITLE_ABS:"autism spectrum" OR TITLE_ABS:autistic '
    'OR TITLE_ABS:insomnia OR TITLE_ABS:"sleep disorder" '
    'OR TITLE_ABS:"neurocognitive disorder" OR TITLE_ABS:dementia OR TITLE_ABS:Alzheimer*)'
)

BLOCK_RCT = (
    '(TITLE_ABS:"randomized" OR TITLE_ABS:"randomised" '
    'OR TITLE_ABS:"placebo" OR TITLE_ABS:"clinical trial" '
    'OR TITLE_ABS:"controlled trial" OR TITLE_ABS:"randomly" '
    'OR TITLE_ABS:"drug therapy" OR TITLE_ABS:"crossover" '
    'OR TITLE_ABS:"double-blind" OR TITLE_ABS:"single-blind")'
)

BLOCK_CANADA = (
    '(TITLE_ABS:"Canada" OR TITLE_ABS:"Canadian" OR AFF:"Canada" '
    'OR TITLE_ABS:"Alberta" OR TITLE_ABS:"British Columbia" '
    'OR TITLE_ABS:"Manitoba" OR TITLE_ABS:"New Brunswick" '
    'OR TITLE_ABS:"Newfoundland" OR TITLE_ABS:"Nova Scotia" '
    'OR TITLE_ABS:"Ontario" OR TITLE_ABS:"Quebec" '
    'OR TITLE_ABS:"Saskatchewan" OR TITLE_ABS:"Prince Edward Island" '
    'OR TITLE_ABS:"Nunavut" OR TITLE_ABS:"Yukon" '
    'OR TITLE_ABS:"Toronto" OR TITLE_ABS:"Montreal" '
    'OR TITLE_ABS:"Vancouver" OR TITLE_ABS:"Ottawa" '
    'OR TITLE_ABS:"Calgary" OR TITLE_ABS:"Edmonton" '
    'OR TITLE_ABS:"Winnipeg" OR TITLE_ABS:"Halifax" '
    'OR TITLE_ABS:"Hamilton")'
)

QUERY = (
    f"{BLOCK_MENTAL} AND {BLOCK_RCT} AND {BLOCK_CANADA} "
    'AND PUB_YEAR:[2000 TO 2026] AND LANG:"eng"'
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

CSV_COLUMNS = [
    "pmid", "title", "authors", "journal", "year", "doi",
    "abstract", "europepmc_id",
]


def _make_request(params: dict, retry: int = 0) -> dict:
    """Send a GET request to Europe PMC and return parsed JSON.

    Retries up to MAX_RETRIES times with exponential backoff.
    """
    qs = urllib.parse.urlencode(params)
    url = f"{BASE_URL}?{qs}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        # Don't retry client errors (4xx) - they won't succeed on retry
        if isinstance(exc, urllib.error.HTTPError) and 400 <= exc.code < 500:
            raise
        if retry < MAX_RETRIES:
            wait = INITIAL_BACKOFF * (2 ** retry)
            print(f"  Request failed ({exc}), retrying in {wait}s "
                  f"(attempt {retry + 1}/{MAX_RETRIES})...")
            time.sleep(wait)
            return _make_request(params, retry + 1)
        raise


def _extract_record(result: dict) -> dict:
    """Pull the fields we need from a single Europe PMC result object."""
    return {
        "pmid": result.get("pmid", ""),
        "title": result.get("title", ""),
        "authors": result.get("authorString", ""),
        "journal": result.get("journalTitle", ""),
        "year": result.get("pubYear", ""),
        "doi": result.get("doi", ""),
        "abstract": result.get("abstractText", ""),
        "europepmc_id": result.get("pmcid", "") or result.get("id", ""),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def fetch_all() -> list[dict]:
    """Page through all Europe PMC results and return a list of records."""
    records: list[dict] = []
    cursor_mark = "*"  # initial cursor
    batch = 0

    while True:
        batch += 1
        params = {
            "query": QUERY,
            "format": "json",
            "pageSize": PAGE_SIZE,
            "cursorMark": cursor_mark,
            "resultType": "core",  # includes abstracts
        }

        print(f"Batch {batch}: fetching (cursorMark={cursor_mark[:20]}...) ...")
        data = _make_request(params)

        result_list = data.get("resultList", {}).get("result", [])
        if not result_list:
            print("  No more results returned. Done.")
            break

        for item in result_list:
            records.append(_extract_record(item))

        print(f"  Received {len(result_list)} results "
              f"(total so far: {len(records)})")

        # Check for next cursor
        next_cursor = data.get("nextCursorMark")
        if not next_cursor or next_cursor == cursor_mark:
            print("  Reached last page. Done.")
            break

        cursor_mark = next_cursor
        time.sleep(RATE_LIMIT_SECONDS)

    return records


def write_csv(records: list[dict]) -> None:
    """Write records to the output CSV file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(records)

    print(f"\nWrote {len(records)} records to {OUTPUT_FILE}")


def main() -> None:
    print("Europe PMC search for EDIA scoping review")
    print("=" * 50)
    print(f"Query length: {len(QUERY)} characters")
    print()

    records = fetch_all()

    if records:
        write_csv(records)
    else:
        print("No results found.")

    # Summary
    unique_pmids = {r["pmid"] for r in records if r["pmid"]}
    print(f"\nSummary:")
    print(f"  Total records: {len(records)}")
    print(f"  Unique PMIDs:  {len(unique_pmids)}")
    print(f"  Records with abstracts: "
          f"{sum(1 for r in records if r['abstract'])}")


if __name__ == "__main__":
    main()
