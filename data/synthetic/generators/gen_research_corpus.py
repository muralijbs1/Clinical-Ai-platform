#!/usr/bin/env python3
"""
Generator: writes synthetic clinical research abstracts as a MEDLINE XML file.

Run once to produce the data file. Re-run to regenerate or add more abstracts.
Output: data/synthetic/research_corpus.xml

Structure exactly matches real PubMed efetch MEDLINE XML output so the same
parser that reads live PubMed data also reads this file. Custom <OtherID>
elements carry evidence_level and evidence_grade (non-standard MEDLINE extension).

DATA TAG: SYNTHETIC — realistic structure, no real publications.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

_OUT_FILE = Path(__file__).parent.parent / "research_corpus.xml"

_ABSTRACTS = [
    {
        "pmid": "38421001",
        "title": "Dapagliflozin in Heart Failure with Reduced Ejection Fraction: Outcomes from the DAPA-HF Extension Trial",
        "authors": ["Greene SJ", "McMurray JJV", "Solomon SD", "Kosiborod MN"],
        "journal": "New England Journal of Medicine",
        "journal_abbr": "N Engl J Med",
        "year": 2024, "volume": "390", "issue": "4", "pages": "312-323",
        "doi": "10.1056/NEJMoa2317445",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Heart Failure/drug therapy", "Heart Failure/physiopathology",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "Stroke Volume/physiology", "Treatment Outcome", "Humans",
            "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: SGLT2 inhibitors reduce mortality and hospitalisation in patients with heart "
            "failure with reduced ejection fraction (HFrEF). Long-term data beyond 18 months remain "
            "limited. Methods: We conducted a double-blind, randomised, placebo-controlled extension of "
            "the DAPA-HF trial enrolling 4,744 patients with HFrEF (LVEF ≤40%) and NYHA class II-IV "
            "symptoms. The primary composite endpoint was worsening heart failure or cardiovascular death. "
            "Results: Over a median follow-up of 36 months, the primary composite endpoint occurred in "
            "26.3% of the dapagliflozin group versus 34.1% of the placebo group (HR 0.74, 95% CI "
            "0.65-0.85, P<0.001). All-cause mortality was 19.8% vs 24.6% (HR 0.80, 95% CI 0.68-0.93). "
            "Benefits were consistent regardless of diabetes status (P-interaction 0.89). "
            "Conclusions: Dapagliflozin provides sustained reduction in cardiovascular death and worsening "
            "heart failure over 36 months in HFrEF patients independent of diabetes status. These findings "
            "(Level I, Grade A evidence) support universal incorporation of SGLT2 inhibitors into "
            "guideline-directed medical therapy for HFrEF."
        ),
    },
    {
        "pmid": "37892044",
        "title": "Early Restrictive versus Liberal Fluid Resuscitation in Septic Shock: A Multicentre Randomised Trial",
        "authors": ["Hjortrup PB", "Møller MH", "Vestergaard SR", "Perner A"],
        "journal": "Intensive Care Medicine",
        "journal_abbr": "Intensive Care Med",
        "year": 2023, "volume": "49", "issue": "11", "pages": "1298-1309",
        "doi": "10.1007/s00134-023-07214-3",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Septic Shock/therapy", "*Fluid Therapy/methods",
            "Resuscitation/methods", "Hemodynamics", "Critical Care",
            "Humans", "Adult", "Intensive Care Units",
        ],
        "abstract": (
            "Background: Optimal fluid volume during resuscitation of septic shock remains debated. "
            "Excessive fluid may worsen outcomes through oedema and organ failure. "
            "Methods: In this multicentre, open-label randomised trial, we enrolled 1,554 adult patients "
            "with septic shock randomised 1:1 to restrictive fluid strategy or liberal strategy. "
            "Results: The restrictive group received a median 2.4 L versus 4.1 L in the liberal group "
            "in the first 72 hours (P<0.001). Ninety-day mortality was 36.8% restrictive vs 37.9% liberal "
            "(OR 0.95, 95% CI 0.78-1.16, P=0.62). Serious adverse events occurred in 23.6% vs 28.4% "
            "(OR 0.78, P=0.02), driven by fewer acute kidney injury episodes in the restrictive group. "
            "Conclusions: Restrictive fluid resuscitation does not reduce 90-day mortality in septic shock "
            "but is associated with fewer serious adverse events (Level II, Grade A). A targeted, "
            "reassessment-based fluid approach is supported over protocolised liberal resuscitation."
        ),
    },
    {
        "pmid": "38104782",
        "title": "Procalcitonin-Guided Antibiotic Stewardship in Sepsis: Systematic Review and Meta-Analysis of 32 Randomised Trials",
        "authors": ["Schuetz P", "Wirz Y", "Sager R", "Müller B"],
        "journal": "Lancet Infectious Diseases",
        "journal_abbr": "Lancet Infect Dis",
        "year": 2024, "volume": "24", "issue": "3", "pages": "289-301",
        "doi": "10.1016/S1473-3099(23)00512-8",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Procalcitonin/blood", "*Anti-Bacterial Agents/therapeutic use",
            "*Sepsis/drug therapy", "Biomarkers/blood", "Antibiotic Stewardship",
            "Systematic Review", "Meta-Analysis", "Humans",
        ],
        "abstract": (
            "Background: Procalcitonin (PCT) is used to guide antibiotic initiation and discontinuation "
            "in sepsis, but its net clinical benefit remains uncertain. "
            "Methods: We systematically searched MEDLINE, Cochrane, and EMBASE for randomised trials "
            "comparing PCT-guided antibiotic decisions to standard care. Thirty-two trials (n=8,473) met "
            "inclusion criteria. "
            "Results: PCT-guided care reduced antibiotic duration by 1.9 days (95% CI 1.4-2.4, P<0.001) "
            "without increasing 28-day mortality (RR 0.91, 95% CI 0.84-0.99, P=0.03 favouring PCT). "
            "PCT cut-off of ≤0.5 ng/mL for discontinuation had highest sensitivity-specificity balance. "
            "Conclusions: PCT-guided antibiotic stewardship safely reduces antibiotic exposure and may "
            "reduce mortality in sepsis. This meta-analysis (Level I, Grade A) supports integration of "
            "PCT thresholds into sepsis antibiotic management protocols at cut-off ≤0.5 ng/mL."
        ),
    },
    {
        "pmid": "38231567",
        "title": "High-Sensitivity Troponin T in the Rapid Evaluation of Non-ST-Elevation Acute Coronary Syndrome: The RAPID-NSTEMI Validation Study",
        "authors": ["Shah ASV", "Sandoval Y", "Nofer JR", "Mills NL"],
        "journal": "Journal of the American College of Cardiology",
        "journal_abbr": "J Am Coll Cardiol",
        "year": 2024, "volume": "83", "issue": "7", "pages": "701-713",
        "doi": "10.1016/j.jacc.2023.11.042",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Troponin T/blood", "*Non-ST Elevated Myocardial Infarction/diagnosis",
            "Acute Coronary Syndrome/diagnosis", "Biomarkers/blood",
            "Sensitivity and Specificity", "Humans", "Emergency Service, Hospital",
        ],
        "abstract": (
            "Background: Rapid rule-out of NSTEMI using high-sensitivity cardiac troponin (hs-cTnT) "
            "reduces unnecessary admissions. Optimal 0/1-hour versus 0/2-hour strategies require "
            "prospective validation across diverse ED populations. "
            "Methods: We prospectively enrolled 3,612 consecutive patients with chest pain and no "
            "ST-elevation. Hs-cTnT was measured at 0 and 1 hour. The ESC 0/1-hour algorithm was applied. "
            "Results: NSTEMI was diagnosed in 17.3%. The 0/1-hour algorithm classified 41.2% as rule-out "
            "(sensitivity 99.4%, NPV 99.9%), 22.6% as rule-in (PPV 74.8%). Among rule-out patients, "
            "30-day MACE occurred in 0.6% (95% CI 0.1-1.4%). "
            "Conclusions: The ESC 0/1-hour hs-cTnT algorithm demonstrates excellent safety for NSTEMI "
            "rule-out in routine ED practice (Level II, Grade B)."
        ),
    },
    {
        "pmid": "37654321",
        "title": "Empagliflozin in Heart Failure with Preserved Ejection Fraction: Subgroup Analysis of the EMPEROR-Preserved Trial by Ejection Fraction Quartile",
        "authors": ["Anker SD", "Butler J", "Filippatos G", "Zannad F"],
        "journal": "European Heart Journal",
        "journal_abbr": "Eur Heart J",
        "year": 2023, "volume": "44", "issue": "22", "pages": "2058-2071",
        "doi": "10.1093/eurheartj/ehad178",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Heart Failure/drug therapy",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "Stroke Volume", "Ventricular Function, Left",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: EMPEROR-Preserved demonstrated empagliflozin reduces heart failure "
            "hospitalisation in HFpEF (LVEF ≥40%). Whether benefit varies by ejection fraction subgroup "
            "remains unclear. "
            "Methods: Pre-specified subgroup analysis of n=5,988 patients divided by LVEF quartile. "
            "Results: Empagliflozin reduced the primary endpoint across all EF quartiles (HR range 0.73-0.82). "
            "Absolute risk reduction was greatest in Q1 (HFmrEF): 5.4% vs 2.1% in Q4. "
            "Conclusions: Empagliflozin benefits are present across the full spectrum of preserved and "
            "mildly reduced EF, with greatest absolute benefit in HFmrEF (Level I, Grade A). LVEF should "
            "not be used to exclude patients from SGLT2 inhibitor therapy in the EF ≥40% population."
        ),
    },
    {
        "pmid": "38561234",
        "title": "Intensive Blood Pressure Reduction in Patients with Type 2 Diabetes and Stage 3 Chronic Kidney Disease: A Multicentre RCT",
        "authors": ["Whelton PK", "Carey RM", "Aronow WS", "Wright JT Jr"],
        "journal": "Hypertension",
        "journal_abbr": "Hypertension",
        "year": 2024, "volume": "81", "issue": "5", "pages": "1042-1055",
        "doi": "10.1161/HYPERTENSIONAHA.123.22981",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Hypertension/drug therapy", "*Diabetes Mellitus, Type 2/complications",
            "*Renal Insufficiency, Chronic/drug therapy", "Blood Pressure/physiology",
            "Antihypertensive Agents/therapeutic use", "Humans", "Adult",
        ],
        "abstract": (
            "Background: Optimal BP targets in patients with coexisting T2DM and CKD stage 3 are undefined. "
            "Methods: We randomised 2,184 adults with T2DM, CKD3, and SBP 130-179 mmHg to intensive "
            "(target SBP <120 mmHg) versus standard (target SBP <140 mmHg) treatment. Mean follow-up 4.1 years. "
            "Results: The intensive group achieved mean SBP 118.3 vs 133.7 mmHg. Primary endpoint occurred "
            "in 14.2% intensive vs 19.8% standard (HR 0.69, 95% CI 0.58-0.83, P<0.001). "
            "Conclusions: Intensive BP control targeting SBP <120 mmHg significantly reduces kidney and "
            "cardiovascular events in T2DM-CKD3 patients (Level II, Grade A) at cost of modest increase "
            "in hypotension."
        ),
    },
    {
        "pmid": "37123456",
        "title": "GLP-1 Receptor Agonists for Weight Loss and Glycaemic Control in Obese Adults with Type 2 Diabetes: A Network Meta-Analysis",
        "authors": ["Davies MJ", "Aroda VR", "Collins BS", "Buse JB"],
        "journal": "Diabetes Care",
        "journal_abbr": "Diabetes Care",
        "year": 2023, "volume": "46", "issue": "9", "pages": "1721-1734",
        "doi": "10.2337/dc23-0442",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Glucagon-Like Peptide-1 Receptor/agonists",
            "*Diabetes Mellitus, Type 2/drug therapy", "*Obesity/drug therapy",
            "Hypoglycemic Agents/therapeutic use", "Glycated Hemoglobin/analysis",
            "Network Meta-Analysis", "Humans",
        ],
        "abstract": (
            "Background: Multiple GLP-1 receptor agonists (GLP-1 RAs) are now approved for T2DM and "
            "obesity but direct head-to-head comparisons are scarce. "
            "Methods: Network meta-analysis of 61 trials (n=52,413 patients) comparing GLP-1 RAs. "
            "Results: Semaglutide 2.4 mg weekly produced greatest HbA1c reduction (-1.8%, 95% CrI -2.1 "
            "to -1.5) and weight loss (-12.4 kg). All GLP-1 RAs significantly reduced weight vs placebo. "
            "MACE reduction confirmed for semaglutide and liraglutide. "
            "Conclusions: Semaglutide 2.4 mg provides superior glycaemic and weight outcomes among GLP-1 "
            "RAs in obese T2DM patients (Level I, Grade A). Agent selection should balance efficacy, cost, "
            "dosing frequency, and individual cardiovascular risk profile."
        ),
    },
    {
        "pmid": "38441289",
        "title": "Vasopressor Initiation Timing in Septic Shock: Early vs Delayed Norepinephrine and Effects on 28-Day Mortality",
        "authors": ["Lamontagne F", "Meade MO", "Hébert PC", "Asfar P"],
        "journal": "Critical Care Medicine",
        "journal_abbr": "Crit Care Med",
        "year": 2024, "volume": "52", "issue": "6", "pages": "878-890",
        "doi": "10.1097/CCM.0000000000006231",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Shock, Septic/therapy", "*Norepinephrine/administration & dosage",
            "*Vasoconstrictor Agents/therapeutic use",
            "Time-to-Treatment", "Intensive Care Units", "Humans",
        ],
        "abstract": (
            "Background: Current sepsis guidelines recommend vasopressors when MAP remains <65 mmHg "
            "despite fluid resuscitation, but optimal timing relative to fluid resuscitation is unknown. "
            "Methods: This parallel-group RCT enrolled 820 adults presenting to 12 ICUs with septic shock. "
            "Early arm initiated norepinephrine within 1 hour. Delayed arm used fluid resuscitation alone "
            "for up to 3 hours. "
            "Results: 28-day mortality was 34.1% early vs 40.2% delayed (RR 0.85, 95% CI 0.72-0.99, P=0.04). "
            "Early norepinephrine reduced total fluid volume at 6h by 1.1 L (P<0.001). "
            "Conclusions: Early norepinephrine initiation within 1 hour of septic shock recognition reduces "
            "28-day mortality and fluid requirements (Level II, Grade A). This supports earlier vasopressor "
            "use in haemodynamically unstable septic shock."
        ),
    },
    {
        "pmid": "37789012",
        "title": "Canagliflozin and Renal Outcomes in Diabetic Nephropathy: Five-Year Follow-Up of the CREDENCE Trial Cohort",
        "authors": ["Perkovic V", "Jardine MJ", "Neal B", "Mahaffey KW"],
        "journal": "Journal of the American Society of Nephrology",
        "journal_abbr": "J Am Soc Nephrol",
        "year": 2023, "volume": "34", "issue": "8", "pages": "1398-1411",
        "doi": "10.1681/ASN.0000000000000171",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Diabetic Nephropathies/drug therapy",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "*Canagliflozin/therapeutic use",
            "Renal Insufficiency, Chronic/prevention & control",
            "Glomerular Filtration Rate/drug effects", "Humans",
        ],
        "abstract": (
            "Background: The CREDENCE trial demonstrated canagliflozin reduces end-stage kidney disease "
            "in diabetic nephropathy. Extended follow-up examines durability of renoprotective effects. "
            "Methods: Extended follow-up of 4,401 CREDENCE participants for 5 years. "
            "Results: The primary renal composite was 24.2% canagliflozin vs 31.4% placebo "
            "(HR 0.72, 95% CI 0.62-0.83). eGFR slope in years 1-5: -0.8 vs -2.1 mL/min/1.73m² per year "
            "(P<0.001). Post-treatment eGFR trajectories remained diverged for 24 months after discontinuation. "
            "Conclusions: Canagliflozin provides durable renoprotection over 5 years in diabetic nephropathy "
            "with persistent benefit for 24 months after treatment discontinuation (Level I, Grade A)."
        ),
    },
    {
        "pmid": "38198740",
        "title": "Laparoscopic Cholecystectomy Complications and Risk Stratification: A Prospective Cohort Study of 18,420 Procedures",
        "authors": ["Strasberg SM", "Pucci MJ", "Brunt LM", "Deziel DJ"],
        "journal": "Annals of Surgery",
        "journal_abbr": "Ann Surg",
        "year": 2024, "volume": "279", "issue": "3", "pages": "442-451",
        "doi": "10.1097/SLA.0000000000006089",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Cholecystectomy, Laparoscopic/adverse effects",
            "*Bile Duct Injuries/etiology", "Intraoperative Complications",
            "Risk Factors", "Retrospective Studies", "Humans", "Postoperative Complications",
        ],
        "abstract": (
            "Background: Bile duct injury (BDI) remains the most serious complication of laparoscopic "
            "cholecystectomy (LC). Real-world incidence and risk factors from large prospective series are needed. "
            "Methods: Prospective single-registry cohort study of 18,420 consecutive LC procedures across "
            "34 hospitals (2019-2023). "
            "Results: BDI occurred in 0.38% of cases. Independent risk factors: acute cholecystitis within "
            "72h (OR 3.2), obesity BMI >40 (OR 2.1), inexperienced surgeon <50 cases (OR 4.7). "
            "Intraoperative cholangiography reduced BDI by 62%. Critical view of safety (CVS) documented "
            "in 71% of cases; CVS documentation associated with 79% lower BDI rate. "
            "Conclusions: BDI rate of 0.38% confirms LC safety at experienced centres (Level II, Grade B). "
            "Systematic CVS documentation and liberal IOC use are the most effective preventive strategies."
        ),
    },
    {
        "pmid": "37456789",
        "title": "Atrial Fibrillation Detection Using Wearable Single-Lead ECG: Validation Against 24-Hour Holter Monitoring in 5,000 Patients",
        "authors": ["Hindricks G", "Potpara T", "Dagres N", "Arbelo E"],
        "journal": "European Heart Journal - Digital Health",
        "journal_abbr": "Eur Heart J Digit Health",
        "year": 2023, "volume": "4", "issue": "4", "pages": "298-308",
        "doi": "10.1093/ehjdh/ztad041",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Atrial Fibrillation/diagnosis", "*Wearable Electronic Devices",
            "*Electrocardiography, Ambulatory/methods",
            "Sensitivity and Specificity", "Humans", "Diagnosis, Computer-Assisted",
        ],
        "abstract": (
            "Background: Wearable single-lead ECG devices may enable opportunistic AF detection in "
            "community settings, but diagnostic accuracy versus standard Holter monitoring requires validation. "
            "Methods: Prospective cross-sectional study in 5,000 patients wearing both devices simultaneously. "
            "Results: AF confirmed in 18.3% by Holter. Wearable device sensitivity 93.4% (95% CI 91.6-95.0%), "
            "specificity 91.8%, PPV 82.3%, NPV 97.3%. Paroxysmal AF <30 minutes had lower sensitivity (76.2%). "
            "Conclusions: Single-lead wearable ECG demonstrates high sensitivity and specificity for AF "
            "detection versus 24-hour Holter (Level II, Grade B). NPV supports use as a rule-out tool."
        ),
    },
    {
        "pmid": "38342156",
        "title": "Sepsis-3 Criteria versus SIRS in Predicting 30-Day Mortality: Retrospective Analysis of 98,000 Hospital Admissions",
        "authors": ["Seymour CW", "Liu VX", "Iwashyna TJ", "Shankar-Hari M"],
        "journal": "Critical Care",
        "journal_abbr": "Crit Care",
        "year": 2024, "volume": "28", "issue": "1", "pages": "89",
        "doi": "10.1186/s13054-024-04872-z",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Sepsis/diagnosis", "*Systemic Inflammatory Response Syndrome/diagnosis",
            "Hospital Mortality", "Organ Dysfunction Scores",
            "Retrospective Studies", "Humans", "Intensive Care Units",
        ],
        "abstract": (
            "Background: The Sepsis-3 definitions replaced SIRS-based criteria with organ dysfunction "
            "(SOFA ≥2) as the diagnostic cornerstone. Whether this improves mortality prediction remains debated. "
            "Methods: Retrospective analysis of 98,241 hospital admissions at 12 US academic medical centres. "
            "Results: Sepsis-3 C-statistic for 30-day mortality: 0.74 vs SIRS C-statistic 0.64 "
            "(difference 0.10, P<0.001). qSOFA ≥2 had C-statistic 0.71 with high specificity (98.9%) "
            "but low sensitivity (28.5%). "
            "Conclusions: Sepsis-3 criteria significantly outperform SIRS in predicting 30-day mortality "
            "(Level III, Grade B). qSOFA is highly specific but misses sepsis cases; SOFA-based criteria "
            "should remain primary in ICU settings."
        ),
    },
    {
        "pmid": "37654987",
        "title": "Robotic-Assisted versus Laparoscopic Cholecystectomy: Operative Outcomes from a Propensity-Matched National Database Study",
        "authors": ["Azagury D", "Liu RC", "Morgan A", "Curet MJ"],
        "journal": "JAMA Surgery",
        "journal_abbr": "JAMA Surg",
        "year": 2023, "volume": "158", "issue": "10", "pages": "1089-1097",
        "doi": "10.1001/jamasurg.2023.3442",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Cholecystectomy, Laparoscopic/methods", "*Robotic Surgical Procedures/methods",
            "Postoperative Complications", "Operative Time",
            "Treatment Outcome", "Propensity Score", "Humans",
        ],
        "abstract": (
            "Background: Robotic-assisted cholecystectomy adoption is increasing despite limited comparative "
            "safety data versus standard laparoscopic approach. "
            "Methods: 14,228 robotic-assisted were propensity-matched to 14,228 laparoscopic cases from "
            "the ACS NSQIP database (2019-2022). "
            "Results: Major complication rate: robotic 3.1% vs laparoscopic 3.4% (OR 0.91, P=0.26). "
            "Operative time was longer for robotic (68 vs 51 min). Bile duct injury: 0.24% vs 0.31% (P=0.31). "
            "Hospital cost was 34% higher for robotic. "
            "Conclusions: Robotic-assisted cholecystectomy provides equivalent safety to laparoscopic approach "
            "but with longer operative times and substantially higher cost (Level III, Grade B)."
        ),
    },
    {
        "pmid": "38123409",
        "title": "Clinical Decision Support for Sepsis Recognition: Alert Fatigue and Override Rates in a Tertiary Care System",
        "authors": ["Rhee C", "Dantes R", "Epstein L", "Murphy DJ"],
        "journal": "Journal of Hospital Medicine",
        "journal_abbr": "J Hosp Med",
        "year": 2024, "volume": "19", "issue": "3", "pages": "211-219",
        "doi": "10.1002/jhm.13292",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level III", "evidence_grade": "Grade C",
        "mesh_terms": [
            "*Sepsis/diagnosis", "*Decision Support Systems, Clinical",
            "Alert Fatigue, Health Personnel", "Electronic Health Records",
            "Humans", "Hospital Information Systems",
        ],
        "abstract": (
            "Background: Sepsis alert systems improve recognition but generate high rates of false-positive "
            "alerts leading to alert fatigue and reduced adherence. "
            "Methods: Retrospective analysis of 48,291 sepsis alerts at a 500-bed tertiary hospital over "
            "24 months. "
            "Results: Alert positive predictive value was 31.2%. Clinician override rate was 54.2%; 82.4% "
            "of overrides were appropriate (true false positives). Machine learning re-calibration reduced "
            "false-positive alerts by 41% without increasing missed sepsis cases. "
            "Conclusions: Current sepsis alert systems suffer from high false-positive rates driving alert "
            "fatigue (Level III, Grade C). Machine learning optimisation reduces false positives substantially. "
            "Human-in-the-loop review workflows must account for clinician override patterns."
        ),
    },
    {
        "pmid": "37891234",
        "title": "Metformin versus SGLT2 Inhibitor as First-Line Therapy in Newly Diagnosed Type 2 Diabetes with High Cardiovascular Risk",
        "authors": ["Kosiborod MN", "Lam CSP", "Kohsaka S", "Kim DJ"],
        "journal": "Journal of Clinical Endocrinology & Metabolism",
        "journal_abbr": "J Clin Endocrinol Metab",
        "year": 2023, "volume": "108", "issue": "7", "pages": "1802-1814",
        "doi": "10.1210/clinem/dgad142",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Metformin/therapeutic use",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "*Diabetes Mellitus, Type 2/drug therapy",
            "Cardiovascular Diseases/prevention & control",
            "Hypoglycemic Agents/therapeutic use", "Humans",
        ],
        "abstract": (
            "Background: Current T2DM guidelines recommend metformin as first-line therapy, but SGLT2 "
            "inhibitors have demonstrated superior cardiovascular and renal outcomes. "
            "Methods: Propensity-matched cohort study (n=24,816) of newly diagnosed T2DM patients with "
            "established cardiovascular disease initiating metformin or empagliflozin as monotherapy. "
            "Results: MACE occurred in 6.8% empagliflozin vs 9.2% metformin (HR 0.73, 95% CI 0.62-0.87, "
            "P<0.001). Heart failure hospitalisation: 2.1% vs 3.8% (HR 0.54). "
            "Conclusions: Empagliflozin as initial monotherapy provides superior cardiovascular and renal "
            "outcomes versus metformin in high-risk T2DM (Level II, Grade B). These data support "
            "re-evaluation of metformin as default first-line in high cardiovascular risk patients."
        ),
    },
    # ── Abstracts 16-60 ──────────────────────────────────────────────────────
    {
        "pmid": "39201847", "title": "Apixaban versus Enoxaparin for VTE Treatment in Cancer Patients: CARAVAGGIO Trial 3-Year Follow-Up",
        "authors": ["Agnelli G", "Becattini C", "Meyer G", "Munoz A", "Nishida T"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "391", "issue": "8", "pages": "712-724",
        "doi": "10.1056/NEJMoa2024847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Apixaban/therapeutic use", "*Enoxaparin/therapeutic use",
                       "*Venous Thromboembolism/drug therapy", "Neoplasms/complications",
                       "*Factor Xa Inhibitors/therapeutic use", "Humans"],
        "abstract": (
            "Background: VTE in cancer patients requires extended anticoagulation; the optimal agent remains debated. "
            "Methods: 1,170 cancer patients with acute VTE randomised to apixaban 10mg BID x7d then 5mg BID, or "
            "dalteparin for 6 months. Extended follow-up to 36 months. "
            "Results: Recurrent VTE: apixaban 9.1% vs dalteparin 10.3% (HR 0.87, P=0.02). Major bleeding: "
            "apixaban 3.7% vs dalteparin 4.0% (HR 0.93, P=0.82). GI cancer subgroup: no excess GI bleeding. "
            "Conclusions: Apixaban is effective for cancer-associated VTE with no excess bleeding signal, "
            "including GI cancers. Oral anticoagulation preferred over LMWH for most cancer-associated VTE."
        ),
    },
    {
        "pmid": "39312847", "title": "Pulmonary Embolism Response Team (PERT) Outcomes: National Registry Analysis",
        "authors": ["Kabrhel C", "Rosovsky R", "Channick R", "Jaff MR", "Weinberg I"],
        "journal": "JACC: Cardiovascular Interventions", "journal_abbr": "JACC Cardiovasc Interv",
        "year": "2024", "volume": "17", "issue": "3", "pages": "328-340",
        "doi": "10.1016/j.jcin.2024.01.022", "publication_type": "REGISTRY STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Pulmonary Embolism/therapy", "*Patient Care Team", "Thrombolytic Therapy",
                       "Registries", "*Embolectomy/methods", "Humans"],
        "abstract": (
            "Background: PERT programs coordinate multidisciplinary management of high-risk PE but outcome data "
            "are limited. Methods: National PERT Consortium Registry, 3,822 PE patients across 30 centres (2019-2023). "
            "Results: PERT activation: 42% massive, 58% submassive. Systemic thrombolysis rate 18% (massive), "
            "catheter-directed treatment 28% (submassive). In-hospital mortality: massive 24%, submassive 3.1%. "
            "PERT consultation associated with lower mortality in submassive PE (OR 0.64, 95% CI 0.48-0.85). "
            "Conclusions: PERT-based management of submassive PE is associated with improved outcomes. "
            "Systemic thrombolysis should be reserved for haemodynamically unstable patients."
        ),
    },
    {
        "pmid": "39428371", "title": "Corticosteroids in COPD Exacerbations: REDUCE-COPD Trial 5-Day versus 14-Day",
        "authors": ["Leuppi JD", "Schuetz P", "Bingisser R", "Bodmer M", "Briel M"],
        "journal": "JAMA Internal Medicine", "journal_abbr": "JAMA Intern Med",
        "year": "2024", "volume": "184", "issue": "2", "pages": "189-198",
        "doi": "10.1001/jamainternmed.2024.0128", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Pulmonary Disease, Chronic Obstructive/drug therapy",
                       "*Glucocorticoids/therapeutic use", "*Prednisone/therapeutic use",
                       "Disease Exacerbation", "Hospitalization", "Humans"],
        "abstract": (
            "Background: COPD exacerbations require systemic corticosteroids; optimal duration is uncertain. "
            "Methods: RCT comparing prednisone 40mg/day x5 days versus x14 days in 314 COPD patients "
            "admitted for exacerbation. Primary endpoint: time to next exacerbation within 180 days. "
            "Results: No significant difference in time to re-exacerbation: 5-day 57 days vs 14-day 54 days "
            "(HR 0.92, 95% CI 0.72-1.18). Adverse events: hyperglycaemia significantly less in 5-day group "
            "(18% vs 41%, P<0.001). Hospital stay similar. "
            "Conclusions: 5-day corticosteroid course is non-inferior to 14-day for COPD exacerbations with "
            "significantly fewer steroid-related adverse effects (Level I, Grade A)."
        ),
    },
    {
        "pmid": "39517284", "title": "NIV versus HFNC for Hypercapnic COPD Exacerbations: RECOVER Trial",
        "authors": ["Plant PK", "Owen JL", "Elliot MW", "Thomas J", "Millar A"],
        "journal": "Chest", "journal_abbr": "Chest",
        "year": "2024", "volume": "165", "issue": "4", "pages": "892-902",
        "doi": "10.1016/j.chest.2024.02.017", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Noninvasive Ventilation", "*High-Flow Nasal Cannula", "*COPD/therapy",
                       "*Respiratory Failure/therapy", "Intubation, Intratracheal", "Humans"],
        "abstract": (
            "Background: HFNC is increasingly used for hypercapnic respiratory failure but evidence in COPD is limited. "
            "Methods: 428 COPD patients with acute hypercapnic RF (pH 7.25-7.35) randomised to NIV (BiPAP) vs HFNC. "
            "Results: Treatment failure (intubation or pH deterioration): NIV 14% vs HFNC 26% (P=0.003). "
            "pH normalisation at 2h: NIV 72% vs HFNC 48% (P<0.001). Hospital stay similar (6.2 vs 6.5 days). "
            "Mortality: NIV 8% vs HFNC 11% (P=0.18). "
            "Conclusions: NIV remains superior to HFNC for hypercapnic COPD exacerbations. HFNC may be considered "
            "for milder hypercapnia (pH >7.32) or NIV intolerance."
        ),
    },
    {
        "pmid": "39623847", "title": "Tenecteplase versus Alteplase for Acute Ischaemic Stroke: AcT Trial Extended Analysis",
        "authors": ["Menon BK", "Buck BH", "Singh N", "Deschaintre Y", "Almekhlafi M"],
        "journal": "Lancet Neurology", "journal_abbr": "Lancet Neurol",
        "year": "2024", "volume": "23", "issue": "6", "pages": "581-592",
        "doi": "10.1016/S1474-4422(24)00128-4", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Tenecteplase/therapeutic use", "*Tissue Plasminogen Activator/therapeutic use",
                       "*Ischemic Stroke/drug therapy", "Thrombolytic Therapy", "*Fibrinolytic Agents", "Humans"],
        "abstract": (
            "Background: Tenecteplase offers a simplified single-bolus administration vs alteplase for stroke thrombolysis. "
            "Methods: 1,600 patients eligible for IV thrombolysis randomised to tenecteplase 0.25mg/kg vs alteplase 0.9mg/kg. "
            "Results: mRS 0-1 at 90 days: tenecteplase 36.9% vs alteplase 34.8% (OR 1.09, 95% CI 0.86-1.38). "
            "Symptomatic ICH: 3.4% vs 3.2%. Door-to-needle time 3 min shorter with tenecteplase. "
            "Recanalization pre-EVT: tenecteplase 22% vs alteplase 10% (P=0.003) in LVO subgroup. "
            "Conclusions: Tenecteplase non-inferior to alteplase with similar safety; single-bolus administration "
            "enables faster workflow and better recanalization before thrombectomy (Level I, Grade A)."
        ),
    },
    {
        "pmid": "39718472", "title": "Time Window for Mechanical Thrombectomy: DAWN-Extended Trial",
        "authors": ["Nogueira RG", "Jadhav AP", "Haussen DC", "Bonafe A", "Budzik RF"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "391", "issue": "14", "pages": "1289-1301",
        "doi": "10.1056/NEJMoa2401728", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Thrombectomy", "*Stroke/surgery", "Brain Ischemia/surgery",
                       "Endovascular Procedures", "Time-to-Treatment", "Humans"],
        "abstract": (
            "Background: DAWN and DEFUSE-3 established thrombectomy utility to 24h in selected patients. "
            "Methods: DAWN-Extended enrolled 520 patients with LVO stroke 24-36h from last known well, "
            "perfusion mismatch on CT (core <70mL, mismatch ratio >1.8). "
            "Results: mRS 0-2 at 90 days: thrombectomy 44% vs medical 17% (aOR 4.2, 95% CI 2.8-6.4). "
            "Symptomatic ICH: 6% vs 3% (P=0.11). Mortality: 18% vs 22% (P=0.32). "
            "Conclusions: Mechanical thrombectomy up to 36h from last known well provides significant benefit "
            "in patients with favourable imaging profiles (large penumbra, small core), supporting extended "
            "time window thrombectomy protocols."
        ),
    },
    {
        "pmid": "39827483", "title": "CRRT versus IHD in Septic AKI: STARRT-AKI Trial Outcomes",
        "authors": ["Bagshaw SM", "Wald R", "Adhikari NK", "Bellomo R", "da Costa BR"],
        "journal": "JAMA", "journal_abbr": "JAMA",
        "year": "2024", "volume": "331", "issue": "12", "pages": "1024-1034",
        "doi": "10.1001/jama.2024.1847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Renal Replacement Therapy", "*Acute Kidney Injury/therapy",
                       "*Sepsis/complications", "Critical Care", "Kidney/physiopathology", "Humans"],
        "abstract": (
            "Background: Timing and modality of renal replacement therapy in septic AKI influence outcomes. "
            "Methods: 3,019 critically ill patients with severe AKI randomised to accelerated versus standard "
            "RRT initiation (STARRT-AKI). Extended analysis at 90 days comparing CRRT versus IHD subgroups. "
            "Results: 90-day mortality did not differ significantly by modality: CRRT 44.2% vs IHD 43.8% "
            "(aOR 1.01, 95% CI 0.88-1.16). CRRT showed better haemodynamic stability (MAP>65 maintained in "
            "92% vs 78%, P<0.001). Renal recovery: CRRT 52% vs IHD 48% (P=0.22). "
            "Conclusions: No mortality benefit of CRRT over IHD in septic AKI, but CRRT offers haemodynamic "
            "advantages in unstable patients. Modality should be guided by haemodynamic status."
        ),
    },
    {
        "pmid": "39934821", "title": "Bundled Care for Community-Acquired Pneumonia: SMART-CAP Trial",
        "authors": ["Mandell LA", "Wunderink R", "Anzueto A", "Torres A", "Waterer GW"],
        "journal": "Clinical Infectious Diseases", "journal_abbr": "Clin Infect Dis",
        "year": "2024", "volume": "78", "issue": "5", "pages": "612-622",
        "doi": "10.1093/cid/ciad847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Pneumonia/therapy", "*Community-Acquired Infections/drug therapy",
                       "*Anti-Bacterial Agents/therapeutic use", "Hospitalization",
                       "Severity of Illness Index", "Humans"],
        "abstract": (
            "Background: CAP management varies; bundled care protocols may improve outcomes. "
            "Methods: Cluster-randomised trial, 28 hospitals, 4,218 CAP patients. Intervention: standardised "
            "severity scoring (PSI/CURB-65), automated antibiotic selection, 3-day ABST-guided switch, "
            "early discharge protocol. "
            "Results: 30-day mortality: intervention 8.2% vs control 11.1% (OR 0.72, P=0.003). "
            "Length of stay: 4.2 vs 5.8 days (P<0.001). IDSA-guideline adherence: 94% vs 68%. "
            "Antibiotic duration: 5.2 vs 8.4 days (P<0.001). "
            "Conclusions: Bundled CAP care reduces mortality, LOS, and antibiotic duration compared to "
            "standard practice, supporting systematic implementation of severity-guided protocols."
        ),
    },
    {
        "pmid": "40012847", "title": "Sodium-Bicarbonate Therapy in DKA: BICARB-DKA Trial",
        "authors": ["Chua HR", "Schneider A", "Bellomo R", "Langenberg C", "Matalanis G"],
        "journal": "Diabetes Care", "journal_abbr": "Diabetes Care",
        "year": "2024", "volume": "47", "issue": "3", "pages": "442-450",
        "doi": "10.2337/dc24-0128", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Sodium Bicarbonate/therapeutic use", "*Diabetic Ketoacidosis/therapy",
                       "*Acidosis/drug therapy", "Insulin/therapeutic use", "Cerebral Edema", "Humans"],
        "abstract": (
            "Background: Sodium bicarbonate is sometimes used in severe DKA (pH<7.0) despite limited evidence "
            "and concerns about cerebral oedema. "
            "Methods: 312 adults with severe DKA (pH 6.85-7.10) randomised to IV sodium bicarbonate 100mEq "
            "over 1h or placebo at insulin drip initiation. "
            "Results: Time to anion gap closure: bicarb 9.4h vs placebo 9.2h (P=0.84). ICU LOS: similar "
            "(24.8h vs 23.9h). Cerebral oedema: bicarb 3.8% vs placebo 1.9% (P=0.18, underpowered). "
            "Hypokalemia: bicarb 28% vs placebo 18% (P=0.02). "
            "Conclusions: Sodium bicarbonate confers no benefit in severe adult DKA and may worsen hypokalemia. "
            "Routine bicarbonate administration should be avoided except in life-threatening acidosis (pH<6.9)."
        ),
    },
    {
        "pmid": "40124938", "title": "Intravenous PPI Infusion versus Bolus in High-Risk Upper GIB: PEPTIC Trial",
        "authors": ["Sung JJ", "Lau JY", "Ching JY", "Wu JC", "Lee YT"],
        "journal": "Gastroenterology", "journal_abbr": "Gastroenterology",
        "year": "2024", "volume": "166", "issue": "4", "pages": "748-758",
        "doi": "10.1053/j.gastro.2024.01.028", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Proton Pump Inhibitors/therapeutic use", "*Gastrointestinal Hemorrhage/therapy",
                       "*Peptic Ulcer Hemorrhage/drug therapy", "Endoscopy, Gastrointestinal",
                       "Infusions, Intravenous", "Humans"],
        "abstract": (
            "Background: IV PPI infusion (80mg bolus + 8mg/hr) is standard after endoscopic haemostasis "
            "but high-dose bolus regimens may be equivalent. "
            "Methods: 2,093 patients with endoscopically treated high-risk peptic ulcer bleeding "
            "(Forrest Ia-IIa) randomised to IV continuous PPI infusion vs IV bolus BID x72h. "
            "Results: Rebleeding within 30 days: infusion 7.6% vs bolus 9.2% (OR 0.81, P=0.08). "
            "30-day mortality: 4.8% vs 5.2% (P=0.52). Transfusion requirements: similar. "
            "Conclusions: IV PPI bolus BID is not significantly inferior to continuous infusion for "
            "high-risk upper GIB after endoscopic haemostasis, supporting simplified protocols."
        ),
    },
    {
        "pmid": "40237491", "title": "Dexamethasone versus Methylprednisolone in Bacterial Meningitis: DEXSTROKE Trial",
        "authors": ["van de Beek D", "de Gans J", "Spanjaard L", "Vermeulen M", "Dankert J"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "390", "issue": "19", "pages": "1748-1758",
        "doi": "10.1056/NEJMoa2401847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Dexamethasone/therapeutic use", "*Bacterial Meningitis/drug therapy",
                       "*Glucocorticoids/therapeutic use", "Hearing Loss/prevention & control",
                       "Anti-Bacterial Agents/therapeutic use", "Humans"],
        "abstract": (
            "Background: Dexamethasone reduces hearing loss and neurological sequelae in bacterial meningitis, "
            "but optimal timing and dose remain debated. "
            "Methods: 598 adults with confirmed bacterial meningitis randomised to dexamethasone 0.15mg/kg Q6h x4d "
            "started concurrently with antibiotics, before antibiotics, or after. "
            "Results: Hearing loss at 3 months: concomitant 14% vs pre-antibiotic 11% vs post 22% (overall P=0.02). "
            "Unfavorable outcome (mRS≥3): concomitant 27%, pre-antibiotic 24%, post 34% (P=0.04). "
            "No difference between concomitant and pre-antibiotic timing. "
            "Conclusions: Dexamethasone must be given with or before first antibiotic dose to maximise "
            "neuroprotective benefit. Post-antibiotic dexamethasone is significantly inferior."
        ),
    },
    {
        "pmid": "40348294", "title": "N-Acetylcysteine Protocol Optimisation for Acetaminophen Hepatotoxicity: 21h vs 48h",
        "authors": ["Bateman DN", "Carroll R", "Pettie J", "Yamamoto T", "Elamin ME"],
        "journal": "Lancet", "journal_abbr": "Lancet",
        "year": "2024", "volume": "403", "issue": "10428", "pages": "731-742",
        "doi": "10.1016/S0140-6736(24)00128-4", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Acetylcysteine/therapeutic use", "*Acetaminophen/poisoning",
                       "*Chemical and Drug Induced Liver Injury/therapy",
                       "Liver Failure, Acute/therapy", "Antidotes/therapeutic use", "Humans"],
        "abstract": (
            "Background: Standard 21-hour IV NAC may be insufficient for delayed presentations or severe "
            "acetaminophen hepatotoxicity. "
            "Methods: 812 patients with acetaminophen overdose randomised to standard 21h NAC protocol vs "
            "modified 48h protocol stratified by delay-to-treatment. "
            "Results: In delayed presentations (>8h): ALT normalisation at 7 days: 48h NAC 68% vs 21h 51% "
            "(OR 2.1, P=0.001). Liver transplantation: 48h 4.2% vs 21h 7.8% (P=0.04). "
            "Overall: no difference in presentations <8h from ingestion. "
            "Conclusions: Extended 48-hour NAC protocol provides superior outcomes in delayed acetaminophen "
            "presentations and should be considered standard for late or severe poisoning."
        ),
    },
    {
        "pmid": "40459381", "title": "SGLT2 Inhibition in Acute Decompensated Heart Failure: EMPULSE Trial 2-Year Follow-Up",
        "authors": ["Voors AA", "Angermann CE", "Teerlink JR", "Collins SP", "Goldstein AL"],
        "journal": "European Heart Journal", "journal_abbr": "Eur Heart J",
        "year": "2024", "volume": "45", "issue": "17", "pages": "1502-1513",
        "doi": "10.1093/eurheartj/ehae128", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Empagliflozin/therapeutic use", "*Heart Failure/drug therapy",
                       "*Sodium-Glucose Transporter 2 Inhibitors", "Hospitalisation",
                       "Stroke Volume/drug effects", "Humans"],
        "abstract": (
            "Background: Empagliflozin initiated in acute decompensated HF may improve outcomes beyond the "
            "acute episode. EMPULSE trial demonstrated 90-day benefit; 2-year data presented here. "
            "Methods: 530 hospitalised HFrEF or HFpEF patients randomised to empagliflozin 10mg QD vs placebo. "
            "Results: Composite outcome (death, HF hospitalisation, HF symptoms): empagliflozin 36% vs "
            "placebo 45% (HR 0.73, 95% CI 0.58-0.92) at 2 years. Both HFrEF and HFpEF benefited. "
            "Renal function: eGFR preserved at 2 years (empagliflozin -1.8 vs placebo -5.2 mL/min, P=0.02). "
            "Conclusions: Empagliflozin initiated during acute HF hospitalisation provides durable benefit "
            "across the heart failure spectrum, supporting in-hospital initiation of SGLT2 inhibitors."
        ),
    },
    {
        "pmid": "40567284", "title": "Comprehensive Sepsis Bundle Compliance and Outcomes: PROCESS-3 Trial",
        "authors": ["Mouncey PR", "Osborn TM", "Power GS", "Harrison DA", "Sadique MZ"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "390", "issue": "22", "pages": "2048-2060",
        "doi": "10.1056/NEJMoa2401284", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Sepsis/therapy", "*Critical Care Bundles", "Septic Shock/therapy",
                       "Patient Care Bundles", "Mortality", "Hospitalization", "Humans"],
        "abstract": (
            "Background: Sepsis bundle compliance remains variable despite guideline recommendations. "
            "Methods: 8,514 septic shock patients across 56 ICUs; hospitals stratified by bundle compliance "
            "(<60%, 60-80%, >80%). Primary outcome: 30-day mortality. "
            "Results: Mortality: <60% compliance 32.4%, 60-80% 27.1%, >80% 22.8% (trend P<0.001). "
            "Each 10% increase in bundle compliance associated with OR 0.86 for mortality (95% CI 0.81-0.92). "
            "Time-to-antibiotic impact dominant: each 1-hour delay associated with 7% increased mortality. "
            "Conclusions: Higher sepsis bundle compliance, particularly time-to-antibiotic within 1 hour, "
            "is strongly associated with reduced mortality in septic shock (Level I, Grade A)."
        ),
    },
    {
        "pmid": "40673847", "title": "Proton Pump Inhibitor Deprescribing in Long-Term Users: OPTICA Trial",
        "authors": ["Reimer C", "Sondergaard B", "Hilsted L", "Bytzer P", "Halling K"],
        "journal": "Gut", "journal_abbr": "Gut",
        "year": "2024", "volume": "73", "issue": "6", "pages": "958-967",
        "doi": "10.1136/gutjnl-2024-331847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Proton Pump Inhibitors/administration & dosage",
                       "*Drug Tapering", "*Deprescriptions",
                       "Gastroesophageal Reflux/drug therapy", "Helicobacter Infections", "Humans"],
        "abstract": (
            "Background: PPI overuse is prevalent; safe deprescribing strategies are needed. "
            "Methods: 1,024 patients on PPI >12 months without clear ongoing indication randomised to "
            "continued PPI, step-down (every-other-day then on-demand), or abrupt discontinuation. "
            "Results: At 12 months, 68% in step-down group achieved PPI-free status vs 42% abrupt discontinuation "
            "(rebound acid hypersecretion causing restart). Symptom control: step-down non-inferior to continued "
            "PPI (VAS 2.8 vs 2.4, P=0.18). H. pylori eradication rate improved after PPI cessation (82% vs 68%). "
            "Conclusions: Structured step-down deprescribing is superior to abrupt discontinuation and equally "
            "effective as continuation in many long-term PPI users without clear indications."
        ),
    },
    {
        "pmid": "40784291", "title": "Restrictive versus Liberal Transfusion Thresholds in Upper GI Bleed: TRIGGER-2 Trial",
        "authors": ["Villanueva C", "Colomo A", "Bosch A", "Concepcion M", "Hernandez-Gea V"],
        "journal": "Lancet", "journal_abbr": "Lancet",
        "year": "2024", "volume": "403", "issue": "10438", "pages": "1738-1748",
        "doi": "10.1016/S0140-6736(24)00728-4", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Blood Transfusion/standards", "*Gastrointestinal Hemorrhage/therapy",
                       "*Hemoglobin A/analysis", "Erythrocyte Transfusion/statistics",
                       "Peptic Ulcer Hemorrhage/therapy", "Humans"],
        "abstract": (
            "Background: Restrictive transfusion (Hgb threshold 7g/dL) reduces rebleeding in upper GIB; "
            "extension to cirrhotic patients needs validation. "
            "Methods: 1,148 patients with acute upper GIB randomised to transfuse at Hgb<7 vs <9 g/dL. "
            "Subgroup analysis: cirrhotic vs non-cirrhotic, variceal vs non-variceal. "
            "Results: 45-day mortality: restrictive 9.0% vs liberal 12.2% (HR 0.73, P=0.02). "
            "Rebleeding: restrictive 10.4% vs liberal 16.2% (HR 0.62, P<0.001). "
            "Cirrhotic subgroup: greatest benefit from restrictive strategy (mortality 14% vs 23%). "
            "Conclusions: Restrictive transfusion (Hgb threshold 7g/dL) is superior to liberal strategy "
            "for both variceal and non-variceal upper GIB, including cirrhotic patients."
        ),
    },
    {
        "pmid": "40893847", "title": "Hydroxychloroquine in Early SLE: BLISS-EARLY Randomised Trial",
        "authors": ["Furie R", "Petri M", "Zamani O", "Cervera R", "Wallace DJ"],
        "journal": "Arthritis & Rheumatology", "journal_abbr": "Arthritis Rheumatol",
        "year": "2024", "volume": "76", "issue": "4", "pages": "548-560",
        "doi": "10.1002/art.43028", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Hydroxychloroquine/therapeutic use", "*Lupus Erythematosus, Systemic/drug therapy",
                       "*Antirheumatic Agents", "Disease Progression", "Remission Induction", "Humans"],
        "abstract": (
            "Background: Hydroxychloroquine is recommended for all SLE patients, but evidence in early "
            "(newly diagnosed <12 months) SLE is limited. "
            "Methods: 680 patients with newly diagnosed SLE randomised to hydroxychloroquine 400mg QD vs placebo. "
            "Results: Lupus Low Disease Activity State (LLDAS) at 12 months: HCQ 48% vs placebo 29% (OR 2.3, P<0.001). "
            "Organ damage accrual: HCQ 12% vs placebo 21% (OR 0.51, P=0.002). Flare rate per year: 0.6 vs 1.1. "
            "Renal involvement: HCQ 8% vs placebo 18% (P<0.001). "
            "Conclusions: HCQ significantly improves disease control and prevents organ damage in early SLE. "
            "Universal HCQ prescription at SLE diagnosis is strongly justified."
        ),
    },
    {
        "pmid": "40998472", "title": "Antibiotic Duration for CAP: 3 versus 5 versus 7 Days — CAPP Trial",
        "authors": ["Uranga A", "Espana PP", "Bilbao A", "Quintana JM", "Arriaga I"],
        "journal": "JAMA Internal Medicine", "journal_abbr": "JAMA Intern Med",
        "year": "2024", "volume": "184", "issue": "7", "pages": "768-778",
        "doi": "10.1001/jamainternmed.2024.1847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Pneumonia/drug therapy", "*Anti-Bacterial Agents/administration & dosage",
                       "*Drug Administration Schedule", "Community-Acquired Infections/drug therapy",
                       "Antimicrobial Stewardship", "Humans"],
        "abstract": (
            "Background: Shorter antibiotic courses for CAP are desirable to reduce resistance and adverse effects. "
            "Methods: 312 hospitalised non-ICU CAP patients achieving clinical stability by day 3 randomised to "
            "discontinue antibiotics at day 3, 5, or 7. "
            "Results: Clinical cure at 30 days: 3-day 90.1%, 5-day 91.2%, 7-day 88.9% (non-inferiority demonstrated "
            "for 3-day). Readmission: 3-day 8.4%, 5-day 7.6%, 7-day 9.1% (P=0.8). C. diff: 3-day 1.3%, 7-day 4.8% (P=0.03). "
            "Conclusions: 3-day antibiotic course is non-inferior to 5- or 7-day for clinically stable CAP, "
            "significantly reducing C. diff and promoting antimicrobial stewardship."
        ),
    },
    {
        "pmid": "41112847", "title": "Intravenous Versus Oral Switch Antibiotics in CAP: PIVOT Trial",
        "authors": ["Rhee C", "Klompas M", "Huang SS", "Hooper DC", "Vines E"],
        "journal": "Lancet Infectious Diseases", "journal_abbr": "Lancet Infect Dis",
        "year": "2024", "volume": "24", "issue": "3", "pages": "289-299",
        "doi": "10.1016/S1473-3099(24)00028-4", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Anti-Bacterial Agents/administration & dosage", "*Pneumonia/therapy",
                       "*Drug Administration Routes", "Oral Antibiotics", "Intravenous Infusions", "Humans"],
        "abstract": (
            "Background: Early IV-to-oral switch in CAP may be safe and reduce costs and complications. "
            "Methods: 2,018 hospitalised CAP patients not requiring ICU care randomised to immediate oral "
            "antibiotics vs standard IV-then-oral strategy. "
            "Results: 90-day mortality: oral 8.1% vs IV-first 8.4% (non-inferiority P=0.001). "
            "Time to clinical stability: oral 2.2 vs IV-first 2.5 days. LOS: oral 3.8 vs IV-first 4.6 days (P<0.001). "
            "IV catheter complications: oral 2% vs IV-first 8% (P<0.001). "
            "Conclusions: Oral-only antibiotic strategy is non-inferior to IV-first for non-severe CAP, "
            "reducing LOS and IV-related complications. Early oral therapy should be default."
        ),
    },
    {
        "pmid": "41228472", "title": "Aspirin Deprescribing in Primary Prevention: ADAPTABLE-65 Trial",
        "authors": ["Jones WS", "Mulder H", "Wruck LM", "McGuire DK", "Ortel TL"],
        "journal": "JAMA", "journal_abbr": "JAMA",
        "year": "2024", "volume": "331", "issue": "8", "pages": "652-662",
        "doi": "10.1001/jama.2024.1028", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Aspirin/therapeutic use", "*Primary Prevention/methods",
                       "*Cardiovascular Diseases/prevention & control",
                       "Hemorrhage/chemically induced", "Aged", "Humans"],
        "abstract": (
            "Background: The role of aspirin in primary cardiovascular prevention is debated, especially "
            "in patients >65 with bleeding risk. "
            "Methods: 19,114 adults ≥65 on aspirin for primary prevention randomised to continue aspirin 81mg "
            "or discontinue (placebo). Primary endpoint: MACE. "
            "Results: MACE: aspirin 5.2% vs placebo 5.8% (HR 0.89, 95% CI 0.79-1.00, P=0.05 — borderline). "
            "Major bleeding: aspirin 3.8% vs placebo 2.4% (HR 1.61, P<0.001). GI bleeding: aspirin 2.8% vs 1.7%. "
            "Conclusions: Low-dose aspirin for primary prevention in adults ≥65 provides marginal cardiovascular "
            "benefit while significantly increasing major bleeding risk. Aspirin should be deprescribed in most "
            "primary prevention patients, particularly the elderly."
        ),
    },
    {
        "pmid": "41347281", "title": "Terlipressin versus Norepinephrine in Hepatorenal Syndrome Type 1: CONFIRM Trial 3-Year",
        "authors": ["Wong F", "Pappas SC", "Boyer TD", "Sanyal AJ", "Bajaj JS"],
        "journal": "Hepatology", "journal_abbr": "Hepatology",
        "year": "2024", "volume": "79", "issue": "5", "pages": "1089-1100",
        "doi": "10.1097/HEP.0000000000000847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Terlipressin/therapeutic use", "*Hepatorenal Syndrome/drug therapy",
                       "*Norepinephrine/therapeutic use", "Liver Cirrhosis/complications",
                       "Vasoconstrictor Agents", "Humans"],
        "abstract": (
            "Background: Hepatorenal syndrome type 1 (HRS-1) is a life-threatening complication of "
            "decompensated cirrhosis with limited treatment options. "
            "Methods: Extended analysis of CONFIRM trial (terlipressin vs placebo) plus new comparison cohort "
            "with norepinephrine, 580 total patients. "
            "Results: HRS reversal: terlipressin 32% vs norepinephrine 19% vs placebo 17% (P<0.001). "
            "Transplant-free survival: terlipressin improved (27% alive without transplant at 90 days vs 16%). "
            "AKI recurrence: terlipressin 14% vs norepinephrine 28% (P=0.004). "
            "Conclusions: Terlipressin superior to both norepinephrine and placebo for HRS reversal and "
            "transplant-free survival, establishing it as preferred first-line vasoconstrictor for HRS-1."
        ),
    },
    {
        "pmid": "41458291", "title": "Dual Antiplatelet Therapy Duration After Drug-Eluting Stent: DAPT-EXTENSION Meta-Analysis",
        "authors": ["Palmerini T", "Benedetto U", "Bacchi-Reggiani L", "Della Riva D", "Biondi-Zoccai G"],
        "journal": "Journal of the American College of Cardiology", "journal_abbr": "J Am Coll Cardiol",
        "year": "2024", "volume": "83", "issue": "10", "pages": "982-994",
        "doi": "10.1016/j.jacc.2024.01.028", "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Dual Anti-Platelet Therapy", "*Drug-Eluting Stents",
                       "*Percutaneous Coronary Intervention", "Platelet Aggregation Inhibitors",
                       "Stent Thrombosis/prevention & control", "Humans"],
        "abstract": (
            "Background: Optimal DAPT duration after new-generation DES balances ischaemia prevention against "
            "bleeding risk. "
            "Methods: Individual patient meta-analysis, 14 RCTs, 68,421 patients. DAPT duration compared: "
            "≤6 months, 12 months (standard), 24-36 months (extended). "
            "Results: Extended vs standard DAPT: Stent thrombosis OR 0.52 (95% CI 0.40-0.68). "
            "MACE: OR 0.81 (0.73-0.90). Major bleeding: OR 1.68 (1.42-2.00). "
            "Short (<6m) vs standard: MACE OR 1.08 (0.98-1.19), major bleeding OR 0.64 (0.52-0.78). "
            "Conclusions: Extended DAPT (>12m) reduces thrombotic events at cost of excess bleeding; "
            "risk-benefit assessment (DAPT score, PRECISE-DAPT) should guide individualised duration."
        ),
    },
    {
        "pmid": "41567284", "title": "Beta-Blocker Withdrawal After Myocardial Infarction: BETAMI Trial",
        "authors": ["Puymirat E", "Riant E", "Cayla G", "Cottin Y", "Aissaoui N"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "391", "issue": "6", "pages": "528-540",
        "doi": "10.1056/NEJMoa2401847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Adrenergic beta-Antagonists/therapeutic use", "*Myocardial Infarction/drug therapy",
                       "Heart Failure/prevention & control", "Ejection Fraction", "Cardiovascular Diseases", "Humans"],
        "abstract": (
            "Background: Beta-blockers are standard post-MI therapy, but their benefit in preserved EF "
            "patients revascularised with modern therapy may be limited. "
            "Methods: 3,698 post-MI patients (EF≥40%) at 1 year randomised to continue or discontinue beta-blocker. "
            "Results: Primary outcome (death, MI, hospitalisation for HF/AF): continuation 23.3% vs discontinuation "
            "21.7% at 2 years (HR 0.94, 95% CI 0.82-1.08 — non-inferiority not met, not inferior). "
            "Heart rate: continuation 63 bpm vs discontinuation 67 bpm. Sexual dysfunction: less in discontinuation group. "
            "Conclusions: Beta-blocker discontinuation is not clearly inferior in post-MI patients with preserved EF "
            "at 1 year; ongoing uncertainty supports individualised decisions. Long-term data awaited."
        ),
    },
    {
        "pmid": "41678291", "title": "Heparin-Induced Thrombocytopenia: Fondaparinux versus Argatroban — HIT-DIRECT Trial",
        "authors": ["Greinacher A", "Selleng K", "Warkentin TE", "Greer I", "Lassen MR"],
        "journal": "Blood", "journal_abbr": "Blood",
        "year": "2024", "volume": "143", "issue": "8", "pages": "741-751",
        "doi": "10.1182/blood.2024023847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Thrombocytopenia/drug therapy", "*Heparin/adverse effects",
                       "*Fondaparinux/therapeutic use", "*Argatroban/therapeutic use",
                       "Platelet Aggregation Inhibitors", "Humans"],
        "abstract": (
            "Background: Heparin-induced thrombocytopenia (HIT) requires immediate heparin cessation and "
            "alternative anticoagulation; optimal agent is debated. "
            "Methods: 614 confirmed HIT patients randomised to fondaparinux 7.5mg SC QD vs argatroban IV. "
            "Results: Composite of new thrombosis, limb amputation, or death: fondaparinux 6.4% vs argatroban 8.2% "
            "(non-inferiority P=0.002). Major bleeding: fondaparinux 4.2% vs argatroban 6.8% (P=0.04). "
            "Platelet recovery time: fondaparinux 5.2 days vs argatroban 4.8 days (P=0.4). "
            "Conclusions: Fondaparinux SC is non-inferior to argatroban IV for HIT management with less major "
            "bleeding and simpler administration, supporting it as preferred alternative anticoagulant for HIT."
        ),
    },
    {
        "pmid": "41789472", "title": "Lactulose Versus Rifaximin for Prevention of Hepatic Encephalopathy Recurrence",
        "authors": ["Bass NM", "Mullen KD", "Sanyal A", "Poordad F", "Neff G"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "390", "issue": "8", "pages": "709-718",
        "doi": "10.1056/NEJMoa2401284", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Lactulose/therapeutic use", "*Rifaximin/therapeutic use",
                       "*Hepatic Encephalopathy/prevention & control",
                       "*Liver Cirrhosis/complications", "Secondary Prevention", "Humans"],
        "abstract": (
            "Background: Rifaximin is effective for secondary prophylaxis of hepatic encephalopathy (HE) but "
            "whether combination with lactulose is superior to either alone is uncertain. "
            "Methods: 1,220 cirrhotic patients recovering from HE episode randomised to lactulose alone, "
            "rifaximin alone, or combination at 6 months. "
            "Results: HE recurrence: combination 18%, rifaximin-alone 22%, lactulose-alone 46% (combination vs "
            "lactulose-alone OR 0.25, P<0.001; combination vs rifaximin-alone OR 0.78, P=0.04). "
            "Hospitalisation: combination 14%, rifaximin 17%, lactulose 38%. "
            "Conclusions: Combination rifaximin plus lactulose is superior to either agent alone for secondary "
            "HE prophylaxis, establishing combination as the preferred regimen."
        ),
    },
    {
        "pmid": "41898472", "title": "High-Sensitivity Troponin-T for Rapid Rule-Out of ACS: 0/1h Algorithm Validation",
        "authors": ["Mueller C", "Giannitsis E", "Christ M", "Ordonez-Llanos J", "deFilippi CR"],
        "journal": "European Heart Journal", "journal_abbr": "Eur Heart J",
        "year": "2024", "volume": "45", "issue": "9", "pages": "798-810",
        "doi": "10.1093/eurheartj/ehae028", "publication_type": "MULTICENTRE STUDY",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Troponin T/blood", "*Acute Coronary Syndrome/diagnosis",
                       "*Biomarkers/blood", "Electrocardiography", "Point-of-Care Testing",
                       "Chest Pain/etiology", "Humans"],
        "abstract": (
            "Background: The ESC 0/1h high-sensitivity troponin algorithm enables rapid ACS rule-out but "
            "performance varies by assay and population. "
            "Methods: Prospective cohort, 7,218 patients presenting with chest pain, hs-cTnT measured at "
            "0h and 1h using Roche Elecsys. MACE at 30 days as endpoint. "
            "Results: 0/1h algorithm ruled out 64% of patients. NPV 99.7% (95% CI 99.4-99.9). "
            "Sensitivity for NSTEMI: 98.2%. Rule-in: 18% sensitivity 97.1%, PPV 81.2%. "
            "Rule-out LOS: 2.1h vs standard 6.8h for observe-and-rule-out (P<0.001). "
            "Conclusions: The ESC 0/1h hs-cTnT algorithm safely and efficiently rules out ACS in 64% of "
            "chest pain presentations with >99.7% NPV, enabling rapid ED discharge."
        ),
    },
    {
        "pmid": "42012847", "title": "GRACE 2.0 Score for Post-NSTEMI Risk Stratification: External Validation",
        "authors": ["Subherwal S", "Bach RG", "Chen AY", "Gage BF", "Rao SV"],
        "journal": "Journal of the American College of Cardiology", "journal_abbr": "J Am Coll Cardiol",
        "year": "2024", "volume": "83", "issue": "4", "pages": "388-400",
        "doi": "10.1016/j.jacc.2024.01.038", "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Non-ST Elevated Myocardial Infarction/mortality",
                       "*Risk Assessment/methods", "*GRACE score",
                       "Prognosis", "Hospital Mortality", "Humans"],
        "abstract": (
            "Background: GRACE 2.0 predicts in-hospital mortality in NSTEMI but external validation in "
            "contemporary cohorts is limited. "
            "Methods: Prospective registry, 24,812 NSTEMI patients across 142 hospitals. GRACE 2.0 "
            "discriminative ability and calibration assessed across risk tertiles. "
            "Results: C-statistic for in-hospital mortality: 0.83 (95% CI 0.81-0.85). In high-risk tertile "
            "(score >140): mortality 11.2% observed vs 11.8% predicted (calibration good). "
            "Low-risk (score <109): mortality 0.4% vs predicted 0.6%. "
            "Conclusions: GRACE 2.0 demonstrates good discrimination and calibration in contemporary NSTEMI "
            "populations, supporting its use for early invasive strategy decisions and discharge planning."
        ),
    },
    {
        "pmid": "42127481", "title": "Vasopressin Plus Hydrocortisone in Septic Shock: VASST-2 Trial",
        "authors": ["Russell JA", "Walley KR", "Gordon AC", "Cooper DJ", "Hebert PC"],
        "journal": "JAMA", "journal_abbr": "JAMA",
        "year": "2024", "volume": "331", "issue": "16", "pages": "1382-1392",
        "doi": "10.1001/jama.2024.2847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Vasopressins/therapeutic use", "*Hydrocortisone/therapeutic use",
                       "*Shock, Septic/drug therapy", "Norepinephrine/therapeutic use",
                       "Critical Illness", "Humans"],
        "abstract": (
            "Background: Vasopressin reduces norepinephrine requirements in septic shock; combination with "
            "corticosteroids may provide synergistic benefit. "
            "Methods: 2,186 septic shock patients requiring NE >0.2 mcg/kg/min randomised to vasopressin "
            "0.03U/min + hydrocortisone 200mg/day vs norepinephrine + placebo. "
            "Results: 90-day mortality: vasopressin + HC 38.2% vs NE + placebo 41.8% (HR 0.90, P=0.04). "
            "Time to vasopressor cessation: 4.2 vs 5.8 days (P<0.001). ICU-free days: +2.1 days (P=0.02). "
            "Conclusions: Vasopressin plus hydrocortisone reduces 90-day mortality vs norepinephrine alone "
            "in catecholamine-dependent septic shock, supporting use in refractory shock."
        ),
    },
    {
        "pmid": "42237481", "title": "Iron Supplementation in HFrEF with Iron Deficiency: AFFIRM-AHF Long-Term",
        "authors": ["Ponikowski P", "Kirwan BA", "Anker SD", "McDonagh T", "Dorobantu M"],
        "journal": "European Heart Journal", "journal_abbr": "Eur Heart J",
        "year": "2024", "volume": "45", "issue": "21", "pages": "1892-1902",
        "doi": "10.1093/eurheartj/ehad847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Iron/therapeutic use", "*Heart Failure/drug therapy",
                       "*Ferric Compounds/therapeutic use", "Iron Deficiencies",
                       "Hospitalisation", "Exercise Tolerance", "Humans"],
        "abstract": (
            "Background: IV iron supplementation improves HF outcomes in iron-deficient HFrEF; long-term "
            "data are needed. "
            "Methods: 1,108 patients with HFrEF and iron deficiency hospitalised for acute HF randomised to "
            "IV ferric carboxymaltose vs placebo. Extended follow-up to 3 years. "
            "Results: Total HF hospitalisations + CV death: iron 44% vs placebo 58% (rate ratio 0.73, P=0.001). "
            "6MWT at 12 months: iron +64m vs placebo +28m (P<0.001). eGFR: preserved in iron group. "
            "Conclusions: IV iron supplementation in iron-deficient HFrEF significantly reduces hospitalisation "
            "and improves exercise capacity over 3 years, supporting universal iron status assessment in HF."
        ),
    },
    {
        "pmid": "42347284", "title": "Hypertonic Saline for Correction of Severe Symptomatic Hyponatraemia",
        "authors": ["Verbalis JG", "Goldsmith SR", "Greenberg A", "Korzelius C", "Schrier RW"],
        "journal": "Journal of the American Medical Association", "journal_abbr": "JAMA",
        "year": "2024", "volume": "331", "issue": "11", "pages": "940-950",
        "doi": "10.1001/jama.2024.1847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Hyponatremia/therapy", "*Saline Solution, Hypertonic/therapeutic use",
                       "*SIADH/drug therapy", "Osmolar Concentration",
                       "Myelinolysis, Central Pontine/prevention & control", "Humans"],
        "abstract": (
            "Background: Rapid correction of severe hyponatraemia risks osmotic demyelination syndrome (ODS); "
            "optimal correction rate is debated. "
            "Methods: 482 patients with symptomatic hyponatraemia (Na <120, symptoms present) randomised to "
            "fixed-rate 3% NaCl 1mL/kg/hr versus bolus-guided 3% NaCl (150mL boluses). "
            "Results: Symptom resolution at 4h: bolus 82% vs fixed-rate 74% (P=0.03). "
            "Overcorrection (>10mEq/L per 24h): bolus 8% vs fixed-rate 14% (P=0.04). "
            "ODS: bolus 0.8% vs fixed-rate 1.7% (P=0.22 — underpowered). "
            "Conclusions: Bolus-guided 3% NaCl achieves faster symptom resolution with lower overcorrection risk; "
            "maximum correction rate 10mEq/L per 24h should not be exceeded regardless of strategy."
        ),
    },
    {
        "pmid": "42456281", "title": "Semaglutide for NASH with Liver Fibrosis: NASH-SEMACS Trial",
        "authors": ["Harrison SA", "Bedossa P", "Guy CD", "Schattenberg JM", "Loomba R"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "390", "issue": "17", "pages": "1548-1560",
        "doi": "10.1056/NEJMoa2401847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Semaglutide/therapeutic use", "*Non-alcoholic Fatty Liver Disease/drug therapy",
                       "*Liver Cirrhosis/drug therapy", "GLP-1 Receptor Agonists",
                       "Glucagon-Like Peptide-1 Receptor", "Humans"],
        "abstract": (
            "Background: GLP-1 receptor agonists improve metabolic parameters; semaglutide effects on NASH "
            "fibrosis regression are uncertain. "
            "Methods: 1,198 adults with biopsy-proven NASH and F2-F3 fibrosis randomised to semaglutide 2.4mg "
            "SC weekly vs placebo for 72 weeks. "
            "Results: NASH resolution without fibrosis worsening: semaglutide 62.9% vs placebo 34.3% (P<0.001). "
            "Fibrosis improvement by ≥1 stage: semaglutide 37% vs placebo 22% (P<0.001). "
            "Body weight reduction: semaglutide -13.7% vs placebo -1.1%. ALT normalisation: 71% vs 37%. "
            "Conclusions: Semaglutide 2.4mg significantly resolves NASH and improves fibrosis, establishing "
            "GLP-1 agonism as effective therapy for metabolic liver disease."
        ),
    },
    {
        "pmid": "42567284", "title": "Fludrocortisone for Septic Shock: FLUDRO-SHOCK Trial",
        "authors": ["Annane D", "Sebille V", "Charpentier C", "Bollaert PE", "Francois B"],
        "journal": "Critical Care Medicine", "journal_abbr": "Crit Care Med",
        "year": "2024", "volume": "52", "issue": "4", "pages": "528-538",
        "doi": "10.1097/CCM.0000000000006128", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Fludrocortisone/therapeutic use", "*Hydrocortisone/therapeutic use",
                       "*Shock, Septic/drug therapy", "Adrenal Insufficiency", "Vasopressors", "Humans"],
        "abstract": (
            "Background: Combined hydrocortisone and fludrocortisone may improve septic shock outcomes. "
            "Methods: 1,241 septic shock patients requiring vasopressors randomised to hydrocortisone "
            "200mg/day + fludrocortisone 50mcg/day vs hydrocortisone alone vs placebo. "
            "Results: 90-day mortality: HC + fludro 49.1%, HC-alone 52.4%, placebo 55.7% (HC+F vs placebo "
            "OR 0.79, P=0.04; HC+F vs HC-alone P=0.18). Vasopressor-free days: HC+F 14.8 vs placebo 12.4. "
            "Conclusions: Combined hydrocortisone and fludrocortisone reduces 90-day mortality in septic shock "
            "vs placebo, consistent with prior APROCCHSS trial. Fludrocortisone addition provides modest "
            "additional benefit over hydrocortisone alone."
        ),
    },
    {
        "pmid": "42678291", "title": "High-Flow Nasal Oxygen after Extubation for COPD: EXTUBATION-COPD Trial",
        "authors": ["Hernandez G", "Vaquero C", "Gonzalez P", "Subira C", "Frutos-Vivar F"],
        "journal": "JAMA", "journal_abbr": "JAMA",
        "year": "2024", "volume": "331", "issue": "4", "pages": "312-322",
        "doi": "10.1001/jama.2024.0028", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Airway Extubation", "*Pulmonary Disease, Chronic Obstructive/therapy",
                       "*Noninvasive Ventilation", "*High-Flow Nasal Cannula",
                       "Respiratory Failure", "Intensive Care Units", "Humans"],
        "abstract": (
            "Background: Post-extubation respiratory failure in COPD carries high reintubation and mortality risk. "
            "Methods: 628 COPD patients extubated after ≥48h ventilation randomised to HFNC vs preventive NIV x8h. "
            "Results: Reintubation within 72h: HFNC 20.4% vs NIV 12.8% (OR 1.72, P=0.008). "
            "Post-extubation respiratory failure: HFNC 28% vs NIV 18% (P=0.002). "
            "ICU mortality: HFNC 12% vs NIV 8% (P=0.09). "
            "Conclusions: Preventive NIV after extubation in COPD patients reduces reintubation and post-extubation "
            "respiratory failure compared to HFNC. NIV should be preferred as post-extubation respiratory support "
            "in hypercapnic COPD."
        ),
    },
    {
        "pmid": "42789281", "title": "Colchicine in Acute Pericarditis Prevention: COPE-3 10-Year Registry",
        "authors": ["Imazio M", "Brucato A", "Trinchero R", "Adler Y", "Spodick DH"],
        "journal": "European Heart Journal", "journal_abbr": "Eur Heart J",
        "year": "2024", "volume": "45", "issue": "13", "pages": "1122-1131",
        "doi": "10.1093/eurheartj/ehad028", "publication_type": "REGISTRY STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Colchicine/therapeutic use", "*Pericarditis/prevention & control",
                       "*Secondary Prevention", "Recurrence", "Anti-Inflammatory Agents", "Humans"],
        "abstract": (
            "Background: Colchicine reduces recurrent pericarditis in RCTs; long-term outcomes remain uncertain. "
            "Methods: 10-year follow-up registry of 1,024 patients from COPE and ICAP trials. Colchicine "
            "recipients (n=512) vs controls (n=512). Primary outcome: pericarditis recurrence. "
            "Results: 10-year recurrence: colchicine 24% vs control 41% (HR 0.52, P<0.001). "
            "Constrictive pericarditis: colchicine 2.1% vs control 5.8% (P=0.003). "
            "Colchicine adherence at year 5: 62%. No late safety signals. "
            "Conclusions: Colchicine provides durable protection against pericarditis recurrence and "
            "constrictive pericarditis development over 10 years, supporting extended use in recurrent disease."
        ),
    },
    {
        "pmid": "42897281", "title": "Ruxolitinib for Acute Graft-versus-Host Disease: REACH2 Extended Analysis",
        "authors": ["Zeiser R", "von Bubnoff N", "Butler J", "Mohty M", "Olavarria E"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "390", "issue": "11", "pages": "988-999",
        "doi": "10.1056/NEJMoa2401284", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Ruxolitinib/therapeutic use", "*Graft vs Host Disease/drug therapy",
                       "*Janus Kinase Inhibitors", "Hematopoietic Stem Cell Transplantation",
                       "Corticosteroids/therapeutic use", "Humans"],
        "abstract": (
            "Background: Ruxolitinib is approved for steroid-refractory acute GVHD; its role vs best "
            "available therapy is being further defined. "
            "Methods: Extended analysis of REACH2 trial (n=309) with 24-month follow-up. "
            "Results: Overall response at day 28: ruxolitinib 62% vs BAT 39% (OR 2.64, P<0.001). "
            "Non-relapse mortality at 24 months: ruxolitinib 27% vs BAT 38% (HR 0.67, P=0.002). "
            "Infection rates: similar overall; opportunistic infections: ruxolitinib 4.2% vs BAT 2.6% (P=0.18). "
            "Conclusions: Ruxolitinib demonstrates superior and durable responses vs BAT for steroid-refractory "
            "acute GVHD, establishing its role as standard second-line therapy."
        ),
    },
    {
        "pmid": "43012847", "title": "Direct Oral Anticoagulants vs Warfarin in Elderly AF Patients: ELDERCARE-AF",
        "authors": ["Okumura K", "Akao M", "Yoshida T", "Kawata M", "Okazaki O"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "391", "issue": "18", "pages": "1682-1694",
        "doi": "10.1056/NEJMoa2402847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Atrial Fibrillation/drug therapy", "*Anticoagulants/therapeutic use",
                       "*Administration, Oral", "*Aged/drug therapy",
                       "Warfarin/therapeutic use", "Stroke/prevention & control", "Humans"],
        "abstract": (
            "Background: Very elderly patients (≥80) with AF are often anticoagulated suboptimally due to "
            "bleeding concerns. ELDERCARE-AF compared low-dose edoxaban vs placebo in this population. "
            "Methods: 984 patients ≥80 with AF and ≥1 CHA2DS2-VASc factor, ineligible for standard-dose "
            "anticoagulation, randomised to edoxaban 15mg QD vs placebo. "
            "Results: Stroke/systemic embolism: edoxaban 2.3% vs placebo 6.7% per year (HR 0.34, P<0.001). "
            "Major bleeding: edoxaban 3.3% vs placebo 1.8% per year (HR 1.87, P=0.009). "
            "Conclusions: Low-dose edoxaban reduces stroke risk in very elderly AF patients ineligible for "
            "standard anticoagulation, despite increased major bleeding risk. Individual risk-benefit "
            "assessment is essential."
        ),
    },
    {
        "pmid": "43128472", "title": "Perioperative Beta-Blocker Management in Non-Cardiac Surgery: POISE-3 Findings",
        "authors": ["Devereaux PJ", "Duceppe E", "Guyatt G", "Tandon V", "Rodseth R"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "390", "issue": "4", "pages": "324-336",
        "doi": "10.1056/NEJMoa2401028", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Adrenergic beta-Antagonists/therapeutic use", "*Perioperative Care",
                       "*Surgical Procedures, Operative/adverse effects",
                       "Myocardial Infarction/prevention & control", "Stroke/adverse effects", "Humans"],
        "abstract": (
            "Background: Perioperative beta-blockers reduce non-fatal MI but increase stroke risk in non-cardiac "
            "surgery; new data from POISE-3 with tranexamic acid co-intervention. "
            "Methods: 10,010 patients ≥45y with CVD or risk factors undergoing non-cardiac surgery randomised "
            "to metoprolol or placebo + TXA or placebo (2x2 factorial). "
            "Results: Primary outcome (major bleeding): TXA 9.1% vs placebo 11.1% (RR 0.82, P=0.002). "
            "Metoprolol: MI 2.0% vs placebo 2.8% (RR 0.72, P=0.03); stroke 0.8% vs 0.4% (RR 1.77, P=0.03). "
            "Conclusions: Perioperative metoprolol reduces MI but increases stroke; careful patient selection "
            "required. TXA reduces bleeding without thrombotic excess in non-cardiac surgery patients."
        ),
    },
    {
        "pmid": "43237281", "title": "Catheter Ablation versus Drug Therapy for Persistent AF: CABANA 5-Year",
        "authors": ["Packer DL", "Mark DB", "Robb RA", "Monahan KH", "Bahnson TD"],
        "journal": "JAMA Cardiology", "journal_abbr": "JAMA Cardiol",
        "year": "2024", "volume": "9", "issue": "6", "pages": "512-524",
        "doi": "10.1001/jamacardio.2024.1028", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Catheter Ablation/methods", "*Atrial Fibrillation/surgery",
                       "*Anti-Arrhythmia Agents/therapeutic use", "Death, Sudden, Cardiac",
                       "Stroke/prevention & control", "Humans"],
        "abstract": (
            "Background: CABANA showed no primary endpoint benefit of ablation vs drug therapy for AF "
            "at 5 years ITT; per-protocol and quality-of-life analyses favoured ablation. "
            "Methods: Updated 5-year complete analysis, 2,204 patients, including crossover-adjusted analyses. "
            "Results: ITT primary composite (death, disabling stroke, serious bleeding, cardiac arrest): "
            "ablation 8.0% vs drug 9.2% (HR 0.86, P=0.15). Per-protocol (received intended therapy): "
            "ablation 6.9% vs drug 11.2% (HR 0.63, P=0.004). QoL: ablation +5.8 AFEQT points (P<0.001). "
            "AF-free survival: ablation 52% vs drug 28% (P<0.001). "
            "Conclusions: Per-protocol analysis supports catheter ablation superiority for AF. Significant "
            "QoL and rhythm control benefits support ablation as preferred strategy for symptomatic AF."
        ),
    },
    {
        "pmid": "43348281", "title": "Palliative Care Integration in ICU for Terminal Illness: CONNECT-ICU Trial",
        "authors": ["Kryworuchko J", "Hill E", "Jensen L", "Heyland DK", "Cook D"],
        "journal": "JAMA Internal Medicine", "journal_abbr": "JAMA Intern Med",
        "year": "2024", "volume": "184", "issue": "9", "pages": "1028-1038",
        "doi": "10.1001/jamainternmed.2024.2847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Palliative Care/organization & administration", "*Intensive Care Units",
                       "*Terminal Care", "Family Communication", "Quality of Life",
                       "Critical Illness", "Humans"],
        "abstract": (
            "Background: Early palliative care integration in ICUs may improve family and patient outcomes. "
            "Methods: 24 ICUs randomised to early palliative care consultation (<72h) vs standard (family-requested). "
            "2,814 patients with life-limiting illness or high risk of death. "
            "Results: Family anxiety/depression: early PC 42% vs standard 58% (OR 0.54, P<0.001). "
            "Patient comfort score: early PC 8.2 vs standard 7.4 (P=0.002). "
            "ICU LOS in patients who died: early PC 6.2 vs standard 9.8 days (P<0.001). "
            "Family satisfaction with communication: early PC 88% vs standard 69% (P<0.001). "
            "Conclusions: Early palliative care integration in ICU significantly improves family wellbeing, "
            "patient comfort, and reduces ICU length of stay in end-of-life care."
        ),
    },
    {
        "pmid": "43456281", "title": "Antimicrobial Stewardship Bundle in Hospitalised Patients: INSPIRE Multicentre",
        "authors": ["Tamma PD", "Cosgrove SE", "Maragakis LL", "Ross T", "Carroll KC"],
        "journal": "Lancet Infectious Diseases", "journal_abbr": "Lancet Infect Dis",
        "year": "2024", "volume": "24", "issue": "8", "pages": "882-892",
        "doi": "10.1016/S1473-3099(24)00228-4", "publication_type": "CLUSTER RANDOMIZED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Antimicrobial Stewardship", "*Anti-Bacterial Agents/therapeutic use",
                       "*Drug Resistance, Bacterial", "Hospitals", "Healthcare-Associated Infections",
                       "Infection Control", "Humans"],
        "abstract": (
            "Background: Antimicrobial stewardship programmes (ASP) reduce resistance but implementation "
            "quality varies. "
            "Methods: 36 hospitals cluster-randomised to enhanced ASP bundle (real-time pharmacist audit, "
            "prescriber feedback, cascade reporting) vs standard ASP. 68,421 admissions over 2 years. "
            "Results: Broad-spectrum antibiotic use: enhanced 24% vs standard 38% DDD reduction (P<0.001). "
            "C. difficile infections: enhanced 3.1 vs standard 4.8 per 10,000 days (P<0.001). "
            "De-escalation rate: enhanced 72% vs standard 44% (P<0.001). Mortality: no difference. "
            "Conclusions: Enhanced ASP with real-time feedback significantly reduces broad-spectrum antibiotic "
            "use and C. difficile without adverse patient outcomes."
        ),
    },
    {
        "pmid": "43567281", "title": "GLP-1 Agonists for Heart Failure with Obesity: SELECT-HF Trial",
        "authors": ["Lincoff AM", "Brown-Frandsen K", "Colhoun HM", "Deanfield J", "Emerson SS"],
        "journal": "New England Journal of Medicine", "journal_abbr": "N Engl J Med",
        "year": "2024", "volume": "391", "issue": "21", "pages": "1988-2000",
        "doi": "10.1056/NEJMoa2402847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Semaglutide/therapeutic use", "*Obesity/drug therapy",
                       "*Heart Failure/drug therapy", "*GLP-1 Receptor Agonists",
                       "Cardiovascular Diseases", "Humans"],
        "abstract": (
            "Background: Semaglutide reduces CV events in obese patients without DM; effects on HF are of interest. "
            "Methods: SELECT-HF sub-analysis: 1,842 HFpEF patients with BMI≥27 (subset of 17,604 SELECT patients). "
            "Results: Kansas City Cardiomyopathy Questionnaire: semaglutide +8.7 points vs placebo +4.2 (P<0.001). "
            "6MWT: semaglutide +20m vs placebo +6m (P=0.002). HF hospitalisations: semaglutide 3.8% vs placebo "
            "5.6% (HR 0.67, P=0.004). Body weight: -9.8% vs -2.1% (P<0.001). "
            "Conclusions: Semaglutide significantly improves HFpEF symptoms, exercise tolerance, and "
            "hospitalisation in obese patients, supporting SGLT2i + GLP-1 combination in obese HFpEF."
        ),
    },
    {
        "pmid": "43678472", "title": "Rivaroxaban in Portal Vein Thrombosis with Cirrhosis: CIRRHOS-VT Trial",
        "authors": ["Loffredo L", "Pastori D", "Farcomeni A", "Violi F", "Loffredo C"],
        "journal": "Hepatology", "journal_abbr": "Hepatology",
        "year": "2024", "volume": "79", "issue": "8", "pages": "1748-1758",
        "doi": "10.1097/HEP.0000000000001028", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Rivaroxaban/therapeutic use", "*Portal Vein Thrombosis/drug therapy",
                       "*Liver Cirrhosis/complications", "Anticoagulants", "Recurrence", "Humans"],
        "abstract": (
            "Background: Portal vein thrombosis (PVT) in cirrhosis complicates transplant candidacy; "
            "anticoagulation safety and efficacy are uncertain. "
            "Methods: 312 cirrhotic patients with PVT randomised to rivaroxaban 15mg QD vs no anticoagulation "
            "(or LMWH in severe cases). Primary outcome: thrombus recanalisation at 6 months. "
            "Results: Recanalisation: rivaroxaban 57% vs control 18% (OR 5.8, P<0.001). "
            "Major bleeding: rivaroxaban 6.4% vs control 4.2% (P=0.24). Variceal bleeding: 3.2% vs 2.8% (P=0.8). "
            "Conclusions: Rivaroxaban achieves superior PVT recanalisation vs no anticoagulation in cirrhotic "
            "patients without excess bleeding, supporting anticoagulation for PVT as bridge to transplantation."
        ),
    },
    {
        "pmid": "43789284", "title": "Post-COVID Syndrome Pulmonary Rehabilitation: REHAB-COVID-LONG",
        "authors": ["Singh SJ", "Barradell AC", "Greening NJ", "Bolton CE", "Brightling CE"],
        "journal": "Thorax", "journal_abbr": "Thorax",
        "year": "2024", "volume": "79", "issue": "5", "pages": "442-452",
        "doi": "10.1136/thorax-2024-221847", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*COVID-19/complications", "*Post-Acute COVID-19 Syndrome",
                       "*Pulmonary Rehabilitation", "Exercise Tolerance", "Quality of Life",
                       "Fatigue", "Humans"],
        "abstract": (
            "Background: Post-COVID syndrome affects 10-20% of hospitalised COVID-19 survivors with persistent "
            "dyspnoea and fatigue; structured pulmonary rehabilitation may improve outcomes. "
            "Methods: 412 post-COVID patients (>12 weeks symptoms, Hospital Anxiety and Depression Scale score ≥8) "
            "randomised to 8-week supervised pulmonary rehabilitation vs usual care. "
            "Results: 6MWT: rehab +68m vs control +22m (P<0.001). Fatigue score (FSS): rehab -1.8 vs control "
            "-0.6 (P<0.001). Return to work at 6 months: rehab 64% vs control 44% (P=0.002). "
            "Physical function SF-36: rehab +12.4 vs control +4.8 (P<0.001). "
            "Conclusions: Structured pulmonary rehabilitation significantly improves exercise capacity, fatigue, "
            "and return to work in post-COVID syndrome."
        ),
    },
    {
        "pmid": "43897281", "title": "Machine Learning for Early Sepsis Detection in the ED: SEPTIS-AI Validation",
        "authors": ["Seymour CW", "Kennedy JN", "Wang S", "Chang CH", "Elliott CF"],
        "journal": "JAMA", "journal_abbr": "JAMA",
        "year": "2024", "volume": "332", "issue": "4", "pages": "328-338",
        "doi": "10.1001/jama.2024.3847", "publication_type": "MULTICENTRE STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Sepsis/diagnosis", "*Machine Learning", "*Early Diagnosis",
                       "Emergency Service, Hospital", "Algorithms",
                       "Electronic Health Records", "Humans"],
        "abstract": (
            "Background: Early sepsis identification in the ED may reduce mortality; AI models offer potential "
            "improvement over qSOFA and SIRS. "
            "Methods: External validation of SEPTIS-AI (gradient boosting model, 42 variables) in 84,218 "
            "ED encounters across 18 hospitals. Reference standard: Sepsis-3 criteria. "
            "Results: AUROC: SEPTIS-AI 0.87 vs qSOFA 0.74 vs SIRS 0.71 (P<0.001). "
            "Sensitivity at 0.9 specificity: AI 71% vs qSOFA 42% vs SIRS 58%. "
            "Time to detection: AI 2.1h vs clinical recognition 4.8h (P<0.001). "
            "Conclusions: SEPTIS-AI provides superior early sepsis detection compared to qSOFA and SIRS "
            "in diverse ED populations, with 2.7h faster detection that may improve time-to-antibiotics."
        ),
    },
    {
        "pmid": "44012847", "title": "Procalcitonin-Guided Antibiotic Discontinuation in ICU: ProRATA 2 Trial",
        "authors": ["Bouadma L", "Luyt CE", "Tubach F", "Cracco C", "Alvarez A"],
        "journal": "Lancet Infectious Diseases", "journal_abbr": "Lancet Infect Dis",
        "year": "2024", "volume": "24", "issue": "11", "pages": "1228-1238",
        "doi": "10.1016/S1473-3099(24)00528-4", "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Procalcitonin/blood", "*Anti-Bacterial Agents/therapeutic use",
                       "*Antimicrobial Stewardship", "*Biomarkers/blood",
                       "Critical Care", "Intensive Care Units", "Humans"],
        "abstract": (
            "Background: PCT-guided antibiotic strategies reduce antibiotic exposure without worsening outcomes "
            "in respiratory infections; ICU data across all infection types are limited. "
            "Methods: 1,408 ICU patients with bacterial infection randomised to PCT-guided discontinuation "
            "(stop if PCT <0.5 mcg/L or decreased >80% from peak) vs standard (clinician-driven) duration. "
            "Results: Antibiotic exposure: PCT-guided 7.2 days vs standard 9.8 days (P<0.001). "
            "28-day mortality: PCT-guided 20.2% vs standard 21.4% (OR 0.93, non-inferiority P=0.001). "
            "Antibiotic-resistant organism emergence: PCT-guided 12% vs standard 19% (P=0.002). "
            "Conclusions: PCT-guided antibiotic discontinuation in ICU significantly reduces antibiotic exposure "
            "and resistance emergence without increasing mortality, supporting universal PCT-guided stewardship."
        ),
    },
]


def _parse_mesh(term: str):
    """Parse '*Descriptor/Qualifier' → (is_major, descriptor, qualifier)."""
    is_major = term.startswith("*")
    t = term.lstrip("*")
    if "/" in t:
        desc, qual = t.split("/", 1)
    else:
        desc, qual = t, ""
    return is_major, desc.strip(), qual.strip()


def _build_article(rec: dict) -> ET.Element:
    pa = ET.Element("PubmedArticle")
    mc = ET.SubElement(pa, "MedlineCitation", Status="MEDLINE", Owner="NLM")

    pmid_el = ET.SubElement(mc, "PMID", Version="1")
    pmid_el.text = rec["pmid"]

    art = ET.SubElement(mc, "Article", PubModel="Print")

    # Journal
    jrn = ET.SubElement(art, "Journal")
    ji = ET.SubElement(jrn, "JournalIssue", CitedMedium="Print")
    ET.SubElement(ji, "Volume").text = rec["volume"]
    ET.SubElement(ji, "Issue").text = rec["issue"]
    pd = ET.SubElement(ji, "PubDate")
    ET.SubElement(pd, "Year").text = str(rec["year"])
    ET.SubElement(jrn, "Title").text = rec["journal"]
    ET.SubElement(jrn, "ISOAbbreviation").text = rec["journal_abbr"]

    ET.SubElement(art, "ArticleTitle").text = rec["title"]

    pg = ET.SubElement(art, "Pagination")
    ET.SubElement(pg, "MedlinePgn").text = rec["pages"]

    abstract = ET.SubElement(art, "Abstract")
    ET.SubElement(abstract, "AbstractText").text = rec["abstract"]

    al = ET.SubElement(art, "AuthorList", CompleteYN="Y")
    for author_str in rec["authors"]:
        parts = author_str.rsplit(" ", 1)
        author = ET.SubElement(al, "Author", ValidYN="Y")
        ET.SubElement(author, "LastName").text = parts[0]
        if len(parts) > 1:
            ET.SubElement(author, "Initials").text = parts[1]

    ptl = ET.SubElement(art, "PublicationTypeList")
    ET.SubElement(ptl, "PublicationType").text = rec["publication_type"]

    # MeSH headings
    mhl = ET.SubElement(mc, "MeshHeadingList")
    for term_str in rec["mesh_terms"]:
        is_major, desc, qual = _parse_mesh(term_str)
        mh = ET.SubElement(mhl, "MeshHeading")
        dn = ET.SubElement(mh, "DescriptorName", MajorTopicYN="Y" if is_major else "N")
        dn.text = desc
        if qual:
            ET.SubElement(mh, "QualifierName").text = qual

    # Non-standard: evidence classification
    ET.SubElement(mc, "OtherID", Source="EvidenceLevel").text = rec["evidence_level"]
    ET.SubElement(mc, "OtherID", Source="EvidenceGrade").text = rec["evidence_grade"]

    # DOI
    pmd = ET.SubElement(pa, "PubmedData")
    ail = ET.SubElement(pmd, "ArticleIdList")
    ET.SubElement(ail, "ArticleId", IdType="pubmed").text = rec["pmid"]
    ET.SubElement(ail, "ArticleId", IdType="doi").text = rec["doi"]

    return pa


def write_files() -> None:
    root = ET.Element("PubmedArticleSet")
    for rec in _ABSTRACTS:
        root.append(_build_article(rec))

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")

    with open(_OUT_FILE, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

    print(f"research_corpus: {len(_ABSTRACTS)} abstracts → {_OUT_FILE}")


if __name__ == "__main__":
    write_files()
