#!/usr/bin/env python3
"""
Deduplicate search results from PubMed, Europe PMC, OpenAlex, and Scopus.

Deduplication strategy (priority order):
  1. DOI match (exact, case-insensitive)
  2. PMID match (exact)
  3. Fuzzy title match (SequenceMatcher ratio > 0.90 AND same year)

Merging keeps the longest abstract, collects all IDs, and tracks source databases.
"""

import csv
import os
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ABSTRACTS_DIR = os.path.join(SCRIPT_DIR, "abstracts")
REPORTS_DIR = os.path.join(SCRIPT_DIR, "reports")

FUZZY_THRESHOLD = 0.93  # Conservative for narrow clinical domain to avoid false merges

DATABASE_FILES = {
    "PubMed": {
        "file": "pubmed_results.csv",
        "columns": ["pmid", "title", "authors", "journal", "year", "doi", "abstract"],
    },
    "Europe PMC": {
        "file": "europepmc_results.csv",
        "columns": ["pmid", "title", "authors", "journal", "year", "doi", "abstract", "europepmc_id"],
    },
    "OpenAlex": {
        "file": "openalex_results.csv",
        "columns": ["pmid", "title", "authors", "journal", "year", "doi", "abstract", "openalex_id", "cited_by_count"],
    },
    "Scopus": {
        "file": "scopus_results.csv",
        "columns": ["pmid", "title", "authors", "journal", "year", "doi", "abstract", "scopus_id", "citedby_count"],
    },
}

