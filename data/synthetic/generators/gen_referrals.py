#!/usr/bin/env python3
"""
Generator: writes synthetic clinical referral letters as plain .txt files.

Run once to produce data files. Re-run to regenerate or add more referrals.
Output: data/synthetic/referrals/ref_001.txt ... ref_004.txt

Each file has a metadata header (key: value pairs, terminated by ---) followed
by the referral letter text. Mirrors how referrals arrive from referring physicians
or are exported from EHR systems.
"""

from pathlib import Path

_OUT_DIR = Path(__file__).parent.parent / "referrals"

_REFERRALS = [
    {
        "referral_id": "REF-2025-045782",
        "specialty": "Cardiology",
        "urgency": "URGENT",
        "patient_name": "James Patterson",
        "patient_dob": "1961-07-22",
        "patient_sex": "Male",
        "patient_mrn": "MRN-7283940",
        "insurance": "Aetna Commercial",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — CARDIOLOGY
Date: 2025-03-14    Referral ID: REF-2025-045782
Urgency: URGENT — Patient to be seen within 24-48 hours

TO: Cardiology Department, Heart & Vascular Center
FROM: Dr. Michael Chen, MD — Internal Medicine, NPI 1234567890
      Primary Care Associates, Phone: (555) 200-1010, Fax: (555) 200-1011

PATIENT: James Patterson | DOB: 1961-07-22 | Age: 63 | Sex: Male
MRN: MRN-7283940 | Insurance: Aetna Commercial | Member ID: AC-7382910-1

REASON FOR REFERRAL: Chest pain with rising high-sensitivity troponin — rule out NSTEMI;
urgent cardiology evaluation and consideration for cardiac catheterisation.

CLINICAL SUMMARY:
Mr. Patterson is a 63-year-old male with significant cardiac risk factors including hypertension
(on Lisinopril and Amlodipine), hyperlipidemia (on Atorvastatin), and type 2 diabetes (on Metformin).
He is a former smoker with 35 pack-year history, quit 8 years ago. Family history notable for father
with MI at age 59 and brother with CABG at age 62.

Patient presented this evening with 4 hours of substernal, pressure-like chest pain (7/10) radiating
to left jaw and left arm, associated with diaphoresis and dyspnoea. He reports a similar self-limited
20-minute episode 2 weeks ago that he did not seek care for.

Physical examination: BP 162/94, HR 98, RR 20, SpO2 95% on room air. In mild distress.
Cardiac exam: RRR, no murmurs. Lungs clear. No peripheral oedema.

EKG: New T-wave inversions in V2-V4. Biphasic T-waves in V1. No ST-elevation.

Laboratory results today:
- hs-cTnT 0h: 65 ng/L (ref <14) — ELEVATED
- hs-cTnT 1h: 118 ng/L (delta 53 ng/L) — RISING — meets ESC 0/1h rule-in
- BNP: 148 pg/mL (mildly elevated)
- CMP: Cr 1.1, Glu 194, all others normal
- Lipids: LDL 162, HDL 38 (suboptimal control)

Current medications: Lisinopril 20mg QD, Atorvastatin 40mg QHS, Metformin 1000mg BID,
Omeprazole 20mg QD, Aspirin 81mg QD.
Allergies: Sulfa drugs (rash).

ASSESSMENT: Rising hs-cTnT with anterior T-wave changes in a patient with multiple cardiac
risk factors — consistent with NSTEMI. Patient was given aspirin loading, ticagrelor 180mg
loading dose, and started on IV heparin per ACS protocol.

QUESTIONS FOR CARDIOLOGY:
1. Does patient require urgent cardiac catheterisation?
2. What is TIMI/GRACE risk stratification?
3. Confirm appropriateness of ticagrelor vs clopidogrel?
4. Is early invasive strategy (<24h) indicated?

PRIOR AUTHORISATION:
Auth Number: PA-847372 | Insurance: Aetna Commercial
Authorised for: Urgent cardiology consultation and possible cardiac catheterisation

Referring Physician: Dr. Michael Chen, MD
NPI: 1234567890 | Phone: (555) 200-1010 | Fax Results To: (555) 200-1011
""",
    },
    {
        "referral_id": "REF-2025-048291",
        "specialty": "Nephrology",
        "urgency": "SOON",
        "patient_name": "Susan Williams",
        "patient_dob": "1962-07-22",
        "patient_sex": "Female",
        "patient_mrn": "MRN-3927548",
        "insurance": "BlueCross BlueShield",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — NEPHROLOGY
Date: 2025-06-20    Referral ID: REF-2025-048291
Urgency: SOON — Appointment within 2-3 weeks

TO: Nephrology Department, Kidney Disease Center
FROM: Dr. Jennifer Patel, MD — Internal Medicine/Geriatrics, NPI 1029384756
      Comprehensive Care Clinic, Phone: (555) 311-2200, Fax: (555) 311-2201

PATIENT: Susan Williams | DOB: 1962-07-22 | Age: 62 | Sex: Female
MRN: MRN-3927548 | Insurance: BlueCross BlueShield | Member ID: BS-5029847-2

REASON FOR REFERRAL: Chronic kidney disease stage 3b with declining eGFR and significant
proteinuria in the setting of longstanding hypertension and type 2 diabetes.

CLINICAL SUMMARY:
Ms. Williams is a 62-year-old female with 22-year history of hypertension and 14-year history
of type 2 diabetes who presents with progressive CKD. Six months ago: creatinine 1.35, eGFR 51.
Most recent labs this month demonstrate continued deterioration.

Current labs:
- Creatinine: 1.62 mg/dL (was 1.35 six months ago — declining)
- eGFR: 35 mL/min/1.73m² (Stage 3b — was Stage 3a)
- BUN: 28 mg/dL
- 24-hour urine protein: 1.8 g/day (approaching nephrotic range)
- HbA1c: 7.2% (reasonably controlled)
- Potassium: 4.2 | Phosphorus: 3.6 | Calcium: 8.9 (all normal)

Physical examination: BP 132/78 on triple antihypertensive therapy. BMI 28.1.
No peripheral oedema. No uremic changes.

Current medications: Lisinopril 40mg QD (maximum dose), Amlodipine 5mg QD, HCTZ 12.5mg QD,
Atorvastatin 40mg QHS, Metformin 1000mg BID, Glipizide 5mg BID, Levothyroxine 75mcg QD.
Allergies: Penicillin (rash).

ASSESSMENT: Stage 3b CKD with progressive decline and significant proteinuria (1.8g/day).
Primary aetiology: diabetic nephropathy (other causes should be excluded). BP controlled at
132/78 but proteinuria high despite maximum-dose ACEi.

QUESTIONS FOR NEPHROLOGY:
1. Is diabetic nephropathy confirmed or should renal biopsy be considered?
2. Should we add SGLT2 inhibitor for additional nephroprotection?
3. What is the projected trajectory to ESRD?
4. When should dialysis access planning begin?
5. Should we evaluate for pre-emptive transplant candidacy?

PRIOR AUTHORISATION:
Auth Number: PA-928374 | Insurance: BlueCross BlueShield
Authorised for: Nephrology consultation, renal ultrasound, and possible renal biopsy

Referring Physician: Dr. Jennifer Patel, MD
NPI: 1029384756 | Phone: (555) 311-2200 | Fax Results To: (555) 311-2201
""",
    },
    {
        "referral_id": "REF-2025-047382",
        "specialty": "Endocrinology",
        "urgency": "ROUTINE",
        "patient_name": "Robert Martinez",
        "patient_dob": "1978-05-11",
        "patient_sex": "Male",
        "patient_mrn": "MRN-7293847",
        "insurance": "Humana HMO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — ENDOCRINOLOGY
Date: 2025-06-18    Referral ID: REF-2025-047382
Urgency: ROUTINE — Appointment within 4 weeks

TO: Endocrinology Department, Diabetes & Endocrine Center
FROM: Dr. David Thompson, MD — Family Medicine, NPI 8374829014
      Family Care Network, Phone: (555) 400-3300, Fax: (555) 400-3301

PATIENT: Robert Martinez | DOB: 1978-05-11 | Age: 47 | Sex: Male
MRN: MRN-7293847 | Insurance: Humana HMO | Member ID: HM-3847291-2

REASON FOR REFERRAL: Poorly controlled type 2 diabetes mellitus with HbA1c 8.9% despite
maximum doses of oral agents. Significant insulin resistance.

CLINICAL SUMMARY:
Mr. Martinez is a 47-year-old male with 8-year history of type 2 diabetes and progressively
worsening glycaemic control. Currently on triple oral therapy at maximum doses.

Relevant labs this month:
- HbA1c: 8.9% (goal <7%)
- Fasting glucose: 156 mg/dL
- Fasting insulin: 34 mIU/L (ref 2-12) — MARKEDLY ELEVATED
- HOMA-IR: 13.3 (ref <2) — SEVERE insulin resistance
- C-peptide: 3.2 ng/mL (elevated — sufficient endogenous production)
- Creatinine: 0.95, eGFR 91 (normal — SGLT2 inhibitor feasible)
- ALT: 78 U/L (elevated — NAFLD suspected, confirmed on prior ultrasound)
- Triglycerides: 256 mg/dL | LDL: 118 mg/dL | HDL: 38 mg/dL

Physical examination: BP 138/84, HR 76. Weight 242 lbs, Ht 70 inches, BMI 34.7.
No acanthosis nigricans. Central obesity. No neuropathy.

Current medications: Metformin 1000mg BID, Pioglitazone 45mg QD, Linagliptin 5mg QD,
Losartan 100mg QD, Atorvastatin 80mg QHS, Allopurinol 300mg QD, Aspirin 81mg QD.

Comorbidities: HTN, hyperlipidemia, obesity (BMI 34.7), OSA on CPAP, NAFLD, gout.

ASSESSMENT: Poorly controlled T2DM with severe insulin resistance (HOMA-IR 13.3), metabolic
syndrome, NAFLD. Insufficient C-peptide suggests adequate beta-cell reserve — primary issue is
insulin resistance. Candidate for GLP-1 agonist or SGLT2 inhibitor therapy.

QUESTIONS FOR ENDOCRINOLOGY:
1. Is GLP-1 agonist (semaglutide or liraglutide) preferred over insulin initiation?
2. Should we add SGLT2 inhibitor given no cardiovascular events but high risk?
3. How to best address the underlying insulin resistance?
4. What is the goal BMI — does patient qualify for obesity pharmacotherapy?

PRIOR AUTHORISATION:
Auth Number: PA-847291 | Insurance: Humana HMO
Authorised for: Endocrinology consultation and diabetes management optimisation

Referring Physician: Dr. David Thompson, MD
NPI: 8374829014 | Phone: (555) 400-3300 | Fax Results To: (555) 400-3301
""",
    },
    {
        "referral_id": "REF-2025-049182",
        "specialty": "Orthopaedic Surgery",
        "urgency": "SOON",
        "patient_name": "Margaret Davis",
        "patient_dob": "1954-09-30",
        "patient_sex": "Female",
        "patient_mrn": "MRN-8374928",
        "insurance": "UnitedHealthcare Senior Plus",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — ORTHOPAEDIC SURGERY
Date: 2025-06-22    Referral ID: REF-2025-049182
Urgency: SOON — Appointment within 3-4 weeks

TO: Orthopaedic Surgery Department, Orthopaedic Centre of Excellence
FROM: Dr. Elizabeth Rodriguez, MD — Geriatric Medicine, NPI 4738291047
      Senior Health & Wellness, Phone: (555) 520-4400, Fax: (555) 520-4401

PATIENT: Margaret Davis | DOB: 1954-09-30 | Age: 70 | Sex: Female
MRN: MRN-8374928 | Insurance: UnitedHealthcare Senior Plus | Member ID: UH-2847392-1

REASON FOR REFERRAL: Severe bilateral knee osteoarthritis with significant functional impairment,
failed conservative management. Requesting evaluation for total knee arthroplasty.

CLINICAL SUMMARY:
Mrs. Davis is a 70-year-old retired teacher with 15-year history of bilateral knee OA (right worse
than left). Failed conservative management: corticosteroid injections, hyaluronic acid, physiotherapy,
NSAIDs at maximum doses.

Current functional status: Pain 8-9/10 bilateral. Wakes 2-3x/night. Walks only 1-2 blocks with
difficulty. Cannot climb stairs without significant discomfort. Antalgic gait with crutch assistance.

Physical examination: BP 132/78, HR 68, BMI 28.9.
Right knee: Significant effusion, valgus deformity, ROM 0-90° (pain-limited), marked crepitus.
Left knee: Moderate effusion, ROM 0-100°, mild valgus deformity.

Imaging:
- Right knee X-rays: Kellgren-Lawrence Grade 4 (severe) OA — marked medial JSN, osteophytes.
- Left knee X-rays: Kellgren-Lawrence Grade 3 (moderate-to-severe) OA.

Recent labs: HbA1c 6.9%, Cr 0.88, eGFR 78, Hgb 13.2, INR normal (all acceptable for surgery).

Medical comorbidities (well controlled): T2DM (HbA1c 6.9%), HTN (BP 132/78), hyperlipidemia, osteoporosis.
Allergies: Latex (contact urticaria only — NO systemic anaphylaxis). Advise surgical team.
Prior surgery: Right shoulder rotator cuff repair 2015 — successful.

Current medications: Metformin 1000mg QD, Lisinopril 20mg QD, HCTZ 12.5mg QD, Atorvastatin 40mg QHS,
Alendronate 70mg weekly, Calcium carbonate 600mg BID + Vit D, Naproxen 500mg BID, Acetaminophen 1g TID.

ASSESSMENT: Severe bilateral knee OA with significant functional decline and exhausted conservative
management. Medically fit for surgery. Appropriate candidate for total knee arthroplasty evaluation.

QUESTIONS FOR ORTHOPAEDICS:
1. Candidate for bilateral TKA? Staged vs simultaneous?
2. Planned timeline for scheduling?
3. What pre-operative clearance required?
4. Peri-operative management of alendronate and NSAIDs?
5. Expected functional outcome and rehabilitation timeline?

PRIOR AUTHORISATION:
Auth Number: PA-938482 | Insurance: UnitedHealthcare Senior Plus
Authorised for: Orthopaedic surgical consultation and evaluation for bilateral TKA

Referring Physician: Dr. Elizabeth Rodriguez, MD
NPI: 4738291047 | Phone: (555) 520-4400 | Fax Results To: (555) 520-4401
""",
    },
]


def write_files() -> None:
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, ref in enumerate(_REFERRALS, start=1):
        fname = _OUT_DIR / f"ref_{i:03d}.txt"
        header = (
            f"referral_id: {ref['referral_id']}\n"
            f"specialty: {ref['specialty']}\n"
            f"urgency: {ref['urgency']}\n"
            f"patient_name: {ref['patient_name']}\n"
            f"patient_dob: {ref['patient_dob']}\n"
            f"patient_sex: {ref['patient_sex']}\n"
            f"patient_mrn: {ref['patient_mrn']}\n"
            f"insurance: {ref['insurance']}\n"
            f"data_tag: {ref['data_tag']}\n"
            f"---\n"
        )
        fname.write_text(header + ref["text"].lstrip("\n"), encoding="utf-8")
        print(f"  wrote {fname.name}")
    print(f"referrals: {len(_REFERRALS)} files → {_OUT_DIR}")


if __name__ == "__main__":
    write_files()
