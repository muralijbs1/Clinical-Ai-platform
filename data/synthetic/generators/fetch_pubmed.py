#!/usr/bin/env python3
"""
Fetches real PubMed abstracts via NCBI E-utilities (no auth required).

DATA TAG: REAL-PUBLIC — genuine non-PHI public data from PubMed.

Output: appends <PubmedArticle> elements to data/synthetic/research_corpus.xml
Rate limit: 3 requests/sec (no API key). Sleep 0.4s between calls to be safe.

Run once. Re-run is safe — deduplicates by PMID before writing.

Quality gates applied:
  - Skip if AbstractText is missing or empty
  - Skip if title is missing
  - Truncate abstract to 2000 chars max (keeps XML manageable)
"""

import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

_OUT_FILE = Path(__file__).parent.parent / "research_corpus.xml"
_BASE_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
_BASE_EFETCH  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
_BATCH_SIZE   = 200   # records per efetch call (NCBI recommended max)
_SLEEP        = 0.4   # seconds between requests (stays under 3 req/sec limit)
_MAX_ABSTRACT = 2000  # chars — truncate to keep XML file size sane

# 25 clinical topics × up to 2,000 results each → ~50,000 abstracts
# retmax capped at 2000 per topic to keep fetch time reasonable
_TOPICS = [
    ("cardiology",              "cardiology[MeSH Major Topic] AND hasabstract[text]",           2000),
    ("heart_failure",           "heart failure[MeSH Terms] AND hasabstract[text]",              2000),
    ("atrial_fibrillation",     "atrial fibrillation[MeSH Terms] AND hasabstract[text]",        2000),
    ("oncology",                "neoplasms[MeSH Major Topic] AND hasabstract[text]",             2000),
    ("lung_cancer",             "lung neoplasms[MeSH Terms] AND hasabstract[text]",              2000),
    ("diabetes",                "diabetes mellitus[MeSH Major Topic] AND hasabstract[text]",     2000),
    ("neurology",               "neurology[MeSH Major Topic] AND hasabstract[text]",             2000),
    ("stroke",                  "stroke[MeSH Terms] AND hasabstract[text]",                      2000),
    ("sepsis",                  "sepsis[MeSH Terms] AND hasabstract[text]",                      2000),
    ("pneumonia",               "pneumonia[MeSH Terms] AND hasabstract[text]",                   2000),
    ("acute_kidney_injury",     "acute kidney injury[MeSH Terms] AND hasabstract[text]",         2000),
    ("copd",                    "pulmonary disease, chronic obstructive[MeSH Terms] AND hasabstract[text]", 2000),
    ("hypertension",            "hypertension[MeSH Major Topic] AND hasabstract[text]",          2000),
    ("rheumatology",            "rheumatic diseases[MeSH Major Topic] AND hasabstract[text]",    2000),
    ("psychiatry",              "mental disorders[MeSH Major Topic] AND hasabstract[text]",      2000),
    ("gastroenterology",        "gastrointestinal diseases[MeSH Major Topic] AND hasabstract[text]", 2000),
    ("infectious_disease",      "communicable diseases[MeSH Major Topic] AND hasabstract[text]", 2000),
    ("emergency_medicine",      "emergency medicine[MeSH Major Topic] AND hasabstract[text]",    2000),
    ("intensive_care",          "critical care[MeSH Major Topic] AND hasabstract[text]",         2000),
    ("surgery",                 "surgical procedures, operative[MeSH Major Topic] AND hasabstract[text]", 2000),
    ("obstetrics",              "obstetrics[MeSH Major Topic] AND hasabstract[text]",             2000),
    ("paediatrics",             "pediatrics[MeSH Major Topic] AND hasabstract[text]",             2000),
    ("geriatrics",              "geriatrics[MeSH Major Topic] AND hasabstract[text]",             2000),
    ("endocrinology",           "endocrine system diseases[MeSH Major Topic] AND hasabstract[text]", 2000),
    ("palliative_care",         "palliative care[MeSH Terms] AND hasabstract[text]",              2000),
]


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "ClinicalAI-PoC/1.0 (educational)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def _esearch(query: str, retmax: int) -> list[str]:
    params = urllib.parse.urlencode({
        "db": "pubmed", "term": query, "retmax": retmax,
        "retmode": "json", "usehistory": "n",
    })
    import json
    data = json.loads(_get(f"{_BASE_ESEARCH}?{params}"))
    return data["esearchresult"]["idlist"]


