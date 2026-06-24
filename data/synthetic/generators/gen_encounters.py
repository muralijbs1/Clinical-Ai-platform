#!/usr/bin/env python3
"""
Generator: writes synthetic EHR encounter records as FHIR R4 XML Bundle files.

Run once to produce data files. Re-run to regenerate or add more encounters.
Output: data/synthetic/encounters/enc_001.xml ... enc_016.xml

Each file is a FHIR R4 Bundle (type=collection) containing Patient, Encounter,
Condition, Procedure, Observation (vitals + labs), MedicationRequest, and
AllergyIntolerance resources. This matches the structure of real EHR exports.

DATA TAG: SYNTHETIC — realistic FHIR records, no real patients.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

_OUT_DIR = Path(__file__).parent.parent / "encounters"

NS = "http://hl7.org/fhir"
ET.register_namespace("", NS)


def _f(parent, tag):
    """Append a FHIR-namespaced child element."""
    return ET.SubElement(parent, f"{{{NS}}}{tag}")


def _val(parent, tag, value):
    """Append <tag value="..."/> — the FHIR pattern for primitives."""
    el = _f(parent, tag)
    el.set("value", str(value))
    return el


def _ext(parent, url, value_str):
    """Append <extension url="..."><valueString value="..."/></extension>."""
    ext = _f(parent, "extension")
    ext.set("url", url)
    _val(ext, "valueString", value_str)


def _coding(parent, code, display=""):
    coding = _f(parent, "coding")
    _val(coding, "code", code)
    if display:
        _val(coding, "display", display)
    return coding


def _build_patient(enc: dict) -> ET.Element:
    dem = enc["demographics"]
    pt = ET.Element(f"{{{NS}}}Patient")
    _val(pt, "id", dem.get("mrn", enc.get("mrn", "unknown")))

    ident = _f(pt, "identifier")
    _val(ident, "system", "urn:hospital:mrn")
    _val(ident, "value", dem.get("mrn", enc.get("mrn", "")))

    name = _f(pt, "name")
    _val(name, "text", dem.get("name", ""))

    _val(pt, "birthDate", dem.get("dob", ""))
    _val(pt, "gender", dem.get("sex", "").lower())

    for url_key, field in [
        ("urn:poc:race", "race"),
        ("urn:poc:language", "language"),
        ("urn:poc:insurance", "insurance"),
        ("urn:poc:member-id", "member_id"),
    ]:
        if dem.get(field):
            _ext(pt, url_key, dem[field])

    return pt


def _build_encounter(enc: dict) -> ET.Element:
    e = ET.Element(f"{{{NS}}}Encounter")
    _val(e, "id", enc["encounter_id"])
    _val(e, "status", "finished")

    cls = _f(e, "class")
    _coding(cls, "IMP" if "Inpatient" in enc["encounter_type"] else "AMB",
            enc["encounter_type"])

    period = _f(e, "period")
    _val(period, "start", enc["encounter_date"])
    if enc.get("discharge_date"):
        _val(period, "end", enc["discharge_date"])

    if enc.get("length_of_stay_days"):
        ln = _f(e, "length")
        _val(ln, "value", enc["length_of_stay_days"])
        _val(ln, "unit", "days")

    sp = _f(e, "serviceProvider")
    _val(sp, "display", enc.get("department", ""))

    participant = _f(e, "participant")
    individual = _f(participant, "individual")
    _val(individual, "display", enc.get("attending", ""))

    reason = _f(e, "reasonCode")
    _val(reason, "text", enc.get("admitting_diagnosis", ""))

    _ext(e, "urn:poc:data-tag", "SYNTHETIC")

    if enc.get("discharge_summary"):
        _ext(e, "urn:poc:discharge-summary", enc["discharge_summary"])
    if enc.get("follow_up"):
        _ext(e, "urn:poc:follow-up", enc["follow_up"])

    return e


def _build_condition(enc_id: str, mrn: str, idx: int, dx: dict) -> ET.Element:
    cond = ET.Element(f"{{{NS}}}Condition")
    _val(cond, "id", f"cond-{enc_id}-{idx}")

    cat = _f(cond, "category")
    cat_coding = _coding(cat, "encounter-diagnosis")
    _val(cat, "text", dx.get("type", "Secondary"))

    code = _f(cond, "code")
    code_coding = _f(code, "coding")
    _val(code_coding, "system", "http://hl7.org/fhir/sid/icd-10")
    _val(code_coding, "code", dx["code"])
    _val(code, "text", dx.get("description", ""))

    enc_ref = _f(cond, "encounter")
    _val(enc_ref, "reference", f"Encounter/{enc_id}")

    subj = _f(cond, "subject")
    _val(subj, "reference", f"Patient/{mrn}")

    return cond


def _build_procedure(enc_id: str, mrn: str, idx: int, px: dict) -> ET.Element:
    proc = ET.Element(f"{{{NS}}}Procedure")
    _val(proc, "id", f"proc-{enc_id}-{idx}")
    _val(proc, "status", "completed")

    code = _f(proc, "code")
    code_coding = _f(code, "coding")
    _val(code_coding, "system", "http://www.ama-assn.org/go/cpt")
    _val(code_coding, "code", px.get("code", ""))
    _val(code, "text", px.get("description", ""))

    enc_ref = _f(proc, "encounter")
    _val(enc_ref, "reference", f"Encounter/{enc_id}")

    subj = _f(proc, "subject")
    _val(subj, "reference", f"Patient/{mrn}")

    return proc


_VITAL_LOINC = {
    "bp": ("55284-4", "Blood pressure"),
    "heart_rate_bpm": ("8867-4", "Heart rate"),
    "respiratory_rate_per_min": ("9279-1", "Respiratory rate"),
    "temperature_c": ("8310-5", "Body temperature"),
    "spo2_percent": ("59408-5", "Oxygen saturation"),
    "weight_kg": ("29463-7", "Body weight"),
    "bmi": ("39156-5", "Body mass index"),
}


def _build_vitals_obs(enc_id: str, mrn: str, vs: dict) -> list:
    obs_list = []

    # Blood pressure — component observation
    obs = ET.Element(f"{{{NS}}}Observation")
    _val(obs, "id", f"obs-{enc_id}-bp")
    _val(obs, "status", "final")
    cat = _f(obs, "category")
    _coding(cat, "vital-signs", "Vital Signs")
    code = _f(obs, "code")
    code_coding = _f(code, "coding")
    _val(code_coding, "system", "http://loinc.org")
    _val(code_coding, "code", "55284-4")
    _val(code_coding, "display", "Blood pressure")
    enc_ref = _f(obs, "encounter")
    _val(enc_ref, "reference", f"Encounter/{enc_id}")
    subj = _f(obs, "subject")
    _val(subj, "reference", f"Patient/{mrn}")
    # Systolic component
    comp_s = _f(obs, "component")
    comp_s_code = _f(comp_s, "code")
    comp_s_coding = _f(comp_s_code, "coding")
    _val(comp_s_coding, "system", "http://loinc.org")
    _val(comp_s_coding, "code", "8480-6")
    _val(comp_s_coding, "display", "Systolic BP")
    comp_s_vq = _f(comp_s, "valueQuantity")
    _val(comp_s_vq, "value", vs.get("bp_systolic", ""))
    _val(comp_s_vq, "unit", "mmHg")
    # Diastolic component
    comp_d = _f(obs, "component")
    comp_d_code = _f(comp_d, "code")
    comp_d_coding = _f(comp_d_code, "coding")
    _val(comp_d_coding, "system", "http://loinc.org")
    _val(comp_d_coding, "code", "8462-4")
    _val(comp_d_coding, "display", "Diastolic BP")
    comp_d_vq = _f(comp_d, "valueQuantity")
    _val(comp_d_vq, "value", vs.get("bp_diastolic", ""))
    _val(comp_d_vq, "unit", "mmHg")
    obs_list.append(obs)

    # Simple scalar vitals
    simple = [
        ("heart_rate_bpm", "8867-4", "Heart rate", vs.get("heart_rate"), "bpm"),
        ("rr", "9279-1", "Respiratory rate", vs.get("respiratory_rate"), "/min"),
        ("temp", "8310-5", "Body temperature", vs.get("temperature_c"), "Cel"),
        ("spo2", "59408-5", "Oxygen saturation", vs.get("spo2_percent"), "%"),
        ("weight", "29463-7", "Body weight", vs.get("weight_kg"), "kg"),
        ("bmi", "39156-5", "Body mass index", vs.get("bmi"), "kg/m2"),
    ]
    for obs_id, loinc, display, value, unit in simple:
        if value is None:
            continue
        obs = ET.Element(f"{{{NS}}}Observation")
        _val(obs, "id", f"obs-{enc_id}-{obs_id}")
        _val(obs, "status", "final")
        cat = _f(obs, "category")
        _coding(cat, "vital-signs", "Vital Signs")
        code = _f(obs, "code")
        code_coding = _f(code, "coding")
        _val(code_coding, "system", "http://loinc.org")
        _val(code_coding, "code", loinc)
        _val(code_coding, "display", display)
        enc_ref = _f(obs, "encounter")
        _val(enc_ref, "reference", f"Encounter/{enc_id}")
        subj = _f(obs, "subject")
        _val(subj, "reference", f"Patient/{mrn}")
        vq = _f(obs, "valueQuantity")
        _val(vq, "value", value)
        _val(vq, "unit", unit)
        obs_list.append(obs)

    return obs_list


def _build_lab_obs(enc_id: str, mrn: str, labs: dict) -> list:
    obs_list = []
    for lab_name, result in labs.items():
        obs = ET.Element(f"{{{NS}}}Observation")
        _val(obs, "id", f"obs-{enc_id}-lab-{lab_name[:20]}")
        _val(obs, "status", "final")
        cat = _f(obs, "category")
        _coding(cat, "laboratory", "Laboratory")
        code = _f(obs, "code")
        _val(code, "text", lab_name)
        enc_ref = _f(obs, "encounter")
        _val(enc_ref, "reference", f"Encounter/{enc_id}")
        subj = _f(obs, "subject")
        _val(subj, "reference", f"Patient/{mrn}")
        vq = _f(obs, "valueQuantity")
        _val(vq, "value", result.get("value", ""))
        if result.get("flag") and result["flag"] not in ("NORMAL", ""):
            interp = _f(obs, "interpretation")
            _val(interp, "text", result["flag"])
        if result.get("ref"):
            rr = _f(obs, "referenceRange")
            _val(rr, "text", result["ref"])
        obs_list.append(obs)
    return obs_list


def _build_med_request(enc_id: str, mrn: str, idx: int, med: dict, timing: str) -> ET.Element:
    mr = ET.Element(f"{{{NS}}}MedicationRequest")
    _val(mr, "id", f"mr-{enc_id}-{timing[:3]}-{idx}")
    _val(mr, "status", "active")
    _val(mr, "intent", "order")
    _ext(mr, "urn:poc:medication-timing", timing)
    subj = _f(mr, "subject")
    _val(subj, "reference", f"Patient/{mrn}")
    enc_ref = _f(mr, "encounter")
    _val(enc_ref, "reference", f"Encounter/{enc_id}")
    drug_text = f"{med['drug']} {med['dose']} {med['route']} {med['frequency']}"
    mc = _f(mr, "medicationCodeableConcept")
    _val(mc, "text", drug_text)
    di = _f(mr, "dosageInstruction")
    _val(di, "text", f"{med['dose']} {med['route']} {med['frequency']}")
    if med.get("indication"):
        ai = _f(di, "additionalInstruction")
        _val(ai, "text", med["indication"])
    return mr


def _build_allergy(enc_id: str, mrn: str, idx: int, allergy: dict) -> ET.Element:
    ai = ET.Element(f"{{{NS}}}AllergyIntolerance")
    _val(ai, "id", f"allergy-{enc_id}-{idx}")
    subj = _f(ai, "patient")
    _val(subj, "reference", f"Patient/{mrn}")
    code = _f(ai, "code")
    _val(code, "text", allergy.get("allergen", ""))
    reaction = _f(ai, "reaction")
    severity_map = {"Mild": "mild", "Moderate": "moderate", "Severe": "severe"}
    severity = severity_map.get(allergy.get("severity", ""), "moderate")
    _val(reaction, "severity", severity)
    manifestation = _f(reaction, "manifestation")
    _val(manifestation, "text", allergy.get("reaction", ""))
    return reaction


def _build_microbiology(enc_id: str, mrn: str, micro: dict) -> ET.Element:
    obs = ET.Element(f"{{{NS}}}Observation")
    _val(obs, "id", f"obs-{enc_id}-micro")
    _val(obs, "status", "final")
    cat = _f(obs, "category")
    _coding(cat, "laboratory", "Microbiology")
    code = _f(obs, "code")
    _val(code, "text", "Microbiology Results")
    subj = _f(obs, "subject")
    _val(subj, "reference", f"Patient/{mrn}")
    enc_ref = _f(obs, "encounter")
    _val(enc_ref, "reference", f"Encounter/{enc_id}")
    _val(obs, "valueString", " | ".join(f"{k}: {v}" for k, v in micro.items()))
    return obs


def _build_bundle(enc: dict) -> ET.Element:
    mrn = enc.get("mrn", enc["demographics"].get("mrn", enc["encounter_id"]))
    enc_id = enc["encounter_id"]

    bundle = ET.Element(f"{{{NS}}}Bundle")
    _val(bundle, "id", f"bundle-{enc_id}")
    _val(bundle, "type", "collection")
    _val(bundle, "timestamp", f"{enc['encounter_date']}T00:00:00+00:00")

    def _entry(resource: ET.Element):
        entry = _f(bundle, "entry")
        res_el = _f(entry, "resource")
        res_el.append(resource)

    # Patient
    _entry(_build_patient(enc))

    # Encounter
    _entry(_build_encounter(enc))

    # Diagnoses
    for i, dx in enumerate(enc.get("diagnoses", []), 1):
        _entry(_build_condition(enc_id, mrn, i, dx))

    # Procedures
    for i, px in enumerate(enc.get("procedures", []), 1):
        _entry(_build_procedure(enc_id, mrn, i, px))

    # Vitals observations
    vs = enc.get("vital_signs", {})
    for obs in _build_vitals_obs(enc_id, mrn, vs):
        _entry(obs)

    # Lab observations
    for obs in _build_lab_obs(enc_id, mrn, enc.get("labs", {})):
        _entry(obs)

    # Microbiology (ICU encounter)
    if enc.get("microbiology"):
        _entry(_build_microbiology(enc_id, mrn, enc["microbiology"]))

    # Medications
    for timing, key in [
        ("at-admission", "medications_on_admission"),
        ("at-discharge", "medications_at_discharge"),
        ("current", "medications_current"),
    ]:
        for i, med in enumerate(enc.get(key, []), 1):
            _entry(_build_med_request(enc_id, mrn, i, med, timing))

    # Allergies
    for i, allergy in enumerate(enc.get("allergies", []), 1):
        ai = ET.Element(f"{{{NS}}}AllergyIntolerance")
        _val(ai, "id", f"allergy-{enc_id}-{i}")
        subj = _f(ai, "patient")
        _val(subj, "reference", f"Patient/{mrn}")
        code = _f(ai, "code")
        _val(code, "text", allergy.get("allergen", ""))
        reaction = _f(ai, "reaction")
        severity_map = {"Mild": "mild", "Moderate": "moderate", "Severe": "severe"}
        _val(reaction, "severity", severity_map.get(allergy.get("severity", ""), "moderate"))
        manifestation = _f(reaction, "manifestation")
        _val(manifestation, "text", allergy.get("reaction", ""))
        _entry(ai)

    return bundle


# ── Encounter data ─────────────────────────────────────────────────────────────

_ENCOUNTERS = [
    {
        "encounter_id": "ENC-2025-001842",
        "mrn": "MRN-7283940",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-03-14",
        "discharge_date": "2025-03-18",
        "length_of_stay_days": 4,
        "department": "Cardiology / Cardiac Care Unit",
        "attending": "Dr. James Liu, MD (Cardiology)",
        "admitting_diagnosis": "NSTEMI",
        "demographics": {
            "name": "James Patterson", "dob": "1961-07-22", "age": 63,
            "sex": "Male", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-7283940", "insurance": "Aetna Commercial",
            "member_id": "AC-7382910-1",
        },
        "diagnoses": [
            {"code": "I21.4", "description": "Non-ST elevation myocardial infarction", "type": "Primary"},
            {"code": "I25.10", "description": "Atherosclerotic heart disease, native coronary", "type": "Secondary"},
            {"code": "I10", "description": "Essential hypertension", "type": "Secondary"},
            {"code": "E78.5", "description": "Hyperlipidemia, unspecified", "type": "Secondary"},
            {"code": "E11.9", "description": "Type 2 diabetes mellitus, without complications", "type": "Secondary"},
        ],
        "procedures": [
            {"code": "93459", "description": "Left heart catheterisation with coronary angiography"},
            {"code": "92928", "description": "Percutaneous coronary revascularization with stent (LAD)"},
            {"code": "93000", "description": "Electrocardiogram, 12-lead"},
        ],
        "vital_signs": {
            "bp_systolic": 162, "bp_diastolic": 94, "heart_rate": 98,
            "respiratory_rate": 20, "temperature_c": 37.1, "spo2_percent": 95,
            "weight_kg": 91.0, "bmi": 28.7,
        },
        "labs": {
            "hs_troponin_t_ng_l": {"value": 65, "ref": "<14", "flag": "HIGH"},
            "ck_mb_ng_ml": {"value": 9.4, "ref": "<5.0", "flag": "HIGH"},
            "bnp_pg_ml": {"value": 148, "ref": "<100", "flag": "HIGH"},
            "wbc_k_ul": {"value": 9.8, "ref": "4.5-11.0", "flag": "NORMAL"},
            "hemoglobin_g_dl": {"value": 14.6, "ref": "13.5-17.5", "flag": "NORMAL"},
            "platelets_k_ul": {"value": 312, "ref": "150-400", "flag": "NORMAL"},
            "sodium_meq_l": {"value": 139, "ref": "136-145", "flag": "NORMAL"},
            "potassium_meq_l": {"value": 4.2, "ref": "3.5-5.0", "flag": "NORMAL"},
            "creatinine_mg_dl": {"value": 1.1, "ref": "0.7-1.3", "flag": "NORMAL"},
            "egfr_ml_min": {"value": 72, "ref": ">60", "flag": "NORMAL"},
            "glucose_mg_dl": {"value": 194, "ref": "70-100", "flag": "HIGH"},
            "ldl_mg_dl": {"value": 162, "ref": "<100", "flag": "HIGH"},
            "hdl_mg_dl": {"value": 38, "ref": ">40", "flag": "LOW"},
            "triglycerides_mg_dl": {"value": 198, "ref": "<150", "flag": "HIGH"},
        },
        "medications_on_admission": [
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Atorvastatin", "dose": "40 mg", "route": "PO", "frequency": "QHS"},
            {"drug": "Metformin", "dose": "1000 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Omeprazole", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Aspirin", "dose": "81 mg", "route": "PO", "frequency": "QD"},
        ],
        "medications_at_discharge": [
            {"drug": "Aspirin", "dose": "81 mg", "route": "PO", "frequency": "QD", "indication": "Antiplatelet"},
            {"drug": "Ticagrelor", "dose": "90 mg", "route": "PO", "frequency": "BID", "indication": "DAPT post-PCI"},
            {"drug": "Atorvastatin", "dose": "80 mg", "route": "PO", "frequency": "QHS", "indication": "High-intensity statin"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD", "indication": "Post-MI cardioprotection"},
            {"drug": "Metoprolol succinate", "dose": "50 mg", "route": "PO", "frequency": "QD", "indication": "Beta-blocker post-MI"},
            {"drug": "Metformin", "dose": "500 mg", "route": "PO", "frequency": "BID", "indication": "DM2 (dose-reduced post-PCI)"},
            {"drug": "Omeprazole", "dose": "20 mg", "route": "PO", "frequency": "QD", "indication": "GI protection with DAPT"},
        ],
        "allergies": [
            {"allergen": "Sulfa drugs", "reaction": "Rash (maculopapular)", "severity": "Moderate"},
        ],
        "discharge_summary": (
            "Mr. Patterson presented with NSTEMI. Cardiac catheterisation on HD2 demonstrated 70% LAD "
            "stenosis; drug-eluting stent placed successfully (TIMI III flow achieved). Troponin peak "
            "892 ng/L, normalised by HD3. EF on echo 48%. Discharged HD4 on DAPT, high-intensity statin, "
            "beta-blocker. Follow-up cardiology 1 week, PCP 2 weeks, cardiac rehab referral made."
        ),
    },
    {
        "encounter_id": "ENC-2025-003291",
        "mrn": "MRN-5192837",
        "encounter_type": "Office Visit — Outpatient",
        "encounter_date": "2025-04-08",
        "department": "Internal Medicine",
        "attending": "Dr. Maria Garcia, MD (Internal Medicine)",
        "admitting_diagnosis": "Diabetes mellitus type 2 follow-up",
        "demographics": {
            "name": "Linda Nguyen", "dob": "1967-09-14", "age": 57,
            "sex": "Female", "race": "Asian", "language": "English",
            "mrn": "MRN-5192837", "insurance": "Cigna PPO",
            "member_id": "CG-4829310-2",
        },
        "diagnoses": [
            {"code": "E11.9", "description": "Type 2 diabetes mellitus, without complications", "type": "Primary"},
            {"code": "E11.40", "description": "Diabetic peripheral neuropathy, unspecified", "type": "Secondary"},
            {"code": "E11.65", "description": "Type 2 DM with hyperglycaemia", "type": "Secondary"},
            {"code": "I10", "description": "Essential hypertension", "type": "Secondary"},
            {"code": "E78.5", "description": "Hyperlipidemia, unspecified", "type": "Secondary"},
            {"code": "D50.9", "description": "Iron deficiency anaemia, unspecified", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 136, "bp_diastolic": 84, "heart_rate": 74,
            "respiratory_rate": 16, "temperature_c": 37.0, "spo2_percent": 99,
            "weight_kg": 88.0, "bmi": 32.3,
        },
        "labs": {
            "hba1c_percent": {"value": 8.9, "ref": "<7.0", "flag": "HIGH"},
            "fasting_glucose_mg_dl": {"value": 178, "ref": "70-100", "flag": "HIGH"},
            "urine_acr_mg_g": {"value": 68, "ref": "<30", "flag": "HIGH"},
            "wbc_k_ul": {"value": 7.2, "ref": "4.5-11.0", "flag": "NORMAL"},
            "hemoglobin_g_dl": {"value": 12.8, "ref": "12.0-15.5", "flag": "NORMAL"},
            "ferritin_ng_ml": {"value": 18, "ref": "12-150", "flag": "LOW-NORMAL"},
            "creatinine_mg_dl": {"value": 1.0, "ref": "0.6-1.1", "flag": "NORMAL"},
            "egfr_ml_min": {"value": 68, "ref": ">60", "flag": "NORMAL"},
            "ldl_mg_dl": {"value": 138, "ref": "<70 (DM goal)", "flag": "HIGH"},
            "tsh_miu_l": {"value": 2.4, "ref": "0.4-4.0", "flag": "NORMAL"},
        },
        "medications_current": [
            {"drug": "Metformin", "dose": "1000 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Amlodipine", "dose": "5 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Atorvastatin", "dose": "40 mg", "route": "PO", "frequency": "QHS"},
            {"drug": "Omeprazole", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Empagliflozin", "dose": "10 mg", "route": "PO", "frequency": "QD", "indication": "DM2 + DKD renoprotection"},
            {"drug": "Atorvastatin", "dose": "80 mg", "route": "PO", "frequency": "QHS", "indication": "Uptitrated — LDL <70"},
            {"drug": "Ferrous sulphate", "dose": "325 mg", "route": "PO", "frequency": "QD", "indication": "Iron deficiency"},
        ],
        "allergies": [
            {"allergen": "Penicillin", "reaction": "Rash", "severity": "Mild"},
            {"allergen": "Shellfish", "reaction": "Urticaria", "severity": "Moderate"},
        ],
        "follow_up": "3 months — recheck HbA1c, empagliflozin response, renal function. Ophthalmology URGENT (new dot haemorrhage OD).",
    },
    {
        "encounter_id": "ENC-2025-004771",
        "mrn": "MRN-6384920",
        "encounter_type": "Inpatient Hospitalization — ICU",
        "encounter_date": "2025-01-07",
        "discharge_date": "2025-01-14",
        "length_of_stay_days": 7,
        "department": "Medical Intensive Care Unit (MICU)",
        "attending": "Dr. Lisa Ramirez, MD (Pulmonary/Critical Care)",
        "admitting_diagnosis": "Septic shock — urosepsis",
        "demographics": {
            "name": "Eleanor Fitzgerald", "dob": "1950-11-30", "age": 74,
            "sex": "Female", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-6384920", "insurance": "Medicare Advantage — Humana",
            "member_id": "HM-3847291-1",
        },
        "diagnoses": [
            {"code": "A41.9", "description": "Sepsis, unspecified organism", "type": "Primary"},
            {"code": "R65.21", "description": "Severe sepsis with septic shock", "type": "Secondary"},
            {"code": "N39.0", "description": "Urinary tract infection", "type": "Secondary"},
            {"code": "N17.9", "description": "Acute kidney injury, unspecified", "type": "Secondary"},
            {"code": "I48.91", "description": "Unspecified atrial fibrillation", "type": "Secondary"},
            {"code": "I50.20", "description": "Unspecified systolic heart failure", "type": "Secondary"},
            {"code": "E11.9", "description": "Type 2 diabetes mellitus", "type": "Secondary"},
            {"code": "N18.3", "description": "Chronic kidney disease, stage 3b", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 88, "bp_diastolic": 54, "heart_rate": 118,
            "respiratory_rate": 28, "temperature_c": 39.8, "spo2_percent": 90,
            "weight_kg": 61.0, "bmi": 24.7,
        },
        "labs": {
            "wbc_k_ul": {"value": 22.4, "ref": "4.5-11.0", "flag": "HIGH"},
            "hemoglobin_g_dl": {"value": 9.8, "ref": "12.0-15.5", "flag": "LOW"},
            "platelets_k_ul": {"value": 88, "ref": "150-400", "flag": "LOW"},
            "sodium_meq_l": {"value": 128, "ref": "136-145", "flag": "LOW"},
            "potassium_meq_l": {"value": 5.4, "ref": "3.5-5.0", "flag": "HIGH"},
            "creatinine_mg_dl": {"value": 2.9, "ref": "0.6-1.1", "flag": "HIGH"},
            "bun_mg_dl": {"value": 52, "ref": "7-20", "flag": "HIGH"},
            "glucose_mg_dl": {"value": 312, "ref": "70-100", "flag": "HIGH"},
            "lactate_mmol_l": {"value": 4.1, "ref": "<2.0", "flag": "HIGH"},
            "procalcitonin_ng_ml": {"value": 18.4, "ref": "<0.5", "flag": "HIGH"},
            "ph_arterial": {"value": 7.26, "ref": "7.35-7.45", "flag": "LOW"},
            "paco2_mmhg": {"value": 28, "ref": "35-45", "flag": "LOW"},
            "hco3_meq_l": {"value": 12, "ref": "22-28", "flag": "LOW"},
            "inr": {"value": 3.8, "ref": "<1.1", "flag": "HIGH"},
            "fibrinogen_mg_dl": {"value": 148, "ref": ">200", "flag": "LOW"},
        },
        "microbiology": {
            "urine_gram_stain": "Gram-negative rods (many)",
            "urine_culture": "Escherichia coli — pan-sensitive (ampicillin intermediate)",
            "blood_culture_1": "No growth at 5 days",
            "blood_culture_2": "No growth at 5 days",
        },
        "medications_on_admission": [
            {"drug": "Warfarin", "dose": "5 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Metformin", "dose": "500 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Furosemide", "dose": "40 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Metoprolol", "dose": "25 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Levothyroxine", "dose": "75 mcg", "route": "PO", "frequency": "QD"},
            {"drug": "Atorvastatin", "dose": "40 mg", "route": "PO", "frequency": "QHS"},
        ],
        "allergies": [
            {"allergen": "Cephalosporins", "reaction": "Anaphylaxis", "severity": "Severe"},
        ],
        "discharge_summary": (
            "Ms. Fitzgerald admitted in septic shock secondary to E. coli urosepsis. Managed in MICU "
            "with norepinephrine (weaned off HD4), levofloxacin + gentamicin (adjusted to levofloxacin "
            "monotherapy after sensitivities). AKI resolved (Cr 1.9 at discharge). Coagulopathy resolved. "
            "Lactate cleared within 12 hours. Warfarin restarted HD6. Discharged to SNF."
        ),
    },
    {
        "encounter_id": "ENC-2025-006113",
        "mrn": "MRN-8473920",
        "encounter_type": "Office Visit — Outpatient",
        "encounter_date": "2025-02-20",
        "department": "Internal Medicine",
        "attending": "Dr. Robert Chen, MD (Internal Medicine)",
        "admitting_diagnosis": "Hypertension follow-up",
        "demographics": {
            "name": "Michael Torres", "dob": "1972-05-08", "age": 52,
            "sex": "Male", "race": "Hispanic / Latino", "language": "English",
            "mrn": "MRN-8473920", "insurance": "UnitedHealthcare Choice Plus",
            "member_id": "UH-2847392-1",
        },
        "diagnoses": [
            {"code": "I10", "description": "Essential hypertension", "type": "Primary"},
            {"code": "E78.5", "description": "Hyperlipidemia, unspecified", "type": "Secondary"},
            {"code": "N40.0", "description": "Benign prostatic hyperplasia, without LUTS", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 138, "bp_diastolic": 86, "heart_rate": 68,
            "respiratory_rate": 16, "temperature_c": 37.0, "spo2_percent": 98,
            "weight_kg": 88.0, "bmi": 27.2,
        },
        "labs": {
            "wbc_k_ul": {"value": 6.4, "ref": "4.5-11.0", "flag": "NORMAL"},
            "hemoglobin_g_dl": {"value": 15.2, "ref": "13.5-17.5", "flag": "NORMAL"},
            "sodium_meq_l": {"value": 140, "ref": "136-145", "flag": "NORMAL"},
            "potassium_meq_l": {"value": 3.7, "ref": "3.5-5.0", "flag": "NORMAL"},
            "creatinine_mg_dl": {"value": 0.9, "ref": "0.7-1.3", "flag": "NORMAL"},
            "egfr_ml_min": {"value": 94, "ref": ">60", "flag": "NORMAL"},
            "glucose_mg_dl": {"value": 94, "ref": "70-100", "flag": "NORMAL"},
            "ldl_mg_dl": {"value": 121, "ref": "<130", "flag": "NORMAL"},
            "hdl_mg_dl": {"value": 52, "ref": ">40", "flag": "NORMAL"},
            "urine_acr_mg_g": {"value": 8, "ref": "<30", "flag": "NORMAL"},
        },
        "medications_current": [
            {"drug": "Amlodipine", "dose": "10 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Hydrochlorothiazide", "dose": "25 mg", "route": "PO", "frequency": "QAM"},
            {"drug": "Atorvastatin", "dose": "20 mg", "route": "PO", "frequency": "QHS"},
            {"drug": "Tamsulosin", "dose": "0.4 mg", "route": "PO", "frequency": "QHS"},
            {"drug": "Aspirin", "dose": "81 mg", "route": "PO", "frequency": "QD"},
        ],
        "allergies": [
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "Mild"},
        ],
        "follow_up": "3 months. Consider adding spironolactone 25mg if BP remains >130/80 after lifestyle changes.",
    },
    # ── Encounters 5-16 ──────────────────────────────────────────────────────
    {
        "encounter_id": "ENC-2025-007442",
        "mrn": "MRN-2938471",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-03-02",
        "discharge_date": "2025-03-08",
        "length_of_stay_days": 6,
        "department": "Pulmonary Medicine / Step-Down Unit",
        "attending": "Dr. Nathan Brooks, MD (Pulmonology)",
        "admitting_diagnosis": "Acute Exacerbation of COPD — Influenza-triggered",
        "demographics": {
            "name": "Harold Dixon", "dob": "1957-02-14", "age": 68,
            "sex": "Male", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-2938471", "insurance": "Medicare Part B",
            "member_id": "MC-2938471-1",
        },
        "diagnoses": [
            {"code": "J44.1", "description": "Acute exacerbation of COPD", "type": "Primary"},
            {"code": "J10.1", "description": "Influenza A with pneumonia", "type": "Secondary"},
            {"code": "J96.01", "description": "Acute-on-chronic hypercapnic respiratory failure", "type": "Secondary"},
            {"code": "I27.0", "description": "Primary pulmonary hypertension", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 142, "bp_diastolic": 88, "heart_rate": 102,
            "respiratory_rate": 26, "temperature_c": 37.4, "spo2_percent": 88,
            "weight_kg": 78.0, "bmi": 27.1,
        },
        "labs": {
            "wbc_k_ul": {"value": 13.8, "ref": "4.5-11.0", "flag": "HIGH"},
            "hemoglobin_g_dl": {"value": 16.2, "ref": "13.5-17.5", "flag": "HIGH"},
            "ph_arterial": {"value": 7.32, "ref": "7.35-7.45", "flag": "LOW"},
            "paco2_mmhg": {"value": 64, "ref": "35-45", "flag": "HIGH"},
            "hco3_meq_l": {"value": 32, "ref": "22-28", "flag": "HIGH"},
            "pao2_mmhg": {"value": 54, "ref": "75-100", "flag": "LOW"},
            "procalcitonin_ng_ml": {"value": 0.18, "ref": "<0.5", "flag": "NORMAL"},
            "crp_mg_l": {"value": 68, "ref": "<5", "flag": "HIGH"},
            "bnp_pg_ml": {"value": 280, "ref": "<100", "flag": "HIGH"},
        },
        "medications_on_admission": [
            {"drug": "Tiotropium", "dose": "18 mcg", "route": "Inh", "frequency": "QD"},
            {"drug": "Salmeterol/Fluticasone", "dose": "50/500 mcg", "route": "Inh", "frequency": "BID"},
            {"drug": "Albuterol", "dose": "2.5 mg", "route": "Neb", "frequency": "PRN"},
            {"drug": "Metformin", "dose": "500 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Lisinopril", "dose": "10 mg", "route": "PO", "frequency": "QD"},
        ],
        "medications_at_discharge": [
            {"drug": "Tiotropium", "dose": "18 mcg", "route": "Inh", "frequency": "QD"},
            {"drug": "Salmeterol/Fluticasone", "dose": "50/500 mcg", "route": "Inh", "frequency": "BID"},
            {"drug": "Albuterol", "dose": "2.5 mg", "route": "Neb", "frequency": "PRN"},
            {"drug": "Prednisone", "dose": "30 mg", "route": "PO", "frequency": "QD", "indication": "5-day taper post-exacerbation"},
            {"drug": "Oseltamivir", "dose": "75 mg", "route": "PO", "frequency": "BID", "indication": "Complete 5-day course"},
            {"drug": "Lisinopril", "dose": "10 mg", "route": "PO", "frequency": "QD"},
        ],
        "allergies": [
            {"allergen": "Penicillin", "reaction": "GI intolerance", "severity": "Mild"},
        ],
        "discharge_summary": (
            "Mr. Dixon admitted with AECOPD triggered by Influenza A. BiPAP initiated on admission "
            "(IPAP 14/EPAP 6) — pH corrected to 7.38 by day 2. Oseltamivir 75mg BID x5d. "
            "Azithromycin 5d. Methylprednisolone → prednisone taper. SpO2 92% on 2L at discharge. "
            "Follow-up pulmonology 2 weeks. Influenza vaccine to be administered at follow-up."
        ),
    },
    {
        "encounter_id": "ENC-2025-008563",
        "mrn": "MRN-4738291",
        "encounter_type": "Inpatient Hospitalization — Stroke Unit",
        "encounter_date": "2025-05-08",
        "discharge_date": "2025-05-14",
        "length_of_stay_days": 6,
        "department": "Neurology / Stroke Unit",
        "attending": "Dr. Helen Voss, MD (Neurology — Stroke)",
        "admitting_diagnosis": "Acute Ischaemic Stroke — Right MCA",
        "demographics": {
            "name": "Theodore Kapoor", "dob": "1954-08-27", "age": 70,
            "sex": "Male", "race": "South Asian", "language": "English",
            "mrn": "MRN-4738291", "insurance": "BlueCross PPO",
            "member_id": "BC-4738291-1",
        },
        "diagnoses": [
            {"code": "I63.9", "description": "Acute ischaemic stroke, unspecified", "type": "Primary"},
            {"code": "I48.91", "description": "Unspecified atrial fibrillation (source)", "type": "Secondary"},
            {"code": "I10", "description": "Essential hypertension", "type": "Secondary"},
            {"code": "E11.9", "description": "Type 2 diabetes mellitus", "type": "Secondary"},
        ],
        "procedures": [
            {"code": "37215", "description": "IV thrombolysis — alteplase 0.9 mg/kg"},
            {"code": "61645", "description": "Mechanical thrombectomy — right MCA M1"},
        ],
        "vital_signs": {
            "bp_systolic": 188, "bp_diastolic": 102, "heart_rate": 82,
            "respiratory_rate": 18, "temperature_c": 37.0, "spo2_percent": 96,
            "weight_kg": 84.0, "bmi": 28.6,
        },
        "labs": {
            "wbc_k_ul": {"value": 9.2, "ref": "4.5-11.0", "flag": "NORMAL"},
            "hemoglobin_g_dl": {"value": 14.8, "ref": "13.5-17.5", "flag": "NORMAL"},
            "glucose_mg_dl": {"value": 162, "ref": "70-100", "flag": "HIGH"},
            "sodium_meq_l": {"value": 141, "ref": "136-145", "flag": "NORMAL"},
            "creatinine_mg_dl": {"value": 1.0, "ref": "0.7-1.3", "flag": "NORMAL"},
            "inr": {"value": 1.0, "ref": "<1.1", "flag": "NORMAL"},
            "ldl_mg_dl": {"value": 148, "ref": "<70 (stroke goal)", "flag": "HIGH"},
        },
        "medications_at_discharge": [
            {"drug": "Apixaban", "dose": "5 mg", "route": "PO", "frequency": "BID", "indication": "AF stroke prevention"},
            {"drug": "Atorvastatin", "dose": "80 mg", "route": "PO", "frequency": "QHS", "indication": "High-intensity post-stroke"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Metformin", "dose": "500 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Metoprolol", "dose": "25 mg", "route": "PO", "frequency": "BID"},
        ],
        "allergies": [
            {"allergen": "Codeine", "reaction": "Nausea and vomiting", "severity": "Mild"},
        ],
        "discharge_summary": (
            "Mr. Kapoor admitted with right MCA stroke (M1 occlusion). IV tPA given at 47 min "
            "door-to-needle. Mechanical thrombectomy with successful recanalization (TICI 2b). "
            "NIHSS improved 12→4 at discharge. Apixaban started 48h post-tPA. Atorvastatin 80mg. "
            "Discharge NIHSS 4 — mild residual left arm weakness. Cardiac rehab + stroke rehab."
        ),
    },
    {
        "encounter_id": "ENC-2025-009284",
        "mrn": "MRN-5192837",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-06-01",
        "discharge_date": "2025-06-05",
        "length_of_stay_days": 4,
        "department": "General Medicine / Nephrology Consult",
        "attending": "Dr. Ahmed Qureshi, MD (Internal Medicine)",
        "admitting_diagnosis": "Contrast-Induced AKI",
        "demographics": {
            "name": "Harold Chen", "dob": "1966-03-18", "age": 59,
            "sex": "Male", "race": "Chinese-American", "language": "English",
            "mrn": "MRN-5192837", "insurance": "UnitedHealthcare Select",
            "member_id": "UH-5192837-1",
        },
        "diagnoses": [
            {"code": "N17.9", "description": "Acute kidney injury", "type": "Primary"},
            {"code": "N18.3", "description": "Chronic kidney disease, stage 3a (baseline)", "type": "Secondary"},
            {"code": "I50.20", "description": "HFrEF, EF 40%", "type": "Secondary"},
            {"code": "E11.9", "description": "Type 2 diabetes", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 152, "bp_diastolic": 88, "heart_rate": 76,
            "respiratory_rate": 16, "temperature_c": 36.9, "spo2_percent": 97,
            "weight_kg": 86.0, "bmi": 28.2,
        },
        "labs": {
            "creatinine_mg_dl": {"value": 2.6, "ref": "0.7-1.3 (baseline 1.4)", "flag": "HIGH"},
            "egfr_ml_min": {"value": 27, "ref": ">60", "flag": "LOW"},
            "bun_mg_dl": {"value": 44, "ref": "7-20", "flag": "HIGH"},
            "potassium_meq_l": {"value": 5.2, "ref": "3.5-5.0", "flag": "HIGH"},
            "hco3_meq_l": {"value": 18, "ref": "22-28", "flag": "LOW"},
            "fena_percent": {"value": 2.1, "ref": "<1% (prerenal)", "flag": "HIGH"},
            "bnp_pg_ml": {"value": 480, "ref": "<100", "flag": "HIGH"},
        },
        "medications_current": [
            {"drug": "Aspirin", "dose": "81 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Atorvastatin", "dose": "80 mg", "route": "PO", "frequency": "QHS"},
            {"drug": "Metoprolol", "dose": "50 mg", "route": "PO", "frequency": "BID"},
        ],
        "allergies": [
            {"allergen": "Cephalosporins", "reaction": "Rash", "severity": "Mild"},
        ],
        "discharge_summary": (
            "Cr improved from 2.6 peak to 1.6 at discharge (approaching baseline 1.4). "
            "Hyperkalaemia resolved with dietary restriction + Kayexalate. "
            "Lisinopril held — reintroduce at PCP follow-up if Cr <1.6. "
            "Metformin and NSAIDs permanently discontinued. Nephrology follow-up 2 weeks."
        ),
    },
    {
        "encounter_id": "ENC-2025-010391",
        "mrn": "MRN-6384920",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-02-14",
        "discharge_date": "2025-02-20",
        "length_of_stay_days": 6,
        "department": "General Medicine",
        "attending": "Dr. Yuki Tanaka, MD (Internal Medicine)",
        "admitting_diagnosis": "Community-Acquired Pneumonia — LLL, S. pneumoniae",
        "demographics": {
            "name": "Dorothy Walsh", "dob": "1948-05-12", "age": 77,
            "sex": "Female", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-6384920", "insurance": "Medicare Advantage",
            "member_id": "MA-6384920-2",
        },
        "diagnoses": [
            {"code": "J18.9", "description": "Community-acquired pneumonia, unspecified", "type": "Primary"},
            {"code": "I50.20", "description": "Unspecified systolic heart failure", "type": "Secondary"},
            {"code": "E87.1", "description": "Hyponatraemia (SIADH secondary to pneumonia)", "type": "Secondary"},
            {"code": "N17.9", "description": "Acute kidney injury (mild, prerenal)", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 136, "bp_diastolic": 82, "heart_rate": 98,
            "respiratory_rate": 24, "temperature_c": 38.8, "spo2_percent": 91,
            "weight_kg": 68.0, "bmi": 24.2,
        },
        "labs": {
            "wbc_k_ul": {"value": 18.6, "ref": "4.5-11.0", "flag": "HIGH"},
            "hemoglobin_g_dl": {"value": 11.8, "ref": "12.0-15.5", "flag": "LOW"},
            "sodium_meq_l": {"value": 132, "ref": "136-145", "flag": "LOW"},
            "creatinine_mg_dl": {"value": 1.4, "ref": "0.6-1.1 (baseline 1.1)", "flag": "HIGH"},
            "procalcitonin_ng_ml": {"value": 1.8, "ref": "<0.5", "flag": "HIGH"},
            "crp_mg_l": {"value": 198, "ref": "<5", "flag": "HIGH"},
            "bnp_pg_ml": {"value": 320, "ref": "<100", "flag": "HIGH"},
        },
        "medications_at_discharge": [
            {"drug": "Levofloxacin", "dose": "750 mg", "route": "PO", "frequency": "QD", "indication": "Complete 5d CAP course"},
            {"drug": "Furosemide", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Carvedilol", "dose": "12.5 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Atorvastatin", "dose": "40 mg", "route": "PO", "frequency": "QHS"},
            {"drug": "Levothyroxine", "dose": "75 mcg", "route": "PO", "frequency": "QD"},
        ],
        "allergies": [
            {"allergen": "Penicillin", "reaction": "Anaphylaxis", "severity": "Severe"},
        ],
        "discharge_summary": (
            "Mrs. Walsh admitted with LLL CAP, Streptococcus pneumoniae (urine Ag positive). "
            "Levofloxacin IV 750mg QD (penicillin allergy). Improvement by day 3. "
            "Na 132→137 with fluid restriction (SIADH resolved). Cr 1.4→1.1. "
            "SpO2 94% on RA at discharge. CXR improved at discharge."
        ),
    },
    {
        "encounter_id": "ENC-2025-011482",
        "mrn": "MRN-8374020",
        "encounter_type": "Emergency Department",
        "encounter_date": "2025-06-14",
        "department": "Emergency Department",
        "attending": "Dr. Jordan Lee, MD (Emergency Medicine)",
        "admitting_diagnosis": "Anaphylaxis — penicillin",
        "demographics": {
            "name": "Dylan Reed", "dob": "1990-04-22", "age": 35,
            "sex": "Male", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-8374020", "insurance": "Cigna PPO",
            "member_id": "CI-8374020-1",
        },
        "diagnoses": [
            {"code": "T78.2XXA", "description": "Anaphylaxis — penicillin-induced", "type": "Primary"},
        ],
        "vital_signs": {
            "bp_systolic": 84, "bp_diastolic": 52, "heart_rate": 118,
            "respiratory_rate": 24, "temperature_c": 37.3, "spo2_percent": 91,
            "weight_kg": 78.0, "bmi": 24.1,
        },
        "labs": {
            "tryptase_ug_l": {"value": 42, "ref": "<11.4", "flag": "HIGH"},
            "wbc_k_ul": {"value": 10.2, "ref": "4.5-11.0", "flag": "NORMAL"},
            "glucose_mg_dl": {"value": 118, "ref": "70-100", "flag": "HIGH"},
        },
        "medications_at_discharge": [
            {"drug": "EpiPen 0.3mg", "dose": "0.3 mg", "route": "IM", "frequency": "PRN anaphylaxis", "indication": "Self-administration — 2 devices"},
            {"drug": "Diphenhydramine", "dose": "25 mg", "route": "PO", "frequency": "PRN urticaria"},
            {"drug": "Prednisone", "dose": "40 mg", "route": "PO", "frequency": "QD x3d", "indication": "Biphasic reaction prevention"},
        ],
        "allergies": [
            {"allergen": "Penicillin", "reaction": "Anaphylaxis (IgE-mediated — systemic)", "severity": "Severe"},
        ],
        "follow_up": "Immunology/Allergy clinic in 4 weeks. Anaphylaxis action plan provided.",
    },
    {
        "encounter_id": "ENC-2025-012573",
        "mrn": "MRN-3847292",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-07-10",
        "discharge_date": "2025-07-14",
        "length_of_stay_days": 4,
        "department": "Cardiology",
        "attending": "Dr. Kevin Park, MD (Cardiology)",
        "admitting_diagnosis": "New-Onset AF with RVR — thyrotoxicosis",
        "demographics": {
            "name": "Patricia Huang", "dob": "1959-01-15", "age": 66,
            "sex": "Female", "race": "Chinese-American", "language": "English",
            "mrn": "MRN-3847292", "insurance": "Medicare + Supplement",
            "member_id": "MC-3847292-1",
        },
        "diagnoses": [
            {"code": "I48.0", "description": "Paroxysmal atrial fibrillation", "type": "Primary"},
            {"code": "E05.90", "description": "Thyrotoxicosis, unspecified", "type": "Secondary"},
            {"code": "I10", "description": "Hypertension", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 128, "bp_diastolic": 82, "heart_rate": 148,
            "respiratory_rate": 20, "temperature_c": 37.1, "spo2_percent": 96,
            "weight_kg": 62.0, "bmi": 26.4,
        },
        "labs": {
            "tsh_miu_l": {"value": 0.08, "ref": "0.4-4.0", "flag": "LOW"},
            "free_t4_ng_dl": {"value": 2.6, "ref": "0.8-1.8", "flag": "HIGH"},
            "magnesium_meq_l": {"value": 1.8, "ref": "1.7-2.2", "flag": "LOW-NORMAL"},
            "potassium_meq_l": {"value": 3.6, "ref": "3.5-5.0", "flag": "NORMAL"},
            "troponin_ng_ml": {"value": 0.01, "ref": "<0.04", "flag": "NORMAL"},
            "bnp_pg_ml": {"value": 188, "ref": "<100", "flag": "HIGH"},
        },
        "medications_at_discharge": [
            {"drug": "Diltiazem ER", "dose": "120 mg", "route": "PO", "frequency": "QD", "indication": "Rate control"},
            {"drug": "Apixaban", "dose": "5 mg", "route": "PO", "frequency": "BID", "indication": "Stroke prevention — CHA2DS2-VASc 2"},
            {"drug": "Methimazole", "dose": "10 mg", "route": "PO", "frequency": "TID", "indication": "Thyrotoxicosis treatment"},
            {"drug": "Lisinopril", "dose": "10 mg", "route": "PO", "frequency": "QD"},
        ],
        "allergies": [
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "Mild"},
        ],
        "discharge_summary": (
            "Rate controlled with IV diltiazem (HR 82 at discharge). Thyrotoxicosis confirmed — "
            "started methimazole. Anticoagulated (apixaban). AF rhythm cardioversion planned "
            "after 3-week anticoagulation. Endocrinology follow-up 1 week."
        ),
    },
    {
        "encounter_id": "ENC-2025-013684",
        "mrn": "MRN-7384920",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-09-14",
        "discharge_date": "2025-09-19",
        "length_of_stay_days": 5,
        "department": "Gastroenterology",
        "attending": "Dr. Daniela Torres, MD (Gastroenterology)",
        "admitting_diagnosis": "Acute Alcoholic Pancreatitis",
        "demographics": {
            "name": "Frank Matthews", "dob": "1981-07-09", "age": 44,
            "sex": "Male", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-7384920", "insurance": "Cigna HMO",
            "member_id": "CI-7384920-1",
        },
        "diagnoses": [
            {"code": "K85.1", "description": "Alcoholic acute pancreatitis", "type": "Primary"},
            {"code": "F10.20", "description": "Alcohol use disorder, severe", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 118, "bp_diastolic": 76, "heart_rate": 106,
            "respiratory_rate": 18, "temperature_c": 38.1, "spo2_percent": 97,
            "weight_kg": 84.0, "bmi": 27.4,
        },
        "labs": {
            "lipase_u_l": {"value": 1840, "ref": "<60", "flag": "HIGH"},
            "amylase_u_l": {"value": 620, "ref": "<100", "flag": "HIGH"},
            "wbc_k_ul": {"value": 15.2, "ref": "4.5-11.0", "flag": "HIGH"},
            "crp_mg_l": {"value": 182, "ref": "<5", "flag": "HIGH"},
            "glucose_mg_dl": {"value": 188, "ref": "70-100", "flag": "HIGH"},
            "calcium_mg_dl": {"value": 8.6, "ref": "8.5-10.5", "flag": "NORMAL"},
            "triglycerides_mg_dl": {"value": 284, "ref": "<150", "flag": "HIGH"},
        },
        "medications_at_discharge": [
            {"drug": "Pantoprazole", "dose": "40 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Thiamine", "dose": "100 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Multivitamin", "dose": "1 tablet", "route": "PO", "frequency": "QD"},
        ],
        "allergies": [
            {"allergen": "Sulfa drugs", "reaction": "Stevens-Johnson syndrome", "severity": "Severe"},
        ],
        "discharge_summary": (
            "Admitted with moderate acute alcoholic pancreatitis (Balthazar C, Ranson 3). "
            "CT: oedematous pancreas, no necrosis. Managed with aggressive IVF, analgesia, "
            "NPO x2d → liquid diet day 3. Lipase trending down. Alcohol cessation counselling. "
            "AA referral made. Follow-up GI in 4 weeks."
        ),
    },
    {
        "encounter_id": "ENC-2025-014795",
        "mrn": "MRN-2847391",
        "encounter_type": "Emergency Department",
        "encounter_date": "2025-10-19",
        "discharge_date": "2025-10-23",
        "length_of_stay_days": 4,
        "department": "Endocrinology / ICU",
        "attending": "Dr. Samuel Wright, MD (Endocrinology)",
        "admitting_diagnosis": "Diabetic Ketoacidosis — Severe",
        "demographics": {
            "name": "Ashley Park", "dob": "2001-06-28", "age": 24,
            "sex": "Female", "race": "Korean-American", "language": "English",
            "mrn": "MRN-2847391", "insurance": "Parent's employer insurance",
            "member_id": "EI-2847391-1",
        },
        "diagnoses": [
            {"code": "E11.10", "description": "Type 1 DM with DKA", "type": "Primary"},
            {"code": "E87.2", "description": "Acidosis — metabolic", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 96, "bp_diastolic": 64, "heart_rate": 118,
            "respiratory_rate": 28, "temperature_c": 37.4, "spo2_percent": 98,
            "weight_kg": 58.0, "bmi": 21.4,
        },
        "labs": {
            "glucose_mg_dl": {"value": 482, "ref": "70-100", "flag": "HIGH"},
            "ph_arterial": {"value": 7.12, "ref": "7.35-7.45", "flag": "LOW"},
            "hco3_meq_l": {"value": 6, "ref": "22-28", "flag": "LOW"},
            "anion_gap_meq_l": {"value": 32, "ref": "8-12", "flag": "HIGH"},
            "potassium_meq_l": {"value": 5.8, "ref": "3.5-5.0", "flag": "HIGH"},
            "serum_ketones_mmol_l": {"value": 5.4, "ref": "<0.6", "flag": "HIGH"},
            "hba1c_percent": {"value": 11.8, "ref": "<7.0", "flag": "HIGH"},
        },
        "medications_at_discharge": [
            {"drug": "Insulin pump (resumed)", "dose": "0.6 units/kg/day", "route": "SC", "frequency": "Continuous", "indication": "T1DM management"},
            {"drug": "Oral potassium supplement", "dose": "40 mEq", "route": "PO", "frequency": "BID x3d"},
        ],
        "allergies": [
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "Mild"},
        ],
        "discharge_summary": (
            "DKA resolved: AG closed at 12h, pH 7.38 at 18h. Glucose 164 at discharge. "
            "Insulin drip transitioned to pump after anion gap closed. "
            "Diabetes pump educator reviewed pump settings. Follow-up endocrinology 1 week."
        ),
    },
    {
        "encounter_id": "ENC-2025-015906",
        "mrn": "MRN-3847203",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-08-03",
        "discharge_date": "2025-08-07",
        "length_of_stay_days": 4,
        "department": "Gastroenterology / ICU",
        "attending": "Dr. Priya Nair, MD (Gastroenterology)",
        "admitting_diagnosis": "Upper GI Bleed — Duodenal Ulcer",
        "demographics": {
            "name": "Victor Sullivan", "dob": "1967-11-22", "age": 58,
            "sex": "Male", "race": "Irish-American", "language": "English",
            "mrn": "MRN-3847203", "insurance": "Aetna PPO",
            "member_id": "AE-3847203-1",
        },
        "diagnoses": [
            {"code": "K27.4", "description": "Peptic ulcer with haemorrhage", "type": "Primary"},
            {"code": "K92.1", "description": "Melaena", "type": "Secondary"},
            {"code": "F10.20", "description": "Alcohol use disorder, severe", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 92, "bp_diastolic": 58, "heart_rate": 118,
            "respiratory_rate": 20, "temperature_c": 37.2, "spo2_percent": 98,
            "weight_kg": 82.0, "bmi": 26.8,
        },
        "labs": {
            "hemoglobin_g_dl": {"value": 7.4, "ref": "13.5-17.5", "flag": "LOW"},
            "bun_mg_dl": {"value": 44, "ref": "7-20", "flag": "HIGH"},
            "creatinine_mg_dl": {"value": 0.9, "ref": "0.7-1.3", "flag": "NORMAL"},
            "bun_cr_ratio": {"value": 48.9, "ref": "<20 (UGIB pattern)", "flag": "HIGH"},
            "inr": {"value": 1.4, "ref": "<1.1", "flag": "HIGH"},
            "albumin_g_dl": {"value": 3.6, "ref": "3.5-5.0", "flag": "NORMAL"},
        },
        "medications_at_discharge": [
            {"drug": "Pantoprazole", "dose": "40 mg", "route": "PO", "frequency": "BID x8 weeks", "indication": "Peptic ulcer healing"},
            {"drug": "Amoxicillin/Clarithromycin", "dose": "1g/500mg", "route": "PO", "frequency": "BID x14d", "indication": "H. pylori eradication"},
        ],
        "allergies": [
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "Mild"},
        ],
        "discharge_summary": (
            "EGD: Large posterior duodenal ulcer with visible vessel — endoscopic clipping performed. "
            "Transfused 2u pRBC (Hgb 7.4 → 10.2). PPI 80mg bolus → 8mg/hr x72h → PO switch. "
            "H. pylori CLO test positive — triple therapy prescribed. NSAIDs permanently stopped. "
            "Alcohol cessation counselling. Follow-up GI 4 weeks for repeat scope."
        ),
    },
    {
        "encounter_id": "ENC-2025-016017",
        "mrn": "MRN-6238470",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-12-08",
        "discharge_date": "2025-12-18",
        "length_of_stay_days": 10,
        "department": "Medical Intensive Care Unit (MICU) / Neurology",
        "attending": "Dr. Fatima Hassan, MD (Infectious Disease / Neurology co-management)",
        "admitting_diagnosis": "Bacterial Meningitis — N. meningitidis",
        "demographics": {
            "name": "Tyler Nguyen", "dob": "1997-09-14", "age": 28,
            "sex": "Male", "race": "Vietnamese-American", "language": "English",
            "mrn": "MRN-6238470", "insurance": "Employer PPO",
            "member_id": "EP-6238470-1",
        },
        "diagnoses": [
            {"code": "G00.9", "description": "Bacterial meningitis — Neisseria meningitidis Group B", "type": "Primary"},
            {"code": "A39.4", "description": "Meningococcaemia", "type": "Secondary"},
            {"code": "D65", "description": "Disseminated intravascular coagulation", "type": "Secondary"},
            {"code": "E87.1", "description": "SIADH — secondary to meningitis", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 118, "bp_diastolic": 72, "heart_rate": 112,
            "respiratory_rate": 20, "temperature_c": 40.1, "spo2_percent": 99,
            "weight_kg": 74.0, "bmi": 22.8,
        },
        "labs": {
            "wbc_k_ul": {"value": 24.6, "ref": "4.5-11.0", "flag": "HIGH"},
            "platelets_k_ul": {"value": 88, "ref": "150-400", "flag": "LOW"},
            "procalcitonin_ng_ml": {"value": 22.4, "ref": "<0.5", "flag": "HIGH"},
            "sodium_meq_l": {"value": 131, "ref": "136-145", "flag": "LOW"},
            "inr": {"value": 2.4, "ref": "<1.1", "flag": "HIGH"},
            "csf_wbc_per_ul": {"value": 8200, "ref": "<5", "flag": "HIGH"},
            "csf_glucose_mg_dl": {"value": 22, "ref": ">60% of serum", "flag": "LOW"},
        },
        "microbiology": {
            "csf_gram_stain": "Gram-negative diplococci",
            "csf_culture": "Neisseria meningitidis Group B — ceftriaxone sensitive",
            "blood_culture_1": "N. meningitidis Group B",
            "nasopharyngeal_swab": "N. meningitidis Group B carrier state",
        },
        "medications_at_discharge": [
            {"drug": "Ceftriaxone", "dose": "2 g", "route": "IV", "frequency": "Q12h x14d total", "indication": "Meningococcal meningitis"},
            {"drug": "Dexamethasone (completed)", "dose": "0.15 mg/kg", "route": "IV", "frequency": "Q6h x4d — completed"},
        ],
        "allergies": [
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "Mild"},
        ],
        "discharge_summary": (
            "CSF confirmed N. meningitidis Group B. Ceftriaxone x14d. Dexamethasone x4d. "
            "DIC resolved with supportive care. Na normalised day 5 (SIADH). "
            "Residual: mild bilateral hearing loss — audiology referral. "
            "Public health notified. Close contacts given rifampicin prophylaxis."
        ),
    },
    {
        "encounter_id": "ENC-2025-017128",
        "mrn": "MRN-5839201",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-04-22",
        "discharge_date": "2025-04-26",
        "length_of_stay_days": 4,
        "department": "Cardiology / Pulmonary",
        "attending": "Dr. Anika Sharma, MD (Cardiology)",
        "admitting_diagnosis": "Submassive Pulmonary Embolism",
        "demographics": {
            "name": "Claire Thompson", "dob": "1987-02-14", "age": 38,
            "sex": "Female", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-5839201", "insurance": "Cigna Select",
            "member_id": "CI-5839201-1",
        },
        "diagnoses": [
            {"code": "I26.09", "description": "Pulmonary embolism without acute cor pulmonale", "type": "Primary"},
            {"code": "I82.4B1", "description": "Acute DVT right popliteal vein", "type": "Secondary"},
            {"code": "Z79.3", "description": "Long-term use of oral contraceptives", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 108, "bp_diastolic": 72, "heart_rate": 108,
            "respiratory_rate": 24, "temperature_c": 37.3, "spo2_percent": 93,
            "weight_kg": 64.0, "bmi": 23.8,
        },
        "labs": {
            "d_dimer_ug_ml": {"value": 4.8, "ref": "<0.5", "flag": "HIGH"},
            "troponin_i_ng_ml": {"value": 0.08, "ref": "<0.04", "flag": "HIGH"},
            "pro_bnp_pg_ml": {"value": 620, "ref": "<125", "flag": "HIGH"},
            "inr": {"value": 1.0, "ref": "<1.1", "flag": "NORMAL"},
            "creatinine_mg_dl": {"value": 0.7, "ref": "0.5-1.1", "flag": "NORMAL"},
            "ph_arterial": {"value": 7.48, "ref": "7.35-7.45", "flag": "HIGH"},
            "paco2_mmhg": {"value": 28, "ref": "35-45", "flag": "LOW"},
        },
        "medications_at_discharge": [
            {"drug": "Rivaroxaban", "dose": "15 mg", "route": "PO", "frequency": "BID x21d then 20mg QD", "indication": "PE/DVT treatment"},
        ],
        "allergies": [
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "Mild"},
        ],
        "discharge_summary": (
            "Bilateral PE with DVT confirmed on CTPA + Doppler US. RV:LV ratio 1.2 (intermediate-risk). "
            "Anticoagulated with enoxaparin bridge → rivaroxaban. SpO2 97% on RA at discharge. "
            "OCP stopped permanently. Haematology referral for thrombophilia screen at 3 months."
        ),
    },
    {
        "encounter_id": "ENC-2025-018239",
        "mrn": "MRN-7483920",
        "encounter_type": "Inpatient Hospitalization",
        "encounter_date": "2025-08-18",
        "discharge_date": "2025-08-23",
        "length_of_stay_days": 5,
        "department": "Hepatology / Transplant Surgery — ICU",
        "attending": "Dr. Ronald Kim, MD (Hepatology)",
        "admitting_diagnosis": "Acute Liver Failure — Acetaminophen overdose",
        "demographics": {
            "name": "Emma Crawford", "dob": "1994-03-05", "age": 31,
            "sex": "Female", "race": "White / Non-Hispanic", "language": "English",
            "mrn": "MRN-7483920", "insurance": "State Medicaid",
            "member_id": "MD-7483920-1",
        },
        "diagnoses": [
            {"code": "K72.00", "description": "Acute liver failure — drug-induced (acetaminophen)", "type": "Primary"},
            {"code": "T39.1X1A", "description": "Poisoning by acetaminophen, intentional self-harm", "type": "Secondary"},
            {"code": "N17.9", "description": "Acute kidney injury", "type": "Secondary"},
            {"code": "G92.9", "description": "Hepatic encephalopathy, grade 3", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 102, "bp_diastolic": 64, "heart_rate": 108,
            "respiratory_rate": 18, "temperature_c": 37.8, "spo2_percent": 95,
            "weight_kg": 62.0, "bmi": 22.1,
        },
        "labs": {
            "alt_u_l": {"value": 8240, "ref": "7-56", "flag": "HIGH"},
            "ast_u_l": {"value": 12600, "ref": "10-40", "flag": "HIGH"},
            "total_bilirubin_mg_dl": {"value": 14.2, "ref": "0.1-1.2", "flag": "HIGH"},
            "inr": {"value": 6.8, "ref": "<1.1", "flag": "HIGH"},
            "creatinine_mg_dl": {"value": 2.4, "ref": "0.5-1.1", "flag": "HIGH"},
            "ammonia_umol_l": {"value": 188, "ref": "<47", "flag": "HIGH"},
            "lactate_mmol_l": {"value": 4.8, "ref": "<2.0", "flag": "HIGH"},
        },
        "medications_at_discharge": [
            {"drug": "Rifaximin", "dose": "550 mg", "route": "PO", "frequency": "BID", "indication": "Hepatic encephalopathy prevention"},
            {"drug": "Lactulose", "dose": "30 g", "route": "PO", "frequency": "TID"},
            {"drug": "Prophylactic fluconazole", "dose": "200 mg", "route": "PO", "frequency": "QD"},
        ],
        "allergies": [
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "Mild"},
        ],
        "discharge_summary": (
            "Acetaminophen-induced ALF. N-acetylcysteine infusion x72h. INR peaked 7.4 then improved. "
            "Liver transplant evaluation initiated — King's College criteria met. Listed status 1A. "
            "Liver transplant performed day 5. Post-transplant recovering at discharge. "
            "Psychiatry follow-up. Social work support. Acetaminophen permanently contraindicated."
        ),
    },
]


def write_files() -> None:
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, enc in enumerate(_ENCOUNTERS, start=1):
        fname = _OUT_DIR / f"enc_{i:03d}.xml"
        bundle = _build_bundle(enc)
        tree = ET.ElementTree(bundle)
        ET.indent(tree, space="  ")
        with open(fname, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)
        print(f"  wrote {fname.name}  ({enc['encounter_id']})")
    print(f"encounters: {len(_ENCOUNTERS)} FHIR R4 bundles → {_OUT_DIR}")


if __name__ == "__main__":
    write_files()
