# Workflow Reference

The workflow has two entry modes but one shared final-report path.

## Startup

1. Locate the experiment directory.
2. If no directory is provided, ask the user for it.
3. Check `<experiment>/analysis/workflow_state.json`.
4. If the state file is missing, ask the user to choose:
   - `预习报告`
   - `直接数据分析`
5. If the state file exists, read it, summarize current progress, state the next
   recommended action, and ask the user to confirm continuing from that stage.

## Prelab Entry

Prelab entry loads only:

```text
modules/prelab.md
```

It generates:

```text
reports/prelab_report.html
analysis/workflow_state.json
```

Then it stops with `current_stage: prelab_done`.

## Data-Processing Entry

Data-processing entry loads these modules in order:

1. `modules/report-analysis.md`
2. `modules/figure-handoff.md`
3. `modules/postlab.md`
4. `modules/appendix-docx.md`

If prelab was already completed, inherit its state. If no state file exists,
create one and mark that the workflow started from analysis.

## Continuation Steps

1. Generate `analysis/raw-data/raw_data_review.html` and provisional CSV.
2. Wait for the user to confirm raw data and say `我审查好了`.
3. Read `analysis/raw-data/verified_raw_data.csv`.
4. Run formal analysis in terminal step-by-step mode:
   - explain each step's input/operation/output/risk
   - get user confirmation for key steps
   - then execute the step
5. Generate processed outputs and figure handoff files.
6. Invoke `nature-figure` with Python using the handoff files.
7. Verify required figures exist.
8. Generate and review `reports/postlab_report.html`.
9. Generate and render-check `reports/appendix_figures_tables.docx`.

Major approval gates:

- `raw_data_review.html` (the only HTML review gate)
- terminal step-by-step analysis review confirmations
