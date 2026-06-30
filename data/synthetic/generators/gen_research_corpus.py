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
        "year": 2023, "volume": "24", "issue": "3", "pages": "289-301",
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
        "year": 2022, "volume": "81", "issue": "5", "pages": "1042-1055",
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
        "year": 2023, "volume": "52", "issue": "6", "pages": "878-890",
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
        "year": 2022, "volume": "279", "issue": "3", "pages": "442-451",
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
        "year": 2022, "volume": "28", "issue": "1", "pages": "89",
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
        "year": 2023, "volume": "19", "issue": "3", "pages": "211-219",
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
        "journal": "Lancet", "journal_abbr": "Lancet",
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
        "year": "2022", "volume": "17", "issue": "3", "pages": "328-340",
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
        "year": "2022", "volume": "184", "issue": "2", "pages": "189-198",
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
        "year": "2021", "volume": "391", "issue": "14", "pages": "1289-1301",
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
        "year": "2022", "volume": "331", "issue": "12", "pages": "1024-1034",
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
        "year": "2022", "volume": "78", "issue": "5", "pages": "612-622",
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
        "year": "2021", "volume": "47", "issue": "3", "pages": "442-450",
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
        "year": "2021", "volume": "166", "issue": "4", "pages": "748-758",
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
        "year": "2021", "volume": "390", "issue": "19", "pages": "1748-1758",
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
        "year": "2021", "volume": "403", "issue": "10428", "pages": "731-742",
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
        "journal": "JAMA", "journal_abbr": "JAMA",
        "year": "2022", "volume": "390", "issue": "22", "pages": "2048-2060",
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
        "year": "2021", "volume": "73", "issue": "6", "pages": "958-967",
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
        "year": "2021", "volume": "403", "issue": "10438", "pages": "1738-1748",
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
        "year": "2020", "volume": "76", "issue": "4", "pages": "548-560",
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
        "year": "2021", "volume": "184", "issue": "7", "pages": "768-778",
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
        "year": "2021", "volume": "24", "issue": "3", "pages": "289-299",
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
        "year": "2020", "volume": "331", "issue": "8", "pages": "652-662",
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
        "year": "2020", "volume": "79", "issue": "5", "pages": "1089-1100",
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
        "year": "2020", "volume": "83", "issue": "10", "pages": "982-994",
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
        "journal": "European Heart Journal", "journal_abbr": "Eur Heart J",
        "year": "2019", "volume": "391", "issue": "6", "pages": "528-540",
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
        "year": "2019", "volume": "143", "issue": "8", "pages": "741-751",
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
        "journal": "Alimentary Pharmacology & Therapeutics", "journal_abbr": "Aliment Pharmacol Ther",
        "year": "2019", "volume": "390", "issue": "8", "pages": "709-718",
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
        "year": "2022", "volume": "45", "issue": "9", "pages": "798-810",
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
        "year": "2022", "volume": "83", "issue": "4", "pages": "388-400",
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
        "year": "2020", "volume": "331", "issue": "16", "pages": "1382-1392",
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
        "year": "2020", "volume": "45", "issue": "21", "pages": "1892-1902",
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
        "year": "2019", "volume": "331", "issue": "11", "pages": "940-950",
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
        "year": "2019", "volume": "390", "issue": "17", "pages": "1548-1560",
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
        "year": "2020", "volume": "52", "issue": "4", "pages": "528-538",
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
        "year": "2020", "volume": "331", "issue": "4", "pages": "312-322",
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
        "year": "2020", "volume": "45", "issue": "13", "pages": "1122-1131",
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
        "journal": "Blood", "journal_abbr": "Blood",
        "year": "2019", "volume": "390", "issue": "11", "pages": "988-999",
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
        "journal": "Annals of Internal Medicine", "journal_abbr": "Ann Intern Med",
        "year": "2019", "volume": "390", "issue": "4", "pages": "324-336",
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
        "year": "2021", "volume": "9", "issue": "6", "pages": "512-524",
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
        "year": "2020", "volume": "184", "issue": "9", "pages": "1028-1038",
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
        "year": "2019", "volume": "24", "issue": "8", "pages": "882-892",
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
        "year": "2019", "volume": "79", "issue": "8", "pages": "1748-1758",
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
        "year": "2019", "volume": "79", "issue": "5", "pages": "442-452",
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

    # ── NEW BALANCED ADDITIONS (abstracts 61–80): fills missing pub types, topics, years ──

    {
        "pmid": "44100001",
        "title": "PD-1/PD-L1 Inhibitors as First-Line Therapy in Advanced Non-Small Cell Lung Cancer: Meta-Analysis of 18 Phase III Trials",
        "authors": ["Reck M", "Mok TSK", "Nishio M", "Socinski MA"],
        "journal": "JAMA Oncology", "journal_abbr": "JAMA Oncol",
        "year": 2022, "volume": "8", "issue": "6", "pages": "891-902",
        "doi": "10.1001/jamaoncol.2022.1047",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Carcinoma, Non-Small-Cell Lung/drug therapy",
            "*Programmed Cell Death 1 Receptor/antagonists & inhibitors",
            "*B7-H1 Antigen/antagonists & inhibitors",
            "Immune Checkpoint Inhibitors/therapeutic use",
            "Meta-Analysis as Topic", "Humans", "Survival Analysis",
        ],
        "abstract": (
            "Background: PD-1/PD-L1 inhibitors have transformed first-line management of advanced NSCLC. "
            "Comparative efficacy across agents and PD-L1 expression levels requires meta-analytic synthesis. "
            "Methods: We searched MEDLINE, Embase, and ClinicalTrials.gov for phase III RCTs comparing "
            "PD-1/PD-L1 inhibitors (± chemotherapy) to chemotherapy alone in treatment-naive advanced NSCLC. "
            "Eighteen trials (n=12,847 patients) met inclusion criteria. Network meta-analysis was performed. "
            "Results: PD-1/PD-L1 monotherapy improved OS versus chemotherapy in PD-L1 ≥50% tumours "
            "(HR 0.63, 95% CI 0.57-0.70). Combined chemo-immunotherapy improved OS regardless of PD-L1 level "
            "(HR 0.74, 95% CI 0.69-0.79). No significant difference between individual agents (pembrolizumab, "
            "nivolumab, atezolizumab) was detected (P-heterogeneity 0.41). Grade 3-4 immune-related adverse "
            "events occurred in 15.3% of immunotherapy-treated patients. "
            "Conclusions: PD-1/PD-L1 inhibition improves survival in advanced NSCLC; combined chemo-immunotherapy "
            "is preferred for PD-L1 <50% tumours. Agent choice should be guided by availability, toxicity profile, "
            "and tumour mutational burden testing."
        ),
    },
    {
        "pmid": "44100002",
        "title": "Real-World Outcomes of Trastuzumab Deruxtecan versus Trastuzumab Emtansine in HER2-Positive Metastatic Breast Cancer",
        "authors": ["Cortés J", "Kim SB", "Chung WP", "Im SA"],
        "journal": "Journal of Clinical Oncology", "journal_abbr": "J Clin Oncol",
        "year": 2021, "volume": "39", "issue": "18", "pages": "1987-1999",
        "doi": "10.1200/JCO.21.00892",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Breast Neoplasms/drug therapy",
            "*Receptor, ErbB-2/antagonists & inhibitors",
            "*Trastuzumab/therapeutic use",
            "Antineoplastic Agents, Immunological/therapeutic use",
            "Cohort Studies", "Treatment Outcome", "Humans", "Female",
        ],
        "abstract": (
            "Background: Trastuzumab deruxtecan (T-DXd) showed superior efficacy over trastuzumab emtansine "
            "(T-DM1) in the DESTINY-Breast03 trial; real-world data on unselected patients are limited. "
            "Methods: Retrospective cohort of 1,284 HER2+ metastatic breast cancer patients who received T-DXd "
            "(n=612) or T-DM1 (n=672) as second-line therapy across 28 oncology centres. Primary endpoint: "
            "real-world progression-free survival (rwPFS). "
            "Results: Median rwPFS: T-DXd 18.4 months vs T-DM1 7.1 months (HR 0.38, 95% CI 0.32-0.46, P<0.001). "
            "Objective response rate: T-DXd 72% vs T-DM1 34%. Interstitial lung disease (ILD) occurred in 11.4% "
            "of T-DXd patients (Grade 3-4: 2.8%). Treatment discontinuation due to toxicity: T-DXd 18% vs T-DM1 9%. "
            "Conclusions: T-DXd demonstrates markedly superior effectiveness over T-DM1 in real-world HER2+ "
            "metastatic breast cancer, confirming trial findings. ILD monitoring protocols are essential given the "
            "11% overall incidence observed in unselected patients."
        ),
    },
    {
        "pmid": "44100003",
        "title": "ESMO Clinical Practice Guidelines for Management of Immune-Related Adverse Events from Checkpoint Inhibitors: 2023 Update",
        "authors": ["Haanen J", "Carbonnel F", "Robert C", "Kerr KM"],
        "journal": "Annals of Oncology", "journal_abbr": "Ann Oncol",
        "year": 2023, "volume": "34", "issue": "9", "pages": "1034-1058",
        "doi": "10.1016/j.annonc.2023.06.001",
        "publication_type": "CLINICAL PRACTICE GUIDELINE",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Immune Checkpoint Inhibitors/adverse effects",
            "*Drug-Related Side Effects and Adverse Reactions/therapy",
            "Immunosuppressive Agents/therapeutic use",
            "Practice Guidelines as Topic", "Humans",
            "Neoplasms/drug therapy",
        ],
        "abstract": (
            "Background: Immune-related adverse events (irAEs) from checkpoint inhibitors affect 60-90% of patients "
            "and can be life-threatening. Standardised management guidance is needed across organ systems. "
            "Methods: ESMO multidisciplinary guideline committee reviewed evidence from prospective cohorts, "
            "pharmacovigilance registries, and expert consensus panels. Grading uses ESMO Scale of Clinical "
            "Actionability of molecular Targets (ESCAT). "
            "Recommendations: Grade 1 irAEs: continue immunotherapy with close monitoring and topical/supportive "
            "care. Grade 2: hold immunotherapy; start systemic corticosteroids (prednisone 0.5-1 mg/kg/day). "
            "Grade 3-4: permanently discontinue; high-dose IV methylprednisolone 1-2 mg/kg/day; specialist "
            "involvement mandatory. Steroid-refractory irAEs: infliximab (colitis, hepatitis) or mycophenolate "
            "(pneumonitis, hepatitis). Organ-specific algorithms provided for 18 irAE categories. "
            "Conclusions: Early recognition, graded corticosteroid therapy, and specialist co-management are the "
            "cornerstones of irAE management; permanent discontinuation is required for severe immune toxicity."
        ),
    },
    {
        "pmid": "44100004",
        "title": "High-Flow Nasal Cannula versus Standard Oxygen in Moderate Bronchiolitis: HFNC-BRONCH Randomised Trial",
        "authors": ["Franklin D", "Babl FE", "Schlapbach LJ", "Oakley E"],
        "journal": "Pediatrics", "journal_abbr": "Pediatrics",
        "year": 2020, "volume": "145", "issue": "5", "pages": "e20200-e20212",
        "doi": "10.1542/peds.2019-3811",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Bronchiolitis/therapy", "*Cannula",
            "*Oxygen Inhalation Therapy/methods",
            "Respiratory Syncytial Viruses", "Pediatric Emergency Medicine",
            "Humans", "Infant", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: High-flow nasal cannula (HFNC) is increasingly used for moderate bronchiolitis, "
            "but evidence for superiority over standard oxygen therapy (SOT) remains uncertain. "
            "Methods: Multicentre RCT in 22 paediatric emergency departments. Infants aged 0-12 months with "
            "moderate bronchiolitis (Respiratory Distress Assessment Instrument ≥4) randomised to HFNC "
            "(2 L/kg/min) or SOT (via nasal cannula or mask). Primary outcome: treatment failure within 24h. "
            "N=1,472 infants enrolled. "
            "Results: Treatment failure: HFNC 12% vs SOT 23% (RR 0.52, 95% CI 0.41-0.67, P<0.001). "
            "PICU escalation: HFNC 3.8% vs SOT 7.4% (P=0.002). Length of stay: HFNC 48h vs SOT 52h (P=0.09). "
            "No significant difference in intubation rates (0.9% vs 1.4%, P=0.31). "
            "Conclusions: HFNC significantly reduces treatment failure and PICU escalation in moderate bronchiolitis "
            "versus standard oxygen, supporting HFNC as first-line therapy in this population."
        ),
    },
    {
        "pmid": "44100005",
        "title": "Short versus Standard Antibiotic Duration for Febrile Urinary Tract Infection in Children: PEDS-UTI Prospective Cohort",
        "authors": ["Shaikh N", "Mattoo TK", "Keren R", "Ivanova A"],
        "journal": "JAMA Pediatrics", "journal_abbr": "JAMA Pediatr",
        "year": 2024, "volume": "178", "issue": "2", "pages": "143-152",
        "doi": "10.1001/jamapediatrics.2023.5921",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Urinary Tract Infections/drug therapy",
            "*Anti-Bacterial Agents/administration & dosage",
            "Febrile Neutropenia", "Vesico-Ureteral Reflux",
            "Treatment Outcome", "Humans", "Child",
        ],
        "abstract": (
            "Background: Standard antibiotic duration for paediatric febrile UTI is 7-14 days; shorter courses "
            "may reduce adverse effects without compromising efficacy. "
            "Methods: Prospective cohort of 2,184 children aged 2 months to 10 years with febrile UTI. "
            "Physicians prescribed short (3-5 days) or standard (7-14 days) oral antibiotics per clinical judgement. "
            "Primary outcome: UTI recurrence within 30 days and 12 months. "
            "Results: 30-day recurrence: short 4.8% vs standard 5.1% (aOR 0.94, 95% CI 0.62-1.42). "
            "12-month recurrence: short 18.4% vs standard 19.7% (aOR 0.93, 95% CI 0.72-1.20). "
            "Adverse effects (diarrhoea, rash): short 8.2% vs standard 15.6% (P<0.001). "
            "Vesicoureteral reflux grade did not modify the treatment-duration effect (P-interaction 0.62). "
            "Conclusions: Short antibiotic courses are non-inferior to standard duration for paediatric febrile UTI "
            "with significantly fewer adverse effects, supporting 3-5 day therapy in uncomplicated cases."
        ),
    },
    {
        "pmid": "44100006",
        "title": "Nirsevimab for RSV Prevention in Infants and Toddlers: Systematic Review and Meta-Analysis of Phase 2-3 Trials",
        "authors": ["Hammitt LL", "Dagan R", "Yuan Y", "Gottlieb SL"],
        "journal": "Lancet Child & Adolescent Health", "journal_abbr": "Lancet Child Adolesc Health",
        "year": 2022, "volume": "6", "issue": "12", "pages": "859-870",
        "doi": "10.1016/S2352-4642(22)00286-4",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Respiratory Syncytial Virus Infections/prevention & control",
            "*Antibodies, Monoclonal, Humanized/therapeutic use",
            "Respiratory Syncytial Viruses/immunology",
            "Immunization, Passive", "Meta-Analysis as Topic",
            "Humans", "Infant",
        ],
        "abstract": (
            "Background: Nirsevimab is a long-acting monoclonal antibody targeting RSV pre-fusion protein F. "
            "Its efficacy across infant subgroups requires systematic synthesis. "
            "Methods: Systematic review of phase 2-3 trials. Five trials (n=5,492 infants) met inclusion. "
            "Primary endpoint: medically attended RSV lower respiratory tract infection (LRTI). "
            "Results: Nirsevimab reduced medically attended RSV LRTI by 74% (RR 0.26, 95% CI 0.19-0.36) "
            "versus placebo. Hospitalisation for RSV: RR 0.21 (95% CI 0.13-0.34). Efficacy was consistent "
            "in preterm infants (RR 0.27) and infants with congenital heart disease (RR 0.23). A single "
            "injection provides protection for the entire RSV season (5-6 months). Adverse events similar "
            "to placebo. "
            "Conclusions: Nirsevimab provides robust, season-long RSV protection with a single dose in infants "
            "including high-risk subgroups. These data support universal neonatal nirsevimab immunisation programs."
        ),
    },
    {
        "pmid": "44100007",
        "title": "Aspirin for Prevention of Preeclampsia in High-Risk Pregnancy: PREVECLAMP Randomised Trial",
        "authors": ["Rolnik DL", "Wright D", "Poon LC", "O'Gorman N"],
        "journal": "Lancet", "journal_abbr": "Lancet",
        "year": 2021, "volume": "397", "issue": "10285", "pages": "1693-1703",
        "doi": "10.1016/S0140-6736(21)00781-3",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Pre-Eclampsia/prevention & control",
            "*Aspirin/therapeutic use",
            "Platelet Aggregation Inhibitors/therapeutic use",
            "Pregnant Women", "High Risk Pregnancy",
            "Randomized Controlled Trials as Topic", "Humans", "Female",
        ],
        "abstract": (
            "Background: Low-dose aspirin reduces preeclampsia risk in high-risk pregnancies. Optimal timing, "
            "dose, and patient selection using first-trimester screening require prospective validation. "
            "Methods: Double-blind RCT enrolling 1,776 women with singleton pregnancy and high first-trimester "
            "risk of preterm preeclampsia (combined algorithm ≥1:100). Randomised to aspirin 150 mg/day from "
            "11-14 weeks until 36 weeks or placebo. Primary outcome: preterm preeclampsia <37 weeks. "
            "Results: Preterm preeclampsia: aspirin 1.6% vs placebo 4.3% (OR 0.38, 95% CI 0.20-0.74, P=0.004). "
            "Term preeclampsia: aspirin 2.3% vs placebo 2.9% (OR 0.78, P=0.29). No significant difference in "
            "fetal/neonatal adverse outcomes. Aspirin adherence >90% associated with greater protection. "
            "Conclusions: 150 mg aspirin initiated in the first trimester halves preterm preeclampsia in "
            "screen-positive women, supporting universal first-trimester risk screening and aspirin prophylaxis."
        ),
    },
    {
        "pmid": "44100008",
        "title": "Gestational Diabetes Management Intensity and Adverse Perinatal Outcomes: Population Cohort of 87,000 Deliveries",
        "authors": ["Crowther CA", "Hiller JE", "Moss JR", "McPhee AJ"],
        "journal": "Obstetrics & Gynecology", "journal_abbr": "Obstet Gynecol",
        "year": 2020, "volume": "135", "issue": "4", "pages": "889-900",
        "doi": "10.1097/AOG.0000000000003779",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Diabetes, Gestational/therapy",
            "*Pregnancy Outcome",
            "Blood Glucose/metabolism",
            "Macrosomia/prevention & control",
            "Cohort Studies", "Humans", "Female", "Pregnancy",
        ],
        "abstract": (
            "Background: Gestational diabetes mellitus (GDM) management intensity varies widely; the dose-response "
            "relationship between glycaemic control tightness and perinatal outcomes is incompletely characterised. "
            "Methods: Population-based cohort of 87,241 singleton deliveries to women with GDM from 2014-2019 "
            "across 42 obstetric units. Categorised by management intensity: diet-only, oral agents, insulin. "
            "Primary outcomes: large-for-gestational-age (LGA), birth trauma, neonatal hypoglycaemia. "
            "Results: LGA incidence: diet-only 18.4%, oral agents 16.1%, insulin 12.8% (P-trend <0.001). "
            "Neonatal hypoglycaemia: diet-only 3.2%, oral agents 6.8%, insulin 9.1% (P-trend <0.001). "
            "Birth trauma: no significant difference across groups (P=0.41). Time-in-range (3.9-7.8 mmol/L) "
            ">70% was the strongest predictor of normal birth weight (OR 0.44, P<0.001). "
            "Conclusions: Tighter glycaemic control reduces LGA but increases neonatal hypoglycaemia risk in GDM. "
            "Time-in-range optimisation, rather than pharmacological escalation alone, should guide management."
        ),
    },
    {
        "pmid": "44100009",
        "title": "Prevention and Management of Postpartum Haemorrhage: FIGO Updated Clinical Practice Guidelines 2023",
        "authors": ["Bonet M", "Oladapo OT", "Souza JP", "Gülmezoglu AM"],
        "journal": "American Journal of Obstetrics & Gynecology", "journal_abbr": "Am J Obstet Gynecol",
        "year": 2023, "volume": "229", "issue": "3", "pages": "456-480",
        "doi": "10.1016/j.ajog.2023.04.012",
        "publication_type": "CLINICAL PRACTICE GUIDELINE",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Postpartum Hemorrhage/prevention & control",
            "*Postpartum Hemorrhage/therapy",
            "Oxytocin/therapeutic use",
            "Uterotonic Agents/therapeutic use",
            "Practice Guidelines as Topic", "Humans", "Female",
        ],
        "abstract": (
            "Background: Postpartum haemorrhage (PPH) remains the leading cause of maternal mortality globally. "
            "Evidence-based bundles require updated synthesis incorporating heat-stable carbetocin and tranexamic acid "
            "data. Methods: FIGO guidelines committee conducted systematic reviews and GRADE evidence assessment. "
            "Key recommendations: (1) Active management of third stage of labour (AMTSL) with uterotonics for all "
            "deliveries (strong recommendation, high-quality evidence). (2) Oxytocin 10 IU IM/IV remains first-line "
            "uterotonic; heat-stable carbetocin 100 mcg IM is an equivalent alternative in settings without cold chain. "
            "(3) Tranexamic acid 1 g IV within 3 hours of PPH onset reduces PPH mortality (RR 0.81, NNT 267). "
            "(4) Uterine massage after oxytocin is no longer recommended (increases maternal discomfort without benefit). "
            "(5) Non-pneumatic anti-shock garment as bridge therapy in resource-limited settings. "
            "Conclusions: AMTSL with oxytocin or carbetocin, plus early tranexamic acid for established PPH, "
            "forms the evidence-based foundation of PPH prevention and management worldwide."
        ),
    },
    {
        "pmid": "44100010",
        "title": "Venlafaxine versus Sertraline for First-Episode Major Depressive Disorder: COMPARE-MDD Randomised Trial",
        "authors": ["Cipriani A", "Furukawa TA", "Salanti G", "Chaimani A"],
        "journal": "JAMA Psychiatry", "journal_abbr": "JAMA Psychiatry",
        "year": 2022, "volume": "79", "issue": "8", "pages": "771-781",
        "doi": "10.1001/jamapsychiatry.2022.1534",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Depressive Disorder, Major/drug therapy",
            "*Venlafaxine Hydrochloride/therapeutic use",
            "*Sertraline/therapeutic use",
            "Antidepressive Agents/therapeutic use",
            "Serotonin-Norepinephrine Reuptake Inhibitors",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: SSRIs and SNRIs are both recommended first-line treatments for major depressive disorder (MDD). "
            "Head-to-head comparisons in first-episode MDD are limited. "
            "Methods: Double-blind RCT. 1,102 adults with first-episode MDD randomised to venlafaxine 75-225 mg/day "
            "or sertraline 50-200 mg/day for 24 weeks. Primary outcome: response (≥50% PHQ-9 reduction) at 8 weeks. "
            "Results: Response at 8 weeks: venlafaxine 58% vs sertraline 54% (RR 1.07, 95% CI 0.97-1.19, P=0.17). "
            "Remission at 24 weeks: 46% vs 43% (P=0.31). Discontinuation due to adverse effects: venlafaxine 14% "
            "vs sertraline 9% (P=0.004), driven by nausea (18% vs 12%) and sweating (16% vs 8%). "
            "Conclusions: Venlafaxine and sertraline have equivalent antidepressant efficacy in first-episode MDD. "
            "Sertraline's superior tolerability supports SSRI as preferred first-line therapy, with SNRI reserved "
            "for non-response or comorbid anxiety with somatic symptoms."
        ),
    },
    {
        "pmid": "44100011",
        "title": "Long-Acting Injectable Antipsychotics and Relapse Prevention in Schizophrenia: 5-Year Population Cohort",
        "authors": ["Tiihonen J", "Mittendorfer-Rutz E", "Majak M", "Mehtälä J"],
        "journal": "Lancet Psychiatry", "journal_abbr": "Lancet Psychiatry",
        "year": 2019, "volume": "6", "issue": "3", "pages": "223-233",
        "doi": "10.1016/S2215-0366(18)30480-0",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Antipsychotic Agents/administration & dosage",
            "*Schizophrenia/drug therapy",
            "*Secondary Prevention",
            "Delayed-Action Preparations/therapeutic use",
            "Medication Adherence", "Cohort Studies",
            "Humans", "Recurrence",
        ],
        "abstract": (
            "Background: Medication non-adherence is the leading cause of schizophrenia relapse. Long-acting "
            "injectable antipsychotics (LAIs) may reduce relapse rates compared to oral formulations. "
            "Methods: Nationwide cohort of 29,823 patients with first-episode schizophrenia in Finland (2000-2017). "
            "Time-to-psychiatric-rehospitalisation compared between LAI and oral antipsychotic users using within-subject "
            "analysis to control for selection bias. "
            "Results: LAIs reduced rehospitalisation risk by 30% compared to equivalent oral agents "
            "(HR 0.70, 95% CI 0.63-0.77). Aripiprazole LAI showed the greatest effect (HR 0.55, 95% CI 0.43-0.72). "
            "LAI advantage was most pronounced in patients with prior non-adherence history (HR 0.58). "
            "Clozapine showed the lowest overall rehospitalisation rate but is restricted to treatment-resistant cases. "
            "Conclusions: LAIs reduce schizophrenia relapse risk by 30% versus oral equivalents. Their underuse in "
            "first-episode schizophrenia represents an important clinical quality gap warranting systematic reassessment "
            "of prescribing practices."
        ),
    },
    {
        "pmid": "44100012",
        "title": "Cognitive Behavioural Therapy versus Pharmacotherapy for Generalised Anxiety Disorder: Network Meta-Analysis of 44 Trials",
        "authors": ["Bandelow B", "Michaelis S", "Wedekind D"],
        "journal": "Psychological Medicine", "journal_abbr": "Psychol Med",
        "year": 2021, "volume": "51", "issue": "11", "pages": "1869-1881",
        "doi": "10.1017/S0033291721000580",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Anxiety Disorders/therapy",
            "*Cognitive Behavioral Therapy",
            "*Anti-Anxiety Agents/therapeutic use",
            "Selective Serotonin Reuptake Inhibitors/therapeutic use",
            "Network Meta-Analysis", "Humans",
            "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Both cognitive behavioural therapy (CBT) and pharmacotherapy are effective for generalised "
            "anxiety disorder (GAD). Direct comparative evidence is heterogeneous; network meta-analysis can resolve "
            "indirect comparisons. "
            "Methods: Network meta-analysis of 44 RCTs (n=7,284 patients) comparing CBT, SSRIs, SNRIs, buspirone, "
            "pregabalin, or placebo. Primary outcome: HAM-A response at 12 weeks. "
            "Results: All active interventions outperformed placebo. CBT (SMD -0.82, 95% CI -1.02 to -0.62) "
            "and SNRIs (SMD -0.79, 95% CI -0.93 to -0.64) had the largest effects. SSRIs: SMD -0.72. "
            "Combination CBT + SSRI did not significantly outperform CBT alone (SMD -0.12, P=0.38). "
            "Relapse at 12 months: CBT 22%, SSRI 38%, SNRI 41% (P<0.001 for CBT vs medication). "
            "Conclusions: CBT and pharmacotherapy are comparably effective acutely for GAD; CBT provides superior "
            "relapse prevention at 12 months. Combination therapy offers minimal additional acute benefit. "
            "Patient preference and resource availability should guide first-line choice."
        ),
    },
    {
        "pmid": "44100013",
        "title": "Enhanced Recovery After Surgery for Colorectal Resection: ERAS-COLON Multicentre Randomised Trial",
        "authors": ["Gustafsson UO", "Scott MJ", "Schwenk W", "Demartines N"],
        "journal": "British Journal of Surgery", "journal_abbr": "Br J Surg",
        "year": 2020, "volume": "107", "issue": "8", "pages": "1035-1046",
        "doi": "10.1002/bjs.11540",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Colorectal Surgery/methods",
            "*Enhanced Recovery After Surgery",
            "*Postoperative Care/methods",
            "Length of Stay", "Complications, Postoperative",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Enhanced Recovery After Surgery (ERAS) protocols reduce length of stay in colorectal surgery, "
            "but compliance with individual protocol elements and their relative contributions are poorly characterised. "
            "Methods: Cluster-randomised trial across 36 hospitals. High-compliance ERAS (≥14/16 elements implemented) "
            "versus standard ERAS (<14 elements) for elective colorectal resection. 2,847 patients enrolled. "
            "Primary outcome: length of stay. "
            "Results: High-compliance ERAS: median LOS 3 days vs standard ERAS 5 days (P<0.001). "
            "30-day complications: 22% vs 31% (RR 0.71, 95% CI 0.62-0.81). Readmission: 8% vs 11% (P=0.04). "
            "Key elements with greatest individual impact: multimodal analgesia (OR 0.61), early mobilisation "
            "(OR 0.67), and oral carbohydrate loading (OR 0.74). "
            "Conclusions: Full ERAS protocol compliance reduces LOS by 2 days and complications by 29% versus "
            "partial implementation. Audit and feedback on compliance should be routine in surgical units."
        ),
    },
    {
        "pmid": "44100014",
        "title": "Surgical Site Infection Prevention Bundle in Abdominal Surgery: Outcomes from 22 Academic Centres",
        "authors": ["Ban KA", "Minei JP", "Laronga C", "Harbrecht BG"],
        "journal": "JAMA Surgery", "journal_abbr": "JAMA Surg",
        "year": 2019, "volume": "154", "issue": "1", "pages": "21-29",
        "doi": "10.1001/jamasurg.2018.3817",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Surgical Wound Infection/prevention & control",
            "*Patient Care Bundles",
            "*Abdomen/surgery",
            "Antibiotic Prophylaxis", "Wound Closure Techniques",
            "Cohort Studies", "Humans", "Quality Improvement",
        ],
        "abstract": (
            "Background: Surgical site infections (SSIs) affect 2-5% of abdominal procedures and cause significant "
            "morbidity. Bundled prevention strategies have heterogeneous evidence across surgical subtypes. "
            "Methods: Prospective cohort of 18,442 abdominal surgeries (colectomy, hysterectomy, hernia repair, "
            "cholecystectomy) at 22 academic centres before (2013-2015) and after (2016-2019) implementation of "
            "an 8-element SSI prevention bundle (antibiotic timing, wound irrigation, glove change, normothermia, "
            "glucose control, wound closure optimisation, skin preparation, drain avoidance). "
            "Results: SSI rate: pre-bundle 4.8% vs post-bundle 2.9% (OR 0.59, 95% CI 0.51-0.68, P<0.001). "
            "Greatest reductions in colectomy (7.1%→4.2%) and hysterectomy (3.8%→1.9%). Cost per SSI prevented: "
            "$4,200 saved in downstream treatment costs per bundle implementation cost of $180/case. "
            "Conclusions: A systematic SSI prevention bundle reduces SSI rates by 40% across abdominal surgical "
            "subtypes with favourable cost-effectiveness. Universal bundle implementation should be a quality standard."
        ),
    },
    {
        "pmid": "44100015",
        "title": "Delayed Trocar-Site Hernia Following Laparoscopic Surgery: Case Series of 18 Patients and Review of the Literature",
        "authors": ["Tonouchi H", "Ohmori Y", "Kobayashi M", "Kusunoki M"],
        "journal": "Journal of Gastrointestinal Surgery", "journal_abbr": "J Gastrointest Surg",
        "year": 2023, "volume": "27", "issue": "4", "pages": "712-719",
        "doi": "10.1007/s11605-023-05621-3",
        "publication_type": "CASE SERIES",
        "evidence_level": "Level IV", "evidence_grade": "Grade C",
        "mesh_terms": [
            "*Hernia, Ventral/etiology",
            "*Laparoscopy/adverse effects",
            "*Surgical Wound Dehiscence/etiology",
            "Postoperative Complications", "Case Reports",
            "Humans", "Adult",
        ],
        "abstract": (
            "Background: Trocar-site hernia (TSH) is an uncommon but clinically significant complication of "
            "laparoscopic surgery. Risk factors and optimal prevention strategies for delayed presentations "
            "(>30 days post-operatively) are not well characterised. "
            "Methods: Retrospective case series of 18 consecutive patients presenting with TSH more than 30 days "
            "post-laparoscopy at a single tertiary referral centre over 8 years. All cases reviewed for port site "
            "characteristics, surgical technique, patient factors, and management outcomes. "
            "Results: Median time to presentation: 14 months (range 1-48 months). Predominant port size involved: "
            "10-12 mm (83%). Sites: umbilical 67%, epigastric 22%, lateral 11%. Predisposing factors: obesity "
            "(BMI >30) in 78%, wound infection history 33%, immunosuppression 22%. Fourteen patients managed "
            "laparoscopically; 4 required open repair for incarceration. No recurrences at median 24-month follow-up. "
            "Conclusions: Delayed TSH most commonly involves 10-12 mm umbilical ports in obese patients. Fascial "
            "closure of all ports ≥10 mm is supported; routine follow-up imaging for high-risk patients should be "
            "considered."
        ),
    },
    {
        "pmid": "44100016",
        "title": "Long-Term Cardiovascular and Metabolic Outcomes After Bariatric Surgery in Morbid Obesity: 10-Year Prospective Cohort",
        "authors": ["Sjöström L", "Peltonen M", "Jacobson P", "Ahlin S"],
        "journal": "Lancet Diabetes & Endocrinology", "journal_abbr": "Lancet Diabetes Endocrinol",
        "year": 2022, "volume": "10", "issue": "7", "pages": "512-523",
        "doi": "10.1016/S2213-8587(22)00119-4",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Bariatric Surgery",
            "*Obesity, Morbid/surgery",
            "*Cardiovascular Diseases/prevention & control",
            "Weight Loss", "Diabetes Mellitus, Type 2/prevention & control",
            "Cohort Studies", "Humans", "Prospective Studies",
        ],
        "abstract": (
            "Background: Short-term metabolic benefits of bariatric surgery are established; 10-year cardiovascular "
            "outcomes in real-world populations require prospective data. "
            "Methods: Prospective cohort of 4,047 obese patients (BMI ≥35) undergoing bariatric surgery matched 1:2 "
            "to obese controls receiving conventional treatment, followed for 10 years. Surgical procedures: RYGB "
            "(51%), sleeve gastrectomy (35%), adjustable gastric band (14%). Primary outcome: composite of MACE. "
            "Results: MACE: surgery 9.1% vs controls 14.8% (HR 0.61, 95% CI 0.52-0.71). Type 2 DM remission at "
            "10 years: 36% (surgery) vs 3% (controls). Weight loss maintenance: surgery -18% vs controls +2% of "
            "baseline weight. Late complications requiring re-operation: 12.4%. Nutritional deficiencies: 28% "
            "required supplementation escalation beyond standard protocols. "
            "Conclusions: Bariatric surgery provides sustained 10-year reductions in cardiovascular events and "
            "diabetes in morbidly obese patients, though late complications and nutritional monitoring remain "
            "important clinical considerations."
        ),
    },
    {
        "pmid": "44100017",
        "title": "Vitamin D Supplementation and Acute Respiratory Tract Infections: Individual Patient Data Meta-Analysis of 25 Randomised Trials",
        "authors": ["Martineau AR", "Jolliffe DA", "Hooper RL", "Greenberg L"],
        "journal": "BMJ", "journal_abbr": "BMJ",
        "year": 2019, "volume": "356", "issue": "", "pages": "i6583",
        "doi": "10.1136/bmj.i6583",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Vitamin D/therapeutic use",
            "*Respiratory Tract Infections/prevention & control",
            "*Dietary Supplements",
            "Vitamin D Deficiency/drug therapy",
            "Meta-Analysis as Topic", "Humans",
            "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Vitamin D has immunomodulatory properties that may protect against acute respiratory tract "
            "infections (ARTIs). Individual trials are underpowered; individual patient data (IPD) meta-analysis "
            "can assess effect modifiers. "
            "Methods: IPD meta-analysis of 25 RCTs (n=11,321 participants) comparing vitamin D supplementation "
            "to placebo for ARTI prevention. Primary outcome: proportion experiencing at least one ARTI. "
            "Results: Vitamin D reduced ARTI risk (OR 0.88, 95% CI 0.81-0.96). Effect strongest in participants "
            "with baseline 25-OH vitamin D <25 nmol/L (OR 0.58, 95% CI 0.40-0.82). Daily/weekly dosing superior "
            "to bolus dosing (OR 0.81 vs 0.97 for daily vs bolus, P-interaction 0.004). No reduction in severe "
            "ARTI or hospitalisation. "
            "Conclusions: Vitamin D supplementation provides modest protection against ARTI, predominantly in "
            "vitamin D-deficient individuals using daily or weekly dosing. Universal ARTI prophylaxis is not "
            "supported; targeted supplementation for deficient patients is recommended."
        ),
    },
    {
        "pmid": "44100018",
        "title": "Clinical Practice Guideline for Opioid Therapy in Chronic Non-Cancer Pain: 2021 Revision",
        "authors": ["Dowell D", "Haegerich TM", "Chou R"],
        "journal": "Annals of Internal Medicine", "journal_abbr": "Ann Intern Med",
        "year": 2021, "volume": "174", "issue": "9", "pages": "1280-1293",
        "doi": "10.7326/M21-1skipped",
        "publication_type": "CLINICAL PRACTICE GUIDELINE",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Analgesics, Opioid/therapeutic use",
            "*Chronic Pain/drug therapy",
            "*Opioid-Related Disorders/prevention & control",
            "Drug Prescriptions/standards",
            "Practice Guidelines as Topic", "Humans",
            "Risk Assessment",
        ],
        "abstract": (
            "Background: Opioid prescribing for chronic non-cancer pain (CNCP) is associated with dependency, "
            "overdose risk, and diversion. Evidence-based guidance is needed to balance analgesia with harm reduction. "
            "Methods: Systematic evidence review and expert panel consensus for primary care opioid prescribing. "
            "Guideline covers initiation, dosage, duration, risk mitigation, and tapering. "
            "Key recommendations: (1) Non-opioid therapies (NSAIDs, SNRIs, CBT, physical therapy) are preferred "
            "first-line for CNCP. (2) If opioids prescribed, use lowest effective dose; avoid escalation above "
            "50 MME/day without specialist review. (3) Avoid concurrent benzodiazepine prescribing (OR for overdose "
            "death 3.86). (4) Review opioid risk with validated tool (ORT) before initiation. (5) Naloxone "
            "co-prescription for patients on ≥50 MME/day or concurrent CNS depressants. (6) Structured tapering "
            "for patients wishing to discontinue. "
            "Conclusions: Opioid therapy for CNCP requires individualised risk-benefit assessment; non-opioid "
            "alternatives should be exhausted before initiation, and ongoing prescribing requires regular structured "
            "review."
        ),
    },
    {
        "pmid": "44100019",
        "title": "Anti-NMDA Receptor Encephalitis Presenting as New-Onset Refractory Status Epilepticus: Diagnostic Pitfalls and Immunotherapy Response",
        "authors": ["Titulaer MJ", "McCracken L", "Gabilondo I", "Armangué T"],
        "journal": "Neurology", "journal_abbr": "Neurology",
        "year": 2024, "volume": "102", "issue": "3", "pages": "e208194",
        "doi": "10.1212/WNL.0000000000208194",
        "publication_type": "CASE REPORT",
        "evidence_level": "Level IV", "evidence_grade": "Grade C",
        "mesh_terms": [
            "*Anti-N-Methyl-D-Aspartate Receptor Encephalitis/diagnosis",
            "*Anti-N-Methyl-D-Aspartate Receptor Encephalitis/therapy",
            "*Status Epilepticus/etiology",
            "Autoantibodies/blood", "Immunotherapy",
            "Humans", "Female", "Young Adult",
        ],
        "abstract": (
            "Background: Anti-NMDAR encephalitis is the most common autoimmune encephalitis and can present with "
            "new-onset refractory status epilepticus (NORSE), which may delay autoimmune diagnosis in favour of "
            "infectious or structural aetiologies. "
            "Case: A 24-year-old female presented with NORSE after a 3-day prodrome of headache and behavioural "
            "change. MRI unremarkable; CSF showed mild lymphocytosis. Extensive infectious work-up negative. "
            "Anti-NMDAR antibodies detected in CSF on day 8 (serum negative). EEG demonstrated delta brush pattern. "
            "Ovarian teratoma identified on pelvic MRI. Management: IV methylprednisolone, IVIG, and teratoma "
            "resection. Significant neurological improvement by day 28; near-complete recovery at 6 months. "
            "Discussion: NORSE as the initial presentation of anti-NMDAR encephalitis is under-recognised. CSF "
            "antibody testing is mandatory even with negative serum results. Delta brush on EEG is pathognomonic. "
            "Conclusions: Anti-NMDAR encephalitis should be considered in all NORSE cases; early immunotherapy "
            "and teratoma resection are associated with favourable outcomes."
        ),
    },
    {
        "pmid": "44100020",
        "title": "Spontaneous Coronary Artery Dissection in a Peripartum Patient: Multivessel Involvement and Conservative Management Outcomes",
        "authors": ["Hayes SN", "Kim ESH", "Saw J", "Adlam D"],
        "journal": "BMJ Case Reports", "journal_abbr": "BMJ Case Rep",
        "year": 2023, "volume": "16", "issue": "5", "pages": "e254821",
        "doi": "10.1136/bcr-2023-254821",
        "publication_type": "CASE REPORT",
        "evidence_level": "Level IV", "evidence_grade": "Grade C",
        "mesh_terms": [
            "*Coronary Vessel Anomalies/diagnosis",
            "*Vascular Diseases/pathology",
            "*Peripartum Period",
            "Coronary Angiography", "Conservative Treatment",
            "Humans", "Female", "Postpartum Period",
        ],
        "abstract": (
            "Background: Spontaneous coronary artery dissection (SCAD) accounts for up to 35% of myocardial "
            "infarctions in women under 50 and is over-represented in the peripartum period. Multivessel SCAD "
            "carries particular management complexity given the risk of iatrogenic propagation during percutaneous "
            "intervention. "
            "Case: A 32-year-old G2P2 woman presented 8 days postpartum with STEMI. Emergent coronary angiography "
            "revealed dissection of the LAD (type 2, IMH pattern) with extension to the diagonal branch. A second "
            "dissection of the proximal RCA was incidentally identified. LVEF 38% on presentation. Conservative "
            "management pursued given haemodynamic stability — no PCI performed. Beta-blocker and ACE inhibitor "
            "initiated. LVEF recovered to 55% at 6 weeks; both dissections healed on repeat angiography at 4 months. "
            "Discussion: Conservative management is preferred in haemodynamically stable multivessel peripartum SCAD; "
            "PCI carries high risk of propagation. Pregnancy-associated hormonal and haemodynamic stress are the "
            "dominant precipitants. Conclusions: Peripartum SCAD should be suspected in young women presenting with "
            "ACS; conservative management with close monitoring achieves favourable outcomes in most cases."
        ),
    },
    {
        "pmid": "44200001",
        "title": "Intravenous Alteplase within 4.5 Hours for Ischaemic Stroke with Unknown Onset Time",
        "authors": ["Ma H", "Campbell BCV", "Parsons MW", "Christensen S"],
        "journal": "Brain",
        "journal_abbr": "Brain",
        "year": 2019, "volume": "142", "issue": "3", "pages": "710-721",
        "doi": "10.1093/brain/awz009",
        "publication_type": "RANDOMISED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Stroke/drug therapy", "*Tissue Plasminogen Activator/administration & dosage",
                       "*Thrombolytic Therapy", "Time-to-Treatment"],
        "topic": "neurology",
        "abstract": "Background: Intravenous alteplase use in ischaemic stroke with unknown onset time is controversial. Methods: Patients with wake-up stroke and DWI-FLAIR mismatch were randomised to alteplase or placebo within 4.5h of awakening. Results: Alteplase significantly improved functional outcome (modified Rankin ≤1: 53.3% vs 41.8%, OR 1.61). Symptomatic intracranial haemorrhage occurred in 3.6% vs 0.4%. Conclusion: DWI-FLAIR mismatch selects patients for late-window thrombolysis with net clinical benefit.",
    },
    {
        "pmid": "44200002",
        "title": "Lecanemab in Early Alzheimer's Disease: 18-Month Efficacy and Safety",
        "authors": ["van Dyck CH", "Swanson CJ", "Aisen P", "Bateman RJ"],
        "journal": "JAMA Neurology",
        "journal_abbr": "JAMA Neurol",
        "year": 2019, "volume": "80", "issue": "2", "pages": "117-128",
        "doi": "10.1001/jamaneurol.2022.4672",
        "publication_type": "RANDOMISED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Alzheimer Disease/drug therapy", "*Amyloid beta-Peptides", "*Antibodies, Monoclonal, Humanized",
                       "Cognitive Dysfunction/prevention & control"],
        "topic": "neurology",
        "abstract": "Background: Anti-amyloid immunotherapy represents a disease-modifying approach to early Alzheimer's disease. Methods: 1,795 patients with early AD were randomised to lecanemab 10mg/kg biweekly or placebo for 18 months. Results: Lecanemab reduced CDR-SB decline by 27% (p<0.001); amyloid-related imaging abnormalities occurred in 21.3% of treated patients. Conclusion: Lecanemab slows clinical progression in early AD but requires careful safety monitoring for ARIA.",
    },
    {
        "pmid": "44200003",
        "title": "Psilocybin-Assisted Therapy for Treatment-Resistant Depression: Randomised Trial",
        "authors": ["Carhart-Harris R", "Giribaldi B", "Watts R", "Baker-Jones M"],
        "journal": "British Journal of Psychiatry",
        "journal_abbr": "Br J Psychiatry",
        "year": 2019, "volume": "218", "issue": "4", "pages": "215-223",
        "doi": "10.1192/bjp.2020.225",
        "publication_type": "RANDOMISED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Psilocybin/therapeutic use", "*Depressive Disorder, Treatment-Resistant/therapy",
                       "*Serotonin Receptor Agonists/therapeutic use", "Antidepressants/therapeutic use"],
        "topic": "psychiatry",
        "abstract": "Background: Treatment-resistant depression affects 30% of patients with MDD; novel interventions are needed. Methods: 59 patients with TRD were randomised to psilocybin 25mg, 10mg, or 1mg (control) with psychological support. Results: Psilocybin 25mg produced significant MADRS reduction at week 3 (NNT=4); response rate 37% vs 18% for control. Conclusion: High-dose psilocybin with psychological support is effective and acceptable for treatment-resistant depression.",
    },
    {
        "pmid": "44200004",
        "title": "Safety and Immunogenicity of Meningococcal B Vaccine in Adolescents: 4-Year Follow-Up",
        "authors": ["Bexsero Study Group", "Findlow J", "Borrow R", "Snape MD"],
        "journal": "Archives of Disease in Childhood",
        "journal_abbr": "Arch Dis Child",
        "year": 2019, "volume": "104", "issue": "6", "pages": "528-535",
        "doi": "10.1136/archdischild-2018-315673",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Meningococcal Vaccines/immunology", "*Adolescent", "*Neisseria meningitidis, Serogroup B",
                       "Vaccination/adverse effects"],
        "topic": "paediatrics",
        "abstract": "Background: Long-term immunogenicity data for the meningococcal B vaccine (4CMenB) in adolescents are limited. Methods: 1,040 adolescents vaccinated with 4CMenB were followed for 4 years with hSBA titres at 12, 24, and 48 months. Results: hSBA titres remained above protective threshold in 72-89% of participants at 4 years depending on strain; booster dose restored titres to baseline. Conclusion: 4CMenB provides durable protection through adolescence with a single booster dose.",
    },
    {
        "pmid": "44200005",
        "title": "Dupilumab for Moderate-to-Severe Atopic Dermatitis: Real-World 52-Week Outcomes",
        "authors": ["Thyssen JP", "de Bruin-Weller M", "Paller AS", "Wollenberg A"],
        "journal": "British Journal of Dermatology",
        "journal_abbr": "Br J Dermatol",
        "year": 2019, "volume": "181", "issue": "3", "pages": "567-578",
        "doi": "10.1111/bjd.17902",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Dermatitis, Atopic/drug therapy", "*Antibodies, Monoclonal, Humanized/therapeutic use",
                       "*Biological Therapy", "Treatment Outcome"],
        "topic": "dermatology",
        "abstract": "Background: Phase 3 trials of dupilumab for atopic dermatitis may not reflect real-world heterogeneity. Methods: 1,284 adult AD patients treated with dupilumab in 12 European centres were followed for 52 weeks (IGA, EASI, DLQI outcomes). Results: EASI-75 achieved in 64% at week 16, maintained in 71% at week 52; conjunctivitis occurred in 14.8%. Conclusion: Real-world dupilumab outcomes mirror trial data with slightly higher conjunctivitis rates in clinical practice.",
    },
    {
        "pmid": "44200006",
        "title": "DMARD Combination vs Monotherapy in Early Rheumatoid Arthritis: 5-Year Outcomes",
        "authors": ["Smolen JS", "Landewe R", "Bijlsma J", "Burmester G"],
        "journal": "Annals of the Rheumatic Diseases",
        "journal_abbr": "Ann Rheum Dis",
        "year": 2019, "volume": "78", "issue": "9", "pages": "1205-1216",
        "doi": "10.1136/annrheumdis-2019-215428",
        "publication_type": "RANDOMISED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Arthritis, Rheumatoid/drug therapy", "*Antirheumatic Agents/therapeutic use",
                       "*Methotrexate/therapeutic use", "Drug Therapy, Combination"],
        "topic": "rheumatology",
        "abstract": "Background: Optimal DMARD strategy for early RA influences long-term joint damage. Methods: 848 early RA patients (<2 years) were randomised to methotrexate monotherapy vs combination (MTX+sulfasalazine+HCQ) with treat-to-target protocol for 5 years. Results: Combination therapy achieved remission faster (28 weeks vs 42 weeks) but 5-year DAS remission rates were similar (58% vs 55%). Conclusion: Treat-to-target with MTX monotherapy achieves equivalent 5-year outcomes to initial combination DMARD therapy.",
    },
    {
        "pmid": "44200007",
        "title": "Functional Endoscopic Sinus Surgery vs Medical Management for Chronic Rhinosinusitis: RCT",
        "authors": ["Smith KA", "Orlandi RR", "Rudmik L"],
        "journal": "Ear Nose Throat Journal",
        "journal_abbr": "Ear Nose Throat J",
        "year": 2019, "volume": "98", "issue": "7", "pages": "412-421",
        "doi": "10.1177/0145561319849701",
        "publication_type": "RANDOMISED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Rhinosinusitis/surgery", "*Endoscopy/methods", "*Sinusitis/therapy",
                       "*Nasal Polyps/surgery", "Treatment Outcome"],
        "topic": "ent",
        "abstract": "Background: FESS vs maximal medical therapy for chronic rhinosinusitis with nasal polyps remains debated. Methods: 220 adult CRSwNP patients refractory to intranasal steroids were randomised to FESS+post-op steroids vs continuing medical management for 12 months. Results: FESS arm: SNOT-22 improved 24 points vs 11 points (p<0.001); polyp recurrence 28% vs 46% at 12 months. Conclusion: FESS provides superior symptom control and polyp clearance compared to medical management alone in CRSwNP.",
    },
    {
        "pmid": "44200008",
        "title": "Early Palliative Care Integration for Advanced Cancer: Systematic Review and Meta-Analysis",
        "authors": ["Haun MW", "Estel S", "Rücker G", "Friederich HC"],
        "journal": "Palliative Medicine",
        "journal_abbr": "Palliat Med",
        "year": 2019, "volume": "31", "issue": "9", "pages": "781-800",
        "doi": "10.1177/0269216317706614",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Palliative Care/methods", "*Neoplasms/therapy", "*Early Medical Intervention",
                       "Quality of Life", "Patient Satisfaction"],
        "topic": "palliative",
        "abstract": "Background: Early palliative care integration may improve outcomes beyond late-stage symptom management. Methods: Systematic review and meta-analysis of 10 RCTs (n=2,454) comparing early PC integration vs standard oncology care in advanced cancer. Results: Early PC significantly improved quality of life (SMD 0.35) and reduced aggressive end-of-life care; modest survival benefit in 3 trials (HR 0.83). Conclusion: Early palliative care integration improves QOL and reduces futile interventions without compromising survival.",
    },
    {
        "pmid": "44200009",
        "title": "Generalised Anxiety Disorder Prevalence and Treatment Gap in Primary Care: Cross-Sectional Study",
        "authors": ["Ruscio AM", "Hallion LS", "Lim CCW", "Aguilar-Gaxiola S"],
        "journal": "JAMA Psychiatry",
        "journal_abbr": "JAMA Psychiatry",
        "year": 2019, "volume": "74", "issue": "5", "pages": "435-446",
        "doi": "10.1001/jamapsychiatry.2017.0056",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Anxiety Disorders/epidemiology", "*Primary Health Care", "*Mental Health Services/utilization",
                       "Prevalence", "Healthcare Disparities"],
        "topic": "psychiatry",
        "abstract": "Background: GAD is highly prevalent but undertreated in primary care settings. Methods: Cross-sectional survey of 150,000 adults across 26 WHO World Mental Health surveys assessed GAD prevalence and treatment-seeking in primary care settings. Results: GAD lifetime prevalence 3.7% globally; only 26.9% received minimally adequate treatment; treatment gap widest in low-income countries (87.8%). Conclusion: Substantial global treatment gap for GAD persists; primary care integration is essential for closing the gap.",
    },
    {
        "pmid": "44200010",
        "title": "Childhood Obesity Intervention in Primary Care: Cluster RCT",
        "authors": ["Danielsson P", "Kowalski J", "Ekblom Ö", "Marcus C"],
        "journal": "Paediatrics",
        "journal_abbr": "Pediatrics",
        "year": 2019, "volume": "143", "issue": "2", "pages": "e20182093",
        "doi": "10.1542/peds.2018-2093",
        "publication_type": "RANDOMISED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Pediatric Obesity/therapy", "*Primary Health Care", "*Family Therapy",
                       "Body Mass Index", "Life Style/classification"],
        "topic": "paediatrics",
        "abstract": "Background: Primary care-based family interventions for childhood obesity lack robust evidence. Methods: 585 children aged 4-11 with obesity were randomised to a 12-month intensive family-based primary care programme vs standard care. Results: BMI-SDS reduced significantly in intervention (-0.29 vs -0.12, p=0.003); physical activity and dietary quality improved. Conclusion: Intensive family-based obesity management in primary care achieves meaningful weight reduction in school-age children.",
    },
    {
        "pmid": "44200011",
        "title": "Sodium Valproate in Women of Childbearing Age: Neurodevelopmental Outcomes in Exposed Offspring",
        "authors": ["Bröker V", "Meador KJ", "Baker GA", "Bromley RL"],
        "journal": "Lancet Neurology",
        "journal_abbr": "Lancet Neurol",
        "year": 2020, "volume": "19", "issue": "3", "pages": "231-242",
        "doi": "10.1016/S1474-4422(19)30489-0",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Valproic Acid/adverse effects", "*Prenatal Exposure Delayed Effects",
                       "*Neurodevelopmental Disorders", "*Anticonvulsants/adverse effects"],
        "topic": "neurology",
        "abstract": "Background: Valproate exposure in utero is associated with neurodevelopmental harm; exact dose-response is unclear. Methods: Prospective cohort of 1,802 children born to women with epilepsy; neurodevelopmental assessment at 3 and 6 years. Results: Valproate-exposed children had mean IQ 10 points lower than lamotrigine-exposed (p<0.001); dose-response confirmed — doses >1000mg/day highest risk. Conclusion: Valproate in pregnancy carries dose-dependent neurodevelopmental risk; alternative ASMs should be prioritised in women of childbearing potential.",
    },
    {
        "pmid": "44200012",
        "title": "Cognitive-Behavioural Therapy for Schizophrenia: Network Meta-Analysis",
        "authors": ["Jauhar S", "McKenna PJ", "Radua J", "Fung E"],
        "journal": "JAMA Psychiatry",
        "journal_abbr": "JAMA Psychiatry",
        "year": 2020, "volume": "71", "issue": "7", "pages": "692-704",
        "doi": "10.1001/jamapsychiatry.2014.1337",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Schizophrenia/therapy", "*Cognitive Behavioral Therapy",
                       "*Psychotherapy", "*Antipsychotic Agents/therapeutic use"],
        "topic": "psychiatry",
        "abstract": "Background: The efficacy of CBT for schizophrenia remains debated, particularly for positive symptoms. Methods: Network meta-analysis of 34 RCTs (n=3,572) comparing CBT, supportive therapy, treatment as usual, and pharmacotherapy for schizophrenia. Results: CBT produced modest but significant reductions in positive symptoms (SMD -0.25) and overall symptoms; effects did not differ by blinding status. Conclusion: CBT for schizophrenia has a small but consistent positive effect on symptom burden as an adjunct to antipsychotic medication.",
    },
    {
        "pmid": "44200013",
        "title": "Hepatitis C Virus Elimination with Pangenotypic Direct-Acting Antivirals: Population Cohort",
        "authors": ["Innes H", "Dillon JF", "Lazarus JV", "Buti M"],
        "journal": "Journal of Hepatology",
        "journal_abbr": "J Hepatol",
        "year": 2020, "volume": "72", "issue": "5", "pages": "860-869",
        "doi": "10.1016/j.jhep.2020.01.027",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Hepatitis C/drug therapy", "*Antiviral Agents/therapeutic use",
                       "*Hepacivirus", "Sustained Virologic Response"],
        "topic": "hepatology",
        "abstract": "Background: Pangenotypic DAA regimens have transformed HCV treatment; real-world cure rates in diverse populations are critical for elimination targets. Methods: 18,742 HCV patients treated with sofosbuvir-based pangenotypic regimens in 9 European countries were analysed for SVR12. Results: Overall SVR12 96.8%; lowest in genotype 3 cirrhotic patients (89.2%); no significant disparities by ethnicity or socioeconomic status. Conclusion: Pangenotypic DAAs achieve near-universal HCV cure across genotypes and patient populations, supporting WHO elimination targets.",
    },
    {
        "pmid": "44200014",
        "title": "Effect of High-Dose Vitamin D Supplementation on Fracture Risk: RCT",
        "authors": ["LeBlanc ES", "Zakher B", "Daeges M", "Pappas M"],
        "journal": "Journal of the American Academy of Dermatology",
        "journal_abbr": "J Am Acad Dermatol",
        "year": 2020, "volume": "70", "issue": "4", "pages": "551-560",
        "doi": "10.1016/j.jaad.2013.10.052",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": ["*Vitamin D/therapeutic use", "*Fractures, Bone/prevention & control",
                       "*Osteoporosis/prevention & control", "Dietary Supplements"],
        "topic": "geriatrics",
        "abstract": "Background: Vitamin D supplementation recommendations vary widely in older adults. Methods: Systematic review of 15 RCTs (n=19,642) comparing vitamin D supplementation doses and fracture outcomes in adults ≥60 years. Results: Vitamin D alone did not reduce fracture risk (RR 0.98); combined calcium+vitamin D reduced hip fracture in institutionalised older adults (RR 0.73). Conclusion: Vitamin D alone is insufficient for fracture prevention; combined supplementation benefits institutionalised elderly but not community-dwelling adults.",
    },
    {
        "pmid": "44200015",
        "title": "Neonatal Outcomes After Prolonged Premature Rupture of Membranes Before 26 Weeks: Cohort Study",
        "authors": ["Kibel M", "Asztalos E", "Barrett J", "Dunn MS"],
        "journal": "Archives of Disease in Childhood",
        "journal_abbr": "Arch Dis Child",
        "year": 2020, "volume": "100", "issue": "3", "pages": "F230-F237",
        "doi": "10.1136/archdischild-2014-307487",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Fetal Membranes, Premature Rupture", "*Gestational Age",
                       "*Infant, Premature", "*Infant Mortality", "Perinatal Care"],
        "topic": "paediatrics",
        "abstract": "Background: PPROM before 26 weeks gestation carries high perinatal morbidity and mortality. Methods: Retrospective cohort of 228 pregnancies with PPROM at 14-25+6 weeks; outcomes tracked to NICU discharge. Results: Survival to discharge 49.8% overall; survival improved with gestational age at rupture (23 weeks 68% vs 18 weeks 12%); pulmonary hypoplasia occurred in 34%. Conclusion: PPROM before 26 weeks carries high mortality; gestational age at rupture and membrane-to-delivery interval are key prognostic determinants.",
    },
    {
        "pmid": "44200016",
        "title": "Clozapine-Associated Neutropenia: Frequency and Risk Factors in a National Cohort",
        "authors": ["Atake K", "Yoshimura R", "Hori H", "Katsuki A"],
        "journal": "British Journal of Psychiatry",
        "journal_abbr": "Br J Psychiatry",
        "year": 2020, "volume": "214", "issue": "1", "pages": "45-52",
        "doi": "10.1192/bjp.2018.207",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Clozapine/adverse effects", "*Neutropenia/chemically induced",
                       "*Antipsychotic Agents/adverse effects", "*Schizophrenia/drug therapy"],
        "topic": "psychiatry",
        "abstract": "Background: Clozapine-associated neutropenia requires mandatory monitoring but rates and predictors in diverse populations are not well characterised. Methods: National registry study of 8,422 clozapine-treated patients with mandatory blood count monitoring from 2000-2018. Results: Neutropenia occurred in 2.8%; agranulocytosis in 0.38%; highest risk in patients of Ashkenazi Jewish descent and with viral infections. Conclusion: Clozapine neutropenia is infrequent but mandates vigilant monitoring; ethnicity and intercurrent illness are modifiable risk factors.",
    },
    {
        "pmid": "44200017",
        "title": "Skin Cancer Prevention: Evidence from Sunscreen RCTs — Systematic Review",
        "authors": ["Green AC", "Williams GM", "Logan V", "Strutton GM"],
        "journal": "Journal of the American Academy of Dermatology",
        "journal_abbr": "J Am Acad Dermatol",
        "year": 2020, "volume": "60", "issue": "2", "pages": "262-269",
        "doi": "10.1016/j.jaad.2008.07.064",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Skin Neoplasms/prevention & control", "*Sunscreening Agents/therapeutic use",
                       "*Carcinoma, Squamous Cell/prevention & control", "Melanoma/prevention & control"],
        "topic": "dermatology",
        "abstract": "Background: Regular sunscreen use may reduce skin cancer incidence; long-term randomised evidence was lacking. Methods: Systematic review of 4 RCTs (n=3,218) testing daily SPF15+ sunscreen vs discretionary use with 4-10 year follow-up. Results: Daily sunscreen reduced invasive melanoma incidence by 50% (OR 0.50) and SCC by 40%; effect stronger in high UV-index environments. Conclusion: Daily broad-spectrum sunscreen significantly reduces melanoma and SCC risk, supporting population-level public health recommendations.",
    },
    {
        "pmid": "44200018",
        "title": "Biologic Therapy Switching in Psoriatic Arthritis: Real-World Registry Analysis",
        "authors": ["Gottlieb AB", "Strand V", "Kishimoto M", "McInnes IB"],
        "journal": "Annals of the Rheumatic Diseases",
        "journal_abbr": "Ann Rheum Dis",
        "year": 2020, "volume": "79", "issue": "6", "pages": "768-777",
        "doi": "10.1136/annrheumdis-2019-216754",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Arthritis, Psoriatic/drug therapy", "*Biological Products/therapeutic use",
                       "*Tumor Necrosis Factor Inhibitors/therapeutic use", "Drug Substitution"],
        "topic": "rheumatology",
        "abstract": "Background: Drug switching is common in PsA biologic therapy; outcomes after first and subsequent switches are incompletely characterised. Methods: CORRONA PsA registry analysis of 1,842 patients on first biologic and 624 patients on second biologic after inadequate TNFi response. Results: ACR20 response 56% on first biologic vs 41% on second biologic (p=0.003); IL-17A inhibitors demonstrated superior response after TNFi failure vs second TNFi. Conclusion: Second-line IL-17A inhibitors outperform a second TNFi after primary TNFi failure in PsA.",
    },
    {
        "pmid": "44200019",
        "title": "Opioid Prescribing in Palliative Care: Safety of Dose Escalation for Refractory Pain",
        "authors": ["Caraceni A", "Hanks G", "Kaasa S", "Bennett MI"],
        "journal": "Journal of Pain and Symptom Management",
        "journal_abbr": "J Pain Symptom Manage",
        "year": 2020, "volume": "46", "issue": "2", "pages": "230-243",
        "doi": "10.1016/j.jpainsymman.2013.02.014",
        "publication_type": "CLINICAL PRACTICE GUIDELINE",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": ["*Palliative Care/methods", "*Opioid Analgesics/administration & dosage",
                       "*Cancer Pain/drug therapy", "Practice Guidelines as Topic"],
        "topic": "palliative",
        "abstract": "Background: Guidance on safe opioid dose escalation in cancer-related refractory pain is needed. Methods: EAPC expert panel review and consensus of evidence from 68 RCTs and observational studies; GRADE methodology applied. Results: Strong recommendations for oral morphine as first-line opioid; dose titration by 25-33% per step; evidence for opioid rotation reduces adverse effects with inadequate analgesia. Conclusion: Systematic opioid titration and rotation based on EAPC guidelines optimises analgesia with acceptable adverse effect burden in advanced cancer.",
    },
    {
        "pmid": "44200020",
        "title": "Epilepsy Surgery Outcomes in Drug-Resistant Temporal Lobe Epilepsy: 10-Year Cohort",
        "authors": ["Wiebe S", "Blume WT", "Girvin JP", "Eliasziw M"],
        "journal": "Lancet Neurology",
        "journal_abbr": "Lancet Neurol",
        "year": 2020, "volume": "12", "issue": "8", "pages": "789-798",
        "doi": "10.1016/S1474-4422(13)70105-8",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": ["*Epilepsy, Temporal Lobe/surgery", "*Drug Resistant Epilepsy/surgery",
                       "*Neurosurgical Procedures/methods", "Seizures/prevention & control"],
        "topic": "neurology",
        "abstract": "Background: Long-term outcomes after temporal lobe epilepsy surgery for drug-resistant epilepsy remain variable. Methods: Prospective 10-year cohort of 412 patients undergoing temporal lobectomy or selective amygdalohippocampectomy for drug-resistant TLE. Results: Engel class I seizure-free outcome 65% at 5 years, declining to 52% at 10 years; neuropsychological decline occurred in 18%. Conclusion: TLE surgery provides durable seizure freedom in over half of drug-resistant patients, justifying early surgical referral when medical therapy fails.",
    },
    {
        "pmid": "44200061",
        "title": "AI-Based Diagnostic Support for Diabetic Retinopathy Screening in Primary Care: Prospective Observational Study",
        "authors": ["Abramoff MD", "Lavin PT", "Birch M", "Shah N"],
        "journal": "npj Digital Medicine",
        "journal_abbr": "npj Digit Med",
        "year": 2023, "volume": "6", "issue": "1", "pages": "42",
        "doi": "10.1038/s41746-023-00789-3",
        "publication_type": "OBSERVATIONAL STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Diabetic Retinopathy/diagnosis",
            "*Artificial Intelligence",
            "*Mass Screening/methods",
            "Primary Health Care", "Deep Learning",
            "Sensitivity and Specificity", "Humans",
        ],
        "abstract": (
            "Background: AI-based diabetic retinopathy (DR) detection may extend screening capacity in "
            "primary care settings where ophthalmologists are unavailable. "
            "Methods: Prospective observational study across 30 primary care clinics; 22,384 patients with "
            "diabetes underwent autonomous AI grading (IDx-DR) with ophthalmologist adjudication for positives. "
            "Results: AI sensitivity for more-than-mild DR: 91.3% (95% CI 88.6-93.7%); specificity 91.8%; "
            "positive referral rate 11.4%; mean time-to-result 23 seconds. Ophthalmologist agreement with AI "
            "grade: 94.2% (kappa 0.88). Screening uptake increased by 38% versus prior year's manual scheduling. "
            "Conclusion: Autonomous AI grading achieves high sensitivity and specificity for DR in unselected "
            "primary care patients and significantly increases screening throughput without specialist bottleneck."
        ),
    },
    {
        "pmid": "44200062",
        "title": "Telehealth versus In-Person Follow-Up for Chronic Heart Failure: 12-Month Randomised Controlled Trial",
        "authors": ["Lam CSP", "Teng THK", "Tay WT", "Anand IS"],
        "journal": "Journal of Medical Internet Research",
        "journal_abbr": "J Med Internet Res",
        "year": 2024, "volume": "26", "issue": "", "pages": "e51203",
        "doi": "10.2196/51203",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Heart Failure/therapy",
            "*Telemedicine",
            "*Ambulatory Care/methods",
            "Patient Satisfaction", "Hospitalisation",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Telehealth follow-up for chronic heart failure (CHF) may maintain outcomes while "
            "reducing patient travel burden and clinic congestion. "
            "Methods: 612 stable CHF patients (NYHA II-III, EF <45%) randomised 1:1 to monthly telehealth "
            "video consultations or standard in-person outpatient review for 12 months; primary outcome was "
            "composite of HF hospitalisation or all-cause death. "
            "Results: Primary outcome: telehealth 18.2% vs in-person 19.7% (HR 0.92, 95% CI 0.70-1.20, "
            "non-inferiority P=0.002); patient satisfaction higher in telehealth group (NPS +24 vs +8, P<0.001); "
            "medication optimisation visits were equivalent between arms (2.1 vs 2.3 per patient, P=0.31). "
            "Conclusion: Telehealth follow-up is non-inferior to in-person care for stable CHF and improves "
            "patient satisfaction, supporting hybrid telehealth models as standard practice."
        ),
    },
    {
        "pmid": "44200063",
        "title": "Electronic Health Record Sepsis Alerts with Machine Learning Re-Calibration: Impact on Time-to-Antibiotics",
        "authors": ["Ginestra JC", "Giannini HM", "Schweickert WD", "Meadows L"],
        "journal": "Lancet Digital Health",
        "journal_abbr": "Lancet Digit Health",
        "year": 2023, "volume": "5", "issue": "10", "pages": "e681-e691",
        "doi": "10.1016/S2589-7500(23)00150-2",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Sepsis/diagnosis",
            "*Decision Support Systems, Clinical",
            "*Electronic Health Records",
            "Machine Learning", "Anti-Bacterial Agents/therapeutic use",
            "Time-to-Treatment", "Humans",
        ],
        "abstract": (
            "Background: EHR sepsis alerts suffer from high false-positive rates; ML re-calibration may "
            "improve specificity without sacrificing sensitivity. "
            "Methods: Pre-post cohort at a 900-bed academic medical centre comparing a rule-based SIRS/Sepsis-2 "
            "alert (pre) to an ML-recalibrated gradient-boosting alert (post) over 24 months each; 84,000 admissions. "
            "Results: False-positive alert rate fell from 64% to 38% (P<0.001); sensitivity for Sepsis-3 criteria "
            "maintained at 89%; median time-to-antibiotic order fell from 3.8h to 2.6h (P<0.001); 30-day mortality "
            "in alerted patients fell from 14.1% to 11.8% (aOR 0.82, P=0.04). "
            "Conclusion: ML-recalibrated EHR sepsis alerts substantially reduce false-positive burden and are "
            "associated with faster antibiotic administration and lower mortality."
        ),
    },
    {
        "pmid": "44200064",
        "title": "Global Burden of Antimicrobial Resistance in Gram-Negative Bloodstream Infections: 2023 Systematic Review",
        "authors": ["Murray CJ", "Ikuta KS", "Sharara F", "Swetschinski L"],
        "journal": "Emerging Infectious Diseases",
        "journal_abbr": "Emerg Infect Dis",
        "year": 2023, "volume": "29", "issue": "8", "pages": "1-14",
        "doi": "10.3201/eid2908.221913",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Drug Resistance, Multiple, Bacterial",
            "*Bacteremia/microbiology",
            "*Gram-Negative Bacteria/drug effects",
            "Global Health", "Anti-Bacterial Agents/therapeutic use",
            "Systematic Review as Topic", "Humans",
        ],
        "abstract": (
            "Background: Antimicrobial resistance (AMR) in gram-negative bloodstream infections is a growing "
            "threat; updated global burden estimates are needed to guide policy. "
            "Methods: Systematic review and meta-analysis of 412 studies (2012-2022) reporting AMR prevalence "
            "and attributable mortality for Enterobacterales, Pseudomonas aeruginosa, and Acinetobacter baumannii "
            "BSIs across 110 countries; standardised to Global Burden of Disease 2019 population denominators. "
            "Results: AMR-attributable deaths estimated at 1.27 million annually (95% UI 0.91-1.71 million); "
            "carbapenem-resistant Acinetobacter baumannii had highest attributable mortality (OR 2.82); "
            "low- and middle-income countries bore 75% of the burden; ESBL-producing Enterobacterales prevalence "
            "increased from 18% (2012) to 34% (2022). "
            "Conclusion: AMR in gram-negative BSI kills over one million people annually and is rising; accelerated "
            "stewardship, novel agent development, and infection-control investment are urgent global health imperatives."
        ),
    },
    {
        "pmid": "44200065",
        "title": "Shorter Versus Longer Duration of Rifampicin-Based Regimens for Drug-Susceptible Pulmonary Tuberculosis: TRUNCATE-TB Randomised Trial",
        "authors": ["Gillespie SH", "Crook AM", "McHugh TD", "Mendel CM"],
        "journal": "International Journal of Antimicrobial Agents",
        "journal_abbr": "Int J Antimicrob Agents",
        "year": 2024, "volume": "63", "issue": "4", "pages": "107063",
        "doi": "10.1016/j.ijantimicag.2024.107063",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Tuberculosis, Pulmonary/drug therapy",
            "*Rifampin/therapeutic use",
            "*Antitubercular Agents/administration & dosage",
            "Drug Administration Schedule",
            "Treatment Outcome", "Recurrence", "Humans",
        ],
        "abstract": (
            "Background: Standard 6-month TB treatment (2HRZE/4HR) is burdensome; shorter regimens may "
            "improve adherence and programme outcomes. "
            "Methods: Open-label RCT across 12 sites in Africa and Asia; 804 adults with drug-susceptible "
            "pulmonary TB randomised to truncated 4-month regimen (2HRZE/2HR) or standard 6-month regimen; "
            "primary endpoint: unfavourable outcome (treatment failure, relapse, or death) at 18 months. "
            "Results: Unfavourable outcome: 4-month 19.4% vs 6-month 11.6% (risk difference +7.8%, 95% CI "
            "+3.1 to +12.5, non-inferiority not met); relapse drove the difference (12.8% vs 5.9%); "
            "adverse events leading to discontinuation lower in 4-month arm (4.2% vs 7.8%). "
            "Conclusion: The 4-month rifampicin-based regimen does not achieve non-inferiority versus standard "
            "therapy; 6-month treatment remains the evidence-based standard for drug-susceptible pulmonary TB."
        ),
    },
    {
        "pmid": "44200066",
        "title": "Seasonal Malaria Chemoprevention with Sulfadoxine-Pyrimethamine plus Amodiaquine in Sub-Saharan Africa: Individual Patient Data Meta-Analysis",
        "authors": ["Cissé B", "Sokhna C", "Boulanger D", "Milet J"],
        "journal": "Emerging Infectious Diseases",
        "journal_abbr": "Emerg Infect Dis",
        "year": 2023, "volume": "29", "issue": "11", "pages": "2183-2195",
        "doi": "10.3201/eid2911.230344",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Malaria/prevention & control",
            "*Pyrimethamine/therapeutic use",
            "*Sulfadoxine/therapeutic use",
            "Amodiaquine/therapeutic use", "Chemoprevention",
            "Seasons", "Africa South of the Sahara", "Humans", "Child",
        ],
        "abstract": (
            "Background: Seasonal malaria chemoprevention (SMC) with SP+AQ reduces malaria in the Sahel; "
            "impact on mortality and resistance requires updated synthesis. "
            "Methods: Individual patient data meta-analysis of 8 RCTs (n=18,402 children under 5) conducted "
            "across Mali, Senegal, Burkina Faso, and Niger; outcomes included clinical malaria, severe malaria, "
            "anaemia, and all-cause mortality. "
            "Results: SMC reduced clinical malaria by 75% (RR 0.25, 95% CI 0.21-0.30); severe malaria by 73% "
            "(RR 0.27, 95% CI 0.19-0.39); all-cause mortality by 26% (RR 0.74, 95% CI 0.59-0.93); "
            "SP resistance markers (dhps K540E) did not attenuate SMC efficacy in available analyses. "
            "Conclusion: SMC with SP+AQ provides substantial protection against clinical and severe malaria in "
            "children under 5 in the Sahel and should be scaled up as a cornerstone of malaria control."
        ),
    },
    {
        "pmid": "44200067",
        "title": "Circulating Tumour DNA as a Predictive Biomarker for Immunotherapy Response in Advanced Melanoma: Prospective Cohort",
        "authors": ["Marsavela G", "Ioannidis LJ", "Drucker AM", "McArthur GA"],
        "journal": "Clinical Cancer Research",
        "journal_abbr": "Clin Cancer Res",
        "year": 2024, "volume": "30", "issue": "7", "pages": "1421-1432",
        "doi": "10.1158/1078-0432.CCR-23-2847",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Melanoma/drug therapy",
            "*Circulating Tumor DNA/blood",
            "*Immune Checkpoint Inhibitors/therapeutic use",
            "Biomarkers, Tumor/blood", "Prognosis",
            "Cohort Studies", "Humans",
        ],
        "abstract": (
            "Background: Liquid biopsy via circulating tumour DNA (ctDNA) may predict immunotherapy response "
            "earlier than radiographic assessment in advanced melanoma. "
            "Methods: Prospective cohort of 318 patients with advanced melanoma commencing anti-PD-1 therapy; "
            "ctDNA measured at baseline, 6 weeks, and 12 weeks; radiographic assessment at 12 weeks; primary "
            "endpoint: correlation between ctDNA dynamics and 12-month progression-free survival. "
            "Results: ctDNA clearance at 6 weeks predicted 12-month PFS with AUROC 0.84 vs imaging AUROC 0.78 "
            "(P=0.03); 6-week ctDNA clearance identified responders 6 weeks earlier than standard imaging; "
            "patients with ctDNA clearance had median PFS 22.4 months vs 4.8 months in non-clearers (HR 0.24). "
            "Conclusion: Early ctDNA clearance is a superior early predictor of immunotherapy benefit compared "
            "to standard imaging in advanced melanoma, supporting integration of liquid biopsy into response "
            "assessment workflows."
        ),
    },
    {
        "pmid": "44200068",
        "title": "Precision Oncology Tumour Board Outcomes: Impact of Molecular Profiling on Treatment Decisions and Survival",
        "authors": ["Schwaederle M", "Zhao M", "Lee JJ", "Lazar V"],
        "journal": "Nature Medicine",
        "journal_abbr": "Nat Med",
        "year": 2023, "volume": "29", "issue": "9", "pages": "2183-2194",
        "doi": "10.1038/s41591-023-02459-3",
        "publication_type": "OBSERVATIONAL STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Precision Medicine",
            "*Neoplasms/genetics",
            "*Antineoplastic Agents/therapeutic use",
            "Molecular Targeted Therapy", "Biomarkers, Tumor",
            "Survival Analysis", "Humans",
        ],
        "abstract": (
            "Background: Molecular tumour boards (MTBs) aim to translate genomic profiling into actionable "
            "treatment decisions, but their impact on real-world survival is incompletely characterised. "
            "Methods: Observational study of 1,872 patients with advanced solid tumours discussed at an MTB "
            "across 18 cancer centres; actionable alteration identified in 47%; genotype-matched therapy "
            "recommended in 31%; primary outcome was overall survival by matched-therapy receipt. "
            "Results: Patients receiving genotype-matched therapy had median OS of 18.6 months vs 11.2 months "
            "for unmatched (HR 0.61, 95% CI 0.52-0.71, P<0.001); benefit observed across tumour types; "
            "MTB recommendation changed treating oncologist's plan in 38% of cases reviewed. "
            "Conclusion: Precision oncology MTBs improve overall survival in advanced solid tumours when "
            "actionable alterations are identified and matched therapy is delivered, justifying systematic "
            "molecular profiling and multidisciplinary tumour board review."
        ),
    },
    {
        "pmid": "44200069",
        "title": "Metabolic Side Effects of Second-Generation Antipsychotics in Schizophrenia: 2-Year Randomised Comparison",
        "authors": ["Lieberman JA", "Stroup TS", "McEvoy JP", "Swartz MS"],
        "journal": "Psychological Medicine",
        "journal_abbr": "Psychol Med",
        "year": 2024, "volume": "54", "issue": "3", "pages": "612-624",
        "doi": "10.1017/S0033291723002847",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Antipsychotic Agents/adverse effects",
            "*Schizophrenia/drug therapy",
            "*Metabolic Syndrome/chemically induced",
            "Weight Gain/drug effects",
            "Blood Glucose/drug effects", "Humans",
            "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Second-generation antipsychotics (SGAs) differ in their metabolic adverse effect "
            "profiles; head-to-head 2-year data in schizophrenia are limited. "
            "Methods: 886 patients with schizophrenia stabilised on any SGA randomised to continue current "
            "agent or switch to aripiprazole, quetiapine, olanzapine, or ziprasidone; metabolic outcomes "
            "assessed at 6, 12, and 24 months. "
            "Results: Weight gain at 24 months: olanzapine +6.4 kg, quetiapine +4.1 kg, aripiprazole +0.8 kg, "
            "ziprasidone -0.3 kg (P<0.001 across groups); new-onset metabolic syndrome: olanzapine 28%, "
            "quetiapine 21%, aripiprazole 9%, ziprasidone 7%; psychiatric relapse rates did not differ "
            "significantly between agents (P=0.18). "
            "Conclusion: Metabolic risk profiles differ substantially across SGAs; aripiprazole and ziprasidone "
            "are preferred when metabolic risk is a clinical priority without sacrificing antipsychotic efficacy."
        ),
    },
    {
        "pmid": "44200070",
        "title": "Cognitive Behavioural Therapy for Insomnia in Cancer Survivors: Multisite Randomised Trial",
        "authors": ["Espie CA", "Fleming L", "Cassidy J", "Samuel L"],
        "journal": "Psychological Medicine",
        "journal_abbr": "Psychol Med",
        "year": 2023, "volume": "53", "issue": "14", "pages": "6642-6653",
        "doi": "10.1017/S0033291722003847",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Sleep Initiation and Maintenance Disorders/therapy",
            "*Cognitive Behavioral Therapy",
            "*Cancer Survivors",
            "Fatigue/therapy", "Quality of Life",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Insomnia is highly prevalent in cancer survivors and impairs quality of life; "
            "CBT for insomnia (CBT-I) is effective in general populations but evidence in cancer survivors "
            "is limited. "
            "Methods: 432 cancer survivors (mixed tumour types, >3 months post-active treatment) with DSM-5 "
            "insomnia disorder randomised to 6-session CBT-I or sleep hygiene education control; primary "
            "outcome: Insomnia Severity Index (ISI) at 6 weeks. "
            "Results: ISI reduction at 6 weeks: CBT-I -8.4 vs control -3.1 (between-group difference -5.3, "
            "95% CI -6.4 to -4.2, P<0.001); remission rate (ISI <8): CBT-I 58% vs control 18%; gains "
            "maintained at 6 months follow-up (ISI -7.9); fatigue scores also improved (FACIT-F +6.2 "
            "vs +1.4, P<0.001). "
            "Conclusion: CBT-I is highly effective for insomnia disorder in cancer survivors with durable "
            "benefits at 6 months and should be offered as first-line therapy in oncology survivorship programmes."
        ),
    },
    {
        "pmid": "44200071",
        "title": "Point-of-Care Ultrasound for Fluid Responsiveness Assessment in Septic Shock: Diagnostic Accuracy Study",
        "authors": ["Volpicelli G", "Elbarbary M", "Blaivas M", "Lichtenstein DA"],
        "journal": "Critical Care Medicine",
        "journal_abbr": "Crit Care Med",
        "year": 2024, "volume": "52", "issue": "9", "pages": "1418-1429",
        "doi": "10.1097/CCM.0000000000006389",
        "publication_type": "OBSERVATIONAL STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Shock, Septic/therapy",
            "*Point-of-Care Systems",
            "*Ultrasonography/methods",
            "Fluid Therapy/methods", "Hemodynamics",
            "Intensive Care Units", "Humans",
        ],
        "abstract": (
            "Background: Identifying fluid-responsive patients in septic shock may prevent fluid overload; "
            "point-of-care ultrasound (POCUS) assessment of IVC collapsibility and cardiac output may serve "
            "as a bedside predictor. "
            "Methods: Prospective diagnostic accuracy study in 284 ICU patients with septic shock; POCUS "
            "assessments (IVC collapsibility index, cardiac output by VTI, passive leg raise response) "
            "compared to gold-standard transpulmonary thermodilution for fluid responsiveness. "
            "Results: IVC collapsibility index AUROC 0.79 (95% CI 0.73-0.84); VTI-based stroke volume "
            "variation AUROC 0.86 (95% CI 0.81-0.91); PLR + POCUS composite AUROC 0.91 (95% CI 0.87-0.95); "
            "POCUS reclassified fluid management in 34% of patients compared to clinical assessment alone. "
            "Conclusion: POCUS-guided fluid responsiveness assessment combining PLR response and cardiac "
            "output tracking achieves high diagnostic accuracy and improves fluid management decisions in "
            "septic shock."
        ),
    },
    {
        "pmid": "44200072",
        "title": "Lactate-Guided Resuscitation versus Standard Care in Septic Shock: LACTATE-SHOCK Randomised Trial",
        "authors": ["Jansen TC", "van Bommel J", "Schoonderbeek FJ", "Sleeswijk Visser SJ"],
        "journal": "Resuscitation",
        "journal_abbr": "Resuscitation",
        "year": 2023, "volume": "184", "issue": "", "pages": "109694",
        "doi": "10.1016/j.resuscitation.2023.109694",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Shock, Septic/therapy",
            "*Lactic Acid/blood",
            "*Resuscitation/methods",
            "Biomarkers/blood", "Critical Care",
            "Mortality", "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Lactate clearance is a surrogate for tissue hypoxia; lactate-guided resuscitation "
            "targets may improve outcomes in septic shock beyond MAP and urine output targets. "
            "Methods: 492 patients with septic shock (lactate ≥2 mmol/L) randomised to lactate-guided "
            "resuscitation (target: lactate clearance ≥10% per 2h or absolute <2 mmol/L) versus standard "
            "haemodynamic targets; primary outcome: 28-day mortality. "
            "Results: 28-day mortality: lactate-guided 29.4% vs standard 36.2% (HR 0.78, 95% CI 0.63-0.97, "
            "P=0.02); fluid volumes similar at 24h (3.1 vs 3.3 L); vasopressor duration shorter in "
            "lactate-guided arm (3.8 vs 4.9 days, P=0.03). "
            "Conclusion: Lactate-guided resuscitation reduces 28-day mortality in septic shock compared to "
            "standard haemodynamic targets, supporting lactate clearance as a resuscitation endpoint alongside "
            "MAP and urine output."
        ),
    },
    {
        "pmid": "44200073",
        "title": "Out-of-Hospital Cardiac Arrest Resuscitation Outcomes by Bystander CPR Quality: Population Registry Study",
        "authors": ["Rea TD", "Fahrenbruch C", "Culley LL", "Donohoe RT"],
        "journal": "Resuscitation",
        "journal_abbr": "Resuscitation",
        "year": 2024, "volume": "196", "issue": "", "pages": "110129",
        "doi": "10.1016/j.resuscitation.2024.110129",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Out-of-Hospital Cardiac Arrest/therapy",
            "*Cardiopulmonary Resuscitation/standards",
            "*Emergency Medical Services",
            "Bystanders", "Survival Rate",
            "Registries", "Humans",
        ],
        "abstract": (
            "Background: Bystander CPR improves survival from out-of-hospital cardiac arrest (OHCA); "
            "whether CPR quality (compression rate, depth, hands-only vs rescue breathing) modifies "
            "survival is incompletely characterised. "
            "Methods: Registry-based cohort of 8,742 witnessed adult OHCAs with bystander CPR across "
            "14 EMS systems; CPR quality assessed via dispatcher telephone coaching records and AED data; "
            "primary outcome: survival to hospital discharge with good neurological outcome (CPC 1-2). "
            "Results: Good-quality CPR (rate 100-120/min, depth ≥5 cm) associated with 2.3-fold higher "
            "neurologically intact survival vs poor-quality CPR (OR 2.31, 95% CI 1.84-2.90); hands-only "
            "CPR equivalent to CPR with rescue breathing in witnessed shockable arrests (OR 1.04, P=0.81); "
            "dispatcher-assisted CPR improved compression quality by 28% versus unaided. "
            "Conclusion: Bystander CPR quality significantly modifies OHCA survival; dispatcher-assisted "
            "coaching and hands-only CPR promotion are effective public health strategies."
        ),
    },
    {
        "pmid": "44200074",
        "title": "National Colorectal Cancer Screening Programme Impact on Incidence and Mortality: 10-Year Analysis",
        "authors": ["Brenner H", "Schrotz-King P", "Holleczek B", "Katalinic A"],
        "journal": "Preventive Medicine",
        "journal_abbr": "Prev Med",
        "year": 2023, "volume": "172", "issue": "", "pages": "107527",
        "doi": "10.1016/j.ypmed.2023.107527",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Colorectal Neoplasms/prevention & control",
            "*Mass Screening/statistics & numerical data",
            "*Early Detection of Cancer",
            "Colonoscopy", "Incidence",
            "Mortality", "Registries", "Humans",
        ],
        "abstract": (
            "Background: Organised colorectal cancer screening programmes are expanding internationally; "
            "population-level impact on incidence and mortality requires long-term registry analysis. "
            "Methods: Time-trend analysis of CRC incidence and mortality in Germany (2003-2022) using "
            "national cancer registry data; screening colonoscopy uptake linked to incidence trends using "
            "joinpoint regression; age-standardised rates compared between high- and low-uptake regions. "
            "Results: CRC incidence fell 21.4% over the study period; regions with colonoscopy uptake >30% "
            "experienced 34% greater incidence reduction than low-uptake regions (<15%); CRC mortality fell "
            "28.6% nationally; distal colon and rectal cancers showed the largest declines; interval cancer "
            "rate remained 2.4% at 10 years post-colonoscopy. "
            "Conclusion: National colonoscopy screening is associated with substantial reductions in CRC "
            "incidence and mortality; maximising uptake in eligible populations should be a public health priority."
        ),
    },
    {
        "pmid": "44200075",
        "title": "Polypill Strategy for Cardiovascular Risk Reduction in Low- and Middle-Income Countries: TIPS-3 Trial",
        "authors": ["Yusuf S", "Joseph P", "Dans A", "Gao P"],
        "journal": "Preventive Medicine",
        "journal_abbr": "Prev Med",
        "year": 2024, "volume": "179", "issue": "", "pages": "107824",
        "doi": "10.1016/j.ypmed.2024.107824",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Cardiovascular Diseases/prevention & control",
            "*Drug Combinations",
            "*Polypharmacy",
            "Blood Pressure/drug effects", "Developing Countries",
            "Primary Prevention", "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: A polypill combining antihypertensive, statin, and aspirin may simplify cardiovascular "
            "primary prevention in low-resource settings where adherence to multiple tablets is poor. "
            "Methods: 5,713 adults with intermediate cardiovascular risk (no prior CVD) from India, Malaysia, "
            "Tanzania, and Colombia randomised to polypill (telmisartan 40 mg, atorvastatin 40 mg, aspirin "
            "75 mg) or placebo; median follow-up 4.6 years; primary outcome: composite of CVD death, MI, stroke. "
            "Results: Primary outcome: polypill 4.4% vs placebo 5.8% (HR 0.75, 95% CI 0.60-0.95, P=0.02); "
            "SBP reduced by 6.4 mmHg, LDL-C by 0.81 mmol/L; adherence 76% vs 78% at 4 years (P=0.48); "
            "major bleeding 1.2% vs 0.9% (P=0.28). "
            "Conclusion: A fixed-dose polypill reduces cardiovascular events by 25% in intermediate-risk adults "
            "in LMICs and represents a scalable prevention strategy for settings with limited healthcare access."
        ),
    },
    {
        "pmid": "44200076",
        "title": "Childhood Vaccination Coverage and Herd Immunity Thresholds: Global Analysis Across 194 Countries",
        "authors": ["Hu Y", "Chen Y", "Guo J", "Tang S"],
        "journal": "Journal of Clinical Oncology",
        "journal_abbr": "J Clin Oncol",
        "year": 2023, "volume": "41", "issue": "19", "pages": "3547-3558",
        "doi": "10.1200/JCO.23.00289",
        "publication_type": "OBSERVATIONAL STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade C",
        "mesh_terms": [
            "*Vaccination Coverage/statistics & numerical data",
            "*Immunization Programs",
            "*Herd Immunity",
            "Measles/prevention & control", "Global Health",
            "Child", "Humans",
        ],
        "abstract": (
            "Background: Childhood vaccine coverage is a key determinant of herd immunity and outbreak "
            "prevention; post-pandemic recovery trajectories require characterisation. "
            "Methods: Analysis of WHO/UNICEF WUENIC 2023 database covering DTP3, MCV1, MCV2, and PCV3 "
            "coverage in 194 countries (2018-2022); joinpoint regression to identify trend changes; "
            "herd immunity threshold modelling for measles (95%), pertussis (92%), polio (80%). "
            "Results: Global DTP3 coverage fell from 86% (2019) to 81% (2021) then partially recovered "
            "to 84% (2022); 43 countries remained below measles herd immunity threshold in 2022; "
            "sub-Saharan Africa had the largest coverage gaps (DTP3 72%); COVID-19 pandemic disrupted "
            "routine immunisation in 112 countries. "
            "Conclusion: Childhood vaccine coverage declines during the COVID-19 pandemic have not been "
            "fully recovered; urgent remediation targeting sub-Saharan Africa and conflict-affected states "
            "is needed to maintain herd immunity and prevent outbreak resurgence."
        ),
    },
    {
        "pmid": "44200077",
        "title": "Negative Pressure Wound Therapy for Open Abdomen Management after Damage-Control Surgery: Systematic Review",
        "authors": ["Bruhin A", "Ferreira F", "Chariker M", "Smith J"],
        "journal": "Journal of Wound Care",
        "journal_abbr": "J Wound Care",
        "year": 2024, "volume": "33", "issue": "4", "pages": "202-214",
        "doi": "10.12968/jowc.2024.33.4.202",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Negative-Pressure Wound Therapy",
            "*Abdomen/surgery",
            "*Wound Closure Techniques",
            "Damage Control Surgery", "Fascia",
            "Systematic Review as Topic", "Humans",
        ],
        "abstract": (
            "Background: Negative pressure wound therapy (NPWT) for open abdomen (OA) management after "
            "damage-control surgery may facilitate fascial closure and reduce complications; evidence "
            "quality is heterogeneous. "
            "Methods: Systematic review of 28 studies (6 RCTs, 22 cohorts; n=3,847 patients) evaluating "
            "NPWT versus standard temporary abdominal closure in OA; outcomes: fascial closure rate, "
            "enteroatmospheric fistula (EAF), mortality, and time to closure. "
            "Results: Fascial closure rate: NPWT 68% vs standard 52% (RR 1.31, 95% CI 1.18-1.45); "
            "EAF incidence: NPWT 6.4% vs standard 11.2% (RR 0.57, 95% CI 0.42-0.78); time to fascial "
            "closure shorter with NPWT (8.2 vs 11.4 days); mortality: no significant difference (RR 0.93). "
            "Conclusion: NPWT significantly improves fascial closure rates and reduces enteroatmospheric "
            "fistula formation in open abdomen management after damage-control surgery, supporting its "
            "use as the preferred temporary closure technique."
        ),
    },
    {
        "pmid": "44200078",
        "title": "Split-Thickness Skin Graft Outcomes for Lower Limb Defects: Predictors of Graft Failure in 1,200 Procedures",
        "authors": ["Simman R", "Phavixay L", "Priebe CJ", "Jenkins A"],
        "journal": "Burns",
        "journal_abbr": "Burns",
        "year": 2023, "volume": "49", "issue": "6", "pages": "1384-1394",
        "doi": "10.1016/j.burns.2023.03.015",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Skin Transplantation/methods",
            "*Surgical Flaps",
            "*Lower Extremity/surgery",
            "Graft Survival", "Wound Healing",
            "Cohort Studies", "Humans", "Risk Factors",
        ],
        "abstract": (
            "Background: Split-thickness skin grafts (STSGs) for lower limb defects are common but graft "
            "failure rates of 10-30% persist; predictors of failure are incompletely characterised in "
            "contemporary practice. "
            "Methods: Retrospective cohort of 1,200 consecutive STSGs for lower limb defects at three "
            "plastic surgery centres (2016-2022); primary outcome: partial or complete graft failure "
            "within 4 weeks. "
            "Results: Graft failure rate: 18.4% overall; independent predictors on multivariate logistic "
            "regression: wound infection at time of grafting (OR 3.82), diabetes (OR 2.14), graft area "
            ">200 cm2 (OR 1.88), and non-meshed graft (OR 2.31); NPWT bolster dressing versus tie-over "
            "dressing reduced failure (OR 0.61, P=0.002); venous insufficiency without compression "
            "dressing increased failure (OR 2.94). "
            "Conclusion: Wound infection, diabetes, large graft area, and inadequate post-graft "
            "compression are the dominant predictors of STSG failure; NPWT bolster dressings and "
            "pre-operative infection clearance should be prioritised."
        ),
    },
    {
        "pmid": "44200079",
        "title": "Fluid Resuscitation Strategy in Major Burns: Parkland versus Modified Brooke Formula — Multicentre RCT",
        "authors": ["Cartotto RC", "Innes M", "Musgrave MA", "Gomez M"],
        "journal": "Plastic and Reconstructive Surgery",
        "journal_abbr": "Plast Reconstr Surg",
        "year": 2024, "volume": "153", "issue": "5", "pages": "1082-1094",
        "doi": "10.1097/PRS.0000000000011189",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Burns/therapy",
            "*Fluid Therapy/methods",
            "*Resuscitation/methods",
            "Crystalloid Solutions/therapeutic use",
            "Edema/prevention & control", "Critical Care", "Humans",
        ],
        "abstract": (
            "Background: The Parkland formula (4 mL/kg/%TBSA) and Modified Brooke formula (2 mL/kg/%TBSA) "
            "are both used for major burn resuscitation; head-to-head RCT data are lacking. "
            "Methods: 318 adults with burns ≥20% TBSA randomised to Parkland or Modified Brooke formula "
            "for initial 24-hour resuscitation with urine-output-guided adjustments; primary outcome: "
            "24-hour fluid volume administered and abdominal compartment syndrome rate. "
            "Results: Fluid at 24h: Parkland 5.8 mL/kg/%TBSA vs Brooke 4.2 mL/kg/%TBSA (P<0.001); "
            "both exceeded formula predictions due to resuscitation creep; abdominal compartment syndrome: "
            "Parkland 12.6% vs Brooke 7.0% (OR 0.52, P=0.04); mortality 18% vs 19% (P=0.81); "
            "acute kidney injury: Parkland 42% vs Brooke 38% (P=0.38). "
            "Conclusion: Modified Brooke formula results in less fluid administration and lower abdominal "
            "compartment syndrome risk without increasing mortality; it should be preferred as the initial "
            "resuscitation guide for major burns."
        ),
    },
    {
        "pmid": "44200080",
        "title": "Biofilm-Based Wound Care and Antimicrobial Dressings for Chronic Non-Healing Wounds: Clinical Practice Guideline",
        "authors": ["Bjarnsholt T", "Eberlein T", "Malone M", "Metcalf DG"],
        "journal": "Journal of Wound Care",
        "journal_abbr": "J Wound Care",
        "year": 2024, "volume": "33", "issue": "8", "pages": "S1-S48",
        "doi": "10.12968/jowc.2024.33.Sup8.S1",
        "publication_type": "CLINICAL PRACTICE GUIDELINE",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Biofilms",
            "*Wound Healing",
            "*Bandages",
            "Chronic Disease", "Anti-Infective Agents, Local/therapeutic use",
            "Practice Guidelines as Topic", "Humans",
        ],
        "abstract": (
            "Background: Biofilm formation in chronic wounds drives non-healing; evidence-based guidance "
            "on biofilm-targeted wound care and antimicrobial dressing selection is needed. "
            "Methods: International wound care expert panel conducted systematic literature review and "
            "GRADE evidence synthesis across 187 studies on biofilm diagnosis, disruption strategies, "
            "and antimicrobial dressing efficacy for chronic wounds (diabetic foot, venous leg, pressure). "
            "Results: Strong evidence supports serial sharp debridement to disrupt biofilm every 1-2 weeks "
            "(OR for healing improvement 2.14); silver-containing dressings reduce biofilm load in "
            "clinically infected wounds (evidence level B); DACC-coated dressings showed benefit in "
            "critically colonised wounds; topical antiseptics (PHMB, cadexomer iodine) preferred over "
            "topical antibiotics to avoid resistance; wound swab cultures have limited utility for "
            "biofilm diagnosis (sensitivity 35%). "
            "Conclusion: Biofilm management through regular debridement and appropriate antimicrobial "
            "dressing selection improves healing rates in chronic wounds; routine wound cultures should "
            "not guide dressing choice in the absence of clinical infection signs."
        ),
    },
    {
        "pmid": "44200021",
        "title": "SGLT2 Inhibitors versus Placebo in Type 2 Diabetes with Established Cardiovascular Disease: EMPA-REG OUTCOME 5-Year Extended Analysis",
        "authors": ["Zinman B", "Wanner C", "Lachin JM", "Fitchett D"],
        "journal": "Journal of Clinical Endocrinology & Metabolism",
        "journal_abbr": "J Clin Endocrinol Metab",
        "year": 2021, "volume": "106", "issue": "4", "pages": "1044-1057",
        "doi": "10.1210/clinem/dgab021",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "*Diabetes Mellitus, Type 2/drug therapy",
            "*Cardiovascular Diseases/prevention & control",
            "Empagliflozin/therapeutic use",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Empagliflozin reduced cardiovascular mortality in T2DM patients with established CVD in the "
            "original EMPA-REG OUTCOME trial; 5-year extended follow-up data are presented here. "
            "Methods: Double-blind RCT extended follow-up of 7,020 T2DM patients with established CVD randomised to "
            "empagliflozin 10 or 25 mg QD vs placebo; primary composite endpoint was CV death, non-fatal MI, or stroke. "
            "Results: CV death/MI/stroke at 5 years: empagliflozin 22.1% vs placebo 27.4% (HR 0.76, 95% CI 0.69-0.83, "
            "P<0.001); CV mortality: 9.2% vs 13.1% (HR 0.68); hospitalisation for HF: 3.1% vs 5.7% (HR 0.53, P<0.001). "
            "Conclusion: Empagliflozin provides durable 5-year cardiovascular and heart failure benefits in T2DM-CVD, "
            "confirming its role as a cornerstone of cardiometabolic pharmacotherapy."
        ),
    },
    {
        "pmid": "44200022",
        "title": "GLP-1 Receptor Agonist Therapy and Thyroid Cancer Surveillance: Population-Based Cohort Study",
        "authors": ["Lega IC", "Austin PC", "Fischer HD", "Fung K"],
        "journal": "Lancet Diabetes & Endocrinology",
        "journal_abbr": "Lancet Diabetes Endocrinol",
        "year": 2021, "volume": "9", "issue": "8", "pages": "511-521",
        "doi": "10.1016/S2213-8587(21)00130-7",
        "publication_type": "Cohort Study",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Glucagon-Like Peptide-1 Receptor/agonists",
            "*Thyroid Neoplasms/epidemiology",
            "*Diabetes Mellitus, Type 2/drug therapy",
            "Cohort Studies", "Pharmacovigilance", "Humans",
        ],
        "abstract": (
            "Background: Preclinical data raised concerns about GLP-1 receptor agonist-associated thyroid C-cell "
            "tumours; human epidemiological data have been conflicting. "
            "Methods: Population-based cohort of 399,124 T2DM patients initiating GLP-1 RAs, DPP4 inhibitors, or "
            "insulin from 2007-2018; thyroid cancer diagnosis ascertained via provincial cancer registry linkage. "
            "Results: Thyroid cancer incidence per 10,000 person-years: GLP-1 RA 3.1 vs DPP4i 2.8 vs insulin 3.4 "
            "(adjusted HR for GLP-1 RA vs DPP4i 1.06, 95% CI 0.88-1.28); medullary thyroid cancer did not differ "
            "significantly across groups (HR 1.18, 95% CI 0.71-1.97). "
            "Conclusion: GLP-1 receptor agonist use is not significantly associated with increased thyroid cancer "
            "risk in real-world T2DM populations, providing reassurance for clinical prescribing."
        ),
    },
    {
        "pmid": "44200023",
        "title": "Alpha-Blockers versus Combination Therapy for Benign Prostatic Hyperplasia: 4-Year Outcomes from the CONDUCT Trial",
        "authors": ["Roehrborn CG", "Barkin J", "Siami P", "Tubaro A"],
        "journal": "European Urology",
        "journal_abbr": "Eur Urol",
        "year": 2021, "volume": "80", "issue": "3", "pages": "349-360",
        "doi": "10.1016/j.eururo.2021.04.022",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Prostatic Hyperplasia/drug therapy",
            "*Adrenergic alpha-Antagonists/therapeutic use",
            "*5-alpha Reductase Inhibitors/therapeutic use",
            "Drug Therapy, Combination", "Humans", "Male",
        ],
        "abstract": (
            "Background: Combination alpha-blocker plus 5-alpha reductase inhibitor therapy is recommended for "
            "BPH with moderate-to-severe symptoms, but long-term comparative data against alpha-blocker monotherapy "
            "are needed. "
            "Methods: RCT of 3,047 men with BPH (IPSS >=12, prostate volume >=30 mL) randomised to dutasteride-tamsulosin "
            "combination versus tamsulosin monotherapy for 4 years; primary endpoint: IPSS reduction at 4 years. "
            "Results: IPSS improvement: combination -6.3 vs monotherapy -4.9 points (P<0.001); acute urinary retention: "
            "combination 1.8% vs monotherapy 4.2% (HR 0.43, P<0.001); BPH-related surgery: combination 2.1% vs 5.4% "
            "(HR 0.37, P<0.001); sexual adverse events: higher with combination (22% vs 14%). "
            "Conclusion: Combination therapy provides superior symptomatic and clinical outcomes versus alpha-blocker "
            "monotherapy in men with large-volume BPH, at the cost of greater sexual adverse effects."
        ),
    },
    {
        "pmid": "44200024",
        "title": "Surveillance Intervals After Endoscopic Resection of Non-Muscle-Invasive Bladder Cancer: Systematic Review and Meta-Analysis",
        "authors": ["Sylvester RJ", "Rodriguez O", "Hernandez V", "Turturica D"],
        "journal": "Journal of Urology",
        "journal_abbr": "J Urol",
        "year": 2021, "volume": "206", "issue": "5", "pages": "1145-1156",
        "doi": "10.1097/JU.0000000000002029",
        "publication_type": "Systematic Review",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Urinary Bladder Neoplasms/surgery",
            "*Cystoscopy/standards",
            "*Neoplasm Recurrence, Local/prevention & control",
            "Endoscopy", "Systematic Reviews as Topic", "Humans",
        ],
        "abstract": (
            "Background: Cystoscopic surveillance after transurethral resection of bladder tumour (TURBT) reduces "
            "recurrence-related mortality, but optimal intervals across risk strata remain debated. "
            "Methods: Systematic review of 34 studies (n=26,841 patients) comparing surveillance intervals in "
            "low-, intermediate-, and high-risk non-muscle-invasive bladder cancer (NMIBC) following TURBT. "
            "Results: Extended 12-month surveillance in low-risk NMIBC was non-inferior to 3-month intervals "
            "(progression HR 0.98, 95% CI 0.79-1.22); high-risk NMIBC required 3-month cystoscopy in year 1 to "
            "detect recurrence at a clinically meaningful rate (sensitivity 94% vs 78% for 6-monthly intervals). "
            "Conclusion: Surveillance intensity should be stratified by risk: low-risk NMIBC tolerates 12-month "
            "intervals without harm, while high-risk disease requires quarterly cystoscopy in the first year."
        ),
    },
    {
        "pmid": "44200025",
        "title": "Open Repair versus Endovascular Aneurysm Repair for Abdominal Aortic Aneurysm: 15-Year Results of the EVAR-1 Trial",
        "authors": ["Patel R", "Sweeting MJ", "Powell JT", "Greenhalgh RM"],
        "journal": "Annals of Vascular Surgery",
        "journal_abbr": "Ann Vasc Surg",
        "year": 2022, "volume": "79", "issue": "1", "pages": "14-25",
        "doi": "10.1016/j.avsg.2021.09.014",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Aortic Aneurysm, Abdominal/surgery",
            "*Endovascular Procedures/methods",
            "*Vascular Surgical Procedures/methods",
            "Stents", "Survival Analysis", "Humans",
        ],
        "abstract": (
            "Background: EVAR provided early mortality benefit over open repair for AAA, but late outcomes including "
            "aneurysm-related death and reintervention rates require 15-year follow-up data. "
            "Methods: Long-term follow-up of 1,252 patients randomised to EVAR vs open surgical repair; primary "
            "outcomes were all-cause mortality, aneurysm-related mortality, and reintervention rate. "
            "Results: All-cause mortality at 15 years was similar (EVAR 67% vs open 64%; HR 1.07, P=0.28); "
            "aneurysm-related mortality was higher with EVAR after 8 years (HR 1.64, P=0.02); reintervention rate "
            "was three-fold higher with EVAR (26% vs 9%, P<0.001). "
            "Conclusion: EVAR's early mortality benefit is not sustained beyond 8 years and is associated with "
            "substantially higher reintervention rates, underscoring the importance of lifelong surveillance after EVAR."
        ),
    },
    {
        "pmid": "44200026",
        "title": "Supervised Exercise Therapy versus Revascularisation for Peripheral Arterial Disease: META-PAD Network Meta-Analysis",
        "authors": ["Fakhry F", "Rouwet EV", "den Hoed PT", "Hunink MG"],
        "journal": "Journal of Bone and Joint Surgery",
        "journal_abbr": "J Bone Joint Surg Am",
        "year": 2022, "volume": "104", "issue": "10", "pages": "897-908",
        "doi": "10.2106/JBJS.21.01184",
        "publication_type": "Meta-Analysis",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Peripheral Arterial Disease/therapy",
            "*Exercise Therapy/methods",
            "*Endovascular Procedures/methods",
            "Ankle Brachial Index", "Walking", "Humans",
        ],
        "abstract": (
            "Background: Supervised exercise therapy (SET) and revascularisation are both guideline-recommended for "
            "intermittent claudication in peripheral arterial disease; comparative long-term effectiveness is uncertain. "
            "Methods: Network meta-analysis of 22 RCTs (n=3,840 patients) comparing SET, endovascular revascularisation, "
            "surgical bypass, or hybrid approaches for intermittent claudication. "
            "Results: Maximum walking distance at 12 months: SET improved by 178% vs 138% for endovascular (NMD 40%, "
            "95% CrI 12-68%); functional capacity at 6 minutes favoured SET (SMD 0.42, 95% CrI 0.18-0.66); "
            "no significant differences in MACE or limb salvage across treatment modalities at 3 years. "
            "Conclusion: SET provides superior walking distance and functional capacity compared to endovascular "
            "revascularisation at 12 months; initial SET should be the standard first-line strategy for claudication."
        ),
    },
    {
        "pmid": "44200027",
        "title": "Total Hip Arthroplasty Outcomes in Patients Aged 75 and Over: A Prospective Cohort Study",
        "authors": ["Prokopetz JJ", "Losina E", "Bliss RL", "Wright J"],
        "journal": "Journal of Bone and Joint Surgery",
        "journal_abbr": "J Bone Joint Surg Am",
        "year": 2021, "volume": "103", "issue": "9", "pages": "782-791",
        "doi": "10.2106/JBJS.20.01184",
        "publication_type": "Cohort Study",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Arthroplasty, Replacement, Hip/methods",
            "*Osteoarthritis, Hip/surgery",
            "*Aged/surgery",
            "Patient Satisfaction", "Postoperative Complications",
            "Cohort Studies", "Humans", "Prospective Studies",
        ],
        "abstract": (
            "Background: Total hip arthroplasty (THA) is increasingly performed in elderly patients; outcomes and "
            "complication profiles in those aged 75 and over compared to younger cohorts require prospective data. "
            "Methods: Prospective cohort of 4,218 THA procedures; 1,094 patients were aged >=75 and compared to "
            "3,124 aged 18-74 on WOMAC scores, 90-day complications, and 5-year revision rates. "
            "Results: WOMAC improvement at 12 months was similar across age groups (mean difference -2.1 points, "
            "95% CI -4.3 to 0.1, P=0.06); 90-day major complications were higher in >=75 group (7.2% vs 4.1%, "
            "P<0.001), primarily driven by delirium (4.8%) and VTE (1.9%); 5-year revision rate did not differ "
            "(4.1% vs 4.4%, P=0.72). "
            "Conclusion: THA provides equivalent functional outcomes in patients aged >=75 versus younger patients, "
            "though perioperative complication risk is higher and requires targeted prevention strategies."
        ),
    },
    {
        "pmid": "44200028",
        "title": "Subcutaneous Allergen Immunotherapy for House Dust Mite Allergic Rhinitis: 3-Year Randomised Controlled Trial",
        "authors": ["Demoly P", "Calderon MA", "Casale T", "Scadding G"],
        "journal": "Clinical & Experimental Allergy",
        "journal_abbr": "Clin Exp Allergy",
        "year": 2022, "volume": "52", "issue": "6", "pages": "742-753",
        "doi": "10.1111/cea.14124",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Rhinitis, Allergic/therapy",
            "*Desensitization, Immunologic/methods",
            "*Pyroglyphidae/immunology",
            "Allergens/immunology", "Injections, Subcutaneous",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Subcutaneous allergen immunotherapy (SCIT) modifies allergic disease; 3-year outcomes "
            "for house dust mite (HDM) SCIT in allergic rhinitis require prospective validation. "
            "Methods: Double-blind RCT of 618 adults with HDM-sensitised allergic rhinitis randomised to HDM "
            "SCIT or placebo for 3 years; primary endpoint was total nasal symptom score (TNSS) at 3 years. "
            "Results: TNSS reduction: SCIT -42% vs placebo -18% (between-group difference -24%, 95% CI -29 to -19, "
            "P<0.001); rhinoconjunctivitis quality-of-life score improved by 1.8 vs 0.7 points (P<0.001); "
            "asthma exacerbations were reduced in the SCIT group at 3 years (12% vs 22%, HR 0.53, P=0.002). "
            "Conclusion: Three-year HDM SCIT provides substantial and sustained symptom reduction in allergic "
            "rhinitis and reduces asthma exacerbation risk, supporting its use as disease-modifying therapy."
        ),
    },
    {
        "pmid": "44200029",
        "title": "Oral Immunotherapy for Peanut Allergy Desensitisation: PALISADE Extension Cohort 4-Year Follow-Up",
        "authors": ["Vickery BP", "Vereda A", "Casale TB", "Beyer K"],
        "journal": "Allergy",
        "journal_abbr": "Allergy",
        "year": 2022, "volume": "77", "issue": "3", "pages": "894-905",
        "doi": "10.1111/all.15124",
        "publication_type": "Cohort Study",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Peanut Hypersensitivity/therapy",
            "*Desensitization, Immunologic/methods",
            "*Administration, Oral",
            "Allergens/immunology", "Immunotherapy",
            "Cohort Studies", "Humans", "Child",
        ],
        "abstract": (
            "Background: AR101 (peanut oral immunotherapy) achieved desensitisation in 67% of participants in "
            "the PALISADE RCT; long-term maintenance and sustained unresponsiveness data are limited. "
            "Methods: Open-label extension cohort of 372 PALISADE completers continuing AR101 300 mg/day for "
            "4 years; primary endpoint: sustained unresponsiveness (SU) after 8-week avoidance period. "
            "Results: SU at 4 years achieved in 29% of participants; 58% maintained desensitisation at "
            "300 mg but lost SU after avoidance; adverse events in 8% (predominantly gastrointestinal); "
            "eosinophilic oesophagitis confirmed in 3 participants (0.8%). "
            "Conclusion: Long-term peanut OIT maintains desensitisation in the majority but sustained "
            "unresponsiveness is achieved in fewer than one-third, indicating ongoing daily dosing is required "
            "for most patients."
        ),
    },
    {
        "pmid": "44200030",
        "title": "Dupilumab for Moderate-to-Severe Atopic Dermatitis in Adults: LIBERTY AD CHRONOS 3-Year Analysis",
        "authors": ["Blauvelt A", "de Bruin-Weller M", "Gooderham M", "Cather JC"],
        "journal": "Allergy",
        "journal_abbr": "Allergy",
        "year": 2022, "volume": "77", "issue": "4", "pages": "1123-1134",
        "doi": "10.1111/all.15234",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Dermatitis, Atopic/drug therapy",
            "*Antibodies, Monoclonal, Humanized/therapeutic use",
            "*Interleukin-4 Receptor alpha Subunit/antagonists & inhibitors",
            "Eczema Area and Severity Index", "Pruritus/drug therapy",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Dupilumab (anti-IL-4Ralpha) demonstrated 1-year efficacy and safety in atopic dermatitis; "
            "3-year durability data are needed. "
            "Methods: Double-blind RCT extension enrolling 740 adults with moderate-to-severe AD randomised to "
            "dupilumab 300 mg every 2 weeks plus topical corticosteroids vs placebo plus TCS for 3 years; "
            "primary endpoint was IGA 0/1 at week 148. "
            "Results: IGA 0/1 at week 148: dupilumab 39% vs placebo 12% (P<0.001); EASI-75: 64% vs 24% "
            "(P<0.001); pruritus NRS >=4-point improvement: 55% vs 19% (P<0.001); no new safety signals at "
            "3 years including no increased infection risk. "
            "Conclusion: Dupilumab provides durable 3-year efficacy and acceptable safety in adults with "
            "moderate-to-severe atopic dermatitis, supporting its use as long-term maintenance therapy."
        ),
    },
    {
        "pmid": "44200031",
        "title": "Anti-VEGF Therapy for Neovascular Age-Related Macular Degeneration: Treat-and-Extend versus Monthly Dosing - HARBOR 5-Year Trial",
        "authors": ["Busbee BG", "Ho AC", "Brown DM", "Heier JS"],
        "journal": "Ophthalmology",
        "journal_abbr": "Ophthalmology",
        "year": 2021, "volume": "128", "issue": "11", "pages": "1573-1584",
        "doi": "10.1016/j.ophtha.2021.04.012",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Macular Degeneration/drug therapy",
            "*Angiogenesis Inhibitors/therapeutic use",
            "*Vascular Endothelial Growth Factor A/antagonists & inhibitors",
            "Ranibizumab/therapeutic use", "Visual Acuity",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Anti-VEGF injections are the standard of care for neovascular AMD; treat-and-extend (T&E) "
            "may reduce injection burden while preserving visual outcomes versus monthly dosing. "
            "Methods: RCT of 1,098 neovascular AMD patients randomised to ranibizumab 0.5 mg T&E vs monthly "
            "0.5 mg for 5 years; primary endpoint was mean BCVA change from baseline. "
            "Results: Mean BCVA gain: T&E +6.1 letters vs monthly +7.0 letters (non-inferiority margin 5 letters "
            "met; P<0.001 for non-inferiority); injection burden: T&E 36 vs monthly 60 injections over 5 years; "
            "geographic atrophy incidence: T&E 22% vs monthly 19% (P=0.31). "
            "Conclusion: T&E ranibizumab achieves non-inferior visual acuity outcomes compared to monthly dosing "
            "while reducing injection burden by 40%, supporting T&E as the preferred dosing strategy for neovascular AMD."
        ),
    },
    {
        "pmid": "44200032",
        "title": "Selective Laser Trabeculoplasty versus Prostaglandin Analogue Eye Drops as First-Line Glaucoma Treatment: LiGHT Trial 6-Year Follow-Up",
        "authors": ["Garg A", "Vickerstaff V", "Nathwani N", "Garway-Heath D"],
        "journal": "British Journal of Ophthalmology",
        "journal_abbr": "Br J Ophthalmol",
        "year": 2022, "volume": "106", "issue": "8", "pages": "1099-1107",
        "doi": "10.1136/bjophthalmol-2021-320499",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Glaucoma, Open-Angle/therapy",
            "*Trabeculoplasty, Laser/methods",
            "*Prostaglandins, Synthetic/therapeutic use",
            "Intraocular Pressure/drug effects", "Visual Fields",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: The LiGHT trial showed selective laser trabeculoplasty (SLT) was non-inferior to "
            "prostaglandin analogue (PGA) drops at 3 years; 6-year durability data are needed. "
            "Methods: Continued follow-up of 718 LiGHT trial participants (OHT or early/moderate POAG); "
            "primary outcome was IOP control within target range without medication or surgery. "
            "Results: IOP within target range at 6 years: SLT 76% vs PGA 72% (P=0.31; non-inferiority maintained); "
            "patients requiring rescue treatment: SLT 22% vs PGA 28% (HR 0.75, P=0.04); mean IOP: SLT 15.9 "
            "vs PGA 16.3 mmHg (P=0.18); visual field progression: no significant difference (P=0.62). "
            "Conclusion: SLT maintains non-inferior IOP control to PGA drops at 6 years and reduces rescue "
            "treatment need, supporting SLT as first-line therapy for newly diagnosed OHT and early glaucoma."
        ),
    },
    {
        "pmid": "44200033",
        "title": "Phacoemulsification Cataract Surgery Outcomes in Patients with Diabetic Retinopathy: Multicentre Prospective Case Series",
        "authors": ["Squirrell D", "Bhola R", "Bush J", "Bhoskar A"],
        "journal": "British Journal of Ophthalmology",
        "journal_abbr": "Br J Ophthalmol",
        "year": 2021, "volume": "105", "issue": "4", "pages": "517-523",
        "doi": "10.1136/bjophthalmol-2020-317348",
        "publication_type": "Case Series",
        "evidence_level": "Level IV", "evidence_grade": "Grade C",
        "mesh_terms": [
            "*Cataract Extraction/methods",
            "*Diabetic Retinopathy/complications",
            "*Phacoemulsification",
            "Visual Acuity", "Macular Edema/etiology",
            "Humans", "Prospective Studies",
        ],
        "abstract": (
            "Background: Phacoemulsification in diabetic patients carries higher risk of postoperative macular "
            "oedema and retinopathy progression; prospective multicentre data are limited. "
            "Methods: Prospective case series of 486 diabetic eyes undergoing phacoemulsification at 8 centres; "
            "diabetic retinopathy was graded preoperatively; primary outcomes were visual acuity at 3 months "
            "and retinopathy progression at 12 months. "
            "Results: Visual acuity improved >=2 Snellen lines in 72% at 3 months; CMO occurred in 14% overall "
            "(21% in pre-existing DMO vs 8% in no DMO, P<0.001); retinopathy progressed by >=1 ETDRS step in "
            "18% at 12 months, highest in proliferative DR (32%); intravitreal anti-VEGF prophylaxis reduced "
            "CMO in high-risk eyes (7% vs 19%, P=0.02). "
            "Conclusion: Phacoemulsification achieves good visual outcomes in diabetic patients, but pre-existing "
            "DMO and proliferative DR require targeted peri-operative anti-VEGF prophylaxis to reduce CMO risk."
        ),
    },
    {
        "pmid": "44200034",
        "title": "Laparoscopic versus Open Right Hemicolectomy for Colon Cancer: Long-Term Oncological Outcomes from the COLOR II Randomised Trial",
        "authors": ["Buunen M", "Veldkamp R", "Hop WC", "Kuhry E"],
        "journal": "Annals of Surgery",
        "journal_abbr": "Ann Surg",
        "year": 2021, "volume": "274", "issue": "6", "pages": "963-972",
        "doi": "10.1097/SLA.0000000000005158",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Colectomy/methods",
            "*Colonic Neoplasms/surgery",
            "*Laparoscopy/methods",
            "Disease-Free Survival", "Neoplasm Recurrence, Local",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Short-term outcomes favour laparoscopic right hemicolectomy for colon cancer; 10-year "
            "oncological equivalence requires demonstration through long-term follow-up. "
            "Methods: Long-term follow-up of COLOR II RCT: 1,065 patients with right-sided colon cancer "
            "randomised to laparoscopic (n=534) or open (n=531) right hemicolectomy; primary endpoint was "
            "3-year disease-free survival, extended to 10-year overall survival for this report. "
            "Results: 10-year overall survival: laparoscopic 63% vs open 61% (HR 0.96, 95% CI 0.80-1.15, "
            "P=0.63); 10-year disease-free survival: 61% vs 59% (HR 0.94, 95% CI 0.78-1.13, P=0.50); "
            "locoregional recurrence: 5.2% vs 5.8% (P=0.71); port-site or wound recurrence: 0.8% vs 0.7%. "
            "Conclusion: Laparoscopic right hemicolectomy provides equivalent long-term oncological outcomes "
            "to open surgery, confirming its status as the standard surgical approach for right colon cancer."
        ),
    },
    {
        "pmid": "44200035",
        "title": "Prostate Cancer Active Surveillance: 15-Year Outcomes from the PRIAS International Cohort",
        "authors": ["Bokhorst LP", "Valdagni R", "Rannikko A", "Kakehi Y"],
        "journal": "European Urology",
        "journal_abbr": "Eur Urol",
        "year": 2022, "volume": "81", "issue": "4", "pages": "421-432",
        "doi": "10.1016/j.eururo.2021.11.022",
        "publication_type": "Cohort Study",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Prostatic Neoplasms/therapy",
            "*Watchful Waiting",
            "*Disease Management",
            "PSA/blood", "Biopsy", "Cohort Studies",
            "Humans", "Male", "Disease Progression",
        ],
        "abstract": (
            "Background: Active surveillance (AS) for low-risk prostate cancer defers treatment while monitoring "
            "for disease reclassification; 15-year metastasis-free and cancer-specific survival data are needed. "
            "Methods: International PRIAS cohort of 8,122 men with low-risk PCa (PSA <=10, Gleason <=6, cT1c-T2a) "
            "on AS; outcomes: reclassification, treatment conversion, metastasis-free survival, cancer-specific survival. "
            "Results: 15-year metastasis-free survival: 98.2%; cancer-specific survival: 99.4%; treatment conversion "
            "rate: 52% at 15 years (predominantly grade reclassification); 28% of untreated men remained on AS; "
            "PSA doubling time <3 years predicted 7.2-fold increase in reclassification (95% CI 5.8-8.9). "
            "Conclusion: Active surveillance for low-risk prostate cancer achieves excellent 15-year cancer-specific "
            "outcomes, validating AS as the preferred management strategy for carefully selected men."
        ),
    },
    {
        "pmid": "44200036",
        "title": "Carotid Endarterectomy versus Stenting in Symptomatic Stenosis: EVA-3S Trial 10-Year Outcomes",
        "authors": ["Mas JL", "Trinquart L", "Leys D", "Albucher JF"],
        "journal": "Annals of Vascular Surgery",
        "journal_abbr": "Ann Vasc Surg",
        "year": 2022, "volume": "81", "issue": "3", "pages": "198-208",
        "doi": "10.1016/j.avsg.2022.01.071",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Carotid Stenosis/surgery",
            "*Endarterectomy, Carotid/methods",
            "*Stents",
            "Stroke/prevention & control", "Angioplasty",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: The EVA-3S trial showed higher periprocedural stroke risk with carotid artery stenting (CAS) "
            "versus endarterectomy (CEA); 10-year ipsilateral stroke recurrence data are now available. "
            "Methods: Ten-year follow-up of 527 patients with symptomatic carotid stenosis >=60% randomised to CAS "
            "or CEA; primary outcome was ipsilateral stroke or any periprocedural stroke/death. "
            "Results: 10-year ipsilateral stroke recurrence: CAS 11.2% vs CEA 6.1% (HR 1.90, 95% CI 1.12-3.24, "
            "P=0.02); periprocedural period (30 days) events drove most of the difference (9% vs 3.9%); "
            "after the periprocedural period, no significant difference between arms (HR 1.21, P=0.48). "
            "Conclusion: CEA remains superior to CAS for preventing ipsilateral stroke in symptomatic carotid "
            "stenosis, largely attributable to lower periprocedural risk; CAS may be reserved for CEA-ineligible patients."
        ),
    },
    {
        "pmid": "44200037",
        "title": "Zoledronic Acid for Osteoporosis Fracture Prevention: HORIZON Pivotal Fracture Trial 10-Year Extended Follow-Up",
        "authors": ["Black DM", "Reid IR", "Boonen S", "Bucci-Rechtweg C"],
        "journal": "Journal of Bone and Joint Surgery",
        "journal_abbr": "J Bone Joint Surg Am",
        "year": 2021, "volume": "103", "issue": "12", "pages": "1089-1099",
        "doi": "10.2106/JBJS.20.02406",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Osteoporosis/drug therapy",
            "*Zoledronic Acid/therapeutic use",
            "*Fractures, Bone/prevention & control",
            "Bone Density/drug effects",
            "Diphosphonates/therapeutic use", "Humans", "Female",
        ],
        "abstract": (
            "Background: Zoledronic acid 5 mg annually reduced fracture risk in the HORIZON trial; optimal "
            "treatment duration beyond 3 years and whether a drug holiday is safe remain uncertain. "
            "Methods: Extended follow-up of HORIZON participants (original 3-year RCT followed by 3-year "
            "extension then open-label follow-up to 10 years) assessing fracture rates and BMD trajectory "
            "with continued vs discontinued zoledronic acid. "
            "Results: Patients continuing at year 6-9 had lower vertebral fracture rates vs discontinuers "
            "(HR 0.62, 95% CI 0.43-0.90); hip BMD declined 1.8% after cessation vs +0.4% with continuation; "
            "atypical femoral fractures: 3 events/10,000 patient-years with cumulative use >6 years; "
            "osteonecrosis of the jaw: 0.2 per 10,000 patient-years. "
            "Conclusion: Extended zoledronic acid beyond 6 years reduces vertebral fracture risk in high-risk "
            "patients; drug holidays are appropriate for lower-risk individuals after 3-6 years of treatment."
        ),
    },
    {
        "pmid": "44200038",
        "title": "Open versus Laparoscopic Mesh Repair for Primary Inguinal Hernia: TEP versus Lichtenstein Multicentre RCT",
        "authors": ["Eker HH", "Langeveld HR", "Klitsie PJ", "van t Riet M"],
        "journal": "Hernia",
        "journal_abbr": "Hernia",
        "year": 2022, "volume": "26", "issue": "4", "pages": "1019-1028",
        "doi": "10.1007/s10029-022-02609-x",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Hernia, Inguinal/surgery",
            "*Herniorrhaphy/methods",
            "*Laparoscopy/methods",
            "Surgical Mesh", "Pain, Postoperative/prevention & control",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Laparoscopic totally extraperitoneal (TEP) and open Lichtenstein mesh repair are both "
            "standard approaches for inguinal hernia; comparative recurrence and chronic pain data at 5 years "
            "from multicentre trials are needed. "
            "Methods: RCT of 1,128 men with primary unilateral inguinal hernia randomised to TEP (n=569) or "
            "Lichtenstein repair (n=559); primary endpoints were recurrence and chronic postoperative inguinal "
            "pain (CPIP) at 5 years. "
            "Results: 5-year recurrence: TEP 3.1% vs Lichtenstein 2.8% (HR 1.10, P=0.71, non-inferiority met); "
            "CPIP (VAS >=3/10): TEP 10% vs Lichtenstein 15% (HR 0.65, P=0.006); return to normal activity: "
            "TEP 7 vs Lichtenstein 12 days (P<0.001); operative time: TEP longer (55 vs 40 min, P<0.001). "
            "Conclusion: TEP and Lichtenstein repair provide equivalent recurrence rates; TEP offers superior "
            "chronic pain outcomes and faster recovery but requires greater operative time and expertise."
        ),
    },
    {
        "pmid": "44200039",
        "title": "Intramedullary Nailing versus Plate Fixation for Distal Radius Fractures in Adults: DRAFFT2 Randomised Trial",
        "authors": ["Costa ML", "Achten J", "Plant C", "Parsons NR"],
        "journal": "BJS (British Journal of Surgery)",
        "journal_abbr": "BJS",
        "year": 2021, "volume": "108", "issue": "5", "pages": "522-531",
        "doi": "10.1093/bjs/znab102",
        "publication_type": "Randomised Controlled Trial",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Radius Fractures/surgery",
            "*Fracture Fixation, Intramedullary/methods",
            "*Bone Plates",
            "Wrist Joint/surgery", "Patient-Reported Outcome Measures",
            "Randomized Controlled Trials as Topic", "Humans",
        ],
        "abstract": (
            "Background: Volar locking plate (VLP) fixation is widely used for displaced distal radius fractures "
            "but Kirschner wire fixation and newer intramedullary nail techniques offer alternatives; comparative "
            "patient-reported outcomes at 12 months are needed. "
            "Methods: RCT of 503 adults with displaced distal radius fracture requiring operative fixation "
            "randomised to intramedullary nail (n=250) or volar locking plate (n=253); primary outcome: "
            "PRWE score at 12 months. "
            "Results: PRWE at 12 months: nail 19.2 vs VLP 19.8 (adjusted difference 0.6, 95% CI -2.8 to 4.0, "
            "P=0.73, non-inferiority demonstrated); range of motion at 12 months: similar across groups; "
            "complications: nail 12% vs VLP 20% (P=0.01), driven by fewer tendon complications with nail; "
            "operative time: nail shorter (32 vs 54 min, P<0.001). "
            "Conclusion: Intramedullary nail fixation is non-inferior to volar locking plate for distal radius "
            "fractures with fewer complications and shorter operative time, offering a valid alternative technique."
        ),
    },
    {
        "pmid": "44200040",
        "title": "ERAS Protocol for Elective Colorectal Surgery: Impact on Postoperative Ileus and Length of Stay - Multicentre Cohort Study",
        "authors": ["Ljungqvist O", "Scott M", "Fearon KC"],
        "journal": "Colorectal Disease",
        "journal_abbr": "Colorectal Dis",
        "year": 2022, "volume": "24", "issue": "3", "pages": "312-322",
        "doi": "10.1111/codi.16002",
        "publication_type": "Cohort Study",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Enhanced Recovery After Surgery",
            "*Colorectal Surgery/methods",
            "*Ileus/prevention & control",
            "Length of Stay", "Postoperative Complications",
            "Cohort Studies", "Humans", "Prospective Studies",
        ],
        "abstract": (
            "Background: Postoperative ileus (POI) prolongs hospital stay after colorectal surgery; ERAS protocol "
            "elements targeting POI include early feeding, alvimopan, and avoidance of nasogastric tubes. "
            "Methods: Prospective multicentre cohort of 5,284 elective colorectal resections across 28 hospitals "
            "comparing pre- and post-ERAS implementation; primary outcomes: POI incidence (no passage of flatus "
            "by day 4) and length of stay. "
            "Results: POI incidence: pre-ERAS 28% vs post-ERAS 14% (OR 0.43, 95% CI 0.36-0.51, P<0.001); "
            "median LOS: pre-ERAS 7 vs post-ERAS 4 days (P<0.001); 30-day readmission: 11% vs 9% (P=0.06); "
            "key ERAS elements most strongly associated with POI reduction: early oral feeding by day 1 "
            "(OR 0.51) and opioid-sparing analgesia (OR 0.58). "
            "Conclusion: ERAS implementation nearly halves POI incidence and reduces LOS by 3 days in elective "
            "colorectal surgery; early feeding and opioid sparing are the most impactful individual elements."
        ),
    },

    # ── Abstracts PMIDs 44200041-44200060: Cardiology/Haematology/Geriatrics/Reproductive Medicine/Sports Medicine/Nutrition/Pharmacology ──

    {
        "pmid": "44200041",
        "title": "Transcatheter Aortic Valve Implantation versus Surgical Aortic Valve Replacement in Intermediate-Risk Patients: 5-Year PARTNER 2A Outcomes",
        "authors": ["Leon MB", "Smith CR", "Mack MJ", "Makkar RR", "Svensson LG"],
        "journal": "European Journal of Cardio-Thoracic Surgery",
        "journal_abbr": "Eur J Cardiothorac Surg",
        "year": 2022, "volume": "62", "issue": "4", "pages": "641-652",
        "doi": "10.1093/ejcts/ezac228",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Transcatheter Aortic Valve Replacement/methods",
            "*Aortic Valve Stenosis/surgery",
            "*Heart Valve Prosthesis Implantation/methods",
            "Treatment Outcome", "Risk Assessment",
            "Humans", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: TAVI has expanded to intermediate-risk patients; long-term comparative data versus "
            "surgical AVR are needed to guide durable device selection. "
            "Methods: Extended 5-year follow-up of PARTNER 2A RCT (n=2,032 intermediate-risk patients "
            "randomised to TAVI with SAPIEN XT versus surgical AVR); primary endpoint all-cause mortality "
            "or disabling stroke. "
            "Results: Primary endpoint TAVI 47.9% vs surgery 43.4% (HR 1.10, 95% CI 0.96-1.27, P=0.17); "
            "haemodynamic valve deterioration lower with TAVI (3.9% vs 5.6%, P=0.03); paravalvular leak "
            "moderate or greater higher with TAVI (5.3% vs 0.6%, P<0.001); pacemaker implantation TAVI "
            "19% vs surgery 9% (P<0.001). "
            "Conclusion: TAVI and surgical AVR have similar 5-year survival in intermediate-risk patients; "
            "TAVI shows lower structural valve deterioration but higher paravalvular leak and pacemaker "
            "rates, informing patient-specific device selection."
        ),
    },
    {
        "pmid": "44200042",
        "title": "Cardiac Device Infections: Epidemiology, Risk Factors, and Outcomes from the ELECTRA Registry",
        "authors": ["Blomström-Lundqvist C", "Traykov V", "Erba PA", "Burri H", "Nielsen JC"],
        "journal": "Heart Rhythm",
        "journal_abbr": "Heart Rhythm",
        "year": 2022, "volume": "19", "issue": "9", "pages": "1452-1462",
        "doi": "10.1016/j.hrthm.2022.05.018",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Defibrillators, Implantable/adverse effects",
            "*Pacemaker, Artificial/adverse effects",
            "*Prosthesis-Related Infections/epidemiology",
            "Risk Factors", "Registries", "Humans", "Endocarditis",
        ],
        "abstract": (
            "Background: Cardiac implantable electronic device infections carry high mortality; contemporary "
            "epidemiology and modifiable risk factors across device types require large-scale data. "
            "Methods: Prospective registry of 5,847 CIED infection episodes across 84 European centres "
            "(2018-2022) with outcomes assessed at 1 year. "
            "Results: Incidence 1.9 per 1,000 device-years; ICD/CRT-D carried higher risk than pacemaker "
            "(HR 1.82); independent risk factors included diabetes (OR 2.1), renal failure (OR 3.4), and "
            "prior device revision (OR 4.2); in-hospital mortality 4.8% and 1-year mortality 18.2%; complete "
            "device extraction associated with 3-fold lower relapse versus partial extraction. "
            "Conclusion: CIED infections carry substantial mortality; complete device extraction with "
            "antimicrobial therapy is essential and modifiable risk factors should be optimised before implant."
        ),
    },
    {
        "pmid": "44200043",
        "title": "Wearable Cardioverter-Defibrillator for Sudden Cardiac Death Prevention After Acute MI with Low Ejection Fraction: VEST-2 Trial",
        "authors": ["Olgin JE", "Pletcher MJ", "Vittinghoff E", "Wranicz J", "Malik M"],
        "journal": "Heart Rhythm",
        "journal_abbr": "Heart Rhythm",
        "year": 2023, "volume": "20", "issue": "3", "pages": "372-381",
        "doi": "10.1016/j.hrthm.2022.11.024",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Death, Sudden, Cardiac/prevention & control",
            "*Defibrillators, Implantable",
            "*Myocardial Infarction/complications",
            "Ventricular Dysfunction, Left", "Wearable Electronic Devices",
            "Humans", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Patients with low LVEF post-MI face highest sudden cardiac death risk in the first "
            "90 days when ICD implantation is deferred; a wearable cardioverter-defibrillator may bridge "
            "this gap. "
            "Methods: 2,302 post-MI patients with LVEF ≤35% randomised to wearable cardioverter-defibrillator "
            "plus guideline-directed medical therapy versus GDMT alone; primary outcome sudden death at 90 days. "
            "Results: Sudden death: WCD 1.6% vs control 2.4% (HR 0.67, 95% CI 0.41-1.09, P=0.11); all-cause "
            "mortality WCD 3.1% vs control 4.9% (HR 0.63, P=0.03); median WCD wear compliance 21.4 h/day "
            "was the strongest predictor of benefit. "
            "Conclusion: WCD did not significantly reduce sudden death but reduced all-cause mortality; "
            "adherence to wear-compliance counselling is essential for deriving benefit."
        ),
    },
    {
        "pmid": "44200044",
        "title": "Axicabtagene Ciloleucel CAR-T Therapy versus Standard of Care in Relapsed/Refractory Large B-Cell Lymphoma: ZUMA-7 Extended Follow-Up",
        "authors": ["Locke FL", "Miklos DB", "Jacobson CA", "Perales MA", "Kersten MJ"],
        "journal": "Haematologica",
        "journal_abbr": "Haematologica",
        "year": 2022, "volume": "107", "issue": "12", "pages": "2878-2890",
        "doi": "10.3324/haematol.2022.281208",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Receptors, Chimeric Antigen/therapeutic use",
            "*Lymphoma, Large B-Cell, Diffuse/therapy",
            "*Immunotherapy, Adoptive/methods",
            "Hematopoietic Stem Cell Transplantation",
            "Neoplasm Recurrence", "Humans",
            "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: CAR-T therapy with axicabtagene ciloleucel showed superior event-free survival "
            "versus standard-of-care salvage in ZUMA-7; long-term overall survival data are now mature. "
            "Methods: 359 patients with relapsed/refractory large B-cell lymphoma within 12 months of "
            "first-line therapy randomised to axi-cel versus SOC chemotherapy with autologous SCT if eligible. "
            "Results: Median EFS axi-cel 8.3 months vs SOC 2.0 months (HR 0.40, 95% CI 0.31-0.51); 2-year "
            "OS axi-cel 61% vs SOC 52% (HR 0.73, P=0.03); complete response 65% vs 32%; grade ≥3 cytokine "
            "release syndrome 6% and neurological events 21%. "
            "Conclusion: Axi-cel provides superior long-term survival over SOC for early relapsed/refractory "
            "large B-cell lymphoma and is the preferred second-line therapy in transplant-eligible patients."
        ),
    },
    {
        "pmid": "44200045",
        "title": "Rivaroxaban versus Low-Molecular-Weight Heparin for Cancer-Associated Thrombosis: SELECT-D 2-Year Outcomes",
        "authors": ["Young AM", "Marshall A", "Thirlwall J", "Chapman O", "Lokare A"],
        "journal": "British Journal of Haematology",
        "journal_abbr": "Br J Haematol",
        "year": 2022, "volume": "199", "issue": "4", "pages": "512-521",
        "doi": "10.1111/bjh.18461",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Rivaroxaban/therapeutic use",
            "*Heparin, Low-Molecular-Weight/therapeutic use",
            "*Venous Thromboembolism/drug therapy",
            "*Neoplasms/complications",
            "Factor Xa Inhibitors/therapeutic use",
            "Humans", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Rivaroxaban is an attractive oral alternative to LMWH for cancer-associated "
            "thrombosis; 2-year durability and bleeding data in gastrointestinal tumour subgroups are needed. "
            "Methods: 406 cancer patients with VTE randomised to rivaroxaban or dalteparin for 6 months "
            "with extended follow-up to 24 months. "
            "Results: VTE recurrence at 6 months rivaroxaban 4% vs dalteparin 11% (HR 0.43, P=0.01); "
            "clinically relevant non-major bleeding higher with rivaroxaban in GI tumour subgroup (13% vs "
            "4%, P=0.004); 2-year recurrence rivaroxaban 8% vs dalteparin 18% (HR 0.44, P=0.002). "
            "Conclusion: Rivaroxaban substantially reduces cancer-associated thrombosis recurrence versus "
            "LMWH over 2 years; GI tumour patients carry higher bleeding risk requiring individualised "
            "anticoagulant selection."
        ),
    },
    {
        "pmid": "44200046",
        "title": "Hydroxyurea versus Voxelotor for Vaso-Occlusive Crisis Prevention in Paediatric Sickle Cell Disease: HOPE-KIDS Randomised Trial",
        "authors": ["Vichinsky E", "Hoppe CC", "Ataga KI", "Ware RE", "Nduba V"],
        "journal": "British Journal of Haematology",
        "journal_abbr": "Br J Haematol",
        "year": 2023, "volume": "201", "issue": "2", "pages": "298-309",
        "doi": "10.1111/bjh.18682",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Anemia, Sickle Cell/drug therapy",
            "*Hydroxyurea/therapeutic use",
            "*Hemoglobin, Sickle/antagonists & inhibitors",
            "Vaso-Occlusive Crisis/prevention & control",
            "Humans", "Child", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Voxelotor inhibits HbS polymerisation and improves haemolytic anaemia; direct "
            "comparison with hydroxyurea for vaso-occlusive crisis prevention in children is lacking. "
            "Methods: 320 children aged 4-17 years with HbSS or HbSβ0 randomised to voxelotor 900 mg/day "
            "or hydroxyurea (target dose 20-30 mg/kg/day); primary endpoint annual VOC rate at 72 weeks. "
            "Results: Annual VOC rate hydroxyurea 1.8 vs voxelotor 2.4 (rate ratio 1.33, P=0.07); "
            "haemoglobin increase greater with voxelotor (+1.4 vs +0.9 g/dL, P=0.01); transcranial Doppler "
            "normalisation higher with hydroxyurea (38% vs 18%, P=0.006). "
            "Conclusion: Hydroxyurea remains the preferred disease-modifying therapy for VOC prevention "
            "and cerebrovascular risk reduction in paediatric sickle cell disease."
        ),
    },
    {
        "pmid": "44200047",
        "title": "Multicomponent Frailty Intervention in Hospitalised Older Adults: FRAIL-PREVENT Randomised Trial",
        "authors": ["Clegg A", "Young J", "Iliffe S", "Rikkert MO", "Rockwood K"],
        "journal": "Age and Ageing",
        "journal_abbr": "Age Ageing",
        "year": 2022, "volume": "51", "issue": "8", "pages": "afac167",
        "doi": "10.1093/ageing/afac167",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Frailty/therapy",
            "*Geriatric Assessment/methods",
            "*Exercise Therapy/methods",
            "Hospitalization", "Aged", "Muscle Strength",
            "Humans", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Frailty is associated with adverse hospital outcomes; structured multicomponent "
            "intervention during hospitalisation may attenuate functional decline. "
            "Methods: 812 hospitalised adults aged ≥70 with Clinical Frailty Scale score 4-7 randomised "
            "to multicomponent intervention (structured exercise, nutritional supplementation, medication "
            "review, cognitive stimulation) versus usual care; primary outcome Barthel Index at discharge. "
            "Results: Barthel Index at discharge: intervention 82 vs control 74 (mean difference +8.1, "
            "95% CI 5.4-10.8, P<0.001); 30-day readmission intervention 18% vs control 27% (OR 0.61, "
            "P=0.003); length of stay intervention 6.2 vs control 7.8 days (P=0.01). "
            "Conclusion: Multicomponent frailty intervention significantly improves functional discharge "
            "status and reduces readmissions in hospitalised older adults, supporting routine frailty "
            "screening and targeted intervention in all acute wards."
        ),
    },
    {
        "pmid": "44200048",
        "title": "Non-Pharmacological Delirium Prevention in the ICU: PREVENT-ICU Cluster Randomised Trial",
        "authors": ["Bounds M", "Kram S", "Speroni KG", "Brice K", "Luschinski MA"],
        "journal": "Gerontology",
        "journal_abbr": "Gerontology",
        "year": 2022, "volume": "68", "issue": "6", "pages": "678-688",
        "doi": "10.1159/000522847",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Delirium/prevention & control",
            "*Intensive Care Units",
            "*Early Ambulation",
            "Sleep Deprivation/prevention & control",
            "Reorientation", "Humans", "Aged",
        ],
        "abstract": (
            "Background: Delirium affects 30-80% of ICU patients and prolongs ventilation and stay; "
            "non-pharmacological ABCDEF bundles may reduce incidence without adverse drug effects. "
            "Methods: 24 ICUs cluster-randomised to ABCDEF bundle versus standard care; 4,221 mechanically "
            "ventilated adults enrolled; primary outcome delirium prevalence. "
            "Results: Delirium prevalence bundle 52% vs control 71% (OR 0.44, 95% CI 0.38-0.51, P<0.001); "
            "ventilator-free days +2.1 days (P=0.002); ICU mortality bundle 22% vs control 27% (OR 0.77, P=0.01). "
            "Conclusion: Full ABCDEF bundle implementation significantly reduces ICU delirium, ventilator "
            "duration, and mortality; incremental compliance with each element is independently beneficial."
        ),
    },
    {
        "pmid": "44200049",
        "title": "Multifactorial Falls Prevention in Community-Dwelling Older Adults: PROFANE Systematic Review and Meta-Analysis",
        "authors": ["Sherrington C", "Michaleff ZA", "Fairhall N", "Paul SS", "Tiedemann A"],
        "journal": "Age and Ageing",
        "journal_abbr": "Age Ageing",
        "year": 2023, "volume": "52", "issue": "1", "pages": "afac287",
        "doi": "10.1093/ageing/afac287",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Accidental Falls/prevention & control",
            "*Exercise Therapy/methods",
            "*Aged/physiology",
            "Balance Postural/physiology", "Muscle Strength",
            "Systematic Reviews as Topic", "Humans",
        ],
        "abstract": (
            "Background: Falls affect one-third of adults over 65 annually and are the leading cause of "
            "injury-related mortality; synthesis of effective prevention strategies is needed to guide practice. "
            "Methods: Systematic review and meta-analysis of 108 RCTs (n=55,374 participants) evaluating "
            "falls prevention interventions in community-dwelling older adults. "
            "Results: Exercise reduced fall rate by 23% (RR 0.77, 95% CI 0.71-0.83) with balance and "
            "functional exercise most effective (RR 0.71); multifactorial programmes reduced falls (RR 0.78); "
            "vitamin D alone did not reduce falls in non-deficient individuals (RR 0.97, P=0.53); home "
            "hazard modification reduced falls in those with prior falls (RR 0.81). "
            "Conclusion: Supervised balance-focused exercise is the most effective single falls prevention "
            "intervention; multifactorial programmes offer additional benefit for high-risk individuals "
            "with multiple modifiable risk factors."
        ),
    },
    {
        "pmid": "44200050",
        "title": "Cumulative Live Birth Rates After IVF: Freeze-All Embryo Strategy versus Fresh Transfer — FREEZE-ALL RCT",
        "authors": ["Shi Y", "Sun Y", "Hao C", "Zhang H", "Wei D"],
        "journal": "Human Reproduction",
        "journal_abbr": "Hum Reprod",
        "year": 2022, "volume": "37", "issue": "9", "pages": "2059-2070",
        "doi": "10.1093/humrep/deac166",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Fertilization in Vitro/methods",
            "*Embryo Transfer/methods",
            "*Cryopreservation/methods",
            "Live Birth",
            "Ovarian Hyperstimulation Syndrome/prevention & control",
            "Humans", "Female", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: The freeze-all strategy with frozen embryo transfer avoids ovarian hyperstimulation "
            "syndrome but its effect on cumulative live birth rate versus fresh transfer remains debated. "
            "Methods: 1,650 infertile women undergoing first IVF cycle randomised to freeze-all with FET "
            "or fresh embryo transfer; primary outcome cumulative live birth rate within 2 years. "
            "Results: Cumulative live birth rate at 2 years: freeze-all 78% vs fresh transfer 72% (RR 1.08, "
            "95% CI 1.01-1.16, P=0.02); OHSS freeze-all 0.9% vs fresh 2.8% (P=0.003); time to first birth "
            "4.2 weeks longer in freeze-all group. "
            "Conclusion: The freeze-all strategy modestly improves cumulative live birth rate and significantly "
            "reduces OHSS; it should be preferred when OHSS risk is elevated or polycystic ovarian morphology "
            "is present."
        ),
    },
    {
        "pmid": "44200051",
        "title": "Letrozole versus Clomiphene for Ovulation Induction in Polycystic Ovary Syndrome: PPCOSII Network Meta-Analysis",
        "authors": ["Legro RS", "Brzyski RG", "Diamond MP", "Coutifaris C", "Schlaff WD"],
        "journal": "Fertility and Sterility",
        "journal_abbr": "Fertil Steril",
        "year": 2023, "volume": "120", "issue": "3", "pages": "612-622",
        "doi": "10.1016/j.fertnstert.2023.06.001",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Polycystic Ovary Syndrome/drug therapy",
            "*Letrozole/therapeutic use",
            "*Clomiphene/therapeutic use",
            "Ovulation Induction/methods",
            "Live Birth", "Humans", "Female",
        ],
        "abstract": (
            "Background: Letrozole has largely replaced clomiphene for ovulation induction in PCOS; "
            "network meta-analysis can quantify benefit across outcomes and patient subgroups. "
            "Methods: Network meta-analysis of 28 RCTs (n=7,214 women) comparing letrozole, clomiphene, "
            "and metformin combinations; primary outcome live birth rate. "
            "Results: Letrozole superior to clomiphene for live birth (OR 1.42, 95% CI 1.22-1.65) and "
            "ovulation (OR 1.61); letrozole plus metformin achieved the highest live birth rate (OR 1.84 "
            "vs clomiphene alone); multiple pregnancy letrozole 2.1% vs clomiphene 7.4% (P<0.001). "
            "Conclusion: Letrozole is superior to clomiphene for live birth and ovulation in PCOS with "
            "lower multiple pregnancy risk; combined with metformin it should be first-line in "
            "insulin-resistant PCOS."
        ),
    },
    {
        "pmid": "44200052",
        "title": "Varicocele Repair versus Expectant Management for Male Factor Infertility: VARICOFIX Systematic Review",
        "authors": ["Alsaikhan B", "Alrabeeah K", "Delouya G", "Zini A"],
        "journal": "Fertility and Sterility",
        "journal_abbr": "Fertil Steril",
        "year": 2022, "volume": "118", "issue": "5", "pages": "876-886",
        "doi": "10.1016/j.fertnstert.2022.08.001",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Varicocele/surgery",
            "*Infertility, Male/therapy",
            "*Spermatogenesis/physiology",
            "Sperm Count", "Pregnancy Rate",
            "Systematic Reviews as Topic", "Humans", "Male",
        ],
        "abstract": (
            "Background: Varicocele repair to improve male factor infertility remains controversial; "
            "systematic synthesis across RCTs and cohort studies is needed. "
            "Methods: Systematic review of 12 RCTs and 24 cohort studies (n=4,812 couples) comparing "
            "varicocele repair to expectant management in men with clinical varicocele and abnormal semen "
            "parameters. "
            "Results: Spontaneous pregnancy rate repair 38% vs expectant 20% (OR 2.39, 95% CI 1.74-3.28); "
            "sperm concentration increase repair +9.7 million/mL vs expectant +1.2 million/mL (P<0.001); "
            "IVF/ICSI utilisation lower in repair group (28% vs 47%, P<0.001). "
            "Conclusion: Varicocele repair significantly improves spontaneous pregnancy rates and semen "
            "parameters; treatment is recommended before proceeding to assisted reproductive technology."
        ),
    },
    {
        "pmid": "44200053",
        "title": "Graft Choice in ACL Reconstruction and Return-to-Sport Outcomes: COMPARE-ACL Multicentre RCT",
        "authors": ["Monk AP", "Davies LJ", "Hopewell S", "Harris K", "Beard DJ"],
        "journal": "British Journal of Sports Medicine",
        "journal_abbr": "Br J Sports Med",
        "year": 2022, "volume": "56", "issue": "12", "pages": "682-691",
        "doi": "10.1136/bjsports-2021-105012",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Anterior Cruciate Ligament Reconstruction/methods",
            "*Patellar Ligament/transplantation",
            "*Hamstring Tendons/transplantation",
            "Return to Sport", "Knee Joint/surgery",
            "Humans", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Bone-patellar tendon-bone and hamstring tendon autografts are the most common "
            "choices for ACL reconstruction; comparative return-to-sport outcomes remain debated. "
            "Methods: 492 athletes with ACL rupture randomised to BPTB or hamstring tendon reconstruction "
            "at 8 centres; primary outcome return-to-sport clearance at 9 months by functional testing battery. "
            "Results: Return-to-sport clearance BPTB 68% vs HT 61% (OR 1.35, 95% CI 0.97-1.88, P=0.07); "
            "re-rupture at 2 years BPTB 4.2% vs HT 8.1% (P=0.04); anterior knee pain BPTB 18% vs HT 9% "
            "(P=0.004); quadriceps strength deficit greater with BPTB at 6 months but equalised at 12 months. "
            "Conclusion: BPTB and hamstring tendon grafts have comparable return-to-sport rates; BPTB "
            "confers lower re-rupture risk at cost of higher anterior knee pain, informing patient-specific "
            "graft choice based on sport demands."
        ),
    },
    {
        "pmid": "44200054",
        "title": "Arthroscopic Bankart Repair versus Latarjet Procedure for Recurrent Anterior Shoulder Instability: BANKART-LATARJET RCT",
        "authors": ["Lädermann A", "Denard PJ", "Collin P", "Zbinden O", "Bothorel H"],
        "journal": "British Journal of Sports Medicine",
        "journal_abbr": "Br J Sports Med",
        "year": 2023, "volume": "57", "issue": "8", "pages": "494-502",
        "doi": "10.1136/bjsports-2022-106211",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Shoulder Dislocation/surgery",
            "*Joint Instability/surgery",
            "*Arthroscopy/methods",
            "Recurrence", "Bone-Block Procedure",
            "Humans", "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: Arthroscopic Bankart repair and the Latarjet procedure are both used for recurrent "
            "anterior shoulder instability; comparative recurrence and functional outcomes require RCT evidence. "
            "Methods: 218 patients with recurrent anterior shoulder dislocation and glenoid bone loss less "
            "than 20% randomised to arthroscopic Bankart repair or Latarjet procedure; primary outcome "
            "recurrence at 2 years. "
            "Results: Recurrence at 2 years Bankart 13% vs Latarjet 3% (OR 4.9, 95% CI 1.6-15.2, P=0.006); "
            "Rowe score Latarjet 88 vs Bankart 82 (P=0.02); return to contact sport Latarjet 80% vs "
            "Bankart 65% (P=0.04); complication rate similar (9% vs 5%, P=0.28). "
            "Conclusion: The Latarjet procedure provides significantly lower recurrence rates and superior "
            "return to contact sport versus Bankart repair and should be preferred for athletes in contact "
            "sports or those with prior Bankart failure."
        ),
    },
    {
        "pmid": "44200055",
        "title": "Exercise-Based Cardiac Rehabilitation After Acute Coronary Syndrome: HEART-REHAB Systematic Review and Meta-Analysis",
        "authors": ["Anderson L", "Oldridge N", "Thompson DR", "Zwisler AD", "Rees K"],
        "journal": "Clinical Rehabilitation",
        "journal_abbr": "Clin Rehabil",
        "year": 2023, "volume": "37", "issue": "5", "pages": "623-636",
        "doi": "10.1177/02692155221147832",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Cardiac Rehabilitation/methods",
            "*Acute Coronary Syndrome/rehabilitation",
            "*Exercise Therapy/methods",
            "Cardiovascular Diseases/prevention & control",
            "Quality of Life", "Mortality", "Humans",
        ],
        "abstract": (
            "Background: Exercise-based cardiac rehabilitation is recommended after ACS but uptake remains "
            "suboptimal; updated meta-analysis incorporating home-based and hybrid delivery models is needed. "
            "Methods: Systematic review of 63 RCTs (n=14,486 patients) comparing exercise-based CR to usual "
            "care after ACS with separate analyses for centre-based, home-based, and hybrid delivery. "
            "Results: CR reduced cardiovascular mortality (RR 0.74, 95% CI 0.64-0.86) and hospitalisation "
            "(RR 0.82); home-based CR non-inferior to centre-based for mortality and quality of life; "
            "high-intensity interval training showed greater cardiorespiratory fitness gains than moderate "
            "continuous training (VO2peak +1.8 mL/kg/min, P=0.01). "
            "Conclusion: Exercise-based CR reduces mortality and hospitalisation after ACS; home-based "
            "delivery is equivalent to centre-based programmes, supporting flexible implementation to "
            "improve access."
        ),
    },
    {
        "pmid": "44200056",
        "title": "Mediterranean Diet Adherence and Major Cardiovascular Events: PREDIMED-PLUS Extended Cohort Analysis",
        "authors": ["Estruch R", "Ros E", "Salas-Salvadó J", "Covas MI", "Corella D"],
        "journal": "American Journal of Clinical Nutrition",
        "journal_abbr": "Am J Clin Nutr",
        "year": 2022, "volume": "116", "issue": "4", "pages": "1076-1087",
        "doi": "10.1093/ajcn/nqac201",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level II", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Diet, Mediterranean",
            "*Cardiovascular Diseases/prevention & control",
            "*Olive Oil/therapeutic use",
            "Nuts", "Dietary Fats", "Cohort Studies",
            "Humans", "Prospective Studies",
        ],
        "abstract": (
            "Background: PREDIMED showed Mediterranean diet reduces cardiovascular events; PREDIMED-PLUS "
            "adds caloric restriction and physical activity context for weight management. "
            "Methods: Extended prospective cohort of 6,874 PREDIMED-PLUS participants at high cardiovascular "
            "risk; median follow-up 6.3 years; adherence scored with 17-point Mediterranean diet score. "
            "Results: Each 2-point increment in diet score associated with HR 0.82 (95% CI 0.76-0.89) for "
            "MACE; top-tertile adherence conferred 31% lower MACE incidence; combined high adherence with "
            "physical activity (≥45 min/day) yielded HR 0.64 (95% CI 0.53-0.78). "
            "Conclusion: High Mediterranean diet adherence, particularly combined with physical activity, "
            "substantially reduces major cardiovascular events in high-risk adults."
        ),
    },
    {
        "pmid": "44200057",
        "title": "Long-Term Nutritional and Microbiome Outcomes Following Roux-en-Y Gastric Bypass versus Sleeve Gastrectomy: MICROBY-2 Cohort",
        "authors": ["Tremaroli V", "Karlsson F", "Werling M", "Ståhlman M", "Kovatcheva-Datchary P"],
        "journal": "Obesity Surgery",
        "journal_abbr": "Obes Surg",
        "year": 2023, "volume": "33", "issue": "7", "pages": "2012-2023",
        "doi": "10.1007/s11695-023-06588-1",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Gastric Bypass/adverse effects",
            "*Gastrectomy/adverse effects",
            "*Gastrointestinal Microbiome",
            "Nutritional Status", "Weight Loss", "Vitamin B 12 Deficiency",
            "Humans", "Cohort Studies",
        ],
        "abstract": (
            "Background: RYGB and sleeve gastrectomy differ in anatomy and gut microbiome effects; long-term "
            "nutritional consequences and microbiome trajectories require prospective comparison. "
            "Methods: Prospective cohort of 412 patients (RYGB n=208, SG n=204) followed for 5 years with "
            "annual gut microbiome profiling and nutritional blood panels. "
            "Results: Excess weight loss RYGB 72% vs SG 58% at 5 years (P<0.001); nutritional deficiencies "
            "more frequent after RYGB including iron deficiency (28% vs 14%) and B12 deficiency (18% vs "
            "6%, both P<0.001 despite supplementation); microbiome diversity increased more after RYGB "
            "(Shannon index +0.82 vs +0.41, P=0.01) and correlated with metabolic improvement (r=0.41). "
            "Conclusion: RYGB achieves greater weight loss and microbiome diversification than sleeve "
            "gastrectomy but carries higher nutritional deficiency risk requiring lifelong monitoring and "
            "supplementation."
        ),
    },
    {
        "pmid": "44200058",
        "title": "Deprescribing Polypharmacy in Older Adults: Systematic Review of Intervention Effectiveness and Safety",
        "authors": ["Dills H", "Shah K", "Bhavsar J", "Shah R", "Lekura N"],
        "journal": "Clinical Pharmacology & Therapeutics",
        "journal_abbr": "Clin Pharmacol Ther",
        "year": 2023, "volume": "114", "issue": "2", "pages": "351-362",
        "doi": "10.1002/cpt.2954",
        "publication_type": "SYSTEMATIC REVIEW",
        "evidence_level": "Level II", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Polypharmacy",
            "*Deprescriptions",
            "*Aged/drug therapy",
            "Medication Errors/prevention & control",
            "Drug-Related Side Effects and Adverse Reactions",
            "Systematic Reviews as Topic", "Humans",
        ],
        "abstract": (
            "Background: Polypharmacy affects over 40% of older adults and is associated with adverse drug "
            "events, falls, and hospitalisation; structured deprescribing interventions may reduce medication "
            "burden safely. "
            "Methods: Systematic review of 32 RCTs and controlled cohort studies (n=22,847 patients) "
            "evaluating structured deprescribing interventions in adults aged 65 or older with polypharmacy. "
            "Results: Deprescribing reduced mean medications by 2.1 per patient (95% CI 1.6-2.6); adverse "
            "drug events OR 0.72 (95% CI 0.61-0.85); falls OR 0.80 (95% CI 0.68-0.94); mortality no "
            "increase (OR 0.96); hospitalisation reduced by 12%. "
            "Conclusion: Structured deprescribing safely reduces medication burden, adverse drug events, "
            "and falls without increasing mortality, supporting routine deprescribing reviews as part of "
            "geriatric care."
        ),
    },
    {
        "pmid": "44200059",
        "title": "Medication Error Prevention: Impact of Electronic Prescribing with Clinical Decision Support in 12 Hospitals",
        "authors": ["Bates DW", "Leape LL", "Cullen DJ", "Laird N", "Petersen LA"],
        "journal": "Clinical Pharmacology & Therapeutics",
        "journal_abbr": "Clin Pharmacol Ther",
        "year": 2023, "volume": "112", "issue": "4", "pages": "819-829",
        "doi": "10.1002/cpt.2690",
        "publication_type": "COHORT STUDY",
        "evidence_level": "Level III", "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Medication Errors/prevention & control",
            "*Electronic Prescribing",
            "*Decision Support Systems, Clinical",
            "Drug Interactions", "Patient Safety",
            "Hospitals", "Humans",
        ],
        "abstract": (
            "Background: Medication errors are a leading cause of preventable adverse events in hospitals; "
            "electronic prescribing with clinical decision support is widely implemented but real-world error "
            "reduction data are heterogeneous. "
            "Methods: Before-after cohort study in 12 hospitals implementing CPOE-CDS with 124,000 admissions "
            "pre- and 131,000 post-implementation reviewed by pharmacist-adjudicated trigger tool methodology. "
            "Results: Serious medication errors per 1,000 admissions pre-CPOE 11.4 vs post-CPOE 5.8 (RR 0.51, "
            "95% CI 0.44-0.59, P<0.001); drug interaction alerts overridden in 82% of cases driven by "
            "low-specificity alerts; new alert-fatigue-related errors emerged at 0.8 per 1,000 admissions. "
            "Conclusion: CPOE-CDS reduces serious medication errors by approximately 50%; alert specificity "
            "must be optimised to minimise alert-fatigue-driven override rates."
        ),
    },
    {
        "pmid": "44200060",
        "title": "Oral Fosfomycin for ESBL-Producing Enterobacteriaceae Urinary Tract Infection: FOSTER Randomised Trial",
        "authors": ["Huttner A", "Kowalczyk A", "Turjeman A", "Babich T", "Brossier C"],
        "journal": "Journal of Antimicrobial Chemotherapy",
        "journal_abbr": "J Antimicrob Chemother",
        "year": 2023, "volume": "78", "issue": "9", "pages": "2182-2192",
        "doi": "10.1093/jac/dkad224",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I", "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Fosfomycin/therapeutic use",
            "*Urinary Tract Infections/drug therapy",
            "*beta-Lactamases/metabolism",
            "*Enterobacteriaceae Infections/drug therapy",
            "Anti-Bacterial Agents/therapeutic use",
            "Drug Resistance, Bacterial", "Humans",
        ],
        "abstract": (
            "Background: ESBL-producing Enterobacteriaceae UTI often require IV carbapenems; oral fosfomycin "
            "may provide an effective outpatient alternative and preserve carbapenem stewardship. "
            "Methods: 458 women with uncomplicated cystitis caused by ESBL-producing E. coli or K. pneumoniae "
            "randomised to oral fosfomycin 3 g single dose or nitrofurantoin 100 mg BD x5 days; clinical "
            "and microbiological cure assessed at day 14. "
            "Results: Clinical cure fosfomycin 70% vs nitrofurantoin 58% in ESBL subgroup (OR 1.67, 95% CI "
            "1.12-2.49, P=0.01); microbiological eradication fosfomycin 62% vs nitrofurantoin 48% (P=0.02); "
            "resistance acquisition fosfomycin 3% vs nitrofurantoin 6%; no serious adverse events. "
            "Conclusion: Oral fosfomycin provides superior clinical and microbiological cure for ESBL UTI "
            "and should be considered first-line oral therapy, supporting carbapenem sparing in uncomplicated "
            "ESBL cystitis."
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
