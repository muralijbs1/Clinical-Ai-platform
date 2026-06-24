#!/usr/bin/env python3
"""
Generator: writes synthetic EHR encounter records as FHIR R4 XML Bundle files.

Run once to produce data files. Re-run to regenerate or add more encounters.
Output: data/synthetic/encounters/enc_001.xml ... enc_004.xml

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
