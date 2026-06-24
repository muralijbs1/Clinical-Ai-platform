"""
Unified data loader — reads native format data files and returns Document objects.

No Python data files are imported. Every source is a real-world format file on disk:

  data/synthetic/research_corpus.xml      MEDLINE XML → Document (SYNTHETIC)
  data/synthetic/transcripts/note_*.txt   plain text SOAP notes → Document (SYNTHETIC)
  data/synthetic/encounters/enc_*.xml     FHIR R4 Bundle XML → Document (SYNTHETIC)
  data/synthetic/referrals/ref_*.txt      plain text referral letters → Document (SYNTHETIC)
  data/synthetic/diagnostic_cases.csv    CSV feature vectors → Document (SYNTHETIC)
  data/randomised/vitals.csv             CSV vital sign streams → Document (RANDOMISED)
  data/randomised/surgical_frames.json   Cholec80 JSON frame detections → Document (RANDOMISED)

Usage:
    from data.loader import load_all, load_for_agent, load_real_public, summarise

    all_docs     = load_all()
    research     = load_for_agent("research")
    diagnostic   = load_for_agent("diagnostic")
    real_pubmed  = load_real_public(query="sepsis guidelines", max_results=10)
"""

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from schemas import Document, DataTag
from data.real_public.pubmed import fetch_pubmed_abstracts

_DATA_DIR = Path(__file__).parent
_SYNTHETIC  = _DATA_DIR / "synthetic"
_RANDOMISED = _DATA_DIR / "randomised"

_FHIR = {"f": "http://hl7.org/fhir"}   # FHIR namespace prefix for XPath

_AGENT_SOURCES = {
    "research":      ["research_corpus", "pubmed_real"],
    "documentation": ["transcripts", "encounters"],
    "diagnostic":    ["encounters", "diagnostic_cases", "vitals"],
    "coordination":  ["referrals", "encounters"],
    "surgical":      ["surgical_frames"],
}


# ── Helpers ────────────────────────────────────────────────────────────────────

def _parse_frontmatter(raw: str) -> tuple[dict, str]:
    """Parse 'key: value\\n---\\nbody' into (meta_dict, body)."""
    if "---\n" not in raw:
        return {}, raw
    header, _, body = raw.partition("---\n")
    meta = {}
    for line in header.strip().splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            meta[k.strip()] = v.strip()
    return meta, body


def _fhir_val(el: ET.Element, tag: str) -> str:
    """Return value attr of first child <tag value="..."/> under el."""
    child = el.find(f"f:{tag}", _FHIR)
    return child.get("value", "") if child is not None else ""


def _fhir_ext(el: ET.Element, url: str) -> str:
    """Return valueString from <extension url="..."><valueString value="..."/>."""
    for ext in el.findall("f:extension", _FHIR):
        if ext.get("url") == url:
            vs = ext.find("f:valueString", _FHIR)
            if vs is not None:
                return vs.get("value", "")
    return ""


def _fhir_text(el: ET.Element, tag: str) -> str:
    """Return value attr of <tag><text value="..."/>."""
    child = el.find(f"f:{tag}", _FHIR)
    if child is None:
        return ""
    text_el = child.find("f:text", _FHIR)
    return text_el.get("value", "") if text_el is not None else ""


def _obs_category(obs: ET.Element) -> str:
    """Return the code value of the first category/coding/code in an Observation."""
    cat = obs.find("f:category", _FHIR)
    if cat is None:
        return ""
    coding = cat.find("f:coding", _FHIR)
    if coding is None:
        return ""
    code_el = coding.find("f:code", _FHIR)
    return code_el.get("value", "") if code_el is not None else ""


# ── Source parsers ─────────────────────────────────────────────────────────────

