#!/usr/bin/env python3
"""
Fetch PubMed search results (titles + abstracts) for the EDIA Canadian
mental health pharmacotherapy RCT search strategy.
Uses NCBI E-utilities with history server for large result sets.
"""

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import time
import csv
import sys
import os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
BATCH_SIZE = 500  # efetch batch size
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Full PubMed search query (3 concept blocks AND'd together + limits)
QUERY = (
    '("Mental Disorders"[MeSH] OR psychiatr*[tiab] OR "mental illness"[tiab] '
    'OR "mental illnesses"[tiab] OR "mental disorder"[tiab] OR "mental disorders"[tiab] '
    'OR "mental health"[tiab] OR psychopatholog*[tiab] OR psychopharmac*[tiab] '
    'OR antidepressant*[tiab] OR antipsychotic*[tiab] OR anxiolytic*[tiab] '
    'OR "mood stabiliz*"[tiab] OR neuroleptic*[tiab] OR SSRI[tiab] OR SNRI[tiab] '
    'OR benzodiazepine*[tiab] OR lithium[tiab] OR depress*[tiab] '
    'OR "major depressive"[tiab] OR dysthymi*[tiab] OR "postpartum depression"[tiab] '
    'OR "perinatal depression"[tiab] OR anxiety[tiab] OR "panic disorder"[tiab] '
    'OR "social anxiety"[tiab] OR phobia*[tiab] OR "generalized anxiety"[tiab] '
    'OR agoraphobia[tiab] OR schizophren*[tiab] OR psychosis[tiab] OR psychotic[tiab] '
    'OR schizoaffective[tiab] OR bipolar[tiab] OR mania[tiab] OR manic[tiab] '
    'OR "mood disorder"[tiab] OR "mood disorders"[tiab] OR "obsessive compulsive"[tiab] '
    'OR OCD[tiab] OR "post-traumatic stress"[tiab] OR "posttraumatic stress"[tiab] '
    'OR PTSD[tiab] OR "attention deficit"[tiab] OR ADHD[tiab] '
    'OR "anorexia nervosa"[tiab] OR bulimia[tiab] OR "eating disorder"[tiab] '
    'OR "eating disorders"[tiab] OR "binge eating"[tiab] '
    'OR "substance use disorder"[tiab] OR "substance abuse"[tiab] '
    'OR "alcohol use disorder"[tiab] OR "opioid use disorder"[tiab] '
    'OR "drug dependence"[tiab] OR "alcohol dependence"[tiab] '
    'OR "opioid dependence"[tiab] OR "personality disorder"[tiab] '
    'OR "personality disorders"[tiab] OR "borderline personality"[tiab] '
    'OR "autism spectrum"[tiab] OR autistic[tiab] OR insomnia[tiab] '
    'OR "sleep-wake disorder"[tiab] OR "sleep disorder"[tiab] '
    'OR "neurocognitive disorder"[tiab] OR dementia[tiab] OR Alzheimer*[tiab]) '
    'AND '
    '("Randomized Controlled Trial"[pt] OR "Controlled Clinical Trial"[pt] '
    'OR randomized[tiab] OR randomised[tiab] OR placebo[tiab] OR "drug therapy"[sh] '
    'OR randomly[tiab] OR trial[tiab] OR groups[tiab]) '
    'NOT ("Animals"[MeSH] NOT "Humans"[MeSH]) '
    'AND '
    '("Canada"[MeSH] OR Canada[tiab] OR Canadian[tiab] OR Canadians[tiab] '
    'OR Alberta[tiab] OR "British Columbia"[tiab] OR Manitoba[tiab] '
    'OR "New Brunswick"[tiab] OR Newfoundland[tiab] OR Labrador[tiab] '
    'OR "Nova Scotia"[tiab] OR Ontario[tiab] OR Quebec[tiab] '
    'OR Saskatchewan[tiab] OR "Prince Edward Island"[tiab] '
    'OR "Northwest Territories"[tiab] OR Nunavut[tiab] OR Yukon[tiab] '
    'OR Toronto[tiab] OR Montreal[tiab] OR Vancouver[tiab] OR Ottawa[tiab] '
    'OR Calgary[tiab] OR Edmonton[tiab] OR Winnipeg[tiab] OR Halifax[tiab] '
    'OR Hamilton[tiab] OR Mississauga[tiab] OR Saskatoon[tiab] OR Regina[tiab] '
    'OR Sherbrooke[tiab] OR Fredericton[tiab] OR Charlottetown[tiab] '
    'OR Whitehorse[tiab] OR Yellowknife[tiab] OR Iqaluit[tiab] '
    'OR "Thunder Bay"[tiab] OR "Quebec City"[tiab] OR Kingston[tiab] '
    'OR Sudbury[tiab] OR "St. John"[tiab] '
    'OR Canada[ad] OR Canadian[ad] OR Alberta[ad] OR "British Columbia"[ad] '
    'OR Manitoba[ad] OR Ontario[ad] OR Quebec[ad] OR Saskatchewan[ad] '
    'OR "Nova Scotia"[ad] OR Newfoundland[ad] OR Toronto[ad] OR Montreal[ad] '
    'OR Vancouver[ad] OR Ottawa[ad] OR Calgary[ad] OR Edmonton[ad] '
    'OR Winnipeg[ad] OR Halifax[ad] OR Hamilton[ad]) '
    f'AND ("2000/01/01"[PDAT] : "{time.strftime("%Y")}/12/31"[PDAT]) '
    'AND English[la]'
)


def fetch_url(url, retries=3):
    """Fetch URL with retry logic."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Python/EDIA-Review"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            if attempt < retries - 1:
                print(f"  Retry {attempt+1} after error: {e}")
                time.sleep(2 * (attempt + 1))
            else:
                raise


def esearch():
    """Run esearch with history server, return (count, webenv, query_key)."""
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": QUERY,
        "usehistory": "y",
        "retmax": 0,
        "retmode": "json",
    })
    url = f"{BASE}/esearch.fcgi?{params}"
    print("Running esearch...")
    data = json.loads(fetch_url(url))
    result = data["esearchresult"]
    count = int(result["count"])
    webenv = result["webenv"]
    query_key = result["querykey"]
    print(f"  Found {count:,} results")
    return count, webenv, query_key


def efetch_batch(webenv, query_key, retstart, retmax):
    """Fetch a batch of records in XML format."""
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "query_key": query_key,
        "WebEnv": webenv,
        "retstart": retstart,
        "retmax": retmax,
        "retmode": "xml",
        "rettype": "abstract",
    })
    url = f"{BASE}/efetch.fcgi?{params}"
    return fetch_url(url)


def parse_articles(xml_text):
    """Parse PubMed XML and extract PMID, title, authors, journal, year, abstract."""
    articles = []
    root = ET.fromstring(xml_text)
    for article_el in root.findall(".//PubmedArticle"):
        pmid_el = article_el.find(".//PMID")
        pmid = pmid_el.text if pmid_el is not None else ""

        title_el = article_el.find(".//ArticleTitle")
        title = "".join(title_el.itertext()) if title_el is not None else ""

        # Authors
        author_list = article_el.findall(".//Author")
        authors = []
        for auth in author_list:
            last = auth.find("LastName")
            fore = auth.find("ForeName")
            if last is not None:
                name = last.text or ""
                if fore is not None and fore.text:
                    name += " " + fore.text
                authors.append(name)
        author_str = "; ".join(authors) if authors else ""

        # Journal
        journal_el = article_el.find(".//Title")
        journal = journal_el.text if journal_el is not None else ""

        # Year
        year_el = article_el.find(".//PubDate/Year")
        if year_el is None:
            year_el = article_el.find(".//PubDate/MedlineDate")
        year = (year_el.text or "")[:4] if year_el is not None else ""

        # Abstract
        abstract_parts = []
        for abs_el in article_el.findall(".//Abstract/AbstractText"):
            label = abs_el.get("Label", "")
            text = "".join(abs_el.itertext()) or ""
            if label:
                abstract_parts.append(f"{label}: {text}")
            else:
                abstract_parts.append(text)
        abstract = " ".join(abstract_parts)

        # DOI
        doi = ""
        for id_el in article_el.findall(".//ArticleId"):
            if id_el.get("IdType") == "doi":
                doi = id_el.text or ""
                break

        articles.append({
            "pmid": pmid,
            "title": title,
            "authors": author_str,
            "journal": journal,
            "year": year,
            "doi": doi,
            "abstract": abstract,
        })
    return articles


def main():
    count, webenv, query_key = esearch()

    csv_path = os.path.join(OUTPUT_DIR, "abstracts", "pubmed_results.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    fieldnames = ["pmid", "title", "authors", "journal", "year", "doi", "abstract"]

    # Write header
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    total_fetched = 0
    total_batches = (count + BATCH_SIZE - 1) // BATCH_SIZE
    max_per_session = 9500  # re-auth before NCBI 10k session limit

    for i in range(total_batches):
        retstart = i * BATCH_SIZE

        # Re-establish session before hitting the 10k limit
        if retstart > 0 and retstart % max_per_session < BATCH_SIZE:
            print(f"  Re-establishing NCBI history session...")
            time.sleep(1)
            count, webenv, query_key = esearch()

        batch_end = min(retstart + BATCH_SIZE, count)
        print(f"Fetching batch {i+1}/{total_batches} (records {retstart+1}-{batch_end})...")

        try:
            xml_text = efetch_batch(webenv, query_key, retstart, BATCH_SIZE)
            articles = parse_articles(xml_text)
        except Exception as e:
            print(f"  Error on batch {i+1}: {e}")
            print(f"  Re-establishing session and retrying...")
            time.sleep(3)
            count, webenv, query_key = esearch()
            try:
                xml_text = efetch_batch(webenv, query_key, retstart, BATCH_SIZE)
                articles = parse_articles(xml_text)
            except Exception as e2:
                print(f"  Failed again: {e2}. Skipping batch.")
                continue

        # Append to CSV incrementally
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows(articles)

        total_fetched += len(articles)
        print(f"  Parsed {len(articles)} articles (total: {total_fetched:,})")

        # Respect NCBI rate limit
        if i < total_batches - 1:
            time.sleep(0.4)

    print(f"\nDone! {total_fetched:,} articles saved to {csv_path}")

    # Read back from CSV for summary
    all_articles = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_articles.append(row)

    summary_path = os.path.join(OUTPUT_DIR, "abstracts", "pubmed_search_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(f"PubMed Search Results Summary\n")
        f.write(f"{'='*50}\n")
        f.write(f"Date executed: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total results: {len(all_articles):,}\n")
        f.write(f"Records with abstracts: {sum(1 for a in all_articles if a['abstract']):,}\n")
        f.write(f"Records without abstracts: {sum(1 for a in all_articles if not a['abstract']):,}\n\n")
        year_counts = {}
        for a in all_articles:
            yr = a["year"] or "Unknown"
            year_counts[yr] = year_counts.get(yr, 0) + 1
        f.write("Year distribution:\n")
        for yr in sorted(year_counts.keys()):
            f.write(f"  {yr}: {year_counts[yr]:,}\n")

    print(f"Summary saved to {summary_path}")


if __name__ == "__main__":
    main()
