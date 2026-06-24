"""
Synthetic clinical SOAP notes and consultation transcripts.

Data tag: SYNTHETIC
Mirrors real clinical documentation: SOAP structure, clinical abbreviations,
realistic vital signs, real medication names, ICD-10 codes, and physician
language patterns derived from standard medical documentation practices.

Usage:
    from data.synthetic.transcripts import get_transcripts
    docs = get_transcripts()   # list[Document]
"""

from schemas import Document, DataTag


_TRANSCRIPTS = [
    {
        "id": "transcript-001",
        "encounter_type": "Emergency Department",
        "condition": "NSTEMI / Acute Coronary Syndrome",
        "icd10_primary": "I21.4",
        "soap_note": """DATE: 2025-03-14   TIME: 22:10   PROVIDER: Dr. Sandra Okoye, MD (Emergency Medicine)

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
   - Morphine 2mg IV PRN severe pain (use judiciously — may mask symptoms)
   - Serial hs-cTnT at 0, 1, 3, 6h — troponin rising, confirm peak
   - Repeat EKG q30min x2h then q4h or with symptom change
   - Likely cardiac catheterisation within 24h (early invasive strategy for NSTEMI)
   - Post-catheterisation: PCI if obstructive lesion found; discuss CABG if multivessel disease

2. Hypertension:
   - Continue Lisinopril 20mg — do not hold (renoprotective, cardioprotective in ACS)
   - BP goal <140/90 acutely; can tighten after acute phase

3. General:
   - NPO after midnight for likely cath AM
   - O2 via NC at 2L/min (SpO2 95% — maintain >94%)
   - Foley catheter to monitor urine output
   - Patient and wife counselled regarding diagnosis, plan, and likely catheterisation

DISPOSITION: Admitted to Cardiac Telemetry under Cardiology service. Stable condition.
""",
    },
    {
        "id": "transcript-002",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Type 2 Diabetes Follow-up",
        "icd10_primary": "E11.9",
        "soap_note": """DATE: 2025-04-08   TIME: 10:30   PROVIDER: Dr. Maria Garcia, MD (Internal Medicine)

CC: Diabetes follow-up, medication refill

HPI: 58 yo F here for routine DM2 management, 3-month interval visit. A1c at last visit 8.4%.
States she has been trying to walk 20 min/day and reduce carbohydrates. Admits to inconsistent
exercise due to work schedule (shift nurse). Home glucose log: fasting 140-190 range,
post-meal spikes to 240-260 after dinner. Denies polyuria, polydipsia, blurred vision, foot pain
or tingling. No hypoglycaemic episodes. Has not started Jardiance as discussed last visit — was
waiting for insurance approval, which cleared 2 weeks ago. Menses regular. No new complaints.

ROS: Negative for: polyuria, polydipsia, weight loss, vision changes, focal numbness, tingling,
chest pain, SOB, palpitations, nausea, vomiting. Positive: fatigue (attributes to shift work).

PMH: DM2 x 10 years | HTN x 15 years | Hyperlipidemia x 8 years | Obesity | GERD | Osteoarthritis R knee
PSH: Appendectomy 1994 | Caesarean section x2 (1989, 1992)
FHx: Mother: DM2, hypertension, stroke age 72. Father: DM2, MI age 67.
SHx: Registered nurse, 12h shift rotations. Married. Non-smoker. Alcohol: rare. No illicit drugs.

Meds: Metformin 1000mg BID | Lisinopril 20mg QD | Amlodipine 5mg QD | Atorvastatin 40mg QHS
      Omeprazole 20mg QD | Naproxen 500mg PRN (arthritis) | Acetaminophen 1g PRN

ALLERGIES: Penicillin (rash — not anaphylaxis). Shellfish (urticaria).

OBJECTIVE:
VS: BP 136/84 | HR 74 | RR 16 | Temp 37.0°C | SpO2 99% RA | Wt 88kg (up 1kg from last visit) | Ht 5'5"
BMI: 32.4 kg/m² (obese class I)

General: Well-appearing, alert, pleasant, NAD. No obvious distress.
HEENT: Normocephalic. PERRL. EOMI. Fundi: small dot haemorrhage noted OD — new finding.
CV: RRR, no murmurs. Good peripheral pulses. No JVD. Mild pretibial pitting oedema 1+ bilat (new).
Lungs: CTAB bilaterally.
Abdomen: Soft, obese, NT. Normoactive BS. No masses.
Extremities: 1+ pitting oedema bilateral ankles and shins. 10g monofilament: decreased sensation
   left plantar surface (4/10 sites) — new deficit. Right intact (10/10). Nails unremarkable.
Skin: No foot ulcers, calluses, or erythema. Skin intact bilaterally.
Neuro: A&Ox3. Grossly intact. Reflexes 1+ ankles bilaterally (slightly diminished).

LABS (TODAY):
Fasting glucose: 178 mg/dL [elevated]
HbA1c: 8.9% [worsened from 8.4% — target <7%]
Urine microalbumin/creatinine ratio: 68 mg/g [mildly elevated; ref <30; ADA threshold for nephropathy]
CBC: WBC 7.2 | Hgb 12.8 | Plt 284 [Hgb mildly low for female; check iron]
CMP: Na 138 | K 4.0 | Cl 101 | CO2 23 | BUN 19 | Cr 1.0 | Glu 178 | eGFR 68 mL/min/1.73m²
Lipids: TC 218 | LDL 138 | HDL 44 | TG 176
TSH: 2.4 mIU/L [normal]
Ferritin: 18 ng/mL [low-normal; may explain fatigue]

ASSESSMENT:
1. DM2 — suboptimal control, worsening — E11.9
   A1c 8.9% (worse); new microalbuminuria 68 mg/g; early peripheral neuropathy suspected.
   New dot haemorrhage OD → early non-proliferative diabetic retinopathy possible.
2. Diabetic peripheral neuropathy — early — E11.40
3. Diabetic kidney disease — early — E11.65 (microalbuminuria threshold crossed)
4. Hypertension — adequately controlled at 136/84 on current regimen — I10
5. Hyperlipidemia — inadequate LDL control (goal <70 for DM + microalbuminuria) — E78.5
6. Iron deficiency anaemia — mild — D50.9
7. Peripheral oedema — new — suspect amlodipine-related — R60.0

PLAN:
1. DM2 / Glycaemic Control:
   - START Empagliflozin (Jardiance) 10mg QD — now approved; renoprotective given microalbuminuria;
     also cardioprotective. Continue existing Metformin 1000mg BID.
   - Goal: A1c <7%; reassess at 3 months
   - Counsel patient: empagliflozin → increased UTI and GYN yeast infection risk; stay hydrated
   - Reinforce SMBG before and 2h after dinner where spikes are worst
   - Medical nutrition therapy referral — low-carbohydrate meal planning for shift workers
   - Pedometer challenge: step count goal 7,500/day (feasible for her schedule)

2. Diabetic Neuropathy:
   - Confirmed by monofilament testing. Annual foot exam protocol.
   - Podiatry referral for baseline evaluation and nail care guidance
   - Reinforce daily foot inspection at home

3. Diabetic Retinopathy:
   - Ophthalmology referral URGENT — new dot haemorrhage requires formal dilated exam within 4 weeks
   - If NPDR confirmed: annual ophthalmology visits minimum

4. Diabetic Kidney Disease:
   - Empagliflozin addresses microalbuminuria (renoprotective)
   - Lisinopril provides additional nephroprotection — continue at current dose
   - Recheck ACR at 6 months

5. Hypertension:
   - Continue Lisinopril 20mg. Target BP <130/80 (ADA recommendation for DM)
   - Uptitrate Amlodipine to 10mg if BP remains above goal at next visit
   - Note 1+ oedema — may be amlodipine-related; monitor

6. Hyperlipidemia:
   - Uptitrate Atorvastatin to 80mg QHS (high-intensity statin — target LDL <70 given DM + kidney)
   - Recheck lipids at 3 months

7. Anaemia / Fatigue:
   - Iron deficiency: start Ferrous sulphate 325mg QD with orange juice (vitamin C enhances absorption)
   - Recheck CBC and ferritin in 8 weeks

8. Medications:
   - Caution: NSAIDs (naproxen) contraindicated with DKD — switch to Acetaminophen 1g TID PRN arthritis
   - Consider orthopaedics referral for knee OA if acetaminophen inadequate

9. Preventive:
   - Flu vaccine: given today
   - Repeat pneumococcal vaccine due (PPSV23 if not received since age 50)
   - DEXA scan: not yet due (age 58, premenopausal)

F/U: 3 months for A1c recheck, empagliflozin response, renal function. Ophthalmology URGENT.
""",
    },
    {
        "id": "transcript-003",
        "encounter_type": "Outpatient — Primary Care",
        "condition": "Hypertension Management",
        "icd10_primary": "I10",
        "soap_note": """DATE: 2025-02-20   TIME: 14:45   PROVIDER: Dr. Robert Chen, MD (Internal Medicine)

CC: Hypertension follow-up, BP medication refill

HPI: 52 yo M for routine HTN management at 6-month interval. Reports generally feeling well.
Home BP log (last 4 weeks): morning readings 128-142/78-88, evening 118-134/72-82. Average 133/82.
Takes medications consistently — uses pill organiser. Denies headache, dizziness, chest pain,
palpitations, SOB, or visual changes. Increased aerobic exercise from 2x to 3x/week per prior
counselling. Trying low-sodium diet — reduced fast food, but admits to eating out 3x/week.
No new medications. No sick contacts.

ROS: All systems reviewed, negative except: occasional occipital headaches on awakening (new, ~monthly).
Denies visual changes, nausea, epistaxis, oedema, focal weakness.

PMH: Essential HTN x 18 years | Hyperlipidemia x 12 years | BPH (mild) | Ex-smoker
PSH: Inguinal hernia repair 2007
FHx: Father: HTN, fatal MI age 69. Mother: HTN, alive age 78. Sister: HTN.
SHx: Accountant, desk job. Married with 3 adult children. Tobacco: quit 14 years ago (22 pack-years).
Alcohol: 5-7 units/week (glasses wine, beer). No illicit drugs.

Meds: Amlodipine 10mg QD | Lisinopril 20mg QD | Hydrochlorothiazide 25mg QAM | Atorvastatin 20mg QHS
      Tamsulosin 0.4mg QHS (BPH) | Aspirin 81mg QD

ALLERGIES: NKDA

OBJECTIVE:
VS: BP 138/86 (R arm, seated, 5-min rest) → repeat 136/84
HR 68 | RR 16 | Temp 37.0°C | SpO2 98% RA | Wt 88kg (stable) | Ht 5'11" | BMI 24.5

General: Well-appearing male, no distress.
HEENT: PERRL. EOMI. Fundoscopy: A/V ratio approximately 2:3 (mild arteriovenous nipping noted —
consistent with chronic HTN). No haemorrhages, papilloedema, or exudates.
Neck: Supple. No JVD. Carotids 2+ without bruits. No thyromegaly.
CV: RRR 68 bpm. Normal S1/S2. No murmurs, rubs, or gallops. Peripheral pulses 2+ bilaterally.
Lungs: CTAB. No adventitious sounds.
Abdomen: Soft, NT/ND. No aortic bruit. Normoactive BS. No bruits.
Extremities: No oedema, clubbing, or cyanosis. Ankle-brachial index not formally measured today.
Neuro: A&Ox3. No focal deficits.

LABS (TODAY):
CBC: WBC 6.4 | Hgb 15.2 | Plt 298 [normal]
CMP: Na 140 | K 3.7 | Cl 102 | CO2 26 | BUN 14 | Cr 0.9 | Glu 94 | eGFR >90 [normal]
Lipids: TC 196 | LDL 121 | HDL 52 | TG 92 [well controlled]
Urine microalbumin/Cr ratio: negative [no nephropathy]
Fasting glucose: 94 mg/dL [normal — monitoring given father's DM2]

EKG: NSR at 68. Normal axis. QTc 432ms. Borderline LVH by Sokolow-Lyon criteria
(S in V1 + R in V5 = 38mm; voltage criterion only, no ST/T changes). Compare to prior (unchanged x2 years).

ASSESSMENT:
1. Essential Hypertension — partially controlled — I10
   Average 137/85 at home; at-goal target per JNC-8 (<140/90) but above ACC/AHA 2017 (<130/80).
   On triple therapy (CCB + ACE + thiazide). Voltage LVH by ECG (unchanged).
   Borderline LVH is an end-organ marker — warrants discussion of intensification.
2. Hyperlipidemia — adequately controlled at current dose — E78.5
3. BPH — stable, symptom-free on tamsulosin — N40.0
4. Alcohol use — 5-7 units/week; above recommended limit — discuss counselling — Z72.1

PLAN:
1. Hypertension:
   - At current triple therapy maximum tolerated dose. BP 137/85 is at JNC-8 goal but above ACC/AHA 2017.
   - Options discussed with patient: (a) add spironolactone 25mg for resistant HTN, (b) intensify
     lifestyle. Patient prefers lifestyle intensification for 3 months before adding medication.
   - LIFESTYLE: Low-sodium diet (<2g/day sodium). Formal DASH diet counselling referral.
     Alcohol reduction counselling — target <14 units/week. Continue aerobic exercise 3x/week.
   - Home BP monitoring: take readings AM and PM, log in app, bring to next visit.
   - Recheck BP in 3 months. If still >130/80: add spironolactone.
   - Mild morning headaches: likely related to nocturnal BP rise. Evening amlodipine timing may help
     — counsel to take amlodipine at bedtime instead of morning; discuss at next visit.

2. Fundoscopic Findings:
   - A/V nipping consistent with chronic HTN — no haemorrhages or papilloedema (good).
   - Annual fundoscopy recommended (ophthalmology or primary care)

3. LVH on ECG:
   - Voltage criterion only, unchanged. Continue strict BP control.
   - If worsening: echocardiography to quantify LV mass.

4. Hyperlipidemia:
   - LDL 121 at target for patient without DM (goal <130). Continue Atorvastatin 20mg.
   - Recheck lipids annually.

5. Diabetes Prevention:
   - Fasting glucose normal (94). Continue annual fasting glucose; HbA1c at next visit (paternal DM2).

6. Alcohol:
   - 5-7 units/week is above recommended limits and raises BP. Brief counselling provided.
   - Referral to health coaching / brief intervention for alcohol if patient interested.

7. Medications:
   - Refills: Amlodipine x 180d, Lisinopril x 180d, HCTZ x 180d, Atorvastatin x 180d, Aspirin x 365d
   - Monitor potassium at next visit (HCTZ may lower, Lisinopril may raise — currently 3.7, normal)

F/U: 3 months. Patient instructed to call if developing severe headache, visual changes, chest pain,
or if home BP consistently >160/100.
""",
    },
    {
        "id": "transcript-004",
        "encounter_type": "Inpatient — ICU",
        "condition": "Urosepsis / Septic Shock",
        "icd10_primary": "A41.9",
        "soap_note": """DATE: 2025-01-07   TIME: 03:20   PROVIDER: Dr. Lisa Ramirez, MD (Pulmonary/Critical Care)

CC: Septic shock secondary to urosepsis

HPI: 74 yo F transferred from ED to MICU at 03:00. Family reports 3-day h/o dysuria, frequency,
and confusion, worsening today. Presented to ED in acute distress. PMH significant for DM2, CHF
(EF 40%), CKD stage 3b (baseline Cr 1.6-1.8), and AFib on warfarin. Source likely urinary — UA
positive LE/nitrites, urine culture pending. Initially hypotensive in ED (SBP 78) — received 2L
NS, BP partially responsive; norepinephrine initiated. Temperature 39.8°C. Altered mental status
persisting. Lactate 4.1 on arrival.

PMH: Sepsis secondary to UTI x2 (2022, 2023) | DM2 x 22 years | CHF (systolic, EF 40%) x 4 years
     CKD stage 3b (baseline Cr 1.6-1.8) | AFib — on warfarin | HTN x 20 years | Hypothyroidism
PSH: Hysterectomy 1984 | Colectomy (partial, diverticulitis) 2010

FHx: Not contributory to current admission.

SHx: Widowed, lives alone. Daughter lives 15 min away (present now). Retired schoolteacher.
Denies tobacco and alcohol.

Meds (home): Warfarin 5mg QD (for AFib) | Metformin 500mg BID | Furosemide 40mg QD | Metoprolol 25mg BID
             Lisinopril 20mg QD | Levothyroxine 75mcg QD | Atorvastatin 40mg QHS

ALLERGIES: Cephalosporins (documented anaphylaxis). NKDA otherwise.

OBJECTIVE:
VS on ICU admission: BP 88/54 | HR 118 (irregular — AFib) | RR 28 | Temp 39.8°C | SpO2 90% on NRB mask
Wt 61kg | Central line: CVP 4 cmH2O (low — still volume depleted)
Urine output last 2h: 35 mL total (oliguric — goal >0.5 mL/kg/hr = 30.5 mL/hr)

General: Acutely ill-appearing, elderly female. Eyes open but not tracking. Not following commands.
Diaphoretic. Skin mottled over knees bilaterally.
HEENT: Pupils 3mm equal, sluggish reaction. Dry mucous membranes. No scleral icterus.
Neck: Supple. Central line (R IJ) in place.
CV: Irregularly irregular, tachycardic. S1/S2 present. No murmurs. Peripheral pulses faint bilat.
Lungs: Bibasilar crackles. Decreased breath sounds RLL.
Abdomen: Soft, mildly distended. Suprapubic tenderness. Normoactive BS. Foley in place — cloudy amber urine.
Extremities: Mottling bilateral knees/calves. Capillary refill 4s (delayed). No edema (dry).
Neuro: Altered — GCS 9 (E3V2M4). Not following commands. Localising to pain. AFVPU: Confusion.

LABS (MICU ADMISSION):
CBC: WBC 22.4 [ELEVATED] | Hgb 9.8 [LOW] | Plt 88 [LOW — DIC concern] | Bands 18% [elevated bands]
CMP: Na 128 [LOW — hyponatremia] | K 5.4 [HIGH — renal] | Cl 93 | CO2 16 [LOW — metabolic acidosis]
     BUN 52 [ELEVATED] | Cr 2.9 [ELEVATED — AKI on CKD] | Glu 312 [HIGH] | Ca 8.1 | Albumin 2.8 [LOW]
Lactate: 4.1 mmol/L [SEVERELY ELEVATED; ref <2 — septic shock territory]
Procalcitonin: 18.4 ng/mL [MARKEDLY ELEVATED; ref <0.5]
ABG: pH 7.26 | PaCO2 28 | PaO2 62 | HCO3 12 | SaO2 90% [metabolic acidosis with resp compensation]
INR: 3.8 [ELEVATED — warfarin + sepsis effects]
Fibrinogen: 148 mg/dL [LOW; ref >200 — DIC pattern]
D-dimer: 8.4 ug/mL [MARKEDLY ELEVATED]
Blood cultures x2 (central and peripheral): PENDING
UA: WBC >100/hpf | Nitrites POSITIVE | LE LARGE | Bacteria MANY | RBC 12/hpf
Urine Cx: PENDING (Gram-negative rods on Gram stain preliminary)

EKG: Irregularly irregular, AFib at 118 bpm. No acute ST changes. QTc 492ms (prolonged — monitor).

CXR: Bilateral patchy infiltrates — L > R. RLL atelectasis vs early infiltrate. Possible early ARDS
vs cardiogenic pulmonary oedema (difficult to differentiate). No pneumothorax.

Echo (bedside, done in ED): EF ~35-38% (at lower end of prior known EF). No tamponade. IVC
collapsible (volume-responsive). Moderate pulmonary hypertension evident.

ASSESSMENT:
1. Septic Shock — urosepsis source — A41.9 + R65.21 (severe sepsis with septic shock)
   qSOFA 3/3 (AMS + RR≥22 + SBP≤100). SOFA estimated 10-12 (respiratory, renal, hepatic, coagulation
   components). Gram-negative rods on urine Gram stain — E. coli/Klebsiella most likely.
2. Acute Kidney Injury — stage 3 — N17.9 on CKD stage 3b
   Cr 2.9 (baseline 1.6-1.8); oliguric; haemodynamic compromise contribution.
3. Sepsis-induced coagulopathy / early DIC — D65
   Plt 88, Fibrinogen 148, D-dimer 8.4, INR 3.8.
4. Metabolic acidosis — lactic / type A — E87.2
   pH 7.26, Lactate 4.1, HCO3 12. Respiratory compensation (RR 28, PaCO2 28).
5. Hypoxaemic respiratory failure — J96.01
   PaO2 62 on NRB mask; bilateral infiltrates — early ARDS vs cardiogenic pulmonary oedema.
6. Hyponatraemia — likely SIADH in setting of sepsis — E87.1
7. Atrial Fibrillation — rate uncontrolled — I48.91
8. DM2 — decompensated (glucose 312) — E11.22
9. CHF — systolic, EF 35-38% — I50.20 — fluid management critical given shock vs HF

PLAN:
1. SEPSIS SHOCK RESUSCITATION:
   - Norepinephrine via central line: currently at 0.12 mcg/kg/min; titrate to MAP ≥65 mmHg
   - Cautious fluid challenge: given EF 35% and CHF risk, 250mL NS boluses with reassessment
     (IVC collapsible suggests volume-responsiveness — but guard against pulmonary oedema)
   - Target: MAP ≥65, lactate clearance ≥10% per 2h, urine output ≥0.5 mL/kg/hr
   - Vasopressin 0.03 units/min (add as second vasopressor if norepinephrine >0.25 mcg/kg/min)

2. ANTIBIOTICS — Given cephalosporin anaphylaxis:
   - Levofloxacin 750mg IV q24h (gram-negative UTI coverage incl. E. coli, Klebsiella)
   - PLUS Gentamicin 1.5 mg/kg IV q8h (double gram-negative coverage for shock; monitor renal function)
   - NO cephalosporins — anaphylaxis documented
   - Adjust to sensitivities when culture finalised (24-48h)
   - Vancomycin NOT required unless gram-positive source identified

3. RESPIRATORY:
   - Current: NRB mask, SpO2 90-92% target initially
   - If SpO2 <88% or WOB increases: discuss BiPAP or low-threshold for intubation
   - Bilateral infiltrates: favour ARDS lung-protective ventilation if intubation required

4. RENAL:
   - Hold Metformin (lactic acidosis risk in AKI)
   - Hold Lisinopril (hypoperfusion risk)
   - Hold Furosemide (need perfusion pressure first; no diuresis until MAP stable)
   - Monitor UO q1h via Foley; if <0.5 mL/kg/hr for >6h → nephrology consult for CRRT discussion
   - Renal labs q8h (Cr, BUN, electrolytes)

5. COAGULOPATHY:
   - Hold Warfarin (INR 3.8 — supratherapeutic + sepsis consumptive coagulopathy)
   - FFP 2 units now if active bleeding or INR >4 and procedure needed
   - Platelet transfusion if Plt <50 and active bleeding or procedure
   - Monitor fibrinogen q12h; cryoprecipitate if fibrinogen <100

6. GLYCAEMIC CONTROL:
   - Insulin infusion protocol: maintain glucose 140-180 mg/dL
   - Glucose q1h while insulin infusing

7. MONITORING:
   - A-line placement for continuous BP monitoring + frequent ABGs
   - Repeat lactate q2h until <2.0 or confirmed clearance
   - ABG q4-6h to monitor respiratory/acid-base status
   - Repeat CBC, CMP, coagulation q6h x 24h
   - Repeat echo if haemodynamic status not improving

8. GOALS OF CARE:
   - Family (daughter) at bedside; meeting planned for 08:00 regarding prognosis
   - Patient has DNR/DNI per prior directive — CONFIRM with family before any intubation
   - [CRITICAL: verify advance directive paperwork in chart and with daughter]
   - If patient deteriorates to requiring intubation — family meeting immediately

DISPOSITION: MICU, continuous monitoring. Critical condition. Guarded prognosis.
""",
    },
    {
        "id": "transcript-005",
        "encounter_type": "Outpatient — Surgical",
        "condition": "Post-operative — Laparoscopic Cholecystectomy",
        "icd10_primary": "Z48.815",
        "soap_note": """DATE: 2025-05-12   TIME: 09:00   PROVIDER: Dr. Thomas Eriksson, MD (General Surgery)
Post-operative Day 7 — Laparoscopic Cholecystectomy (s/p 2025-05-05)

CC: Post-op check, wound check

HPI: 46 yo F for 1-week post-operative visit after elective laparoscopic cholecystectomy for
symptomatic cholelithiasis with acute cholecystitis. Procedure uneventful — critical view of
safety documented, no IOC performed (anatomy clear), no conversion to open, OR time 62 minutes.
Discharged day of surgery (same-day surgery protocol). Patient reports progressive improvement.
Pain now 2/10 (was 6/10 POD1). Tolerating regular diet without nausea. Returned to desk work
POD5 (light duties). Incisions healing well per patient report. No fever at home. No jaundice.
Denies: clay-coloured stools, dark urine, right shoulder tip pain, distension, rigours.
Gas and flatus since POD1. BM POD2 (normal, brown). Ambulating independently.
No complications at home.

PMH: Cholelithiasis with acute cholecystitis — now s/p lap chole | HTN | Hypothyroidism | Obesity
PSH: Appendectomy 1999 | C-section 2003
FHx: Mother: gallstones. Father: HTN.
SHx: Legal assistant, desk job. Married. Non-smoker. Social alcohol. No illicit drugs.

Meds (post-op, current):
- Acetaminophen 1000mg q6h PRN pain (using ~2x/day now)
- Ibuprofen 400mg q6h PRN (using sparingly — renal caution)
- Omeprazole 20mg QD (stress ulcer / GI protection)
- Levothyroxine 88mcg QD (continue)
- Lisinopril 20mg QD (continue)
- Docusate 100mg BID (stool softener — continue x 2 more weeks)

ALLERGIES: Latex (contact urticaria). NKDA.

OBJECTIVE:
VS: BP 128/80 | HR 72 | RR 16 | Temp 37.0°C | SpO2 99% RA | Wt 82kg (stable) | Ht 5'6"

General: Well-appearing, comfortable female. Alert and in NAD. Good colour. No jaundice.
HEENT: Sclera non-icteric. Conjunctivae pink. Oropharynx clear.
Abdomen: Soft, non-distended. Mild tenderness on deep palpation RUQ — expected POD7.
   No guarding, rebound, or rigidity. Bowel sounds present x4. No Murphy's sign (gallbladder absent).

INCISION ASSESSMENT:
   Port site 1 (umbilical, 12mm): Healed well. No erythema. No discharge. Sutures absorbed.
     Minimal bruising. Skin edges well-approximated.
   Port site 2 (epigastric, 5mm): Well-healed. Clean and dry. No signs of infection.
   Port site 3 (RUQ, 5mm): Mild periincisional ecchymosis, resolving. No erythema, no warmth,
     no purulence. Well-approximated.
   Port site 4 (RUQ lateral, 5mm): Well-healed. Clean.

Shoulder pain: Denies right shoulder tip pain (no residual CO2 diaphragmatic irritation).
Extremities: No lower extremity oedema. No calf tenderness. Pedal pulses 2+ bilat.

Pathology result: Chronic cholecystitis with acute-on-chronic cholecystitis. Cholelithiasis.
No dysplasia or malignancy. [EXPECTED — communicated to patient]

LABS (today — selective, per post-op protocol for complications check):
ALT: 28 U/L [NORMAL — important to check for bile duct injury; was 62 pre-op due to cholecystitis]
AST: 24 U/L [NORMAL]
Total bilirubin: 0.8 mg/dL [NORMAL — no bile duct injury / biloma concern]
Alk Phos: 88 U/L [NORMAL — previously 134; resolving]
[All liver enzymes trending toward normal — excellent sign, no biliary complication]

ASSESSMENT:
1. Post-op Day 7 s/p laparoscopic cholecystectomy — uncomplicated — Z48.815
   Healing well. LFTs normalising. No signs of bile duct injury, wound infection, or biloma.
2. Hypertension — stable, BP 128/80 on Lisinopril — I10
3. Hypothyroidism — stable on Levothyroxine — E03.9
4. Obesity — BMI 29.6 — E66.9

PLAN:
1. Post-Operative Care:
   - No complications identified. Normal post-cholecystectomy recovery course.
   - Pain: Taper acetaminophen — use PRN only (as needed for pain >3/10). Stop ibuprofen at 2 weeks.
   - Activity: No restrictions at 1 week for desk work and light activities.
   - NO heavy lifting >10 lbs until 4 weeks post-op (port site hernia prevention)
   - Can return to gym / light exercise at 3 weeks (avoid core exertion until 4 weeks)
   - Driving: Cleared as of today (no opioids, pain controlled, reflex intact)
   - Showering: Fine — keep incisions clean and dry. No submerging in pool/bath for 2 more weeks.
   - Diet: No restrictions. Fatty foods well tolerated now without gallbladder — occasionally
     transient diarrhoea post-fat meal is normal for first 6-8 weeks (bile acid adjustment).

2. Wound Care:
   - No dressing needed — all sites healed. Steri-strips can be removed gently if still attached.
   - Return if: incision becomes red, warm, swollen, or produces discharge — wound infection.

3. Pathology:
   - Results reviewed with patient. No malignancy. Chronic cholecystitis — explains chronic symptoms.

4. Medications:
   - Discontinue Omeprazole at 4 weeks post-op (no longer needed without ongoing NSAID use).
   - Discontinue Docusate at 2 weeks (constipation risk resolved).
   - Continue Levothyroxine, Lisinopril as chronic medications.

5. Surveillance:
   - No further imaging or labs required unless new symptoms develop.
   - LFTs trending to normal — no further follow-up needed unless pain, jaundice, fever.

6. Return Precautions — Return to ED or call office if:
   - Fever >38.5°C / >101.3°F
   - Worsening abdominal pain (not improving or getting worse)
   - Jaundice (yellow skin, yellow eyes)
   - Dark urine / clay-coloured stools (biliary leak signs)
   - Persistent nausea/vomiting unable to tolerate oral fluids

F/U: No routine follow-up needed. Call office or return PRN if any concerning symptoms.
Discharge from surgical care. Manage HTN and hypothyroidism with primary care.
""",
    },
]


# ── Public API ────────────────────────────────────────────────────────────────

def get_transcripts() -> list[Document]:
    """
    Returns the synthetic SOAP note corpus as Document objects.
    Each document is one complete clinical encounter note.
    Tag: SYNTHETIC — realistic clinical language, no real patients.
    """
    docs = []
    for rec in _TRANSCRIPTS:
        metadata = {
            "encounter_id": rec["id"],
            "encounter_type": rec["encounter_type"],
            "condition": rec["condition"],
            "icd10_primary": rec["icd10_primary"],
            "source_type": "soap_note",
        }
        docs.append(
            Document(
                id=rec["id"],
                text=rec["soap_note"],
                metadata=metadata,
                tag=DataTag.SYNTHETIC,
            )
        )
    return docs