def _load_research_corpus() -> list[Document]:
    xml_file = _SYNTHETIC / "research_corpus.xml"
    if not xml_file.exists():
        return []

    root = ET.parse(xml_file).getroot()
    docs = []

    for article in root.findall(".//PubmedArticle"):
        try:
            citation  = article.find("MedlineCitation")
            pmid      = citation.findtext("PMID", "")
            art       = citation.find("Article")
            title     = art.findtext("ArticleTitle", "")

            # Authors
            authors = []
            for author in art.findall(".//Author"):
                last = author.findtext("LastName", "")
                inits = author.findtext("Initials", "")
                if last:
                    authors.append(f"{last} {inits}".strip())

            # Journal
            jrn       = art.find("Journal")
            j_title   = jrn.findtext("Title", "")   if jrn else ""
            j_abbr    = jrn.findtext("ISOAbbreviation", "") if jrn else ""
            year = volume = issue = pages = ""
            if jrn:
                ji = jrn.find("JournalIssue")
                if ji:
                    year   = ji.findtext(".//Year",   "")
                    volume = ji.findtext("Volume",    "")
                    issue  = ji.findtext("Issue",     "")
                pg = art.find("Pagination")
                if pg:
                    pages = pg.findtext("MedlinePgn", "")

            # Abstract
            abstract_parts = []
            abstract_el = art.find("Abstract")
            if abstract_el is not None:
                for t in abstract_el.findall("AbstractText"):
                    label = t.get("Label", "")
                    txt   = t.text or ""
                    abstract_parts.append(f"{label}: {txt}" if label else txt)
            abstract = " ".join(abstract_parts)

            # DOI
            doi = ""
            for loc in article.findall(".//ArticleId"):
                if loc.get("IdType") == "doi":
                    doi = loc.text or ""

            # MeSH terms
            mesh_terms = []
            for mh in citation.findall(".//MeshHeading"):
                dn      = mh.find("DescriptorName")
                desc    = dn.text or "" if dn is not None else ""
                is_maj  = dn is not None and dn.get("MajorTopicYN") == "Y"
                qual    = mh.findtext("QualifierName", "")
                term    = f"{'*' if is_maj else ''}{desc}"
                if qual:
                    term += f"/{qual}"
                mesh_terms.append(term)

            # Evidence (custom OtherID elements)
            evidence_level = evidence_grade = pub_type = ""
            for oid in citation.findall("OtherID"):
                src = oid.get("Source", "")
                if src == "EvidenceLevel":
                    evidence_level = oid.text or ""
                elif src == "EvidenceGrade":
                    evidence_grade = oid.text or ""
            for pt_el in art.findall(".//PublicationType"):
                pub_type = pt_el.text or ""

            # Compose plain text
            authors_str = ", ".join(authors[:6])
            if len(authors) > 6:
                authors_str += " et al."
            j_str = f"{j_title} ({j_abbr}). {year}"
            if volume and issue and pages:
                j_str += f";{volume}({issue}):{pages}"
            evidence_str = ""
            if evidence_level or evidence_grade:
                evidence_str = f"\nEvidence: {evidence_level}, {evidence_grade}"
            mesh_str = "; ".join(mesh_terms[:12]) if mesh_terms else "N/A"

            text = (
                f"Title: {title}\n\n"
                f"Authors: {authors_str}\n"
                f"Journal: {j_str}.\n"
                f"DOI: {doi}\n"
                f"Publication Type: {pub_type}"
                f"{evidence_str}\n\n"
                f"Abstract:\n{abstract}\n\n"
                f"MeSH Terms: {mesh_str}"
            )
            docs.append(Document(
                id=f"pubmed-{pmid}",
                text=text,
                metadata={
                    "pmid": pmid, "title": title, "authors": authors,
                    "journal": j_title, "year": year, "doi": doi,
                    "evidence_level": evidence_level, "evidence_grade": evidence_grade,
                    "publication_type": pub_type, "mesh_terms": mesh_terms,
                    "source_type": "pubmed_abstract",
                    "source_file": xml_file.name,
                },
                tag=DataTag.SYNTHETIC,
            ))
        except Exception:
            continue

    return docs


