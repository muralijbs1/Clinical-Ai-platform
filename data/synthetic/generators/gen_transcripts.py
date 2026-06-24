#!/usr/bin/env python3
"""
Generator: writes synthetic clinical SOAP notes as plain .txt files.

Run once to produce data files. Re-run to regenerate or add more notes.
Output: data/synthetic/transcripts/note_001.txt ... note_005.txt

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
