"""
Synthetic clinical referral letters.

Data tag: SYNTHETIC
Mirrors real referral letter format: header, patient info, referring physician,
clinical summary, urgency, prior auth, and specialty questions. Covers
cardiology, nephrology, endocrinology, and orthopaedic specialties.

Usage:
    from data.synthetic.referrals import get_referrals
    docs = get_referrals()   # list[Document]
"""

from schemas import Document, DataTag


_REFERRALS = [
    {
        "referral_id": "REF-2025-045782",
        "specialty": "Cardiology",
        "urgency": "URGENT",
        "referring_physician": "Dr. Michael Chen, MD — Internal Medicine, NPI 1234567890",
        "patient": {
            "name": "James Patterson",
            "dob": "1961-07-22",
            "age": 63,
            "sex": "Male",
            "mrn": "MRN-7283940",
            "insurance": "Aetna Commercial",
            "member_id": "AC-7382910-1",
        },
        "letter": """
REFERRAL LETTER — CARDIOLOGY
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
20-minute episode 2 weeks ago that he did not seek care for. Tonight's episode did not resolve with
rest or aspirin 650mg taken at home.

Physical examination: BP 162/94, HR 98, RR 20, SpO2 95% on room air. In mild distress.
Cardiac exam: RRR, no murmurs. Lungs clear. No peripheral oedema.

EKG: New T-wave inversions in V2-V4. Biphasic T-waves in V1. No ST-elevation.
Previously normal EKG on file (6 months ago).

Laboratory results today:
- hs-cTnT 0h: 65 ng/L (ref <14) — ELEVATED
- hs-cTnT 1h: 118 ng/L (delta 53 ng/L) — RISING → meets ESC 0/1h rule-in criteria
- BNP: 148 pg/mL (mildly elevated)
- CMP: Cr 1.1, Glu 194, all others normal
- Lipids: LDL 162, HDL 38 (suboptimal control)
- CXR: No acute cardiopulmonary process

Current medications: Lisinopril 20mg QD, Atorvastatin 40mg QHS, Metformin 1000mg BID,
Omeprazole 20mg QD, Aspirin 81mg QD.
Allergies: Sulfa drugs (rash).

ASSESSMENT: Rising hs-cTnT with anterior T-wave changes in a patient with multiple cardiac
risk factors is consistent with NSTEMI. Patient was given aspirin loading, ticagrelor 180mg
loading dose, and started on IV heparin per ACS protocol in our ED. Troponin continuing to rise.

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
        "referring_physician": "Dr. Jennifer Patel, MD — Internal Medicine/Geriatrics, NPI 1029384756",
        "patient": {
            "name": "Susan Williams",
            "dob": "1962-07-22",
            "age": 62,
            "sex": "Female",
            "mrn": "MRN-3927548",
            "insurance": "BlueCross BlueShield",
            "member_id": "BS-5029847-2",
        },
        "letter": """
REFERRAL LETTER — NEPHROLOGY
Date: 2025-06-20    Referral ID: REF-2025-048291
Urgency: SOON — Appointment within 2-3 weeks

TO: Nephrology Department, Kidney Disease Center
FROM: Dr. Jennifer Patel, MD — Internal Medicine/Geriatrics, NPI 1029384756
      Comprehensive Care Clinic, Phone: (555) 311-2200, Fax: (555) 311-2201

PATIENT: Susan Williams | DOB: 1962-07-22 | Age: 62 | Sex: Female
MRN: MRN-3927548 | Insurance: BlueCross BlueShield | Member ID: BS-5029847-2

REASON FOR REFERRAL: Chronic kidney disease stage 3b with declining eGFR and significant
proteinuria in the setting of longstanding hypertension and type 2 diabetes. Request for
nephrology co-management and evaluation for progression.

CLINICAL SUMMARY:
Ms. Williams is a 62-year-old female with 22-year history of hypertension and 14-year history
of type 2 diabetes who presents with progressive CKD. Approximately 6 months ago, routine labs
revealed creatinine 1.35 with eGFR 51 mL/min (Stage 3a). We optimised antihypertensive therapy
targeting BP <120/80 per CKD guidelines and intensified diabetes management. However, most recent
labs this month demonstrate continued deterioration.

Current labs:
- Creatinine: 1.62 mg/dL (was 1.35 six months ago — declining)
- eGFR: 35 mL/min/1.73m² (Stage 3b — was Stage 3a)
- BUN: 28 mg/dL
- 24-hour urine protein: 1.8 g/day (significant proteinuria — approaching nephrotic range)
- Urinalysis: 3+ proteinuria, negative hematuria, no WBC, no casts
- Potassium: 4.2 (normal — monitoring given ACEi)
- Phosphorus: 3.6 (normal)
- Calcium: 8.9 (normal)
- HbA1c: 7.2% (reasonably controlled)

Physical examination: BP 132/78 on triple antihypertensive therapy. Weight 168 lbs, BMI 28.1.
No peripheral oedema. Skin without uremic changes. No peripheral neuropathy evident.

Current medications: Lisinopril 40mg QD (maximum dose), Amlodipine 5mg QD, HCTZ 12.5mg QD,
Atorvastatin 40mg QHS, Metformin 1000mg BID, Glipizide 5mg BID, Levothyroxine 75mcg QD,
Aspirin 81mg QD.
Allergies: Penicillin (rash).

ASSESSMENT: 62-year-old with longstanding diabetes and hypertension presenting with Stage 3b CKD
with progressive decline in eGFR and significant proteinuria (1.8g/day). Primary aetiology is
likely diabetic nephropathy, but other causes (IgA nephropathy, membranous nephropathy) should
be excluded. BP appears controlled at 132/78 but urine protein remains high despite maximum-dose
ACEi, suggesting inadequate nephroprotection. Patient is at risk for progression to ESRD.

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
        "referring_physician": "Dr. David Thompson, MD — Family Medicine, NPI 8374829014",
        "patient": {
            "name": "Robert Martinez",
            "dob": "1978-05-11",
            "age": 47,
            "sex": "Male",
            "mrn": "MRN-7293847",
            "insurance": "Humana HMO",
            "member_id": "HM-3847291-2",
        },
        "letter": """
REFERRAL LETTER — ENDOCRINOLOGY
Date: 2025-06-18    Referral ID: REF-2025-047382
Urgency: ROUTINE — Appointment within 4 weeks

TO: Endocrinology Department, Diabetes & Endocrine Center
FROM: Dr. David Thompson, MD — Family Medicine, NPI 8374829014
      Family Care Network, Phone: (555) 400-3300, Fax: (555) 400-3301

PATIENT: Robert Martinez | DOB: 1978-05-11 | Age: 47 | Sex: Male
MRN: MRN-7293847 | Insurance: Humana HMO | Member ID: HM-3847291-2

REASON FOR REFERRAL: Poorly controlled type 2 diabetes mellitus with HbA1c 8.9% despite
maximum doses of oral agents. Significant insulin resistance. Request for evaluation for
advanced therapies and possible insulin initiation.

CLINICAL SUMMARY:
Mr. Martinez is a 47-year-old male with 8-year history of type 2 diabetes who has had
progressively worsening glycaemic control despite escalating oral medication regimens.
He was started on metformin monotherapy at diagnosis, then pioglitazone was added 3 years ago,
and linagliptin added 18 months ago. Despite this triple oral regimen at maximum doses,
HbA1c remains elevated at 8.9% (goal <7%).

Patient reports reasonable medication adherence using pill organiser. He checks blood glucose
2-3 times per week; fasting readings 160-220 mg/dL. Works as an accountant (sedentary).
Walks approximately 1-2 miles/week. Diet: standard American diet with frequent fast food.
Weight gain of 35 lbs since DM diagnosis 8 years ago.

Physical examination: BP 138/84, HR 76. Weight 242 lbs, Ht 70 inches, BMI 34.7.
No acanthosis nigricans. Skin intact. Monofilament sensation intact bilaterally (no neuropathy yet).
Abdomen: central obesity, non-tender.

Relevant labs this month:
- HbA1c: 8.9% (goal <7%)
- Fasting glucose: 156 mg/dL
- Fasting insulin: 34 mIU/L (ref 2-12) — MARKEDLY ELEVATED
- HOMA-IR: 13.3 (ref <2) — SEVERE insulin resistance
- C-peptide: 3.2 ng/mL (elevated — sufficient endogenous production)
- Creatinine: 0.95, eGFR 91 (normal kidneys — SGLT2 inhibitor feasible)
- ALT: 78 U/L (elevated — NAFLD suspected, confirmed on prior ultrasound)
- Triglycerides: 256 mg/dL (elevated — metabolic syndrome)
- LDL: 118 mg/dL (above goal for high-risk patient)
- HDL: 38 mg/dL (low)
- TSH: 3.2 (normal)

Current medications: Metformin 1000mg BID, Pioglitazone 45mg QD, Linagliptin 5mg QD,
Losartan 100mg QD, Atorvastatin 80mg QHS, Allopurinol 300mg QD, Aspirin 81mg QD,
Omeprazole 20mg QD.
Allergies: NKDA.

Comorbidities: HTN, hyperlipidemia, obesity (BMI 34.7), OSA on CPAP, NAFLD (on ultrasound),
gout (on allopurinol). No cardiovascular events to date.

ASSESSMENT: Poorly controlled T2DM with severe insulin resistance (HOMA-IR 13.3), metabolic
syndrome, NAFLD, and central obesity. Insufficient beta-cell failure — adequate C-peptide.
Primary issue is insulin resistance, not secretory failure. Patient is a candidate for GLP-1
receptor agonist therapy for both glycaemic control and weight loss, or SGLT2 inhibitor for
metabolic and cardiovascular protection, or combination. Insulin may eventually be needed.

QUESTIONS FOR ENDOCRINOLOGY:
1. Is GLP-1 agonist (semaglutide or liraglutide) preferred over insulin initiation?
2. Should we add SGLT2 inhibitor given no cardiovascular events but high risk?
3. How to best address the underlying insulin resistance?
4. What is the goal BMI, and does patient qualify for obesity pharmacotherapy?
5. What cardiovascular risk reduction strategy is recommended?

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
        "referring_physician": "Dr. Elizabeth Rodriguez, MD — Geriatric Medicine, NPI 4738291047",
        "patient": {
            "name": "Margaret Davis",
            "dob": "1954-09-30",
            "age": 70,
            "sex": "Female",
            "mrn": "MRN-8374928",
            "insurance": "UnitedHealthcare Senior Plus",
            "member_id": "UH-2847392-1",
        },
        "letter": """
REFERRAL LETTER — ORTHOPAEDIC SURGERY
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
Mrs. Davis is a 70-year-old retired teacher with 15-year history of bilateral knee osteoarthritis,
right worse than left. She worked 35 years as a teacher requiring prolonged standing, which likely
contributed to knee degeneration.

Conservative management history:
- Right knee: 3 series of intra-articular corticosteroid injections (most recent 8 months ago —
  minimal benefit), failed 6-month trial of topical diclofenac, failed 3-session hyaluronic acid
  injection course (6 months ago — minimal sustained relief). Physiotherapy completed (12 sessions).
- Left knee: 2 corticosteroid injection series, physiotherapy.
- NSAIDs: chronic naproxen 500mg BID + acetaminophen 1g TID — partial relief only.

Current functional status: Pain rated 8-9/10 bilateral, worse with walking, stairs, and
prolonged standing. Pain disrupts sleep (wakes 2-3x/night). Can walk only 1-2 blocks
with difficulty. Cannot climb stairs without significant discomfort. Has stopped gardening
and playing with grandchildren. Antalgic gait with crutch assistance bilaterally.

Physical examination: BP 132/78, HR 68, weight 168 lbs, BMI 28.9.
Right knee: Significant effusion, warmth (no erythema), valgus deformity, ROM 0-90° (pain-limited),
significant crepitus, stable ligaments.
Left knee: Moderate effusion, ROM 0-100°, mild valgus deformity, less severe than right.
Gait: antalgic, bilateral. Walking with forearm crutches.

Imaging:
Right knee X-rays (AP/lateral/weight-bearing): Kellgren-Lawrence Grade 4 (severe) OA.
Marked medial compartment joint space narrowing, prominent osteophytes, subchondral sclerosis.
Left knee X-rays: Kellgren-Lawrence Grade 3 (moderate-to-severe) OA.

Recent labs: HbA1c 6.9% (well controlled), Creatinine 0.88, eGFR 78, Hgb 13.2, Plt 245,
INR normal. All within acceptable surgical parameters.

Medical comorbidities (well controlled): T2DM (HbA1c 6.9%), HTN (BP 132/78), hyperlipidemia,
osteoporosis (on alendronate), GERD.
Prior surgery: Right shoulder rotator cuff repair 2015 — successful outcome.
Allergies: Latex (local contact reaction) — NO systemic anaphylaxis. Advise surgical team.

Current medications: Metformin 1000mg QD, Lisinopril 20mg QD, HCTZ 12.5mg QD, Atorvastatin 40mg QHS,
Alendronate 70mg weekly, Calcium carbonate 600mg BID + Vitamin D, Omeprazole 20mg QD,
Naproxen 500mg BID, Acetaminophen 1g TID PRN.

Functional status / home situation: Lives alone in single-story home (favourable layout — no stairs
to bedroom). Daughter lives 10 minutes away, willing to provide post-operative support. Patient
is motivated and has realistic expectations about recovery timeline.

ASSESSMENT: 70-year-old with severe bilateral knee OA, right grade 4 and left grade 3, with
significant functional decline and exhausted conservative management options. Medically fit for
surgery with well-controlled comorbidities. She is an appropriate candidate for total knee
arthroplasty (TKA) consideration. The degree of functional impairment, sleep disruption, and
failure of 18+ months of conservative management meets standard criteria for surgical referral.

QUESTIONS FOR ORTHOPAEDICS:
1. Is patient a candidate for bilateral TKA? Would you recommend staged procedures or simultaneous?
2. What is the planned timeline for scheduling?
3. What pre-operative clearance will be required (cardiac, anaesthesia)?
4. What are the peri-operative management protocols for her alendronate and NSAIDs?
5. What is the expected functional outcome and rehabilitation timeline?

PRIOR AUTHORISATION:
Auth Number: PA-938482 | Insurance: UnitedHealthcare Senior Plus
Authorised for: Orthopaedic surgical consultation and evaluation for bilateral TKA

Referring Physician: Dr. Elizabeth Rodriguez, MD
NPI: 4738291047 | Phone: (555) 520-4400 | Fax Results To: (555) 520-4401
""",
    },
]


# ── Public API ────────────────────────────────────────────────────────────────

def get_referrals() -> list[Document]:
    """
    Returns the synthetic referral letter corpus as Document objects.
    Tag: SYNTHETIC — realistic referral format, no real patients.
    """
    docs = []
    for ref in _REFERRALS:
        metadata = {
            "referral_id": ref["referral_id"],
            "specialty": ref["specialty"],
            "urgency": ref["urgency"],
            "patient_name": ref["patient"]["name"],
            "patient_dob": ref["patient"]["dob"],
            "patient_sex": ref["patient"]["sex"],
            "insurance": ref["patient"]["insurance"],
            "source_type": "referral_letter",
        }
        docs.append(
            Document(
                id=ref["referral_id"],
                text=ref["letter"].strip(),
                metadata=metadata,
                tag=DataTag.SYNTHETIC,
            )
        )
    return docs