def _load_transcripts() -> list[Document]:
    folder = _SYNTHETIC / "transcripts"
    if not folder.exists():
        return []
    docs = []
    for f in sorted(folder.glob("note_*.txt")):
        raw = f.read_text(encoding="utf-8")
        meta, body = _parse_frontmatter(raw)
        docs.append(Document(
            id=meta.get("encounter_id", f.stem),
            text=body,
            metadata={
                "encounter_id":   meta.get("encounter_id",   ""),
                "encounter_type": meta.get("encounter_type", ""),
                "condition":      meta.get("condition",      ""),
                "icd10_primary":  meta.get("icd10_primary",  ""),
                "source_type":    "soap_note",
                "source_file":    f.name,
            },
            tag=DataTag.SYNTHETIC,
        ))
    return docs


def _parse_fhir_bundle(xml_file: Path) -> tuple[str, dict]:
    """Parse a FHIR R4 Bundle XML file → (plain_text, metadata_dict)."""
    root = ET.parse(xml_file).getroot()
    lines = []

    # ── Encounter resource ────────────────────────────────────────────────
    enc      = root.find(".//f:Encounter",  _FHIR)
    enc_id   = enc_type = enc_date = enc_dept = ""
    enc_attending = enc_reason = enc_discharge = enc_followup = ""
    if enc is not None:
        enc_id   = _fhir_val(enc, "id")
        cls_el   = enc.find("f:class", _FHIR)
        if cls_el is not None:
            d = cls_el.find("f:display", _FHIR)
            enc_type = d.get("value", "") if d is not None else ""
        period  = enc.find("f:period", _FHIR)
        if period is not None:
            enc_date = _fhir_val(period, "start")
        sp = enc.find("f:serviceProvider", _FHIR)
        if sp is not None:
            d = sp.find("f:display", _FHIR)
            enc_dept = d.get("value", "") if d is not None else ""
        part = enc.find("f:participant", _FHIR)
        if part is not None:
            ind = part.find("f:individual", _FHIR)
            if ind is not None:
                d = ind.find("f:display", _FHIR)
                enc_attending = d.get("value", "") if d is not None else ""
        reason = enc.find("f:reasonCode", _FHIR)
        if reason is not None:
            t = reason.find("f:text", _FHIR)
            enc_reason = t.get("value", "") if t is not None else ""
        enc_discharge = _fhir_ext(enc, "urn:poc:discharge-summary")
        enc_followup  = _fhir_ext(enc, "urn:poc:follow-up")

    # ── Patient resource ──────────────────────────────────────────────────
    pt = root.find(".//f:Patient", _FHIR)
    pt_mrn = pt_name = pt_dob = pt_sex = pt_race = pt_insurance = ""
    if pt is not None:
        pt_mrn = _fhir_val(pt, "id")
        name_el = pt.find("f:name", _FHIR)
        if name_el is not None:
            t = name_el.find("f:text", _FHIR)
            pt_name = t.get("value", "") if t is not None else ""
        pt_dob       = _fhir_val(pt, "birthDate")
        pt_sex       = _fhir_val(pt, "gender").capitalize()
        pt_race      = _fhir_ext(pt, "urn:poc:race")
        pt_insurance = _fhir_ext(pt, "urn:poc:insurance")

    lines += [
        "ENCOUNTER RECORD", "================",
        f"Encounter ID: {enc_id}",
        f"Type: {enc_type}",
        f"Date: {enc_date}",
        f"Department: {enc_dept}",
        f"Attending: {enc_attending}",
        f"Admitting Diagnosis: {enc_reason}",
        "",
        "PATIENT DEMOGRAPHICS",
        f"Name: {pt_name}",
        f"DOB: {pt_dob}",
        f"Sex: {pt_sex}  Race: {pt_race}",
        f"MRN: {pt_mrn}  Insurance: {pt_insurance}",
    ]

    # ── Diagnoses ─────────────────────────────────────────────────────────
    conditions = root.findall(".//f:Condition", _FHIR)
    if conditions:
        lines += ["", "DIAGNOSES"]
        for cond in conditions:
            icd = desc = cat_type = ""
            code_el = cond.find("f:code", _FHIR)
            if code_el is not None:
                coding = code_el.find("f:coding", _FHIR)
                if coding is not None:
                    c = coding.find("f:code", _FHIR)
                    icd = c.get("value", "") if c is not None else ""
                t = code_el.find("f:text", _FHIR)
                desc = t.get("value", "") if t is not None else ""
            cat_el = cond.find("f:category", _FHIR)
            if cat_el is not None:
                t = cat_el.find("f:text", _FHIR)
                cat_type = t.get("value", "") if t is not None else ""
            lines.append(f"  [{cat_type}] {icd} — {desc}")

    # ── Procedures ────────────────────────────────────────────────────────
    procedures = root.findall(".//f:Procedure", _FHIR)
    if procedures:
        lines += ["", "PROCEDURES"]
        for proc in procedures:
            cpt = proc_desc = ""
            code_el = proc.find("f:code", _FHIR)
            if code_el is not None:
                coding = code_el.find("f:coding", _FHIR)
                if coding is not None:
                    c = coding.find("f:code", _FHIR)
                    cpt = c.get("value", "") if c is not None else ""
                t = code_el.find("f:text", _FHIR)
                proc_desc = t.get("value", "") if t is not None else ""
            lines.append(f"  CPT {cpt}: {proc_desc}")

    # ── Observations: vitals and labs ─────────────────────────────────────
    bp_s = bp_d = hr = rr = temp = spo2 = weight = bmi_val = ""
    lab_rows: list[tuple[str, str, str, str]] = []   # (name, value, ref, flag)

    for obs in root.findall(".//f:Observation", _FHIR):
        cat_code = _obs_category(obs)

        if cat_code == "vital-signs":
            # BP is a component observation
            for comp in obs.findall("f:component", _FHIR):
                comp_code_el = comp.find("f:code", _FHIR)
                if comp_code_el is None:
                    continue
                comp_coding = comp_code_el.find("f:coding", _FHIR)
                if comp_coding is None:
                    continue
                loinc_el = comp_coding.find("f:code", _FHIR)
                loinc = loinc_el.get("value", "") if loinc_el is not None else ""
                vq = comp.find("f:valueQuantity", _FHIR)
                v_el = vq.find("f:value", _FHIR) if vq is not None else None
                val  = v_el.get("value", "") if v_el is not None else ""
                if loinc == "8480-6":
                    bp_s = val
                elif loinc == "8462-4":
                    bp_d = val

            # Scalar vitals
            obs_code_el = obs.find("f:code", _FHIR)
            if obs_code_el is not None:
                coding = obs_code_el.find("f:coding", _FHIR)
                if coding is not None:
                    loinc_el = coding.find("f:code", _FHIR)
                    loinc = loinc_el.get("value", "") if loinc_el is not None else ""
                    vq = obs.find("f:valueQuantity", _FHIR)
                    v_el = vq.find("f:value", _FHIR) if vq is not None else None
                    val  = v_el.get("value", "") if v_el is not None else ""
                    if loinc == "8867-4":
                        hr    = val
                    elif loinc == "9279-1":
                        rr    = val
                    elif loinc == "8310-5":
                        temp  = val
                    elif loinc == "59408-5":
                        spo2  = val
                    elif loinc == "29463-7":
                        weight = val
                    elif loinc == "39156-5":
                        bmi_val = val

        elif cat_code in ("laboratory", "Laboratory"):
            code_el = obs.find("f:code", _FHIR)
            lab_name = ""
            if code_el is not None:
                t = code_el.find("f:text", _FHIR)
                lab_name = t.get("value", "") if t is not None else ""

            # valueQuantity or valueString
            vq = obs.find("f:valueQuantity", _FHIR)
            vs = obs.find("f:valueString",   _FHIR)
            lab_val = ""
            if vq is not None:
                v_el = vq.find("f:value", _FHIR)
                lab_val = v_el.get("value", "") if v_el is not None else ""
            elif vs is not None:
                lab_val = vs.get("value", "")

            flag = ""
            interp = obs.find("f:interpretation", _FHIR)
            if interp is not None:
                t = interp.find("f:text", _FHIR)
                flag = t.get("value", "") if t is not None else ""

            ref = ""
            rr_el = obs.find("f:referenceRange", _FHIR)
            if rr_el is not None:
                t = rr_el.find("f:text", _FHIR)
                ref = t.get("value", "") if t is not None else ""

            if lab_name:
                lab_rows.append((lab_name, lab_val, ref, flag))

    if any([bp_s, hr, rr, temp, spo2]):
        lines += ["", "VITAL SIGNS  "]
        vs_parts = []
        if bp_s and bp_d:
            vs_parts.append(f"BP {bp_s}/{bp_d} mmHg")
        if hr:
            vs_parts.append(f"HR {hr} bpm")
        if rr:
            vs_parts.append(f"RR {rr}")
        if temp:
            vs_parts.append(f"Temp {temp}°C")
        if spo2:
            vs_parts.append(f"SpO2 {spo2}%")
        if weight:
            vs_parts.append(f"Wt {weight} kg")
        if bmi_val:
            vs_parts.append(f"BMI {bmi_val}")
        lines.append(f"  {' | '.join(vs_parts)}")

    if lab_rows:
        lines += ["", "LABORATORY RESULTS"]
        for lab_name, lab_val, ref, flag in lab_rows:
            if lab_name == "Microbiology Results":
                lines += ["", "MICROBIOLOGY", f"  {lab_val}"]
            else:
                flag_str = f" [{flag}]" if flag and flag != "NORMAL" else ""
                ref_str  = f" (ref {ref})" if ref else ""
                lines.append(f"  {lab_name}: {lab_val}{ref_str}{flag_str}")

    # ── Medications ───────────────────────────────────────────────────────
    for timing_key, label in [
        ("at-admission", "at admission"),
        ("at-discharge", "at discharge"),
        ("current",      "current"),
    ]:
        meds_for_timing = []
        for mr in root.findall(".//f:MedicationRequest", _FHIR):
            if _fhir_ext(mr, "urn:poc:medication-timing") != timing_key:
                continue
            mc = mr.find("f:medicationCodeableConcept", _FHIR)
            med_text = ""
            if mc is not None:
                t = mc.find("f:text", _FHIR)
                med_text = t.get("value", "") if t is not None else ""
            indication = ""
            di = mr.find("f:dosageInstruction", _FHIR)
            if di is not None:
                ai = di.find("f:additionalInstruction", _FHIR)
                if ai is not None:
                    t = ai.find("f:text", _FHIR)
                    indication = t.get("value", "") if t is not None else ""
            suffix = f" [{indication}]" if indication else ""
            meds_for_timing.append(f"  {med_text}{suffix}")
        if meds_for_timing:
            lines += ["", f"MEDICATIONS ({label})"]
            lines.extend(meds_for_timing)

    # ── Allergies ─────────────────────────────────────────────────────────
    allergies = root.findall(".//f:AllergyIntolerance", _FHIR)
    if allergies:
        lines += ["", "ALLERGIES"]
        for ai in allergies:
            allergen  = _fhir_text(ai, "code")
            reaction  = ""
            severity  = ""
            rxn_el    = ai.find("f:reaction", _FHIR)
            if rxn_el is not None:
                sev_el = rxn_el.find("f:severity", _FHIR)
                severity = sev_el.get("value", "").capitalize() if sev_el is not None else ""
                mf_el  = rxn_el.find("f:manifestation", _FHIR)
                if mf_el is not None:
                    t = mf_el.find("f:text", _FHIR)
                    reaction = t.get("value", "") if t is not None else ""
            lines.append(f"  {allergen}: {reaction} ({severity})")

    if enc_discharge:
        lines += ["", "DISCHARGE SUMMARY", enc_discharge]
    if enc_followup:
        lines += ["", f"FOLLOW-UP: {enc_followup}"]

    meta = {
        "encounter_id":   enc_id,
        "mrn":            pt_mrn,
        "encounter_type": enc_type,
        "encounter_date": enc_date,
        "source_type":    "ehr_encounter",
        "source_file":    xml_file.name,
    }
    return "\n".join(lines), meta


