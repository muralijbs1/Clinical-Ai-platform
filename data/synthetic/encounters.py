"""
Synthetic EHR patient encounter records.

Data tag: SYNTHETIC
Mirrors real HL7 FHIR-inspired encounter records: demographics, diagnoses
(ICD-10), procedures (CPT), medications (with real drug names/doses), lab
results with reference ranges, allergies, and vital signs.

Usage:
    from data.synthetic.encounters import get_encounters
    docs = get_encounters()   # list[Document]
"""

from schemas import Document, DataTag


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
            "name": "James Patterson",
            "dob": "1961-07-22",
            "age": 63,
            "sex": "Male",
            "race": "White / Non-Hispanic",
            "language": "English",
            "address_city": "Springfield",
            "address_state": "IL",
            "insurance": "Aetna Commercial",
            "member_id": "AC-7382910-1",
            "group": "EMPLOYER-8472",
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
            "bp_systolic": 162, "bp_diastolic": 94,
            "heart_rate": 98, "respiratory_rate": 20,
            "temperature_c": 37.1, "spo2_percent": 95,
            "weight_kg": 91.0, "height_cm": 178.0, "bmi": 28.7,
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
            {"allergen": "Sulfa drugs", "reaction": "Rash (maculopapular)", "severity": "Moderate", "confirmed": True},
        ],
        "discharge_summary": (
            "Mr. Patterson presented with NSTEMI. Cardiac catheterisation on HD2 demonstrated "
            "70% LAD stenosis; drug-eluting stent placed successfully (TIMI III flow achieved). "
            "Troponin peak 892 ng/L, normalised by HD3. EF on echo 48% (preserved). "
            "Discharged HD4 on DAPT, high-intensity statin, beta-blocker. "
            "Follow-up cardiology in 1 week, PCP in 2 weeks, cardiac rehab referral made."
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
            "name": "Linda Nguyen",
            "dob": "1967-09-14",
            "age": 57,
            "sex": "Female",
            "race": "Asian",
            "language": "English",
            "insurance": "Cigna PPO",
            "member_id": "CG-4829310-2",
            "group": "EMPLOYER-3871",
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
            "bp_systolic": 136, "bp_diastolic": 84,
            "heart_rate": 74, "respiratory_rate": 16,
            "temperature_c": 37.0, "spo2_percent": 99,
            "weight_kg": 88.0, "height_cm": 165.0, "bmi": 32.3,
        },
        "labs": {
            "hba1c_percent": {"value": 8.9, "ref": "<7.0", "flag": "HIGH"},
            "fasting_glucose_mg_dl": {"value": 178, "ref": "70-100", "flag": "HIGH"},
            "urine_acr_mg_g": {"value": 68, "ref": "<30", "flag": "HIGH"},
            "wbc_k_ul": {"value": 7.2, "ref": "4.5-11.0", "flag": "NORMAL"},
            "hemoglobin_g_dl": {"value": 12.8, "ref": "12.0-15.5", "flag": "NORMAL"},
            "ferritin_ng_ml": {"value": 18, "ref": "12-150", "flag": "LOW-NORMAL"},
            "sodium_meq_l": {"value": 138, "ref": "136-145", "flag": "NORMAL"},
            "creatinine_mg_dl": {"value": 1.0, "ref": "0.6-1.1", "flag": "NORMAL"},
            "egfr_ml_min": {"value": 68, "ref": ">60", "flag": "NORMAL"},
            "ldl_mg_dl": {"value": 138, "ref": "<70 (DM goal)", "flag": "HIGH"},
            "hdl_mg_dl": {"value": 44, "ref": ">50", "flag": "LOW"},
            "triglycerides_mg_dl": {"value": 176, "ref": "<150", "flag": "HIGH"},
            "tsh_miu_l": {"value": 2.4, "ref": "0.4-4.0", "flag": "NORMAL"},
        },
        "medications_current": [
            {"drug": "Metformin", "dose": "1000 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Amlodipine", "dose": "5 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Atorvastatin", "dose": "40 mg", "route": "PO", "frequency": "QHS"},
            {"drug": "Omeprazole", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Naproxen", "dose": "500 mg", "route": "PO", "frequency": "PRN"},
            {"drug": "Acetaminophen", "dose": "1000 mg", "route": "PO", "frequency": "PRN"},
        ],
        "new_medications_added": [
            {"drug": "Empagliflozin", "dose": "10 mg", "route": "PO", "frequency": "QD", "indication": "DM2 + DKD + renoprotection"},
            {"drug": "Atorvastatin", "dose": "80 mg", "route": "PO", "frequency": "QHS", "indication": "Uptitrated — target LDL <70"},
            {"drug": "Ferrous sulphate", "dose": "325 mg", "route": "PO", "frequency": "QD", "indication": "Iron deficiency"},
        ],
        "allergies": [
            {"allergen": "Penicillin", "reaction": "Rash", "severity": "Mild", "confirmed": True},
            {"allergen": "Shellfish", "reaction": "Urticaria", "severity": "Moderate", "confirmed": True},
        ],
        "follow_up": "3 months — recheck HbA1c, empagliflozin response. Ophthalmology urgent (new dot haemorrhage).",
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
            "name": "Eleanor Fitzgerald",
            "dob": "1950-11-30",
            "age": 74,
            "sex": "Female",
            "race": "White / Non-Hispanic",
            "language": "English",
            "insurance": "Medicare Advantage — Humana",
            "member_id": "HM-3847291-1",
            "group": "MEDICARE",
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
            "bp_systolic": 88, "bp_diastolic": 54,
            "heart_rate": 118, "respiratory_rate": 28,
            "temperature_c": 39.8, "spo2_percent": 90,
            "weight_kg": 61.0, "height_cm": 157.0, "bmi": 24.7,
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
        "medications_at_admission": [
            {"drug": "Warfarin", "dose": "5 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Metformin", "dose": "500 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Furosemide", "dose": "40 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Metoprolol", "dose": "25 mg", "route": "PO", "frequency": "BID"},
            {"drug": "Lisinopril", "dose": "20 mg", "route": "PO", "frequency": "QD"},
            {"drug": "Levothyroxine", "dose": "75 mcg", "route": "PO", "frequency": "QD"},
            {"drug": "Atorvastatin", "dose": "40 mg", "route": "PO", "frequency": "QHS"},
        ],
        "allergies": [
            {"allergen": "Cephalosporins", "reaction": "Anaphylaxis", "severity": "Severe", "confirmed": True},
        ],
        "discharge_summary": (
            "Ms. Fitzgerald was admitted in septic shock secondary to E. coli urosepsis. "
            "Managed in MICU with norepinephrine (weaned off HD4), levofloxacin + gentamicin "
            "(adjusted to levofloxacin monotherapy after sensitivities confirmed E. coli pan-sensitive). "
            "AKI resolved (Cr 1.9 at discharge, near baseline). Coagulopathy resolved. "
            "Lactate cleared within 12 hours. Extubation not required. "
            "Warfarin restarted HD6. Metformin held at discharge (restart with PCP). "
            "Discharged to SNF for continued rehab."
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
            "name": "Michael Torres",
            "dob": "1972-05-08",
            "age": 52,
            "sex": "Male",
            "race": "Hispanic / Latino",
            "language": "English",
            "insurance": "UnitedHealthcare Choice Plus",
            "member_id": "UH-2847392-1",
            "group": "EMPLOYER-7283",
        },
        "diagnoses": [
            {"code": "I10", "description": "Essential hypertension", "type": "Primary"},
            {"code": "E78.5", "description": "Hyperlipidemia, unspecified", "type": "Secondary"},
            {"code": "N40.0", "description": "Benign prostatic hyperplasia, without lower urinary tract symptoms", "type": "Secondary"},
        ],
        "vital_signs": {
            "bp_systolic": 138, "bp_diastolic": 86,
            "heart_rate": 68, "respiratory_rate": 16,
            "temperature_c": 37.0, "spo2_percent": 98,
            "weight_kg": 88.0, "height_cm": 180.0, "bmi": 27.2,
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
            "triglycerides_mg_dl": {"value": 92, "ref": "<150", "flag": "NORMAL"},
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
            {"allergen": "No known drug allergies", "reaction": "N/A", "severity": "N/A", "confirmed": True},
        ],
        "follow_up": "3 months. Consider adding spironolactone if BP remains >130/80 after lifestyle changes.",
    },
]


