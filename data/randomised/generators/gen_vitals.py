#!/usr/bin/env python3
"""
Generator: writes randomised ICU vital sign streams as a CSV file.

Run once to produce the data file. Re-run to produce a new random snapshot.
Output: data/randomised/vitals.csv

One row per reading per patient. Distribution parameters calibrated to
MIMIC-IV ICU ranges. Fixed random seed (42) for reproducibility.

DATA TAG: RANDOMISED — random values prove pipeline wiring only, no clinical meaning.
"""

import csv
import math
import random
from pathlib import Path

random.seed(42)

_OUT_FILE = Path(__file__).parent.parent / "vitals.csv"

_N_PATIENTS = 8
_READINGS_PER_PATIENT = 24

_FIELDNAMES = [
    "patient_id", "timestamp_offset_hours",
    "heart_rate_bpm", "systolic_bp_mmhg", "diastolic_bp_mmhg", "map_mmhg",
    "respiratory_rate_per_min", "temperature_celsius", "spo2_percent",
    "weight_kg", "lactate_mmol_l", "data_tag",
]


def _normal(mu: float, sigma: float, lo: float, hi: float) -> float:
    val = random.gauss(mu, sigma)
    return max(lo, min(hi, round(val, 1)))


def _reading(patient_id: str, offset_h: int) -> dict:
    return {
        "patient_id": patient_id,
        "timestamp_offset_hours": offset_h,
        "heart_rate_bpm": _normal(85, 18, 40, 180),
        "systolic_bp_mmhg": _normal(118, 22, 70, 220),
        "diastolic_bp_mmhg": _normal(72, 14, 40, 130),
        "map_mmhg": _normal(82, 16, 50, 160),
        "respiratory_rate_per_min": _normal(18, 5, 8, 40),
        "temperature_celsius": _normal(37.1, 0.6, 35.0, 41.0),
        "spo2_percent": _normal(96.5, 2.5, 80.0, 100.0),
        "weight_kg": _normal(80, 20, 40, 180),
        "lactate_mmol_l": round(max(0.4, random.gauss(1.8, 1.4)), 2),
        "data_tag": "RANDOMISED",
    }


def write_files() -> None:
    rows = []
    for i in range(_N_PATIENTS):
        pid = f"RND-PT-{i+1:04d}"
        for h in range(_READINGS_PER_PATIENT):
            rows.append(_reading(pid, h))

    with open(_OUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"vitals: {len(rows)} rows ({_N_PATIENTS} patients × {_READINGS_PER_PATIENT} readings) → {_OUT_FILE}")


if __name__ == "__main__":
    write_files()