def _efetch_xml(pmids: list[str]) -> ET.Element:
    params = urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(pmids),
        "rettype": "abstract", "retmode": "xml",
    })
    raw = _get(f"{_BASE_EFETCH}?{params}")
    return ET.fromstring(raw)


def _extract_text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    parts = []
    if el.text:
        parts.append(el.text.strip())
    for child in el:
        t = _extract_text(child)
        if t:
            parts.append(t)
        if child.tail:
            parts.append(child.tail.strip())
    return " ".join(p for p in parts if p)


def _article_is_valid(article: ET.Element) -> bool:
    title = _extract_text(article.find(".//ArticleTitle"))
    abstract = _extract_text(article.find(".//AbstractText"))
    if not title or not abstract:
        return False
    if len(abstract) < 100:
        return False
    return True


def _load_existing_pmids(tree: ET.ElementTree) -> set[str]:
    root = tree.getroot()
    pmids = set()
    for el in root.findall(".//PMID"):
        if el.text:
            pmids.add(el.text.strip())
    return pmids


def fetch_and_append(target: int = 50_000) -> None:
    # Load existing XML
    tree = ET.parse(_OUT_FILE)
    root = tree.getroot()
    existing_pmids = _load_existing_pmids(tree)
    existing_count = len(root.findall("PubmedArticle"))
    print(f"Existing articles in XML: {existing_count} (PMIDs tracked: {len(existing_pmids)})")

    added = 0
    skipped_dup = 0
    skipped_quality = 0

    for topic_name, query, retmax in _TOPICS:
        if added >= (target - existing_count):
            break

        print(f"\n[{topic_name}] Searching (retmax={retmax})...", flush=True)
        try:
            time.sleep(_SLEEP)
            pmid_list = _esearch(query, retmax)
        except Exception as e:
            print(f"  esearch error: {e}")
            continue

        print(f"  Found {len(pmid_list)} PMIDs. Fetching in batches of {_BATCH_SIZE}...")

        for i in range(0, len(pmid_list), _BATCH_SIZE):
            batch = pmid_list[i:i + _BATCH_SIZE]
            # Deduplicate before fetching
            batch = [p for p in batch if p not in existing_pmids]
            if not batch:
                continue

            try:
                time.sleep(_SLEEP)
                batch_root = _efetch_xml(batch)
            except Exception as e:
                print(f"  efetch error (batch {i}): {e}")
                time.sleep(2)
                continue

            for article in batch_root.findall("PubmedArticle"):
                pmid_el = article.find(".//PMID")
                pmid = pmid_el.text.strip() if pmid_el is not None and pmid_el.text else None
                if not pmid or pmid in existing_pmids:
                    skipped_dup += 1
                    continue
                if not _article_is_valid(article):
                    skipped_quality += 1
                    continue

                # Truncate abstract to keep file size manageable
                for ab in article.findall(".//AbstractText"):
                    if ab.text and len(ab.text) > _MAX_ABSTRACT:
                        ab.text = ab.text[:_MAX_ABSTRACT] + "..."

                # Tag with data provenance
                other_id = ET.SubElement(
                    article.find(".//PubmedData") or article,
                    "OtherID", Source="DataTag"
                )
                other_id.text = "REAL-PUBLIC"

                root.append(article)
                existing_pmids.add(pmid)
                added += 1

            total_now = existing_count + added
            print(f"  batch {i//200 + 1}: +{len(batch)} fetched | total in XML: {total_now}", flush=True)

            if total_now >= target:
                print(f"\nReached target of {target}. Stopping.")
                break

        if (existing_count + added) >= target:
            break

    # Write back
    ET.indent(root, space="  ")
    tree.write(_OUT_FILE, encoding="unicode", xml_declaration=True)

    total_final = len(root.findall("PubmedArticle"))
    print(f"\nDone. Articles in XML: {total_final} (+{added} added, {skipped_dup} dup, {skipped_quality} quality-filtered)")


if __name__ == "__main__":
    fetch_and_append(target=50_000)
