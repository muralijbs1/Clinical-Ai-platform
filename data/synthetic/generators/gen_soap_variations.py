#!/usr/bin/env python3
"""
Generates clinically safe variations of the 52 hand-authored SOAP notes.

Each archetype produces N_VARIATIONS new notes by changing ONLY:
  - DATE / TIME
  - PROVIDER name (from a curated pool)
  - Patient age in HPI (±AGE_DELTA years, clamped to condition-safe bounds)
  - Vital signs (±VITALS_PCT%, clamped to physiologically sane ranges)

Everything clinical — diagnosis, plan, medications, ICD codes, reasoning — is
preserved exactly. Sex is never changed (many conditions are sex-specific).

DATA TAG: SYNTHETIC
Output: data/synthetic/transcripts/note_053.txt … note_NNN.txt
"""

import re
import random
from pathlib import Path

random.seed(99)

_TRANSCRIPTS_DIR = Path(__file__).parent.parent / "transcripts"
_N_VARIATIONS    = 10     # per archetype
_AGE_DELTA       = 7      # ± years of age variation
_VITALS_PCT      = 0.08   # ± 8% on numeric vital values

# Provider name pool (fictional)
_PROVIDERS = [
    "Dr. Aisha Nkemdirim", "Dr. Marcus Lee", "Dr. Priya Patel",
    "Dr. James Okafor", "Dr. Rachel Torres", "Dr. Brendan Murphy",
    "Dr. Yuki Tanaka", "Dr. Nina Osei", "Dr. Samuel Adeyemi",
    "Dr. Mark Chen", "Dr. Angela Foster", "Dr. Keisha Thompson",
    "Dr. Jordan Lee", "Dr. Priya Anand", "Dr. Amanda Walsh",
    "Dr. Nguyen Van Minh", "Dr. Elena Rossi", "Dr. Patrick Brennan",
    "Dr. Alicia Nwosu", "Dr. Marcus Williams", "Dr. Sophie Hart",
    "Dr. Liam O'Brien", "Dr. Fatima Al-Rashidi", "Dr. Carlos Rivera",
    "Dr. Hannah Kim", "Dr. David Okonkwo", "Dr. Sarah Mitchell",
    "Dr. Thomas Andersson", "Dr. Meera Krishnaswamy", "Dr. Wei Zhang",
]

# Specialties extracted from each note (to keep provider + specialty consistent)
_SPECIALTIES = [
    "Emergency Medicine", "General Medicine", "Cardiology",
    "Neurology", "Gastroenterology", "Respiratory Medicine",
    "Intensive Care Medicine", "Family Medicine", "Internal Medicine",
    "Obstetrics & Gynaecology", "Paediatrics", "Geriatric Medicine",
    "Nephrology", "Hepatology", "Endocrinology", "Haematology",
    "Oncology", "Rheumatology", "Orthopaedics", "Psychiatry",
    "Pre-Operative Assessment", "Neurocritical Care",
]

# Vital sign field: (regex pattern, min_value, max_value, is_integer)
_VITAL_PATTERNS = [
    # BP: match e.g. "BP 118/74"  or  "BP 102/64 (improving to 110/72 post-adrenaline)"
    # We only vary the first BP pair found
    (r'BP (\d{2,3})/(\d{2,3})', "bp"),
    (r'HR (\d{2,3})',            "hr"),
    (r'RR (\d{1,2})',            "rr"),
    (r'Temp (\d{2})\.(\d)',      "temp"),
    (r'SpO2 (\d{2,3})',          "spo2"),
    (r'BMI (\d{2})\.(\d)',       "bmi"),
]

# Age bounds per encounter context (to avoid e.g. 2-year-old becoming 9-year-old)
# Key = substring in the original HPI age line; Value = (min_age, max_age)
_AGE_BOUNDS_OVERRIDES = {
    "2 yo": (1, 4),      # paediatric febrile convulsion
    "yo M 2": (1, 4),
    " yo F 2": (1, 4),
    "19 yo": (16, 25),   # status epilepticus young adult
    "22 yo": (18, 30),   # DKA
    "27 yo": (22, 35),   # preterm labour
    "29 yo": (22, 38),
    "31 yo": (24, 40),
    "84 yo": (78, 92),   # geriatric
}
_AGE_DEFAULT_BOUNDS = (18, 90)


def _vary_age(text: str, seed_age: int) -> tuple[str, int]:
    """Replace '[seed_age] yo' with a new age within clinically safe bounds."""
    # Determine bounds
    lo, hi = _AGE_DEFAULT_BOUNDS
    for marker, bounds in _AGE_BOUNDS_OVERRIDES.items():
        if marker in text:
            lo, hi = bounds
            break

    delta = random.randint(-_AGE_DELTA, _AGE_DELTA)
    new_age = max(lo, min(hi, seed_age + delta))
    # Replace first occurrence of the exact age pattern in HPI
    new_text = re.sub(
        rf'\b{seed_age} yo\b',
        f'{new_age} yo',
        text, count=1
    )
    return new_text, new_age


