# Workflow State Rules

Use this reference whenever starting, resuming, or updating an experiment.

## State File Location

Each experiment stores workflow continuity in:

```text
analysis/workflow_state.json
```

Create `analysis/` if needed.

## Startup Rules

1. Do not choose an experiment folder silently.
2. If the user did not specify an experiment directory, ask for it.
3. After the directory is known, check for `analysis/workflow_state.json`.
4. If the file exists, read it and summarize:
   - experiment name
   - current stage
   - completed outputs
   - pending questions
   - next recommended step
5. Ask the user to confirm continuing from that stage.
6. If the file does not exist, ask whether to start from `预习报告` or
   `直接数据分析`.

## Recommended Schema

```json
{
  "experiment_dir": "",
  "experiment_name": "",
  "current_stage": "initialized",
  "entry_history": [],
  "source_files_used": [],
  "reference_files_used": [],
  "prelab_report": null,
  "raw_data_review": null,
  "verified_raw_data": null,
  "analysis_report": null,
  "figure_handoff_dir": null,
  "figures_dir": null,
  "postlab_report": null,
  "appendix_docx": null,
  "raw_data_confirmed": false,
  "analysis_report_approved": false,
  "figures_completed": false,
  "postlab_review_passed": false,
  "appendix_docx_checked": false,
  "source_requirement_summary": [],
  "pending_questions": [],
  "last_recommended_next_step": "",
  "last_updated": ""
}
```

## Stages And Next Steps

| current_stage | Meaning | Next recommended step |
| --- | --- | --- |
| `initialized` | Experiment state exists, but no major output is complete | Read `source/` and `reference/`, then run chosen entry |
| `prelab_done` | Prelab HTML exists | Wait for raw data, then generate `raw_data_review.html` |
| `raw_data_review_ready` | Review HTML and provisional CSV exist | Wait for user to say `我审查好了` |
| `raw_data_confirmed` | `verified_raw_data.csv` exists and review state is saved | Run formal analysis |
| `analysis_report_ready` | Analysis report and figure plan exist | Wait for user to say `审查通过` |
| `analysis_report_approved` | User approved analysis and figure plan | Invoke `nature-figure` with Python |
| `figures_completed` | Required final figures exist | Generate postlab report |
| `postlab_review_passed` | Postlab exists and reviewer has no high-risk issue | Generate appendix DOCX |
| `appendix_done` | DOCX exists and has been render-checked | Workflow complete |

## Update Rules

Update the state after every completed stage:

- after prelab generation: set `current_stage: "prelab_done"`
- after raw-data review page generation: set `current_stage: "raw_data_review_ready"`
- after confirmed raw data exists: set `current_stage: "raw_data_confirmed"` and `raw_data_confirmed: true`
- after analysis report generation: set `current_stage: "analysis_report_ready"`
- after the user says `审查通过`: set `current_stage: "analysis_report_approved"` and `analysis_report_approved: true`
- after required figures are verified: set `current_stage: "figures_completed"` and `figures_completed: true`
- after postlab passes reviewer: set `current_stage: "postlab_review_passed"` and `postlab_review_passed: true`
- after appendix DOCX render check: set `current_stage: "appendix_done"` and `appendix_docx_checked: true`

Always update `last_updated` and `last_recommended_next_step`.

## Staleness Check

When resuming from an existing state, compare the current `source/` and
`reference/` file list with `source_files_used` and `reference_files_used`.

If files were added, removed, or changed in a way that could affect formulas,
units, report structure, or teacher requirements, tell the user that the previous
state may be stale and ask whether to re-read the changed materials.

Do not silently reuse stale requirements.
