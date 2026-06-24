"""
Synthetic diagnostic ML feature vectors and differential diagnosis cases.

Data tag: SYNTHETIC
Mirrors MIMIC-IV / eICU diagnostic record structure: demographics, vital signs,
lab values, composite severity scores (SOFA, qSOFA, NEWS2, SIRS), and ranked
differential diagnoses with confidence scores and evidence lists.

Sepsis thresholds used:
  SIRS ≥2 criteria + infection source = SIRS sepsis
  qSOFA ≥2 = high-risk bedside screen
  SOFA ≥2 increase = organ dysfunction (Sepsis-3)
  Lactate >2 = hypoperfusion; >4 = shock territory
  NEWS2 ≥5 with infection = likely sepsis; ≥7 = escalate immediately

Usage:
    from data.synthetic.diagnostic_cases import get_diagnostic_cases
    docs = get_diagnostic_cases()   # list[Document]
"""

import json
from schemas import Document, DataTag


_CASES = [
    {
        "case_id": "DIAG-2025-001",
        "presentation": "Fever, altered mental status, hypotension",
        "demographics": {
            "age": 72, "sex": "F", "bmi": 24.7,
            "charlson_comorbidity_index": 5,
            "comorbidities": ["DM2", "CHF_EF40", "CKD3b", "AFib", "HTN"],
        },
        "vital_signs": {
            "heart_rate_bpm": 118,
            "systolic_bp_mmhg": 88,
            "diastolic_bp_mmhg": 54,
            "map_mmhg": 65,
            "respiratory_rate_per_min": 28,
            "temperature_celsius": 39.8,
            "spo2_percent": 90.0,
            "timestamp": "2025-01-07T03:20:00",
        },
        "laboratory_values": {
            "wbc_k_ul": 22.4,
            "lactate_mmol_l": 4.1,
            "platelets_k_ul": 88,
            "creatinine_mg_dl": 2.9,
            "bilirubin_mg_dl": 1.2,
            "ph_arterial": 7.26,
            "paco2_mmhg": 28,
            "hco3_meq_l": 12,
            "glucose_mg_dl": 312,
            "sodium_meq_l": 128,
            "potassium_meq_l": 5.4,
            "procalcitonin_ng_ml": 18.4,
            "fibrinogen_mg_dl": 148,
            "inr": 3.8,
            "albumin_g_dl": 2.8,
        },
        "severity_scores": {
            "sirs_criteria_met": 4,
            "sirs_positive": True,
            "qsofa_score": 3,
            "qsofa_components": {
                "sbp_le_100": True,
                "rr_ge_22": True,
                "altered_mental_status": True,
            },
            "sofa_score": 11,
            "sofa_components": {
                "respiratory_pf_ratio": 185,
                "cardiovascular_map": 65,
                "hepatic_bilirubin": 1.2,
                "coagulation_platelets": 88,
                "renal_creatinine": 2.9,
                "neurological_gcs": 9,
            },
            "news2_score": 13,
            "news2_risk_level": "HIGH — Escalate immediately",
        },
        "clinical_context": {
            "infection_source_suspected": "Urinary tract (E. coli)",
            "culture_status": "Blood cultures pending; urine Gram stain: GNR",
            "antibiotic_hours_from_presentation": 1.2,
            "fluid_given_ml": 2000,
            "vasopressor_started": True,
            "vasopressor_agent": "Norepinephrine 0.12 mcg/kg/min",
        },
        "differential_diagnosis": [
            {
                "rank": 1,
                "diagnosis": "SEPTIC SHOCK",
                "icd10": "A41.9 + R65.21",
                "confidence": 0.95,
                "probability": 0.95,
                "likelihood_category": "VERY LIKELY",
                "key_features": [
                    "SIRS 4/4 criteria met",
                    "qSOFA 3/3 — confirmed high-risk",
                    "Lactate 4.1 mmol/L (shock territory >4)",
                    "MAP 65 despite 2L fluid + vasopressor required",
                    "Urinary source: GNR on Gram stain",
                    "Procalcitonin 18.4 ng/mL (markedly elevated)",
                ],
                "supporting_labs": ["Lactate 4.1", "WBC 22.4", "PCT 18.4", "Plt 88 (DIC risk)"],
                "recommended_action": "ICU admission; continue vasopressors; broad-spectrum IV antibiotics",
            },
            {
                "rank": 2,
                "diagnosis": "SEPSIS-INDUCED DIC",
                "icd10": "D65",
                "confidence": 0.72,
                "probability": 0.68,
                "likelihood_category": "LIKELY (secondary to sepsis)",
                "key_features": [
                    "Platelets 88K (LOW)",
                    "Fibrinogen 148 mg/dL (<200)",
                    "INR 3.8 (supratherapeutic in non-anticoagulated context)",
                    "D-dimer markedly elevated (pattern consistent with DIC)",
                ],
                "recommended_action": "Monitor fibrinogen q12h; FFP if active bleeding or INR >4 for procedure",
            },
            {
                "rank": 3,
                "diagnosis": "ACUTE KIDNEY INJURY on CKD",
                "icd10": "N17.9 on N18.3",
                "confidence": 0.90,
                "probability": 0.90,
                "likelihood_category": "VERY LIKELY (secondary complication)",
                "key_features": [
                    "Creatinine 2.9 (baseline 1.6-1.8 — acute-on-chronic)",
                    "BUN 52 (elevated)",
                    "Oliguria: 35 mL/2h (<0.5 mL/kg/hr)",
                    "Haemodynamic compromise (MAP 65 borderline)",
                ],
                "recommended_action": "Hourly urine output monitoring; hold nephrotoxics; nephrology if anuric",
            },
            {
                "rank": 4,
                "diagnosis": "CARDIOGENIC SHOCK",
                "icd10": "R57.0",
                "confidence": 0.25,
                "probability": 0.08,
                "likelihood_category": "LESS LIKELY",
                "distinguishing_features": [
                    "Known CHF EF 40% — background risk",
                    "However: fever 39.8°C strongly suggests infectious source",
                    "Bedside echo: IVC collapsible (volume-responsive — not cardiogenic pattern)",
                ],
                "recommended_action": "Exclude with serial echos and troponin trending",
            },
        ],
        "outcome_48h": "Vasopressor weaned, lactate cleared to 1.8, transferred to step-down",
        "outcome_28day": "Survived — discharged to SNF",
        "sepsis_alert_triggered": True,
        "alert_trigger_time": "2025-01-07T01:15:00",
        "time_to_antibiotics_minutes": 72,
    },
    {
        "case_id": "DIAG-2025-002",
        "presentation": "Chest pain, diaphoresis, dyspnoea at rest",
        "demographics": {
            "age": 63, "sex": "M", "bmi": 28.7,
            "charlson_comorbidity_index": 3,
            "comorbidities": ["HTN", "DM2", "Hyperlipidemia", "Ex-smoker_35pack"],
        },
        "vital_signs": {
            "heart_rate_bpm": 98,
            "systolic_bp_mmhg": 162,
            "diastolic_bp_mmhg": 94,
            "map_mmhg": 117,
            "respiratory_rate_per_min": 20,
            "temperature_celsius": 37.1,
            "spo2_percent": 95.0,
            "timestamp": "2025-03-14T22:10:00",
        },
        "laboratory_values": {
            "hs_troponin_t_ng_l": 118,
            "hs_troponin_t_delta_1h_ng_l": 53,
            "ck_mb_ng_ml": 9.4,
            "bnp_pg_ml": 148,
            "wbc_k_ul": 9.8,
            "creatinine_mg_dl": 1.1,
            "glucose_mg_dl": 194,
            "ldl_mg_dl": 162,
            "hdl_mg_dl": 38,
            "triglycerides_mg_dl": 198,
            "lactate_mmol_l": 1.1,
        },
        "ekg_findings": {
            "rhythm": "Sinus tachycardia",
            "rate": 98,
            "st_changes": "T-wave inversions V2-V4; biphasic T in V1",
            "stemi_criteria_met": False,
            "new_vs_prior": "New changes vs EKG 6 months ago",
            "qtc_ms": 441,
        },
        "severity_scores": {
            "sirs_criteria_met": 1,
            "sirs_positive": False,
            "qsofa_score": 0,
            "timi_risk_score": 5,
            "grace_risk_score_estimated": "High (>140)",
            "heart_score": 8,
        },
        "differential_diagnosis": [
            {
                "rank": 1,
                "diagnosis": "NON-ST-ELEVATION MYOCARDIAL INFARCTION (NSTEMI)",
                "icd10": "I21.4",
                "confidence": 0.94,
                "probability": 0.94,
                "likelihood_category": "VERY LIKELY",
                "key_features": [
                    "Rising hs-cTnT: 65→118 ng/L (delta 53 ng/L — meets ESC 0/1h rule-in ≥6 ng/L)",
                    "T-wave inversions V2-V4 (new anterior changes)",
                    "High-risk profile: age 63M, DM, HTN, dyslipidaemia, family hx",
                    "TIMI score 5/7 (high risk)",
                    "HEART score 8 (high — >50% MACE risk)",
                    "No ST elevation — differentiates from STEMI",
                ],
                "supporting_labs": ["hs-cTnT rising 53 ng/L delta", "CK-MB 9.4 elevated", "BNP 148"],
                "recommended_action": "Aspirin + P2Y12 loading; heparin; urgent cardiology consult; cath within 24h",
            },
            {
                "rank": 2,
                "diagnosis": "UNSTABLE ANGINA",
                "icd10": "I20.0",
                "confidence": 0.35,
                "probability": 0.04,
                "likelihood_category": "LESS LIKELY",
                "distinguishing_features": [
                    "Rising troponin rules against unstable angina (no biomarker rise expected)",
                    "Troponin rise confirms myocardial injury — NSTEMI preferred",
                ],
                "recommended_action": "De-prioritised given confirmed troponin rise",
            },
            {
                "rank": 3,
                "diagnosis": "PULMONARY EMBOLISM",
                "icd10": "I26.09",
                "confidence": 0.20,
                "probability": 0.02,
                "likelihood_category": "UNLIKELY",
                "distinguishing_features": [
                    "No pleuritic pain, no unilateral leg swelling",
                    "EKG pattern: T-wave inversions anterior (not S1Q3T3 PE pattern)",
                    "Chest pain character: pressure, radiating — not pleuritic",
                    "D-dimer not elevated (not checked but pre-test probability low)",
                ],
                "recommended_action": "D-dimer if clinical picture changes; CT-PE not currently indicated",
            },
        ],
        "outcome_28day": "PCI with DES to LAD lesion — successful revascularisation",
        "sepsis_alert_triggered": False,
    },
    {
        "case_id": "DIAG-2025-003",
        "presentation": "Progressive dyspnoea, bilateral leg swelling, orthopnoea",
        "demographics": {
            "age": 71, "sex": "F", "bmi": 32.1,
            "charlson_comorbidity_index": 4,
            "comorbidities": ["HTN", "DM2", "Hyperlipidemia", "Prior_MI_2021"],
        },
        "vital_signs": {
            "heart_rate_bpm": 104,
            "systolic_bp_mmhg": 148,
            "diastolic_bp_mmhg": 92,
            "map_mmhg": 111,
            "respiratory_rate_per_min": 22,
            "temperature_celsius": 37.1,
            "spo2_percent": 92.0,
            "timestamp": "2025-05-20T16:00:00",
        },
        "laboratory_values": {
            "bnp_pg_ml": 1480,
            "nt_probnp_pg_ml": 4200,
            "hs_troponin_t_ng_l": 28,
            "wbc_k_ul": 8.1,
            "hemoglobin_g_dl": 11.4,
            "creatinine_mg_dl": 1.6,
            "bun_mg_dl": 34,
            "sodium_meq_l": 134,
            "potassium_meq_l": 4.6,
            "albumin_g_dl": 3.2,
            "lactate_mmol_l": 1.4,
            "tsh_miu_l": 3.8,
        },
        "imaging": {
            "cxr": "Cardiomegaly. Bilateral pleural effusions. Pulmonary venous congestion. Kerley B lines.",
            "echo_ef_percent": 32,
            "echo_findings": "Dilated LV, global hypokinesis, moderate MR, elevated PCWP estimated",
        },
        "severity_scores": {
            "nyha_class": "III",
            "sirs_criteria_met": 1,
            "sirs_positive": False,
            "qsofa_score": 0,
            "news2_score": 5,
        },
        "differential_diagnosis": [
            {
                "rank": 1,
                "diagnosis": "ACUTE DECOMPENSATED HEART FAILURE (systolic)",
                "icd10": "I50.20",
                "confidence": 0.96,
                "probability": 0.96,
                "likelihood_category": "VERY LIKELY",
                "key_features": [
                    "BNP 1480 pg/mL (markedly elevated; >400 = very high probability)",
                    "NT-proBNP 4200 pg/mL",
                    "CXR: cardiomegaly + bilateral effusions + pulmonary vascular congestion",
                    "Echo EF 32% (reduced — systolic HF)",
                    "Orthopnoea, PND, bilateral leg oedema (classic HF triad)",
                    "Prior MI 2021 — substrate for ischaemic cardiomyopathy",
                ],
                "supporting_labs": ["BNP 1480", "CXR congestion", "Echo EF 32%"],
                "recommended_action": "IV furosemide diuresis; telemetry monitoring; cardiology consult; optimise GDMT",
            },
            {
                "rank": 2,
                "diagnosis": "CARDIORENAL SYNDROME",
                "icd10": "I13.10",
                "confidence": 0.65,
                "probability": 0.60,
                "likelihood_category": "LIKELY (secondary complication)",
                "key_features": [
                    "Creatinine 1.6 (elevated — AKI risk with aggressive diuresis)",
                    "BUN 34 (elevated)",
                    "Na 134 (dilutional hyponatraemia — common in ADHF)",
                ],
                "recommended_action": "Cautious diuresis; monitor renal function daily; avoid nephrotoxins",
            },
            {
                "rank": 3,
                "diagnosis": "PULMONARY EMBOLISM",
                "icd10": "I26.09",
                "confidence": 0.18,
                "probability": 0.04,
                "likelihood_category": "UNLIKELY",
                "distinguishing_features": [
                    "Bilateral (not unilateral) oedema favours HF",
                    "BNP 1480 — extreme elevation favours HF not PE",
                    "No pleuritic pain, no haemoptysis",
                    "Echo shows global LV dysfunction — not RV dilation pattern of PE",
                ],
                "recommended_action": "CT-PE not currently indicated; reassess if clinical picture changes",
            },
        ],
        "outcome_48h": "Diuresis 3.2L net negative; dyspnoea improved; SpO2 97% on RA by 48h",
        "outcome_28day": "Discharged home with optimised GDMT; LVEF 38% at 4-week echo",
        "sepsis_alert_triggered": False,
    },
    {
        "case_id": "DIAG-2025-004",
        "presentation": "Annual wellness check — asymptomatic, incidental finding",
        "demographics": {
            "age": 58, "sex": "M", "bmi": 29.4,
            "charlson_comorbidity_index": 1,
            "comorbidities": ["HTN"],
        },
        "vital_signs": {
            "heart_rate_bpm": 72,
            "systolic_bp_mmhg": 142,
            "diastolic_bp_mmhg": 88,
            "map_mmhg": 106,
            "respiratory_rate_per_min": 16,
            "temperature_celsius": 36.9,
            "spo2_percent": 98.0,
            "timestamp": "2025-04-15T10:00:00",
        },
        "laboratory_values": {
            "hba1c_percent": 7.2,
            "fasting_glucose_mg_dl": 132,
            "creatinine_mg_dl": 0.95,
            "egfr_ml_min": 84,
            "ldl_mg_dl": 148,
            "hdl_mg_dl": 42,
            "triglycerides_mg_dl": 188,
            "tsh_miu_l": 2.9,
            "wbc_k_ul": 6.8,
            "hemoglobin_g_dl": 14.9,
            "urine_acr_mg_g": 22,
        },
        "severity_scores": {
            "sirs_criteria_met": 0,
            "sirs_positive": False,
            "qsofa_score": 0,
            "news2_score": 0,
            "framingham_10yr_cvd_risk_percent": 18,
        },
        "differential_diagnosis": [
            {
                "rank": 1,
                "diagnosis": "TYPE 2 DIABETES MELLITUS — newly diagnosed",
                "icd10": "E11.9",
                "confidence": 0.92,
                "probability": 0.92,
                "likelihood_category": "VERY LIKELY",
                "key_features": [
                    "HbA1c 7.2% — meets ADA DM diagnosis threshold (≥6.5%)",
                    "Fasting glucose 132 mg/dL — meets DM threshold (≥126 fasting on 2 occasions)",
                    "No symptoms (osmotic) — asymptomatic type 2",
                    "Risk factors: age 58M, BMI 29.4, HTN, dyslipidaemia",
                ],
                "supporting_labs": ["HbA1c 7.2%", "Fasting glucose 132"],
                "recommended_action": "Confirm with repeat fasting glucose; initiate metformin; diabetes education",
            },
            {
                "rank": 2,
                "diagnosis": "HYPERTENSION — inadequately controlled",
                "icd10": "I10",
                "confidence": 0.88,
                "probability": 0.88,
                "likelihood_category": "CONFIRMED (pre-existing, now above goal)",
                "key_features": [
                    "BP 142/88 — above ACC/AHA 2017 target (<130/80 for DM)",
                    "Given new DM diagnosis, BP target tightens to <130/80",
                ],
                "recommended_action": "Uptitrate antihypertensive; add ACE inhibitor for DM + nephroprotection",
            },
            {
                "rank": 3,
                "diagnosis": "HYPERLIPIDAEMIA — undertreated",
                "icd10": "E78.5",
                "confidence": 0.85,
                "probability": 0.85,
                "likelihood_category": "CONFIRMED",
                "key_features": [
                    "LDL 148 mg/dL — above goal for DM patient (target <70 per ACC guidelines)",
                    "10-year CVD risk 18% — high-risk category",
                    "TG 188 elevated — metabolic syndrome feature",
                ],
                "recommended_action": "High-intensity statin; lifestyle counselling",
            },
        ],
        "outcome_28day": "Referred to diabetes education; metformin started; lisinopril added for nephroprotection",
        "sepsis_alert_triggered": False,
    },
    {
        "case_id": "DIAG-2025-005",
        "presentation": "Post-operative day 2 — fever and rising WBC",
        "demographics": {
            "age": 46, "sex": "F", "bmi": 29.6,
            "charlson_comorbidity_index": 1,
            "comorbidities": ["HTN", "Hypothyroidism"],
        },
        "vital_signs": {
            "heart_rate_bpm": 96,
            "systolic_bp_mmhg": 118,
            "diastolic_bp_mmhg": 72,
            "map_mmhg": 87,
            "respiratory_rate_per_min": 18,
            "temperature_celsius": 38.3,
            "spo2_percent": 97.0,
            "timestamp": "2025-05-07T08:00:00",
        },
        "laboratory_values": {
            "wbc_k_ul": 13.8,
            "hemoglobin_g_dl": 10.2,
            "platelets_k_ul": 312,
            "creatinine_mg_dl": 0.9,
            "alt_u_l": 48,
            "ast_u_l": 38,
            "bilirubin_total_mg_dl": 1.1,
            "lactate_mmol_l": 1.1,
            "procalcitonin_ng_ml": 1.2,
        },
        "clinical_context": {
            "surgery_performed": "Laparoscopic cholecystectomy",
            "surgery_date": "2025-05-05",
            "post_op_day": 2,
            "incisions": "4 port sites — no erythema, no discharge noted",
            "fever_onset": "POD2 AM",
        },
        "severity_scores": {
            "sirs_criteria_met": 2,
            "sirs_positive": True,
            "qsofa_score": 0,
            "news2_score": 2,
            "news2_risk_level": "LOW",
        },
        "differential_diagnosis": [
            {
                "rank": 1,
                "diagnosis": "POST-OPERATIVE FEVER — atelectasis (Wind)",
                "icd10": "J98.11",
                "confidence": 0.72,
                "probability": 0.72,
                "likelihood_category": "LIKELY",
                "key_features": [
                    "POD2 fever — peak incidence atelectasis-related fever",
                    "No wound erythema, no urinary symptoms, no respiratory distress",
                    "CXR: bibasilar atelectasis (expected post-laparoscopic surgery)",
                    "PCT 1.2 ng/mL — mild elevation (significant bacterial infection usually >2)",
                    "Haemodynamically stable (qSOFA 0)",
                ],
                "supporting_labs": ["PCT mildly elevated", "WBC 13.8 (mild)"],
                "recommended_action": "Incentive spirometry; ambulation; monitor; repeat cultures only if worsening",
            },
            {
                "rank": 2,
                "diagnosis": "SURGICAL SITE INFECTION",
                "icd10": "T81.41XA",
                "confidence": 0.28,
                "probability": 0.18,
                "likelihood_category": "POSSIBLE",
                "key_features": [
                    "Post-operative fever always raises wound infection concern",
                    "However: no wound erythema, warmth, drainage, or dehiscence noted",
                    "Onset POD2 — SSI typically manifests POD4-7",
                    "Laparoscopic approach has lower SSI risk than open",
                ],
                "recommended_action": "Inspect all port sites twice daily; culture any exudate; antibiotics if signs develop",
            },
            {
                "rank": 3,
                "diagnosis": "BILE LEAK / BILOMA",
                "icd10": "K91.5",
                "confidence": 0.15,
                "probability": 0.06,
                "likelihood_category": "LOW PROBABILITY",
                "key_features": [
                    "Cholecystectomy complication risk ~0.3-0.5%",
                    "Currently: LFTs normal (ALT 48, bilirubin 1.1)",
                    "No abdominal pain beyond incisional",
                    "No bile drainage from ports",
                ],
                "recommended_action": "Monitor LFTs; HIDA scan or CT abdomen if RUQ pain or LFT rise",
            },
        ],
        "outcome_48h": "Fever resolved by POD3 with incentive spirometry; WBC normalised; discharged POD3",
        "outcome_28day": "No complications. Surgical site intact at 7-day post-op visit",
        "sepsis_alert_triggered": False,
    },
]


