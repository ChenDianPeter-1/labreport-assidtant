# Postlab Module

Use this module only after all prerequisites are complete.

Output:

```text
reports/postlab_report.html
```

## Required Prerequisites

All must be true:

- raw data are confirmed
- `analysis/raw-data/verified_raw_data.csv` exists
- formal analysis is complete
- `analysis/report/analysis_report.html` was reviewed and approved by the user
- `nature-figure` has completed final figures
- every required figure exists in `figures/`
- `analysis/workflow_state.json` exists and is consistent with these outputs

If any prerequisite is false, stop.

## Content

The postlab report may include:

- 实验记录
- 数据处理说明
- 结果讨论
- 误差分析
- 思考题
- 实验结论
- 正式图表引用

Follow the report template and teacher requirements from `source/`.

## Rules

- Use verified raw data and approved analysis results only.
- Use final figures from `figures/`.
- Do not create image placeholders for missing figures.
- Do not recalculate values in the writing stage.
- Do not write beyond what the data support.
- Error analysis must be specific and tied to experiment design, measurement
  limits, data scatter, instrument constraints, or source-supported factors. Do
  not use empty phrases such as only `人为误差`.
- Answer thinking questions one by one according to the handout.
- Use `reference/` for expression or background support, never to override
  `source/`.

## Reviewer

After generating `reports/postlab_report.html`, run the reviewer described in
`agents/reviewer.md` and embed the results in the same HTML.

High-risk reviewer findings stop the workflow and must be shown to the user.

## Workflow State Update

After generating `reports/postlab_report.html` and embedding reviewer results,
update `analysis/workflow_state.json`.

If reviewer has no high-risk issue:

```json
{
  "current_stage": "postlab_review_passed",
  "postlab_report": "reports/postlab_report.html",
  "postlab_review_passed": true,
  "last_recommended_next_step": "从 postlab_report.html 提取最终采用的图表并生成 appendix_figures_tables.docx。"
}
```

If reviewer finds a high-risk issue, keep or set the stage to the blocking stage
and record the issue in `pending_questions`. Do not proceed to DOCX.

