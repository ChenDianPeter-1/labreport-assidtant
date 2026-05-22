# Report Analysis Module

Use this module for the `直接数据分析` entry mode and for continuation after
prelab.

Outputs:

```text
analysis/raw-data/raw_data_review.html
analysis/raw-data/provisional_raw_data.csv
analysis/raw-data/verified_raw_data.csv
analysis/raw-data/review_state.json
analysis/processed/processed_data.csv
analysis/processed/summary_data.csv
analysis/processed/calculation_chain.md
```

## Entry And State Recovery

Before starting data processing, read:

```text
analysis/workflow_state.json
```

If it exists, inherit:

- experiment name
- source/reference file lists
- source requirement summary
- prelab report path
- pending questions

If it does not exist, create it before analysis with:

```json
{
  "current_stage": "initialized",
  "entry_history": ["analysis"],
  "raw_data_confirmed": false,
  "analysis_report_approved": false,
  "figures_completed": false
}
```

Stage behavior:

- `prelab_done`: continue from raw-data review.
- `raw_data_review_ready`: wait for or verify user confirmation.
- `raw_data_confirmed`: begin formal analysis.
- `analysis_step_reviewing`: wait for terminal step confirmation.
- later stages: summarize the current stage and ask before rewinding.

## Raw-Data Review Stage

When the user provides raw-data images, handwritten records, Excel files, CSV
files, or other sources, create a provisional table first. Preserve:

- sample or condition labels
- repeated trials
- measured values
- units
- source file names
- any unclear or suspicious entries

Export:

```text
analysis/raw-data/provisional_raw_data.csv
analysis/raw-data/raw_data_review.html
```

After generating these files, update `analysis/workflow_state.json`:

```json
{
  "current_stage": "raw_data_review_ready",
  "raw_data_review": "analysis/raw-data/raw_data_review.html",
  "last_recommended_next_step": "请在 raw_data_review.html 中核对并确认原始数据，然后告诉 Codex：我审查好了。"
}
```

### raw_data_review.html Requirements

The HTML should be simple and local-file friendly. It must include:

- an editable table
- one confirmation button per row
- an `全部确认` button
- a save/export action for `review_state.json`
- a save/export action for `verified_raw_data.csv`

Do not include:

- OCR confidence
- confidence percentages
- unnecessary remarks columns
- complex dashboard interactions

The browser page is the user review surface. The canonical downstream data file
is `analysis/raw-data/verified_raw_data.csv`.

For transcription:

- Use the user-provided table as the primary skeleton.
- Do not semantically rename physical quantities.
- Keep headers mostly Chinese and close to the raw record.
- Do not add remarks/annotation columns unless strictly necessary for ambiguity.
- Keep the table minimal; avoid bloated metadata.

### Save Mechanism

Use `scripts/build_raw_data_review.py` to generate an HTML page whose buttons can:

1. track row confirmation state in the page,
2. export or save `review_state.json`,
3. export or save edited confirmed rows as `verified_raw_data.csv`.

If the browser supports the File System Access API, the page should let the user
save directly to the expected paths. Otherwise it should download the files and
tell the user to place them under `analysis/raw-data/`.

After the user says `我审查好了`, check that `verified_raw_data.csv` and
`review_state.json` exist. Read only `verified_raw_data.csv`; do not go back to
images and guess values again.

After both files exist, update `analysis/workflow_state.json`:

```json
{
  "current_stage": "raw_data_confirmed",
  "verified_raw_data": "analysis/raw-data/verified_raw_data.csv",
  "raw_data_confirmed": true,
  "last_recommended_next_step": "开始正式数据分析、计算、拟合和误差分析。"
}
```

### Blocking Rule

Before raw data are confirmed, do not:

- calculate
- fit
- plot
- write conclusions
- generate `postlab_report.html`

## Formal Analysis Stage

After raw-data confirmation:

1. Read `analysis/raw-data/verified_raw_data.csv`.
2. Read the data-processing requirements from `source/`.
3. Identify formulas, units, significant-figure rules, fitting requirements,
   reference values, and required output tables.
4. Before each analysis operation, explain in terminal:
   - what will be done
   - why this step is needed
   - input/output files
   - main risk/boundary
5. If any of these are missing or unclear, stop and ask the user.
6. After user confirms the step logic in terminal, execute the step.
7. Calculate averages, standard deviations, relative errors, unit conversions,
   transformed variables, and fitted parameters only when supported by `source/`.
8. Preserve a traceable calculation chain.

Required outputs:

```text
analysis/processed/processed_data.csv
analysis/processed/summary_data.csv
analysis/processed/calculation_chain.md
```

Use `scripts/analyze_data.py` only with an explicit analysis plan derived from
`source/`. The script must not choose formulas by itself.

### calculation_chain.md Reasoning Structure

`calculation_chain.md` must be written as a dependency-ordered reasoning chain.
It is not enough to list formulas. Every step must show how known physical
quantities lead to unknown physical quantities.

Use this structure:

```markdown
## Step 0: 已知量清单
- 来自 verified_raw_data.csv 的量：
- 来自 source/ 的常数、条件或参考值：
- 用户已确认的外部参考值：

## Step 1: [待求物理量名称]
- 本步已知量：
- 本步待求量：
- 公式：
- 公式来源：
- 代入值及来源：
- 单位换算：
- 本步输出：
- 输出供后续哪一步使用：

## Step N: 最终结果与误差
- 本步已知量：
- 本步待求量：
- 公式：
- 公式来源：
- 代入值及来源：
- 单位换算：
- 本步输出：
- 结论边界：
```

Rules:

- Do not use a quantity before it appears in `Step 0` or an earlier step.
- Do not use fitting parameters before the fitting step.
- Do not calculate relative error before both the experimental value and the
  reference value are defined.
- Do not discuss or conclude from a quantity that has not yet been calculated.
- If a quantity cannot be traced, stop and ask the user.

## Review Mode For Formal Analysis

After raw-data confirmation, use terminal step-by-step review only.

- Do not create additional mandatory HTML review gates for:
  - `calculation_chain_review.html`
  - `analysis_results_review.html`
  - `figure_handoff_review.html`
- If a summary page is produced, treat it as optional artifact, not a user
  approval gate.
- The required approval chain is terminal-based step confirmation.

## Required Sections For Terminal Review

Include:

- 已确认原始数据摘要
- 数据处理依据
- 公式来源
- 单位换算逻辑
- 计算链
- 计算链逻辑审查
- 物理量依赖顺序表
- 已知量到未知量推导说明
- 关键中间计算表
- 拟合结果
- 误差分析
- 最终分析结果
- 结论边界
- 需要生成的图表清单
- 每张图的作图规则
- 每张图的横纵坐标和单位
- 每张图的数据来源
- 是否符合 `source/` 要求
- 是否参考 `reference/` 优化作图方案
- 将要传给 `nature-figure` 的指令摘要
- reviewer results when applicable

If any required item is not applicable, state why. If it is unknown, stop rather
than filling a placeholder.