# ── Public API ────────────────────────────────────────────────────────────────

def get_diagnostic_cases() -> list[Document]:
    """
    Returns the synthetic diagnostic ML feature corpus as Document objects.
    Each document contains a full case with vitals, labs, scores, and differentials.
    Tag: SYNTHETIC — realistic clinical feature vectors, no real patients.
    """
    docs = []
    for case in _CASES:
        text = (
            f"DIAGNOSTIC CASE: {case['case_id']}\n"
            f"Presentation: {case['presentation']}\n\n"
            f"Demographics: Age {case['demographics']['age']}, "
            f"Sex {case['demographics']['sex']}, BMI {case['demographics']['bmi']}\n"
            f"Comorbidities: {', '.join(case['demographics']['comorbidities'])}\n\n"
            f"VITAL SIGNS:\n"
            + "\n".join(
                f"  {k.replace('_', ' ').title()}: {v}"
                for k, v in case["vital_signs"].items()
                if k != "timestamp"
            )
            + f"\n\nLABORATORY VALUES:\n"
            + "\n".join(
                f"  {k.replace('_', ' ').title()}: {v}"
                for k, v in case["laboratory_values"].items()
            )
            + f"\n\nSEVERITY SCORES:\n"
            + "\n".join(
                f"  {k.replace('_', ' ').title()}: {v}"
                for k, v in case["severity_scores"].items()
            )
            + f"\n\nDIFFERENTIAL DIAGNOSIS:\n"
            + "\n".join(
                f"  [{dx['rank']}] {dx['diagnosis']} — Confidence: {dx['confidence']:.0%}\n"
                f"      {'; '.join((dx.get('key_features') or dx.get('distinguishing_features') or dx.get('missing_features') or [])[:3])}"
                for dx in case["differential_diagnosis"]
            )
        )
        docs.append(
            Document(
                id=case["case_id"],
                text=text,
                metadata={
                    "case_id": case["case_id"],
                    "presentation": case["presentation"],
                    "primary_diagnosis": case["differential_diagnosis"][0]["icd10"],
                    "sepsis_alert_triggered": case.get("sepsis_alert_triggered", False),
                    "qsofa_score": case["severity_scores"].get("qsofa_score"),
                    "sofa_score": case["severity_scores"].get("sofa_score"),
                    "raw": json.dumps(case),
                    "source_type": "diagnostic_case",
                },
                tag=DataTag.SYNTHETIC,
            )
        )
    return docs
