# Prelab Module

Use this module only for the `预习报告` entry mode.

Output:

```text
reports/prelab_report.html
```

It must also create or update:

```text
analysis/workflow_state.json
```

## Inputs

Read the current experiment folder:

1. `source/` for the experiment handout, teacher requirements, report template,
   experiment steps, instruments, reagents, and required prelab sections.
2. `reference/` for wording improvement, background support, and expression
   examples only.

Ignore `achive/` unless the user explicitly asks to use it.

## Required Content

The prelab report normally contains:

- 实验目的
- 实验原理
- 仪器与试剂
- 实验步骤

If the template or teacher requirement uses different section names, follow
`source/`.

## Rules

- Use `source/` as the authority for objectives, procedures, instruments,
  reagents, conditions, formulas, and required sections.
- Do not add purposes, steps, instruments, reaction conditions, or preparation
  tasks that are not present in `source/`.
- Use `reference/` only to improve explanation quality and concise wording.
- Do not include results, data processing, error analysis, discussion, or final
  conclusions in the prelab report.
- If a required section cannot be supported by `source/`, stop and ask the user.
- In prelab, the instrument/reagent section must use concise paragraph or list
  form. Do not use tables for this section.

## HTML Requirements

Generate a single local HTML file:

```text
reports/prelab_report.html
```

The page should be Chinese, compact, printable, and easy to copy into a report.
Use simple CSS and readable headings. Do not make a dashboard or require a
server.

## Recommended Process

1. Verify the experiment folder and create missing output directories.
2. List `source/` files and identify the handout/template.
3. List `reference/` files and classify which are relevant for background or
   expression.
4. Extract prelab requirements from the template or teacher instructions.
5. Map every section to `source/` evidence.
6. Ask the user if any essential source material is missing.
7. Generate `reports/prelab_report.html`.
8. Create or update `analysis/workflow_state.json`.
9. Tell the user which file was generated and what to check.

## Workflow State Update

After generating the prelab report, update the state file with at least:

```json
{
  "current_stage": "prelab_done",
  "entry_history": ["prelab"],
  "prelab_report": "reports/prelab_report.html",
  "raw_data_confirmed": false,
  "analysis_report_approved": false,
  "figures_completed": false,
  "postlab_review_passed": false,
  "appendix_docx_checked": false,
  "last_recommended_next_step": "等待用户完成实验并提供原始数据，然后进入原始数据审核。",
  "last_updated": ""
}
```

Also record:

- experiment directory
- experiment name if known
- `source_files_used`
- `reference_files_used`
- concise `source_requirement_summary`
- unresolved `pending_questions`

Stop after this stage. Do not begin raw-data transcription or formal analysis
from prelab mode unless the user explicitly asks to continue and provides raw
data.

