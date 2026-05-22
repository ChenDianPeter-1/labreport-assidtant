# Changelog

## Unreleased

- Repository scope is limited to `lab-report-master` and minimal repository
  metadata.
- Added `README.md` and `CHANGELOG.md`.

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