# ── Serialiser ────────────────────────────────────────────────────────────────

def _encounter_to_text(enc: dict) -> str:
    """Converts a structured encounter record into a readable text representation."""
    lines = [
        f"ENCOUNTER RECORD",
        f"================",
        f"Encounter ID: {enc['encounter_id']}",
        f"MRN: {enc['mrn']}",
        f"Type: {enc['encounter_type']}",
        f"Date: {enc['encounter_date']}",
        f"Department: {enc['department']}",
        f"Attending: {enc['attending']}",
        f"",
        f"PATIENT DEMOGRAPHICS",
        f"Name: {enc['demographics']['name']}",
        f"DOB: {enc['demographics']['dob']}  Age: {enc['demographics']['age']}",
        f"Sex: {enc['demographics']['sex']}  Race: {enc['demographics']['race']}",
        f"Insurance: {enc['demographics']['insurance']}",
        f"Member ID: {enc['demographics']['member_id']}",
        f"",
        f"DIAGNOSES",
    ]
    for dx in enc.get("diagnoses", []):
        lines.append(f"  [{dx['type']}] {dx['code']} — {dx['description']}")

    if enc.get("procedures"):
        lines.append("")
        lines.append("PROCEDURES")
        for px in enc["procedures"]:
            lines.append(f"  CPT {px['code']}: {px['description']}")

    lines += ["", "VITAL SIGNS"]
    vs = enc["vital_signs"]
    lines.append(
        f"  BP {vs['bp_systolic']}/{vs['bp_diastolic']} mmHg | "
        f"HR {vs['heart_rate']} bpm | RR {vs['respiratory_rate']} | "
        f"Temp {vs['temperature_c']}°C | SpO2 {vs['spo2_percent']}% | "
        f"BMI {vs.get('bmi', 'N/A')}"
    )

    lines += ["", "LABORATORY RESULTS"]
    for test, result in enc.get("labs", {}).items():
        flag = f" [{result['flag']}]" if result.get("flag") not in ("NORMAL", None) else ""
        lines.append(f"  {test}: {result['value']} (ref {result['ref']}){flag}")

    if enc.get("microbiology"):
        lines += ["", "MICROBIOLOGY"]
        for k, v in enc["microbiology"].items():
            lines.append(f"  {k.replace('_', ' ').title()}: {v}")

    meds_key = "medications_at_discharge" if "medications_at_discharge" in enc else "medications_current"
    if enc.get(meds_key):
        lines += ["", "MEDICATIONS"]
        for med in enc[meds_key]:
            indication = f" [{med['indication']}]" if "indication" in med else ""
            lines.append(f"  {med['drug']} {med['dose']} {med['route']} {med['frequency']}{indication}")

    lines += ["", "ALLERGIES"]
    for allergy in enc.get("allergies", []):
        lines.append(f"  {allergy['allergen']}: {allergy['reaction']} ({allergy['severity']})")

    if enc.get("discharge_summary"):
        lines += ["", "DISCHARGE SUMMARY", enc["discharge_summary"]]

    if enc.get("follow_up"):
        lines += ["", f"FOLLOW-UP: {enc['follow_up']}"]

    return "\n".join(lines)


# ── Public API ────────────────────────────────────────────────────────────────

def get_encounters() -> list[Document]:
    """
    Returns the synthetic EHR encounter corpus as Document objects.
    Tag: SYNTHETIC — realistic clinical records, no real patients.
    """
    docs = []
    for enc in _ENCOUNTERS:
        docs.append(
            Document(
                id=enc["encounter_id"],
                text=_encounter_to_text(enc),
                metadata={
                    "encounter_id": enc["encounter_id"],
                    "mrn": enc["mrn"],
                    "encounter_type": enc["encounter_type"],
                    "encounter_date": enc["encounter_date"],
                    "primary_diagnosis": enc["diagnoses"][0]["code"] if enc.get("diagnoses") else None,
                    "source_type": "ehr_encounter",
                },
                tag=DataTag.SYNTHETIC,
            )
        )
    return docs
