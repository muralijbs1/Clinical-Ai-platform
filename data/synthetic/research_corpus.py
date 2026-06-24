"""
Synthetic clinical research abstracts — PubMed/MEDLINE format.

Data tag: SYNTHETIC
All PMIDs, DOIs, authors, and abstracts are synthetic. Structure mirrors
real MEDLINE records exactly: IMRAD abstract, MeSH headings, DOI prefix
matched to journal publisher, evidence grade in conclusions.

Usage:
    from data.synthetic.research_corpus import get_research_corpus
    docs = get_research_corpus()   # list[Document]
"""

from schemas import Document, DataTag

# ── Raw abstract records ──────────────────────────────────────────────────────
# Each entry mirrors a MEDLINE tagged-format record.
# doi prefix conventions: 10.1056=NEJM, 10.1161=AHA, 10.1016=Elsevier,
#                         10.1093=OUP, 10.1002=Wiley

_ABSTRACTS = [
    {
        "pmid": "38421001",
        "title": (
            "Dapagliflozin in Heart Failure with Reduced Ejection Fraction: "
            "Outcomes from the DAPA-HF Extension Trial"
        ),
        "authors": ["Greene SJ", "McMurray JJV", "Solomon SD", "Kosiborod MN"],
        "journal": "New England Journal of Medicine",
        "journal_abbr": "N Engl J Med",
        "year": 2024,
        "volume": "390",
        "issue": "4",
        "pages": "312-323",
        "doi": "10.1056/NEJMoa2317445",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level I",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Heart Failure/drug therapy",
            "Heart Failure/physiopathology",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "Stroke Volume/physiology",
            "Treatment Outcome",
            "Humans",
            "Randomized Controlled Trials as Topic",
        ],
        "abstract": (
            "Background: SGLT2 inhibitors reduce mortality and hospitalisation in patients "
            "with heart failure with reduced ejection fraction (HFrEF). Long-term data beyond "
            "18 months remain limited. "
            "Methods: We conducted a double-blind, randomised, placebo-controlled extension of "
            "the DAPA-HF trial enrolling 4,744 patients with HFrEF (LVEF ≤40%) and NYHA class "
            "II-IV symptoms. Patients received dapagliflozin 10 mg daily or matching placebo in "
            "addition to guideline-directed medical therapy. The primary composite endpoint was "
            "worsening heart failure (hospitalisation or urgent visit) or cardiovascular death. "
            "Results: Over a median follow-up of 36 months, the primary composite endpoint "
            "occurred in 26.3% of the dapagliflozin group versus 34.1% of the placebo group "
            "(HR 0.74, 95% CI 0.65-0.85, P<0.001). All-cause mortality was 19.8% vs 24.6% "
            "(HR 0.80, 95% CI 0.68-0.93). Benefits were consistent regardless of diabetes "
            "status (P-interaction 0.89), baseline LVEF quartile, and ACE inhibitor versus "
            "ARNi background therapy. Dapagliflozin was well tolerated; serious adverse events "
            "were less frequent in the treatment group. Volume depletion occurred in 5.2% of "
            "dapagliflozin vs 3.8% of placebo patients (P=0.04). "
            "Conclusions: Dapagliflozin provides sustained reduction in cardiovascular death "
            "and worsening heart failure over 36 months in HFrEF patients independent of "
            "diabetes status. These findings (Level I, Grade A evidence) support universal "
            "incorporation of SGLT2 inhibitors into guideline-directed medical therapy for HFrEF."
        ),
    },
    {
        "pmid": "37892044",
        "title": (
            "Early Restrictive versus Liberal Fluid Resuscitation in Septic Shock: "
            "A Multicentre Randomised Trial"
        ),
        "authors": ["Hjortrup PB", "Møller MH", "Vestergaard SR", "Perner A"],
        "journal": "Intensive Care Medicine",
        "journal_abbr": "Intensive Care Med",
        "year": 2023,
        "volume": "49",
        "issue": "11",
        "pages": "1298-1309",
        "doi": "10.1007/s00134-023-07214-3",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Septic Shock/therapy",
            "*Fluid Therapy/methods",
            "Resuscitation/methods",
            "Hemodynamics",
            "Critical Care",
            "Humans",
            "Adult",
            "Intensive Care Units",
        ],
        "abstract": (
            "Background: Optimal fluid volume during resuscitation of septic shock remains "
            "debated. Excessive fluid may worsen outcomes through oedema and organ failure. "
            "Methods: In this multicentre, open-label randomised trial, we enrolled 1,554 "
            "adult patients with septic shock (MAP <65 mmHg despite 1L crystalloid, lactate "
            ">2 mmol/L). Patients were randomised 1:1 to restrictive fluid strategy (250 mL "
            "boluses only for documented hypovolaemia) or liberal strategy (1L boluses for "
            "MAP <65 mmHg). Co-primary endpoints were 90-day mortality and serious adverse "
            "events. Vasopressor use and fluid balance were tracked throughout ICU stay. "
            "Results: The restrictive group received a median 2.4 L versus 4.1 L in the liberal "
            "group in the first 72 hours (P<0.001). Ninety-day mortality was 36.8% restrictive "
            "vs 37.9% liberal (OR 0.95, 95% CI 0.78-1.16, P=0.62). Serious adverse events "
            "occurred in 23.6% vs 28.4% (OR 0.78, 95% CI 0.63-0.96, P=0.02), driven by fewer "
            "acute kidney injury episodes in the restrictive group. Length of ICU stay was "
            "similar (7.2 vs 7.5 days). Vasopressor-free days were greater in the restrictive "
            "arm (18.3 vs 16.7 days, P=0.03). "
            "Conclusions: Restrictive fluid resuscitation does not reduce 90-day mortality "
            "in septic shock compared with liberal strategy but is associated with fewer "
            "serious adverse events. These findings (Level II, Grade A) support a targeted, "
            "reassessment-based fluid approach over protocolised liberal resuscitation."
        ),
    },
    {
        "pmid": "38104782",
        "title": (
            "Procalcitonin-Guided Antibiotic Stewardship in Sepsis: "
            "Systematic Review and Meta-Analysis of 32 Randomised Trials"
        ),
        "authors": ["Schuetz P", "Wirz Y", "Sager R", "Müller B"],
        "journal": "Lancet Infectious Diseases",
        "journal_abbr": "Lancet Infect Dis",
        "year": 2024,
        "volume": "24",
        "issue": "3",
        "pages": "289-301",
        "doi": "10.1016/S1473-3099(23)00512-8",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Procalcitonin/blood",
            "*Anti-Bacterial Agents/therapeutic use",
            "*Sepsis/drug therapy",
            "Biomarkers/blood",
            "Antibiotic Stewardship",
            "Systematic Review",
            "Meta-Analysis",
            "Humans",
        ],
        "abstract": (
            "Background: Procalcitonin (PCT) is used to guide antibiotic initiation and "
            "discontinuation in sepsis, but its net clinical benefit remains uncertain. "
            "Methods: We systematically searched MEDLINE, Cochrane, and EMBASE for "
            "randomised trials comparing PCT-guided antibiotic decisions to standard care "
            "in adults with suspected or confirmed infection. Primary outcomes were 28-day "
            "mortality and antibiotic duration. We used random-effects meta-analysis with "
            "Cochran Q heterogeneity testing. Thirty-two trials (n=8,473 patients) met "
            "inclusion criteria. "
            "Results: PCT-guided care reduced antibiotic duration by 1.9 days (95% CI "
            "1.4-2.4, P<0.001) without increasing 28-day mortality (RR 0.91, 95% CI "
            "0.84-0.99, P=0.03 favouring PCT). ICU length of stay was reduced by 0.8 days "
            "(95% CI 0.2-1.4, P=0.01). Benefits were consistent across sepsis severity, "
            "infection source, and ICU versus general ward settings. PCT cut-off of "
            "≤0.5 ng/mL for discontinuation had highest sensitivity-specificity balance "
            "(sensitivity 81%, specificity 74%). Subgroup analysis showed greatest mortality "
            "reduction in patients with PCT >10 ng/mL at presentation. "
            "Conclusions: PCT-guided antibiotic stewardship safely reduces antibiotic "
            "exposure and may reduce mortality in sepsis. This meta-analysis (Level I, "
            "Grade A evidence) supports integration of PCT thresholds into sepsis "
            "antibiotic management protocols at cut-off ≤0.5 ng/mL for discontinuation."
        ),
    },
    {
        "pmid": "38231567",
        "title": (
            "High-Sensitivity Troponin T in the Rapid Evaluation of Non-ST-Elevation "
            "Acute Coronary Syndrome: The RAPID-NSTEMI Validation Study"
        ),
        "authors": ["Shah ASV", "Sandoval Y", "Nofer JR", "Mills NL"],
        "journal": "Journal of the American College of Cardiology",
        "journal_abbr": "J Am Coll Cardiol",
        "year": 2024,
        "volume": "83",
        "issue": "7",
        "pages": "701-713",
        "doi": "10.1016/j.jacc.2023.11.042",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II",
        "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Troponin T/blood",
            "*Non-ST Elevated Myocardial Infarction/diagnosis",
            "Acute Coronary Syndrome/diagnosis",
            "Biomarkers/blood",
            "Sensitivity and Specificity",
            "Humans",
            "Emergency Service, Hospital",
        ],
        "abstract": (
            "Background: Rapid rule-out of non-ST-elevation myocardial infarction (NSTEMI) "
            "using high-sensitivity cardiac troponin (hs-cTnT) reduces unnecessary admissions. "
            "Optimal algorithms for 0/1-hour versus 0/2-hour strategies require prospective "
            "validation across diverse ED populations. "
            "Methods: We prospectively enrolled 3,612 consecutive patients presenting to "
            "six emergency departments with chest pain and no ST-elevation. Hs-cTnT was "
            "measured at 0 and 1 hour. The ESC 0/1-hour algorithm (rule-out: hs-cTnT <5 ng/L "
            "at 0h AND delta <2 ng/L; rule-in: hs-cTnT ≥52 ng/L OR delta ≥6 ng/L) was "
            "applied. Final diagnosis adjudicated by two independent cardiologists. "
            "Results: NSTEMI was diagnosed in 17.3% of patients (n=625). The 0/1-hour "
            "algorithm classified 41.2% as rule-out (sensitivity 99.4%, NPV 99.9%), "
            "22.6% as rule-in (PPV 74.8%), and 36.2% as observe. Among rule-out patients, "
            "30-day MACE occurred in 0.6% (95% CI 0.1-1.4%). Female sex and renal impairment "
            "were independent predictors of algorithm failure. "
            "Conclusions: The ESC 0/1-hour hs-cTnT algorithm demonstrates excellent safety "
            "for NSTEMI rule-out in routine ED practice (Level II, Grade B). The 0.6% MACE "
            "rate in the rule-out group is within acceptable safety margins for early discharge."
        ),
    },
    {
        "pmid": "37654321",
        "title": (
            "Empagliflozin in Heart Failure with Preserved Ejection Fraction: "
            "Subgroup Analysis of the EMPEROR-Preserved Trial by Ejection Fraction Quartile"
        ),
        "authors": ["Anker SD", "Butler J", "Filippatos G", "Zannad F"],
        "journal": "European Heart Journal",
        "journal_abbr": "Eur Heart J",
        "year": 2023,
        "volume": "44",
        "issue": "22",
        "pages": "2058-2071",
        "doi": "10.1093/eurheartj/ehad178",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level I",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Heart Failure/drug therapy",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "Stroke Volume",
            "Ventricular Function, Left",
            "Randomized Controlled Trials as Topic",
            "Humans",
        ],
        "abstract": (
            "Background: EMPEROR-Preserved demonstrated empagliflozin reduces heart failure "
            "hospitalisation in HFpEF (LVEF ≥40%). Whether benefit varies by ejection "
            "fraction subgroup remains unclear. "
            "Methods: Pre-specified subgroup analysis of the EMPEROR-Preserved trial "
            "(n=5,988, LVEF ≥40%, NT-proBNP ≥300 pg/mL or ≥900 pg/mL if AF). Patients "
            "were divided by LVEF quartile: Q1 40-49% (HFmrEF), Q2 50-57%, Q3 58-65%, "
            "Q4 >65%. Primary endpoint: composite of cardiovascular death or HF hospitalisation. "
            "Results: Empagliflozin reduced the primary endpoint across all EF quartiles "
            "(HR range 0.73-0.82, all P<0.05). Absolute risk reduction was greatest in "
            "Q1 (HFmrEF): 5.4% vs 2.1% in Q4 (HFpEF, LVEF >65%). NT-proBNP reduction "
            "was more pronounced in lower EF quartiles (mean change -278 vs -89 pg/mL, "
            "P-interaction 0.02). Quality of life improvement measured by KCCQ was "
            "consistent across quartiles. eGFR decline was attenuated in all EF groups. "
            "Conclusions: Empagliflozin benefits are present across the full spectrum of "
            "preserved and mildly reduced EF, with greatest absolute benefit in HFmrEF "
            "(Level I, Grade A). LVEF should not be used to exclude patients from SGLT2 "
            "inhibitor therapy in the EF ≥40% population."
        ),
    },
    {
        "pmid": "38561234",
        "title": (
            "Intensive Blood Pressure Reduction in Patients with Type 2 Diabetes and "
            "Stage 3 Chronic Kidney Disease: A Multicentre RCT"
        ),
        "authors": ["Whelton PK", "Carey RM", "Aronow WS", "Wright JT Jr"],
        "journal": "Hypertension",
        "journal_abbr": "Hypertension",
        "year": 2024,
        "volume": "81",
        "issue": "5",
        "pages": "1042-1055",
        "doi": "10.1161/HYPERTENSIONAHA.123.22981",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Hypertension/drug therapy",
            "*Diabetes Mellitus, Type 2/complications",
            "*Renal Insufficiency, Chronic/drug therapy",
            "Blood Pressure/physiology",
            "Antihypertensive Agents/therapeutic use",
            "Humans",
            "Adult",
        ],
        "abstract": (
            "Background: Optimal blood pressure targets in patients with coexisting type 2 "
            "diabetes (T2DM) and chronic kidney disease stage 3 (CKD3, eGFR 30-59) are "
            "undefined. Intensive lowering may protect kidneys but risk hypoperfusion. "
            "Methods: We randomised 2,184 adults with T2DM, CKD3, and SBP 130-179 mmHg "
            "to intensive (target SBP <120 mmHg) versus standard (target SBP <140 mmHg) "
            "treatment. Antihypertensive regimen was clinician-directed. Primary endpoint "
            "was composite of 40% eGFR decline, end-stage kidney disease, or death. "
            "Mean follow-up 4.1 years. "
            "Results: The intensive group achieved mean SBP 118.3 vs 133.7 mmHg in "
            "standard. Primary endpoint occurred in 14.2% intensive vs 19.8% standard "
            "(HR 0.69, 95% CI 0.58-0.83, P<0.001). Cardiovascular events were also reduced "
            "(HR 0.75, 95% CI 0.60-0.94). Serious hypotension occurred in 3.6% intensive "
            "vs 1.2% standard. AKI episodes were higher in intensive arm during initiation "
            "but resolved over 12 months. Subgroup analysis showed greatest benefit in "
            "patients with albuminuria >300 mg/g. "
            "Conclusions: Intensive BP control targeting SBP <120 mmHg significantly "
            "reduces kidney and cardiovascular events in T2DM-CKD3 patients (Level II, "
            "Grade A), at cost of modest increase in hypotension. Albuminuria severity "
            "should guide individualised target selection."
        ),
    },
    {
        "pmid": "37123456",
        "title": (
            "GLP-1 Receptor Agonists for Weight Loss and Glycaemic Control in Obese "
            "Adults with Type 2 Diabetes: A Network Meta-Analysis"
        ),
        "authors": ["Davies MJ", "Aroda VR", "Collins BS", "Buse JB"],
        "journal": "Diabetes Care",
        "journal_abbr": "Diabetes Care",
        "year": 2023,
        "volume": "46",
        "issue": "9",
        "pages": "1721-1734",
        "doi": "10.2337/dc23-0442",
        "publication_type": "META-ANALYSIS",
        "evidence_level": "Level I",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Glucagon-Like Peptide-1 Receptor/agonists",
            "*Diabetes Mellitus, Type 2/drug therapy",
            "*Obesity/drug therapy",
            "Hypoglycemic Agents/therapeutic use",
            "Glycated Hemoglobin/analysis",
            "Network Meta-Analysis",
            "Humans",
        ],
        "abstract": (
            "Background: Multiple GLP-1 receptor agonists (GLP-1 RAs) are now approved for "
            "T2DM and obesity, but direct head-to-head comparisons are scarce. Network "
            "meta-analysis allows indirect comparative efficacy estimates. "
            "Methods: We searched MEDLINE and CENTRAL for RCTs ≥24 weeks comparing GLP-1 "
            "RAs (semaglutide, liraglutide, dulaglutide, exenatide) against each other or "
            "placebo in adults with T2DM and BMI ≥30. Outcomes: HbA1c reduction, body "
            "weight change, hypoglycaemia, and GI adverse events. Sixty-one trials "
            "(n=52,413 patients) were included. "
            "Results: Semaglutide 2.4 mg weekly produced greatest HbA1c reduction "
            "(-1.8%, 95% CrI -2.1 to -1.5) and weight loss (-12.4 kg, 95% CrI -13.8 to "
            "-11.0) versus placebo. Dulaglutide 1.5 mg ranked second for HbA1c reduction. "
            "All GLP-1 RAs significantly reduced weight versus placebo (range -3.2 to "
            "-12.4 kg). Nausea was most common with semaglutide (21% vs 9% placebo) but "
            "transient. Hypoglycaemia rates were low across all agents. MACE reduction "
            "was confirmed for semaglutide and liraglutide but not dulaglutide or exenatide. "
            "Conclusions: Semaglutide 2.4 mg provides superior glycaemic and weight outcomes "
            "among GLP-1 RAs in obese T2DM patients (Level I, Grade A). Agent selection "
            "should balance efficacy, cost, dosing frequency, and individual cardiovascular "
            "risk profile."
        ),
    },
    {
        "pmid": "38441289",
        "title": (
            "Vasopressor Initiation Timing in Septic Shock: Early vs Delayed Norepinephrine "
            "and Effects on 28-Day Mortality"
        ),
        "authors": ["Lamontagne F", "Meade MO", "Hébert PC", "Asfar P"],
        "journal": "Critical Care Medicine",
        "journal_abbr": "Crit Care Med",
        "year": 2024,
        "volume": "52",
        "issue": "6",
        "pages": "878-890",
        "doi": "10.1097/CCM.0000000000006231",
        "publication_type": "RANDOMIZED CONTROLLED TRIAL",
        "evidence_level": "Level II",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Shock, Septic/therapy",
            "*Norepinephrine/administration & dosage",
            "*Vasoconstrictor Agents/therapeutic use",
            "Time-to-Treatment",
            "Intensive Care Units",
            "Humans",
        ],
        "abstract": (
            "Background: Current sepsis guidelines recommend vasopressors when MAP remains "
            "<65 mmHg despite fluid resuscitation, but the optimal timing of vasopressor "
            "initiation relative to fluid resuscitation is unknown. "
            "Methods: This parallel-group RCT enrolled 820 adults presenting to 12 ICUs "
            "with septic shock (MAP <65, suspected infection, lactate >2). The early "
            "vasopressor arm initiated norepinephrine within 1 hour of septic shock "
            "recognition. The delayed arm used fluid resuscitation alone for up to 3 hours "
            "before vasopressors. Norepinephrine target was MAP ≥65 mmHg in both arms. "
            "Primary outcome: 28-day mortality. Secondary: fluid volume at 6 hours, "
            "vasopressor-free days, organ failure (SOFA). "
            "Results: Twenty-eight-day mortality was 34.1% early vs 40.2% delayed "
            "(RR 0.85, 95% CI 0.72-0.99, P=0.04). Early norepinephrine reduced total fluid "
            "volume at 6h by 1.1 L (P<0.001). Vasopressor-free days were higher in early "
            "arm (16.8 vs 14.2 days, P=0.02). Serious adverse events were similar. "
            "Arrhythmia occurred in 11.2% early vs 9.8% delayed (P=0.52). "
            "Conclusions: Early norepinephrine initiation within 1 hour of septic shock "
            "recognition reduces 28-day mortality and fluid requirements compared to "
            "delayed initiation (Level II, Grade A). This challenges current protocol-first "
            "fluid approaches and supports earlier vasopressor use in haemodynamically "
            "unstable septic shock."
        ),
    },
    {
        "pmid": "37789012",
        "title": (
            "Canagliflozin and Renal Outcomes in Diabetic Nephropathy: "
            "Five-Year Follow-Up of the CREDENCE Trial Cohort"
        ),
        "authors": ["Perkovic V", "Jardine MJ", "Neal B", "Mahaffey KW"],
        "journal": "Journal of the American Society of Nephrology",
        "journal_abbr": "J Am Soc Nephrol",
        "year": 2023,
        "volume": "34",
        "issue": "8",
        "pages": "1398-1411",
        "doi": "10.1681/ASN.0000000000000171",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level I",
        "evidence_grade": "Grade A",
        "mesh_terms": [
            "*Diabetic Nephropathies/drug therapy",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "*Canagliflozin/therapeutic use",
            "Renal Insufficiency, Chronic/prevention & control",
            "Glomerular Filtration Rate/drug effects",
            "Humans",
        ],
        "abstract": (
            "Background: The CREDENCE trial demonstrated canagliflozin reduces end-stage "
            "kidney disease in diabetic nephropathy. Extended follow-up examines durability "
            "of renoprotective effects and off-treatment trajectories. "
            "Methods: Extended follow-up of 4,401 CREDENCE participants for 5 years "
            "(2 additional years post-randomised phase). Primary renal composite: sustained "
            "doubling of serum creatinine, ESKD, or renal death. Secondary: eGFR slope, "
            "cardiovascular events, all-cause mortality. "
            "Results: The primary renal composite was 24.2% canagliflozin vs 31.4% "
            "placebo (HR 0.72, 95% CI 0.62-0.83). eGFR slope in years 1-5 was -0.8 "
            "mL/min/1.73m² per year for canagliflozin vs -2.1 for placebo (P<0.001). "
            "Post-treatment eGFR trajectories remained diverged for 24 months after "
            "drug discontinuation, suggesting persistent renoprotection. ESKD occurred "
            "in 6.7% canagliflozin vs 10.2% placebo. Cardiovascular death and HF "
            "hospitalisation remained reduced (HR 0.79, 95% CI 0.66-0.95). "
            "Conclusions: Canagliflozin provides durable renoprotection over 5 years in "
            "diabetic nephropathy with persistent benefit for 24 months after treatment "
            "discontinuation (Level I, Grade A). Early initiation before significant eGFR "
            "decline maximises kidney-protective benefit."
        ),
    },
    {
        "pmid": "38198740",
        "title": (
            "Laparoscopic Cholecystectomy Complications and Risk Stratification: "
            "A Prospective Cohort Study of 18,420 Procedures"
        ),
        "authors": ["Strasberg SM", "Pucci MJ", "Brunt LM", "Deziel DJ"],
        "journal": "Annals of Surgery",
        "journal_abbr": "Ann Surg",
        "year": 2024,
        "volume": "279",
        "issue": "3",
        "pages": "442-451",
        "doi": "10.1097/SLA.0000000000006089",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II",
        "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Cholecystectomy, Laparoscopic/adverse effects",
            "*Bile Duct Injuries/etiology",
            "Intraoperative Complications",
            "Risk Factors",
            "Retrospective Studies",
            "Humans",
            "Postoperative Complications",
        ],
        "abstract": (
            "Background: Bile duct injury (BDI) remains the most serious complication of "
            "laparoscopic cholecystectomy (LC). Real-world incidence, risk factors, and "
            "outcomes from large prospective series are needed to inform surgical training "
            "and quality improvement. "
            "Methods: Prospective single-registry cohort study of 18,420 consecutive LC "
            "procedures across 34 hospitals (2019-2023). Data collected: operative time, "
            "conversion rate, intraoperative cholangiography use, BDI grade (Strasberg "
            "classification), and 90-day outcomes. Risk factors analysed by multivariate "
            "logistic regression. "
            "Results: BDI occurred in 0.38% of cases (n=70). Severe BDI (Strasberg E) "
            "represented 0.14% of all cases. Conversion to open was 4.2%. Independent "
            "risk factors for BDI: acute cholecystitis within 72h of surgery (OR 3.2, "
            "95% CI 2.1-4.8), obesity BMI >40 (OR 2.1), prior upper abdominal surgery "
            "(OR 1.9), and inexperienced surgeon (<50 LC cases, OR 4.7). Intraoperative "
            "cholangiography reduced BDI by 62% (OR 0.38, 95% CI 0.19-0.74). The critical "
            "view of safety (CVS) was documented in 71% of cases; CVS documentation "
            "associated with 79% lower BDI rate. "
            "Conclusions: BDI rate of 0.38% confirms LC safety at experienced centres "
            "(Level II, Grade B). Systematic CVS documentation and liberal intraoperative "
            "cholangiography use are the most effective preventive strategies, particularly "
            "for high-risk anatomy."
        ),
    },
    {
        "pmid": "37456789",
        "title": (
            "Atrial Fibrillation Detection Using Wearable Single-Lead ECG: "
            "Validation Against 24-Hour Holter Monitoring in 5,000 Patients"
        ),
        "authors": ["Hindricks G", "Potpara T", "Dagres N", "Arbelo E"],
        "journal": "European Heart Journal - Digital Health",
        "journal_abbr": "Eur Heart J Digit Health",
        "year": 2023,
        "volume": "4",
        "issue": "4",
        "pages": "298-308",
        "doi": "10.1093/ehjdh/ztad041",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II",
        "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Atrial Fibrillation/diagnosis",
            "*Wearable Electronic Devices",
            "*Electrocardiography, Ambulatory/methods",
            "Sensitivity and Specificity",
            "Humans",
            "Diagnosis, Computer-Assisted",
        ],
        "abstract": (
            "Background: Wearable single-lead ECG devices may enable opportunistic AF "
            "detection in community settings, but diagnostic accuracy versus standard "
            "Holter monitoring requires rigorous validation. "
            "Methods: Prospective cross-sectional study in 5,000 patients referred for "
            "Holter monitoring (palpitations, syncope, stroke surveillance). Each patient "
            "wore both the wearable device and standard 24-hour Holter simultaneously. "
            "Three cardiologists independently adjudicated AF episodes from Holter as "
            "ground truth. Wearable algorithm outputs were compared. "
            "Results: AF was confirmed in 18.3% by Holter (n=915). Wearable device "
            "sensitivity for AF was 93.4% (95% CI 91.6-95.0%), specificity 91.8% "
            "(90.8-92.8%), PPV 82.3%, NPV 97.3%. Per-patient 12-lead ECG confirmation "
            "raised PPV to 91.4%. Paroxysmal AF lasting <30 minutes had lower detection "
            "sensitivity (76.2%). Artefact rate was 8.4% of recorded periods. Performance "
            "was similar across age groups and BMI categories. "
            "Conclusions: Single-lead wearable ECG demonstrates high sensitivity and "
            "specificity for AF detection versus 24-hour Holter (Level II, Grade B). "
            "Low NPV supports use as a rule-out tool in symptomatic patients, with "
            "12-lead ECG confirmation recommended before initiating anticoagulation."
        ),
    },
    {
        "pmid": "38342156",
        "title": (
            "Sepsis-3 Criteria versus SIRS in Predicting 30-Day Mortality: "
            "Retrospective Analysis of 98,000 Hospital Admissions"
        ),
        "authors": ["Seymour CW", "Liu VX", "Iwashyna TJ", "Shankar-Hari M"],
        "journal": "Critical Care",
        "journal_abbr": "Crit Care",
        "year": 2024,
        "volume": "28",
        "issue": "1",
        "pages": "89",
        "doi": "10.1186/s13054-024-04872-z",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level III",
        "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Sepsis/diagnosis",
            "*Systemic Inflammatory Response Syndrome/diagnosis",
            "Hospital Mortality",
            "Organ Dysfunction Scores",
            "Retrospective Studies",
            "Humans",
            "Intensive Care Units",
        ],
        "abstract": (
            "Background: The Sepsis-3 definitions replaced SIRS-based criteria with organ "
            "dysfunction (SOFA ≥2) as the diagnostic cornerstone. Whether this improves "
            "mortality prediction in routine clinical practice remains debated. "
            "Methods: Retrospective analysis of 98,241 hospital admissions with suspected "
            "infection at 12 US academic medical centres (2018-2022). We compared sepsis "
            "defined by SIRS ≥2 plus infection versus Sepsis-3 (SOFA ≥2 plus infection) "
            "for 30-day mortality prediction. Secondary outcomes: ICU admission, vasopressor "
            "use, mechanical ventilation. C-statistics and net reclassification improvement "
            "calculated. "
            "Results: Sepsis-3 criteria identified 31.2% of admissions, SIRS ≥2 identified "
            "52.8%. Sepsis-3 C-statistic for 30-day mortality: 0.74 vs SIRS C-statistic "
            "0.64 (difference 0.10, P<0.001). Patients meeting Sepsis-3 only (not SIRS) "
            "had higher mortality than SIRS-only patients (24.3% vs 8.2%, P<0.001). NRI "
            "0.28 (95% CI 0.22-0.34) favoured Sepsis-3. qSOFA ≥2 had C-statistic 0.71 "
            "with high specificity (98.9%) but low sensitivity (28.5%). "
            "Conclusions: Sepsis-3 criteria significantly outperform SIRS in predicting "
            "30-day mortality in hospitalised patients with infection (Level III, Grade B). "
            "qSOFA is highly specific but misses sepsis cases; SOFA-based criteria should "
            "remain primary in ICU settings while qSOFA serves as bedside screen."
        ),
    },
    {
        "pmid": "37654987",
        "title": (
            "Robotic-Assisted versus Laparoscopic Cholecystectomy: Operative Outcomes "
            "from a Propensity-Matched National Database Study"
        ),
        "authors": ["Azagury D", "Liu RC", "Morgan A", "Curet MJ"],
        "journal": "JAMA Surgery",
        "journal_abbr": "JAMA Surg",
        "year": 2023,
        "volume": "158",
        "issue": "10",
        "pages": "1089-1097",
        "doi": "10.1001/jamasurg.2023.3442",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level III",
        "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Cholecystectomy, Laparoscopic/methods",
            "*Robotic Surgical Procedures/methods",
            "Postoperative Complications",
            "Operative Time",
            "Treatment Outcome",
            "Propensity Score",
            "Humans",
        ],
        "abstract": (
            "Background: Robotic-assisted cholecystectomy adoption is increasing despite "
            "limited comparative safety data versus standard laparoscopic approach. "
            "Propensity-matched analysis may reduce confounding from patient selection. "
            "Methods: We queried the American College of Surgeons NSQIP database for all "
            "elective cholecystectomies (2019-2022). After propensity matching on age, BMI, "
            "ASA class, and operative indication, 14,228 robotic-assisted were matched to "
            "14,228 laparoscopic cases. Primary outcome: 30-day major complication rate. "
            "Secondary: operative time, conversion, bile duct injury, readmission. "
            "Results: Major complication rate was equivalent: robotic 3.1% vs laparoscopic "
            "3.4% (OR 0.91, 95% CI 0.78-1.07, P=0.26). Operative time was longer for "
            "robotic (68 min vs 51 min, P<0.001). Bile duct injury rate: robotic 0.24% vs "
            "laparoscopic 0.31% (OR 0.78, 95% CI 0.48-1.26, P=0.31). Conversion rates "
            "were similar (robotic 2.8% vs laparoscopic 3.1%). Readmission within 30 days "
            "was equivalent (4.2% vs 4.5%). Hospital cost was 34% higher for robotic. "
            "Conclusions: Robotic-assisted cholecystectomy provides equivalent safety to "
            "laparoscopic approach but with longer operative times and substantially higher "
            "cost (Level III, Grade B). Routine adoption of robotic approach for "
            "uncomplicated cholecystectomy is not supported by current evidence."
        ),
    },
    {
        "pmid": "38123409",
        "title": (
            "Clinical Decision Support for Sepsis Recognition: Alert Fatigue "
            "and Override Rates in a Tertiary Care System"
        ),
        "authors": ["Rhee C", "Dantes R", "Epstein L", "Murphy DJ"],
        "journal": "Journal of Hospital Medicine",
        "journal_abbr": "J Hosp Med",
        "year": 2024,
        "volume": "19",
        "issue": "3",
        "pages": "211-219",
        "doi": "10.1002/jhm.13292",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level III",
        "evidence_grade": "Grade C",
        "mesh_terms": [
            "*Sepsis/diagnosis",
            "*Decision Support Systems, Clinical",
            "Alert Fatigue, Health Personnel",
            "Electronic Health Records",
            "Humans",
            "Hospital Information Systems",
        ],
        "abstract": (
            "Background: Sepsis alert systems improve recognition but generate high rates of "
            "false-positive alerts, leading to alert fatigue and reduced adherence. "
            "Quantifying override rates and factors associated with appropriate versus "
            "inappropriate override is needed for system optimisation. "
            "Methods: Retrospective analysis of 48,291 sepsis alerts generated at a "
            "500-bed tertiary hospital over 24 months. Alerts were classified as "
            "appropriate (confirmed sepsis within 12h), false positive (no sepsis), or "
            "late (sepsis confirmed but alert delayed). Clinician override was defined as "
            "alert acknowledged without bundle initiation. Multivariate analysis identified "
            "predictors of override. "
            "Results: Alert positive predictive value was 31.2%. False-positive rate was "
            "68.8%. Clinician override rate was 54.2%; 82.4% of overrides were appropriate "
            "(true false positives). Alert fatigue increased over the 24 months (override "
            "rate rose from 44% to 62%, P<0.001). Highest override rates occurred on "
            "night shifts (61%) and in non-ICU wards (67%). Machine learning re-calibration "
            "using 8 features reduced false-positive alerts by 41% without increasing "
            "missed sepsis cases. "
            "Conclusions: Current sepsis alert systems suffer from high false-positive rates "
            "driving alert fatigue (Level III, Grade C). Machine learning optimisation "
            "reduces false positives substantially. Human-in-the-loop review workflows "
            "must account for clinician override patterns to maintain system effectiveness."
        ),
    },
    {
        "pmid": "37891234",
        "title": (
            "Metformin versus SGLT2 Inhibitor as First-Line Therapy in Newly Diagnosed "
            "Type 2 Diabetes with High Cardiovascular Risk"
        ),
        "authors": ["Kosiborod MN", "Lam CSP", "Kohsaka S", "Kim DJ"],
        "journal": "Journal of Clinical Endocrinology & Metabolism",
        "journal_abbr": "J Clin Endocrinol Metab",
        "year": 2023,
        "volume": "108",
        "issue": "7",
        "pages": "1802-1814",
        "doi": "10.1210/clinem/dgad142",
        "publication_type": "JOURNAL ARTICLE",
        "evidence_level": "Level II",
        "evidence_grade": "Grade B",
        "mesh_terms": [
            "*Metformin/therapeutic use",
            "*Sodium-Glucose Transporter 2 Inhibitors/therapeutic use",
            "*Diabetes Mellitus, Type 2/drug therapy",
            "Cardiovascular Diseases/prevention & control",
            "Hypoglycemic Agents/therapeutic use",
            "Humans",
        ],
        "abstract": (
            "Background: Current T2DM guidelines recommend metformin as first-line therapy, "
            "but SGLT2 inhibitors have demonstrated superior cardiovascular and renal "
            "outcomes. Whether SGLT2 inhibitors should replace metformin as initial therapy "
            "in high cardiovascular risk patients remains unresolved. "
            "Methods: Propensity-matched cohort study (n=24,816) of newly diagnosed T2DM "
            "patients with established cardiovascular disease initiating either metformin "
            "or empagliflozin as monotherapy (2017-2022). Primary outcome: composite of "
            "MACE (cardiovascular death, MI, stroke). Secondary: HbA1c at 12 months, "
            "heart failure hospitalisation, renal outcomes. Median follow-up 2.8 years. "
            "Results: MACE occurred in 6.8% empagliflozin vs 9.2% metformin (HR 0.73, "
            "95% CI 0.62-0.87, P<0.001). HbA1c reduction at 12 months was similar "
            "(-0.9% vs -0.8%). Heart failure hospitalisation: 2.1% vs 3.8% (HR 0.54). "
            "Renal composite (>40% eGFR decline or ESKD): 1.3% vs 2.4% (HR 0.54). "
            "Empagliflozin was associated with more genital mycotic infections (6.1% vs "
            "1.2%) but similar hypoglycaemia. "
            "Conclusions: Empagliflozin as initial monotherapy provides superior "
            "cardiovascular and renal outcomes versus metformin in high-risk T2DM (Level II, "
            "Grade B). These data support re-evaluation of metformin as default first-line "
            "in high cardiovascular risk patients, pending prospective RCT confirmation."
        ),
    },
]


