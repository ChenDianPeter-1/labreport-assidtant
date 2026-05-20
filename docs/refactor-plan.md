# lab-report 职责边界重构方案

## 1. 当前 `lab-report` 的职责为什么过大

当前 `skills/lab-report/SKILL.md` 的定位是“材料物化实验报告写作助手”，但实际职责覆盖了完整报告生产链：

- 预习报告：实验目的、实验原理、仪器试剂、实验步骤；
- 后续报告：实验记录、数据处理、结果讨论、思考题；
- 数据处理：有效数字检查、计算、标准偏差、相对误差；
- 拟合分析：线性回归、回归方程、斜率、截距、标准偏差、`R^2`；
- 图表生成：三线表、调用 `nature-figure` 生成图；
- 最终整合：输出完整 HTML 报告。

这让 `lab-report` 变成了全能型 skill。它既写文字，又处理数据，又决定拟合，又参与图形生产，导致后续 workflow 中很难判断“谁是数据真相的来源”。

## 2. 它和 `lab-report-analysis` 的冲突点

`skills/lab-report-analysis/` 已经明确负责：

- 从讲义、实验记录、原始数据图片中提取和结构化数据；
- 生成 `provisional_raw_data.csv`；
- 等待用户确认后生成 `verified_raw_data.csv`；
- 建立可追溯计算链；
- 执行数据计算、拟合、误差分析；
- 生成报告用表格、结果摘要和 figure handoff package。

而 `lab-report` 当前仍在后续报告阶段直接执行：

- 有效数字检查；
- 公式计算；
- 标准偏差和相对误差；
- 线性回归；
- 定量误差分析；
- 报告图表准备。

这些都是 `lab-report-analysis` 的核心职责。若保留现状，同一组原始数据可能被两个 skill 分别处理，导致计算链、数值结果、拟合参数和误差解释不一致。

## 3. 它和 `nature-figure` 的冲突点

`skills/nature-figure/` 负责高质量科学图的生成、视觉设计、导出和 QA。它强调先定义 figure contract，再选择后端，最后输出 SVG/PDF/TIFF/PNG 等图形结果。

`lab-report` 当前也在后续报告阶段处理“图表”，并写明图形由 `nature-figure` 生成，但约束不够硬：

- 没有明确禁止 `lab-report` 自己绘图；
- 没有明确禁止 `lab-report` 重绘、修图、美化或导出最终图形；
- 没有明确规定 `nature-figure` 只能使用 confirmed data 和 figure input specification；
- 没有明确禁止 figure 侧重新拟合、删除异常点或改变 confirmed interpretation。

因此需要把图形权力彻底移交给 `nature-figure` 或后续专门 figure 模块，`lab-report-writing` 只负责在报告中引用 approved figures，并基于已确认结果写图文说明。

## 4. 为什么 `lab-report` 应该降级为 `lab-report-writing`

`lab-report` 这个名字过大，会让模型自然以为它可以处理整份实验报告的所有任务。实际更稳定的职责定位应是：

> `lab-report-writing` 是报告写作与整合模块，只负责把已经确认的数据、图形和结论写成报告文本。

它应该从“报告全流程执行者”降级为“写作与整合层”。这样可以形成清晰分工：

- 数据真实性由 `lab-report-analysis` 保证；
- 图形质量由 `nature-figure` 保证；
- 文本表达和最终报告结构由 `lab-report-writing` 保证。

## 5. `lab-report-writing` 应保留哪些职责

从旧 `lab-report` 中保留以下有用能力：

- 判断用户要写预习报告还是后续写作内容；
- 根据讲义撰写实验目的；
- 根据讲义整理实验原理和核心公式；
- 整理仪器与试剂；
- 整理实验步骤；
- 根据 confirmed analysis outputs 撰写结果讨论；
- 回答思考题；
- 将预习报告、结果讨论、图表引用和思考题整合为最终 HTML；
- 遵守报告模板、语言简洁、逻辑清楚、格式统一。

保留这些职责时必须增加限制：凡涉及实验结果、数据、误差、拟合参数和图形解释，必须以 `lab-report-analysis` 的 confirmed outputs 或 `nature-figure` 的 approved figures 为依据。

## 6. `lab-report-writing` 必须禁止哪些职责

第一 PR 中必须在 `lab-report-writing` 中新增 `Forbidden Responsibilities`，明确本模块不得：

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

同时必须写入硬规则：

- 没有 confirmed raw data，不得写正式结果、结论或误差讨论；
- 没有 confirmed analysis outputs，不得生成结果讨论；
- 没有 approved figures，不得把图形当作最终图引用。

## 7. 数据处理为什么必须交给 `lab-report-analysis`

实验报告的数据层需要可追溯、可审查、可暂停确认。`lab-report-analysis` 已经具备这些边界：

- 图片来源数据先进入 `provisional_raw_data.csv`；
- 用户确认后才生成 `verified_raw_data.csv`；
- 未确认前禁止计算、拟合、作图、写结论；
- 计算链、拟合结果和误差分析都应由分析模块产出；
- downstream 模块只能引用 confirmed outputs。

因此所有数据转录、确认、计算、拟合、异常点判断、误差分析计算和表格数值生成都必须交给 `lab-report-analysis`。

## 8. 作图为什么必须交给 `nature-figure` 或后续 figure 模块

