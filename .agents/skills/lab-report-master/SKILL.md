---
name: lab-report-master
description: >
  Integrated master workflow for material physical-chemistry undergraduate lab
  reports. Use this as the primary entry point whenever the user asks for a
  prelab report, raw-data review, data analysis, calculation/fitting, figure
  handoff to nature-figure, postlab report writing, embedded review, or appendix
  figures/tables DOCX for a physical-chemistry experiment. On startup, locate
  the experiment directory, inspect analysis/workflow_state.json if present, and
  route the user into either prelab-only mode or the data-analysis-to-final-report
  continuation workflow.
---

# Lab Report Master

`lab-report-master` is the single main entry point for material physical-chemistry
experiment reports.

Its core design is:

```text
separate entry modes, shared experiment state, one final report workflow
```

The user may generate the prelab report long before doing the experiment. To keep
the later data-processing workflow continuous, every experiment stores progress
in:

```text
analysis/workflow_state.json
```

## Highest Principle

Follow this rule above every workflow convenience:

> 知之为知之，不知为不知。

If an experiment requirement, raw value, unit, formula source, fitting method,
figure rule, template rule, instrument condition, literature value, or conclusion
boundary is unclear, stop and ask the user. Do not guess.

Never invent raw data, experiment observations, literature values, relative
errors, formulas, units, fitted parameters, or experimental conclusions.

Do not generate `reports/postlab_report.html` before the required final figures
exist in `figures/`.

## Startup Router

Always start by locating the experiment directory.

1. If the user specified an experiment directory, use it.
2. If the user did not specify a directory, ask:

   ```text
   请告诉我这次要处理的实验目录在哪里？
   ```

3. After the directory is known, check:

   ```text
   <experiment>/analysis/workflow_state.json
   ```

4. If the state file does not exist, explain that this experiment has no saved
   workflow state yet, then ask:

   ```text
   这个实验还没有 workflow_state.json。你要从哪一步开始？
   1. 预习报告
   2. 直接数据分析
   ```

5. If the user chooses `预习报告`, load only `modules/prelab.md`.
6. If the user chooses `直接数据分析`, create an initial workflow state with
   `entry_history: ["analysis"]`, then load the continuation modules in order:
   `modules/report-analysis.md`, `modules/figure-handoff.md`,
   `modules/postlab.md`, and `modules/appendix-docx.md`.
7. If the state file exists, read it, summarize the current stage and next
   recommended action, then ask the user to confirm continuing from that stage.
   Do not restart the workflow silently.

If the user already says a stage command such as `我审查好了` or `审查通过`, still
locate the experiment directory and read `workflow_state.json` before acting.

Read `references/workflow-state-rules.md` whenever creating, reading, or updating
the state file.

## Authority Order

For each experiment, use:

1. `source/` as the authority for facts, formulas, units, steps, data-processing
   requirements, figure requirements, report structure, and teacher instructions.
2. `reference/` only for better wording, background support, and improved figure
   planning. It must not override `source/`.
3. `achive/` is ignored unless the user explicitly asks to use it.

Read `references/source-reference-priority.md` and
`references/authority-matrix.md` before doing work where source and reference
materials both exist.

## Fixed Output Contract

Keep generated files inside the current experiment folder. Do not scatter outputs
in the experiment root.

Primary outputs:

```text
analysis/workflow_state.json
reports/prelab_report.html
analysis/raw-data/raw_data_review.html
analysis/raw-data/provisional_raw_data.csv
analysis/raw-data/verified_raw_data.csv
analysis/raw-data/review_state.json
analysis/processed/processed_data.csv
analysis/processed/summary_data.csv
analysis/processed/calculation_chain.md
analysis/report/analysis_report.html
analysis/figure-handoff/figure_input_specification.md
analysis/figure-handoff/plotting_constraints.md
analysis/figure-handoff/nature_figure_prompt.md
figures/
scripts/
reports/postlab_report.html
reports/appendix_figures_tables.docx
```

Allowed HTML outputs are limited to:

```text
reports/prelab_report.html
analysis/raw-data/raw_data_review.html
analysis/report/analysis_report.html
reports/postlab_report.html
```

## Required Experiment Layout

Prefer this structure for each experiment:

```text
experiment/
+-- source/
+-- reference/
+-- analysis/
|   +-- raw-data/
|   +-- processed/
|   +-- report/
|   +-- figure-handoff/
|   `-- workflow_state.json
+-- figures/
+-- scripts/
`-- reports/
```

If the folder is flat or mixed, propose a concise reorganization map and ask
before moving existing files. Creating missing output directories is allowed.

## Entry Modes

### Mode A: Prelab Report

Use this mode when the user chooses `预习报告`.

Load only:

```text
modules/prelab.md
```

This mode generates:

```text
reports/prelab_report.html
analysis/workflow_state.json
```

After the prelab report is complete, set:

```json
{
  "current_stage": "prelab_done",
  "prelab_report": "reports/prelab_report.html"
}
```

Then stop. Do not begin raw-data transcription or data analysis in the same mode
unless the user explicitly provides raw data and asks to continue.

