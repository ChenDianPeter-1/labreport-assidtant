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
- terminal step-by-step analysis review is complete and confirmed by the user
- `nature-figure` has completed final figures
- every required figure exists in `figures/`
- `analysis/workflow_state.json` exists and is consistent with these outputs

If any prerequisite is false, stop.

## Required Structure

The postlab report must follow this section order:

1. 实验目的
2. 实验原理
3. 实验装置、设备及试剂
4. 实验步骤（预习准备工作）
5. 实验记录（实验过程中的第一手材料）
6. 数据处理与分析
7. 实验结论
8. 思考题

Follow the report template and teacher requirements from `source/`.

## Rules

- Use verified raw data and approved analysis results only.
- Use final figures from `figures/`.
- Do not create image placeholders for missing figures.
- Do not recalculate values in the writing stage.
- Do not write beyond what the data support.
- Continue postlab writing from prelab structure and language baseline.
- In section 3 (实验装置、设备及试剂), do not use tables.
- Generate section 5 (实验记录) only after raw-data transcription is confirmed.
- Section 5 must reconstruct the real lab process in timeline style. If any
  operation details are unclear, ask the user before writing.
- In section 6 (数据处理与分析), begin with a short organization overview:
  what phases are included, why this order is used, and how phase transitions
  connect.
- In section 6, each phase must state: input, operation, output, and boundary.
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

