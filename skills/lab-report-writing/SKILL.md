---
name: lab-report-writing
description: |
  材料物化实验报告写作与整合模块。用于预习报告、报告正文组织、
  结果讨论文字、思考题回答和最终 HTML 整合。

  本模块不负责原始数据转录、正式数据计算、拟合、误差分析计算、
  异常点判断和图形绘制。凡涉及数据处理，必须使用 lab-report-analysis。
  凡涉及图形绘制、美化和导出，必须使用 nature-figure 或后续 figure 模块。
---

# 材料物化实验报告写作与整合模块

## Core Position

`lab-report-writing` 只负责把已经可靠的材料写成报告文本。它是写作与整合层，不是数据分析层，也不是作图层。

职责分工：

- 数据真实性由 `lab-report-analysis` 负责。
- 图形质量由 `nature-figure` 或后续 figure 模块负责。
- 报告结构、语言表达、思考题和最终整合由 `lab-report-writing` 负责。

## Required First Question

每次开始处理实验报告任务时，先确认用户要做哪一部分：

```text
你要写预习报告，还是基于已确认分析结果整理后续报告？
```

不得跳过此确认。若用户已经明确指定任务阶段，可直接复述确认后进入对应流程。

## Inputs This Module May Use

优先使用当前实验文件夹中的材料：

- 实验讲义、实验记录和报告模板；
- 当前实验文件夹下 `reference/` 中的权威实验资料、教材片段、标准方法或文献笔记；
- 用户明确提供的写作要求、教师要求或格式要求；
- `lab-report-analysis` 产出的 confirmed analysis outputs；
- `nature-figure` 或 figure 模块产出的 approved figures。

`reference/` 的默认位置是当前实验文件夹内：

