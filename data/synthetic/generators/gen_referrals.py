#!/usr/bin/env python3
"""
Generator: writes synthetic clinical referral letters as plain .txt files.

Run once to produce data files. Re-run to regenerate or add more referrals.
Output: data/synthetic/referrals/ref_001.txt ... ref_016.txt

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
    {
        "referral_id": "REF-2025-051234",
        "specialty": "Pulmonology",
        "urgency": "SOON",
        "patient_name": "Nathan Brooks",
        "patient_dob": "1957-02-14",
        "patient_sex": "Male",
        "patient_mrn": "MRN-2938471",
        "insurance": "Medicare Part B",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — PULMONOLOGY
Date: 2025-03-10    Referral ID: REF-2025-051234
Urgency: SOON — Appointment within 2 weeks

TO: Pulmonology Department, Lung Disease Center
FROM: Dr. Alan Foster, MD — Internal Medicine, NPI 3847291038
      Primary Care Partners, Phone: (555) 600-5500, Fax: (555) 600-5501

PATIENT: Nathan Brooks | DOB: 1957-02-14 | Age: 68 | Sex: Male
MRN: MRN-2938471 | Insurance: Medicare Part B

REASON FOR REFERRAL: Severe COPD (GOLD III, FEV1 38%) with frequent exacerbations (2 in 6 months),
persistent dyspnoea despite maximum inhaled therapy. Evaluation for pulmonary rehabilitation and
advanced therapies (LVRS, bronchoscopic lung volume reduction eligibility assessment).

CLINICAL SUMMARY:
Mr. Brooks is a 68-year-old male with severe COPD diagnosed 8 years ago on background of 45 pack-year
smoking history (quit 3 years ago). He is on maximum inhaled therapy (LAMA + LABA + ICS) and home
oxygen (2L/min continuous). Two exacerbations in the past 6 months — one requiring ICU admission
(ventilation-related hypercapnia).

Spirometry (3 months ago): FEV1 38% predicted | FEV1/FVC 0.52 | RV 185% (hyperinflation) | DLCO 40%
6MWT: 220m (significant limitation)
Exacerbation history: Hospital 2024-09 (4 days), ICU 2024-11 (3 days NIV)
CAT Score: 24 (highly symptomatic) | mMRC: 3 (limited to house)

Comorbidities: Pulmonary HTN (mPAP 28 — mild), T2DM, OSA (CPAP non-adherent), HTN.
Current medications: Tiotropium 18mcg QD, Salmeterol/Fluticasone 50/500mcg BID, Albuterol PRN,
Home O2 2L/min, Metformin 500mg BID, Lisinopril 10mg QD.
Allergies: Penicillin (GI intolerance).

QUESTIONS FOR PULMONOLOGY:
1. Does patient qualify for pulmonary rehabilitation programme?
2. Eligibility for LVRS or bronchoscopic valve placement?
3. Optimise NIV settings at home?
4. What is survival prognosis and should palliative care be introduced?

PRIOR AUTHORISATION: Auth PA-915273 | Authorised for pulmonology consultation and PFTs.

Referring Physician: Dr. Alan Foster, MD
NPI: 3847291038 | Phone: (555) 600-5500 | Fax: (555) 600-5501
""",
    },
    {
        "referral_id": "REF-2025-052847",
        "specialty": "Neurology",
        "urgency": "URGENT",
        "patient_name": "Theodore Kapoor",
        "patient_dob": "1954-08-27",
        "patient_sex": "Male",
        "patient_mrn": "MRN-4738291",
        "insurance": "BlueCross PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — NEUROLOGY (STROKE)
Date: 2025-05-09    Referral ID: REF-2025-052847
Urgency: URGENT — Same-day / next-day appointment

TO: Neurology Stroke Clinic
FROM: Dr. Helen Voss, MD — Emergency Medicine, NPI 7382910473
      City General Emergency Department, Phone: (555) 700-0911

PATIENT: Theodore Kapoor | DOB: 1954-08-27 | Age: 70 | Sex: Male
MRN: MRN-4738291 | Insurance: BlueCross PPO

REASON FOR REFERRAL: Transient ischaemic attack (TIA) — 20-minute episode of right arm weakness
and aphasia, fully resolved. ABCD2 score 6 (high-risk). Urgent neurovascular assessment needed.

CLINICAL SUMMARY:
Mr. Kapoor presented to the ED for a 20-minute episode of sudden right arm weakness and expressive
aphasia that resolved completely before arrival. Last known well: 2 hours prior to ED presentation.
ABCD2 score: Age 70 (1) + BP >140 (1) + Clinical features (focal 2) + Duration 10-59min (1) + DM (1) = 6.

On arrival: NIHSS 0. Full recovery. No residual deficit.

CT Head: No infarct. No haemorrhage. MRI DWI: Small acute DWI lesion in left posterior MCA territory (8mm).
MRA: 40% left internal carotid stenosis (moderate).
EKG: Normal sinus rhythm. No AF.
Troponin: negative. BMP: normal.

PMH: HTN (poorly controlled — BP 182/96 on arrival), T2DM, hyperlipidemia.
Meds: Amlodipine 10mg QD, Metformin 1000mg BID, Atorvastatin 20mg QHS, Aspirin 81mg QD.

QUESTIONS FOR NEUROLOGY:
1. Is this TIA or minor stroke given the DWI lesion?
2. Dual antiplatelet therapy (aspirin + clopidogrel) for 21 days per POINT trial?
3. What is the 90-day stroke risk? Requires inpatient admission vs urgent outpatient?
4. Carotid endarterectomy evaluation (40% ICA stenosis)?
5. Long-term BP target and statin intensity?

Referring Physician: Dr. Helen Voss, MD
NPI: 7382910473 | Phone: (555) 700-0911
""",
    },
    {
        "referral_id": "REF-2025-053918",
        "specialty": "Gastroenterology",
        "urgency": "SOON",
        "patient_name": "Victor Chen",
        "patient_dob": "1961-04-15",
        "patient_sex": "Male",
        "patient_mrn": "MRN-5839201",
        "insurance": "Aetna PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — GASTROENTEROLOGY
Date: 2025-08-10    Referral ID: REF-2025-053918
Urgency: SOON — Appointment within 1 week

TO: Gastroenterology Department
FROM: Dr. Priya Nair, MD — Emergency Medicine / Hospitalist, NPI 9283740192
      City Medical Center, Phone: (555) 811-2200

PATIENT: Victor Chen | DOB: 1961-04-15 | Age: 64 | Sex: Male
MRN: MRN-5839201 | Insurance: Aetna PPO

REASON FOR REFERRAL: Recent hospitalisation for upper GIB (haematemesis, melena). Now stable.
Requesting urgent outpatient upper endoscopy with H. pylori testing and GIB source identification.

CLINICAL SUMMARY:
Mr. Chen was hospitalised 5 days ago for upper GIB (haematemesis and melaena) in the setting of
chronic NSAID use (naproxen 500mg BID) and significant alcohol use (6-8 drinks/day). Hgb nadir
7.4g/dL. Received 2u pRBC with Hgb rise to 11.8. Haemodynamically stabilised with IV PPIs.
Endoscopy NOT done during admission (patient declined inpatient procedure; agreed to outpatient).

Risk factors: NSAID use, alcohol, age 64, Hgb decline 7g/dL, haemodynamic instability on admission.
Glasgow-Blatchford Score: 14 (high-risk).

Current outpatient status: Haemodynamically stable. Hgb 11.8. Stools normal colour.
Medications changed: NSAIDs STOPPED, Pantoprazole 40mg BID initiated, Alcohol cessation counselled.

QUESTIONS FOR GASTROENTEROLOGY:
1. EGD with H. pylori biopsy — identify bleeding source (peptic ulcer most likely).
2. Assess for varices/portal hypertension given alcohol history.
3. Should PPI be continued indefinitely?

Referring Physician: Dr. Priya Nair, MD
NPI: 9283740192 | Phone: (555) 811-2200
""",
    },
    {
        "referral_id": "REF-2025-054201",
        "specialty": "Haematology",
        "urgency": "SOON",
        "patient_name": "Jessica Brown",
        "patient_dob": "1985-11-03",
        "patient_sex": "Female",
        "patient_mrn": "MRN-6741830",
        "insurance": "Cigna HMO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — HAEMATOLOGY
Date: 2025-05-01    Referral ID: REF-2025-054201
Urgency: SOON — Appointment within 2 weeks

TO: Haematology / Thrombosis Clinic
FROM: Dr. Ama Asante, MD — Vascular Medicine, NPI 8374920183
      Vascular & Thrombosis Centre, Phone: (555) 922-3300

PATIENT: Jessica Brown | DOB: 1985-11-03 | Age: 39 | Sex: Female
MRN: MRN-6741830 | Insurance: Cigna HMO

REASON FOR REFERRAL: Unprovoked proximal DVT (popliteal + femoral) in a 39-year-old female.
Evaluation for inherited thrombophilia, malignancy screen, and anticoagulation duration discussion.

CLINICAL SUMMARY:
Ms. Brown presented with a 3-day history of right leg swelling confirmed as proximal DVT on Doppler US.
No clear provoking factor identified (no recent travel, surgery, immobility, or hormonal contraception).
No prior VTE. No family history of thrombosis initially reported.

Started on Apixaban 10mg BID x7 days → 5mg BID.

Labs to date: D-dimer 4.8 µg/mL (elevated). CBC/CMP normal. No malignancy identified on CXR or CT Chest/Abdomen (ordered in ED).

Thrombophilia screen ordered but NOT yet performed. Awaiting haematology guidance.

Family history update: Mother had DVT in pregnancy. Maternal aunt had "blood clot in lung."

QUESTIONS FOR HAEMATOLOGY:
1. What thrombophilia screen is appropriate while on anticoagulation?
2. When to test (after stopping anticoagulation vs on drug)?
3. Should anticardiolipin antibody / lupus anticoagulant be checked?
4. Duration of anticoagulation: 3 months vs extended therapy?
5. Genetic counselling for factor V Leiden?

Referring Physician: Dr. Ama Asante, MD
NPI: 8374920183 | Phone: (555) 922-3300
""",
    },
    {
        "referral_id": "REF-2025-055382",
        "specialty": "Rheumatology",
        "urgency": "ROUTINE",
        "patient_name": "Angela Moore",
        "patient_dob": "1970-06-22",
        "patient_sex": "Female",
        "patient_mrn": "MRN-7238490",
        "insurance": "UnitedHealthcare Select",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — RHEUMATOLOGY
Date: 2025-04-28    Referral ID: REF-2025-055382
Urgency: ROUTINE — Appointment within 4-6 weeks

TO: Rheumatology Department
FROM: Dr. Michael Bennett, MD — Primary Care, NPI 6382910473

PATIENT: Angela Moore | DOB: 1970-06-22 | Age: 54 | Sex: Female
MRN: MRN-7238490 | Insurance: UnitedHealthcare Select

REASON FOR REFERRAL: Positive ANA (1:320, homogenous pattern), arthralgia, fatigue, and new
discoid rash — possible SLE. Needs expert evaluation, disease confirmation, and treatment initiation.

CLINICAL SUMMARY:
Ms. Moore is a 54-year-old female with 8-month history of joint pain (MCPs, PIPs, wrists, bilateral),
morning stiffness >1h, fatigue, hair thinning, and new butterfly-shaped facial rash. CXR normal.
ESR 72 mm/h (elevated). CRP 28 mg/L. CBC: mild leukopenia (WBC 3.4k) with lymphopenia.

Autoimmune labs: ANA 1:320 homogenous | anti-dsDNA: 48 IU/mL (elevated) | C3 68 (LOW) | C4 8 (LOW)
Urinalysis: 2+ protein, 10-15 RBC/hpf — proteinuria and haematuria concerning for lupus nephritis.

SLICC criteria: Rash (1), Arthritis (1), CBC (leukopenia 1), ANA positive (1), anti-dsDNA (1),
low complement (1), renal (proteinuria 1) — 7/11 met (threshold ≥4).

QUESTIONS FOR RHEUMATOLOGY:
1. Confirm SLE diagnosis and assess activity/organ involvement?
2. Should hydroxychloroquine be started empirically?
3. Is kidney biopsy indicated (proteinuria + haematuria)?
4. Management if lupus nephritis confirmed?

Referring Physician: Dr. Michael Bennett, MD
NPI: 6382910473 | Phone: (555) 744-2200
""",
    },
    {
        "referral_id": "REF-2025-056491",
        "specialty": "Oncology",
        "urgency": "URGENT",
        "patient_name": "Harold Fisher",
        "patient_dob": "1951-09-14",
        "patient_sex": "Male",
        "patient_mrn": "MRN-3847291",
        "insurance": "Medicare Advantage — Humana",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — THORACIC ONCOLOGY
Date: 2025-06-05    Referral ID: REF-2025-056491
Urgency: URGENT — Seen within 1 week

TO: Thoracic Oncology, Cancer Centre
FROM: Dr. Janet Kim, MD — Pulmonology, NPI 4839201738

PATIENT: Harold Fisher | DOB: 1951-09-14 | Age: 73 | Sex: Male
MRN: MRN-3847291 | Insurance: Medicare Advantage

REASON FOR REFERRAL: New 4.2cm right upper lobe lung mass with mediastinal lymphadenopathy
and right-sided pleural effusion on CT chest. High suspicion for non-small cell lung cancer.

CLINICAL SUMMARY:
Mr. Fisher is a 73-year-old male, 50 pack-year smoker (quit 5 years ago), presenting with 8-week
progressive dyspnoea, 7kg unintentional weight loss, and right-sided chest discomfort.

CT Chest/Abdomen/Pelvis: 4.2cm irregular spiculated RUL mass with satellite nodule (1.2cm).
Enlarged right paratracheal (1.8cm) and subcarinal (1.4cm) nodes. Right pleural effusion (small).
No definitive bone metastases on this CT.

PET-CT: Ordered — pending.
Brain MRI: Ordered — pending.

Laboratory: CBC normal | Na 131 (low) | Ca 11.4 (HIGH — hypercalcaemia of malignancy??)
LDH 348 (elevated) | Albumin 2.8 (depleted)

Bronchoscopy planned — EBUS-TBNA of mediastinal nodes arranged for next week.

QUESTIONS FOR ONCOLOGY:
1. Confirm staging once PET/brain MRI available
2. Tissue diagnosis (EBUS first vs CT-guided biopsy?)
3. If NSCLC confirmed: molecular profiling (EGFR, ALK, PD-L1)?
4. Is patient fit for treatment? PS assessment?
5. Early palliative care integration?

Referring Physician: Dr. Janet Kim, MD
NPI: 4839201738 | Phone: (555) 644-8810
""",
    },
    {
        "referral_id": "REF-2025-057384",
        "specialty": "Hepatology",
        "urgency": "SOON",
        "patient_name": "George Alvarez",
        "patient_dob": "1968-03-27",
        "patient_sex": "Male",
        "patient_mrn": "MRN-9182736",
        "insurance": "Medicaid Managed Care",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — HEPATOLOGY
Date: 2025-07-18    Referral ID: REF-2025-057384
Urgency: SOON — 2 weeks

TO: Hepatology, Liver Disease Program
FROM: Dr. Paul Santos, MD — Primary Care, NPI 3847291029

PATIENT: George Alvarez | DOB: 1968-03-27 | Age: 57 | Sex: Male
MRN: MRN-9182736 | Insurance: Medicaid

REASON FOR REFERRAL: NAFLD with elevated liver enzymes, suspected NASH with bridging fibrosis
on FibroScan. Evaluation for disease staging and management.

CLINICAL SUMMARY:
Mr. Alvarez is a 57-year-old male with obesity (BMI 36), T2DM, hyperlipidemia, and HTN
with persistently elevated transaminases x2 years (ALT 68-94, AST 52-78). FibroScan 2 weeks ago:
CAP 312dB/m (significant steatosis) | LSM 12.8 kPa (F3 — significant fibrosis by M1 cut-off).
No alcohol use. Hepatitis B/C negative. ANA 1:40 (non-specific). No haemochromatosis.
No symptoms of portal HTN. INR normal, albumin normal, bilirubin normal — compensated liver disease.

QUESTIONS FOR HEPATOLOGY:
1. Is liver biopsy indicated to confirm NASH vs other aetiology?
2. Drug eligibility: Semaglutide or Resmetirom (FDA approved for NASH)?
3. Surveillance plan for HCC?
4. Screening for varices (despite compensated — F3 fibrosis)?
5. Dietary programme referral?

Referring Physician: Dr. Paul Santos, MD
NPI: 3847291029 | Phone: (555) 533-4400
""",
    },
    {
        "referral_id": "REF-2025-058293",
        "specialty": "Cardiology — Heart Failure",
        "urgency": "SOON",
        "patient_name": "Dorothy Huang",
        "patient_dob": "1950-12-01",
        "patient_sex": "Female",
        "patient_mrn": "MRN-6473820",
        "insurance": "Medicare + Medigap",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — CARDIOLOGY / HEART FAILURE CLINIC
Date: 2025-11-14    Referral ID: REF-2025-058293
Urgency: SOON — 1-2 weeks

TO: Heart Failure Program, Cardiology
FROM: Dr. Linda Park, MD — Internal Medicine, NPI 8392017483

PATIENT: Dorothy Huang | DOB: 1950-12-01 | Age: 74 | Sex: Female
MRN: MRN-6473820 | Insurance: Medicare

REASON FOR REFERRAL: HFpEF (EF 58%) with recurrent hospitalisations (2 in past year) despite
optimal medical therapy. Requesting advanced heart failure evaluation and optimisation.

CLINICAL SUMMARY:
Mrs. Huang has known HFpEF (echo EF 58%) with 2 hospital admissions for acute decompensation in
the past year, despite compliance with furosemide, spironolactone, and sacubitril/valsartan.
HTN, AF (on apixaban), DM2, obesity (BMI 34).
NT-proBNP remains elevated at 1,240 pg/mL. BNP 380 pg/mL at last check. eGFR 48 (CKD 3b).
Echo: Diastolic dysfunction Grade 2 (E/e' 18). EF 58%. No significant valve disease.
6MWT: 240m. Functional class NYHA III.

QUESTIONS FOR CARDIOLOGY HF CLINIC:
1. Optimise diuretic strategy (torasemide vs furosemide)?
2. Role of SGLT2 inhibitor (empagliflozin — EMPEROR-Preserved)?
3. ICD / CRT indication assessment?
4. Is patient a candidate for advanced HF therapies?
5. Structured HF programme enrolment?

Referring Physician: Dr. Linda Park, MD
NPI: 8392017483 | Phone: (555) 866-3300
""",
    },
    {
        "referral_id": "REF-2025-059182",
        "specialty": "Endocrinology",
        "urgency": "ROUTINE",
        "patient_name": "Sandra Kim",
        "patient_dob": "1979-08-15",
        "patient_sex": "Female",
        "patient_mrn": "MRN-5837290",
        "insurance": "Kaiser Permanente",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — ENDOCRINOLOGY / THYROID
Date: 2025-09-22    Referral ID: REF-2025-059182
Urgency: ROUTINE — 4 weeks

TO: Endocrinology Department
FROM: Dr. Marcus Williams, MD — OBGYN, NPI 7283910473

PATIENT: Sandra Kim | DOB: 1979-08-15 | Age: 45 | Sex: Female
MRN: MRN-5837290 | Insurance: Kaiser

REASON FOR REFERRAL: Thyroid nodule — 2.2cm right lobe, Bethesda Category III (atypia of
undetermined significance) on FNA. Endocrinology evaluation for management.

CLINICAL SUMMARY:
Ms. Kim was found to have a right thyroid nodule on routine neck ultrasound (ordered for neck pain).
Subsequent US showed 2.2cm, hypoechoic, irregular margins, microcalcifications — ACR TIRADS 5.
FNA biopsy: Bethesda Category III (AUS/FLUS). Repeat FNA in 3 months vs molecular testing
vs surgery — requires endocrinology expertise.

TSH 1.8 (normal) | T4 normal | Thyroglobulin normal | Anti-TPO antibodies elevated (Hashimoto's).
No symptoms of hyper/hypothyroidism. No cervical lymphadenopathy palpable.

No family history of thyroid cancer. No neck irradiation history.

QUESTIONS FOR ENDOCRINOLOGY:
1. Repeat FNA vs molecular marker testing (ThyroSeq, Afirma)?
2. If molecular testing: what is malignancy risk with Bethesda III and TIRADS 5?
3. Surgery consultation indicated?
4. Manage Hashimoto's thyroiditis?

Referring Physician: Dr. Marcus Williams, MD
NPI: 7283910473 | Phone: (555) 977-5500
""",
    },
    {
        "referral_id": "REF-2025-060284",
        "specialty": "Urology",
        "urgency": "ROUTINE",
        "patient_name": "Patrick O'Brien",
        "patient_dob": "1962-01-20",
        "patient_sex": "Male",
        "patient_mrn": "MRN-4728390",
        "insurance": "BCBS Federal Employee",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — UROLOGY
Date: 2025-10-08    Referral ID: REF-2025-060284
Urgency: ROUTINE — 4 weeks

TO: Urology Department
FROM: Dr. Thomas Reed, MD — Internal Medicine, NPI 2847391028

PATIENT: Patrick O'Brien | DOB: 1962-01-20 | Age: 63 | Sex: Male
MRN: MRN-4728390 | Insurance: BCBS Federal Employee

REASON FOR REFERRAL: Gross haematuria x2 episodes — microhaematuria persistent on repeat UA.
CT urogram ordered. Requesting urological evaluation to rule out bladder malignancy.

CLINICAL SUMMARY:
Mr. O'Brien is a 63-year-old male ex-smoker (30 pack-years, quit 5 years ago) with two
episodes of gross haematuria in the past 2 months (painless). Repeat urinalysis confirms
persistent microhaematuria (>25 RBC/hpf on two occasions). No UTI. No traumatic cause.
No anticoagulation.

CT Urogram: Irregular filling defect posterior wall bladder (1.4cm) — suspicious for bladder
lesion. No upper tract abnormality. No hydroureteronephrosis.

PSA 2.8 ng/mL (age-adjusted normal). Cr 1.0.

QUESTIONS FOR UROLOGY:
1. Cystoscopy with possible TURBT?
2. Does CT finding require urgent evaluation vs standard outpatient?
3. If transitional cell carcinoma confirmed — staging and treatment?

Referring Physician: Dr. Thomas Reed, MD
NPI: 2847391028 | Phone: (555) 488-6200
""",
    },
    {
        "referral_id": "REF-2025-061385",
        "specialty": "Psychiatry",
        "urgency": "SOON",
        "patient_name": "Michelle Davis",
        "patient_dob": "1990-03-12",
        "patient_sex": "Female",
        "patient_mrn": "MRN-8374019",
        "insurance": "Cigna Behavioral Health",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — PSYCHIATRY
Date: 2025-07-30    Referral ID: REF-2025-061385
Urgency: SOON — 1-2 weeks

TO: Psychiatric Services, Behavioural Health Department
FROM: Dr. Christine Walsh, MD — Primary Care, NPI 3748291047

PATIENT: Michelle Davis | DOB: 1990-03-12 | Age: 35 | Sex: Female
MRN: MRN-8374019 | Insurance: Cigna Behavioral Health

REASON FOR REFERRAL: New diagnosis of Bipolar I disorder following manic episode requiring ED
visit. Requesting psychiatric evaluation, medication management, and long-term care planning.

CLINICAL SUMMARY:
Ms. Davis presented to the ED 2 weeks ago with a 10-day manic episode (grandiosity, racing thoughts,
decreased sleep [2h/night], hypersexuality, excessive spending, pressured speech). No psychotic
features. No suicidal ideation. No substance use (UDS negative). Discharge diagnosis: Bipolar I.
Started on Quetiapine 50mg QHS in ED — tolerating, some improvement. No current depressive symptoms.
No prior psychiatric history. Strong family history: mother with bipolar disorder.

PHQ-9 (current, euthymic phase): 4 (minimal symptoms).

Current meds: Quetiapine 50mg QHS | OCP (may affect mood in some patients — discuss)

QUESTIONS FOR PSYCHIATRY:
1. Confirm diagnosis and assess for mixed features or cycling?
2. Is quetiapine monotherapy sufficient or should lithium/valproate be added?
3. OCP interaction risk with mood stabilisers?
4. Long-term monitoring plan (lithium levels, thyroid, renal)?

Referring Physician: Dr. Christine Walsh, MD
NPI: 3748291047 | Phone: (555) 333-2211
""",
    },
    {
        "referral_id": "REF-2025-062491",
        "specialty": "Pain Management",
        "urgency": "ROUTINE",
        "patient_name": "Carlos Rivera",
        "patient_dob": "1965-10-08",
        "patient_sex": "Male",
        "patient_mrn": "MRN-2938472",
        "insurance": "Humana PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — PAIN MANAGEMENT
Date: 2025-08-22    Referral ID: REF-2025-062491
Urgency: ROUTINE — 4-6 weeks

TO: Chronic Pain Management Clinic
FROM: Dr. Rosa Mendez, MD — Family Medicine, NPI 4738291048

PATIENT: Carlos Rivera | DOB: 1965-10-08 | Age: 59 | Sex: Male
MRN: MRN-2938472 | Insurance: Humana PPO

REASON FOR REFERRAL: Chronic low back pain (LBP) with bilateral L4-L5 radiculopathy, inadequately
controlled with current regimen. Requesting pain management consultation for interventional options.

CLINICAL SUMMARY:
Mr. Rivera is a 59-year-old male with 5-year history of chronic LBP secondary to L4-L5 disc
herniation with bilateral radiculopathy (MRI-confirmed). Physical therapy completed x6 months —
partial response. Currently on gabapentin 900mg TID, meloxicam 15mg QD, and acetaminophen 1g TID.
VAS pain score: 7/10 daily average. Functioning: limited to sedentary activity, not working.

MRI L-spine (4 months ago): L4-L5 large disc herniation with bilateral foraminal narrowing.
L3-L4 mild DDD. No cord compression. No surgical emergency.

PDMP check: No concerning prescribing patterns. No opioid history.

QUESTIONS FOR PAIN MANAGEMENT:
1. Lumbar epidural steroid injection feasibility?
2. Medial branch block / radiofrequency ablation at L4-L5?
3. Role of low-dose opioids if interventional fails?
4. Multidisciplinary pain programme referral?

Referring Physician: Dr. Rosa Mendez, MD
NPI: 4738291048 | Phone: (555) 211-7700
""",
    },

    # ── refs 21–40: expanded specialty coverage ──

    {
        "referral_id": "REF-2025-080193",
        "specialty": "Dermatology",
        "urgency": "ROUTINE",
        "patient_name": "Omar Hassan",
        "patient_dob": "1980-03-17",
        "patient_sex": "Male",
        "patient_mrn": "MRN-1029384",
        "insurance": "Aetna PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — DERMATOLOGY
Date: 2025-11-04    Referral ID: REF-2025-080193
Urgency: ROUTINE — Appointment within 4 weeks

TO: Dermatology Department, Skin & Rheumatology Centre
FROM: Dr. Fatima Al-Rashid, MD — Rheumatology, NPI 1928374650
      Rheumatology Associates, Phone: (555) 120-3344, Fax: (555) 120-3345

PATIENT: Omar Hassan | DOB: 1980-03-17 | Age: 45 | Sex: Male
MRN: MRN-1029384 | Insurance: Aetna PPO | Member ID: AP-8374920-3

REASON FOR REFERRAL: Psoriatic arthritis with prominent skin involvement. Joint disease
is reasonably controlled on current biologic therapy; however, extensive scalp and body
plaque psoriasis remains refractory, requiring dermatology co-management.

CLINICAL SUMMARY:
Mr. Hassan is a 45-year-old male with a 10-year history of psoriatic arthritis, currently
managed on secukinumab 300mg monthly with good articular response (low DAS28). Despite
adequate systemic IL-17A inhibition, he has extensive plaque psoriasis involving the scalp
(>50% involvement), trunk, and extensor surfaces of both arms — estimated BSA involvement
approximately 22%. PASI score: 16 (moderate-to-severe). Significant quality of life impact
(DLQI 18/30). He reports marked pruritus, sleep disturbance, and social embarrassment.

Current topical regimen: clobetasol propionate 0.05% scalp solution and calcipotriol/
betamethasone foam — partial response only (PASI reduced from 24 to current 16).
No prior phototherapy. No biologics solely for skin disease.

Comorbidities: HTN (Ramipril 10mg QD), hyperlipidaemia (Rosuvastatin 20mg QD), obesity BMI 31.
Allergies: NSAIDs (GI intolerance). No hepatic or renal impairment.

Relevant labs: LFTs normal | FBC normal | CRP 8 mg/L (mildly elevated) | HbA1c 6.1%

QUESTIONS FOR DERMATOLOGY:
1. Assess whether secukinumab dose optimisation (increase to 300mg 2-weekly) would benefit
   skin disease, or whether a biologic with higher skin efficacy (e.g., ixekizumab, risankizumab)
   should be considered?
2. Role of topical calcineurin inhibitors (tacrolimus) for facial/flexural involvement?
3. Phototherapy (NB-UVB) as adjunct to systemic biologic — feasibility and photosensitivity risk?
4. Scalp management plan beyond clobetasol — tar shampoo, topical calcipotriene?
5. PASI/DLQI target — define treat-to-target for skin in context of PsA management?

PRIOR AUTHORISATION:
Auth Number: PA-112938 | Insurance: Aetna PPO
Authorised for: Dermatology consultation and phototherapy assessment

Referring Physician: Dr. Fatima Al-Rashid, MD
NPI: 1928374650 | Phone: (555) 120-3344 | Fax Results To: (555) 120-3345
""",
    },
    {
        "referral_id": "REF-2025-081047",
        "specialty": "Vascular Surgery",
        "urgency": "URGENT",
        "patient_name": "Raymond Kowalski",
        "patient_dob": "1957-09-05",
        "patient_sex": "Male",
        "patient_mrn": "MRN-3847562",
        "insurance": "Medicare Part B",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — VASCULAR SURGERY
Date: 2025-11-06    Referral ID: REF-2025-081047
Urgency: URGENT — Seen within 48 hours

TO: Vascular Surgery Department, Aortic Centre
FROM: Dr. Kevin Drummond, MD — General Internal Medicine, NPI 8374920165
      Lakeside Medical Group, Phone: (555) 230-4455, Fax: (555) 230-4456

PATIENT: Raymond Kowalski | DOB: 1957-09-05 | Age: 68 | Sex: Male
MRN: MRN-3847562 | Insurance: Medicare Part B | Medicare ID: 1KW-A8-3847

REASON FOR REFERRAL: Abdominal aortic aneurysm 5.2cm — annual surveillance CT showing growth
of 0.6cm in 12 months (was 4.6cm, now 5.2cm). Approaching surgical threshold. Urgent vascular
surgery assessment for elective repair planning.

CLINICAL SUMMARY:
Mr. Kowalski is a 68-year-old male with known AAA under surveillance since 2021. AAA was 3.8cm
at initial diagnosis. Growth rate this year: 0.6cm in 12 months (threshold for referral ≥0.5cm/year
or absolute diameter ≥5.5cm). Aneurysm is infrarenal. No symptoms — no abdominal or back pain.

CT Aortogram (this month): Infrarenal AAA 5.2cm maximum diameter. Aneurysm neck 2.8cm, length
18mm, angulation 28 degrees. Bilateral iliac arteries: right CIA 1.8cm (mildly dilated), left
CIA 1.4cm. No evidence of rupture. No contained haematoma.

Risk factors: 40 pack-year smoker (quit 3 years ago), hypertension (Amlodipine 10mg, Ramipril
10mg), hyperlipidaemia (Atorvastatin 80mg), BMI 26.8. COPD (FEV1 68% — moderate). eGFR 62.
Cardiac: stress echo 18 months ago — no inducible ischaemia. EF 58%.
Allergies: Contrast dye (mild urticaria — pre-medication protocol required).

QUESTIONS FOR VASCULAR SURGERY:
1. Recommend elective repair now given 5.2cm diameter and rapid growth (0.6cm/year)?
2. EVAR vs open repair — anatomy assessment (neck length/angulation/iliac access)?
3. Pre-operative cardiac and pulmonary optimisation plan?
4. Contrast allergy protocol for CT angiography/operative imaging?
5. If watchful waiting: surveillance interval — 3 months vs 6 months?

PRIOR AUTHORISATION:
Auth Number: PA-229384 | Insurance: Medicare Part B
Authorised for: Urgent vascular surgery consultation and pre-operative imaging

Referring Physician: Dr. Kevin Drummond, MD
NPI: 8374920165 | Phone: (555) 230-4455 | Fax Results To: (555) 230-4456
""",
    },
    {
        "referral_id": "REF-2025-082374",
        "specialty": "Gynaecology",
        "urgency": "SOON",
        "patient_name": "Isabella Ferreira",
        "patient_dob": "1987-06-22",
        "patient_sex": "Female",
        "patient_mrn": "MRN-5920384",
        "insurance": "Cigna PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — GYNAECOLOGY
Date: 2025-11-10    Referral ID: REF-2025-082374
Urgency: SOON — Appointment within 2-3 weeks

TO: Gynaecology Department, Women's Health Centre
FROM: Dr. Aisha Mohammed, MD — Primary Care / Women's Health, NPI 2938471056
      Community Women's Clinic, Phone: (555) 340-5566, Fax: (555) 340-5567

PATIENT: Isabella Ferreira | DOB: 1987-06-22 | Age: 38 | Sex: Female
MRN: MRN-5920384 | Insurance: Cigna PPO | Member ID: CP-3847291-4

REASON FOR REFERRAL: Endometriosis with chronic pelvic pain, dysmenorrhoea, and dyspareunia.
Failed first-line medical management. Requesting specialist evaluation for surgical and/or
advanced hormonal management.

CLINICAL SUMMARY:
Ms. Ferreira is a 38-year-old female with a 6-year history of progressively worsening pelvic
pain. Pain is cyclical (VAS 9/10 dysmenorrhoea, 7/10 intermenstrual), associated with
dyspareunia (deep) and dyschezia during menstruation. She reports significant quality of life
impairment affecting work and relationships (EHP-30 score 68/100).

MRI Pelvis (last month): Findings consistent with deep infiltrating endometriosis (DIE) —
left uterosacral ligament nodule (1.4cm), posterior cul-de-sac obliteration, left ovarian
endometrioma 3.1cm. No bowel or ureteric involvement identified.

Previous treatments: Mefenamic acid + NSAIDs (partial relief), combined OCP (inadequate
control, breakthrough pain), Norethisterone 5mg TID — stopped due to mood changes.

Fertility status: Patient is nulliparous and wishes to preserve fertility. Has not actively
tried to conceive. Concerned about fertility implications.

Bloods: CA-125: 48 U/mL (mildly elevated, non-specific). Normal FBC, renal, liver function.
Cervical smear: up to date, normal (2024).
Allergies: None known.

QUESTIONS FOR GYNAECOLOGY:
1. Laparoscopic excision of DIE nodule and drainage of endometrioma — surgical candidacy?
2. Fertility implications — pre-operative AMH and antral follicle count assessment?
3. Post-operative hormonal suppression — Dienogest vs progestogen IUS vs GnRH agonist?
4. Does MRI suggest involvement of bowel/ureter — colorectal surgical opinion needed?
5. Referral to endometriosis MDT if available?

PRIOR AUTHORISATION:
Auth Number: PA-338492 | Insurance: Cigna PPO
Authorised for: Gynaecology consultation and laparoscopic assessment

Referring Physician: Dr. Aisha Mohammed, MD
NPI: 2938471056 | Phone: (555) 340-5566 | Fax Results To: (555) 340-5567
""",
    },
    {
        "referral_id": "REF-2025-083291",
        "specialty": "Infectious Disease",
        "urgency": "SOON",
        "patient_name": "Darius Washington",
        "patient_dob": "1973-11-08",
        "patient_sex": "Male",
        "patient_mrn": "MRN-7483920",
        "insurance": "Medicaid Managed Care",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — INFECTIOUS DISEASE
Date: 2025-11-12    Referral ID: REF-2025-083291
Urgency: SOON — Appointment within 2 weeks

TO: Infectious Disease Department
FROM: Dr. Tamara Blackwell, MD — Primary Care, NPI 3748201938
      Urban Health Associates, Phone: (555) 450-6677, Fax: (555) 450-6678

PATIENT: Darius Washington | DOB: 1973-11-08 | Age: 52 | Sex: Male
MRN: MRN-7483920 | Insurance: Medicaid Managed Care | Member ID: MC-7483920-5

REASON FOR REFERRAL: Recurrent MRSA skin infections — fourth episode in 18 months. Requires
expert management, decolonisation protocol, and assessment for underlying immunodeficiency.

CLINICAL SUMMARY:
Mr. Washington is a 52-year-old male with a history of recurrent MRSA skin and soft tissue
infections (SSTIs). Episodes: August 2024 — right thigh abscess (I&D + TMP-SMX 10 days);
November 2024 — left axillary abscess (I&D, hospital admission, IV vancomycin 5 days);
March 2025 — neck abscess (I&D + doxycycline); November 2025 (current) — recurrent right
thigh cellulitis with abscess (cultures MRSA, community-acquired, non-USA300 strain PVL+).

The PVL-positive MRSA (community strain) is concerning for household transmission and
ongoing reinfection from a nasal or skin reservoir.

Current social history: lives with partner and two children. No known healthcare worker
exposure. No IV drug use. No recent hospital stay.

HIV test: Negative (October 2025). CD4 not indicated. IgG quantification: IgG 840 mg/dL
(normal). IgA, IgM normal. Neutrophil oxidative burst assay: pending. No diabetes (HbA1c 5.4%).
Skin swabs (nares, axillae, groin): MRSA isolated from anterior nares bilaterally.

Current antibiotics: TMP-SMX DS BID for 10 days (ongoing).
Allergies: Penicillin (anaphylaxis — documented).

QUESTIONS FOR INFECTIOUS DISEASE:
1. Decolonisation protocol — mupirocin nasal, chlorhexidine body wash, household decontamination?
2. Household screening and decolonisation — partner and children?
3. Is there underlying immunodeficiency requiring further work-up?
4. Optimal antibiotic choice given penicillin anaphylaxis for future MRSA SSTIs?
5. Duration of suppressive therapy — is long-term decolonisation indicated?

PRIOR AUTHORISATION:
Auth Number: PA-447382 | Insurance: Medicaid Managed Care
Authorised for: Infectious disease consultation and decolonisation assessment

Referring Physician: Dr. Tamara Blackwell, MD
NPI: 3748201938 | Phone: (555) 450-6677 | Fax Results To: (555) 450-6678
""",
    },
    {
        "referral_id": "REF-2025-084182",
        "specialty": "Allergy/Immunology",
        "urgency": "ROUTINE",
        "patient_name": "Claire Nguyen",
        "patient_dob": "1996-04-03",
        "patient_sex": "Female",
        "patient_mrn": "MRN-2847391",
        "insurance": "BlueCross BlueShield PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — ALLERGY / IMMUNOLOGY
Date: 2025-11-14    Referral ID: REF-2025-084182
Urgency: ROUTINE — Appointment within 4 weeks

TO: Allergy & Immunology Department
FROM: Dr. Rebecca Stone, MD — Respiratory Medicine, NPI 4829301748
      Respiratory Health Partners, Phone: (555) 560-7788, Fax: (555) 560-7789

PATIENT: Claire Nguyen | DOB: 1996-04-03 | Age: 29 | Sex: Female
MRN: MRN-2847391 | Insurance: BlueCross BlueShield PPO | Member ID: BS-2847391-6

REASON FOR REFERRAL: Poorly controlled allergic asthma (Step 3, uncontrolled) and suspected
Hymenoptera venom allergy following local large reaction after wasp sting. Requesting allergen
testing, asthma phenotyping, and venom allergy evaluation.

CLINICAL SUMMARY:
Ms. Nguyen is a 29-year-old female with a 12-year history of atopic asthma and allergic
rhinitis. Despite step 3 therapy (fluticasone/formoterol 250/10 BID + montelukast 10mg QD),
asthma remains poorly controlled — ACQ-6 score 2.4 (uncontrolled). Two ED visits in the past
12 months for acute exacerbations, both requiring systemic corticosteroids.

Three weeks ago, she suffered a wasp sting on her left forearm with a large local reaction
(15cm erythema and induration, persisting >24h). No systemic symptoms on this occasion. She
reports a previous sting 2 years ago that caused urticaria (generalised), throat tightness,
and required a single dose of IM adrenaline in primary care. The risk of venom anaphylaxis
is therefore considered significant.

Spirometry: FEV1 78% predicted | FVC 96% | FEV1/FVC 0.68 | BD response +16% (significant).
FeNO: 62 ppb (markedly elevated — T2/eosinophilic inflammation). Blood eosinophils 0.72×10⁹/L.
Total IgE: 485 IU/mL. Allergen sensitisation screen (RAST): grass pollen +++, cat dander ++,
HDM ++, wasp venom (Vespula) +++ (sIgE 8.4 kUA/L).

No epinephrine auto-injector (EAI) currently prescribed. Lives alone. Outdoor occupation (park ranger).

Allergies: Aspirin (urticaria and bronchospasm — not to be given).

QUESTIONS FOR ALLERGY / IMMUNOLOGY:
1. Venom-specific immunotherapy (VIT) — eligibility, target venom, duration?
2. Prescribe epinephrine auto-injector and action plan pending VIT?
3. Asthma phenotyping — eligibility for biologic therapy (dupilumab, benralizumab)?
4. Step up asthma therapy while awaiting biologic assessment?
5. Skin prick testing and component-resolved diagnosis for venom allergy?

PRIOR AUTHORISATION:
Auth Number: PA-556493 | Insurance: BlueCross BlueShield PPO
Authorised for: Allergy/immunology consultation and allergen testing

Referring Physician: Dr. Rebecca Stone, MD
NPI: 4829301748 | Phone: (555) 560-7788 | Fax Results To: (555) 560-7789
""",
    },
    {
        "referral_id": "REF-2025-085093",
        "specialty": "Sleep Medicine",
        "urgency": "ROUTINE",
        "patient_name": "Marcus Jefferson",
        "patient_dob": "1968-07-19",
        "patient_sex": "Male",
        "patient_mrn": "MRN-3920485",
        "insurance": "Humana HMO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — SLEEP MEDICINE
Date: 2025-11-17    Referral ID: REF-2025-085093
Urgency: ROUTINE — Appointment within 4-6 weeks

TO: Sleep Medicine Department, Sleep Disorders Centre
FROM: Dr. Andrew Collins, MD — Primary Care, NPI 5839201746
      Midtown Family Medicine, Phone: (555) 670-8899, Fax: (555) 670-8900

PATIENT: Marcus Jefferson | DOB: 1968-07-19 | Age: 57 | Sex: Male
MRN: MRN-3920485 | Insurance: Humana HMO | Member ID: HM-3920485-7

REASON FOR REFERRAL: Suspected obstructive sleep apnoea (OSA) — Epworth Sleepiness Scale 14,
BMI 34, witnessed apnoeas, and poorly controlled hypertension. Requesting polysomnography and
management initiation.

CLINICAL SUMMARY:
Mr. Jefferson is a 57-year-old male presenting with a 3-year history of progressive daytime
somnolence, loud habitual snoring, and witnessed apnoeas reported by his wife. He frequently
falls asleep at the wheel (near-miss incident 3 months ago — reported to referring physician)
and while watching television. He reports waking unrefreshed and experiencing morning headaches.

Epworth Sleepiness Scale: 14/24 (abnormal — threshold >10). STOP-BANG score: 6/8 (HIGH risk).
BP: 158/96 mmHg — poorly controlled despite three antihypertensives (Amlodipine 10mg, Lisinopril
40mg, HCTZ 25mg). Neck circumference: 44cm (>40cm — risk factor). BMI: 34.1, weight 108kg.
Oxygen saturation at rest: 96%. No cor pulmonale on CXR.

ECG: Normal sinus rhythm, no LVH pattern. Echo (18 months ago): EF 62%, no significant
valve disease, mild LV diastolic dysfunction.

Comorbidities: HTN (as above), T2DM (HbA1c 7.4%), GORD (Omeprazole 20mg QD), depression
(Sertraline 100mg QD — causes sedation, may contribute to daytime sleepiness).

The near-miss driving incident raises a fitness-to-drive concern that requires urgent sleep
assessment documentation.

Allergies: Sulfonamides (rash). No CPAP experience.

QUESTIONS FOR SLEEP MEDICINE:
1. Overnight polysomnography or home sleep apnoea test (HSAT) — which is appropriate first?
2. If OSA confirmed: CPAP initiation, auto-titration, or fixed pressure?
3. Will CPAP therapy improve blood pressure control?
4. Fitness to drive assessment — pending PSG results?
5. Role of positional therapy given body habitus?

PRIOR AUTHORISATION:
Auth Number: PA-665584 | Insurance: Humana HMO
Authorised for: Sleep medicine consultation and overnight sleep study

Referring Physician: Dr. Andrew Collins, MD
NPI: 5839201746 | Phone: (555) 670-8899 | Fax Results To: (555) 670-8900
""",
    },
    {
        "referral_id": "REF-2025-086284",
        "specialty": "General Surgery",
        "urgency": "URGENT",
        "patient_name": "Brigitte Marceau",
        "patient_dob": "1964-01-14",
        "patient_sex": "Female",
        "patient_mrn": "MRN-4839201",
        "insurance": "Aetna Commercial",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — GENERAL SURGERY
Date: 2025-11-19    Referral ID: REF-2025-086284
Urgency: URGENT — Assessment within 48 hours

TO: General Surgery Department
FROM: Dr. Nathan Owens, MD — Emergency Medicine, NPI 6849201738
      City General Hospital ED, Phone: (555) 780-9911, Fax: (555) 780-9912

PATIENT: Brigitte Marceau | DOB: 1964-01-14 | Age: 61 | Sex: Female
MRN: MRN-4839201 | Insurance: Aetna Commercial | Member ID: AC-4839201-8

REASON FOR REFERRAL: Symptomatic cholelithiasis with recurrent biliary colic — third ED
presentation in 6 weeks. Requesting urgent surgical consultation for elective laparoscopic
cholecystectomy before progression to acute cholecystitis or choledocholithiasis.

CLINICAL SUMMARY:
Ms. Marceau is a 61-year-old female presenting with her third episode of biliary colic in
6 weeks. Episodes: right upper quadrant pain radiating to right shoulder, post-prandial,
associated with nausea and vomiting, each lasting 4-8 hours and then self-resolving. No fever.
No jaundice. No scleral icterus. Murphey's sign: negative on current presentation.

Abdominal Ultrasound (confirmed in ED, 3 weeks ago): Multiple gallstones, largest 1.8cm.
Gallbladder wall normal thickness (2mm). No pericholecystic fluid. CBD 5mm (not dilated).
No hepatic abnormality.

Current labs: WBC 9.2 (normal — no cholecystitis). Total bilirubin 0.9 (normal). ALP 88 (normal).
ALT 22, AST 19 (normal — no CBD stone/Mirizzi). Amylase 48 (normal — no pancreatitis).
CRP 12 mg/L (mildly elevated, post-pain). Haemoglobin 13.8, platelets 224 (normal).

Medical history: HTN (Perindopril 8mg QD), hypothyroidism (Levothyroxine 100mcg QD),
BMI 29.1. No prior abdominal surgery. No anticoagulation. No known bleeding disorder.
Allergies: Aspirin (bronchospasm — NSAID-exacerbated respiratory disease).

Pre-operative risk: ASA Class II. Cardiac clearance not anticipated to be required.

QUESTIONS FOR GENERAL SURGERY:
1. Schedule laparoscopic cholecystectomy — inpatient vs day-case?
2. Pre-operative MRCP or EUS to exclude CBD stone before surgery?
3. IOC (intra-operative cholangiogram) — routine or selective?
4. Any concern regarding peri-operative Levothyroxine management?
5. Preferred anaesthetic considerations given NSAID allergy (aspirin/bronchospasm)?

PRIOR AUTHORISATION:
Auth Number: PA-774693 | Insurance: Aetna Commercial
Authorised for: Urgent surgical consultation and laparoscopic cholecystectomy

Referring Physician: Dr. Nathan Owens, MD
NPI: 6849201738 | Phone: (555) 780-9911 | Fax Results To: (555) 780-9912
""",
    },
    {
        "referral_id": "REF-2025-087193",
        "specialty": "Ophthalmology",
        "urgency": "SOON",
        "patient_name": "Benjamin Oduya",
        "patient_dob": "1953-05-28",
        "patient_sex": "Male",
        "patient_mrn": "MRN-5948302",
        "insurance": "Medicare Advantage — AARP",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — OPHTHALMOLOGY
Date: 2025-11-21    Referral ID: REF-2025-087193
Urgency: SOON — Appointment within 2-3 weeks

TO: Ophthalmology Department, Eye Care Centre
FROM: Dr. Linda Kamara, MD — Primary Care / Geriatrics, NPI 7849201837
      Senior Wellness Group, Phone: (555) 890-1122, Fax: (555) 890-1123

PATIENT: Benjamin Oduya | DOB: 1953-05-28 | Age: 72 | Sex: Male
MRN: MRN-5948302 | Insurance: Medicare Advantage — AARP | Member ID: MA-5948302-9

REASON FOR REFERRAL: Bilateral cataracts with significantly reduced visual acuity (6/18 bilateral).
Functional impairment affecting activities of daily living and driving. Requesting ophthalmology
assessment for phacoemulsification and IOL implantation.

CLINICAL SUMMARY:
Mr. Oduya is a 72-year-old male who has reported progressive visual decline over 3 years.
He describes difficulty reading, driving at night (significant glare and halos), and trouble
recognising faces. He had a minor road traffic incident 6 months ago attributed to impaired
vision. He no longer drives after dark.

Vision assessment in primary care today:
- Right eye: VA 6/18 with best correction. No pinhole improvement.
- Left eye: VA 6/18 with best correction. No pinhole improvement.

Ophthalmoscopic exam: Bilateral dense posterior subcapsular cataracts (right > left).
No view of fundus due to cataract density. IOPs: Right 14mmHg, Left 13mmHg (assessed by
non-contact tonometry).

Medical history: T2DM (HbA1c 7.6% — note: increased surgical infection risk, advise pre-op
optimisation if possible), HTN (Amlodipine 10mg, Valsartan 160mg QD), dyslipidaemia
(Simvastatin 40mg QHS).

Medications: Tamsulosin 0.4mg QD (alpha-1A antagonist — intra-operative floppy iris syndrome
risk, IMPORTANT — inform surgeon). Aspirin 81mg QD (discuss peri-operative management).
Allergies: Sulfonamides (Stevens-Johnson syndrome — SEVERE, document prominently).

QUESTIONS FOR OPHTHALMOLOGY:
1. Confirm bilateral cataract diagnosis and surgical eligibility?
2. IOL selection — standard vs premium (toric given astigmatism TBD at pre-op biometry)?
3. Staged bilateral surgery — which eye first, interval?
4. Intra-operative floppy iris syndrome management plan (Tamsulosin)?
5. Post-operative diabetic retinopathy screening plan once fundal view restored?

PRIOR AUTHORISATION:
Auth Number: PA-883794 | Insurance: Medicare Advantage — AARP
Authorised for: Ophthalmology consultation and bilateral cataract extraction planning

Referring Physician: Dr. Linda Kamara, MD
NPI: 7849201837 | Phone: (555) 890-1122 | Fax Results To: (555) 890-1123
""",
    },
    {
        "referral_id": "REF-2025-088294",
        "specialty": "ENT",
        "urgency": "ROUTINE",
        "patient_name": "Alicia Romero",
        "patient_dob": "1977-09-11",
        "patient_sex": "Female",
        "patient_mrn": "MRN-6039281",
        "insurance": "UnitedHealthcare Select",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — EAR, NOSE & THROAT (ENT) / RHINOLOGY
Date: 2025-11-24    Referral ID: REF-2025-088294
Urgency: ROUTINE — Appointment within 4-6 weeks

TO: ENT / Rhinology Department
FROM: Dr. James Osei, MD — Primary Care, NPI 8940201837
      Community Health Partners, Phone: (555) 900-2233, Fax: (555) 900-2234

PATIENT: Alicia Romero | DOB: 1977-09-11 | Age: 48 | Sex: Female
MRN: MRN-6039281 | Insurance: UnitedHealthcare Select | Member ID: UH-6039281-10

REASON FOR REFERRAL: Recurrent chronic rhinosinusitis (CRS) with nasal polyps — 4 acute
exacerbations per year requiring antibiotics. Failed maximal medical therapy. Requesting ENT
evaluation for possible functional endoscopic sinus surgery (FESS).

CLINICAL SUMMARY:
Ms. Romero is a 48-year-old female with a 9-year history of CRS with nasal polyps (CRSwNP).
She experiences persistent nasal obstruction, anosmia (complete for 2 years), post-nasal drip,
facial pressure and headache, and purulent anterior rhinorrhoea. SNOT-22 score: 62/110 (severe).
She has had 4 acute exacerbations in the past 12 months, each requiring antibiotics (amoxicillin-
clavulanate or clarithromycin).

Medical therapy to date: Mometasone furoate nasal spray 200mcg BID (ongoing 4 years), saline
irrigations BD, oral prednisolone bursts x3 in 18 months (partial and short-lived improvement).
Leukotriene antagonist (Montelukast 10mg QD) added 6 months ago — no significant benefit.

CT Sinuses (3 months ago): Bilateral pansinusitis — Lund-Mackay score 18/24. Large bilateral
ethmoid polyp burden. Mild mucosal thickening maxillary sinuses. No orbital or intracranial
complications.

Comorbidities: Asthma (Step 2 — ICS; well-controlled), allergic rhinitis.
Note: Aspirin sensitivity NOT formally tested — refer for aspirin desensitisation assessment
if Samter's triad suspected (asthma + CRSwNP + aspirin sensitivity).
Allergies: No known drug allergies.

QUESTIONS FOR ENT:
1. Surgical candidacy for FESS — extent of surgery (ethmoidectomy, antrostomy, sphenoidotomy)?
2. Should aspirin desensitisation be considered (Samter's triad)?
3. Biologic therapy (dupilumab, mepolizumab) — is this patient a candidate before or instead of surgery?
4. Post-operative maintenance therapy plan?
5. Smell rehabilitation programme post-FESS?

PRIOR AUTHORISATION:
Auth Number: PA-992804 | Insurance: UnitedHealthcare Select
Authorised for: ENT consultation, nasal endoscopy, and FESS assessment

Referring Physician: Dr. James Osei, MD
NPI: 8940201837 | Phone: (555) 900-2233 | Fax Results To: (555) 900-2234
""",
    },
    {
        "referral_id": "REF-2025-089381",
        "specialty": "Transplant Nephrology",
        "urgency": "SOON",
        "patient_name": "Mei-Ling Tan",
        "patient_dob": "1969-02-07",
        "patient_sex": "Female",
        "patient_mrn": "MRN-7130492",
        "insurance": "BlueCross BlueShield HMO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — TRANSPLANT NEPHROLOGY
Date: 2025-11-26    Referral ID: REF-2025-089381
Urgency: SOON — Appointment within 2-3 weeks

TO: Transplant Nephrology / Pre-Transplant Evaluation Programme
FROM: Dr. Samuel Adeyemi, MD — Nephrology, NPI 9040201938
      Kidney Disease Associates, Phone: (555) 010-3344, Fax: (555) 010-3345

PATIENT: Mei-Ling Tan | DOB: 1969-02-07 | Age: 56 | Sex: Female
MRN: MRN-7130492 | Insurance: BlueCross BlueShield HMO | Member ID: BS-7130492-11

REASON FOR REFERRAL: CKD Stage 4 (eGFR 18 mL/min/1.73m²) approaching ESRD. Requesting
pre-transplant evaluation, listing assessment, and dialysis access planning.

CLINICAL SUMMARY:
Ms. Tan is a 56-year-old female with a 15-year history of CKD secondary to IgA nephropathy
(biopsy-confirmed 2010). Progressive decline despite optimal RAAS blockade, dietary restriction,
and anaemia management.

Current labs (this week): Creatinine 3.8 mg/dL | eGFR 18 mL/min/1.73m² (CKD Stage 4)
Potassium 5.2 mEq/L | Phosphorus 5.8 mg/dL (elevated — on phosphate binders)
Haemoglobin 9.6 g/dL (anaemia of CKD — on Epoetin alfa 10,000 units 3x/week)
Bicarbonate 18 mEq/L (metabolic acidosis — on sodium bicarbonate 650mg BID)
PTH: 248 pg/mL (secondary hyperparathyroidism) | 25-OH Vit D: 14 ng/mL (deficient)
Albumin 3.4 g/dL | BUN 68 mg/dL

Symptoms: progressive fatigue, decreased exercise tolerance, mild ankle oedema, reduced
appetite. No encephalopathy, no pericardial rub, no pulmonary oedema.

Medical history: IgA nephropathy, HTN (Amlodipine 10mg, Lisinopril 40mg), anaemia CKD,
secondary hyperparathyroidism, hypothyroidism (Levothyroxine 125mcg QD), no diabetes,
no malignancy. No prior kidney transplant. Blood group: A positive.
Allergies: Erythromycin (GI intolerance).

QUESTIONS FOR TRANSPLANT NEPHROLOGY:
1. Pre-transplant evaluation — cardiac, vascular, infectious disease, psychosocial workup?
2. Waitlist candidacy — deceased donor listing and living donor discussion?
3. Dialysis access planning — AVF creation now vs haemodialysis vs peritoneal dialysis?
4. Immunological workup — PRA, HLA typing, crossmatch?
5. Expected waiting time — expedited listing considerations for pre-emptive transplant?

PRIOR AUTHORISATION:
Auth Number: PA-101938 | Insurance: BlueCross BlueShield HMO
Authorised for: Transplant nephrology consultation and pre-transplant workup

Referring Physician: Dr. Samuel Adeyemi, MD
NPI: 9040201938 | Phone: (555) 010-3344 | Fax Results To: (555) 010-3345
""",
    },
    {
        "referral_id": "REF-2025-090284",
        "specialty": "Thoracic Surgery",
        "urgency": "URGENT",
        "patient_name": "Gerald Fitzpatrick",
        "patient_dob": "1962-12-03",
        "patient_sex": "Male",
        "patient_mrn": "MRN-8221503",
        "insurance": "BCBS Federal Employee",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — THORACIC SURGERY
Date: 2025-11-28    Referral ID: REF-2025-090284
Urgency: URGENT — Seen within 1 week

TO: Thoracic Surgery Department, Lung Cancer Programme
FROM: Dr. Patricia Nkemdirim, MD — Pulmonology / Oncology, NPI 1140301948
      Thoracic Oncology Associates, Phone: (555) 120-4455, Fax: (555) 120-4456

PATIENT: Gerald Fitzpatrick | DOB: 1962-12-03 | Age: 63 | Sex: Male
MRN: MRN-8221503 | Insurance: BCBS Federal Employee | Member ID: BE-8221503-12

REASON FOR REFERRAL: Solitary pulmonary nodule 2.1cm, left upper lobe, PET-avid (SUVmax 6.8),
no distant metastases on staging. Likely Stage IA2 NSCLC. Surgical consultation for curative
intent lobectomy.

CLINICAL SUMMARY:
Mr. Fitzpatrick is a 63-year-old male, 40 pack-year smoker (currently smoking — cessation
counselled), identified on low-dose CT lung cancer screening. Follow-up CT showed interval
growth from 1.4cm (March 2025) to 2.1cm (October 2025). Nodule: solid, spiculated, left
upper lobe, upper division subsegment.

PET-CT (3 weeks ago): LUL nodule SUVmax 6.8 (highly metabolically active). No hilar or
mediastinal adenopathy (N0). No distant metastasis. Stage: cT1cN0M0 (Stage IA2 — 8th edition).

CT-guided needle biopsy (last week): Adenocarcinoma, acinar-predominant. PD-L1: 45%. EGFR: wild-type.
ALK/ROS1: negative. KRAS G12C mutation detected. Molecular profile confirmed. No targetable
driver mutation appropriate for adjuvant TKI at this stage.

Pulmonary function: FEV1 72% predicted | DLCO 68% | FVC 88% — adequate for lobectomy.
6MWT: 420m (adequate physiological reserve). CPET: VO2 max 16.2 mL/kg/min (borderline).
Echocardiogram: EF 60%, no significant valve disease. Exercise ECG: no ischaemia.

Comorbidities: COPD (moderate), HTN (Amlodipine 10mg QD), dyslipidaemia (Rosuvastatin 20mg QD).
Allergies: Penicillin (rash).

QUESTIONS FOR THORACIC SURGERY:
1. VATS lobectomy (left upper lobe) vs RATS vs open — approach decision based on anatomy?
2. Is mediastinal staging (EBUS/mediastinoscopy) required given PET-negative mediastinum?
3. CPET borderline result — is patient safe for lobectomy vs sub-lobar resection (segmentectomy)?
4. Adjuvant chemotherapy indication (Stage IA2 — borderline, discuss with MDT)?
5. Post-operative smoking cessation plan?

PRIOR AUTHORISATION:
Auth Number: PA-212048 | Insurance: BCBS Federal Employee
Authorised for: Thoracic surgery consultation and lobectomy surgical planning

Referring Physician: Dr. Patricia Nkemdirim, MD
NPI: 1140301948 | Phone: (555) 120-4455 | Fax Results To: (555) 120-4456
""",
    },
    {
        "referral_id": "REF-2025-091375",
        "specialty": "Dermatology",
        "urgency": "SOON",
        "patient_name": "Natasha Ivanova",
        "patient_dob": "1991-08-14",
        "patient_sex": "Female",
        "patient_mrn": "MRN-9312604",
        "insurance": "Cigna HMO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — DERMATOLOGY
Date: 2025-11-30    Referral ID: REF-2025-091375
Urgency: SOON — Appointment within 2 weeks

TO: Dermatology Department (Pigmented Lesion Clinic)
FROM: Dr. Steven Hartley, MD — Primary Care, NPI 2250401958
      North Side Family Practice, Phone: (555) 230-5566, Fax: (555) 230-5567

PATIENT: Natasha Ivanova | DOB: 1991-08-14 | Age: 34 | Sex: Female
MRN: MRN-9312604 | Insurance: Cigna HMO | Member ID: CH-9312604-13

REASON FOR REFERRAL: Suspicious pigmented skin lesion on right upper back — ABCDE criteria
positive for 3/5 features (asymmetry, irregular border, colour variegation). Requesting urgent
dermatological assessment with dermoscopy and excision biopsy if indicated.

CLINICAL SUMMARY:
Ms. Ivanova is a 34-year-old female of Eastern European descent with Fitzpatrick skin type II
(fair skin, burns easily, tans minimally). She presented noting a pigmented lesion on her right
upper back that has changed in appearance over the past 4-6 months — her partner brought this
to her attention. She reports the lesion has darkened and become irregular in shape.

ABCDE Assessment (primary care dermoscopy review):
A — Asymmetry: YES — asymmetrical shape
B — Border: YES — notched, irregular border at inferior pole
C — Colour: YES — mixed tan, dark brown, and focal black area
D — Diameter: 8mm (above 6mm threshold)
E — Evolution: YES — change in colour reported over 4-6 months

Total ABCDE positive: 3/5 (A, B, C, E positive — high clinical concern).

Skin examination: Single lesion right upper back, no satellite lesions. No palpable
regional lymphadenopathy (axillary, supraclavicular examined). No other concerning nevi.
Total body nevi count: approximately 45 (mole mapping not previously performed).

Risk factors: Family history of melanoma (maternal uncle, diagnosed age 52). Multiple
childhood sunburns reported. No prior skin biopsy or malignancy. No immunosuppression.
Not on photosensitising medications.
Allergies: None known.

QUESTIONS FOR DERMATOLOGY:
1. Dermoscopy assessment — dermoscopic criteria for malignancy?
2. Excision biopsy with 2mm margins — immediate or reflectance confocal microscopy first?
3. If melanoma confirmed — Breslow thickness, ulceration, mitotic rate, and sentinel node biopsy threshold?
4. Total body mole mapping — recommended given family history?
5. Surveillance protocol for remaining nevi?

PRIOR AUTHORISATION:
Auth Number: PA-323159 | Insurance: Cigna HMO
Authorised for: Dermatology consultation and excision biopsy

Referring Physician: Dr. Steven Hartley, MD
NPI: 2250401958 | Phone: (555) 230-5566 | Fax Results To: (555) 230-5567
""",
    },
    {
        "referral_id": "REF-2025-092467",
        "specialty": "Endocrinology (Thyroid Cancer)",
        "urgency": "SOON",
        "patient_name": "Lorraine Thibodeau",
        "patient_dob": "1974-04-26",
        "patient_sex": "Female",
        "patient_mrn": "MRN-1403715",
        "insurance": "Humana PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — ENDOCRINOLOGY (THYROID CANCER SURVEILLANCE)
Date: 2025-12-02    Referral ID: REF-2025-092467
Urgency: SOON — Appointment within 2-3 weeks

TO: Endocrinology / Thyroid Cancer Follow-Up Clinic
FROM: Dr. Owen Bradley, MD — Surgical Oncology, NPI 3360501968
      Cancer Surgical Associates, Phone: (555) 340-6677, Fax: (555) 340-6678

PATIENT: Lorraine Thibodeau | DOB: 1974-04-26 | Age: 51 | Sex: Female
MRN: MRN-1403715 | Insurance: Humana PPO | Member ID: HP-1403715-14

REASON FOR REFERRAL: Post-total thyroidectomy surveillance for papillary thyroid carcinoma
(Stage pT2N0M0) — rising serum thyroglobulin (Tg) on TSH-suppression therapy. Requesting
endocrinology assessment for recurrence evaluation and RAI eligibility.

CLINICAL SUMMARY:
Ms. Thibodeau underwent total thyroidectomy in March 2023 for papillary thyroid carcinoma
(classic variant, pT2N0M0, Stage II per 8th edition AJCC — tumour 2.2cm, clear margins,
no lymphovascular invasion, no extrathyroidal extension). Post-operatively received adjuvant
radioactive iodine (RAI 131-I 30mCi) — post-treatment scan showed no residual functioning
thyroid tissue and no metastatic uptake.

She has been on TSH-suppressive levothyroxine (TSH target <0.1 mU/L — high-risk protocol
at time of treatment). Recent serial Tg trending:
- March 2024: Tg <0.1 ng/mL (undetectable — excellent response)
- September 2024: Tg 0.4 ng/mL (detectable but low)
- March 2025: Tg 1.2 ng/mL (rising — concerning for structural recurrence)
- November 2025: Tg 3.8 ng/mL (rising — RISING despite suppression → referred urgently)

Anti-Tg antibodies: negative (confirms Tg values reliable).
TSH: 0.08 mU/L (suppressed, compliant with levothyroxine). Free T4: 1.9 ng/dL.
Neck ultrasound (last month): No definitive structural recurrence in thyroid bed. No cervical
lymphadenopathy (≥5mm). Equivocal 6mm left paratracheal node — cannot exclude recurrence.

Allergies: No known drug allergies. No iodine contrast allergy.

QUESTIONS FOR ENDOCRINOLOGY:
1. Rising Tg — is this structural recurrence or remnant? Next imaging: CT neck/chest with contrast vs
   rhTSH-stimulated Tg/RAI whole body scan?
2. Is re-treatment with RAI appropriate if occult recurrence identified?
3. Should TSH suppression target be maintained, relaxed, or intensified?
4. Neck ultrasound-guided FNA of the equivocal paratracheal node?
5. If distant metastasis — systemic therapy options (lenvatinib, sorafenib) — referral pathway?

PRIOR AUTHORISATION:
Auth Number: PA-434260 | Insurance: Humana PPO
Authorised for: Endocrinology consultation and thyroid cancer surveillance imaging

Referring Physician: Dr. Owen Bradley, MD
NPI: 3360501968 | Phone: (555) 340-6677 | Fax Results To: (555) 340-6678
""",
    },
    {
        "referral_id": "REF-2025-093558",
        "specialty": "Gynaecology (Oncology)",
        "urgency": "URGENT",
        "patient_name": "Eleanor Whitfield",
        "patient_dob": "1967-07-03",
        "patient_sex": "Female",
        "patient_mrn": "MRN-2514826",
        "insurance": "Medicare Advantage — Humana",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — GYNAECOLOGICAL ONCOLOGY
Date: 2025-12-04    Referral ID: REF-2025-093558
Urgency: URGENT — Seen within 1 week

TO: Gynaecological Oncology Department
FROM: Dr. Harriet Johansson, MD — Obstetrics & Gynaecology, NPI 4470601978
      Women's Health Specialists, Phone: (555) 450-7788, Fax: (555) 450-7789

PATIENT: Eleanor Whitfield | DOB: 1967-07-03 | Age: 58 | Sex: Female
MRN: MRN-2514826 | Insurance: Medicare Advantage — Humana | Member ID: MA-2514826-15

REASON FOR REFERRAL: Postmenopausal bleeding (PMB) — two episodes in 6 weeks. Endometrial
biopsy pending results. Transvaginal ultrasound shows significantly thickened endometrium.
Requesting urgent gynaecological oncology assessment to exclude endometrial carcinoma.

CLINICAL SUMMARY:
Ms. Whitfield is a 58-year-old female, 7 years post-menopause, presenting with two episodes
of painless per vaginal bleeding in the past 6 weeks (November 4 and November 28, 2025).
She is NOT on hormone replacement therapy. Bleeding volume: approximately equivalent to a
light menstrual day on each occasion. No pelvic pain. No dysuria. No bowel symptoms.

Transvaginal Ultrasound (December 2, 2025): Endometrial thickness 18mm (abnormal — threshold
>4mm post-menopause). Heterogeneous echogenicity. No intrauterine polyp definitively identified.
No free fluid in pouch of Douglas. Ovaries: postmenopausal appearance, no masses.

Endometrial Pipelle biopsy performed December 3, 2025 — specimen SENT FOR HISTOLOGY — result
expected within 5-7 days. Patient has been advised of the referral urgency.

Risk factor profile: BMI 37 (obesity — significant risk factor), nulliparous, early menarche
(age 11), never used OCP, Type 2 diabetes (HbA1c 7.8%), hypertension (Amlodipine 5mg,
Lisinopril 20mg). No personal or family history of gynaecological cancer. No BRCA status known.

Recent bloods: HbA1c 7.8% | Cr 0.9 (eGFR 72) | FBC: Hgb 11.2 (mild anaemia — likely due to
bleeding). CA-125: 28 U/mL (non-specifically elevated).
Allergies: Codeine (nausea/vomiting).

QUESTIONS FOR GYNAECOLOGICAL ONCOLOGY:
1. Please review histology results when available — endometrial sampling adequate or hysteroscopy/
   curettage required?
2. Staging workup — CT chest/abdomen/pelvis, MRI pelvis for local staging?
3. Is patient a candidate for robotic/laparoscopic hysterectomy + BSO + lymph node dissection?
4. Pre-operative cardiac/metabolic optimisation given BMI 37 and T2DM?
5. Molecular testing (MSI, MMR, POLE mutation) — Lynch syndrome assessment?

PRIOR AUTHORISATION:
Auth Number: PA-545371 | Insurance: Medicare Advantage — Humana
Authorised for: Urgent gynaecological oncology consultation and staging workup

Referring Physician: Dr. Harriet Johansson, MD
NPI: 4470601978 | Phone: (555) 450-7788 | Fax Results To: (555) 450-7789
""",
    },
    {
        "referral_id": "REF-2025-094649",
        "specialty": "Vascular",
        "urgency": "SOON",
        "patient_name": "Arthur Pemberton",
        "patient_dob": "1951-10-17",
        "patient_sex": "Male",
        "patient_mrn": "MRN-3625937",
        "insurance": "Medicare Part B + Medigap",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — VASCULAR MEDICINE / VASCULAR SURGERY
Date: 2025-12-06    Referral ID: REF-2025-094649
Urgency: SOON — Appointment within 2 weeks

TO: Vascular Surgery / Peripheral Arterial Disease Clinic
FROM: Dr. Janet Ogilvie, MD — Cardiology, NPI 5580701988
      Cardiovascular Associates, Phone: (555) 560-8899, Fax: (555) 560-8900

PATIENT: Arthur Pemberton | DOB: 1951-10-17 | Age: 74 | Sex: Male
MRN: MRN-3625937 | Insurance: Medicare Part B + Medigap | Medicare ID: 2PE-B7-3625

REASON FOR REFERRAL: Peripheral arterial disease (PAD) — bilateral lower limb claudication
limiting walking to 150 metres. ABI 0.58 (right), 0.62 (left) — moderate-to-severe PAD.
Requesting vascular assessment for revascularisation planning.

CLINICAL SUMMARY:
Mr. Pemberton is a 74-year-old male with symptomatic PAD presenting with bilateral calf
cramping on walking (claudication distance 150 metres, significantly limiting function).
Pain resolves within 5 minutes of rest. No rest pain. No tissue loss. No ulceration.
No limb colour change at rest.

ABI (ankle-brachial index) performed in clinic today:
- Right ankle/brachial: 0.58 (moderate-to-severe PAD — threshold <0.9)
- Left ankle/brachial: 0.62 (moderate PAD)
Both values consistent with haemodynamically significant disease.

Doppler waveforms: Bilateral monophasic waveforms at posterior tibial and dorsalis pedis
levels — consistent with significant proximal disease.

Risk factor profile: 45 pack-year smoker (current smoker — cessation counselled, offered
NRT), T2DM (HbA1c 8.2% — suboptimal), hypertension (Amlodipine 10mg, Perindopril 10mg),
dyslipidaemia (Atorvastatin 80mg), atrial fibrillation (Apixaban 5mg BID).
Cardiac: known CAD, previous PCI 2019 (RCA stenting) — no current symptoms of angina.

Limb examination: Bilateral femoral pulses present (reduced R>L). Popliteal: absent bilaterally.
Posterior tibial: absent bilaterally. Dorsalis pedis: absent bilaterally. No trophic changes.
Legs warm. Capillary refill <2 seconds.
Allergies: Penicillin (rash — mild).

QUESTIONS FOR VASCULAR SURGERY:
1. CT angiography or MRA to delineate disease distribution (aorto-iliac vs femoropopliteal vs tibial)?
2. Revascularisation candidacy — endovascular (angioplasty/stenting) vs surgical bypass?
3. Exercise rehabilitation programme (supervised walking — evidence-based first-line)?
4. Antiplatelet therapy — Apixaban already on board — should aspirin be added (dual pathway risk)?
5. Smoking cessation — varenicline or bupropion in the context of cardiovascular disease?

PRIOR AUTHORISATION:
Auth Number: PA-656482 | Insurance: Medicare Part B + Medigap
Authorised for: Vascular consultation and lower limb arterial imaging

Referring Physician: Dr. Janet Ogilvie, MD
NPI: 5580701988 | Phone: (555) 560-8899 | Fax Results To: (555) 560-8900
""",
    },
    {
        "referral_id": "REF-2025-095740",
        "specialty": "Cardiothoracic Surgery",
        "urgency": "EMERGENCY",
        "patient_name": "Victor Salazar",
        "patient_dob": "1959-05-24",
        "patient_sex": "Male",
        "patient_mrn": "MRN-4736048",
        "insurance": "Aetna PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — CARDIOTHORACIC SURGERY — EMERGENCY
Date: 2025-12-08    Referral ID: REF-2025-095740
Urgency: EMERGENCY — Immediate operative assessment required

TO: On-Call Cardiothoracic Surgery / Aortic Emergency Team
FROM: Dr. Marco Esposito, MD — Emergency Medicine / Critical Care, NPI 6690802098
      University Hospital Emergency Department, Phone: (555) 670-9911 (ED Direct)

PATIENT: Victor Salazar | DOB: 1959-05-24 | Age: 66 | Sex: Male
MRN: MRN-4736048 | Insurance: Aetna PPO | Member ID: AP-4736048-16

REASON FOR REFERRAL: ACUTE TYPE A AORTIC DISSECTION — CT AORTOGRAM CONFIRMED.
EMERGENCY SURGICAL REPAIR REQUIRED. Patient is in resuscitation bay, haemodynamically
marginal. IMMEDIATE CARDIOTHORACIC SURGICAL RESPONSE REQUESTED.

CLINICAL SUMMARY:
Mr. Salazar is a 66-year-old male presenting via ambulance with sudden-onset, severe tearing
chest pain radiating to the interscapular region, onset approximately 2 hours ago. Initial BP:
210/118 (right arm), 168/104 (left arm) — significant differential. HR 108, irregular.
SpO2: 92% on 15L oxygen via non-rebreather mask.

CT AORTOGRAM (completed 35 minutes ago — CONFIRMED):
Type A aortic dissection — intimal tear at aortic root, extending to the descending thoracic
aorta at the level of T8. Ascending aortic diameter: 5.8cm. Pericardial effusion — small, no
tamponade physiology on CT (echo confirmed below). True and false lumen identified.
No right coronary artery involvement on CT. No carotid artery involvement.
No evidence of contained rupture. Right pleural effusion (haemothorax — small).

BEDSIDE ECHO (ED physician performed): Aortic root 4.9cm. Small pericardial effusion without
tamponade. Moderate AI seen on colour Doppler. EF estimated 45% (mildly reduced).

EKG: Atrial fibrillation with rapid ventricular response (HR 108). No ST-elevation. No PR changes.
Troponin T: 84 ng/L (mildly elevated — likely demand ischaemia / type 2 MI).
Labs: Cr 1.4, Hgb 13.2, INR 1.1, Plt 188. Type and screen SENT — 4 units pRBC on order.

Active management: IV Labetalol infusion targeting SBP 100-120mmHg. IV morphine 4mg boluses
for pain. Anaesthesia team notified. ICU bed confirmed. Patient NBM. Two large-bore IVs + arterial
line right radial. Foley catheter inserted.

ACTIONS REQUIRED FROM CARDIOTHORACIC SURGERY:
1. IMMEDIATE bedside assessment for emergent surgical repair
2. Operative consent — patient alert and lucid (capacity confirmed by ED consultant)
3. Cardiac anaesthesia team notification — urgent
4. Heparin hold decision pre-operatively

Referring Physician: Dr. Marco Esposito, MD
NPI: 6690802098 | Phone: ED Direct (555) 670-9911
""",
    },
    {
        "referral_id": "REF-2025-096831",
        "specialty": "Infectious Disease",
        "urgency": "ROUTINE",
        "patient_name": "Hannah MacLeod",
        "patient_dob": "1984-03-19",
        "patient_sex": "Female",
        "patient_mrn": "MRN-5847159",
        "insurance": "Cigna PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — INFECTIOUS DISEASE (LATENT TB)
Date: 2025-12-10    Referral ID: REF-2025-096831
Urgency: ROUTINE — Appointment within 4 weeks

TO: Infectious Disease / TB Clinic
FROM: Dr. Claire Henderson, MD — Occupational Health / Primary Care, NPI 7700902108
      Riverside Occupational Health, Phone: (555) 780-0011, Fax: (555) 780-0012

PATIENT: Hannah MacLeod | DOB: 1984-03-19 | Age: 41 | Sex: Female
MRN: MRN-5847159 | Insurance: Cigna PPO | Member ID: CP-5847159-17

REASON FOR REFERRAL: Latent TB infection (LTBI) — positive IGRA (QuantiFERON-TB Gold Plus)
on occupational health screening. No active TB. Requesting infectious disease assessment for
treatment eligibility and INH prophylaxis protocol.

CLINICAL SUMMARY:
Ms. MacLeod is a 41-year-old female healthcare worker (registered nurse, ICU) who underwent
routine annual TB screening as part of her occupational health programme. Previous TST (2022):
negative. This year's IGRA (QuantiFERON-TB Gold Plus): POSITIVE — TB1 antigen response 0.84 IU/mL,
TB2 antigen response 1.12 IU/mL (both above 0.35 IU/mL threshold).

She has no symptoms of active TB: no cough, no haemoptysis, no unexplained weight loss, no
fever, no night sweats, no fatigue. General health is excellent.

Chest X-ray (December 8, 2025): No active pulmonary disease. No apical shadowing. No lymphadenopathy.
No calcified granulomata. Normal CXR — active TB excluded.

Risk factor history: Born in the UK, Caucasian. No TB contact identified outside the work
environment. No recent travel to high-prevalence countries. Not immunocompromised. No HIV.
No diabetes. Not pregnant (LMP 3 weeks ago, regular cycle, not planning pregnancy currently).
No prior BCG vaccination documented. No prior TB treatment.

Baseline labs: LFTs normal (ALT 18, AST 14, ALP 72, bilirubin 0.6). FBC normal.
Renal function normal (eGFR 94). No peripheral neuropathy symptoms.
Allergies: None known.

QUESTIONS FOR INFECTIOUS DISEASE:
1. Confirm LTBI diagnosis and treatment indication (occupational exposure risk)?
2. INH 6-month prophylaxis (6H) vs 3HP (rifapentine + INH weekly x12) — which regimen preferred?
3. Pyridoxine (B6) 25mg QD with INH — standard addition?
4. Monitoring plan — LFTs at baseline, 1 month, 3 months?
5. Occupational implications — return to ICU work during treatment?

PRIOR AUTHORISATION:
Auth Number: PA-767593 | Insurance: Cigna PPO
Authorised for: Infectious disease consultation and LTBI treatment initiation

Referring Physician: Dr. Claire Henderson, MD
NPI: 7700902108 | Phone: (555) 780-0011 | Fax Results To: (555) 780-0012
""",
    },
    {
        "referral_id": "REF-2025-097922",
        "specialty": "Palliative Care",
        "urgency": "ROUTINE",
        "patient_name": "Edmund Carlisle",
        "patient_dob": "1947-02-11",
        "patient_sex": "Male",
        "patient_mrn": "MRN-6958260",
        "insurance": "Medicare Part B",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — PALLIATIVE CARE / SUPPORTIVE MEDICINE
Date: 2025-12-12    Referral ID: REF-2025-097922
Urgency: ROUTINE — Appointment within 4 weeks (not an emergency)

TO: Palliative Care & Supportive Medicine Team
FROM: Dr. Caitlin Byrne, MD — Pulmonology, NPI 8811002218
      Respiratory & COPD Clinic, Phone: (555) 890-1133, Fax: (555) 890-1134

PATIENT: Edmund Carlisle | DOB: 1947-02-11 | Age: 78 | Sex: Male
MRN: MRN-6958260 | Insurance: Medicare Part B | Medicare ID: 3CA-B8-6958

REASON FOR REFERRAL: End-stage COPD (GOLD Stage IV, FEV1 22%) with multiple recent
hospitalisations, declining performance status, and significant symptom burden. Goals of
care discussion and advance care planning. Palliative symptom management optimisation.

CLINICAL SUMMARY:
Mr. Carlisle is a 78-year-old male with a 25-year history of COPD, former 60 pack-year smoker
(quit 10 years ago). His disease has been on a relentless decline trajectory. He was hospitalised
4 times in the past 12 months for acute exacerbations — two requiring ICU-level NIV.

PULMONARY FUNCTION (last performed 4 months ago, limited cooperation):
FEV1: 22% predicted | FEV1/FVC: 0.38 | DLCO: 24% (severely reduced)
Post-bronchodilator response: minimal (<5% change)

Current functional status: Housebound. Dyspnoeic at rest (mMRC grade 4). Cannot dress
independently. Sleeps in recliner chair due to orthopnoea. CAT score: 32 (extremely high).
Oxygen: Home O2 3L/min continuous, home NIV (BiPAP) nightly.

Current maximum therapy: Tiotropium, Indacaterol/glycopyrronium/mometasone, Albuterol nebuliser
PRN, oral morphine 2.5mg PRN for dyspnoea (commenced 1 month ago — good effect), Prednisolone
5mg maintenance. Roflumilast 500mcg QD.

Comorbidities: Ischaemic heart disease (EF 40%, stable — Bisoprolol, Ramipril, Furosemide),
atrial fibrillation (Digoxin, Apixaban), T2DM (insulin), depression (Sertraline 50mg QD).
BMI 19.2 (cachectic — weight loss 8kg over 12 months).

Patient's expressed wishes (documented in recent clinic visit): He does not wish further ICU
admissions or mechanical ventilation. He expressed a preference for "comfort-focused care."
Family (wife, two adult children) are aware. Advance directive not yet formally completed.

Allergies: Morphine — tolerated but causes nausea (manage with antiemetic); no allergy.

QUESTIONS FOR PALLIATIVE CARE:
1. Goals of care documentation — advance directive, POLST/MOLST completion?
2. Optimise dyspnoea management — titrate oral morphine, add midazolam PRN?
3. Nutritional support — dietitian referral, appetite stimulants?
4. Hospice referral eligibility assessment — prognosis <6 months?
5. Psychological support for patient and family?

PRIOR AUTHORISATION:
Auth Number: PA-878704 | Insurance: Medicare Part B
Authorised for: Palliative care consultation and advance care planning

Referring Physician: Dr. Caitlin Byrne, MD
NPI: 8811002218 | Phone: (555) 890-1133 | Fax Results To: (555) 890-1134
""",
    },
    {
        "referral_id": "REF-2025-099013",
        "specialty": "Orthopaedics (Spine)",
        "urgency": "SOON",
        "patient_name": "Simone Bergmann",
        "patient_dob": "1982-12-29",
        "patient_sex": "Female",
        "patient_mrn": "MRN-7069371",
        "insurance": "BlueCross PPO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — ORTHOPAEDIC SURGERY (SPINE)
Date: 2025-12-14    Referral ID: REF-2025-099013
Urgency: SOON — Appointment within 2-3 weeks

TO: Spinal Surgery / Orthopaedics Department
FROM: Dr. Mark Szymanski, MD — Primary Care, NPI 9921102328
      Gateway Primary Care, Phone: (555) 900-2244, Fax: (555) 900-2245

PATIENT: Simone Bergmann | DOB: 1982-12-29 | Age: 43 | Sex: Female
MRN: MRN-7069371 | Insurance: BlueCross PPO | Member ID: BP-7069371-19

REASON FOR REFERRAL: L4-L5 disc herniation with left-sided L5 radiculopathy — 6 weeks of
conservative management (physiotherapy, NSAIDs, nerve root block x1) without adequate
improvement. Requesting spine orthopaedic evaluation for surgical consideration.

CLINICAL SUMMARY:
Ms. Bergmann is a 43-year-old female presenting with a 10-week history of left-sided low back
pain with radiation down the posterior left thigh and lateral left calf to the dorsum of the
foot — typical L5 dermatomal distribution. Onset was acute lifting injury at work.

Pain severity: VAS 7/10 (back), 8/10 (leg — worse than back). The leg pain dominates.

Neurological examination today:
- Left knee extension: MRC 5/5 (intact)
- Left great toe dorsiflexion: MRC 3/5 (WEAK — L5 myotome deficit)
- Left ankle eversion: MRC 4-/5 (mildly weak — L5/S1)
- Sensation: Reduced light touch, dorsum of left foot and first web space
- Left ankle reflex: 2+ (intact). Left knee reflex: 2+ (intact)
- Straight leg raise (SLR): Positive at 35 degrees left (strongly positive — root tension sign)
- Crossed SLR: Negative

MRI Lumbar Spine (6 weeks ago): Large left paracentral and foraminal disc herniation at L4-L5
with moderate left lateral recess stenosis and contact with the traversing L5 nerve root.
No epidural abscess. No cord compression (conus at L1). No high-grade canal stenosis.

Conservative management to date (all completed):
- Physiotherapy: 8 sessions (core stability, neural mobilisation) — minimal improvement
- NSAIDs: Naproxen 500mg BID x6 weeks — partial pain relief only
- Fluoroscopy-guided left L4-L5 transforaminal ESI: performed 3 weeks ago — inadequate response

No red flag symptoms: No bladder/bowel dysfunction, no saddle anaesthesia, no fever.
Medical history: Hypothyroidism (Levothyroxine 75mcg QD, TSH normal). BMI 24.1.
Allergies: Sulfonamides (rash).

QUESTIONS FOR SPINE ORTHOPAEDICS:
1. Surgical candidacy — microdiscectomy L4-L5 given failed conservative therapy x6 weeks?
2. Any further imaging required (CT myelogram vs updated MRI)?
3. Timeline expectations — does neurological deficit (great toe weakness) indicate expedited surgery?
4. TLIF or MISS (minimally invasive spine surgery) approach — candidacy assessment?
5. Return to work planning (desk-based work, sedentary job)?

PRIOR AUTHORISATION:
Auth Number: PA-989815 | Insurance: BlueCross PPO
Authorised for: Spine orthopaedics consultation and surgical assessment

Referring Physician: Dr. Mark Szymanski, MD
NPI: 9921102328 | Phone: (555) 900-2244 | Fax Results To: (555) 900-2245
""",
    },
    {
        "referral_id": "REF-2025-100104",
        "specialty": "General Surgery (Colorectal)",
        "urgency": "SOON",
        "patient_name": "Kwame Asante",
        "patient_dob": "1976-08-06",
        "patient_sex": "Male",
        "patient_mrn": "MRN-8180482",
        "insurance": "UnitedHealthcare HMO",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — GENERAL SURGERY (COLORECTAL)
Date: 2025-12-16    Referral ID: REF-2025-100104
Urgency: SOON — Appointment within 2 weeks

TO: Colorectal Surgery / General Surgery Department
FROM: Dr. Louise Pemberton, MD — Gastroenterology, NPI 1031202438
      Digestive Health Associates, Phone: (555) 010-3355, Fax: (555) 010-3356

PATIENT: Kwame Asante | DOB: 1976-08-06 | Age: 49 | Sex: Male
MRN: MRN-8180482 | Insurance: UnitedHealthcare HMO | Member ID: UH-8180482-20

REASON FOR REFERRAL: Colonoscopy-identified 2cm rectal polyp at 8cm from anal verge —
sessile morphology, Paris classification IIa (flat elevated). Endoscopic resection not
performed (size and location — felt to require surgical assessment). Requesting colorectal
surgery evaluation for endoscopic mucosal resection (EMR) or surgical polypectomy.

CLINICAL SUMMARY:
Mr. Asante is a 49-year-old male who presented for diagnostic colonoscopy following 3 months
of intermittent rectal bleeding (bright red blood per rectum, mixed with stool, no pain).
Colonoscopy was performed last week by our gastroenterology unit.

COLONOSCOPY FINDINGS (December 9, 2025):
- Rectal polyp: 2.0cm, sessile, Paris IIa (flat elevated), at 8cm from anal verge, on posterior
  wall. Narrow-band imaging (NBI): Kudo pit pattern IV (tubulo-villous — intermediate risk).
  Lesion crossed two haustral folds — tattooed in 3 quadrants. Biopsy taken.
- Remainder of colon: 3 diminutive (<5mm) hyperplastic polyps (sigmoid) — removed.
  No diverticulosis. No additional significant lesions.

PATHOLOGY (rectal polyp biopsy): Tubulovillous adenoma with low-grade dysplasia. No high-grade
dysplasia or invasive carcinoma on biopsy sample (note: biopsy may under-sample).

CT Abdomen/Pelvis (ordered post-colonoscopy to assess for lymphadenopathy): No peri-rectal
adenopathy. No distant metastasis. No other intra-abdominal pathology. Normal.

Rectal MRI: Not yet performed — requested in this referral for preoperative staging if polyp
is concerning for submucosal invasion.

Family history: Father with colon cancer aged 62 — increased risk. Recommends Lynch syndrome
assessment.
Personal history: No prior colonoscopy. No IBD. No prior colorectal surgery.

Labs: HbA1c 5.9% (normal), eGFR 88, FBC normal, CEA 2.1 ng/mL (normal).
Allergies: None known.

QUESTIONS FOR COLORECTAL SURGERY:
1. Is endoscopic mucosal resection (EMR) by experienced endoscopist feasible vs transanal
   minimally invasive surgery (TAMIS) vs formal anterior resection?
2. Should MRI rectum be performed pre-operatively to exclude T1 submucosal invasion?
3. If low-grade TVA only (no invasion confirmed): observation vs resection?
4. Lynch syndrome testing — MMR IHC on the biopsy — please request if not done?
5. Post-resection surveillance colonoscopy interval?

PRIOR AUTHORISATION:
Auth Number: PA-100926 | Insurance: UnitedHealthcare HMO
Authorised for: Colorectal surgery consultation and rectal polyp resection planning

Referring Physician: Dr. Louise Pemberton, MD
NPI: 1031202438 | Phone: (555) 010-3355 | Fax Results To: (555) 010-3356
""",
    },

    # ── NEW BALANCED ADDITIONS (refs 17–20): young patient, EMERGENCY, paediatric, rehab ──

    {
        "referral_id": "REF-2025-071384",
        "specialty": "Obstetrics & Maternal-Fetal Medicine",
        "urgency": "SOON",
        "patient_name": "Priya Sharma",
        "patient_dob": "1999-04-12",
        "patient_sex": "Female",
        "patient_mrn": "MRN-6173829",
        "insurance": "Medicaid",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — OBSTETRICS / MATERNAL-FETAL MEDICINE
Date: 2025-10-03    Referral ID: REF-2025-071384
Urgency: SOON — within 1 week

TO: Maternal-Fetal Medicine / High-Risk Obstetrics
FROM: Dr. Janet Osei, MD — Family Medicine / Primary Care, NPI 5829301746

PATIENT: Priya Sharma | DOB: 1999-04-12 | Age: 26 | Sex: Female
MRN: MRN-6173829 | Insurance: Medicaid

REASON FOR REFERRAL: First trimester — 11 weeks gestation. High-risk preeclampsia screen positive
(combined algorithm risk 1:48). Requesting MFM evaluation and aspirin prophylaxis initiation.

CLINICAL SUMMARY:
Ms. Sharma is a 26-year-old primigravida at 11+2 weeks gestation. First-trimester combined risk
screening for preterm preeclampsia was performed using the FMF algorithm (MAP, UtA-PI, PAPP-A,
PlGF). Combined risk: 1:48 (>1:100 threshold). Nulliparity, South Asian ethnicity, and BMI 32
are additional risk factors.

BP at booking: 122/78 mmHg. Urine dipstick: negative. Renal function normal.
No history of autoimmune disease, diabetes, or chronic hypertension.

ULTRASOUND: Crown-rump length 55mm, consistent with dates. Normal fetal anatomy for gestation.
Uterine artery PI: 1.84 (elevated, >95th percentile).

MEDICATIONS: Folic acid 5mg QD. No current medications.

QUESTIONS FOR MFM:
1. Confirm high-risk status and aspirin prophylaxis (150mg nocte from 12 weeks)?
2. Additional surveillance protocol — uterine artery Dopplers, serial growth scans?
3. PlGF-based surveillance plan in third trimester?
4. Anaesthetic review timing given preeclampsia risk?

Referring Physician: Dr. Janet Osei, MD
NPI: 5829301746 | Phone: (555) 482-9300
""",
    },
    {
        "referral_id": "REF-2025-073812",
        "specialty": "Orthopaedic Surgery",
        "urgency": "EMERGENCY",
        "patient_name": "Daniel Okonkwo",
        "patient_dob": "1991-07-30",
        "patient_sex": "Male",
        "patient_mrn": "MRN-7291038",
        "insurance": "Aetna Commercial",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — ORTHOPAEDIC SURGERY — EMERGENCY
Date: 2025-10-14    Referral ID: REF-2025-073812
Urgency: EMERGENCY — Immediate surgical assessment required

TO: On-Call Orthopaedic Surgery
FROM: Dr. Amara Diallo, MD — Emergency Medicine, NPI 6293847102

PATIENT: Daniel Okonkwo | DOB: 1991-07-30 | Age: 34 | Sex: Male
MRN: MRN-7291038 | Insurance: Aetna Commercial

REASON FOR REFERRAL: Suspected acute compartment syndrome — left lower leg following
tibial fracture. 6 hours post-injury. EMERGENCY orthopaedic assessment and fasciotomy.

CLINICAL SUMMARY:
Mr. Okonkwo is a 34-year-old male presenting via ambulance following a motorbike accident at
moderate speed. Mechanism: direct impact to left lower leg. X-ray: closed mid-shaft tibial
fracture with minimal displacement.

COMPARTMENT SYNDROME SIGNS (6 HOURS POST-INJURY):
Pain: severe, disproportionate to injury — 9/10, unrelieved by IV morphine 10mg
Pain with passive stretch: markedly positive (passive dorsiflexion and toe extension)
Paresthesia: tingling in dorsum of left foot (anterior compartment)
Compartment pressures (handheld device): anterior compartment 48 mmHg, diastolic BP 78 mmHg
→ Delta-P = 30 mmHg (threshold for fasciotomy ≤30 mmHg)
Pulses: dorsalis pedis weak but present. Capillary refill 3 seconds.

Neurovascular: early anterior compartment involvement; peroneal nerve at risk.

IV ACCESS: 2x large-bore peripheral. Morphine 10mg IV given — inadequate analgesia.
IV fluid resuscitation ongoing.

ACTIONS REQUIRED:
1. EMERGENCY fasciotomy — four-compartment decompression
2. Fracture stabilisation (ex-fix vs definitive fixation at time of fasciotomy)
3. Repeat neurovascular checks q30min until theatre

Referring Physician: Dr. Amara Diallo, MD
NPI: 6293847102 | Phone: ED Direct Line (555) 911-0100
""",
    },
    {
        "referral_id": "REF-2025-076291",
        "specialty": "Paediatrics",
        "urgency": "SOON",
        "patient_name": "Ethan Clarke",
        "patient_dob": "2013-02-14",
        "patient_sex": "Male",
        "patient_mrn": "MRN-8374920",
        "insurance": "CHIP",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — PAEDIATRICS / PAEDIATRIC RESPIRATORY MEDICINE
Date: 2025-10-20    Referral ID: REF-2025-076291
Urgency: SOON — within 1-2 weeks

TO: Paediatric Respiratory Medicine
FROM: Dr. Susan Park, MD — Primary Care Paediatrics, NPI 7384920173

PATIENT: Ethan Clarke | DOB: 2013-02-14 | Age: 12 | Sex: Male
MRN: MRN-8374920 | Insurance: CHIP

REASON FOR REFERRAL: Poorly controlled asthma — 4 exacerbations requiring oral steroids
in the past 12 months. Step 3 therapy (ICS + LABA) inadequate. Requesting specialist review
for step-up and possible biologics assessment.

CLINICAL SUMMARY:
Ethan is a 12-year-old male with a 6-year history of atopic asthma (diagnosed age 6). Also has
allergic rhinitis and mild eczema. Currently on fluticasone/salmeterol 250/25 BD + salbutamol PRN.

EXACERBATIONS (PAST 12 MONTHS):
February 2025: ED visit, PO prednisolone 5 days
May 2025: ED visit, 2-day hospitalisation, IV hydrocortisone, O2 required
August 2025: GP — PO prednisolone 5 days
October 2025: ED visit this week — PO prednisolone 5 days (ongoing)

LUNG FUNCTION (spirometry last month):
FEV1: 72% predicted | FVC: 88% | FEV1/FVC: 0.68 | Bronchodilator response: +14%
FeNO: 48 ppb (elevated — eosinophilic inflammation)
Blood eosinophils: 0.58 × 10⁹/L (elevated)
Total IgE: 320 IU/mL | RAST: house dust mite +++, grass pollen ++

Trigger assessment: house dust mite primary trigger, exercise-induced component.
Inhaler technique checked — adequate.

QUESTIONS FOR PAEDIATRIC RESPIRATORY:
1. Step-up to Step 4 (high-dose ICS/LABA + LTRA) or consider biologics?
2. Eligibility for mepolizumab or dupilumab (eosinophilic phenotype, FeNO 48)?
3. Allergen immunotherapy for HDM — appropriate at age 12?
4. Structured asthma action plan revision

Referring Physician: Dr. Susan Park, MD
NPI: 7384920173 | Phone: (555) 629-4400
""",
    },
    {
        "referral_id": "REF-2025-078473",
        "specialty": "Rehabilitation Medicine",
        "urgency": "ROUTINE",
        "patient_name": "Helen Beaumont",
        "patient_dob": "1955-11-22",
        "patient_sex": "Female",
        "patient_mrn": "MRN-9283741",
        "insurance": "Medicare",
        "data_tag": "SYNTHETIC",
        "text": """REFERRAL LETTER — REHABILITATION MEDICINE / PHYSICAL MEDICINE
Date: 2025-10-28    Referral ID: REF-2025-078473
Urgency: ROUTINE — 4-6 weeks

TO: Physical Medicine & Rehabilitation
FROM: Dr. Kevin Obi, MD — Neurology, NPI 8293746102

PATIENT: Helen Beaumont | DOB: 1955-11-22 | Age: 69 | Sex: Female
MRN: MRN-9283741 | Insurance: Medicare

REASON FOR REFERRAL: Post-stroke rehabilitation needs assessment — 8 weeks post right MCA
ischaemic stroke with residual left hemiparesis and expressive aphasia. Outpatient rehab plan.

CLINICAL SUMMARY:
Mrs. Beaumont is a 69-year-old woman admitted 8 weeks ago with right MCA territory ischaemic
stroke (NIHSS 14 on admission). Treated with IV thrombolysis at 3.5 hours. MRI: right frontal
and parietal cortical infarction with involvement of Broca's area homologue. No haemorrhagic
transformation.

CURRENT NEUROLOGICAL STATUS (8 weeks post-stroke):
Motor: Left arm — proximal power MRC 3/5, distal 2/5. Left leg — MRC 4/5 (ambulatory with AFO).
Speech: Expressive aphasia — non-fluent, word-finding difficulty. Comprehension largely intact.
Cognition: MoCA 22/30 (attention, language domain deficits). No significant memory impairment.
Swallowing: FEES performed — safe with modified texture 3. Progressing towards normal diet.
ADL: Requires assistance with dressing, bathing. Independent for feeding with adapted utensils.

INPATIENT REHAB (weeks 2-6): Physical therapy, occupational therapy, speech therapy — good
engagement. Discharged to home with carer support.

CURRENT MEDICATIONS: Aspirin 75mg, atorvastatin 80mg, ramipril 5mg, metoprolol 25mg BD.
Secondary prevention risk factors: hypertension (controlled), dyslipidaemia (LDL 1.8 on statin).

GOALS: Return to independent living, communication improvement, driving assessment.

QUESTIONS FOR REHABILITATION MEDICINE:
1. Outpatient therapy intensity and modality plan (PT, OT, SLT)?
2. Constraint-induced movement therapy for left arm?
3. Aphasia therapy programme — individual vs group?
4. Driving assessment timeline and process?
5. Vocational rehabilitation — was employed part-time as librarian pre-stroke

Referring Physician: Dr. Kevin Obi, MD
NPI: 8293746102 | Phone: (555) 744-8800
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
