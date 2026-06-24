"""
Randomised surgical video frame detections — Cholec80 format.

Data tag: RANDOMISED
Randomly generated frame-level object detections for a laparoscopic
cholecystectomy simulation. Structure follows the Cholec80 annotation schema:
bounding box (x, y, w, h normalised 0-1), tool/anatomy class label,
confidence score, and surgical phase label.

These prove the surgical agent pipeline wiring only.
Values are random — they carry no clinical meaning.

7 cholecystectomy phases (from Cholec80):
  0 Preparation      1 CalotTriangleDissection   2 ClippingCutting
  3 GallbladderDissection   4 GallbladderPackaging
  5 CleaningCoagulation     6 GallbladderRetraction

Tool classes: Grasper, Clipper, Coagulator, Scissors, Irrigator, SpecimenBag
Anatomy classes: Gallbladder, Liver, CalotTriangle, CysticDuct, CysticArtery, Clip

Usage:
    from data.randomised.surgical_frames import get_surgical_frames
    docs = get_surgical_frames(n_frames=50)
"""

import random
import math
from schemas import Document, DataTag


_PHASES = [
    "Preparation",
    "CalotTriangleDissection",
    "ClippingCutting",
    "GallbladderDissection",
    "GallbladderPackaging",
    "CleaningCoagulation",
    "GallbladderRetraction",
]

# Approximate frame counts per phase for a 45-min / 25fps procedure
# Total ~67,500 frames; distribution based on Cholec80 typical timings
_PHASE_WEIGHTS = [0.06, 0.25, 0.10, 0.35, 0.08, 0.10, 0.06]

_TOOL_CLASSES = ["Grasper", "Clipper", "Coagulator", "Scissors", "Irrigator", "SpecimenBag"]
_ANATOMY_CLASSES = ["Gallbladder", "Liver", "CalotTriangle", "CysticDuct", "CysticArtery", "Clip"]

# Confidence mean/std per phase (from Cholec80 literature)
_PHASE_CONFIDENCE_PARAMS = {
    "Preparation":              {"mean": 0.82, "std": 0.10},
    "CalotTriangleDissection":  {"mean": 0.68, "std": 0.18},
    "ClippingCutting":          {"mean": 0.88, "std": 0.08},
    "GallbladderDissection":    {"mean": 0.71, "std": 0.16},
    "GallbladderPackaging":     {"mean": 0.85, "std": 0.09},
    "CleaningCoagulation":      {"mean": 0.76, "std": 0.14},
    "GallbladderRetraction":    {"mean": 0.84, "std": 0.11},
}

_RISK_FLAGS = [
    "proximity_to_common_bile_duct",
    "bleeding_risk_elevation",
    "bile_spillage_risk",
    "critical_view_not_achieved",
    None, None, None, None, None,  # majority null
]


def _phase_at_frame(frame_idx: int, total_frames: int) -> str:
    """Assign a surgical phase based on frame position."""
    cumulative = 0.0
    ratio = frame_idx / max(total_frames - 1, 1)
    for phase, weight in zip(_PHASES, _PHASE_WEIGHTS):
        cumulative += weight
        if ratio <= cumulative:
            return phase
    return _PHASES[-1]


def _rand_bbox() -> dict[str, float]:
    """Random bounding box (normalised 0-1)."""
    x = round(random.uniform(0.05, 0.85), 3)
    y = round(random.uniform(0.05, 0.85), 3)
    w = round(random.uniform(0.05, min(0.4, 1.0 - x)), 3)
    h = round(random.uniform(0.05, min(0.4, 1.0 - y)), 3)
    return {"x": x, "y": y, "w": w, "h": h}


def _rand_confidence(phase: str) -> float:
    params = _PHASE_CONFIDENCE_PARAMS[phase]
    raw = random.gauss(params["mean"], params["std"])
    return round(max(0.1, min(1.0, raw)), 3)


def _rand_detection(phase: str) -> dict:
    """One detected object in a frame."""
    is_tool = random.random() < 0.55
    label = random.choice(_TOOL_CLASSES if is_tool else _ANATOMY_CLASSES)
    conf = _rand_confidence(phase)
    risk_flag = random.choice(_RISK_FLAGS)
    detection = {
        "label": label,
        "category": "tool" if is_tool else "anatomy",
        "confidence": conf,
        "bbox_normalised": _rand_bbox(),
    }
    if risk_flag:
        detection["risk_flag"] = risk_flag
        detection["risk_composite_score"] = round(random.uniform(0.4, 0.9), 3)
    return detection


def _rand_frame(frame_idx: int, total_frames: int, fps: int = 25) -> dict:
    """One annotated video frame."""
    phase = _phase_at_frame(frame_idx, total_frames)
    n_detections = random.randint(1, 4)
    timestamp_s = round(frame_idx / fps, 2)
    return {
        "frame_index": frame_idx,
        "timestamp_s": timestamp_s,
        "phase": phase,
        "phase_confidence": _rand_confidence(phase),
        "detections": [_rand_detection(phase) for _ in range(n_detections)],
        "data_tag": "RANDOMISED",
    }


def _frames_to_text(frames: list[dict], procedure: str) -> str:
    lines = [
        f"[RANDOMISED] Surgical Frame Detections",
        f"Procedure: {procedure}",
        f"Total frames: {len(frames)} | FPS: 25",
        f"",
    ]
    for f in frames:
        det_summary = "; ".join(
            f"{d['label']}({d['confidence']:.2f})" for d in f["detections"]
        )
        risk_flags = [
            d.get("risk_flag") for d in f["detections"] if d.get("risk_flag")
        ]
        risk_str = f" | RISK: {', '.join(risk_flags)}" if risk_flags else ""
        lines.append(
            f"Frame {f['frame_index']:05d} t={f['timestamp_s']:6.1f}s "
            f"[{f['phase']}] {det_summary}{risk_str}"
        )
    return "\n".join(lines)


def get_surgical_frames(n_frames: int = 60, procedure: str = "Laparoscopic Cholecystectomy") -> list[Document]:
    """
    Returns randomised surgical frame detections as Document objects.
    Tag: RANDOMISED — random values prove wiring only, no clinical meaning.

    Args:
        n_frames: Number of frames to generate per procedure.
        procedure: Procedure name for metadata.
    """
    frames = [_rand_frame(i, n_frames) for i in range(n_frames)]
    text = _frames_to_text(frames, procedure)
    return [
        Document(
            id="surgical-frames-randomised",
            text=text,
            metadata={
                "procedure": procedure,
                "n_frames": n_frames,
                "phases_covered": list({f["phase"] for f in frames}),
                "source_type": "randomised_surgical_frames",
            },
            tag=DataTag.RANDOMISED,
        )
    ]
