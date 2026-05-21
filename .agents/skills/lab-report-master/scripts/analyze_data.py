#!/usr/bin/env python3
"""Run experiment analysis from verified raw data and an explicit plan.

This is a guarded scaffold. It intentionally refuses to choose formulas,
fitting methods, units, or outlier rules by itself. Create an analysis plan from
the experiment `source/` material first, then extend the marked section for the
specific experiment.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_PLAN_KEYS = [
    "formula_sources",
    "unit_rules",
    "processing_steps",
    "outputs",
]


def load_plan(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_PLAN_KEYS if not data.get(key)]
    if missing:
        raise SystemExit(
            "Analysis plan is incomplete. Missing source-backed keys: "
            + ", ".join(missing)
        )
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verified", required=True, help="analysis/raw-data/verified_raw_data.csv")
    parser.add_argument("--plan", required=True, help="JSON analysis plan derived from source/")
    parser.add_argument("--outdir", required=True, help="analysis/processed")
    args = parser.parse_args()

    verified = Path(args.verified)
    plan_path = Path(args.plan)
    outdir = Path(args.outdir)

    if not verified.exists():
        raise SystemExit(f"Missing verified raw data: {verified}")
    plan = load_plan(plan_path)
    outdir.mkdir(parents=True, exist_ok=True)

    # Experiment-specific calculation code belongs here. Do not add generic
    # formulas unless they are explicitly supported by the current source files.
    raise SystemExit(
        "Analysis scaffold is ready, but experiment-specific calculations must "
        "be implemented from source-backed formulas before running. Plan keys: "
        + ", ".join(plan.keys())
    )


if __name__ == "__main__":
    main()

