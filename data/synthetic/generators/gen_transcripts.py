#!/usr/bin/env python3
"""
Generator: writes synthetic clinical SOAP notes as plain .txt files.

Run once to produce data files. Re-run to regenerate or add more notes.
Output: data/synthetic/transcripts/note_001.txt ... note_020.txt

Each file has a metadata header (key: value pairs, terminated by ---) followed
by the SOAP note text. This mirrors how real clinical notes arrive from EHR
export pipelines: plain text with a structured header block.
"""

from pathlib import Path

_OUT_DIR = Path(__file__).parent.parent / "transcripts"

_TRANSCRIPTS = [
    {
        "id": "transcript-001",
        "encounter_type": "Emergency Department",
        "condition": "NSTEMI / Acute Coronary Syndrome",
        "icd10_primary": "I21.4",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-03-14   TIME: 22:10   PROVIDER: Dr. Sandra Okoye, MD (Emergency Medicine)

CC: Chest pain

HPI: 64 yo M presents with 4-hour h/o substernal chest pain, onset while watching television at rest.
Pain described as pressure-like, 7/10, radiating to L jaw and L arm. Associated with diaphoresis and
mild SOB. Took 2 aspirin 325mg at home without relief. Denies syncope, palpitations, or cough.
Similar episode 2 weeks ago lasting 20 min, resolved spontaneously — did not seek care. Significant
cardiac RFs: HTN, DM2, hyperlipidemia, 35 pack-year tobacco history (quit 8 years ago), FHx of
father with MI at age 59.

ROS: Positive: CP, diaphoresis, SOB, jaw discomfort, L arm radiation.
Negative: vomiting, abdominal pain, headache, visual changes, syncope, leg swelling, fever, cough.

PMH: HTN x 14 years | Hyperlipidemia x 9 years | DM2 x 6 years | GERD

PSH: Appendectomy 2001 | Right knee arthroscopy 2014

FHx: Father: MI age 59, DM2. Mother: HTN. Brother: CAD, CABG age 62.

SHx: Retired engineer. Lives with wife. Tobacco: quit 8 years ago (35 pack-years).
Alcohol: 1-2 beers/weekend. No illicit drugs.

Meds: Lisinopril 20mg QD | Atorvastatin 40mg QHS | Metformin 1000mg BID | Omeprazole 20mg QD
      Aspirin 81mg QD (took 650mg additional at home this evening)

ALLERGIES: Sulfa drugs (rash). NKDA to reported drug classes otherwise.

OBJECTIVE:
VS: BP 162/94 | HR 98 | RR 20 | Temp 37.1°C | SpO2 95% RA | Wt 91kg | Ht 5'10"

General: Diaphoretic male, pale, holding chest, mild distress — not writhing.
HEENT: Normocephalic, atraumatic. PERRL 3mm bilat. EOMI intact. Oropharynx clear, moist.
Neck: Supple. JVD absent. Carotids 2+ without bruits. No LAD.
CV: RRR, S1/S2 normal. No murmurs, rubs, or gallops audible. Radial and DP pulses 2+ bilat.
Lungs: CTAB bilaterally. No crackles, wheezes, or rhonchi.
Abdomen: Soft, NT/ND. Normoactive BS x4. No hepatosplenomegaly.
Extremities: No clubbing, cyanosis, or edema. Capillary refill <2s.
Neuro: A&Ox3. CN II-XII grossly intact. No focal deficits.

LABS:
hs-cTnT: 0.065 ng/mL at T=0 [ELEVATED; ref <0.014]
hs-cTnT: 0.118 ng/mL at T=1h [RISING — delta 53 ng/L → meets NSTEMI rule-in]
CK-MB: 9.4 ng/mL [elevated, ref <5]
BNP: 148 pg/mL [mildly elevated, ref <100]
CBC: WBC 9.8 | Hgb 14.6 | Plt 312 [all normal]
CMP: Na 139 | K 4.2 | Cl 103 | CO2 24 | BUN 21 | Cr 1.1 | Glu 194
Lipids: TC 241 | LDL 162 | HDL 38 | TG 198 [elevated LDL, low HDL]

EKG: Sinus rhythm at 98 bpm. New T-wave inversions in V2-V4. Biphasic T-waves in V1.
No ST elevation. QTc 441ms. Compared to prior EKG (PCP 6 months ago): new anterior changes.

CXR: No acute cardiopulmonary process. Heart size upper-normal. No pulmonary oedema.
No pleural effusion. Mediastinum not widened.

ASSESSMENT:
1. Non-ST-Elevation Myocardial Infarction (NSTEMI) — I21.4
   Rising hs-cTnT with anterior T-wave changes; high pre-test probability given risk factors.
   Differential: unstable angina (less likely given troponin rise), GERD, PE (less consistent).
2. Hypertension — uncontrolled in setting of ACS stress — I10
3. Hyperlipidemia — on statin, suboptimally controlled — E78.5
4. DM2 — currently suboptimal; glucose 194 in stress setting — E11.9

PLAN:
1. NSTEMI Management:
   - Aspirin 324mg loading dose given (patient had partial home dose) — continue 81mg QD
   - Ticagrelor 180mg loading dose PO now → 90mg BID maintenance (P2Y12 inhibitor)
   - Heparin IV: bolus 60 units/kg (5,460 units) → infusion 12 units/kg/hr → PTT goal 60-100s
   - Atorvastatin uptitrated to 80mg QHS (high-intensity statin — ACS indication)
   - Hold Metformin pending cardiac catheterisation (contrast nephropathy concern)
   - Cardiology consult STAT — Dr. James Liu paged; response within 30 min
   - Admit to Cardiac Telemetry; continuous rhythm monitoring
   - Nitroglycerin 0.4mg SL q5min x3 PRN ongoing chest pain; start IV nitro drip if pain persists
   - Serial hs-cTnT at 0, 1, 3, 6h — troponin rising, confirm peak
   - Likely cardiac catheterisation within 24h (early invasive strategy for NSTEMI)

2. Hypertension:
   - Continue Lisinopril 20mg — do not hold (renoprotective, cardioprotective in ACS)

3. General:
   - NPO after midnight for likely cath AM
   - O2 via NC at 2L/min (SpO2 95% — maintain >94%)

DISPOSITION: Admitted to Cardiac Telemetry under Cardiology service. Stable condition.
""",
    },
    {
        "id": "transcript-002",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Type 2 Diabetes Follow-up",
        "icd10_primary": "E11.9",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-04-08   TIME: 10:30   PROVIDER: Dr. Maria Garcia, MD (Internal Medicine)

CC: Diabetes follow-up, medication refill

HPI: 58 yo F here for routine DM2 management, 3-month interval visit. A1c at last visit 8.4%.
States she has been trying to walk 20 min/day and reduce carbohydrates. Admits to inconsistent
exercise due to work schedule (shift nurse). Home glucose log: fasting 140-190 range,
post-meal spikes to 240-260 after dinner. Denies polyuria, polydipsia, blurred vision, foot pain
or tingling. No hypoglycaemic episodes. Has not started Jardiance as discussed last visit — was
waiting for insurance approval, which cleared 2 weeks ago.

PMH: DM2 x 10 years | HTN x 15 years | Hyperlipidemia x 8 years | Obesity | GERD

Meds: Metformin 1000mg BID | Lisinopril 20mg QD | Amlodipine 5mg QD | Atorvastatin 40mg QHS
      Omeprazole 20mg QD | Naproxen 500mg PRN | Acetaminophen 1g PRN

ALLERGIES: Penicillin (rash). Shellfish (urticaria).

OBJECTIVE:
VS: BP 136/84 | HR 74 | RR 16 | Temp 37.0°C | SpO2 99% RA | Wt 88kg | BMI 32.4

HEENT: Fundi: small dot haemorrhage noted OD — new finding.
CV: RRR, no murmurs. Mild pretibial pitting oedema 1+ bilat (new).
Extremities: 10g monofilament: decreased sensation left plantar surface (4/10 sites) — new deficit.

LABS:
Fasting glucose: 178 mg/dL | HbA1c: 8.9% [worsened from 8.4%]
Urine microalbumin/creatinine ratio: 68 mg/g [ref <30]
CMP: Cr 1.0 | eGFR 68 | Na 138 | K 4.0
Lipids: LDL 138 | HDL 44 | TG 176
TSH: 2.4 [normal] | Ferritin: 18 ng/mL [low-normal]

ASSESSMENT:
1. DM2 — suboptimal control, worsening — E11.9
2. Diabetic peripheral neuropathy — early — E11.40
3. Diabetic kidney disease — early — E11.65 (microalbuminuria 68 mg/g)
4. Hypertension — adequately controlled — I10
5. Hyperlipidemia — LDL 138, goal <70 — E78.5
6. Iron deficiency anaemia — mild — D50.9

PLAN:
1. START Empagliflozin (Jardiance) 10mg QD — renoprotective + cardioprotective
2. Uptitrate Atorvastatin to 80mg QHS — target LDL <70
3. Start Ferrous sulphate 325mg QD with vitamin C
4. Ophthalmology referral URGENT — new dot haemorrhage
5. Podiatry referral — baseline neuropathy evaluation
6. NSAIDs contraindicated with DKD — switch to Acetaminophen 1g TID PRN

F/U: 3 months for A1c recheck. Ophthalmology URGENT within 4 weeks.
""",
    },
    {
        "id": "transcript-003",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Hypertension Management",
        "icd10_primary": "I10",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-02-20   TIME: 14:45   PROVIDER: Dr. Robert Chen, MD (Internal Medicine)

CC: Hypertension follow-up, BP medication refill

HPI: 52 yo M for routine HTN management at 6-month interval. Home BP log (last 4 weeks):
morning readings 128-142/78-88, evening 118-134/72-82. Average 133/82.
Takes medications consistently. Increased aerobic exercise from 2x to 3x/week.
Occasional occipital headaches on awakening (new, monthly). Denies chest pain, visual changes.

PMH: Essential HTN x 18 years | Hyperlipidemia x 12 years | BPH (mild) | Ex-smoker

Meds: Amlodipine 10mg QD | Lisinopril 20mg QD | Hydrochlorothiazide 25mg QAM
      Atorvastatin 20mg QHS | Tamsulosin 0.4mg QHS | Aspirin 81mg QD

ALLERGIES: NKDA

OBJECTIVE:
VS: BP 138/86 (repeat 136/84) | HR 68 | SpO2 98% | Wt 88kg | BMI 24.5

Fundoscopy: A/V ratio ~2:3 (mild arteriovenous nipping — consistent with chronic HTN).
EKG: NSR at 68. Borderline LVH by Sokolow-Lyon criteria (S V1 + R V5 = 38mm — voltage only).

LABS:
CMP: Na 140 | K 3.7 | Cr 0.9 | eGFR >90 [all normal]
Lipids: LDL 121 | HDL 52 | TG 92 [well controlled]
Urine microalbumin/Cr: negative | Fasting glucose: 94 [normal]

ASSESSMENT:
1. Essential Hypertension — partially controlled — I10
   Average 137/85. At JNC-8 goal but above ACC/AHA 2017 (<130/80). Voltage LVH on ECG (unchanged).
2. Hyperlipidemia — adequately controlled — E78.5
3. BPH — stable on tamsulosin — N40.0
4. Alcohol use — 5-7 units/week — Z72.1

PLAN:
1. Patient prefers lifestyle intensification x3 months before adding spironolactone.
   Low-sodium diet (<2g/day). DASH diet referral. Alcohol reduction (<14 units/week).
2. If BP still >130/80 at 3 months: add spironolactone 25mg.
3. Annual fundoscopy. Continue strict BP control re: voltage LVH.
4. Brief alcohol counselling provided.
5. Refills: Amlodipine x180d, Lisinopril x180d, HCTZ x180d, Atorvastatin x180d.

F/U: 3 months. Return if severe headache, visual changes, chest pain, or BP >160/100.
""",
    },
    {
        "id": "transcript-004",
        "encounter_type": "Inpatient — ICU",
        "condition": "Urosepsis / Septic Shock",
        "icd10_primary": "A41.9",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-01-07   TIME: 03:20   PROVIDER: Dr. Lisa Ramirez, MD (Pulmonary/Critical Care)

CC: Septic shock secondary to urosepsis

HPI: 74 yo F transferred from ED to MICU at 03:00. Family reports 3-day h/o dysuria, frequency,
and confusion, worsening today. PMH: DM2, CHF (EF 40%), CKD 3b (baseline Cr 1.6-1.8), AFib on
warfarin. Source likely urinary — UA positive LE/nitrites, urine culture pending.
Initially hypotensive (SBP 78) — received 2L NS, BP partially responsive; norepinephrine initiated.
Temperature 39.8°C. Lactate 4.1 on arrival.

PMH: Sepsis secondary to UTI x2 | DM2 x 22 years | CHF (EF 40%) x 4 years | CKD 3b | AFib | HTN | Hypothyroidism

Meds (home): Warfarin 5mg QD | Metformin 500mg BID | Furosemide 40mg QD | Metoprolol 25mg BID
             Lisinopril 20mg QD | Levothyroxine 75mcg QD | Atorvastatin 40mg QHS

ALLERGIES: Cephalosporins (documented anaphylaxis).

OBJECTIVE (ICU admission):
VS: BP 88/54 | HR 118 (irregular — AFib) | RR 28 | Temp 39.8°C | SpO2 90% on NRB mask | Wt 61kg
CVP 4 cmH2O (low — volume depleted). UO last 2h: 35 mL (oliguric).

GCS 9 (E3V2M4). Skin mottled bilateral knees. Bibasilar crackles. Suprapubic tenderness.

LABS:
CBC: WBC 22.4 [HIGH] | Hgb 9.8 [LOW] | Plt 88 [LOW — DIC concern] | Bands 18%
CMP: Na 128 [LOW] | K 5.4 [HIGH] | CO2 16 [LOW] | BUN 52 [HIGH] | Cr 2.9 [HIGH — AKI on CKD]
     Glu 312 [HIGH] | Albumin 2.8 [LOW]
Lactate: 4.1 mmol/L [SEVERELY ELEVATED] | Procalcitonin: 18.4 ng/mL [MARKEDLY ELEVATED]
ABG: pH 7.26 | PaCO2 28 | PaO2 62 | HCO3 12 [metabolic acidosis + resp compensation]
INR: 3.8 [ELEVATED] | Fibrinogen: 148 mg/dL [LOW <200 — DIC pattern] | D-dimer 8.4 ug/mL
UA: WBC >100/hpf | Nitrites POS | LE LARGE | Bacteria MANY
Urine Gram stain: Gram-negative rods (preliminary)

ASSESSMENT:
1. Septic Shock — urosepsis — A41.9 + R65.21
   qSOFA 3/3. SOFA estimated 10-12. GNR on Gram stain — E. coli/Klebsiella likely.
2. AKI Stage 3 — N17.9 on CKD 3b — Cr 2.9 (baseline 1.6-1.8)
3. Sepsis-induced coagulopathy / early DIC — D65
4. Metabolic acidosis — lactic / type A — pH 7.26, Lactate 4.1
5. Hypoxaemic respiratory failure — PaO2 62 on NRB; bilateral infiltrates
6. AFib with rapid ventricular response — I48.91

PLAN:
1. Norepinephrine via central line at 0.12 mcg/kg/min; titrate to MAP ≥65
2. Cautious fluid challenges (250mL boluses) given CHF EF 35%
3. Antibiotics (NO cephalosporins — anaphylaxis):
   - Levofloxacin 750mg IV q24h + Gentamicin 1.5 mg/kg IV q8h (double GNR coverage for shock)
4. Hold: Metformin (lactic acidosis risk), Lisinopril (hypoperfusion), Furosemide, Warfarin
5. Insulin infusion: maintain glucose 140-180 mg/dL
6. Repeat lactate q2h. A-line. Repeat echo if haemodynamics not improving.
7. DNR/DNI per prior directive — VERIFY paperwork with daughter.

DISPOSITION: MICU, critical condition, guarded prognosis.
""",
    },
    {
        "id": "transcript-005",
        "encounter_type": "Outpatient — Surgical",
        "condition": "Post-operative — Laparoscopic Cholecystectomy",
        "icd10_primary": "Z48.815",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-05-12   TIME: 09:00   PROVIDER: Dr. Thomas Eriksson, MD (General Surgery)
Post-operative Day 7 — Laparoscopic Cholecystectomy (s/p 2025-05-05)

CC: Post-op check, wound check

HPI: 46 yo F for 1-week post-operative visit after elective laparoscopic cholecystectomy for
symptomatic cholelithiasis with acute cholecystitis. Procedure uneventful — critical view of
safety documented, no IOC performed, no conversion to open, OR time 62 minutes.
Pain now 2/10 (was 6/10 POD1). Tolerating regular diet. No fever at home. No jaundice.
Denies clay-coloured stools, dark urine, right shoulder tip pain. Ambulating independently.

PMH: Cholelithiasis with acute cholecystitis | HTN | Hypothyroidism | Obesity

Meds (post-op): Acetaminophen 1000mg q6h PRN | Ibuprofen 400mg q6h PRN
               Omeprazole 20mg QD | Levothyroxine 88mcg QD | Lisinopril 20mg QD | Docusate 100mg BID

ALLERGIES: Latex (contact urticaria).

OBJECTIVE:
VS: BP 128/80 | HR 72 | Temp 37.0°C | SpO2 99% RA | Wt 82kg

Abdomen: Soft, non-distended. Mild tenderness deep palpation RUQ — expected POD7.
No guarding, rebound, or rigidity.

PORT SITES:
- Umbilical (12mm): Healed well. No erythema, no discharge.
- Epigastric (5mm): Well-healed. Clean and dry.
- RUQ (5mm): Mild periincisional ecchymosis, resolving. No signs of infection.
- RUQ lateral (5mm): Well-healed. Clean.

Pathology: Chronic cholecystitis with acute-on-chronic cholecystitis. No dysplasia or malignancy.

LABS:
ALT: 28 U/L [NORMAL — was 62 pre-op] | AST: 24 [NORMAL]
Total bilirubin: 0.8 mg/dL [NORMAL — no bile duct injury]
Alk Phos: 88 [NORMAL — was 134, resolving]

ASSESSMENT:
1. POD7 s/p laparoscopic cholecystectomy — uncomplicated — Z48.815
2. Hypertension — stable — I10
3. Hypothyroidism — stable — E03.9

PLAN:
1. No complications. Normal recovery. Cleared to drive today.
2. No heavy lifting >10 lbs until 4 weeks. No pool/bath submersion x2 weeks.
3. Taper acetaminophen PRN. Stop ibuprofen at 2 weeks.
4. Discontinue Omeprazole at 4 weeks, Docusate at 2 weeks.
5. Return precautions: fever >38.5°C, worsening pain, jaundice, dark urine, clay stools.

F/U: No routine follow-up needed. Discharge from surgical care.
""",
    },
    {
        "id": "transcript-006",
        "encounter_type": "Emergency Department",
        "condition": "Pulmonary Embolism",
        "icd10_primary": "I26.09",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-04-22   TIME: 16:40   PROVIDER: Dr. Anika Sharma, MD (Emergency Medicine)

CC: Acute onset dyspnoea and right-sided pleuritic chest pain

HPI: 38 yo F presents with 6-hour h/o sudden-onset shortness of breath and right-sided sharp
chest pain, worsening with inspiration. Onset while at her office desk. Denies fever. Notes
calf pain and swelling right leg x 4 days. RFs: started OCP 4 months ago, recent 9-hour flight
from London 2 weeks ago, sedentary desk job. No prior VTE. Non-smoker. No recent surgery.
No personal or family history of thrombophilia.

ROS: Positive: dyspnoea, pleuritic RCP, right calf swelling/pain, mild haemoptysis (blood-streaked sputum x1).
Negative: syncope, leg erythema, fever, chest trauma, recent surgery, prolonged immobility >3d.

PMH: Oral contraceptive pill x 4 months | Seasonal allergies

PSH: Tonsillectomy 2005

Meds: Levonorgestrel/EE 0.15/0.03mg QD | Loratadine 10mg PRN

ALLERGIES: NKDA

OBJECTIVE:
VS: BP 108/72 | HR 108 | RR 24 | Temp 37.3°C | SpO2 93% RA | Wt 64kg | Ht 5'5"
O2 requirement: placed on NC 4L/min → SpO2 97%.

General: Alert, anxious, tachypnoeic.
Respiratory: Reduced air entry RLL. No wheezes. Mild splinting.
Cardiovascular: Tachycardic, regular. Loud P2. No murmurs.
Extremities: Right calf circumference 3cm > left. Right calf pitting oedema. Positive Homan's.
No skin changes/erythema.

LABS:
D-dimer: 4.8 µg/mL [MARKEDLY ELEVATED; ref <0.5]
ABG (4L NC): pH 7.48 | PaO2 74 | PaCO2 28 | HCO3 21 | A-a gradient 31 [elevated]
Troponin I: 0.08 ng/mL [borderline elevated — RV strain marker]
Pro-BNP: 620 pg/mL [elevated — RV stress]
CBC: WBC 11.2 | Hgb 13.8 | Plt 287 [all near-normal]
CMP: all within normal limits | Cr 0.7
INR: 1.0 | APTT: 28s [both normal — baseline]

EKG: Sinus tachycardia at 108 bpm. S1Q3T3 pattern (classic but non-specific). T-wave inversions V1-V4.
No RV strain pattern. QTc 420ms.

CTPA: Multiple bilateral pulmonary emboli — right main PA, RLL segmental, left lower lobe segmental.
Right ventricular dilation (RV:LV ratio 1.2). No saddle embolus. No infarct.
Doppler US right leg: Acute DVT — right popliteal and femoral veins. Left leg: negative.

Wells PE Score: 7 (High probability)

ASSESSMENT:
1. Submassive (intermediate-risk) Pulmonary Embolism — bilateral, RV dilation — I26.09
   Provoked: OCP + long-haul flight. Wells 7 (high). D-dimer markedly elevated.
   RV:LV ratio 1.2 on CTPA, troponin borderline elevated. No haemodynamic instability = sub-massive.
2. Deep Vein Thrombosis — right popliteal + femoral — I82.4B1
3. Oral contraceptive-associated VTE risk — Z79.3 (OCP)

PLAN:
1. Anticoagulation STAT:
   - Enoxaparin 1mg/kg SC q12h (64mg q12h) — bridge to DOAC
   - Rivaroxaban 15mg PO BID x21 days → 20mg QD maintenance (DOAC preferred, avoid OCP interaction)
2. Haematology referral for thrombophilia screen (defer until 3 months anticoagulation complete)
3. STOP ORAL CONTRACEPTIVE PILL — documented counselling provided
4. Continuous cardiac monitoring — watch for haemodynamic deterioration
5. If deteriorates to massive PE criteria → thrombolysis with alteplase
6. Admit to cardiology/medicine with PE protocol
7. Pulmonology follow-up in 3 months — assess for chronic thromboembolic pulmonary hypertension

DISPOSITION: Admitted to cardiac telemetry. Stable — intermediate high-risk PE.
""",
    },
    {
        "id": "transcript-007",
        "encounter_type": "Inpatient — General Medicine",
        "condition": "COPD Acute Exacerbation",
        "icd10_primary": "J44.1",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-03-02   TIME: 11:15   PROVIDER: Dr. Nathan Brooks, MD (Pulmonology)

CC: Worsening dyspnoea, increased sputum production, cough

HPI: 68 yo M with severe COPD (GOLD III, on home O2 at 2L/min) presenting with 5-day worsening
dyspnoea, increased sputum production (greenish, more than usual), and increased cough. Was
managing at home with frequent albuterol nebs (using 4-5x/day vs baseline 1-2x/day) without
improvement. Last COPD exacerbation 6 months ago (required hospitalisation x4d). SpO2 at home
dropping to 84-86%. No fever reported. Cannot say full sentences.

Current exacerbation trigger: flu-like prodrome 1 week ago (fever, myalgias) — likely viral trigger.

PMH: Severe COPD GOLD III (FEV1 38%) | Pack hx 45 pack-years (quit 3 years ago)
     Hypertension | T2DM | Moderate-severe OSA (CPAP non-adherent) | Pulmonary HTN (mild)

Meds: Tiotropium 18mcg inh QD | Salmeterol/Fluticasone 50/500mcg inh BID
      Albuterol 2.5mg neb PRN | Home O2 2L/min continuous
      Metformin 500mg BID | Lisinopril 10mg QD | Aspirin 81mg QD

ALLERGIES: Penicillin (GI intolerance only — rash negative)

OBJECTIVE:
VS: BP 142/88 | HR 102 | RR 26 | Temp 37.4°C | SpO2 88% on 2L NC (home baseline 93%) | Wt 78kg
On 4L NC: SpO2 91%. On Venturi 28%: SpO2 93%.

General: Accessory muscle use, pursed-lip breathing, tripod positioning. Speaking in 3-4 word sentences.
Respiratory: Hyperinflated chest. Barrel chest. Prolonged expiratory phase. Diffuse exp wheeze + crackles.
             Reduced air entry bilaterally, worse at bases.
CV: Tachycardic, regular. No murmurs. Mild elevated JVP.
Extremities: Trace bilateral ankle oedema. No clubbing. Mild central cyanosis.

LABS:
ABG (2L NC): pH 7.32 | PaCO2 64 | PaO2 54 | HCO3 32 | BE +5 [acute-on-chronic hypercapnic failure]
CBC: WBC 13.8 | Neutrophils 11.2 [HIGH] | Hgb 16.2 [elevated — polycythaemia] | Plt 298
CMP: Na 138 | K 3.9 | Cr 1.0 | Glu 224 [HIGH — stress hyperglycaemia]
CRP: 68 mg/L [elevated] | Procalcitonin: 0.18 ng/mL [low — viral/non-bacterial aetiology]
BNP: 280 pg/mL [elevated — cor pulmonale contribution]

Influenza A/B rapid: Influenza A POSITIVE

CXR: Hyperinflated lungs, flattened diaphragms. No new consolidation. No PTX. Increased interstitial markings.
ECG: Sinus tachycardia. P pulmonale. RAD. No RV hypertrophy pattern.

Spirometry (baseline 6 months ago): FEV1 38% predicted, FEV1/FVC 0.52 — GOLD III

ASSESSMENT:
1. Acute Exacerbation of Severe COPD — J44.1
   Triggering factor: Influenza A. pH 7.32, PaCO2 64 — acute-on-chronic hypercapnic failure.
2. Influenza A infection — J10.1
3. Hypercapnic respiratory failure — J96.01
4. Stress hyperglycaemia — glucose 224 — R73.09
5. Pulmonary hypertension — mild — I27.0

PLAN:
1. NIV (BiPAP) — S/T mode: IPAP 14 / EPAP 6 / RR backup 12 — titrate to CO2 and comfort
2. Controlled oxygen therapy: Venturi 28% — target SpO2 88-92% (avoid hypercapnic drive suppression)
3. Albuterol 2.5mg + Ipratropium 0.5mg nebs q20min x3 → q4h scheduled
4. Methylprednisolone 125mg IV q8h x1 day → Prednisone 40mg PO QD x5 days
5. Oseltamivir 75mg BID x5 days (positive Influenza A; within 48h of admission)
6. Azithromycin 500mg IV QD x5d (cover atypical organisms despite low PCT — AECOPD protocol)
7. Hold Metformin (lactic acidosis risk). Insulin sliding scale for glucose.
8. Respiratory therapy in AM. Chest physiotherapy TID.
9. VTE prophylaxis: Enoxaparin 40mg SC QD

DISPOSITION: Pulmonary step-down unit. Close monitoring for NIV failure → intubation criteria.
""",
    },
    {
        "id": "transcript-008",
        "encounter_type": "Emergency Department / Stroke",
        "condition": "Acute Ischaemic Stroke",
        "icd10_primary": "I63.9",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-05-08   TIME: 09:28   PROVIDER: Dr. Helen Voss, MD (Neurology — Stroke)
Last Known Well: 09:05 today. Door-to-CT: 14 min. Door-to-IV tPA: 47 min.

CC: Acute left-sided weakness, facial droop, slurred speech

HPI: 71 yo M presenting via EMS — found by wife at 09:05 unable to lift left arm or leg, with
left facial droop and dysarthria. Wife states was "completely normal" while having breakfast at
09:00. No witnessed seizure. No headache at onset. No recent illness, trauma, or surgery.
No prior TIA or stroke. RFs: HTN (poorly controlled), paroxysmal AFib on aspirin only
(patient declining warfarin), DM2, hyperlipidemia, prior smoker.

EMS at scene: FAST exam positive — facial droop, arm drift, speech abnormality.
Stroke Code activated on arrival.

PMH: Paroxysmal AFib | HTN | DM2 | Hyperlipidemia | Ex-smoker (quit 12 years ago)

Meds: Aspirin 325mg QD | Metoprolol 50mg BID | Lisinopril 20mg QD | Atorvastatin 40mg QHS | Metformin 1000mg BID

ALLERGIES: Codeine (nausea/vomiting)

OBJECTIVE (09:28 arrival):
VS: BP 188/102 | HR 82 irregular (AFib) | RR 18 | Temp 37.0°C | SpO2 96% RA | Wt 84kg

NIHSS Score: 12
  Level of consciousness: Alert (0) | Commands: Follows commands (0) | Gaze: Subtle R preference (1)
  Visual fields: L homonymous hemianopia (2) | Facial palsy: Moderate L (2)
  L arm motor: Drift (2) | R arm motor: Normal (0)
  L leg motor: Drift (2) | R leg motor: Normal (0)
  Ataxia: None (0) | Sensory: Mild L decrease (1) | Language: None (0) | Dysarthria: Mild (1)
  Extinction/Neglect: None (0)

Neurological Exam: Right hemiplegia noted. L gaze deviation. L facial droop. Dysarthria.
                  Neglect: left extinction to double simultaneous stimulation.

IMAGING:
Non-contrast CT Head: No haemorrhage. No early infarct signs. ASPECTS 10/10.
CT Perfusion: Mismatch ratio 1.7. Core infarct ~18mL (right MCA territory). Penumbra ~65mL.
   Large ischaemic penumbra — amenable to both IV tPA and thrombectomy.
CT Angiography: Right M1 MCA occlusion confirmed. No significant intracranial stenosis elsewhere.

LABS:
Glucose: 162 mg/dL [elevated]
CBC: WBC 9.2 | Hgb 14.8 | Plt 334 | INR 1.0 (not on anticoagulation — aspirin only)
CMP: Na 141 | K 4.0 | Cr 1.0 | all normal
PT/INR: 1.0 | APTT: 26s [both normal — tPA eligible]

ASSESSMENT:
1. Acute Ischaemic Stroke — Right MCA territory, M1 occlusion — I63.9
   Onset-to-door 23 minutes. NIHSS 12 (moderate-severe). ASPECTS 10. Core 18mL, penumbra 65mL.
   Aetiology: Cardioembolic (AFib — was on aspirin only, not anticoagulated).
2. Paroxysmal Atrial Fibrillation — I48.91 — thromboembolic source
3. Hypertension — poorly controlled, BP 188/102 — I10

PLAN:
1. IV tPA (alteplase) given 09:52 — Door-to-needle 47 min ✓ (target <60 min)
   Dose: 0.9 mg/kg (75.6 mg total): 10% bolus (7.6mg) → 90% over 60 min (68mg)
   BP management: keep <185/110 during tPA infusion — Labetalol PRN
2. Mechanical thrombectomy — IR activated — anticipated door-to-groin <90 min
3. NPO. No nasogastric tube. Aspiration precautions.
4. Glucose target 140-180 mg/dL — insulin PRN
5. Stroke unit admission. Continuous telemetry.
6. Anticoagulation for AFib: START Apixaban 2.5mg BID 48h post-tPA if imaging stable
7. Statin uptitration to 80mg QHS (high-intensity post-stroke)
8. Swallowing assessment prior to any oral intake
9. PT/OT/Speech therapy consults

DISPOSITION: Neuro ICU/Stroke Unit. Thrombectomy suite → Stroke Unit.
""",
    },
    {
        "id": "transcript-009",
        "encounter_type": "Inpatient — General Medicine",
        "condition": "Acute Kidney Injury — Contrast Nephropathy",
        "icd10_primary": "N17.9",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-06-01   TIME: 14:00   PROVIDER: Dr. Ahmed Qureshi, MD (Internal Medicine / Nephrology Consult)

CC: Rising creatinine post-contrast CT scan

HPI: 59 yo M admitted for rising creatinine 48h after CT coronary angiography with contrast
(iodinated contrast 120mL low-osmolar). Baseline Cr 1.4 (CKD 3a, diabetic nephropathy).
Pre-contrast hydration protocol was administered (0.9% NS 500mL pre and 500mL post).
Post-procedure day 1: Cr 1.8. Post-procedure day 2: Cr 2.6 (today). UO declining.
RFs for CI-AKI: CKD, DM2, reduced EF, large contrast volume, NSAID use.

Was taking ibuprofen 400mg TID at home for knee pain (not disclosed during pre-procedure assessment).

PMH: CKD 3a (baseline Cr 1.4, eGFR 52) | DM2 x 15 years | HTN | CAD (PCI 2019) | HFrEF (EF 40%)

Meds: Aspirin 81mg QD | Atorvastatin 80mg QHS | Metoprolol 50mg BID | Lisinopril 10mg QD
      Furosemide 40mg QD | Metformin 500mg BID | Ibuprofen 400mg TID (undisclosed home use)

ALLERGIES: Cephalosporins (rash)

OBJECTIVE:
VS: BP 152/88 | HR 76 | RR 16 | Temp 36.9°C | SpO2 97% RA | Wt 86kg (up 3kg from baseline)
UO last 8h: 160mL (20mL/hr — oliguric threshold = 0.5mL/kg/hr = 43mL/hr)

General: Alert, mildly puffy periorbital. No jaundice.
CV: RRR. Mild elevated JVP ~5cm. Faint S3.
Chest: Fine bibasilar crackles — new.
Abdomen: Soft, NT. No bruits.
Extremities: 2+ pitting oedema bilaterally to knee.

LABS:
Creatinine: 2.6 mg/dL [HIGH — was 1.4 baseline, 1.8 POD1, 2.6 today — 85% rise from baseline]
eGFR: 27 mL/min [Stage 4 AKI on CKD]
BUN: 44 mg/dL [HIGH] | BUN/Cr ratio: 16.9 [not pre-renal]
Urine Na: 38 mEq/L | FENa: 2.1% [>1% — intrinsic AKI]
UA: 2+ protein, rare granular casts, no blood — tubular injury pattern
Urine myoglobin: negative
K: 5.2 [HIGH] | HCO3: 18 [LOW — metabolic acidosis]
CBC: all normal | BNP: 480 pg/mL [elevated — volume overloaded]
LDH: 188 | Uric acid: 8.1 [elevated]

ASSESSMENT:
1. Contrast-Induced AKI — moderate severity — N17.9
   85% Cr rise from baseline (1.4→2.6) meeting CI-AKI definition. Oliguric.
   Contributing factors: undisclosed NSAID use, CKD baseline, volume overload.
2. Volume overload — 3kg weight gain, bibasilar crackles, peripheral oedema — E87.70
3. Hyperkalaemia — K 5.2 — E87.5
4. Metabolic acidosis — HCO3 18 — E87.2

PLAN:
1. STOP: Metformin (lactic acidosis risk in AKI), Lisinopril (AKI, hyperkalaemia), NSAIDs (nephrotoxic), Furosemide (diuretic resistance in AKI — hold x48h)
2. IV fluid: Normal saline 0.5mL/kg/hr (cautious in HFrEF) with strict fluid balance q4h
3. Hyperkalaemia: Kayexalate 30g PO QD | Dietary K restriction
4. Monitor BMP, magnesium, phosphorus q12h | Urine output q1h
5. Nephrology consult — potential CRRT if Cr continues to rise, severe acidosis, K uncontrolled
6. Re-evaluate Lisinopril at discharge if Cr returns toward baseline
7. Post-AKI clinic — 3 months. CKD education re: contrast avoidance.

DISPOSITION: Medicine floor with strict nephrology monitoring. Dialysis on standby.
""",
    },
    {
        "id": "transcript-010",
        "encounter_type": "Emergency Department",
        "condition": "Community-Acquired Pneumonia (CAP)",
        "icd10_primary": "J18.9",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-02-14   TIME: 20:15   PROVIDER: Dr. Yuki Tanaka, MD (Emergency Medicine)

CC: Productive cough, fever, shortness of breath x 4 days

HPI: 77 yo F presents with 4-day h/o productive cough (yellow-green sputum), fever to 38.9°C at home,
progressive dyspnoea, reduced appetite. Lives independently in assisted living. No recent hospitalisation
in past 90 days. No mechanical ventilation or IV antibiotics in past 6 months. Up to date on pneumococcal
vaccine (received PPSV23 3 years ago, PCV13 5 years ago). Not immunocompromised.

ROS: Positive: cough (productive), fever, dyspnoea, chills, anorexia, pleuritic chest pain (L lateral).
Negative: haemoptysis, vomiting, diarrhoea, confusion (family denies), leg swelling, night sweats.

PMH: HTN | HFrEF (EF 45%, NYHA II) | T2DM | CKD 2 (Cr 1.1) | Hypothyroidism | Diverticulosis

Meds: Furosemide 20mg QD | Lisinopril 20mg QD | Carvedilol 12.5mg BID | Spironolactone 25mg QD
      Metformin 500mg BID | Atorvastatin 40mg QHS | Levothyroxine 75mcg QD | Aspirin 81mg QD

ALLERGIES: Penicillin (documented anaphylaxis — unknown provenance; consider allergy testing)

OBJECTIVE:
VS: BP 136/82 | HR 98 | RR 24 | Temp 38.8°C | SpO2 91% RA | Wt 68kg
On 4L NC: SpO2 95%.

General: Ill-appearing, fatigued, no acute distress at rest. Shallow respirations.
Respiratory: Dullness to percussion LLL. Increased tactile fremitus LLL. Bronchial breath sounds LLL.
             Crackles LLL > LUL. E→A changes LLL.
CV: RRR. Faint S3 audible. Mild JVP elevation 3cm.
Abdomen: Soft, NT. No guarding.
Extremities: 1+ bilateral ankle oedema (chronic, baseline per patient).

LABS:
CBC: WBC 18.6 [HIGH] | Neutrophils 16.2 | Bands 8% | Hgb 11.8 [mild anaemia] | Plt 312
CMP: Na 132 [LOW] | K 4.6 | Cr 1.4 [above baseline 1.1] | BUN 32 | Glu 186 [HIGH]
CRP: 198 mg/L [markedly elevated] | Procalcitonin: 1.8 ng/mL [elevated — bacterial]
Lactate: 1.6 mmol/L [borderline]
BNP: 320 pg/mL [elevated — CHF component]
Blood cultures x2: Pending

Sputum Gram stain: Gram-positive diplococci — consistent with Streptococcus pneumoniae
Urine pneumococcal Ag: POSITIVE

CXR: Dense left lower lobe consolidation. No pneumothorax. Mild cardiomegaly. Mild vascular congestion.
     No significant pleural effusion.

PSI Score: 108 (Class IV — High risk) → Inpatient admission indicated
CURB-65: 3 (urea elevated, RR 24, age ≥65) → Inpatient indicated

ASSESSMENT:
1. Community-Acquired Pneumonia — Left lower lobe, likely S. pneumoniae — J18.9
   High-risk (PSI IV, CURB-65 3). Urine pneumococcal Ag positive. Penicillin allergy documented.
2. Hyponatraemia — Na 132, likely SIADH secondary to pneumonia — E87.1
3. Acute kidney injury (mild) — Cr 1.4 vs baseline 1.1 — likely pre-renal — N17.9
4. CHF exacerbation (mild contribution) — BNP 320, mild vascular congestion — I50.20

PLAN:
1. Antibiotics (PENICILLIN ALLERGY — anaphylaxis):
   - Levofloxacin 750mg IV QD (respiratory fluoroquinolone — covers atypicals + S. pneumoniae)
   - Azithromycin 500mg IV QD (add atypical coverage per IDSA CAP guidelines x5d)
   Alternative to beta-lactams given anaphylaxis history.
2. Controlled O2: Target SpO2 92-95% via NC / Venturi
3. Cautious IV fluids: 250mL NS bolus PRN (HF background) | track fluid balance q4h
4. Hold Metformin (AKI), Hold Spironolactone (AKI, hyperkalaemia risk)
5. Furosemide: continue 20mg QD (gentle diuresis for mild congestion)
6. Daily CXR until clinical improvement
7. Repeat blood cultures. Sputum culture.
8. Nutrition: soft diet, encourage oral intake

DISPOSITION: Admitted to General Medicine floor. IV antibiotics → PO switch at 48-72h if improving.
""",
    },
    {
        "id": "transcript-011",
        "encounter_type": "Emergency Department",
        "condition": "Atrial Fibrillation with Rapid Ventricular Response",
        "icd10_primary": "I48.0",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-07-10   TIME: 18:20   PROVIDER: Dr. Kevin Park, MD (Emergency Medicine)

CC: Palpitations, lightheadedness, and dyspnoea x 3 hours

HPI: 66 yo F presents with sudden onset palpitations at rest, associated with dyspnoea (moderate),
and lightheadedness. No syncope. No chest pain. First episode. Denies fever, recent illness,
caffeine excess. PMH: HTN on HCTZ and lisinopril. Thyroid disease (on levothyroxine). No prior AF.

VS: BP 128/82 | HR 148 (irregular) | RR 20 | SpO2 96% RA | Temp 37.1°C

LABS:
TSH: 0.08 mIU/L [SUPPRESSED — thyrotoxicosis?] | Free T4: 2.6 ng/dL [HIGH]
CBC: WBC 8.4 | Hgb 13.2 | Plt 244
CMP: Na 138 | K 3.6 | Mg 1.8 [LOW-NORMAL] | Cr 0.9 | Glu 102
Troponin: <0.01 [negative] | BNP: 188 pg/mL [mildly elevated]
INR: 1.1

EKG: AF with RVR at 148 bpm. No WPW. No ST changes. Irregularly irregular rhythm confirmed.

ASSESSMENT:
1. New-onset Atrial Fibrillation with RVR — I48.0
   Likely precipitant: thyrotoxicosis (suppressed TSH, elevated T4)
2. Thyrotoxicosis (new finding) — E05.90
3. Hypomagnasaemia — E83.42

PLAN:
1. Rate control: Diltiazem 0.25 mg/kg IV over 2 min → target HR <100 (avoid in WPW — excluded)
2. Magnesium sulphate 2g IV over 20 min
3. Anticoagulation: CHA2DS2-VASc 2 (age, HTN) → start Apixaban 5mg BID
4. Endocrinology consult (thyrotoxicosis) — likely precipitant
5. Admit for cardioversion if AF >48h or haemodynamic compromise
DISPOSITION: Admitted cardiology. Rhythm monitoring. Cardioversion considered once anticoagulated x3 weeks.
""",
    },
    {
        "id": "transcript-012",
        "encounter_type": "Emergency Department",
        "condition": "Upper Gastrointestinal Bleed",
        "icd10_primary": "K92.1",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-08-03   TIME: 04:45   PROVIDER: Dr. Priya Nair, MD (Emergency Medicine)

CC: Haematemesis (coffee-ground vomiting) and melaena x 12 hours

HPI: 58 yo M with 12h h/o vomiting coffee-ground material (x4 episodes, approx 200mL each)
and black tarry stools x2. Lightheaded when standing. Chronic NSAID use for knee OA
(naproxen 500mg BID). Drinks 2-3 whiskeys nightly. No known liver disease. No prior GIB.

VS: BP 92/58 | HR 118 | RR 20 | SpO2 98% RA | Temp 37.2°C
Orthostatics: BP drops 22mmHg on standing.

LABS:
Hgb: 7.4 g/dL [LOW — was 14.2 three months ago] | Hct 22% | Plt 198
BUN: 44 | Cr 0.9 | BUN/Cr ratio 48.9 [HIGH — upper GIB pattern] | INR: 1.4 | aPTT 34
ALT 28 | AST 38 | AlkPhos 88 | T. Bili 0.9 | albumin 3.6

ASSESSMENT:
1. Active Upper GIB — likely peptic ulcer / NSAID-induced — K92.1
   Glasgow-Blatchford Score: 14 (high risk — immediate endoscopy)
2. Haemodynamic instability — hypotension, tachycardia, orthostasis

PLAN:
1. 2x large-bore IVs. Type & cross 4 units pRBC. Transfuse 2u pRBC immediately.
2. PPI: Pantoprazole 80mg IV bolus → 8mg/hr infusion
3. Octreotide 50mcg IV bolus → 50mcg/hr infusion (rule out variceal bleed pending scope)
4. Ceftriaxone 1g IV QD (prophylaxis if suspected cirrhosis)
5. GI STAT — upper endoscopy within 24h (non-variceal; or ASAP if variceal suspected)
6. STOP NSAIDs permanently. Alcohol counselling.
7. ICU admission.
""",
    },
    {
        "id": "transcript-013",
        "encounter_type": "Inpatient — Gastroenterology",
        "condition": "Acute Pancreatitis",
        "icd10_primary": "K85.1",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-09-14   TIME: 10:00   PROVIDER: Dr. Daniela Torres, MD (Gastroenterology)

CC: Epigastric pain radiating to back, nausea, vomiting x 18 hours

HPI: 44 yo M with 18h h/o severe epigastric pain (8/10) radiating to back, nausea, and vomiting.
Pain worse with food. Drinks 6-8 beers/day. No gallstones on prior imaging. No prior pancreatitis.
No fever at home.

VS: BP 118/76 | HR 106 | RR 18 | Temp 38.1°C | SpO2 97% RA | Wt 84kg

LABS:
Lipase: 1,840 U/L [MARKEDLY ELEVATED — ref <60] | Amylase 620 U/L [elevated]
WBC: 15.2 [HIGH] | Hgb 15.8 | CRP: 182 mg/L [HIGH — severity marker]
CMP: Na 136 | K 3.8 | Cr 1.1 | Glu 188 | Ca 8.6 [low normal — monitor]
ALT 42 | AST 58 | ALP 110 | T. bili 0.9 [no biliary obstruction]
Triglycerides: 284 mg/dL [elevated — secondary cause excluded at this level]

CT Abdomen/Pelvis (w/ contrast): Pancreatic oedema with peripancreatic fat stranding.
Balthazar Grade C. No necrosis. No pseudocyst. No abscess.

Ranson Score at 48h: 3 (moderate severity) | BISAP 2

ASSESSMENT:
1. Acute Alcoholic Pancreatitis — moderate severity — K85.1
2. Alcohol use disorder (severe) — F10.20

PLAN:
1. NPO — begin aggressive IV fluids: LR 250-500mL/hr x4h → reassess
2. Pain: Morphine 4mg IV q4h PRN | Ketorolac 30mg IV q6h x2d
3. Antiemetics: Ondansetron 4mg IV q6h
4. Nutrition: restart feeding (NG if still intolerant at 48h — enteral preferred)
5. Monitor for complications: glucose, Ca, haematocrit q6h
6. Alcohol cessation counselling. Thiamine 100mg IV QD.
7. Repeat imaging if no improvement at 48h.
""",
    },
    {
        "id": "transcript-014",
        "encounter_type": "Emergency Department",
        "condition": "Diabetic Ketoacidosis (DKA)",
        "icd10_primary": "E11.10",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-10-19   TIME: 22:35   PROVIDER: Dr. Samuel Wright, MD (Emergency Medicine)

CC: Polyuria, polydipsia, nausea, abdominal pain x 2 days

HPI: 24 yo F with T1DM (x 12 years, on insulin pump) presenting with 2 days of polyuria,
polydipsia, nausea, and vague abdominal pain. Home CGM showing readings >400 mg/dL.
Insulin pump malfunction 3 days ago — used MDI as backup inconsistently. No infection symptoms.
Last ate 12h ago. Vomited x3 today.

VS: BP 96/64 | HR 118 | RR 28 (Kussmaul) | Temp 37.4°C | SpO2 98% RA | Wt 58kg

LABS:
Glucose: 482 mg/dL [MARKEDLY ELEVATED]
ABG: pH 7.12 | PaCO2 18 | HCO3 6 [severe anion-gap metabolic acidosis + respiratory compensation]
Anion gap: 32 [MARKEDLY ELEVATED] | Na 131 [corrected Na 144]
K: 5.8 [HIGH — total body K depletion masked] | Cr 1.2 [mildly elevated]
Ketones: Serum 5.4 mmol/L [HIGH] | Urine ketones 4+
CBC: WBC 18.4 (stress leukocytosis) | No infection source identified
HbA1c: 11.8% [severely uncontrolled]
Phosphate: 2.2 | Mg: 1.6 [low — deplete in DKA]

ASSESSMENT:
1. Diabetic Ketoacidosis — severe — E11.10
   pH 7.12, AG 32, glucose 482, HCO3 6. Precipitated by pump malfunction.
2. Type 1 DM — uncontrolled — E10.65

PLAN:
1. FLUID RESUSCITATION: 0.9% NS 1L over 1h → 500mL/hr x2h → reassess (target BP/HR)
2. INSULIN PROTOCOL: Insulin drip 0.1 unit/kg/hr (5.8 units/hr); DO NOT bolus
   Switch to D5/0.45NS when glucose <250, reduce infusion
3. K REPLACEMENT: KCl 40mEq/L in IVF until K confirmed >3.5 before starting insulin
4. Phosphate: K-Phos 20mEq in IVF if phosphate <1.0 (recheck q4h)
5. Bicarbonate: hold unless pH <6.9 (risk cerebral oedema in T1DM)
6. Monitor glucose, BMP, venous pH q1h
7. ICU admission. Endocrinology consult.
8. Diabetes educator — pump management review prior to discharge.
""",
    },
    {
        "id": "transcript-015",
        "encounter_type": "Inpatient — Cardiology",
        "condition": "Acute Decompensated Heart Failure (HFrEF)",
        "icd10_primary": "I50.21",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-11-05   TIME: 09:30   PROVIDER: Dr. Charles Lambert, MD (Heart Failure / Cardiology)

CC: Worsening dyspnoea, bilateral leg oedema, orthopnoea x 5 days

HPI: 72 yo M with known HFrEF (EF 30%) admitted for acute decompensation. States dyspnoea
on exertion worsening x5 days — now SOB at rest. Orthopnoea (3-pillow). PND x2 nights.
Weight gain 6kg in 5 days. Self-discontinued furosemide 5 days ago (felt "too much urination").
Dietary: admits large salty meal Thanksgiving. BNP last check 3 months ago was 410 pg/mL.

PMH: HFrEF (EF 30%) | Ischaemic CM — prior MI 2020 | T2DM | CKD 3a | AF (on apixaban)

Meds: Carvedilol 25mg BID | Lisinopril 10mg BID | Spironolactone 25mg QD | Furosemide 80mg QD
      Apixaban 5mg BID | Empagliflozin 10mg QD | Atorvastatin 40mg QHS | Metformin 500mg BID

VS: BP 144/88 | HR 94 irregular (AF) | RR 22 | SpO2 89% RA | Wt 98kg (dry wt ~92kg)
On 6L: SpO2 94%.

LABS:
BNP: 2,840 pg/mL [MARKEDLY ELEVATED]
Cr 1.8 [elevated — from baseline 1.2 — cardiorenal syndrome]
Na 129 [LOW — dilutional] | K 5.1 | Hgb 10.8 [LOW — CKD/HF anaemia]
Lactate: 1.9 [mildly elevated — low-output state]
Troponin: 0.04 ng/mL [borderline — demand ischaemia]

CXR: Cardiomegaly. Bilateral pulmonary oedema (bat-wing). Bilateral pleural effusions. KL-B lines.

ASSESSMENT:
1. Acute Decompensated HFrEF — I50.21 — wet/warm haemodynamic profile
2. Cardiorenal syndrome — AKI on CKD — Cr 1.8 from 1.2
3. Dilutional hyponatraemia — Na 129
4. Precipitants: diuretic non-compliance, dietary indiscretion

PLAN:
1. IV diuretics: Furosemide 80mg IV BID (switch from PO — poor absorption in gut oedema)
   Target UO 1-2L/day net negative. Daily weights.
2. Fluid restriction: 1.5L/day. Low-sodium diet.
3. Continue Carvedilol, Lisinopril (hold if systolic <90), Spironolactone, Empagliflozin
4. Telemetry: AF rate monitoring. Digoxin if rate poorly controlled.
5. Swan-Ganz catheter if haemodynamic deterioration (PCWP, CO, SVR)
6. Discharge planning: Home health, structured HF programme, diuretic compliance.
""",
    },
    {
        "id": "transcript-016",
        "encounter_type": "Emergency Department",
        "condition": "Meningitis — Bacterial",
        "icd10_primary": "G00.9",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-12-08   TIME: 03:10   PROVIDER: Dr. Fatima Hassan, MD (Emergency Medicine)

CC: Severe headache, neck stiffness, fever, and photophobia x 8 hours

HPI: 28 yo M presents with 8h h/o severe frontal/occipital headache (10/10), neck stiffness,
photophobia, and fever to 40.1°C. Nausea and two episodes of vomiting. No recent illness.
No rash noted by patient. No prior meningitis. Lives in college dormitory. Meningococcal vaccine:
received at age 12 (prior to MenACWY recommendation update — may not be current).

VS: BP 118/72 | HR 112 | RR 20 | Temp 40.1°C | SpO2 99% RA

EXAM: Nuchal rigidity present. Kernig's sign positive. Brudzinski's sign positive.
Petechial rash noted posterior thighs and buttocks (12-15 pinpoint lesions — non-blanching).
No papilloedema. PERRL. No focal neuro deficits.

LABS:
CBC: WBC 24.6 [HIGH] | Bands 22% [HIGH] | Hgb 14.8 | Plt 88 [LOW — early DIC concern]
CMP: Na 131 [LOW] | K 4.4 | Cr 1.1 | Glu 42 [LOW — glucose consumed by bacteria]
CRP: 384 mg/L [MARKEDLY ELEVATED] | PCT: 22.4 ng/mL [MARKEDLY ELEVATED]
Coags: INR 2.4 | aPTT 44 [coagulopathy]

CT Head (non-contrast): No intracranial hypertension. No herniation. No abscess. Proceed to LP.

CSF Analysis:
Opening pressure: 340 mmH2O [MARKEDLY ELEVATED]
WBC: 8,200 [MARKEDLY ELEVATED — predominantly neutrophils 96%]
Glucose: 22 mg/dL [LOW — serum:CSF ratio 0.28 — bacterial pattern]
Protein: 480 mg/dL [ELEVATED] | Lactate 6.8 [elevated] | Gram stain: Gram-negative diplococci

ASSESSMENT:
1. Bacterial Meningitis — Neisseria meningitidis suspected (non-blanching rash, GN diplococci) — G00.9
2. Meningococcaemia with early DIC — septic shock risk — A39.4
3. SIADH — Na 131 — secondary to meningitis — E22.2

PLAN:
1. ANTIBIOTICS STAT (start BEFORE LP result if LP delayed — do NOT delay for CT if no signs of ICP):
   - Ceftriaxone 2g IV q12h (meningococcal coverage)
   - Vancomycin 15mg/kg IV q8h (coverage until sensitivities)
   - Ampicillin 2g IV q4h (Listeria coverage — given slightly atypical demographics)
2. Dexamethasone 0.15mg/kg q6h x4d (start BEFORE or WITH first antibiotic dose)
3. Isolation precautions: droplet x24h after antibiotic initiation
4. Public health notification (meningococcal disease is reportable)
5. Close contacts: rifampicin prophylaxis
6. ICU admission.
""",
    },
    {
        "id": "transcript-017",
        "encounter_type": "Inpatient — Hepatology",
        "condition": "Acute Liver Failure — Drug-Induced (Acetaminophen)",
        "icd10_primary": "K72.00",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-08-18   TIME: 16:00   PROVIDER: Dr. Ronald Kim, MD (Hepatology)

CC: Jaundice, confusion, right upper quadrant pain following acetaminophen overdose

HPI: 31 yo F transferred from OSH 3 days post-acetaminophen intentional overdose (estimated
20g ingested in a single episode, activated charcoal given at 6h). Progressive jaundice,
confusion (worsening), and right upper quadrant pain. Psychiatry involved at OSH.

VS: BP 102/64 | HR 108 | RR 18 | Temp 37.8°C | SpO2 95% RA | Wt 62kg

EXAM: Deeply jaundiced sclera and skin. Asterixis grade 2. Drowsy, disoriented to place/time.
No Dupuytren's. No spider naevi (no chronic liver disease). Liver edge palpable 2cm below RCM.

LABS:
ALT: 8,240 U/L [MARKEDLY ELEVATED — acute hepatocellular necrosis]
AST: 12,600 U/L [MARKEDLY ELEVATED]
Total bilirubin: 14.2 mg/dL | ALP: 140 [relatively low — hepatocellular pattern]
INR: 6.8 [MARKEDLY ELEVATED — synthetic failure]
Creatinine: 2.4 [HIGH — hepatorenal syndrome or acetaminophen nephrotoxicity]
Ammonia: 188 µmol/L [ELEVATED — hepatic encephalopathy]
Lactate: 4.8 mmol/L [HIGH — hepatic lactate clearance failure]
Phosphate: 1.2 [LOW — phosphate depletion]
CBC: WBC 14.2 | Plt 78 [LOW]
Acetaminophen level (now day 3): 6 µg/mL [residual]

ASSESSMENT:
1. Acetaminophen-induced Acute Liver Failure — Grade 3 hepatic encephalopathy — K72.00
   King's College Criteria: INR>6.8, Cr>3.4 not yet met — monitor closely. ALF listing criteria met.
2. Coagulopathy of ALF — INR 6.8
3. AKI — Cr 2.4 — hepatorenal vs direct nephrotoxicity
4. Hyperammonaemia + hepatic encephalopathy Grade 3 — G92.9

PLAN:
1. N-ACETYLCYSTEINE: Continue IV NAC 6.25mg/kg/hr (maintenance phase) — continue 72h post-ingestion
2. Lactulose 20-30g PO/NG q6h — target 2-3 soft stools/day
3. Rifaximin 550mg BID
4. LIVER TRANSPLANT EVALUATION: IMMEDIATE referral — King's College criteria borderline
5. Avoid hepatotoxic drugs. Avoid benzodiazepines.
6. Nutrition: low-sodium diet, phosphate repletion
7. Monitor q4h: INR, glucose, lactate, Cr, ammonia
8. ICU. Hepatology + Transplant Surgery co-management.
""",
    },
    {
        "id": "transcript-018",
        "encounter_type": "Emergency Department",
        "condition": "Anaphylaxis",
        "icd10_primary": "T78.2XXA",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-06-14   TIME: 13:50   PROVIDER: Dr. Jordan Lee, MD (Emergency Medicine)

CC: Acute urticaria, throat swelling, hypotension 10 minutes after penicillin injection

HPI: 35 yo M developed acute generalised urticaria, throat tightness, and stridor approximately
10 minutes after receiving Amoxicillin 500mg IM at an urgent care clinic for suspected strep throat.
EMS called. Epinephrine 0.3mg IM given by EMS en route — partial response.
No prior anaphylaxis. No known penicillin allergy (first exposure). PMH: nil.

EMS vitals: BP 78/44, HR 124, SpO2 88% on room air.

On arrival: BP 84/52 | HR 118 | RR 24 | SpO2 91% | Temp 37.3°C

EXAM: Generalised urticaria, angioedema of lips/tongue, stridor on inspiration.
Lungs: diffuse bilateral wheezing. Extremities: flushed, warm. No signs of laryngeal closure.

LABS: Tryptase 42 µg/L [ELEVATED — confirm anaphylaxis] | CBC/CMP normal | Glu 118

ASSESSMENT:
1. Anaphylaxis — penicillin-induced, grade III — T78.2XXA
   Systemic: urticaria, bronchospasm, hypotension, angioedema. IgE-mediated.
2. Anaphylactic shock — distributive

PLAN:
1. EPINEPHRINE 0.3mg IM (lateral thigh) — REPEAT DOSE immediately (EMS gave 1 dose)
2. IV access x2. Normal saline 1L bolus STAT (distributive shock)
3. Diphenhydramine 50mg IV + Ranitidine 50mg IV (H1+H2 blockade)
4. Methylprednisolone 125mg IV (corticosteroid — prevent biphasic reaction)
5. Salbutamol 2.5mg neb (bronchospasm)
6. If further stridor: prepare for RSI/intubation (ENT on standby)
7. Observe minimum 6h after last epinephrine dose (biphasic reaction risk)
8. Prescribe Epinephrine autoinjector (EpiPen 0.3mg) x2 at discharge
9. Document PENICILLIN ALLERGY (IgE-mediated anaphylaxis) permanently
10. Immunology/allergy follow-up for penicillin desensitisation evaluation
""",
    },
    {
        "id": "transcript-019",
        "encounter_type": "Inpatient — Nephrology",
        "condition": "Hyponatraemia — SIADH",
        "icd10_primary": "E22.2",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-07-25   TIME: 08:00   PROVIDER: Dr. Elaine Zhao, MD (Nephrology)

CC: Confusion, nausea, and falls x 2 days

HPI: 81 yo F with recent onset confusion, nausea, and two unwitnessed falls at home.
Daughter reports gradual worsening over 2 days. Recently started sertraline (SSRI) 6 weeks ago
for depression. Also takes hydrochlorothiazide for HTN. No vomiting, diarrhoea, or excess water
intake. No known malignancy. Recent CXR 3 months ago normal.

VS: BP 118/70 | HR 82 | RR 16 | Temp 36.8°C | SpO2 97% RA | Wt 58kg

EXAM: Mildly confused — disoriented to date. Mucous membranes moist. No orthostasis. No oedema.
No JVD. Euvolaemic on exam.

LABS:
Na: 118 mEq/L [CRITICALLY LOW] | K: 3.8 | Cl 82 | HCO3 22
Plasma osmolality: 248 mOsm/kg [LOW] | Urine osmolality: 432 mOsm/kg [HIGH — inappropriate]
Urine Na: 68 mEq/L [HIGH — renal Na wasting] | Urine Cl: 62
TSH: 2.1 [normal] | Cortisol (AM): 22 µg/dL [normal]
Cr 0.8 | Glu 92 | Albumin 3.8 | Liver function: normal

ASSESSMENT:
1. Severe Symptomatic Hyponatraemia — Na 118, symptomatic (confusion, falls) — E22.2
2. SIADH — euvolaemic, urine Osm >plasma Osm, urine Na >40 mEq/L
   Likely aetiology: SSRI (sertraline) — most common drug-induced SIADH in elderly
   Secondary: thiazide diuretic (HCT contributing)

PLAN:
1. STOP SERTRALINE immediately. STOP HCTZ.
2. Fluid restriction: 800-1000mL/day
3. Correction target: raise Na 6-8 mEq/L per 24h ONLY (avoid osmotic demyelination — max 10 mEq/L/24h)
4. Hypertonic saline (3% NaCl): 1mL/kg/hr for symptomatic hyponatraemia — check Na q2h
5. Monitor q4h BMP. Urine Na and osmolality q6h.
6. When Na >125 and asymptomatic: stop 3% saline, continue fluid restriction only.
7. Psychiatry re: alternative antidepressant (mirtazapine — low SIADH risk)
8. Neurology consult if rapid overcorrection occurs.
""",
    },
    {
        "id": "transcript-020",
        "encounter_type": "Inpatient — Cardiology",
        "condition": "Deep Vein Thrombosis — Proximal",
        "icd10_primary": "I82.401",
        "data_tag": "SYNTHETIC",
        "text": """DATE: 2025-05-29   TIME: 11:00   PROVIDER: Dr. Ama Asante, MD (Haematology / Vascular Medicine)

CC: Right leg swelling, pain, and redness x 3 days

HPI: 48 yo M with 3-day h/o right lower leg swelling, pain (aching, 5/10), and erythema.
Worsening with weight-bearing. Recent flight from Los Angeles to London (11h) 1 week ago. BMI 31.
No trauma. No malignancy history. No prior VTE. No family history of DVT. Non-smoker.
No dyspnoea or pleuritic chest pain (PE excluded clinically today).

VS: BP 132/82 | HR 74 | RR 16 | SpO2 99% RA

EXAM: Right calf circumference 4cm > left. Pitting oedema right calf to mid-thigh. Erythema
extending from ankle to mid-calf. Tenderness along course of popliteal and femoral veins.
No skin ulceration.

LABS:
D-dimer: 2.8 µg/mL [ELEVATED] | CBC: WBC 8.2 | Hgb 15.0 | Plt 264 [all normal]
CMP: Cr 0.9 | all normal
Thrombophilia screen: ordered — to be done AFTER stopping anticoagulation

Doppler Ultrasound Right Leg: Acute DVT — right popliteal + superficial femoral veins (proximal DVT).
CTPA: Negative for pulmonary embolism.

Wells DVT Score: 5 (high probability) → confirmed by US.

ASSESSMENT:
1. Proximal Deep Vein Thrombosis — right popliteal + femoral veins — I82.401
   Provoked: post-long-haul flight. No PE on CT.
2. Risk assessment: CHA2DS2-VASc-equivalent: isolated provoked VTE — 3-month anticoagulation plan

PLAN:
1. Anticoagulation: Apixaban 10mg PO BID x7 days → 5mg PO BID x3 months (provoked DVT standard)
2. Graduated compression stockings (30-40mmHg) right leg
3. Ambulate with stockings — bed rest NOT indicated (early mobilisation preferred)
4. Thrombophilia testing: defer to 3 months post-anticoagulation (avoid false results)
5. Oncology screen (age-appropriate + new VTE): PSA, CBC, CXR, colonoscopy referral
6. Return if dyspnoea, chest pain, coughing blood — PE instructions given
7. Follow-up haematology clinic at 3 months to reassess anticoagulation duration
""",
    },
]


def write_files() -> None:
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, rec in enumerate(_TRANSCRIPTS, start=1):
        fname = _OUT_DIR / f"note_{i:03d}.txt"
        header = (
            f"encounter_id: {rec['id']}\n"
            f"encounter_type: {rec['encounter_type']}\n"
            f"condition: {rec['condition']}\n"
            f"icd10_primary: {rec['icd10_primary']}\n"
            f"data_tag: {rec['data_tag']}\n"
            f"---\n"
        )
        fname.write_text(header + rec["text"].lstrip("\n"), encoding="utf-8")
        print(f"  wrote {fname.name}")
    print(f"transcripts: {len(_TRANSCRIPTS)} files → {_OUT_DIR}")


if __name__ == "__main__":
    write_files()
