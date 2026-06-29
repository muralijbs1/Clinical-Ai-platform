#!/usr/bin/env python3
"""
Generator: writes randomised surgical frame detections as a JSON file.

Run once to produce the data file. Re-run to produce a new random snapshot.
Output: data/randomised/surgical_frames.json

Structure follows the Cholec80 annotation schema: bounding box (normalised 0-1),
tool/anatomy class label, confidence, surgical phase. Fixed seed (42) for reproducibility.

DATA TAG: RANDOMISED — random values prove pipeline wiring only, no clinical meaning.
"""

import json
import random
from pathlib import Path

random.seed(42)

_OUT_FILE = Path(__file__).parent.parent / "surgical_frames.json"

_N_FRAMES = 300
_PROCEDURE = "Laparoscopic Cholecystectomy"
_FPS = 25

_PHASES = [
    "Preparation", "CalotTriangleDissection", "ClippingCutting",
    "GallbladderDissection", "GallbladderPackaging",
    "CleaningCoagulation", "GallbladderRetraction",
]
# Rebalanced from original [0.06, 0.25, 0.10, 0.35, 0.08, 0.10, 0.06]:
# Preparation, GallbladderPackaging, GallbladderRetraction boosted to 0.10;
# GallbladderDissection reduced from dominant 0.35 → 0.22 to reduce skew.
_PHASE_WEIGHTS = [0.10, 0.20, 0.13, 0.22, 0.13, 0.12, 0.10]
_TOOL_CLASSES = ["Grasper", "Clipper", "Coagulator", "Scissors", "Irrigator", "SpecimenBag"]
_ANATOMY_CLASSES = ["Gallbladder", "Liver", "CalotTriangle", "CysticDuct", "CysticArtery", "Clip"]
_PHASE_CONFIDENCE = {
    "Preparation": (0.82, 0.10), "CalotTriangleDissection": (0.68, 0.18),
    "ClippingCutting": (0.88, 0.08), "GallbladderDissection": (0.71, 0.16),
    "GallbladderPackaging": (0.85, 0.09), "CleaningCoagulation": (0.76, 0.14),
    "GallbladderRetraction": (0.84, 0.11),
}
_RISK_FLAGS = [
    "proximity_to_common_bile_duct", "bleeding_risk_elevation",
    "bile_spillage_risk", "critical_view_not_achieved",
    None, None, None, None, None,
]


def _phase_at(frame_idx: int, total: int) -> str:
    ratio = frame_idx / max(total - 1, 1)
    cumulative = 0.0
    for phase, weight in zip(_PHASES, _PHASE_WEIGHTS):
        cumulative += weight
        if ratio <= cumulative:
            return phase
    return _PHASES[-1]


def _confidence(phase: str) -> float:
    mu, sigma = _PHASE_CONFIDENCE[phase]
    return round(max(0.1, min(1.0, random.gauss(mu, sigma))), 3)


def _detection(phase: str) -> dict:
    is_tool = random.random() < 0.55
    label = random.choice(_TOOL_CLASSES if is_tool else _ANATOMY_CLASSES)
    x = round(random.uniform(0.05, 0.85), 3)
    y = round(random.uniform(0.05, 0.85), 3)
    w = round(random.uniform(0.05, min(0.4, 1.0 - x)), 3)
    h = round(random.uniform(0.05, min(0.4, 1.0 - y)), 3)
    d = {
        "label": label,
        "category": "tool" if is_tool else "anatomy",
        "confidence": _confidence(phase),
        "bbox_normalised": {"x": x, "y": y, "w": w, "h": h},
    }
    risk_flag = random.choice(_RISK_FLAGS)
    if risk_flag:
        d["risk_flag"] = risk_flag
        d["risk_composite_score"] = round(random.uniform(0.4, 0.9), 3)
    return d


def write_files() -> None:
    frames = []
    for i in range(_N_FRAMES):
        phase = _phase_at(i, _N_FRAMES)
        frames.append({
            "frame_index": i,
            "timestamp_s": round(i / _FPS, 2),
            "phase": phase,
            "phase_confidence": _confidence(phase),
            "detections": [_detection(phase) for _ in range(random.randint(1, 4))],
        })

    payload = {
        "data_tag": "RANDOMISED",
        "procedure": _PROCEDURE,
        "n_frames": _N_FRAMES,
        "fps": _FPS,
        "random_seed": 42,
        "phases": _PHASES,
        "frames": frames,
    }

    with open(_OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"surgical_frames: {_N_FRAMES} frames (rebalanced phases) → {_OUT_FILE}")


if __name__ == "__main__":
    write_files()
