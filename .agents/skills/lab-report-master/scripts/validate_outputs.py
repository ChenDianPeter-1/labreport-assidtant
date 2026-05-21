#!/usr/bin/env python3
"""Validate stage outputs for lab-report-master."""

from __future__ import annotations

import argparse
from pathlib import Path


STAGES = {
    "state": [
        "analysis/workflow_state.json",
    ],
    "raw": [
        "analysis/workflow_state.json",
        "analysis/raw-data/raw_data_review.html",
        "analysis/raw-data/provisional_raw_data.csv",
        "analysis/raw-data/verified_raw_data.csv",
        "analysis/raw-data/review_state.json",
    ],
    "analysis": [
        "analysis/workflow_state.json",
        "analysis/raw-data/verified_raw_data.csv",
        "analysis/processed/processed_data.csv",
        "analysis/processed/summary_data.csv",
        "analysis/processed/calculation_chain.md",
        "analysis/report/analysis_report.html",
        "analysis/figure-handoff/figure_input_specification.md",
        "analysis/figure-handoff/plotting_constraints.md",
        "analysis/figure-handoff/nature_figure_prompt.md",
    ],
    "postlab": [
        "analysis/workflow_state.json",
        "analysis/report/analysis_report.html",
        "reports/postlab_report.html",
    ],
    "appendix": [
        "analysis/workflow_state.json",
        "reports/postlab_report.html",
        "reports/appendix_figures_tables.docx",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", required=True)
    parser.add_argument("--stage", choices=STAGES.keys(), required=True)
    args = parser.parse_args()

    root = Path(args.experiment)
    missing = [rel for rel in STAGES[args.stage] if not (root / rel).exists()]
    if missing:
        print("BLOCKED: missing required outputs")
        for rel in missing:
            print(f"- {rel}")
        raise SystemExit(1)
    print(f"OK: {args.stage} outputs are present")


if __name__ == "__main__":
    main()
