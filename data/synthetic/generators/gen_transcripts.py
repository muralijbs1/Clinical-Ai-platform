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

    # ── NEW BALANCED ADDITIONS (notes 21–26): outpatient, preventive, paediatric, OB, geriatric, mental health ──

    {
        "id": "transcript-021",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Annual Wellness Visit — Preventive Care",
        "icd10_primary": "Z00.00",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-04-10   TIME: 09:30   PROVIDER: Dr. Rachel Torres, MD (Family Medicine)

CC: Annual wellness visit

HPI: 42 yo F presents for annual health maintenance. No acute complaints. Last physical 18 months ago.
Reports mild fatigue over the past 3 months, improved with better sleep hygiene. Regular menses.
No chest pain, palpitations, dyspnoea, GI complaints, or urinary symptoms.

ROS: Positive: mild fatigue (improved). Negative: all systems otherwise negative on 14-system review.

PMH: Migraine (well-controlled) | Mild depression (in remission x2 years, no medications)
PSH: Appendectomy 2015
FHx: Mother: breast cancer (dx age 58, BRCA unknown). Father: HTN, DM2.
SHx: Teacher. Married, 2 children. Non-smoker. Occasional alcohol (2 units/week). No illicit drugs.
Meds: Sumatriptan 50mg PRN (used <2x/month). Multivitamin.
Allergies: NKDA.

VITAL SIGNS: BP 118/74 | HR 68 | RR 14 | Temp 36.6°C | SpO2 99% | Wt 64kg | BMI 23.8

PHYSICAL EXAM:
General: Well-appearing, healthy female in no distress.
HEENT: Normal. Thyroid non-palpable.
Cardiovascular: RRR, no murmurs. Peripheral pulses intact.
Respiratory: Clear bilaterally.
Abdomen: Soft, non-tender. No organomegaly.
Breast: No discrete masses, no axillary lymphadenopathy.
Pelvic: Deferred — last PAP 14 months ago (normal).
Skin: No suspicious lesions. SPF counselled.
Neurological: No focal deficits.

INVESTIGATIONS (ordered today):
Fasting lipid panel: TC 188, LDL 112, HDL 58, TG 90 — within target, no action.
HbA1c: 5.4% — normal.
TSH: 2.1 — normal.
Mammogram: due (age 42, maternal FHx) — ordered.
Cervical smear: up-to-date (next due 2026).
Colorectal cancer screen: deferred — age 42, screen at 45 per USPSTF.
Skin self-examination: counselled; dermatology referral offered (maternal FHx melanoma? — no, breast cancer).

ASSESSMENT:
1. Healthy adult female — preventive care visit
2. Migraine — well-controlled
3. Depression — sustained remission, no medications required
4. Maternal FHx breast cancer — genetic counselling offered; BRCA testing discussed

PLAN:
1. Mammogram ordered — results to follow up in 2 weeks
2. Continue sumatriptan PRN — review if frequency increases
3. PHQ-9 completed: score 2 — minimal depression; no treatment change
4. Genetic counselling referral offered for BRCA testing — patient will consider
5. Diet and exercise counselled — Mediterranean diet encouraged
6. Vaccines: Tdap booster (due), influenza (seasonal), COVID-19 booster — administered today
7. Follow-up: annual wellness visit in 12 months or sooner PRN
""",
    },
    {
        "id": "transcript-022",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Chronic Disease Management — Asthma Review",
        "icd10_primary": "J45.40",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-05-19   TIME: 14:15   PROVIDER: Dr. Mark Chen, MD (Internal Medicine)

CC: Asthma routine review — 6-month check

HPI: 31 yo M with moderate persistent asthma presents for scheduled 6-month review. Overall good
control over the past 3 months since step-up to ICS/LABA. Reports 1-2 SABA uses/week (down from
daily), no night-time symptoms. One mild exacerbation 4 months ago — managed by GP with 5-day
prednisolone, no hospitalisation. Exercise tolerance improved — back to gym 3x/week.

ROS: Positive: mild rhinitis (seasonal). Negative: no wheeze at rest, no chest tightness at night,
no cough productive of sputum, no recent viral URTI.

PMH: Moderate persistent asthma (dx age 12) | Allergic rhinitis
PSH: None
FHx: Mother: asthma. Father: eczema.
SHx: Software developer. Non-smoker. No pets. Dust mite allergy confirmed (RAST +++).
Meds: Fluticasone/salmeterol 250/25 BD (Accuhaler) | Salbutamol MDI PRN | Cetirizine 10mg QD
Allergies: Aspirin (bronchospasm) — NSAIDs AVOIDED.

VITAL SIGNS: BP 122/78 | HR 72 | RR 15 | Temp 36.7°C | SpO2 99% | Peak flow: 540 L/min (pred 560)

SPIROMETRY (today):
FEV1: 84% predicted (prev 79% — improved) | FVC: 96% | FEV1/FVC: 0.81
Post-bronchodilator reversibility: +8% — mild residual reversibility
FeNO: 24 ppb (previously 38 — improved with ICS adherence)

PHYSICAL EXAM:
Chest: Good air entry bilaterally. Mild end-expiratory wheeze on forced expiration. No recession.
Nose: Inferior turbinate hypertrophy. No polyps.

ASTHMA CONTROL TEST (ACT): Score 20/25 — well-controlled.
INHALER TECHNIQUE: Checked — adequate. Spacer used with MDI.

ASSESSMENT:
1. Moderate persistent asthma — well-controlled on Step 3 therapy
2. Allergic rhinitis — seasonally active
3. Improved lung function with ICS adherence

PLAN:
1. Continue fluticasone/salmeterol 250/25 BD — do not step down yet (one exacerbation 4 months ago)
2. Intranasal fluticasone spray for rhinitis — added
3. Dust mite avoidance measures reinforced (mattress covers, HEPA filters)
4. Written asthma action plan updated
5. Allergen immunotherapy: discussed, patient declines for now
6. Salbutamol prescription renewed — use <3x/week target
7. Flu vaccine administered today (asthma indication)
8. Review in 6 months or if ACT <16 or 2+ SABA uses/week
""",
    },
    {
        "id": "transcript-023",
        "encounter_type": "Outpatient — Paediatrics",
        "condition": "Paediatric Febrile UTI — 4-year-old Female",
        "icd10_primary": "N10",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-06-04   TIME: 10:00   PROVIDER: Dr. Alicia Nwosu, MD (Paediatrics)

CC: Fever and crying on urination — 3 days

HPI: 4 yo F brought by mother with 3-day history of high-grade fever (max 39.2°C at home), crying
during urination, increased urinary frequency, and two episodes of bedwetting (previously dry for 18
months). No vomiting. Mild abdominal pain (suprapubic). No rash.

ROS: Positive: fever, dysuria, frequency, bedwetting, suprapubic pain. Negative: no diarrhoea,
no flank pain, no skin rash, no joint swelling.

PMH: None. Fully vaccinated per schedule. No prior UTI.
FHx: No known vesicoureteral reflux in family.
SHx: Attends nursery. Non-potty-trained sibling at home.
Meds: Paracetamol PRN. No antibiotics.
Allergies: NKDA.

VITAL SIGNS: Temp 38.8°C | HR 128 | RR 26 | BP 96/58 | SpO2 98% | Wt 16.4kg

PHYSICAL EXAM:
General: Febrile, mildly uncomfortable. Alert and interactive.
Abdomen: Soft. Mild suprapubic tenderness. No costovertebral angle tenderness. No organomegaly.
Genitalia: Normal external genitalia. No vulvovaginitis.
CNS: Alert, appropriate for age. No neck stiffness.

INVESTIGATIONS:
Urine dipstick (MSU): Leukocytes +++, Nitrites +, Blood +
Urine microscopy: WBC 50/hpf, RBC 10/hpf, bacteria seen
Urine C&S: sent (Escherichia coli 10⁵ cfu/mL, pan-sensitive — confirmed 48h)
FBC: WBC 14.2, Neutrophils 11.8 | CRP: 64 mg/L
Renal function: Normal (eGFR adequate for age)
Renal ultrasound: Normal — no hydronephrosis, normal bladder (no post-void residual)

ASSESSMENT:
1. Febrile urinary tract infection (pyelonephritis) — 4-year-old female
2. E. coli — pan-sensitive

PLAN:
1. Oral trimethoprim-sulfamethoxazole (per weight-based dosing) x 7 days — first-line per local guidelines
2. Antipyretics: paracetamol 15mg/kg q6h PRN; ibuprofen alternating if needed
3. Adequate oral fluids — ensure hydration; monitor for vomiting
4. Repeat MSU after completion to confirm clearance
5. VCUG (voiding cystourethrogram): NOT routinely indicated post-first UTI per current AAP/NICE guidelines
   — defer unless recurrent or atypical features
6. DMSA scan: consider if recurrent or evidence of scarring at follow-up
7. Return if worsening, persistent fever >48h on antibiotics, or unable to tolerate oral medications
8. Parental education: perineal hygiene, adequate voiding habits, hydration
""",
    },
    {
        "id": "transcript-024",
        "encounter_type": "Inpatient — Obstetrics",
        "condition": "Gestational Hypertension — 34 Weeks Gestation",
        "icd10_primary": "O13.4",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-07-14   TIME: 16:40   PROVIDER: Dr. Angela Foster, MD (Obstetrics & Gynaecology)

CC: Elevated blood pressure — 34 weeks gestation, referred from community midwife

HPI: 29 yo G1P0 at 34+2 weeks gestation presents following two elevated BP readings at community
midwife appointment (158/98 and 162/101 at 30-minute interval). No headache, visual disturbance,
epigastric pain, or facial oedema. Fetal movements normal. No vaginal bleeding or fluid loss.
No prior hypertension. BP at 16-week booking visit: 110/70.

ROS: Positive: ankle swelling (bilateral, mild — 2 weeks). Negative: no headache, no visual changes,
no right upper quadrant pain, no nausea/vomiting, no dyspnoea.

PMH: None. No pre-existing hypertension. No diabetes.
PSH: None. This is first pregnancy.
FHx: Mother: gestational hypertension in 2 pregnancies. No cardiac history.
SHx: Accountant. Lives with partner. Non-smoker. No alcohol in pregnancy.
Meds: Folic acid (stopped at 12 weeks), Vitamin D 400 IU QD. Low-dose aspirin 75mg (started 13 weeks).
Allergies: NKDA.

VITAL SIGNS: BP 160/100 (confirmed on second reading) | HR 84 | RR 16 | Temp 36.8°C | SpO2 99%

PHYSICAL EXAM:
General: Alert, comfortable. No facial oedema.
Cardiovascular: Normal heart sounds. BP bilateral arms equal.
Respiratory: Clear.
Abdomen: Gravid uterus — fundal height 33cm. Fetal presentation: cephalic, 2/5 palpable.
No uterine tenderness.
Extremities: 1+ pitting oedema bilateral ankles — non-pitting on pressure.
Reflexes: Normal — no clonus.

INVESTIGATIONS:
Urine dipstick: Protein trace (repeat MSU sent)
Spot urinary protein:creatinine ratio: 24 mg/mmol (below 30 threshold for proteinuria)
FBC: Hb 11.8, Platelets 198K, WBC 9.2
LFTs: ALT 22, AST 18, Bilirubin 0.4 — normal
Urea & electrolytes: Normal. Creatinine 62.
Uric acid: 0.38 mmol/L (mildly elevated, non-specific)
LDH: 182 U/L — normal
CTG: Reactive — normal fetal heart rate pattern
Fetal USS: BPP 8/8. Estimated fetal weight 2,180g (30th centile — appropriate for gestation).
Umbilical artery Dopplers: Normal flow.

ASSESSMENT:
1. Gestational hypertension at 34 weeks — BP ≥140/90 without proteinuria
2. Fetal growth appropriate; no fetal compromise

PLAN:
1. Admit for observation and BP monitoring q4h
2. Antihypertensive therapy: Labetalol 200mg BD oral — initiate (target BP 130-150/80-100)
3. Antenatal corticosteroids: Betamethasone 12mg IM x2 doses (24h apart) — fetal lung maturity (34 weeks)
4. Magnesium sulphate: NOT indicated currently (no severe features, no preeclampsia)
5. Continuous CTG monitoring x6h, then intermittent if stable
6. Repeat bloods (FBC, LFTs, renal, LDH) in 24h
7. Consultant review: if BP refractory, if proteinuria develops, or if fetal concerns
8. Delivery plan: aim 37 weeks if stable; expedited if severe hypertension, HELLP criteria, or fetal compromise
9. Aspirin continued until delivery
""",
    },
    {
        "id": "transcript-025",
        "encounter_type": "Outpatient — Geriatrics",
        "condition": "Comprehensive Geriatric Assessment — Recurrent Falls",
        "icd10_primary": "Z87.39",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-08-20   TIME: 11:00   PROVIDER: Dr. Priya Anand, MD (Geriatric Medicine)

CC: Comprehensive Geriatric Assessment — referred by GP for recurrent falls and functional decline

HPI: 82 yo M referred by his GP following 3 falls in the past 4 months. One fall resulted in a right
wrist fracture (treated conservatively). Lives alone since wife's death 8 months ago. Family reports
increased confusion over the past 6 months. Previously independent for all ADLs; now requires help
with shopping and meal preparation. No LOC during falls.

ROS: Positive: falls, functional decline, mild confusion, fatigue, reduced appetite, constipation.
Negative: no chest pain, no syncope, no dyspnoea, no urinary incontinence.

PMH: Hypertension (30 years) | CKD stage 3a (eGFR 52) | BPH | Osteoporosis (DEXA confirmed)
Ischaemic heart disease (PCI 2018) | Hearing impairment (bilateral, moderate)
PSH: CABG 2009, right knee arthroplasty 2020
FHx: Father: dementia. Mother: osteoporosis.
SHx: Retired teacher. Lives alone, ground floor flat. No steps. One adult son — visits weekly.
Meds (12 total): Amlodipine 10mg | Bisoprolol 5mg | Ramipril 5mg | Furosemide 40mg
  Aspirin 75mg | Atorvastatin 40mg | Tamsulosin 0.4mg | Alendronate 70mg weekly
  Calcium + Vit D | Omeprazole 20mg | Zopiclone 7.5mg (nightly — GP started 3 months ago)
  Ferrous sulfate 200mg BD (new, iron-deficiency anaemia)
Allergies: Penicillin (rash).

VITAL SIGNS: BP 144/84 sitting, 128/76 standing (orthostatic drop 16/8 — significant)
HR 58 (bradycardia on bisoprolol) | RR 14 | Temp 36.5°C | SpO2 97% | Wt 68kg | BMI 22.1

FUNCTIONAL ASSESSMENT:
Barthel Index: 65/100 (bathing, dressing partially dependent)
Timed Up and Go (TUG): 22 seconds (>12s = high fall risk) — uses walking stick
Grip strength (dynamometer): 18kg right, 20kg left (below threshold for age)
Gait: Wide-based, shortened stride. No festination. No parkinsonian features.

COGNITIVE ASSESSMENT:
MMSE: 22/30 — deficits: orientation to date (-2), delayed recall (-3), visuospatial (-1)
Clock Drawing Test: 3/4 — minor spatial error
MoCA: 20/30 (referred for formal neuropsychology)

VISION: Bilateral cataracts — reduced visual acuity corrected to 6/18. Ophthalmology referral pending.
HEARING: Bilateral moderate hearing loss — wearing aids inadequately (sizing issue).

INVESTIGATIONS:
FBC: Hb 11.2 (mild anaemia — iron deficiency on treatment) | Platelets 198 | WBC 6.8
Renal: Creatinine 118, eGFR 52, Na 138, K 4.1 (stable CKD)
Calcium: 2.28 (normal on supplementation) | Vitamin D 25-OH: 52 nmol/L (sufficient)
TSH: 2.8 (normal) | HbA1c: 5.6% (no diabetes)

POLYPHARMACY REVIEW:
HIGH-RISK MEDICATIONS IDENTIFIED:
⚠ Zopiclone: benzodiazepine-receptor agonist — fall risk +++ in elderly; STOP (started 3 months ago)
⚠ Tamsulosin: alpha-blocker — orthostatic hypotension; orthostatic drop 16mmHg confirmed; REVIEW dose
⚠ Bisoprolol 5mg: HR 58 — bradycardia may contribute to fall risk; cardiology review for dose reduction
⚠ Furosemide: orthostatic risk; check if still indicated (no current HF decompensation signs)
⚠ Alendronate: CKD eGFR 52 — borderline; acceptable but monitor renal function

ASSESSMENT:
1. Recurrent falls — multifactorial: orthostatic hypotension, polypharmacy (zopiclone, tamsulosin),
   visual impairment, reduced muscle strength, cognitive impairment
2. Mild cognitive impairment — possible early dementia (formal assessment pending)
3. Frailty — Clinical Frailty Scale: 5/9 (mildly frail)
4. Osteoporosis — continue alendronate; ensure calcium/Vit D adequate

PLAN:
1. STOP zopiclone — taper over 2 weeks to avoid withdrawal; offer sleep hygiene advice
2. REDUCE tamsulosin to 0.4mg QD (was BD? — confirm with GP); review in 4 weeks for orthostatic BP
3. Cardiology referral — bisoprolol dose review (HR 58 on 5mg)
4. PHYSIOTHERAPY referral — strength and balance programme (evidence: reduces falls 35%)
5. OCCUPATIONAL THERAPY — home hazard assessment, bathroom grab rails, shower chair
6. Ophthalmology — fast-track cataract assessment (visual impairment is modifiable fall risk)
7. Hearing aid review — ENT/audiology for resizing
8. Nutrition: dietitian referral — BMI 22.1 declining (1 year ago BMI 24.3); high-protein diet
9. Neuropsychology referral — formal cognitive assessment for dementia workup
10. Advance care planning discussion initiated — patient agreeable to GP-held anticipatory care plan
11. DEXA repeat in 2 years; fracture liaison service notification for wrist fracture
12. Review in 3 months post-medication changes and physio assessment
""",
    },
    {
        "id": "transcript-026",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Major Depressive Disorder — Moderate Severity",
        "icd10_primary": "F32.1",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-09-09   TIME: 15:30   PROVIDER: Dr. Samuel Adeyemi, MD (Family Medicine / Mental Health)

CC: Persistent low mood, fatigue, and difficulty functioning at work — 8 weeks

HPI: 39 yo F presents with 8-week history of persistent low mood, anhedonia, fatigue, poor sleep
(early morning waking), reduced appetite (4kg weight loss), difficulty concentrating at work, and
feelings of hopelessness. Reports being passed over for a promotion 9 weeks ago. No history of mania,
psychosis, or mixed episodes. No hallucinations. PHQ-9 today: 16/27 (moderately severe depression).
Denies suicidal ideation currently — has had passive thoughts of "not wanting to be here" but no
plans, intent, or means. Has a supportive partner and two children.

ROS: Positive: depressed mood, anhedonia, fatigue, insomnia (early waking), poor appetite,
weight loss 4kg, poor concentration. Negative: no mania, no psychosis, no substance use.

PMH: Anxiety disorder (treated with CBT 4 years ago — good response) | Hypothyroidism (well-controlled)
PSH: None
FHx: Mother: depression (treated). No family history of bipolar disorder or suicide.
SHx: Marketing manager. Married. 2 children (ages 7 and 10). Non-smoker. Occasional alcohol (4 units/week).
Meds: Levothyroxine 75mcg QD.
Allergies: NKDA.

VITAL SIGNS: BP 116/74 | HR 76 | RR 14 | Temp 36.6°C | SpO2 99% | Wt 61kg (was 65kg 2 months ago)

PHYSICAL EXAM:
General: Well-dressed, soft-spoken. Mildly restricted affect. Appropriate eye contact.
Psychomotor: No agitation or retardation. Speech rate and volume normal.
No physical findings contributory.

INVESTIGATIONS:
TSH: 1.6 (well-controlled hypothyroidism on current levothyroxine dose)
FBC: Normal. Hb 12.8. No anaemia.
Ferritin: 42 (normal). Vitamin D: 48 nmol/L (low — supplementation started).
HbA1c: 5.5% (no diabetes).

RISK ASSESSMENT:
Suicidal ideation: Passive — "not wanting to be here" but NO plan, NO intent, NO means identified.
Protective factors: Supportive partner, children, engaged in assessment, help-seeking.
Risk level: MODERATE — outpatient management appropriate with safety planning.
Safety plan documented — agreed with patient. Emergency contact: partner (notified and engaged).

ASSESSMENT:
1. Major depressive disorder — moderate severity (PHQ-9 16, 8-week duration, functional impairment)
2. Hypothyroidism — well-controlled (not contributing to depression)
3. Vitamin D insufficiency — secondary
4. Moderate suicide risk — outpatient safe with safety plan

PLAN:
1. Sertraline 50mg QD — start today. Review in 4 weeks (increase to 100mg if partial response).
   Counselled: 2-4 weeks for effect; may feel more anxious initially; do NOT stop abruptly.
2. Referral to CBT (individual therapy) — prior good response; psychological therapy + medication
   evidence superior to either alone for moderate MDD.
3. Vitamin D 1,000 IU QD supplementation
4. Safety planning: crisis line number given. Partner engaged. Return to ED if thoughts become active.
5. Sick note provided for 2 weeks — reduce work stress while initiating treatment.
6. Sleep hygiene education: fixed wake time, limit screen use after 9pm, avoid daytime napping.
7. Follow-up: 4 weeks (response assessment PHQ-9), sooner if worsening.
8. PHQ-9 tracking at every visit. Escalation plan if no response at 8 weeks.
""",
    },

    # ── DOUBLING BATCH: transcripts 027–052 ──

    {
        "id": "transcript-027",
        "encounter_type": "Emergency Department",
        "condition": "Acute Pulmonary Embolism",
        "icd10_primary": "I26.99",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-01-22   TIME: 14:30   PROVIDER: Dr. Aisha Nkemdirim, MD (Emergency Medicine)

CC: Sudden-onset dyspnoea and pleuritic chest pain — 4 hours

HPI: 48 yo F presents with acute-onset right-sided pleuritic chest pain and dyspnoea starting 4h ago at
rest. No trauma. Returned from 11-hour flight 36 hours ago. Mild right calf swelling noted for 3 days.
No haemoptysis. Heart rate elevated on self-check at home.

ROS: Positive: dyspnoea, pleuritic chest pain, right leg swelling. Negative: no fever, no cough productive.

PMH: Oral contraceptive pill (10 years) | Hypertension | PSH: None | FHx: Mother: DVT.
SHx: Accountant. Non-smoker. Long-haul flight 36h ago.
Meds: Combined OCP | Amlodipine 5mg QD. Allergies: NKDA.

VITAL SIGNS: BP 118/76 | HR 112 | RR 22 | Temp 37.2°C | SpO2 93% on air | BMI 26.4

PHYSICAL EXAM: Tachycardic. Chest: reduced air entry right base, no wheeze. Right calf: warm,
tender, 3cm circumference difference. No DVT erythema. JVP not elevated.

INVESTIGATIONS:
CTPA: Right lower lobe segmental and subsegmental PE. No RV strain.
D-dimer: 6,400 ng/mL. Troponin: 18 ng/L (normal). BNP 42 pg/mL. ABG: pO2 8.2, pCO2 32.
Doppler USS right leg: proximal DVT confirmed (popliteal–femoral).
ECG: Sinus tachycardia. S1Q3T3 pattern.

ASSESSMENT:
1. Acute pulmonary embolism — segmental, haemodynamically stable (intermediate-low risk)
2. Proximal DVT — right lower limb
3. Predisposing factors: OCP + long-haul flight

PLAN:
1. Anticoagulation: rivaroxaban 15mg BD × 21 days → 20mg QD × 3 months minimum
2. OCP: STOP immediately — switch to progesterone-only or non-hormonal contraception
3. O2 via nasal cannula to maintain SpO2 >95%
4. Admit — observe 24h (intermediate-low risk; RV function normal)
5. Thrombophilia screen: defer 3 months post-anticoagulation
6. Outpatient haematology follow-up at 3 months for duration decision
""",
    },
    {
        "id": "transcript-028",
        "encounter_type": "Emergency Department",
        "condition": "Hypertensive Emergency with Acute End-Organ Damage",
        "icd10_primary": "I16.1",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-02-08   TIME: 09:15   PROVIDER: Dr. Marcus Lee, MD (Emergency Medicine)

CC: Severe headache, blurred vision, BP 230/138

HPI: 63 yo M brought by wife with 6-hour history of severe occipital headache, blurred vision in both
eyes, and one episode of vomiting. Known hypertension — non-adherent to medications for 3 months ("ran
out"). Denied chest pain or focal neurological symptoms.

ROS: Positive: severe headache, blurred vision, vomiting. Negative: no chest pain, no focal neuro deficit.

PMH: HTN (10 years) | CKD stage 2 | PSH: None | FHx: Father: stroke. SHx: Retired mechanic. Smoker 20pk.
Meds: Amlodipine 10mg + lisinopril 10mg (not taking). Allergies: NKDA.

VITAL SIGNS: BP 230/138 | HR 88 | RR 16 | Temp 36.7°C | SpO2 97% | BMI 29.4

PHYSICAL EXAM: Alert, distressed. Fundoscopy: bilateral papilloedema, flame haemorrhages.
Neuro: grossly intact — no focal deficits. Chest: clear. No peripheral oedema.

INVESTIGATIONS:
ECG: LVH (Sokolow-Lyon 48mm). CT head: no haemorrhage, no infarct.
Creatinine: 2.1 mg/dL (baseline 1.4 — acute rise). Urinalysis: protein 3+ (dysmorphic RBCs).
BNP: 620. Troponin: 32 (mildly elevated).

ASSESSMENT:
1. Hypertensive emergency — malignant phase (papilloedema, AKI, proteinuria)
2. Acute kidney injury on CKD2 — hypertensive nephropathy
3. Non-adherence to antihypertensives — primary cause

PLAN:
1. IV labetalol infusion: reduce MAP by 20-25% over 2 hours (target ~170/100, avoid overcorrection)
2. Avoid oral nifedipine (uncontrolled BP drop risk)
3. Nephrology urgent consult — possible renal biopsy if AKI persists
4. Resume amlodipine + lisinopril on discharge; add spironolactone
5. Ophthalmology urgent review — papilloedema
6. Smoking cessation counselling and medication prescribed
""",
    },
    {
        "id": "transcript-029",
        "encounter_type": "Emergency Department",
        "condition": "Acute Pancreatitis — Gallstone Aetiology",
        "icd10_primary": "K85.10",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-03-14   TIME: 22:45   PROVIDER: Dr. Priya Patel, MD (Emergency Medicine)

CC: Severe epigastric and back pain, nausea, vomiting — 8 hours

HPI: 45 yo M presents with 8-hour history of severe constant epigastric pain radiating to the back,
nausea, and 3 episodes of vomiting. Onset after a heavy fatty meal. Pain severity 9/10.
Known cholelithiasis on USS 2 years ago — not followed up.

ROS: Positive: epigastric pain, back radiation, nausea, vomiting. Negative: no jaundice, no fever.

PMH: Cholelithiasis | BMI 31 | PSH: None | FHx: Father: gallstones. SHx: Lorry driver. Alcohol: 14 units/week.
Meds: None. Allergies: NKDA.

VITAL SIGNS: BP 126/82 | HR 104 | RR 18 | Temp 38.0°C | SpO2 97% | BMI 30.8

PHYSICAL EXAM: Distressed. Abdomen: epigastric tenderness with guarding. Bowel sounds present.
No jaundice. No Cullen's or Grey Turner's signs.

INVESTIGATIONS:
Amylase: 1,840 U/L. Lipase: 4,220 U/L. WBC 14.2. CRP 148 (will rise).
ALT 288, ALP 312, bilirubin 2.1 — biliary pattern.
Ultrasound: gallstones + CBD 9mm (borderline dilated). Pancreas not well-visualised.
CT abdomen: pancreatic oedema — no necrosis. Revised Atlanta: moderately severe.

ASSESSMENT:
1. Acute pancreatitis — gallstone aetiology (Modified Glasgow score 2)
2. Possible choledocholithiasis — CBD dilation, raised LFTs

PLAN:
1. Nil by mouth. IV fluids: Ringer's lactate 250mL/h × 48h (aggressive early resuscitation)
2. Analgesia: morphine 5mg IV PRN + IV paracetamol
3. Antiemetics: ondansetron IV
4. MRCP within 48h — CBD stone assessment; ERCP if confirmed
5. Surgery consult — laparoscopic cholecystectomy after recovery (same admission if mild)
6. Alcohol assessment and brief intervention — 14 units/week is a secondary risk factor
7. Strict NPO until pain resolves + lipase trending down
""",
    },
    {
        "id": "transcript-030",
        "encounter_type": "Emergency Department",
        "condition": "Diabetic Ketoacidosis — New Diagnosis Type 1 DM",
        "icd10_primary": "E10.10",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-04-19   TIME: 03:20   PROVIDER: Dr. James Okafor, MD (Emergency Medicine)

CC: Nausea, vomiting, polyuria, polydipsia — 3 days. Confused tonight.

HPI: 22 yo F brought by housemate. 3 days of polyuria, polydipsia, nausea and vomiting.
Worsening confusion over last 4 hours. No prior diabetes diagnosis. No recent illness.
Fruity breath noted by housemate.

ROS: Positive: polyuria, polydipsia, nausea, vomiting, confusion, weight loss 3kg.
Negative: no fever, no diarrhoea, no trauma.

PMH: None | PSH: None | FHx: Father: Type 1 DM. SHx: University student. Non-smoker.
Meds: None. Allergies: NKDA.

VITAL SIGNS: BP 102/64 | HR 124 | RR 26 | Temp 36.9°C | SpO2 98% | Wt 58kg | BMI 20.4

PHYSICAL EXAM: Drowsy (GCS 14). Dry mucous membranes. Kussmaul breathing.
Fruity acetone breath. Abdomen: mild diffuse tenderness. No peritonism.

INVESTIGATIONS:
VBG: pH 7.24, HCO3 12, BE -14, glucose 28.4 mmol/L, ketones 4.8 mmol/L.
Na 128 (corrected 134), K 5.8 (total body depleted), Creatinine 1.4.
HbA1c: 11.2%. C-peptide: undetectable. Anti-GAD antibodies: positive.
ECG: sinus tachycardia. No peaked T-waves (K+ 5.8 — monitor closely).

ASSESSMENT:
1. Diabetic ketoacidosis — new diagnosis Type 1 DM
2. Severe dehydration (estimated 5-8% deficit)

PLAN:
1. Fixed-rate IV insulin infusion 0.1 units/kg/h (6 units/h). Check glucose hourly.
2. IV fluids: 0.9% NaCl 1L over 1h, then 500mL/h × 4h per DKA protocol
3. Potassium replacement: add K+ to IV fluids once urine output confirmed and K <5.5
4. Glucose: add 10% dextrose when glucose <14 mmol/L (do not stop insulin)
5. Cardiac monitoring — hypokalaemia risk as insulin shifts K intracellularly
6. Endocrinology consult — Type 1 DM initiation; insulin education
7. Switch to SC insulin when pH >7.3, HCO3 >18, ketones <0.6
""",
    },
    {
        "id": "transcript-031",
        "encounter_type": "Emergency Department",
        "condition": "Vasovagal Syncope",
        "icd10_primary": "R55",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-05-06   TIME: 11:00   PROVIDER: Dr. Rachel Torres, MD (Emergency Medicine)

CC: Loss of consciousness — witnessed episode at work, fully recovered

HPI: 31 yo M presents after witnessed syncopal episode at workplace. Colleague reports patient appeared
pale and sweaty before slumping to ground. LOC for approximately 30 seconds. Rapid return to full
consciousness. Preceding: prolonged standing (3 hours), skipped breakfast, anxious about meeting.
No tonic-clonic activity observed. No tongue bite. No incontinence.

ROS: Positive: LOC, pre-syncopal prodrome (sweating, nausea, dim vision). Negative: no palpitations,
no chest pain, no confusion post-event.

PMH: None | PSH: None | FHx: No family history sudden death or cardiac disease.
SHx: Office manager. Non-smoker. Occasional alcohol. Meds: None. Allergies: NKDA.

VITAL SIGNS: BP 118/74 (no orthostatic drop on lying/standing) | HR 68 | RR 14 | Temp 36.7°C | SpO2 99%

PHYSICAL EXAM: Fully oriented, no residual neurological deficit. Cardiovascular: regular rhythm, no murmurs.
No tongue bite. Pupils equal and reactive. No focal neuro signs.

INVESTIGATIONS:
ECG: Normal sinus rhythm. No long QT, no pre-excitation, no heart block.
Glucose: 4.2 mmol/L (low-normal, skipped breakfast).
FBC, U&E: Normal. Troponin: <3 ng/L.

ASSESSMENT:
1. Vasovagal syncope — clear precipitants, typical prodrome, rapid recovery
2. Fasting hypoglycaemia as contributing factor

PLAN:
1. Reassure — benign prognosis. ROSE/SFSR scores: low risk
2. Driving: advise DVLA guidance (may drive after 4-week symptom-free period)
3. Avoidance strategies: adequate hydration, avoid prolonged standing, eat regular meals
4. Sit/lie down immediately if prodrome recurs
5. No further cardiac workup required (typical presentation, normal ECG, young healthy male)
6. Return if recurrent episodes, chest pain, or palpitations precede syncope
""",
    },
    {
        "id": "transcript-032",
        "encounter_type": "Emergency Department",
        "condition": "Urosepsis — E. coli Bacteraemia",
        "icd10_primary": "A41.51",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-06-01   TIME: 06:30   PROVIDER: Dr. Brendan Murphy, MD (Emergency Medicine)

CC: Confusion, rigors, fever — 12 hours; family unable to rouse overnight

HPI: 74 yo F brought by son. 12h history of rigors, high fever, confusion, and reduced oral intake.
Son noticed increasing confusion overnight — patient normally independent. Resident reports 3-day
history of offensive urine. Background DM2 and recurrent UTIs. Catheterised 2 months ago (removed).

ROS: Positive: fever, rigors, confusion, offensive urine, reduced intake. Negative: no chest pain, no cough.

PMH: DM2 (HbA1c 8.2) | CKD3a | Recurrent UTIs | PSH: Hysterectomy 1992.
FHx: Not relevant. SHx: Lives alone, independent. Meds: Metformin 500mg BD | Amlodipine 5mg.
Allergies: Trimethoprim (rash).

VITAL SIGNS: BP 94/58 | HR 118 | RR 24 | Temp 39.4°C | SpO2 94% | BMI 24.2

PHYSICAL EXAM: Confused (AMTS 4/10). Dry mucous membranes. CVA tenderness bilateral.
Chest: clear. Abdomen: suprapubic tenderness. No peritonism.

INVESTIGATIONS:
WBC 21.4. CRP 312. PCT 18.6. Lactate 3.8 mmol/L. Creatinine 2.6 (baseline 1.3).
Urine dip: leuk +++, nitrites +, blood +. Blood cultures × 2 drawn.
Urinalysis microscopy: WBC >100/hpf, Gram-negative rods.
CT KUB: No obstruction. Bilateral renal parenchymal changes consistent with pyelonephritis.

ASSESSMENT:
1. Sepsis — urosepsis (qSOFA 3, SOFA 5+)
2. Acute kidney injury on CKD3a — septic + hypoperfusion
3. Type 2 DM — glucose 24.2 (hyperosmolar not DKA)

PLAN:
1. Sepsis-3 bundle initiated within 1 hour: IV meropenem 1g TDS (ESBL risk in elderly DM)
2. IV fluid resuscitation: 30mL/kg crystalloid bolus, then reassess MAP
3. Vasopressors: noradrenaline if MAP <65 after 1L fluid
4. Hold metformin (AKI)
5. Urological USS — exclude obstruction
6. Blood cultures × 2 — review sensitivities at 48h
7. ICU/HDU referral — lactate 3.8, haemodynamic compromise
""",
    },
    {
        "id": "transcript-033",
        "encounter_type": "Emergency Department",
        "condition": "Anaphylaxis — Peanut Allergy",
        "icd10_primary": "T78.01XA",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-07-12   TIME: 19:50   PROVIDER: Dr. Yuki Tanaka, MD (Emergency Medicine)

CC: Anaphylaxis — urticaria, throat tightening, hypotension — 20 minutes after eating

HPI: 29 yo M with known peanut allergy brought by ambulance. Ate a salad at restaurant — unaware of
peanut oil in dressing. Developed urticaria within 5 minutes, then throat tightening, stridor, and
dizziness. EpiPen not carried tonight. Ambulance gave IM adrenaline 0.5mg en route.

ROS: Positive: urticaria, throat swelling, stridor, dizziness. Negative: post-adrenaline improving.

PMH: Peanut allergy (anaphylaxis age 8 — hospitalised) | Eczema | PSH: None.
SHx: Graphic designer. Non-smoker. Meds: Cetirizine PRN. Allergies: Peanut (severe anaphylaxis).

VITAL SIGNS: BP 88/54 (improving to 110/72 post-adrenaline) | HR 118→96 | RR 20 | SpO2 96%→99%

PHYSICAL EXAM: Urticaria resolving. Mild residual angioedema lips. Stridor resolved post-adrenaline.
Chest: mild wheeze. Abdomen: soft.

INVESTIGATIONS:
Serum tryptase (at 1h): 48 μg/L (markedly elevated — confirms anaphylaxis).
ECG: sinus tachycardia. FBC, U&E: unremarkable.

ASSESSMENT:
1. Anaphylaxis — peanut allergy (Resuscitation Council Grade 3)
2. Initial cardiovascular compromise — responded to IM adrenaline

PLAN:
1. IV chlorphenamine 10mg and IV hydrocortisone 200mg (ongoing mediator suppression)
2. Observe minimum 6 hours post-adrenaline (biphasic reaction risk — occurs up to 12h)
3. Repeat tryptase at 2h and 24h for baseline comparison
4. Prescribe EpiPen × 2 — patient counselled on self-administration technique
5. Allergy/immunology outpatient referral — oral immunotherapy consideration
6. MedicAlert bracelet strongly recommended
7. Dietary advice: restaurant labelling, peanut avoidance strategy reinforced
""",
    },
    {
        "id": "transcript-034",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Type 2 Diabetes — Routine 6-Month Review",
        "icd10_primary": "E11.65",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-02-18   TIME: 10:00   PROVIDER: Dr. Nina Osei, MD (Family Medicine)

CC: Routine 6-month diabetes review

HPI: 58 yo M with T2DM for 12 years presents for scheduled review. HbA1c was 8.4% at last visit.
Reports improved dietary adherence over past 3 months — reduced refined carbohydrates. Home glucose
monitoring average 9.2 mmol/L fasting. No hypoglycaemic episodes. Mild fatigue.

ROS: Positive: mild fatigue. Negative: no polyuria, no foot pain, no visual changes, no chest pain.

PMH: T2DM | HTN | Dyslipidaemia | PSH: None | FHx: Father: T2DM (died MI age 62).
SHx: Bus driver. Married. Ex-smoker (5 years). Meds: Metformin 1g BD | Gliclazide 80mg BD |
Lisinopril 10mg | Atorvastatin 40mg. Allergies: NKDA.

VITAL SIGNS: BP 136/82 | HR 74 | Wt 89kg | BMI 30.2

PHYSICAL EXAM: Foot exam: intact sensation (10g monofilament), normal pulses bilaterally.
Peripheral neuropathy screening: absent ankle jerks — mild peripheral neuropathy.
Eyes: awaiting retinal screening (overdue — scheduled).

INVESTIGATIONS:
HbA1c: 7.8% (improved from 8.4%). eGFR: 64 (stable CKD2). ACR: 38 mg/mmol (microalbuminuria).
LDL: 2.4 mmol/L (above target <1.8). Foot vascular Doppler: normal ABI bilaterally.

ASSESSMENT:
1. T2DM — improving control (HbA1c 7.8%), microalbuminuria
2. Mild diabetic peripheral neuropathy — ankle reflexes absent
3. Dyslipidaemia — LDL above target

PLAN:
1. Increase atorvastatin to 80mg QHS (LDL above target — CVD primary prevention)
2. Add empagliflozin 10mg QD (SGLT2i — renal protective, ACR 38, CKD2)
3. Retinal screening: expedite booking
4. Neuropathy: gabapentin available PRN if symptoms develop; avoid foot trauma
5. ACE inhibitor: continue lisinopril (renoprotective — increase to 20mg if BP allows)
6. DVLA notification: diabetes treated with insulin-secretagogue — check driving regulations
7. Review 3 months with repeat HbA1c and ACR
""",
    },
    {
        "id": "transcript-035",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Hypothyroidism — Newly Diagnosed",
        "icd10_primary": "E03.9",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-03-10   TIME: 14:30   PROVIDER: Dr. Samuel Adeyemi, MD (Family Medicine)

CC: Fatigue, weight gain, hair loss, feeling cold — 5 months

HPI: 44 yo F with 5-month history of progressive fatigue, 6kg weight gain without dietary change,
hair thinning, cold intolerance, and constipation. Also notes slowing of speech noticed by husband.
No known thyroid disease. No neck swelling or pain.

ROS: Positive: fatigue, weight gain, hair loss, cold intolerance, constipation, bradylalia.
Negative: no dysphagia, no palpitations, no neck pain.

PMH: None | PSH: None | FHx: Mother: hypothyroidism. SHx: Nurse. Married. Non-smoker.
Meds: None. Allergies: NKDA.

VITAL SIGNS: BP 126/80 | HR 54 | Temp 36.2°C | SpO2 99% | Wt 74kg | BMI 27.4

PHYSICAL EXAM: Coarse, dry skin. Periorbital puffiness. Bradycardia HR 54.
Thyroid: smooth, non-tender, slightly enlarged — no nodules. Ankle reflexes: slow relaxation phase.
No lid lag or exophthalmos.

INVESTIGATIONS:
TSH: 42 mIU/L (markedly elevated). Free T4: 5.8 pmol/L (low).
Anti-TPO: 1,240 IU/mL (strongly positive — Hashimoto's thyroiditis).
FBC: mild normocytic anaemia Hb 10.8. Cholesterol: 6.8 mmol/L (hypothyroidism-associated).

ASSESSMENT:
1. Primary hypothyroidism — Hashimoto's thyroiditis
2. Bradycardia secondary to hypothyroidism
3. Secondary dyslipidaemia — hypothyroidism-related

PLAN:
1. Levothyroxine 50mcg QD (fasting, 30min before food). Start low — elderly/cardiac risk not present.
2. Recheck TFTs at 6-8 weeks; target TSH 0.5-2.5 mIU/L
3. Anaemia: repeat after thyroid replacement (often resolves)
4. Cholesterol: review at 3 months — often resolves with euthyroid state, avoid premature statin
5. Patient education: lifelong treatment, importance of adherence, symptoms of over-treatment
6. Thyroid ultrasound: not routinely needed for Hashimoto's without nodule
""",
    },
    {
        "id": "transcript-036",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Hypertension — Annual Review, BP Suboptimal",
        "icd10_primary": "I10",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-04-22   TIME: 09:30   PROVIDER: Dr. Mark Chen, MD (Internal Medicine / Primary Care)

CC: Annual hypertension review

HPI: 67 yo M with 15-year history of hypertension presents for annual review. Home BP readings over
past 2 weeks average 158/94 (morning). Admits poor medication adherence ("forgets evening dose").
No chest pain, no shortness of breath, no visual disturbance. Mild headaches 2-3x/week.

ROS: Positive: mild headaches, suboptimal BP at home. Negative: no chest pain, no dyspnoea, no focal neuro.

PMH: HTN | AF (on warfarin, paroxysmal) | PSH: TURP 2018. FHx: Brother: stroke age 60.
SHx: Retired teacher. Lives with wife. Ex-smoker (stopped age 55, 40pk history).
Meds: Amlodipine 10mg QD | Losartan 100mg BD (poor adherence — takes once) | Warfarin (INR 2.4 today).
Allergies: ACE inhibitors (dry cough — switched to ARB).

VITAL SIGNS: BP 162/96 (average 3 readings) | HR 72 | BMI 27.8 | Wt 82kg

PHYSICAL EXAM: No bruits. JVP normal. No oedema. Fundoscopy: AV nipping (grade 1 hypertensive retinopathy). No papilloedema.

INVESTIGATIONS:
U&E: Na 140, K 4.2, Creatinine 1.1 (eGFR 68 — CKD2). HbA1c: 5.8% (no DM).
Echocardiogram (last year): mild LVH, EF 58%.

ASSESSMENT:
1. Hypertension — suboptimal control due to non-adherence
2. Paroxysmal AF — adequately anticoagulated (INR 2.4)
3. Grade 1 hypertensive retinopathy — no action change

PLAN:
1. Simplify regimen: change losartan to once-daily formulation (losartan 100mg QD)
2. Consider adding indapamide 2.5mg QD (third agent, well-tolerated with AF)
3. Home BP diary: 2 readings each morning × 7 days before next review
4. Adherence: pill box, phone alarm system
5. ABPM 24-hour recording if home readings remain elevated at 1-month review
6. Continue warfarin; INR 2.4 is therapeutic
7. Ophthalmology: refer for formal retinal assessment (hypertensive retinopathy grade 1)
""",
    },
    {
        "id": "transcript-037",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Major Depression — Annual Review, Stable Remission",
        "icd10_primary": "F33.0",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-05-14   TIME: 15:00   PROVIDER: Dr. Angela Foster, MD (Family Medicine / Mental Health)

CC: Annual mental health review — depression in remission

HPI: 36 yo F with recurrent depressive disorder, currently in remission for 14 months on sertraline.
Reports stable mood, good sleep, no anhedonia. Returned to full-time work 10 months ago. No current
suicidal ideation. Marriage stable. One stressor: caring for elderly parent (acknowledges this with equanimity).

ROS: Positive: mild fatigue (sleep quality 6/10). Negative: no depressed mood, no anhedonia, no SI.

PMH: Recurrent MDD (3 episodes since age 28) | PSH: None | FHx: Mother: bipolar disorder.
SHx: Solicitor. Married. Non-smoker. Meds: Sertraline 100mg QD (3 years). Allergies: NKDA.

VITAL SIGNS: BP 112/70 | HR 72 | Wt 63kg | BMI 23.4

PHYSICAL EXAM: Euthymic, well-presented. Normal psychomotor. No agitation or retardation.

INVESTIGATIONS:
TSH: 1.8 (normal — checked annually). PHQ-9: 3 (minimal). GAD-7: 2 (minimal).
Bloods: FBC, U&E, LFTs normal.

ASSESSMENT:
1. Recurrent MDD — currently in sustained remission (>12 months)
2. Maternal history bipolar — no hypomanic features to date

PLAN:
1. Continue sertraline 100mg QD — minimum 2 years from last episode (risk of relapse if stopped early)
2. Discuss future tapering plan: not before 2 years remission; slow taper if elected
3. PHQ-9 monitoring every 6 months or with any mood change
4. Discuss carer stress — offer carers' support resources and local authority carer assessment
5. Return precautionary signs: poor sleep >1 week, withdrawal, anhedonia, missed work
6. Next review: 12 months unless concerns arise sooner
""",
    },
    {
        "id": "transcript-038",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Chronic Low Back Pain — Non-Specific",
        "icd10_primary": "M54.5",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-06-09   TIME: 11:30   PROVIDER: Dr. Keisha Thompson, MD (Family Medicine)

CC: Chronic low back pain — review and management update

HPI: 52 yo M with 3-year history of non-specific low back pain. Pain 4-6/10, worsens with prolonged
sitting (office work), improves with movement. No radiation below knee. No red flags. Previous
physiotherapy helped briefly. Currently using naproxen 500mg PRN (3-4x/week).

ROS: Positive: chronic LBP. Negative: no radiculopathy, no bladder/bowel change, no saddle anaesthesia,
no night sweats, no unexplained weight loss.

PMH: Hypertension | PSH: Appendicectomy 2004. FHx: No malignancy. SHx: IT manager. Sedentary job.
BMI 29. Meds: Amlodipine 5mg | Naproxen 500mg PRN. Allergies: NKDA.

VITAL SIGNS: BP 132/82 | HR 70 | BMI 29.2 | Wt 88kg

PHYSICAL EXAM: Lumbar: restricted flexion, full extension. Paravertebral tenderness L3-L5. No scoliosis.
SLR: negative bilateral. Reflexes: intact. No focal weakness.

INVESTIGATIONS:
MRI lumbar spine: mild L4-L5 disc degeneration with posterior disc bulge — not impinging nerve root.
PSA, ESR, CRP: normal (red flag exclusion done 18 months ago).

ASSESSMENT:
1. Chronic non-specific low back pain — mechanical, degenerative L4-L5
2. NSAIDs overuse (3-4x/week) — GI risk counselling needed

PLAN:
1. Active exercise programme referral — supervised physiotherapy / back pain group class
2. Cognitive-behavioural approach: address catastrophising (STarT Back score: medium risk)
3. Reduce naproxen reliance: add omeprazole for GI protection; prescribe scheduled paracetamol 1g QDS
4. Ergonomic assessment: standing desk, hourly movement breaks
5. Weight management: 5% weight loss target (improves lumbar load)
6. Acupuncture: offer via self-referral — modest evidence in chronic non-specific LBP
7. Review 3 months. MRI not to be repeated without new symptoms.
""",
    },
    {
        "id": "transcript-039",
        "encounter_type": "Inpatient — General Medicine",
        "condition": "Community-Acquired Pneumonia — Moderate (CURB-65: 3)",
        "icd10_primary": "J15.9",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-01-30   TIME: 16:00   PROVIDER: Dr. Jordan Lee, MD (General Medicine)

CC: Cough, fever, confusion — family brought in after found unwell at home

HPI: 71 yo F admitted with 4-day history of productive cough (rust-coloured sputum), fever, and
confusion today. Lives alone — found by daughter slumped in chair. Declined GP appointment 3 days ago.
Background: COPD, Parkinson's disease (stable).

ROS: Positive: fever, productive cough, confusion. Negative: no chest pain, no haemoptysis.

PMH: COPD (GOLD II) | Parkinson's disease (stable, on levodopa) | PSH: Hip replacement 2019.
FHx: Not relevant. SHx: Retired. Lives alone. Meds: Salbutamol MDI | Tiotropium | Levodopa 100mg TDS.
Allergies: NKDA.

VITAL SIGNS: BP 102/64 | HR 110 | RR 24 | Temp 38.9°C | SpO2 89% on air | BMI 22.6

PHYSICAL EXAM: Confused (AMTS 5/10). Reduced air entry left base with coarse crackles.
No bronchial breathing. No pleuritic rub. Mild peripheral oedema.

INVESTIGATIONS:
WBC 22.4, CRP 388. PCT 8.4. Creatinine 1.6 (baseline 1.0).
CXR: left lower lobe consolidation. CURB-65: 3 (confusion, urea 12, RR 24) → inpatient admission.
Blood cultures × 2: drawn. Urine pneumococcal antigen: positive.
Sputum: sent for C&S.

ASSESSMENT:
1. CAP — left lower lobe, moderate-severe (CURB-65 3)
2. Streptococcus pneumoniae — pneumococcal antigen positive
3. Confusion — likely sepsis-related, not Parkinson's decompensation
4. Acute kidney injury — prerenal (sepsis + reduced intake)

PLAN:
1. IV co-amoxiclav 1.2g TDS + clarithromycin 500mg BD (dual therapy, CURB-65 ≥3)
2. Controlled O2: 28% Venturi, target SpO2 88-92% (COPD risk — hypercapnia)
3. IV fluids: 500mL 0.9% NaCl cautiously (peripheral oedema — likely cor pulmonale)
4. Continue levodopa (do NOT stop in Parkinson's — rigidity/NMS risk)
5. Thromboprophylaxis: LMWH (confusion + reduced mobility)
6. Confusion: 1:1 nursing, non-pharmacological delirium prevention
7. Review 48h — de-escalate to oral amoxicillin if improving
""",
    },
    {
        "id": "transcript-040",
        "encounter_type": "Inpatient — General Medicine",
        "condition": "Acute Kidney Injury — Obstructive (Benign Prostatic Hyperplasia)",
        "icd10_primary": "N17.0",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-02-25   TIME: 20:15   PROVIDER: Dr. Priya Anand, MD (General Internal Medicine)

CC: Reduced urine output, lower abdominal discomfort, confusion — 2 days

HPI: 77 yo M admitted with 2-day history of reduced urine output, suprapubic discomfort, and mild
confusion. Wife noted patient was going to bathroom frequently but passing very little. History of
BPH — declined TURP. No catheter in situ. Creatinine on admission 3.8 mg/dL (baseline 1.2 from 3 months ago).

ROS: Positive: oliguria, suprapubic pain, confusion, nocturia. Negative: no haematuria, no fever.

PMH: BPH (declined surgery) | HTN | CKD2 (baseline) | PSH: Appendicectomy.
SHx: Retired farmer. Meds: Tamsulosin 0.4mg | Amlodipine 10mg. Allergies: Penicillin (rash).

VITAL SIGNS: BP 162/94 | HR 82 | RR 16 | Temp 36.8°C | SpO2 97% | BMI 27.2

PHYSICAL EXAM: Confused (AMTS 6/10). Distended bladder palpable 4cm above pubis.
Abdomen: suprapubic dullness on percussion. DRE: markedly enlarged smooth prostate.

INVESTIGATIONS:
Creatinine 3.8 (AKI stage 3 on baseline 1.2). K+ 5.6. USS bladder: 680mL residual (acute retention).
USS kidneys: bilateral mild hydronephrosis — obstructive uropathy.
CXR: mild pulmonary venous congestion — fluid overload.

ASSESSMENT:
1. Acute kidney injury stage 3 — obstructive (BPH with acute urinary retention)
2. Bilateral hydronephrosis — reversible
3. Hyperkalaemia K+ 5.6 — AKI-related
4. Mild pulmonary congestion — avoid aggressive IV fluids

PLAN:
1. Urethral catheterisation STAT — drain retention slowly (max 500mL/h to prevent haematuria)
2. Post-obstructive diuresis expected — hourly fluid balance, replace output 1:1 until stable
3. IV dextrose + insulin 10 units (K+ 5.6, ECG: peaked T waves)
4. Calcium gluconate 10mL 10% IV — cardiac membrane stabilisation
5. Hold: tamsulosin (alpha-blocker may worsen hypotension), ACEI if on
6. Nephrology consult: AKI stage 3, creatinine 3.8
7. Urology urgent referral: TURP or long-term catheter plan after recovery
""",
    },
    {
        "id": "transcript-041",
        "encounter_type": "Inpatient — Cardiology",
        "condition": "Acute Decompensated Heart Failure — HFrEF",
        "icd10_primary": "I50.21",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-03-18   TIME: 08:30   PROVIDER: Dr. Amanda Walsh, MD (Cardiology)

CC: Worsening dyspnoea at rest, orthopnoea, ankle swelling — 5 days

HPI: 69 yo F with known ischaemic cardiomyopathy (LVEF 30%) presents with 5-day worsening dyspnoea.
Now breathless at rest and unable to lie flat (3-pillow orthopnoea). Bilateral ankle oedema worsening.
Weight gain 5kg in past week. Non-adherent to fluid restriction over Christmas holiday.

ROS: Positive: dyspnoea at rest, orthopnoea, ankle oedema, weight gain, fatigue.
Negative: no chest pain, no fever, no palpitations.

PMH: Ischaemic cardiomyopathy (LVEF 30%) | AF (on anticoagulation) | CKD3 | PSH: CABG 2014.
SHx: Retired. Lives with husband. Meds: Furosemide 80mg BD | Carvedilol 25mg BD |
Sacubitril-valsartan 97/103mg BD | Eplerenone 25mg | Apixaban 5mg BD. Allergies: NKDA.

VITAL SIGNS: BP 108/68 | HR 82 (AF) | RR 22 | SpO2 91% on air | Wt 72kg (dry wt 67kg)

PHYSICAL EXAM: JVP elevated to angle of jaw. Bilateral coarse basal crackles.
Bilateral pitting oedema to knees. No murmurs beyond established findings.

INVESTIGATIONS:
BNP: 2,840 pg/mL (prev 480). Troponin: 28 ng/L (mildly raised, chronic). Creatinine 1.8 (prev 1.4).
CXR: cardiomegaly, bilateral alveolar infiltrates, pleural effusions.
Echo (today): LVEF 28%, dilated LV, no new wall motion abnormality.

ASSESSMENT:
1. Acute decompensated HFrEF — fluid overload (5kg above dry weight)
2. Worsening renal function — cardiorenal syndrome type 1
3. Non-adherence to fluid restriction — precipitating cause

PLAN:
1. IV furosemide 80mg BD (double oral dose) — target urine output >200mL/h for 2-3h
2. Strict fluid restriction 1.5L/24h. Daily weights.
3. Electrolytes monitoring BD (diuresis-related hypokalaemia risk)
4. Continue sacubitril-valsartan and carvedilol (do not stop — beneficial even in decompensation)
5. Cardiology MDT: consider SGLT2i initiation once stable
6. Heart failure nurse specialist referral — fluid management education
7. Discharge planning: home telemonitoring and daily weight diary
""",
    },
    {
        "id": "transcript-042",
        "encounter_type": "Inpatient — Cardiology",
        "condition": "New-Onset Atrial Fibrillation — Rapid Ventricular Rate",
        "icd10_primary": "I48.0",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-04-10   TIME: 23:00   PROVIDER: Dr. Nguyen Van Minh, MD (Cardiology)

CC: Palpitations and dyspnoea — 6 hours. ECG: AF with rapid ventricular response.

HPI: 58 yo M referred from ED with 6h palpitations and exertional dyspnoea. No prior AF documented.
No chest pain, no syncope. Thyroid disease excluded recently. Mild alcohol use (20 units/week).
Haemodynamically stable on presentation.

ROS: Positive: palpitations, mild dyspnoea, fatigue. Negative: no chest pain, no presyncope, no fever.

PMH: Hypertension | Obstructive sleep apnoea (non-adherent CPAP) | PSH: None.
FHx: Father: AF. SHx: Solicitor. Married. Alcohol 20 units/week.
Meds: Amlodipine 10mg. Allergies: NKDA.

VITAL SIGNS: BP 146/88 | HR 142 (irregular) | RR 18 | SpO2 97% | BMI 31.4

PHYSICAL EXAM: Irregular pulse 142bpm. No JVP elevation. Chest: clear.
No peripheral oedema. No thyromegaly.

INVESTIGATIONS:
ECG: AF — no delta waves, no aberrant conduction, no ST changes.
Echo: mildly dilated LA (42mm). EF 55% — normal systolic function. No LVH.
TFTs: TSH 1.8 (normal). HbA1c: 5.6%. U&E: normal. TTE: no pericardial effusion.
CXR: mild cardiomegaly — consistent with LA dilation only.

ASSESSMENT:
1. New-onset AF — rapid ventricular rate (HR 142)
2. Haemodynamically stable — rate control strategy first
3. Onset unclear: not certain <48h → cardioversion not safe without TOE

PLAN:
1. Rate control: bisoprolol 2.5mg PO (titrate to HR <100), check BP response
2. Anticoagulation: initiate apixaban 5mg BD immediately (CHA2DS2-VASc 2: HTN + male sex)
3. TOE-guided cardioversion: if patient opts for rhythm control after anticoagulation established
4. Sleep apnoea: CPAP adherence essential — OSA is independent AF trigger
5. Alcohol counselling: 20 units/week — AF risk factor; refer to alcohol service
6. Cardiology outpatient at 4-6 weeks — AF review and rhythm control decision
""",
    },
    {
        "id": "transcript-043",
        "encounter_type": "Inpatient — ICU",
        "condition": "Moderate-Severe ARDS — Post-Viral Pneumonia",
        "icd10_primary": "J80",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-05-21   TIME: 07:00   PROVIDER: Dr. Elena Rossi, MD (Intensive Care Medicine)

CC: ICU admission — intubated for respiratory failure, ARDS criteria met

HPI: 54 yo M transferred from respiratory ward day 3 of viral pneumonia (influenza A confirmed).
Progressive hypoxia despite high-flow nasal oxygen (FiO2 0.8 — SpO2 84%). CPAP trial failed.
Intubated and ventilated for refractory hypoxia. No significant prior lung disease.

ROS: Assessed via family — no known comorbidities prior to acute illness.

PMH: Hypertension | Obese (BMI 36) | PSH: None. FHx: Not relevant.
SHx: Construction supervisor. Non-smoker. Alcohol 8 units/week.
Meds: Amlodipine 5mg. Allergies: NKDA.

VITAL SIGNS (intubated): HR 106 | BP 112/68 (noradrenaline 0.1mcg/kg/min) | Temp 38.6°C | SpO2 91%

VENTILATOR: Mode: VCV | Vt 420mL (6mL/kg IBW) | PEEP 12cmH2O | FiO2 0.65 | P-plat 28cmH2O

INVESTIGATIONS:
ABG (on FiO2 0.65): pH 7.36, pO2 62, pCO2 44, HCO3 24. PaO2/FiO2: 95 → severe ARDS.
CXR: bilateral diffuse alveolar opacification. No cardiomegaly.
Echo: EF 55%, no LV dysfunction (excludes cardiogenic). PCWP not elevated.
Bronchoalveolar lavage: inflammatory cells ++, influenza PCR positive.

ASSESSMENT:
1. Moderate-severe ARDS — influenza A pneumonia (PaO2/FiO2 95, Berlin criteria)
2. Vasoplegic shock — vasopressors required
3. Obesity — reduced chest wall compliance, challenging ventilation

PLAN:
1. Lung-protective ventilation: Vt 6mL/kg IBW, Pplat <30, PEEP titrated (12cmH2O currently)
2. Prone positioning: 16h/day cycles — improves oxygenation in moderate-severe ARDS
3. Neuromuscular blockade: cisatracurium 48h (improves synchrony, reduces barotrauma risk)
4. Corticosteroids: methylprednisolone 1mg/kg/day (viral-ARDS, >14-day course)
5. Antiviral: oseltamivir 150mg BD (influenza A, severe disease, immunocompromised obese patient)
6. Vasopressors: target MAP >65; noradrenaline first-line
7. Daily spontaneous awakening and breathing trials once FiO2 ≤0.4
""",
    },
    {
        "id": "transcript-044",
        "encounter_type": "Outpatient — Surgical",
        "condition": "Pre-Operative Assessment — Elective Right Hemicolectomy",
        "icd10_primary": "Z01.818",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-06-23   TIME: 10:00   PROVIDER: Dr. Patrick Brennan, MD (Pre-Operative Assessment)

CC: Pre-operative assessment before elective right hemicolectomy (colorectal cancer T2N0)

HPI: 62 yo F scheduled for elective right hemicolectomy for T2N0M0 right-sided colon cancer
(diagnosed on colonoscopy, confirmed histology). MDT: curative resection planned.
Current functional status: NYHA I, no exercise limitation.

ROS: Positive: mild fatigue (anaemia). Negative: no dyspnoea, no angina, no palpitations.

PMH: Hypertension | T2DM (diet-controlled, HbA1c 6.2%) | Anaemia (pre-op Hb 10.4) | PSH: Appendicectomy, Caesarean x2.
SHx: Retired teacher. Lives with husband. Non-smoker. Meds: Amlodipine 5mg | Aspirin 75mg.
Allergies: Sulfa drugs (rash).

VITAL SIGNS: BP 132/80 | HR 72 | SpO2 98% | BMI 26.4 | Hb 10.4

PHYSICAL EXAM: Well-appearing. No cardiorespiratory findings. Surgical scar: right iliac fossa + lower midline.
Abdomen: soft, no palpable mass.

INVESTIGATIONS:
Hb 10.4, MCV 72 (iron deficiency). Ferritin 8. Pre-op bloods: normal coagulation.
ECG: normal sinus rhythm. Echo not required (NYHA I, no cardiac history).
Creatinine 0.9 (eGFR 74). HbA1c 6.2%.
Lung function: FVC 94%, FEV1 88% — no respiratory risk.

ASSESSMENT:
1. Pre-operative evaluation — low cardiac risk (Lee RCRI score 1)
2. Iron deficiency anaemia — needs correction pre-operatively
3. Aspirin: peri-operative management required

PLAN:
1. IV iron infusion: Ferinject 1000mg — target Hb >12 before surgery (book 3 weeks pre-op)
2. Aspirin: continue until surgery (colorectal cancer — thrombotic risk > bleeding)
3. Amlodipine: continue morning of surgery
4. Anaesthetic pre-assessment: spinal vs GA discussion with anaesthetist
5. Enhanced recovery after surgery (ERAS) protocol: carbohydrate drinks pre-op, early mobilisation
6. VTE prophylaxis: LMWH for 28 days post-op (colorectal cancer — high VTE risk)
7. Consent discussion: surgical risks documented, patient questions answered
""",
    },
    {
        "id": "transcript-045",
        "encounter_type": "Emergency Department / Neurology",
        "condition": "Transient Ischaemic Attack — High-Risk (ABCD2 Score 5)",
        "icd10_primary": "G45.9",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-07-08   TIME: 15:20   PROVIDER: Dr. Elena Rossi, MD (Emergency Medicine / Neurology Liaison)

CC: Transient left arm weakness and speech difficulty — 20 minutes, fully resolved

HPI: 66 yo M presents with 20-minute episode of left arm weakness and dysarthria, fully resolved.
Onset while watching television. No LOC. No headache. Symptoms resolved completely within 20min.
Previous TIA 2 years ago — discharged on aspirin and statin. Non-adherent to statin.

ROS: Positive: transient left arm weakness, dysarthria (resolved). Negative: no vision change, no LOC.

PMH: HTN | AF (paroxysmal, NOT anticoagulated — patient declined) | Hypercholesterolaemia | Prior TIA.
PSH: None. FHx: Father: stroke age 68. SHx: Retired plumber. Smoker 30 pack years. Current smoker.
Meds: Aspirin 75mg | Amlodipine 10mg | Atorvastatin (not taking). Allergies: NKDA.

VITAL SIGNS: BP 168/98 | HR 76 (regular) | RR 14 | Temp 36.7°C | SpO2 98%

PHYSICAL EXAM: Fully resolved — no neurological deficit now. NIHSS 0.
Carotid auscultation: right carotid bruit.

INVESTIGATIONS:
CT brain: no acute infarct. MRI DWI: small right hemisphere lacune on DWI (new — microinfarct).
CT angiography: right ICA 68% stenosis. ECG: sinus rhythm today (not AF).
Echocardiogram: mild LA dilation (40mm). LDL 3.4 mmol/L.

ASSESSMENT:
1. TIA — high risk (ABCD2 score 5: age 66 + BP 168 + unilateral weakness + duration 20min)
2. Right ICA stenosis 68% — symptomatic — carotid endarterectomy indicated
3. AF (paroxysmal) — not anticoagulated — major risk factor inadequately managed

PLAN:
1. Dual antiplatelet: add clopidogrel 75mg QD to aspirin for 21 days (POINT trial)
2. Restart atorvastatin 80mg QHS — LDL 3.4 (must be on statin after TIA)
3. Urgent neurology and vascular surgery referral — CEA within 14 days of TIA (symptomatic 68% stenosis)
4. Anticoagulation counselling: paroxysmal AF — apixaban strongly recommended (patient education)
5. Blood pressure: increase amlodipine + add losartan (target BP <130/80 post-TIA)
6. Smoking cessation: NRT prescribed, QUIT referral placed
""",
    },
    {
        "id": "transcript-046",
        "encounter_type": "Inpatient — Gastroenterology",
        "condition": "Crohn's Disease — Moderate Flare, Ileocolonic",
        "icd10_primary": "K50.10",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-08-05   TIME: 14:30   PROVIDER: Dr. Samuel Adeyemi, MD (Gastroenterology)

CC: Abdominal cramping, bloody diarrhoea 8x/day, weight loss — 3 weeks

HPI: 33 yo F with known ileocolonic Crohn's disease (diagnosed age 24, on azathioprine) presents with
3-week history of increased diarrhoea (8 loose stools/day, blood-streaked), abdominal cramping,
and 4kg weight loss. Recent URTI 4 weeks ago — possible trigger. Fevers at home (max 38.2°C).

ROS: Positive: bloody diarrhoea, abdominal cramps, fever, weight loss.
Negative: no oral ulcers this episode, no joint pains.

PMH: Crohn's disease (ileocolonic, B1 Montreal classification) | PSH: None.
FHx: Brother: ulcerative colitis. SHx: Graphic designer. Non-smoker.
Meds: Azathioprine 150mg QD | Ferrous sulfate | Folic acid. Allergies: NKDA.

VITAL SIGNS: BP 108/68 | HR 108 | RR 16 | Temp 38.2°C | SpO2 99% | Wt 54kg (was 58kg)

PHYSICAL EXAM: Thin-appearing. RIF tenderness. No peritonism. No masses.
Perianal: no fistula or abscess. Mouth: no aphthous ulcers.

INVESTIGATIONS:
CRP 128, WBC 14.2, ESR 64, Albumin 28 (low — malnutrition).
Faecal calprotectin: 2,400 μg/g (markedly elevated — active mucosal inflammation).
Stool: C. difficile negative, CMV negative (excluded immunosuppression-related).
Harvey-Bradshaw Index: 11 (moderate-severe). MRI small bowel: ileocolonic inflammation, skip lesions.

ASSESSMENT:
1. Crohn's disease — moderate-severe flare (Harvey-Bradshaw 11)
2. Hypoalbuminaemia — nutritional compromise
3. Azathioprine failure — escalation required

PLAN:
1. IV methylprednisolone 40mg QD (induction)
2. Nutritional support: dietitian review; consider enteral nutrition (NG feed)
3. Thiopurine failure — initiate biologic therapy: infliximab 5mg/kg IV induction
4. TB screening + IGRA, hepatitis B serology (before infliximab)
5. VTE prophylaxis: LMWH (IBD flare + bedbound — high risk)
6. Gastroenterology IBD nurse specialist involvement
7. Switch to vedolizumab if infliximab antibodies develop or primary non-response
""",
    },
    {
        "id": "transcript-047",
        "encounter_type": "Inpatient — Hepatology",
        "condition": "Alcoholic Hepatitis — Severe (Maddrey's DF > 32)",
        "icd10_primary": "K70.10",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-09-03   TIME: 10:00   PROVIDER: Dr. Marcus Williams, MD (Hepatology)

CC: Jaundice, abdominal distension, confusion — 10 days

HPI: 47 yo M with known alcohol use disorder presents with 10-day worsening jaundice, abdominal
distension, and mild confusion over past 2 days. Drinking 20–30 units/day for 15 years.
Last drink: this morning. No prior liver decompensation documented.

ROS: Positive: jaundice, ascites, confusion, anorexia. Negative: no haematemesis, no melaena.

PMH: Alcohol use disorder | PSH: None. FHx: Father: cirrhosis.
SHx: Unemployed. Lives alone. Meds: Thiamine 100mg QD (inconsistent). Allergies: NKDA.

VITAL SIGNS: BP 108/68 | HR 110 | RR 18 | Temp 38.1°C | SpO2 97% | BMI 23.8

PHYSICAL EXAM: Icteric. Spider naevi × 5. Palmar erythema. Gynaecomastia.
Abdomen: tense ascites, shifting dullness positive. Splenomegaly 16cm. Tender hepatomegaly 4cm.
Confusion: AMTS 6/10.

INVESTIGATIONS:
Bilirubin: 18.4 mg/dL. PT 22s, INR 2.1. ALT 112, AST 228 (AST:ALT 2:1 — alcoholic pattern).
Albumin 22. Creatinine 1.4 (MELD-Na score 28 — severe). WBC 18.4.
Maddrey's Discriminant Function: 54 (>32 — severe, steroids indicated).
USS abdomen: cirrhotic liver, large ascites, portal hypertension. No focal lesion.
Diagnostic paracentesis: 0.4g/L protein, SAAG 1.2. WBC <250 — no SBP.

ASSESSMENT:
1. Severe alcoholic hepatitis (Maddrey DF 54, MELD-Na 28)
2. Compensated cirrhosis decompensating (ascites, jaundice, encephalopathy grade I)
3. No spontaneous bacterial peritonitis

PLAN:
1. Prednisolone 40mg QD × 28 days (Lille score at day 7 — stop if non-responder)
2. Pentoxifylline: NOT first-line (STOPAH trial) — prednisolone monotherapy
3. IV thiamine 200mg TDS × 3 days → oral (Wernicke prevention)
4. Rifaximin 550mg BD + lactulose (hepatic encephalopathy prophylaxis)
5. Diuretics for ascites: spironolactone 100mg → furosemide 40mg (stepwise)
6. Alcohol liaison team referral: CAGE assessment, detox planning
7. Liver transplant MDT: abstinence-based assessment at 6 months if MELD improves
""",
    },
    {
        "id": "transcript-048",
        "encounter_type": "Inpatient — Nephrology",
        "condition": "ESRD on Haemodialysis — AV Fistula Thrombosis",
        "icd10_primary": "T82.49XA",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-06-17   TIME: 09:30   PROVIDER: Dr. Elena Rossi, MD (Nephrology)

CC: Unable to dialyse — fistula not functioning since yesterday

HPI: 65 yo F with ESRD on haemodialysis (3x/week via AVF left forearm, created 4 years ago) presents
unable to attend dialysis session yesterday as fistula non-functioning. Missed last 2 sessions.
Complaints of left forearm pain, swelling, and no thrill on palpation. Increasing dyspnoea and ankle oedema.

ROS: Positive: fistula non-functioning, dyspnoea, ankle oedema, left forearm swelling.
Negative: no chest pain, no fever.

PMH: ESRD (IgA nephropathy) | DM2 | HTN | PSH: AVF creation left forearm 2019.
SHx: Retired. Married. Meds: Darbepoetin 40mcg SC (HD days) | Calcium carbonate | Alfacalcidol |
Amlodipine 10mg | Bisoprolol 5mg. Allergies: NKDA.

VITAL SIGNS: BP 176/104 | HR 92 | RR 20 | SpO2 94% | Wt 68kg (dry wt 63kg) | BMI 26.8

PHYSICAL EXAM: Left forearm AVF: no thrill, no bruit (on auscultation). Erythematous firm cord palpable.
Chest: bilateral crackles. Bilateral pitting oedema to mid-thigh.

INVESTIGATIONS:
K+ 6.4 (dangerous — dialysis-dependent), BUN 148, Creatinine 14.8 (no residual renal function).
ABG: pH 7.28, HCO3 14 — metabolic acidosis (uraemic + missed dialysis).
CXR: bilateral pulmonary oedema. ECG: peaked T waves (hyperkalaemia).
Doppler USS fistula: thrombosis left cephalic-radial junction — no flow.

ASSESSMENT:
1. AV fistula thrombosis — left forearm
2. Fluid overload (5kg above dry weight) — 2 missed dialysis sessions
3. Hyperkalaemia K+ 6.4 with ECG changes — medical emergency
4. Metabolic acidosis — uraemic

PLAN:
1. Calcium gluconate 10mL IV STAT (ECG changes — membrane stabilisation)
2. Salbutamol nebuliser 10mg + insulin-dextrose (K+ temporising)
3. Emergency dialysis via temporary CVC (right jugular — inserted by nephrology fellow)
4. Vascular surgery urgent referral: fistula thrombectomy or angioplasty within 24-48h
5. Anticoagulation: IV heparin post-thrombectomy per vascular surgery plan
6. Long-term: consider fistuloplasty surveillance programme
""",
    },
    {
        "id": "transcript-049",
        "encounter_type": "Outpatient — Paediatrics",
        "condition": "Simple Febrile Convulsion — 2-Year-Old",
        "icd10_primary": "R56.00",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-07-29   TIME: 10:15   PROVIDER: Dr. Alicia Nwosu, MD (Paediatrics)

CC: Witnessed tonic-clonic seizure during fever — outpatient follow-up next day

HPI: 2 yo M brought by parents for next-day follow-up after a witnessed tonic-clonic seizure lasting
90 seconds at home during fever. Parents called ambulance; by arrival, seizure had self-terminated.
Child was febrile (39.2°C) with concurrent viral URTI (2-day runny nose). No prior seizures.
Currently well — no fever, playing normally.

ROS: Positive: fever (at time of event), viral URTI symptoms. Negative: no focal weakness, no regression.

PMH: Fully vaccinated. No prior seizures. No neurodevelopmental issues.
FHx: Maternal uncle: childhood febrile convulsions (resolved). SHx: Lives with parents. Attended nursery.
Meds: None. Allergies: NKDA.

VITAL SIGNS: Temp 36.8°C | HR 108 | RR 28 | SpO2 99% | Wt 12.4kg

PHYSICAL EXAM: Alert, interactive, appropriate for age. Normal tone and reflexes. No focal neuro deficit.
No meningism (neck supple, no Kernig's). Throat: red, no exudate. Ears: normal bilaterally. No rash.

INVESTIGATIONS:
FBC: WBC 11.4 (lymphocytosis — viral pattern). CRP 18 (low). Blood glucose: 4.8 (normal).
Electrolytes: normal (Na 138, Ca 2.28, Glucose normal).
No LP performed (simple febrile convulsion criteria met: age 6mo-5yr, <15min, generalised, single event).

ASSESSMENT:
1. Simple febrile convulsion — meets all criteria
2. Viral URTI — likely precipitant
3. Good neurological recovery — no concern for complex febrile seizure or structural cause

PLAN:
1. Reassure parents: excellent prognosis — 30% chance of recurrence, but resolves by age 6
2. Fever management: antipyretics (paracetamol 15mg/kg q6h) — does NOT prevent febrile convulsions
3. Safety: lay child on side if seizes, do not restrain, time episode, call 999 if >5 minutes
4. EEG: NOT routinely indicated for simple febrile convulsion
5. MRI: NOT required (simple presentation, normal neuro exam, normal development)
6. Anticonvulsants: NOT started (single simple event — risk-benefit does not support prophylaxis)
7. Return if: seizure >5 minutes, focal features, afebrile seizure, developmental regression
""",
    },
    {
        "id": "transcript-050",
        "encounter_type": "Inpatient — Obstetrics",
        "condition": "Preterm Labour — 32 Weeks Gestation",
        "icd10_primary": "O60.10",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-08-19   TIME: 03:30   PROVIDER: Dr. Angela Foster, MD (Obstetrics & Gynaecology)

CC: Regular contractions and lower back pain — 32+4 weeks gestation

HPI: 27 yo G1P0 at 32+4 weeks presents with 2-hour history of regular painful contractions (every 5min)
and lower back pain. Cervix 3cm dilated on examination. Intact membranes. No PV bleeding.
Fetal movements normal. No fever.

ROS: Positive: uterine contractions q5min, back pain, mild pelvic pressure. Negative: no bleeding, no SROM.

PMH: None. PSH: None. This is first pregnancy. FHx: Mother: preterm birth at 30 weeks (herself).
SHx: Nurse. Lives with partner. Non-smoker. Meds: Folic acid 400mcg | Vitamin D.
Allergies: NKDA.

VITAL SIGNS: BP 118/72 | HR 88 | RR 16 | Temp 36.8°C | SpO2 99% | Uterine activity: q5min

EXAMINATION: Cervix: 3cm dilated, 70% effaced, cephalic presentation 3/5 palpable.
Speculum: no SROM (negative IGFBP-1 — negative fetal fibronectin). CTG: reactive — no decelerations.
USS: EFW 1,680g (50th centile for 32 weeks). Liquor normal. Doppler: normal flow.

INVESTIGATIONS:
FBC: Hb 11.4, WBC 12.8, CRP 18 (mild — possible subclinical chorioamnionitis to monitor).
High vaginal swab: sent. Urine C&S: sent.
Cervical fibronectin: positive — confirms high risk of delivery within 7 days.

ASSESSMENT:
1. Preterm labour — 32+4 weeks, confirmed (regular contractions + 3cm dilated + positive fFN)
2. Intact membranes — no PPROM
3. No evidence of chorioamnionitis currently

PLAN:
1. Tocolysis: nifedipine 20mg stat → 10-20mg q4-6h (delay delivery 48h for steroids)
2. Corticosteroids: betamethasone 12mg IM now + repeat in 24h (fetal lung maturity)
3. Magnesium sulphate: 4g loading dose → 1g/h infusion (neuroprotection <34 weeks)
4. Paediatrics (NICU) referral: anticipatory counselling with parents — 32-week prognosis
5. Continuous CTG monitoring
6. GBS prophylaxis: IV benzylpenicillin (pending GBS swab — started empirically)
7. Transfer to tertiary obstetric centre with NICU if not already
""",
    },
    {
        "id": "transcript-051",
        "encounter_type": "Outpatient — Geriatrics",
        "condition": "Comprehensive Geriatric Assessment — Delirium Prevention Post-Elective Surgery",
        "icd10_primary": "Z96.641",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-09-16   TIME: 11:00   PROVIDER: Dr. Priya Anand, MD (Geriatric Medicine)

CC: Pre-operative CGA before elective right total hip replacement — 84-year-old

HPI: 84 yo M referred by orthopaedics for pre-operative CGA before elective right THR
(severe osteoarthritis, mobility limited to 50m, pain 8/10). NICE recommends CGA in frail patients
before elective major surgery. Lives alone. Independent with basic ADLs.

ROS: Positive: right hip pain, reduced mobility. Negative: no angina, no dyspnoea at rest.

PMH: Osteoarthritis (bilateral hip/knee) | HTN | Parkinson's disease (mild, H&Y stage 2) | CKD3b (eGFR 42).
PSH: CABG 1998. FHx: Not relevant. SHx: Retired GP. Lives alone. Drives short distances.
Meds: Co-careldopa 12.5/50mg TDS | Amlodipine 10mg | Atorvastatin 40mg | Paracetamol 1g QDS.
Allergies: NSAIDs (acute kidney injury).

VITAL SIGNS: BP 138/80 sitting, 118/72 standing (orthostatic 20mmHg systolic) | HR 64 | SpO2 98% | BMI 24.2

FUNCTIONAL ASSESSMENT:
Barthel Index: 80/100 (independent with all ADLs, dressing takes longer).
Timed Up and Go: 18s (moderate fall risk). 4-metre gait speed: 0.76 m/s (frailty threshold <0.8).
Grip strength: 19kg (below age-norm — sarcopaenia risk).
MMSE: 26/30 (mild cognitive impairment — attention -2, delayed recall -2).
Clinical Frailty Scale: 4/9 (vulnerable — not frail, but at-risk).

INVESTIGATIONS: Hb 11.6 (mild iron deficiency). eGFR 42. Creatinine 1.4. Na 138, K 4.0. HbA1c 5.6%.

ASSESSMENT:
1. Vulnerable frail older adult (CFS 4) — elevated peri-operative delirium risk
2. Mild cognitive impairment — further elevates delirium risk
3. Orthostatic hypotension — peri-operative fall risk; monitor antihypertensives
4. Mild anaemia — correct pre-operatively

PLAN:
1. Pre-op IV iron (Ferinject) — Hb 11.6 with iron deficiency (ferritin 12)
2. Anaesthesia communication: prefer spinal over general (lower delirium risk in elderly)
3. Peri-op: avoid anticholinergic medications, benzodiazepines, opioid excess
4. Delirium prevention protocol: reorientation, sensory aids, early mobilisation
5. Co-careldopa: continue throughout — do NOT stop (rigidity/NMS risk in Parkinson's)
6. Occupational therapy: home assessment for post-discharge aids (raised toilet seat, rails)
7. Physiotherapy: commence pre-operative strength work; early post-op mobilisation same day
8. Discharge planning: planned home with daily care package initially
""",
    },
    {
        "id": "transcript-052",
        "encounter_type": "Inpatient — Neurology",
        "condition": "Status Epilepticus — Refractory, Convulsive",
        "icd10_primary": "G41.2",
        "data_tag": "SYNTHETIC",
        "text": """
DATE: 2025-10-07   TIME: 01:15   PROVIDER: Dr. James Okafor, MD (Neurology / Neurocritical Care)

CC: Ongoing generalised tonic-clonic seizure >30 minutes — status epilepticus

HPI: 19 yo F with known idiopathic generalised epilepsy (levetiracetam 1000mg BD) brought by ambulance.
Generalised tonic-clonic seizure started at 00:40 at home; ambulance arrived 00:55. Lorazepam 4mg IV
given by paramedics — partial response then re-seizure. Arriving at ED at 01:12 — still seizing.
Missed 2 days of levetiracetam (travelling). Concurrent febrile illness (URTI symptoms).

ROS: Via parents — well until 3 days ago. No meningism symptoms. No recent medication change.

PMH: Idiopathic generalised epilepsy (diagnosed age 16) | PSH: None.
FHx: Maternal grandmother: epilepsy. SHx: University student. Non-smoker.
Meds: Levetiracetam 1000mg BD. Allergies: NKDA.

VITAL SIGNS: HR 148 | BP 144/92 | Temp 38.2°C | SpO2 88% on O2 15L NRB | GCS 8 (post-ictal)

PHYSICAL EXAM: Active generalised tonic-clonic movements. Eyes deviated. No focal features.
Post-ictal: GCS improving to 11 after midazolam. No neck stiffness.

INVESTIGATIONS:
BM glucose: 6.8 (normal). ABG: pH 7.22, pCO2 58 (respiratory acidosis — post-ictal hypoventilation).
Na 136, K 4.0, Ca 2.28. CRP 18 (febrile illness — no meningitis).
CT head: no haemorrhage, no focal lesion.
EEG (bedside): generalised epileptiform discharges.

ASSESSMENT:
1. Refractory status epilepticus (>30min, 2nd-line benzodiazepine given)
2. Respiratory acidosis — post-ictal + muscle activity
3. Precipitants: levetiracetam non-adherence + febrile illness

PLAN:
1. IV levetiracetam 60mg/kg (max 4500mg) over 10 minutes — as 2nd anti-seizure medication
2. If no response in 10 min: phenytoin 20mg/kg IV or sodium valproate 40mg/kg IV
3. If refractory (>45min): anaesthetic team → RSI with midazolam/propofol infusion; ICU
4. Airway: position patient, suction ready, anaesthetics on standby
5. Oximetry continuous; consider intubation if SpO2 remains <92%
6. Investigate cause: LP if CT clear (exclude meningitis); MRI brain post-stabilisation
7. Epilepsy team review — levetiracetam adherence support, possible dose escalation
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
