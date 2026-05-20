# 实验报告 Skill Authority Matrix

本矩阵用于约束 `lab-report-writing`、`lab-report-analysis` 和 `nature-figure` 的职责边界。第一 PR 的目标是先让 `lab-report-writing` 不再越权处理数据和图形。

| 任务 | 负责模块 | 其他模块限制 |
|---|---|---|
| 判断当前任务阶段 | 后续总控 skill；第一 PR 暂由用户或当前对话明确 | 单个模块不得自行跳过用户意图确认 |
| 预习报告 | `lab-report-writing` | 不得写实验结果、数据处理、误差分析或结论 |
| 实验目的 | `lab-report-writing` | 不得编造讲义外目的 |
| 实验原理 | `lab-report-writing` | 公式以讲义和当前实验材料为准 |
| 仪器与试剂 | `lab-report-writing` | 不得加入讲义或用户材料外的试剂规格 |
| 实验步骤 | `lab-report-writing` | 不得加入讲义没有的操作 |
| 原始数据转录 | `lab-report-analysis` | `lab-report-writing` 不得代替转录 |
| 原始数据确认 | `lab-report-analysis` | 未确认前不得计算、拟合、作图、写正式结论 |
| 创建 `verified_raw_data.csv` | `lab-report-analysis` | 其他模块不得创建或确认 |
| 有效数字检查 | `lab-report-analysis` | `lab-report-writing` 只能引用结论 |
| 数据计算 | `lab-report-analysis` | `lab-report-writing` 不得重新计算 |
| 平均值、标准偏差、相对误差 | `lab-report-analysis` | `lab-report-writing` 不得独立生成或改数值 |
| 线性回归/曲线拟合 | `lab-report-analysis` | `nature-figure` 不得重新拟合，除非分析模块明确要求 |
| 异常点判断 | `lab-report-analysis` | `lab-report-writing` 和 `nature-figure` 不得自行决定剔除 |
| 误差分析计算 | `lab-report-analysis` | `lab-report-writing` 只负责把已确认依据写成文字 |
| 报告用表格数据 | `lab-report-analysis` | `lab-report-writing` 可排版整合，不得改数值 |
| 图形输入规范 | `lab-report-analysis` | `nature-figure` 按规范作图，不得改 confirmed data |
| 科学图绘制 | `nature-figure` 或后续 figure 模块 | `lab-report-writing` 不得绘图 |
| 图形美化与导出 | `nature-figure` 或后续 figure 模块 | `lab-report-writing` 不得修图或导出 |
| 图题、图注、正文引用 | `lab-report-writing` | 必须基于 approved figures 和 confirmed interpretation |
| 结果讨论 | `lab-report-writing` | 必须基于 `lab-report-analysis` 的 confirmed outputs |
| 思考题 | `lab-report-writing` | 涉及数据时必须引用 confirmed analysis outputs |
| 最终报告整合 | `lab-report-writing` | 不得改动 confirmed data、fitted parameters 或 approved figures |

## Hard Gates

- No confirmed raw data -> no calculation, fitting, plotting, or formal conclusion.
- No confirmed analysis outputs -> no formal result discussion.
- No approved figures -> no final figure citation.
- Writing modules must not invent data, observations, literature values, uncertainty, relative errors, or conclusions.
- Figure modules must not recalculate, refit, remove outliers, or change confirmed interpretation.