```text
experiment/
+-- reference/
+-- source/
+-- analysis/
+-- figures/
`-- reports/
```

预习报告阶段可以协助用户检索权威实验资料、教材资料、标准方法或相关文献，并把可用于写作的出处、摘要和引用建议整理到当前实验的 `reference/` 中。若 `reference/` 不存在，先建议创建该文件夹；除非用户确认，不要把检索资料散落到项目根目录或其他实验文件夹。

参考资料只能用于补充背景、原理解释和参考来源，不得覆盖当前实验讲义的要求，不得代替 `lab-report-analysis` 的数据处理结果。

常见 confirmed analysis outputs 包括：

- `analysis/verified_raw_data.csv`
- `analysis/processed_data.csv`
- `analysis/summary_data.csv`
- `analysis/calculation_chain.md`
- `analysis/analysis_notes.md`
- `analysis/figure_input_specification.md`
- fitted-result summary 或 error-analysis scaffold

如果这些输出不存在或未被用户确认，本模块不得把相关数值、拟合结果、误差结论或图形解释写成正式结论。

## Allowed Responsibilities

本模块可以负责：

1. 判断用户当前要写预习报告还是后续写作内容；
2. 根据讲义撰写实验目的；
3. 根据讲义整理实验原理和核心公式；
4. 整理仪器与试剂；
5. 整理实验步骤；
6. 根据 confirmed analysis outputs 撰写实验记录说明、结果讨论和结论；
7. 根据 confirmed analysis outputs 回答涉及数据的思考题；
8. 回答不涉及数据计算的概念性思考题；
9. 引用 approved figures，并撰写图文说明；
10. 将预习报告、结果讨论、图表引用、思考题整合为最终 HTML。

## Forbidden Responsibilities

本模块不得：

1. 从图片或手写记录中转录原始数据；
2. 创建或确认 `verified_raw_data.csv`；
3. 根据原始数据进行正式计算；
4. 进行曲线拟合或线性回归；
5. 自行决定是否剔除异常点；
6. 独立生成最终数据处理表；
7. 绘制、重绘、美化或导出最终图形；
8. 修改 `lab-report-analysis` 产生的已确认数值；
9. 修改已确认分析链中的拟合参数或实验解释；
10. 编造实验现象、文献值、不确定度或相对误差。

硬规则：

- 没有 confirmed raw data，不得写正式结果、结论或误差讨论。
- 没有 confirmed analysis outputs，不得生成结果讨论。
- 没有 approved figures，不得把图形当作最终图引用。
- 遇到数据处理、计算、拟合、误差分析计算或图形输入生成，必须转交 `lab-report-analysis`。
- 遇到图形绘制、美化、导出或图形 QA，必须转交 `nature-figure` 或后续 figure 模块。

## Prelab Workflow

当用户选择“预习报告”时，本模块可以直接执行以下流程：

1. 确认实验名称或实验编号。
2. 阅读当前实验文件夹中的讲义、模板和格式要求。
3. 检查当前实验文件夹是否已有 `reference/`。
4. 如果`/referrence/`里面没有任何参考文件则需要补充参考资料，检索权威实验、教材资料、标准方法或相关文献
5. 告诉用户找到了什么文献，文献的名字、作者、doi号以及对实验有什么帮助，并告诉用户你需要下载并保存到 `reference/`。
6. 提取讲义中的目的要求、仪器与试剂、实验原理、实验步骤。
7. 生成 HTML 预习报告，默认输出到当前实验文件夹的 `reports/prelab.html`。
8. 暂停给用户确认，必要时按模板或教师要求修改。

各章节写作原则：

- **实验目的**：来自讲义，不编造讲义外目的。
- **实验原理**：保留核心公式和关键逻辑链；公式以讲义为准。
- **仪器与试剂**：按讲义或实验材料列出，试剂注明浓度、规格或必要条件。
- **实验步骤**：按讲义整理，不加入讲义没有的操作；可突出关键条件和待观察现象。

预习报告不得提前写实验结果、结果讨论、误差分析或结论。

预习报告输出规则：

- 默认输出文件：`reports/prelab.html`。
- 若用户指定文件名，则仍放在当前实验文件夹的 `reports/` 下。
- HTML 应包含实验目的、实验原理、仪器与试剂、实验步骤四个主体部分。
- 公式用 MathJax 或 KaTeX 兼容的 LaTeX 表达。
- 如使用 `reference/` 中资料，应在 HTML 末尾加入“参考资料”小节。
- 不得把 `reference/` 中的文献值、理论值或外部实验结果写成当前实验的实测结果。

## Postlab Writing Workflow

当用户选择“后续报告”或“最终报告整合”时，按以下流程执行：

1. 确认实验名称、报告模板和用户要写的章节。
2. 检查是否存在 `lab-report-analysis` 的 confirmed outputs。
3. 若 confirmed outputs 不完整，停止并说明应先交给 `lab-report-analysis` 的任务。
4. 若涉及图形，检查是否存在 approved figures 或 figure handoff package。
5. 基于已确认的结果撰写实验记录说明、结果讨论、结论和思考题。
6. 整合为模板要求的 HTML 或 Markdown 片段。
7. 暂停给用户确认。

结果讨论应包含：

- 已确认的核心测量结果；
- 与讲义、实验目的或 confirmed reference value 的关系；
- 由 `lab-report-analysis` 提供依据的误差来源；
- 基于已确认分析结果的改进建议；
- 简短结论。

不得自行补充文献值、相对误差、不确定度、异常原因或实验现象。

## Figure Handling

本模块只负责引用图和写图文说明。

允许：

- 在报告中引用 approved figures；
- 根据 `figure_input_specification.md` 和已批准图件写图题、图注或正文说明；
- 检查图号、图题、正文引用是否一致。

禁止：

- 直接绘图；
- 修改图形视觉样式；
- 导出 SVG/PDF/PNG；
- 重新拟合图中的曲线；
- 改变图形对应的数据解释。

## Final Integration

最终整合时，本模块只整合已确认内容：

- 预习报告章节；
- 用户确认的实验记录文字；
- `lab-report-analysis` 的 confirmed tables 和 result statements；
- approved figures；
- 结果讨论；
- 思考题；
- 模板要求的 HTML 结构、公式渲染和表格排版。

整合过程中不得改动 confirmed data、拟合参数、误差分析依据或 approved figure conclusions。

## Behavior Rules

1. 不确定就问，不猜测、不编造。
2. 优先使用当前实验文件夹内材料，默认忽略 `achive/`。
3. 每个主要阶段结束时暂停，让用户确认后再继续。
4. 语言要求语义无重复、重逻辑、简明清晰。
5. 格式规范优先；若模板或 `rules/` 有要求，严格遵循。
6. 若任务越过本模块权限，明确说明应转交哪个模块，而不是勉强完成。
