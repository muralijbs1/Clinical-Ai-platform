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
