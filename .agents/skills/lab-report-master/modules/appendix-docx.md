# Appendix DOCX Module

Use this module after `reports/postlab_report.html` exists and passes reviewer
checks.

Output:

```text
reports/appendix_figures_tables.docx
```

## Scope

By default, extract only final tables and figures used in:

```text
reports/postlab_report.html
```

Do not include intermediate calculation tables from `analysis_report.html`
unless the user explicitly asks.

## Format Rules

Follow the user's appendix template PDF when available:

```text
最终版附图附表.pdf
```

Default rules:

- tables use three-line table style
- table titles appear above tables
- figures have figure captions
- tables have table captions
- figures and tables follow their order in `postlab_report.html`
- one page may contain multiple figures when layout remains readable
- do not include discussion prose
- do not modify table or figure content

## Required QA

After generating the DOCX, render-check it before delivery. If rendering shows
broken tables, blurry images, missing captions, or crowded layout, fix and check
again.

Use `scripts/build_appendix_docx.py` as a helper, then follow the document
render-and-verify workflow available in the environment.

## Workflow State Update

After `reports/appendix_figures_tables.docx` is generated and render-checked,
update `analysis/workflow_state.json`:

```json
{
  "current_stage": "appendix_done",
  "appendix_docx": "reports/appendix_figures_tables.docx",
  "appendix_docx_checked": true,
  "last_recommended_next_step": "完整实验报告流程已完成。"
}
```

