# Calculation Chain Logic Rules

Use these rules when building or reviewing the data-processing and analysis part
of a lab report.

## Purpose

The calculation chain must reflect human scientific reasoning:

```text
已知物理量 -> 待求物理量 -> 中间物理量 -> 拟合/统计量 -> 最终结果 -> 误差与结论
```

The report must not present results as if they were already known before the
calculation step that produces them.

## Valid Sources For A Physical Quantity

Every physical quantity must first appear from one of these sources:

- `analysis/raw-data/verified_raw_data.csv`
- `source/` handout, teacher requirement, or template
- a previous calculation step
- a fitting step after fitting has been performed
- a user-confirmed reference value

If none of these applies, stop and ask the user.

## Required Step Format

Each calculation step must state:

- 已知量
- 待求量
- 使用公式
- 公式来源
- 代入数据及来源
- 单位换算
- 本步输出
- 输出供后续哪一步使用

## Forbidden Logic Errors

Treat these as high-risk reviewer findings:

- using a quantity before it is measured, supplied, or derived
- using a fitting parameter before the fitting step
- calculating relative error before both the experimental value and reference
  value are defined
- using a final result to justify an earlier intermediate calculation
- drawing a conclusion from a quantity that has not yet been calculated
- hiding a unit conversion between steps
- mixing source-given constants and calculated quantities without labeling them

## analysis_report.html Requirements

The report should include:

- `已知量清单`
- `物理量依赖顺序表`
- `计算步骤`
- `先用后算检查`
- `reviewer 计算链逻辑审查`

Detailed calculation steps may be placed inside `<details>` blocks, but the
dependency order and high-risk findings must be visible in the reviewer summary.