# ── Public API ────────────────────────────────────────────────────────────────

def get_research_corpus() -> list[Document]:
    """
    Returns the synthetic research corpus as Document objects.
    Each document contains a full clinical abstract with rich metadata.
    Tag: SYNTHETIC — realistic structure, no real publications.
    """
    docs = []
    for rec in _ABSTRACTS:
        text = (
            f"Title: {rec['title']}\n\n"
            f"Authors: {', '.join(rec['authors'])}\n"
            f"Journal: {rec['journal']} ({rec['journal_abbr']}). "
            f"{rec['year']};{rec['volume']}({rec['issue']}):{rec['pages']}.\n"
            f"DOI: {rec['doi']}\n"
            f"Publication Type: {rec['publication_type']}\n"
            f"Evidence: {rec['evidence_level']}, {rec['evidence_grade']}\n\n"
            f"Abstract:\n{rec['abstract']}\n\n"
            f"MeSH Terms: {'; '.join(rec['mesh_terms'])}"
        )
        metadata = {
            "pmid": rec["pmid"],
            "title": rec["title"],
            "authors": rec["authors"],
            "journal": rec["journal"],
            "year": rec["year"],
            "doi": rec["doi"],
            "source_type": "pubmed_abstract",
            "evidence_level": rec["evidence_level"],
            "evidence_grade": rec["evidence_grade"],
            "publication_type": rec["publication_type"],
            "mesh_terms": rec["mesh_terms"],
        }
        docs.append(
            Document(
                id=f"pubmed-{rec['pmid']}",
                text=text,
                metadata=metadata,
                tag=DataTag.SYNTHETIC,
            )
        )
    return docs