### Mode B: Data Processing And Continuation

Use this mode when the user chooses `直接数据分析`, provides raw data, says
`我审查好了`, says `审查通过`, or asks to continue after prelab.

Load continuation modules in this order:

1. `modules/report-analysis.md`
2. `modules/figure-handoff.md`
3. `modules/postlab.md`
4. `modules/appendix-docx.md`

If `workflow_state.json` exists, inherit its source/reference summaries,
prelab path, pending questions, and completed-stage flags.

If it does not exist, create it before analysis and mark:

```json
{
  "current_stage": "initialized",
  "entry_history": ["analysis"]
}
```

## Full Continuation Workflow

After data processing starts, preserve this order:

1. Generate `analysis/raw-data/raw_data_review.html` and
   `analysis/raw-data/provisional_raw_data.csv`.
2. User reviews and confirms raw data in the HTML.
3. User tells Codex: `我审查好了`.
4. Read only `analysis/raw-data/verified_raw_data.csv` for formal analysis.
5. Execute calculations, fitting, unit conversion, significant figures, and error
   analysis.
6. Prepare `nature-figure` input rules and the plotting plan.
7. Generate `analysis/report/analysis_report.html`.
8. User reviews `analysis_report.html`.
9. User tells Codex: `审查通过`.
10. Automatically invoke `nature-figure` with the generated handoff package.
11. `nature-figure` uses Python to produce figures in `figures/` and scripts in
    `scripts/`.
12. Check that required figure files exist.
13. Generate `reports/postlab_report.html`.
14. Run reviewer checks and embed results in `postlab_report.html`.
15. Extract final adopted tables and figures from `postlab_report.html`.
16. Generate `reports/appendix_figures_tables.docx`.
17. Render-check the DOCX and fix obvious layout issues before delivery.

Only two major user approval gates are allowed:

- raw-data confirmation via `raw_data_review.html`
- analysis and figure-plan approval via `analysis_report.html`

Do not ask the user to manually copy the figure handoff into `nature-figure`.

## Module Map

Open only the module needed for the current stage:

| Stage | Module |
| --- | --- |
| Startup and state recovery | `references/workflow-state-rules.md` |
| Prelab report | `modules/prelab.md` |
| Raw-data review and data analysis | `modules/report-analysis.md` |
| Figure handoff | `modules/figure-handoff.md` |
| Postlab report | `modules/postlab.md` |
| Appendix DOCX | `modules/appendix-docx.md` |

Use `agents/reviewer.md` whenever generating or updating
`analysis_report.html` or `postlab_report.html`.

## Script Map

Use bundled scripts when they fit the task:

| Script | Purpose |
| --- | --- |
| `scripts/build_raw_data_review.py` | Build editable raw-data review HTML from provisional CSV |
| `scripts/analyze_data.py` | Scaffold validated analysis execution from verified data and an explicit analysis plan |
| `scripts/build_analysis_report.py` | Build reviewable analysis + figure-plan HTML |
| `scripts/build_appendix_docx.py` | Extract postlab figures/tables into DOCX |
| `scripts/validate_outputs.py` | Check required stage outputs and blockers |

Scripts are helpers, not permission to invent missing scientific decisions. If a
script needs a formula, unit convention, fitting method, or template rule that is
not present in `source/`, stop and ask the user.

## Automatic Nature-Figure Handoff

After the user says `审查通过`, read:

```text
analysis/figure-handoff/figure_input_specification.md
analysis/figure-handoff/plotting_constraints.md
analysis/figure-handoff/nature_figure_prompt.md
```

Then invoke `nature-figure` with the prompt content. The handoff must explicitly
state:

- Python is selected.
- Do not ask `Python or R?`.
- Read only the specified analysis data files.
- Output figures to `figures/`.
- Save reproducible plotting scripts to `scripts/`.
- Do not modify confirmed raw data.
- Do not recalculate, refit, remove outliers, or change approved conclusions.

## Reviewer Embedding

The reviewer does not create standalone review HTML by default. It embeds:

- analysis review into `analysis/report/analysis_report.html`
- final report review into `reports/postlab_report.html`

Reviewer sections must show a short summary first and place detailed checks in
collapsible `<details>` blocks. Use these status markers:

- `✅` pass
- `⚠️` low-risk issue
- `❌` high-risk issue that stops the workflow

If any high-risk issue exists, stop and ask the user before continuing.

## HTML Style

All HTML should be Chinese, simple, printable, and local-file friendly. Avoid
dashboard-style interfaces. Use clean tables and collapsible details for long
calculation chains and reviewer details.

## When To Stop

Stop immediately if:

- the experiment directory is unknown
- `source/` does not specify the required formula, unit, or fitting method
- raw data are not confirmed when analysis starts
- `verified_raw_data.csv` is missing when formal analysis starts
- a needed figure is missing before postlab generation
- `reference/` conflicts with `source/`
- reviewer cannot determine whether a requirement is satisfied
- DOCX render check shows broken tables, missing captions, blurry figures, or
  crowded layout
