"""
Real public PubMed abstract fetcher via NCBI E-utilities API.

Data tag: REAL_PUBLIC
Uses PubMed's free public Entrez API (no API key required for low-volume use,
though NCBI_EMAIL env var is strongly recommended as a courtesy identifier).
No PHI involved — only public medical literature.

API endpoints used:
  esearch: find PMIDs matching a clinical query
  efetch: fetch full record in XML for those PMIDs

Rate limit: 3 requests/sec without API key, 10/sec with NCBI_API_KEY env var.
Each call sleeps 0.34s between requests to stay within limits.

Usage:
    from data.real_public.pubmed import fetch_pubmed_abstracts
    docs = fetch_pubmed_abstracts(query="sepsis management guidelines", max_results=5)
"""

import time
import os
import xml.etree.ElementTree as ET
from schemas import Document, DataTag

try:
    import urllib.request
    import urllib.parse
    _HAS_URLLIB = True
except ImportError:
    _HAS_URLLIB = False

_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
_EFETCH_URL  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
_TOOL        = "clinical-ai-platform-poc"
_EMAIL       = os.environ.get("NCBI_EMAIL", "poc@example.com")
_API_KEY     = os.environ.get("NCBI_API_KEY", "")
_SLEEP_S     = 0.34  # stays within 3 req/sec limit


def _get(url: str, params: dict) -> str:
    """Simple HTTP GET returning response body as string."""
    if _API_KEY:
        params["api_key"] = _API_KEY
    params["tool"] = _TOOL
    params["email"] = _EMAIL
    encoded = urllib.parse.urlencode(params)
    full_url = f"{url}?{encoded}"
    with urllib.request.urlopen(full_url, timeout=20) as resp:
        return resp.read().decode("utf-8")


def _esearch(query: str, max_results: int) -> list[str]:
    """Returns list of PMIDs matching query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": str(max_results),
        "retmode": "json",
        "sort": "relevance",
    }
    raw = _get(_ESEARCH_URL, params)
    # parse JSON manually to avoid importing json (keep dependencies minimal)
    import json
    data = json.loads(raw)
    return data.get("esearchresult", {}).get("idlist", [])


def _efetch_xml(pmids: list[str]) -> str:
    """Fetches full PubMed records in XML for given PMIDs."""
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
        "rettype": "abstract",
    }
    return _get(_EFETCH_URL, params)


def _parse_pubmed_xml(xml_text: str) -> list[dict]:
    """Parses PubMed XML and extracts key fields."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []

    records = []
    for article in root.findall(".//PubmedArticle"):
        try:
            citation = article.find("MedlineCitation")
            pmid = citation.findtext("PMID", "")
            art = citation.find("Article")
            title = art.findtext("ArticleTitle", "")

            # Abstract
            abstract_parts = []
            abstract_elem = art.find("Abstract")
            if abstract_elem is not None:
                for text_elem in abstract_elem.findall("AbstractText"):
                    label = text_elem.get("Label", "")
                    text = text_elem.text or ""
                    if label:
                        abstract_parts.append(f"{label}: {text}")
                    else:
                        abstract_parts.append(text)
            abstract = " ".join(abstract_parts)

            # Authors
            authors = []
            author_list = art.find("AuthorList")
            if author_list is not None:
                for author in author_list.findall("Author"):
                    last = author.findtext("LastName", "")
                    initials = author.findtext("Initials", "")
                    if last:
                        authors.append(f"{last} {initials}".strip())

            # Journal
            journal = art.find("Journal")
            journal_title = ""
            journal_abbr = ""
            year = ""
            if journal is not None:
                journal_title = journal.findtext("Title", "")
                journal_abbr = journal.findtext("ISOAbbreviation", "")
                pub_date = journal.find(".//PubDate")
                if pub_date is not None:
                    year = pub_date.findtext("Year", "")

            # DOI
            doi = ""
            for loc in article.findall(".//ArticleId"):
                if loc.get("IdType") == "doi":
                    doi = loc.text or ""

            # MeSH
            mesh_terms = []
            for heading in citation.findall(".//MeshHeading"):
                desc = heading.findtext("DescriptorName", "")
                major = heading.find("DescriptorName")
                if major is not None and major.get("MajorTopicYN") == "Y":
                    desc = f"*{desc}"
                mesh_terms.append(desc)

            records.append({
                "pmid": pmid,
                "title": title,
                "authors": authors,
                "journal": journal_title,
                "journal_abbr": journal_abbr,
                "year": year,
                "doi": doi,
                "abstract": abstract,
                "mesh_terms": mesh_terms,
            })
        except Exception:
            continue

    return records


def _record_to_text(rec: dict) -> str:
    authors_str = ", ".join(rec["authors"][:6])
    if len(rec["authors"]) > 6:
        authors_str += " et al."
    mesh_str = "; ".join(rec["mesh_terms"][:10]) if rec["mesh_terms"] else "N/A"
    return (
        f"Title: {rec['title']}\n\n"
        f"Authors: {authors_str}\n"
        f"Journal: {rec['journal']} ({rec['journal_abbr']}). {rec['year']}.\n"
        f"DOI: {rec['doi']}\n\n"
        f"Abstract:\n{rec['abstract']}\n\n"
        f"MeSH Terms: {mesh_str}"
    )


def fetch_pubmed_abstracts(
    query: str = "sepsis management clinical practice",
    max_results: int = 5,
) -> list[Document]:
    """
    Fetches real public PubMed abstracts matching the query.

    Data tag: REAL_PUBLIC — genuine medical literature, no PHI.
    Rate-limited to 3 requests/sec to respect NCBI guidelines.

    Args:
        query: PubMed search query (supports MeSH, Boolean operators).
        max_results: Maximum number of abstracts to return (recommend ≤20).

    Returns:
        List of Document objects, each containing one PubMed abstract.
        Returns empty list if network unavailable.
    """
    if not _HAS_URLLIB:
        return []

    try:
        pmids = _esearch(query, max_results)
        time.sleep(_SLEEP_S)

        if not pmids:
            return []

        xml_text = _efetch_xml(pmids)
        time.sleep(_SLEEP_S)

        records = _parse_pubmed_xml(xml_text)
        docs = []
        for rec in records:
            docs.append(
                Document(
                    id=f"pubmed-real-{rec['pmid']}",
                    text=_record_to_text(rec),
                    metadata={
                        "pmid": rec["pmid"],
                        "title": rec["title"],
                        "authors": rec["authors"],
                        "journal": rec["journal"],
                        "year": rec["year"],
                        "doi": rec["doi"],
                        "mesh_terms": rec["mesh_terms"],
                        "source_type": "pubmed_real",
                        "query": query,
                    },
                    tag=DataTag.REAL_PUBLIC,
                )
            )
        return docs

    except Exception:
        return []
