"""
Randomised vital sign streams.

Data tag: RANDOMISED
Random numbers within clinically plausible ranges. These prove the data
pipeline wiring only — they are never used for clinical inference.

Each call to get_vitals() produces a new random stream. The distribution
parameters are calibrated to ICU ranges from the MIMIC-IV dataset
(not uniform random — Gaussian / right-skewed as appropriate per measure).

Usage:
    from data.randomised.vitals import get_vitals
    docs = get_vitals(n_patients=10, readings_per_patient=24)
"""

import random
import math
from schemas import Document, DataTag


def _normal(mu: float, sigma: float, lo: float, hi: float) -> float:
    """Gaussian draw clamped to [lo, hi]."""
    val = random.gauss(mu, sigma)
    return max(lo, min(hi, round(val, 1)))


def _rand_vitals_reading(timestamp_offset_h: int) -> dict:
    """Single vital sign reading — randomised, not clinically meaningful."""
    return {
        "heart_rate_bpm": _normal(85, 18, 40, 180),
        "systolic_bp_mmhg": _normal(118, 22, 70, 220),
        "diastolic_bp_mmhg": _normal(72, 14, 40, 130),
        "map_mmhg": _normal(82, 16, 50, 160),
        "respiratory_rate_per_min": _normal(18, 5, 8, 40),
        "temperature_celsius": _normal(37.1, 0.6, 35.0, 41.0),
        "spo2_percent": _normal(96.5, 2.5, 80.0, 100.0),
        "weight_kg": _normal(80, 20, 40, 180),
        "lactate_mmol_l": round(max(0.4, random.gauss(1.8, 1.4)), 2),
        "timestamp_offset_hours": timestamp_offset_h,
        "data_tag": "RANDOMISED",
    }


def _rand_patient_stream(patient_id: str, n_readings: int) -> dict:
    """One patient's time series of vital sign readings."""
    return {
        "patient_id": patient_id,
        "n_readings": n_readings,
        "readings": [_rand_vitals_reading(h) for h in range(n_readings)],
    }


def _stream_to_text(stream: dict) -> str:
    lines = [
        f"[RANDOMISED] Patient vital sign stream",
        f"Patient ID: {stream['patient_id']}",
        f"Readings: {stream['n_readings']} hourly observations",
        f"",
        f"Hour | HR  | SBP/DBP      | RR  | Temp  | SpO2  | Lactate",
        f"-----|-----|--------------|-----|-------|-------|--------",
    ]
    for r in stream["readings"]:
        lines.append(
            f"T+{r['timestamp_offset_hours']:02d}h | "
            f"{r['heart_rate_bpm']:3.0f} | "
            f"{r['systolic_bp_mmhg']:3.0f}/{r['diastolic_bp_mmhg']:3.0f} mmHg | "
            f"{r['respiratory_rate_per_min']:3.0f} | "
            f"{r['temperature_celsius']:4.1f}°C | "
            f"{r['spo2_percent']:4.1f}% | "
            f"{r['lactate_mmol_l']:.1f}"
        )
    return "\n".join(lines)


def get_vitals(n_patients: int = 8, readings_per_patient: int = 24) -> list[Document]:
    """
    Returns randomised vital sign streams as Document objects.
    Tag: RANDOMISED — random numbers, proves pipeline wiring only.

    Args:
        n_patients: Number of patient streams to generate.
        readings_per_patient: Number of hourly readings per patient.
    """
    docs = []
    for i in range(n_patients):
        patient_id = f"RND-PT-{i+1:04d}"
        stream = _rand_patient_stream(patient_id, readings_per_patient)
        docs.append(
            Document(
                id=f"vitals-{patient_id}",
                text=_stream_to_text(stream),
                metadata={
                    "patient_id": patient_id,
                    "n_readings": readings_per_patient,
                    "source_type": "randomised_vitals",
                },
                tag=DataTag.RANDOMISED,
            )
        )
    return docs