图形生产涉及坐标轴、图例、回归线、导出格式、分辨率、字体、版式和 QA。`lab-report-writing` 不应承担这些视觉和技术判断。

第一 PR 中应明确：

- `lab-report-writing` 不直接生成图；
- `lab-report-writing` 不改图；
- `lab-report-writing` 不重新拟合图中的曲线；
- `nature-figure` 或后续 figure 模块只能使用 confirmed data、summary data、fitted-result summary 和 figure input specification；
- 图形模块不得改 confirmed data，不得重新解释数据结论。

## 9. 旧 `lab-report` 中可被 `lab-report-analysis` 吸收的内容

旧 `lab-report` 中关于数据分析的内容不是全部丢弃。它包含一些适合迁移到 `lab-report-analysis` 的本科实验报告规则，但这些规则应该从“写作模块执行”改为“分析模块执行或约束”。

可以吸收的内容包括：

- 有效数字检查：迁移为 `lab-report-analysis` 的 calculation QA 规则，由分析模块根据仪器精度和讲义要求决定结果保留位数。
- 逐步计算：迁移为 `calculation_chain.md` 或分析模块 workflow 的要求，强调公式、单位换算、中间量和最终量可追溯。
- 平行实验平均值、标准偏差、相对误差：迁移为 `processed_data.csv`、`summary_data.csv` 和 fitted/result summary 的生成规则。
- 线性回归规则：迁移为拟合阶段规则，由 `lab-report-analysis` 产出回归方程、斜率、截距、不确定度和 `R^2`。
- `R^2 < 0.95` 时提醒用户：迁移为分析阶段的风险提示，而不是 writing 阶段自行判断。
- 系统误差和偶然误差区分：迁移为 `analysis_notes.md` 或 error-analysis scaffold 的科学依据部分。
- 报告用三线表内容：迁移为 `lab-report-analysis` 生成数值和表格内容，`lab-report-writing` 只负责排版整合，不改数值。
- 图形上需要标注的回归方程和 `R^2`：迁移为 `figure_input_specification.md`，由 `nature-figure` 读取后作图。

这些迁移应分两层处理：

1. 第一 PR 只在 `lab-report-writing` 中删除或改写执行权，并在 `docs/migration-report.md` 记录“这些能力转交给 `lab-report-analysis`”。
2. 如果发现 `lab-report-analysis` 当前规则还不够细，再开后续 PR 修改 `skills/lab-report-analysis/`，把上述规则正式补进它的 references 或 workflow。

第一 PR 不直接修改 `skills/lab-report-analysis/`，原因是本 PR 的 review 目标要保持清晰：只审 `lab-report` 是否降权成功。`lab-report-analysis` 的吸收增强应作为第二个独立 PR，更容易比较和回滚。

## 10. 第一 PR 的修改范围

本次第一 PR 采用更明确的做法：

```text
skills/lab-report/ -> skills/lab-report-writing/
```

第一 PR 应包含：

- 将 `skills/lab-report/` 改名为 `skills/lab-report-writing/`；
- 更新 `SKILL.md` 的 frontmatter name 和 description；
- 将职责定位改为“报告写作与整合模块”；
- 删除或改写旧 `lab-report` 中直接执行数据处理、计算、拟合、误差分析计算、作图的内容；
- 新增 `Forbidden Responsibilities`；
- 新增 `docs/authority-matrix.md`；
- 新增 `docs/migration-report.md`；
- 新增 `docs/dry-run-test.md` 作为后续 dry-run 记录。

第一 PR 不应包含：

- 修改 `skills/lab-report-analysis/`；
- 修改 `skills/nature-figure/`；
- 创建大型总控 skill；
- 移动真实实验数据、报告、图片或归档文件；
- 提交 `.agents/`、实验文件夹、`analysis/`、`achive/` 等本地材料。

## 11. 后续是否需要总控 skill

后续可以考虑第二阶段新增总控 skill，例如：

```text
skills/material-physical-chemistry-lab/
```

但它不应该放进第一 PR。第一 PR 的目标只有一个：先把 `lab-report` 的权力砍掉，让它成为 `lab-report-writing`。

第二阶段总控 skill 的可能职责是：

- 判断当前任务阶段；
- 把预习和写作任务交给 `lab-report-writing`；
- 把数据任务交给 `lab-report-analysis`；
- 把图形任务交给 `nature-figure` 或后续 figure 模块；
- 维护 authority matrix；
- 防止任何模块越权。

在 `lab-report-writing` 边界稳定之前，不应急着创建总控 skill。

## 12. 第一 PR 检查清单

- [ ] 只改 `skills/lab-report` 到 `skills/lab-report-writing` 相关内容。
- [ ] `skills/lab-report-analysis/` 没有被修改。
- [ ] `skills/nature-figure/` 没有被修改。
- [ ] `lab-report-writing` 不再声称自己能处理全流程。
- [ ] `Forbidden Responsibilities` 明确完整。
- [ ] 数据转录、确认、计算、拟合、误差分析计算全部转交 `lab-report-analysis`。
- [ ] 作图、美化、导出全部转交 `nature-figure` 或后续 figure 模块。
- [ ] writing 只能引用 confirmed analysis outputs。
- [ ] 未确认 raw data 前不得写正式结果、结论或误差讨论。
- [ ] PR 中没有提交 `.agents/` 和真实实验材料。
- [ ] 后续总控 skill 只作为计划，不在本 PR 创建。