def _nudge(value: float, lo: float, hi: float, integer: bool = True) -> str:
    factor = 1.0 + random.uniform(-_VITALS_PCT, _VITALS_PCT)
    result = max(lo, min(hi, value * factor))
    return str(int(round(result))) if integer else f"{result:.1f}"


def _vary_vitals(text: str) -> str:
    # BP
    def replace_bp(m):
        sys_ = int(m.group(1))
        dia_ = int(m.group(2))
        new_s = _nudge(sys_, 60, 220)
        new_d = _nudge(dia_, 40, 130)
        # Ensure systolic > diastolic
        if int(new_s) <= int(new_d):
            new_d = str(int(new_s) - random.randint(20, 35))
        return f"BP {new_s}/{new_d}"

    text = re.sub(r'BP (\d{2,3})/(\d{2,3})', replace_bp, text, count=1)

    def replace_hr(m):
        return f"HR {_nudge(int(m.group(1)), 40, 180)}"
    text = re.sub(r'HR (\d{2,3})', replace_hr, text, count=1)

    def replace_rr(m):
        return f"RR {_nudge(int(m.group(1)), 8, 40)}"
    text = re.sub(r'RR (\d{1,2})', replace_rr, text, count=1)

    def replace_temp(m):
        val = float(f"{m.group(1)}.{m.group(2)}")
        new_v = _nudge(val, 35.0, 41.5, integer=False)
        return f"Temp {new_v}"
    text = re.sub(r'Temp (\d{2})\.(\d)', replace_temp, text, count=1)

    def replace_spo2(m):
        return f"SpO2 {_nudge(int(m.group(1)), 70, 100)}"
    text = re.sub(r'SpO2 (\d{2,3})', replace_spo2, text, count=1)

    return text


def _vary_date(text: str) -> str:
    year  = random.randint(2023, 2025)
    month = random.randint(1, 12)
    day   = random.randint(1, 28)
    hour  = random.randint(0, 23)
    minute = random.choice([0, 15, 30, 45])
    new_date = f"{year}-{month:02d}-{day:02d}"
    new_time = f"{hour:02d}:{minute:02d}"
    text = re.sub(r'DATE:\s*\d{4}-\d{2}-\d{2}', f'DATE: {new_date}', text, count=1)
    text = re.sub(r'TIME:\s*\d{2}:\d{2}', f'TIME: {new_time}', text, count=1)
    return text


def _vary_provider(text: str, original_specialty: str) -> str:
    provider = random.choice(_PROVIDERS)
    # Try to keep the same specialty (found in original text)
    spec = original_specialty
    new_prov_line = f"{provider}, MD ({spec})"
    text = re.sub(r'PROVIDER:\s*Dr\.[^\n]+', f'PROVIDER: {new_prov_line}', text, count=1)
    return text


def _extract_age(text: str) -> int | None:
    m = re.search(r'(\d{1,3}) yo [MF]', text)
    return int(m.group(1)) if m else None


def _extract_specialty(text: str) -> str:
    m = re.search(r'PROVIDER:[^\(]+\(([^)]+)\)', text)
    return m.group(1).strip() if m else "General Medicine"


def generate_variations() -> None:
    source_files = sorted(_TRANSCRIPTS_DIR.glob("note_*.txt"))
    # Only vary the originals (001-052); skip any previously generated variations
    source_files = [f for f in source_files if int(f.stem.split("_")[1]) <= 52]

    # Find the next available note number
    all_existing = sorted(_TRANSCRIPTS_DIR.glob("note_*.txt"))
    next_num = max(int(f.stem.split("_")[1]) for f in all_existing) + 1 if all_existing else 53

    generated = 0
    for src in source_files:
        original = src.read_text()
        age = _extract_age(original)
        specialty = _extract_specialty(original)

        for _ in range(_N_VARIATIONS):
            varied = original

            # 1. Date / time
            varied = _vary_date(varied)

            # 2. Provider
            varied = _vary_provider(varied, specialty)

            # 3. Age (only if age found and not a very young child — protect paediatric accuracy)
            if age is not None and age > 3:
                varied, _ = _vary_age(varied, age)

            # 4. Vital signs
            varied = _vary_vitals(varied)

            # Write
            out_path = _TRANSCRIPTS_DIR / f"note_{next_num:03d}.txt"
            out_path.write_text(varied, encoding="utf-8")
            next_num += 1
            generated += 1

    print(f"Generated {generated} SOAP note variations → {_TRANSCRIPTS_DIR}")
    print(f"Total notes now: {len(list(_TRANSCRIPTS_DIR.glob('*.txt')))}")


if __name__ == "__main__":
    generate_variations()
