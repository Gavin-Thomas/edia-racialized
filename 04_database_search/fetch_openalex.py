#!/usr/bin/env python3
"""
Fetch search results from the OpenAlex API for a scoping review on
EDIA reporting in Canadian mental health pharmacotherapy RCTs.

Two-pass search strategy:
  Pass 1 – Affiliation-based: filter by institutions.country_code:CA
  Pass 2 – Text-based: search for "Canada/Canadian" in title/abstract

Results are deduplicated by OpenAlex ID and saved to CSV.
Uses only the Python 3 standard library.
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

BASE_URL = "https://api.openalex.org/works"
MAILTO = "edia.review@example.com"
PER_PAGE = 200
RATE_LIMIT_DELAY = 0.2  # seconds between requests
MAX_RETRIES = 3
BACKOFF_BASE = 2  # exponential backoff multiplier

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "abstracts")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "openalex_results.csv")

CSV_COLUMNS = [
    "pmid",
    "title",
    "authors",
    "journal",
    "year",
    "doi",
    "abstract",
    "openalex_id",
    "cited_by_count",
]

# ---------------------------------------------------------------------------
# Search definitions (two passes)
# ---------------------------------------------------------------------------

# OpenAlex 'search' is relevance-based full-text (no Boolean operators).
# We use multiple focused passes with different keyword sets and filters,
# then deduplicate. Each search string is just space-separated keywords;
# OpenAlex ranks by relevance to these terms.
SEARCHES = [
    # Pass 1a: Canadian institutions + mental health pharmacotherapy RCT terms
    {
        "label": "Pass 1a – CA affiliation + psych drug RCT terms",
        "filter": (
            "from_publication_date:2000-01-01,"
            "to_publication_date:2026-12-31,"
            "language:en,"
            "type:article,"
            "institutions.country_code:CA"
        ),
        "search": "randomized placebo clinical trial depression anxiety schizophrenia antidepressant antipsychotic pharmacotherapy",
    },
    # Pass 1b: Canadian institutions + broader mental disorder terms
    {
        "label": "Pass 1b – CA affiliation + broader mental disorder terms",
        "filter": (
            "from_publication_date:2000-01-01,"
            "to_publication_date:2026-12-31,"
            "language:en,"
            "type:article,"
            "institutions.country_code:CA"
        ),
        "search": "randomized placebo bipolar PTSD ADHD OCD eating disorder substance use disorder personality disorder insomnia dementia",
    },
    # Pass 2: Text mentions of Canada + mental health RCT terms
    {
        "label": "Pass 2 – Text-based (Canada in title/abstract)",
        "filter": (
            "from_publication_date:2000-01-01,"
            "to_publication_date:2026-12-31,"
            "language:en,"
            "type:article"
        ),
        "search": "Canada Canadian randomized placebo mental disorder depression schizophrenia bipolar anxiety antidepressant antipsychotic",
    },
]

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def reconstruct_abstract(inverted_index):
    """Reconstruct plain-text abstract from OpenAlex inverted index."""
    if not inverted_index:
        return ""
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)


def extract_pmid(ids_dict):
    """Extract bare PMID from the ids object."""
    pmid_url = ids_dict.get("pmid", "") if ids_dict else ""
    if pmid_url:
        return pmid_url.replace("https://pubmed.ncbi.nlm.nih.gov/", "").strip("/")
    return ""


def extract_doi(ids_dict):
    """Extract bare DOI from the ids object."""
    doi_url = ids_dict.get("doi", "") if ids_dict else ""
    if doi_url:
        return doi_url.replace("https://doi.org/", "")
    return ""


def extract_openalex_id(raw_id):
    """Strip the URL prefix from an OpenAlex ID."""
    if raw_id:
        return raw_id.replace("https://openalex.org/", "")
    return ""


def build_authors(authorships):
    """Build a semicolon-separated author string."""
    if not authorships:
        return ""
    names = []
    for authorship in authorships:
        author = authorship.get("author", {})
        name = author.get("display_name", "")
        if name:
            names.append(name)
    return "; ".join(names)


def parse_work(work):
    """Parse a single OpenAlex work record into a flat dict."""
    ids = work.get("ids", {})
    primary_location = work.get("primary_location") or {}
    source = primary_location.get("source") or {}

    return {
        "pmid": extract_pmid(ids),
        "title": work.get("title", "") or "",
        "authors": build_authors(work.get("authorships", [])),
        "journal": source.get("display_name", "") or "",
        "year": work.get("publication_year", ""),
        "doi": extract_doi(ids),
        "abstract": reconstruct_abstract(work.get("abstract_inverted_index")),
        "openalex_id": extract_openalex_id(work.get("id", "")),
        "cited_by_count": work.get("cited_by_count", 0),
    }


def fetch_url(url):
    """Fetch a URL with retry logic and exponential backoff."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": f"EDIA-Review/1.0 (mailto:{MAILTO})"},
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
            wait = BACKOFF_BASE ** attempt
            print(f"  [retry {attempt}/{MAX_RETRIES}] {exc} – waiting {wait}s")
            if attempt == MAX_RETRIES:
                raise
            time.sleep(wait)


def run_search(search_def):
    """
    Run a single paginated OpenAlex search.
    Returns a list of parsed work dicts.
    """
    label = search_def["label"]
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")

    params = {
        "mailto": MAILTO,
        "per_page": str(PER_PAGE),
        "filter": search_def["filter"],
        "search": search_def["search"],
        "cursor": "*",
    }

    results = []
    page = 0

    while True:
        page += 1
        url = BASE_URL + "?" + urllib.parse.urlencode(params)
        print(f"  Fetching page {page} … ", end="", flush=True)

        data = fetch_url(url)
        meta = data.get("meta", {})
        works = data.get("results", [])

        total = meta.get("count", "?")
        print(f"got {len(works)} results (total: {total})")

        for work in works:
            results.append(parse_work(work))

        next_cursor = meta.get("next_cursor")
        if not next_cursor or len(works) == 0:
            break

        params["cursor"] = next_cursor
        time.sleep(RATE_LIMIT_DELAY)

    print(f"  Finished {label}: {len(results)} records retrieved.")
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_results = []
    for search_def in SEARCHES:
        results = run_search(search_def)
        all_results.extend(results)

    # Deduplicate by OpenAlex ID (preferred), then DOI, then title+year+journal
    seen = set()
    unique = []
    for rec in all_results:
        key = rec["openalex_id"] or rec["doi"]
        if not key:
            # Fallback: combine title+year+journal to reduce false merges
            key = f"{rec['title']}|{rec['year']}|{rec['journal']}"
        if key and key not in seen:
            seen.add(key)
            unique.append(rec)

    print(f"\n{'='*60}")
    print(f"  Total records before dedup: {len(all_results)}")
    print(f"  Total records after  dedup: {len(unique)}")
    print(f"{'='*60}")

    # Write CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(unique)

    print(f"\n  Results saved to: {OUTPUT_FILE}")
    print("  Done.")


if __name__ == "__main__":
    main()