def _load_encounters() -> list[Document]:
    folder = _SYNTHETIC / "encounters"
    if not folder.exists():
        return []
    docs = []
    for xml_file in sorted(folder.glob("enc_*.xml")):
        try:
            text, meta = _parse_fhir_bundle(xml_file)
            docs.append(Document(
                id=meta.get("encounter_id", xml_file.stem),
                text=text,
                metadata=meta,
                tag=DataTag.SYNTHETIC,
            ))
        except Exception:
            continue
    return docs


def _load_referrals() -> list[Document]:
    folder = _SYNTHETIC / "referrals"
    if not folder.exists():
        return []
    docs = []
    for f in sorted(folder.glob("ref_*.txt")):
        raw  = f.read_text(encoding="utf-8")
        meta, body = _parse_frontmatter(raw)
        docs.append(Document(
            id=meta.get("referral_id", f.stem),
            text=body,
            metadata={
                "referral_id":  meta.get("referral_id",  ""),
                "specialty":    meta.get("specialty",    ""),
                "urgency":      meta.get("urgency",      ""),
                "patient_name": meta.get("patient_name", ""),
                "patient_dob":  meta.get("patient_dob",  ""),
                "patient_sex":  meta.get("patient_sex",  ""),
                "insurance":    meta.get("insurance",    ""),
                "source_type":  "referral_letter",
                "source_file":  f.name,
            },
            tag=DataTag.SYNTHETIC,
        ))
    return docs


