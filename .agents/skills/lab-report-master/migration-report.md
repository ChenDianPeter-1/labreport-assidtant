# Migration Report

## From old lab-report-writing

Absorbed:

- prelab and postlab as separate writing stages
- current experiment folder first
- `source/`, `reference/`, `analysis/`, `figures/`, and `reports/` layout
- no final discussion without confirmed analysis outputs
- no final figure reference without approved figures

Changed:

- writing is no longer a separate main entry point
- postlab is blocked until `nature-figure` finishes
- output filename is standardized as `reports/prelab_report.html` and
  `reports/postlab_report.html`

## From old lab-report-analysis

Absorbed:

- provisional raw data before confirmed raw data
- user verification gate before calculations
- calculation-chain traceability
- report-ready processed data and figure handoff
- HTML review pages as human-facing checkpoints

Changed:

- review HTML count is reduced
- `analysis_report.html` now combines analysis, figure rules, handoff summary,
  and embedded reviewer results
- raw-data review page must support row confirmation and saving review state

## From nature-figure

Absorbed:

- high-quality scientific plotting responsibility
- Python plotting and export scripts
- visual design is separate from data analysis
- figure QA before report handoff

Changed:

- `lab-report-master` preselects Python in the handoff prompt
- the user is not asked `Python or R?` during the master workflow
- `nature-figure` is constrained not to refit, recalculate, change units, change
  confirmed data, or change approved conclusions

## Weakened Or Removed

- multiple intermediate review HTML pages beyond the required four HTML outputs
- separate writing/analysis entry points as the user's main workflow
- reviewer as an independent report artifact
- placeholders for final figures in postlab

## New Capabilities

- single integrated material physical-chemistry lab-report master workflow
- explicit `source/` vs `reference/` authority rules
- embedded reviewer for analysis and final reports
- formal two-gate workflow
- automatic Python handoff to `nature-figure`
- appendix figures/tables DOCX generation from final postlab content
- validation script for stage outputs and blockers

## Resolved Responsibility Conflicts

- writing and analysis are coordinated by one master skill, but their stage
  boundaries remain explicit
- `figure-handoff` prepares instructions; `nature-figure` draws
- reviewer checks and blocks but does not rewrite scientific content
- appendix DOCX packages final adopted material but does not edit content

## Remaining Risks

- local browser security may require the user to choose save locations when
  `raw_data_review.html` exports `verified_raw_data.csv` and `review_state.json`
- experiment-specific formulas still need `source/` support or user confirmation
- DOCX render checking depends on available document-render tooling in the
  current environment
- `nature-figure` must be invoked with the generated handoff prompt so it does
  not fall back to its normal backend-selection question

