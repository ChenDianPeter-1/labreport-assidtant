# lab-report 到 lab-report-writing 迁移报告

## Summary

本次迁移将 `skills/lab-report/` 改名为 `skills/lab-report-writing/`，并把它从“全能实验报告助手”降权为“报告写作与整合模块”。

本次未修改：

- `skills/lab-report-analysis/`
- `skills/nature-figure/`

本次未创建总控 skill。总控 skill 只作为后续阶段计划。

## Kept From Old `lab-report`

旧 `lab-report` 中以下能力被保留到 `lab-report-writing`：

- 区分预习报告和后续报告任务；
- 撰写实验目的；
- 整理实验原理和核心公式；
- 整理仪器与试剂；
- 整理实验步骤；
- 协助为预习报告检索和整理权威参考资料；
- 根据已确认结果写结果讨论；
- 回答思考题；
- 输出预习报告 HTML 到当前实验文件夹的 `reports/`；
- 最终整合 HTML 报告片段；
- 保持语言简洁、逻辑清楚、格式统一。

这些能力被保留为写作能力，不再包含数据计算、拟合或图形生产权。

## Removed Or Rewritten From `lab-report`

以下旧职责已从 `lab-report-writing` 的执行范围中删除或改写为转交流程：

- 原始数据转录；
- 创建或确认 `verified_raw_data.csv`；
- 有效数字检查；
- 正式计算；
- 平均值、标准偏差、相对误差计算；
- 线性回归或曲线拟合；
- `R^2` 阈值判断；
- 异常点判断；
- 误差分析计算；
- 独立生成最终数据处理表；
- 绘制、重绘、美化或导出最终图形。

`lab-report-writing` 现在遇到上述任务时必须停止并转交给对应模块。

## Transferred To `lab-report-analysis`

以下能力从旧 `lab-report` 转交给 `lab-report-analysis`：

- 从原始材料、图片或手写记录中转录数据；
- 生成 `provisional_raw_data.csv`；
- 等待用户确认后生成 `verified_raw_data.csv`；
- 基于讲义公式建立 `calculation_chain.md`；
- 执行有效数字检查；
- 计算平均值、标准偏差、相对误差和目标物理量；
- 执行线性回归或曲线拟合；
- 记录拟合参数、不确定度和 `R^2`；
- 判断可疑数据和异常点处理策略；
- 提供误差分析科学依据；
- 生成 `processed_data.csv`、`summary_data.csv`；
- 生成 `figure_input_specification.md`。

如果后续发现 `lab-report-analysis` 现有规则不足以吸收这些职责，应在单独 PR 中增强 `skills/lab-report-analysis/`，不混入本次 `lab-report-writing` 降权 PR。

## Transferred To `nature-figure`

以下能力从旧 `lab-report` 转交给 `nature-figure` 或后续 figure 模块：

- 根据 confirmed data 绘制科学图；
- 设置坐标轴、图例、回归线和标签；
- 执行图形美化；
- 导出 SVG/PDF/PNG/TIFF；
- 对图形进行视觉 QA。

`nature-figure` 必须使用 confirmed data、summary data、fitted-result summary 或 `figure_input_specification.md`，不得自行重算、重新拟合、删除异常点或改变分析结论。

## New Boundary For `lab-report-writing`

`lab-report-writing` 现在只能：

- 写预习报告；
- 为预习报告整理当前实验 `reference/` 中的权威参考资料；
- 组织报告正文；
- 基于 confirmed analysis outputs 写结果讨论；
- 基于 approved figures 写图文说明；
- 回答思考题；
- 整合最终报告。

它不得：

- 处理原始数据；
- 执行正式计算；
- 执行拟合；
- 判断异常点；
- 生成最终图形；
- 修改 confirmed data；
- 编造实验现象、文献值、不确定度、相对误差或结论。

## Workflow Tightening After Real Dry-run

真实触发测试暴露出两个问题：预习报告阶段没有强制先整理 `reference/`，且 HTML 输出容易被描述成“网站”。本次修正把 workflow 改得更硬：

- 开始预习报告或后续写作前，先检查并创建当前实验文件夹下的 `source/`、`reference/`、`analysis/`、`figures/`、`reports/`。
- 预习报告阶段如果 `reference/` 为空或缺少本实验相关资料，必须先检索权威实验资料、教材资料、标准方法或相关文献。
- 候选参考资料必须向用户说明标题、作者或机构、年份、DOI 或 URL、可信度和用途。
- 参考资料至少整理到 `reference/reference-notes.md`。
- 预习报告默认输出为本地文件 `reports/prelab.html`。
- 输出时只报告本地 HTML 文件路径，不把它称为“网站”，也不启动服务器。
- 后续报告可以使用 `reference/` 解释背景、方法原理和外部参考，但不得把文献值伪装成当前实验数据。

## Review Notes

本次迁移的重点不是让三个 skill 同时变复杂，而是先把 `lab-report` 的权力砍掉：

- 数据归 `lab-report-analysis`。
- 图归 `nature-figure`。
- 文字归 `lab-report-writing`。

后续如果需要新增 `material-physical-chemistry-lab` 总控 skill，应在本次边界稳定后另开 PR。