def _load_diagnostic_cases() -> list[Document]:
    csv_file = _SYNTHETIC / "diagnostic_cases.csv"
    if not csv_file.exists():
        return []

    lab_fields = [
        "wbc_k_ul", "lactate_mmol_l", "platelets_k_ul", "creatinine_mg_dl",
        "bilirubin_mg_dl", "ph_arterial", "paco2_mmhg", "hco3_meq_l",
        "glucose_mg_dl", "sodium_meq_l", "potassium_meq_l",
        "procalcitonin_ng_ml", "fibrinogen_mg_dl", "inr", "albumin_g_dl",
        "hs_troponin_t_ng_l", "bnp_pg_ml", "hba1c_percent",
    ]
    score_fields = [
        ("sirs_criteria_met",             "SIRS criteria met"),
        ("sirs_positive",                 "SIRS positive"),
        ("qsofa_score",                   "qSOFA score"),
        ("sofa_score",                    "SOFA score"),
        ("news2_score",                   "NEWS2 score"),
        ("news2_risk_level",              "NEWS2 risk level"),
        ("timi_risk_score",               "TIMI risk score"),
        ("heart_score",                   "HEART score"),
        ("framingham_10yr_cvd_risk_percent", "Framingham 10yr CVD risk %"),
        ("nyha_class",                    "NYHA class"),
    ]

    docs = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                differentials = json.loads(row.get("differentials", "[]"))
                diff_lines = []
                for dx in differentials:
                    features = "; ".join(dx.get("key_features", [])[:3])
                    pct = int(float(dx.get("confidence", 0)) * 100)
                    diff_lines.append(
                        f"  [{dx.get('rank','?')}] {dx.get('diagnosis','')} — "
                        f"Confidence: {pct}%\n      {features}"
                    )

                lab_lines   = [f"  {k}: {row[k]}" for k in lab_fields if row.get(k) not in ("", None)]
                score_lines = [f"  {label}: {row[field]}"
                               for field, label in score_fields if row.get(field) not in ("", None)]

                text = (
                    f"DIAGNOSTIC CASE: {row['case_id']}\n"
                    f"Presentation: {row['presentation']}\n\n"
                    f"Demographics: Age {row['age']}, Sex {row['sex']}, BMI {row['bmi']}\n"
                    f"Charlson Comorbidity Index: {row['charlson_comorbidity_index']}\n"
                    f"Comorbidities: {row['comorbidities']}\n\n"
                    f"VITAL SIGNS:\n"
                    f"  HR {row['heart_rate_bpm']} bpm | "
                    f"BP {row['systolic_bp_mmhg']}/{row['diastolic_bp_mmhg']} mmHg | "
                    f"MAP {row['map_mmhg']} | "
                    f"RR {row['respiratory_rate_per_min']} | "
                    f"Temp {row['temperature_celsius']}°C | "
                    f"SpO2 {row['spo2_percent']}%\n\n"
                    f"LABORATORY VALUES:\n" + "\n".join(lab_lines) + "\n\n"
                    f"SEVERITY SCORES:\n" + "\n".join(score_lines) + "\n\n"
                    f"DIFFERENTIAL DIAGNOSIS:\n" + "\n".join(diff_lines)
                )
                if row.get("outcome_48h"):
                    text += f"\n\nOUTCOME (48h): {row['outcome_48h']}"
                if row.get("outcome_28day"):
                    text += f"\nOUTCOME (28d): {row['outcome_28day']}"

                docs.append(Document(
                    id=row["case_id"],
                    text=text,
                    metadata={
                        "case_id":               row["case_id"],
                        "presentation":          row["presentation"],
                        "primary_diagnosis":     row.get("top_dx_icd10", ""),
                        "sepsis_alert_triggered": row.get("sepsis_alert_triggered", "False") == "True",
                        "qsofa_score":           row.get("qsofa_score"),
                        "sofa_score":            row.get("sofa_score"),
                        "source_type":           "diagnostic_case",
                        "source_file":           csv_file.name,
                    },
                    tag=DataTag.SYNTHETIC,
                ))
            except Exception:
                continue
    return docs


