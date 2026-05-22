# Changelog

## Unreleased

- Repository scope is limited to `lab-report-master` and minimal repository
  metadata.
- Added `README.md` and `CHANGELOG.md`.
- Refactored `lab-report-master` workflow to V2:
  - kept only one mandatory HTML review gate:
    `analysis/raw-data/raw_data_review.html`
  - removed mandatory downstream HTML gates and replaced them with
    terminal step-by-step confirmation checkpoints
  - enforced postlab section order and prelab-to-postlab continuity rules
  - enforced no-table rule in `实验装置、设备及试剂`
  - updated figure handoff constraints:
    - no figure title rendered inside figure canvas
    - scientific notation must follow human-readable report style
    - group encoding must use shape + color dual channel
  - aligned output/rules references with the V2 gate model across modules and
    references

## 2026-05-22

- Added the integrated `lab-report-master` skill under
  `.agents/skills/lab-report-master/`.
- Added startup routing by experiment directory and
  `analysis/workflow_state.json`.
- Added two entry modes:
  - `预习报告`
  - `直接数据分析`
- Added workflow-state rules for resumable report generation.
- Added embedded reviewer rules for `analysis_report.html` and
  `postlab_report.html`.
- Added calculation-chain logic review:
  - known physical quantities must precede unknown quantities
  - later-derived quantities must not appear earlier
  - fitted parameters may only appear after fitting
  - relative error may only appear after both experimental and reference values
    are defined
- Added helper scripts for raw-data review HTML, analysis report generation,
  appendix DOCX extraction, and output validation.