OUTPUT_COLUMNS = [
    "pmid", "title", "authors", "journal", "year", "doi", "abstract",
    "sources", "europepmc_id", "openalex_id", "scopus_id", "cited_by_count",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean(value):
    """Strip whitespace and HTML tags from a value; return empty string for None."""
    if value is None:
        return ""
    s = str(value).strip()
    # Remove common HTML tags and entities
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&lt;", "<").replace("&gt;", ">")
    s = s.replace("&amp;", "&").replace("&quot;", '"')
    s = s.replace("&#39;", "'")
    # Clean up any leftover angle bracket artifacts
    s = re.sub(r"</?subtitle>", "", s)
    return s.strip()


def normalize_title(title):
    """Lowercase, remove punctuation, collapse whitespace."""
    t = title.lower()
    t = re.sub(r"[^\w\s]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def normalize_doi(doi):
    """Normalize DOI by stripping URL prefixes and lowercasing."""
    doi = doi.strip().lower()
    for prefix in (
        "https://doi.org/", "http://doi.org/",
        "https://dx.doi.org/", "http://dx.doi.org/",
    ):
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    return doi


def safe_int(value):
    """Convert to int, return 0 on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def load_csv(filepath, expected_columns):
    """Load a CSV file and return a list of dicts. Returns [] if file missing."""
    if not os.path.isfile(filepath):
        print(f"  WARNING: File not found, skipping: {filepath}")
        return []

    records = []
    with open(filepath, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = {}
            for col in expected_columns:
                record[col] = clean(row.get(col, ""))
            records.append(record)

    print(f"  Loaded {len(records)} records from {os.path.basename(filepath)}")
    return records


# ---------------------------------------------------------------------------
# Record cluster: represents one unique study (possibly merged from many DBs)
# ---------------------------------------------------------------------------

class RecordCluster:
    """A merged record that may combine entries from multiple databases."""

    def __init__(self, record, source):
        self.pmid = clean(record.get("pmid", ""))
        self.title = clean(record.get("title", ""))
        self.authors = clean(record.get("authors", ""))
        self.journal = clean(record.get("journal", ""))
        self.year = clean(record.get("year", ""))
        self.doi = normalize_doi(clean(record.get("doi", "")))
        self.abstract = clean(record.get("abstract", ""))
        self.sources = {source}
        self.europepmc_id = clean(record.get("europepmc_id", ""))
        self.openalex_id = clean(record.get("openalex_id", ""))
        self.scopus_id = clean(record.get("scopus_id", ""))
        # Normalize citation count from either field name
        self.cited_by_count = max(
            safe_int(record.get("cited_by_count", 0)),
            safe_int(record.get("citedby_count", 0)),
        )
        self.normalized_title = normalize_title(self.title)

    def merge(self, record, source):
        """Merge another record into this cluster."""
        self.sources.add(source)

        # Keep longest abstract
        other_abstract = clean(record.get("abstract", ""))
        if len(other_abstract) > len(self.abstract):
            self.abstract = other_abstract

        # Keep PMID if we don't have one
        other_pmid = clean(record.get("pmid", ""))
        if not self.pmid and other_pmid:
            self.pmid = other_pmid

        # Keep DOI if we don't have one
        other_doi = normalize_doi(clean(record.get("doi", "")))
        if not self.doi and other_doi:
            self.doi = other_doi

        # Keep longer/better title if current is short
        other_title = clean(record.get("title", ""))
        if len(other_title) > len(self.title):
            self.title = other_title
            self.normalized_title = normalize_title(self.title)

        # Keep longer authors
        other_authors = clean(record.get("authors", ""))
        if len(other_authors) > len(self.authors):
            self.authors = other_authors

        # Keep journal if missing
        other_journal = clean(record.get("journal", ""))
        if not self.journal and other_journal:
            self.journal = other_journal

        # Keep year if missing
        other_year = clean(record.get("year", ""))
        if not self.year and other_year:
            self.year = other_year

        # Collect database-specific IDs
        for field in ("europepmc_id", "openalex_id", "scopus_id"):
            other_val = clean(record.get(field, ""))
            if other_val and not getattr(self, field):
                setattr(self, field, other_val)

        # Keep highest citation count
        other_cited = max(
            safe_int(record.get("cited_by_count", 0)),
            safe_int(record.get("citedby_count", 0)),
        )
        if other_cited > self.cited_by_count:
            self.cited_by_count = other_cited

    def to_dict(self):
        return {
            "pmid": self.pmid,
            "title": self.title,
            "authors": self.authors,
            "journal": self.journal,
            "year": self.year,
            "doi": self.doi,
            "abstract": self.abstract,
            "sources": "; ".join(sorted(self.sources)),
            "europepmc_id": self.europepmc_id,
            "openalex_id": self.openalex_id,
            "scopus_id": self.scopus_id,
            "cited_by_count": self.cited_by_count if self.cited_by_count > 0 else "",
        }


# ---------------------------------------------------------------------------
# Deduplication engine
# ---------------------------------------------------------------------------

class Deduplicator:
    def __init__(self):
        self.clusters = []          # List[RecordCluster]
        self.doi_index = {}         # doi -> cluster index
        self.pmid_index = {}        # pmid -> cluster index
        self.year_title_index = defaultdict(list)  # year -> [(norm_title, cluster_idx)]

        # Statistics
        self.db_counts = {}         # db_name -> raw record count
        self.match_counts = {"doi": 0, "pmid": 0, "title_fuzzy": 0, "new": 0}
        self.pairwise_overlap = defaultdict(int)  # (db_a, db_b) -> count

    def add_records(self, records, source):
        """Add a batch of records from a single database source."""
        self.db_counts[source] = len(records)
        print(f"\nDeduplicating {len(records)} records from {source}...")

        for i, rec in enumerate(records):
            if (i + 1) % 500 == 0:
                print(f"  Processed {i + 1}/{len(records)} from {source}")
            self._add_one(rec, source)

        print(f"  Done. Total unique records so far: {len(self.clusters)}")

    def _add_one(self, record, source):
        doi = normalize_doi(clean(record.get("doi", "")))
        pmid = clean(record.get("pmid", ""))
        title = clean(record.get("title", ""))
        year = clean(record.get("year", ""))
        norm_title = normalize_title(title)

        # 1. DOI match
        if doi and doi in self.doi_index:
            idx = self.doi_index[doi]
            self._record_overlap(self.clusters[idx], source)
            self.clusters[idx].merge(record, source)
            self._update_indices(idx)
            self.match_counts["doi"] += 1
            return

        # 2. PMID match
        if pmid and pmid in self.pmid_index:
            idx = self.pmid_index[pmid]
            self._record_overlap(self.clusters[idx], source)
            self.clusters[idx].merge(record, source)
            self._update_indices(idx)
            self.match_counts["pmid"] += 1
            return

        # 3. Fuzzy title match (within same year only) -- take BEST match
        if norm_title and year:
            candidates = self.year_title_index.get(year, [])
            best_ratio = 0
            best_idx = -1
            for cand_title, cand_idx in candidates:
                if abs(len(norm_title) - len(cand_title)) > max(len(norm_title), len(cand_title)) * 0.15:
                    continue
                ratio = SequenceMatcher(None, norm_title, cand_title).ratio()
                if ratio > FUZZY_THRESHOLD and ratio > best_ratio:
                    best_ratio = ratio
                    best_idx = cand_idx
            if best_idx >= 0:
                self._record_overlap(self.clusters[best_idx], source)
                self.clusters[best_idx].merge(record, source)
                self._update_indices(best_idx)
                self.match_counts["title_fuzzy"] += 1
                return

        # 4. No match found -- create new cluster
        idx = len(self.clusters)
        cluster = RecordCluster(record, source)
        self.clusters.append(cluster)
        self._update_indices(idx)
        self.match_counts["new"] += 1

    def _update_indices(self, idx):
        """Update DOI, PMID, and year-title indices for a cluster."""
        cluster = self.clusters[idx]
        if cluster.doi:
            self.doi_index[cluster.doi] = idx
        if cluster.pmid:
            self.pmid_index[cluster.pmid] = idx
        if cluster.normalized_title and cluster.year:
            # Check if already in the year index
            year_entries = self.year_title_index[cluster.year]
            found = False
            for i, (_, cidx) in enumerate(year_entries):
                if cidx == idx:
                    year_entries[i] = (cluster.normalized_title, idx)
                    found = True
                    break
            if not found:
                year_entries.append((cluster.normalized_title, idx))

    def _record_overlap(self, cluster, new_source):
        """Record pairwise overlap between the new source and existing sources."""
        for existing_source in cluster.sources:
            if existing_source != new_source:
                pair = tuple(sorted([existing_source, new_source]))
                self.pairwise_overlap[pair] += 1

    def get_results(self):
        """Return list of dicts for output."""
        return [c.to_dict() for c in self.clusters]


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(dedup, output_path):
    """Write a Markdown deduplication report."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    db_names = list(dedup.db_counts.keys())
    total_raw = sum(dedup.db_counts.values())
    total_deduped = len(dedup.clusters)

    lines = []
    lines.append("# Deduplication Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Per-database counts
    lines.append("## Records per Database")
    lines.append("")
    lines.append("| Database | Records |")
    lines.append("|----------|---------|")
    for db in db_names:
        lines.append(f"| {db} | {dedup.db_counts[db]} |")
    lines.append(f"| **Total (raw)** | **{total_raw}** |")
    lines.append("")

    # Pairwise overlap
    lines.append("## Pairwise Overlap")
    lines.append("")
    lines.append("Number of records shared between each pair of databases:")
    lines.append("")
    lines.append("| Database Pair | Shared Records |")
    lines.append("|---------------|----------------|")
    for i, db_a in enumerate(db_names):
        for db_b in db_names[i + 1:]:
            pair = tuple(sorted([db_a, db_b]))
            count = dedup.pairwise_overlap.get(pair, 0)
            lines.append(f"| {db_a} / {db_b} | {count} |")
    lines.append("")

    # Match method breakdown
    lines.append("## Match Method Breakdown")
    lines.append("")
    lines.append("How duplicate records were identified:")
    lines.append("")
    lines.append("| Method | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| DOI match | {dedup.match_counts['doi']} |")
    lines.append(f"| PMID match | {dedup.match_counts['pmid']} |")
    lines.append(f"| Fuzzy title match | {dedup.match_counts['title_fuzzy']} |")
    lines.append(f"| New (unique) | {dedup.match_counts['new']} |")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Total raw records across all databases:** {total_raw}")
    lines.append(f"- **Duplicates removed:** {total_raw - total_deduped}")
    lines.append(f"- **Total unique records after deduplication:** {total_deduped}")
    lines.append("")

    # Source distribution
    lines.append("## Source Distribution")
    lines.append("")
    lines.append("How many databases each unique record appeared in:")
    lines.append("")
    source_dist = defaultdict(int)
    for cluster in dedup.clusters:
        n = len(cluster.sources)
        source_dist[n] += 1
    lines.append("| Databases | Records |")
    lines.append("|-----------|---------|")
    for n in sorted(source_dist.keys()):
        label = f"{n} database{'s' if n > 1 else ''}"
        lines.append(f"| {label} | {source_dist[n]} |")
    lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nReport written to: {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Scoping Review Deduplication")
    print("=" * 60)

    # Load all databases
    all_records = {}
    for db_name, config in DATABASE_FILES.items():
        filepath = os.path.join(ABSTRACTS_DIR, config["file"])
        print(f"\nLoading {db_name}...")
        records = load_csv(filepath, config["columns"])
        if records:
            all_records[db_name] = records

    if not all_records:
        print("\nERROR: No database files found. Nothing to deduplicate.")
        sys.exit(1)

    total_raw = sum(len(r) for r in all_records.values())
    print(f"\nTotal raw records loaded: {total_raw}")

    # Run deduplication
    print("\n" + "-" * 60)
    print("Running deduplication...")
    print("-" * 60)

    dedup = Deduplicator()

    # Process databases in a fixed order. PubMed is processed first because its
    # metadata (structured abstracts, MeSH terms, curated author names) is the
    # highest quality among the sources. When a duplicate is found via DOI/PMID,
    # the first-processed record's metadata becomes the canonical baseline and
    # subsequent matches merge into it (keeping the longest abstract/authors).
    # This ordering is a methodological decision documented in the Methods section.
    for db_name in ["PubMed", "Europe PMC", "OpenAlex", "Scopus"]:
        if db_name in all_records:
            dedup.add_records(all_records[db_name], db_name)

    # Write deduplicated output
    results = dedup.get_results()
    output_csv = os.path.join(ABSTRACTS_DIR, "combined_deduplicated.csv")

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nDeduplicated CSV written to: {output_csv}")
    print(f"  {len(results)} unique records")

    # Generate report
    report_path = os.path.join(REPORTS_DIR, "dedup_report.md")
    generate_report(dedup, report_path)

    # Print summary to console
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Raw records:     {total_raw}")
    print(f"  Duplicates:      {total_raw - len(results)}")
    print(f"  Unique records:  {len(results)}")
    print(f"  Match breakdown: DOI={dedup.match_counts['doi']}, "
          f"PMID={dedup.match_counts['pmid']}, "
          f"Title={dedup.match_counts['title_fuzzy']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