def _load_vitals() -> list[Document]:
    csv_file = _RANDOMISED / "vitals.csv"
    if not csv_file.exists():
        return []

    patients: dict[str, list[dict]] = {}
    with open(csv_file, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            patients.setdefault(row["patient_id"], []).append(row)

    docs = []
    for pid, readings in patients.items():
        header = (
            f"[RANDOMISED] Patient vital sign stream\n"
            f"Patient ID: {pid}\n"
            f"Readings: {len(readings)} hourly observations\n\n"
            f"Hour | HR  | SBP/DBP       | RR  | Temp  | SpO2  | Lactate\n"
            f"-----|-----|---------------|-----|-------|-------|--------"
        )
        rows = []
        for r in readings:
            rows.append(
                f"T+{int(float(r['timestamp_offset_hours'])):02d}h | "
                f"{float(r['heart_rate_bpm']):3.0f} | "
                f"{float(r['systolic_bp_mmhg']):3.0f}/{float(r['diastolic_bp_mmhg']):3.0f} mmHg | "
                f"{float(r['respiratory_rate_per_min']):3.0f} | "
                f"{float(r['temperature_celsius']):4.1f}°C | "
                f"{float(r['spo2_percent']):4.1f}% | "
                f"{float(r['lactate_mmol_l']):.1f}"
            )
        docs.append(Document(
            id=f"vitals-{pid}",
            text=header + "\n" + "\n".join(rows),
            metadata={
                "patient_id":  pid,
                "n_readings":  len(readings),
                "source_type": "randomised_vitals",
                "source_file": csv_file.name,
            },
            tag=DataTag.RANDOMISED,
        ))
    return docs


def _load_surgical_frames() -> list[Document]:
    json_file = _RANDOMISED / "surgical_frames.json"
    if not json_file.exists():
        return []

    with open(json_file, encoding="utf-8") as f:
        payload = json.load(f)

    procedure = payload.get("procedure", "")
    frames    = payload.get("frames", [])
    n_frames  = payload.get("n_frames", len(frames))

    header_lines = [
        f"[RANDOMISED] Surgical Frame Detections",
        f"Procedure: {procedure}",
        f"Total frames: {n_frames} | FPS: {payload.get('fps', 25)}",
        "",
    ]
    frame_lines = []
    for fr in frames:
        det = "; ".join(f"{d['label']}({d['confidence']:.2f})" for d in fr.get("detections", []))
        risks = [d.get("risk_flag") for d in fr.get("detections", []) if d.get("risk_flag")]
        risk_str = f" | RISK: {', '.join(risks)}" if risks else ""
        frame_lines.append(
            f"Frame {fr['frame_index']:05d} t={fr['timestamp_s']:6.1f}s "
            f"[{fr['phase']}] {det}{risk_str}"
        )

    return [Document(
        id="surgical-frames-randomised",
        text="\n".join(header_lines + frame_lines),
        metadata={
            "procedure":   procedure,
            "n_frames":    n_frames,
            "source_type": "randomised_surgical_frames",
            "source_file": json_file.name,
        },
        tag=DataTag.RANDOMISED,
    )]


# ── Public API ─────────────────────────────────────────────────────────────────

def load_all(
    include_real_public: bool = False,
    pubmed_query: str = "sepsis management clinical guidelines",
    pubmed_max:   int = 5,
) -> list[Document]:
    """Return all documents from every data source."""
    docs: list[Document] = []
    docs.extend(_load_research_corpus())
    docs.extend(_load_transcripts())
    docs.extend(_load_encounters())
    docs.extend(_load_referrals())
    docs.extend(_load_diagnostic_cases())
    docs.extend(_load_vitals())
    docs.extend(_load_surgical_frames())
    if include_real_public:
        docs.extend(fetch_pubmed_abstracts(pubmed_query, pubmed_max))
    return docs


def load_for_agent(
    agent_name:          str,
    include_real_public: bool = False,
    pubmed_query:        str  = "clinical evidence",
    pubmed_max:          int  = 5,
) -> list[Document]:
    """Return documents relevant to a specific agent.

    agent_name: one of research | documentation | diagnostic | coordination | surgical
    """
    sources = _AGENT_SOURCES.get(agent_name.lower(), [])
    docs: list[Document] = []

    _loader_map = {
        "research_corpus": _load_research_corpus,
        "transcripts":     _load_transcripts,
        "encounters":      _load_encounters,
        "referrals":       _load_referrals,
        "diagnostic_cases": _load_diagnostic_cases,
        "vitals":          _load_vitals,
        "surgical_frames": _load_surgical_frames,
    }
    for src in sources:
        if src == "pubmed_real":
            if include_real_public:
                docs.extend(fetch_pubmed_abstracts(pubmed_query, pubmed_max))
        elif src in _loader_map:
            docs.extend(_loader_map[src]())

    return docs


def load_real_public(
    query:       str = "sepsis clinical guidelines",
    max_results: int = 10,
) -> list[Document]:
    """Fetch live PubMed abstracts (REAL_PUBLIC tag). Requires network."""
    return fetch_pubmed_abstracts(query, max_results)


def summarise(docs: list[Document]) -> dict:
    """Return tag counts and source type counts for a list of Documents."""
    tag_counts:    dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for doc in docs:
        tag_counts[doc.tag.value] = tag_counts.get(doc.tag.value, 0) + 1
        src = doc.metadata.get("source_type", "unknown")
        source_counts[src] = source_counts.get(src, 0) + 1
    return {
        "total":     len(docs),
        "by_tag":    tag_counts,
        "by_source": source_counts,
    }
