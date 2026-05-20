# lab-report-writing Dry-run Test

## Test Scope

This dry-run checks the boundary behavior of `lab-report-writing` after `lab-report` was renamed and restricted to writing responsibilities.

No final report was generated. No data were calculated, fitted, plotted, or interpreted.

## Test Subject

Real experiment folder:

```text
旋光法测定蔗糖转化反应的速率常数/
```

Visible materials:

- `旋光法测定蔗糖转化反应的速率常数讲义.md`
- `材料物化实验报告模板.md`

Missing folders at dry-run time:

- `reference/`
- `analysis/`
- `figures/`
- `reports/`

## Local Skill Availability Check

GitHub-tracked skill path:

```text
skills/lab-report-writing/
```

Local Codex skill path:

```text
.agents/skills/lab-report-writing/
```

Compatibility path:

```text
.agents/skills/lab-report/
```

The local compatibility `lab-report` entry now redirects old `lab-report` requests to `lab-report-writing`, so future local Codex runs should not continue using the old all-in-one behavior.

## Simulated Request 1: Prelab Report

User intent:

```text
为“旋光法测定蔗糖转化反应的速率常数”生成预习报告。
```

Expected `lab-report-writing` behavior:

1. Confirm this is a prelab task.
2. Read the experiment handout and report template from the current experiment folder.
3. Detect that `reference/` does not exist.
4. Offer to search and collect authoritative experiment references, textbook notes, standard methods, or related literature into:

```text
旋光法测定蔗糖转化反应的速率常数/reference/
```

5. Extract only prelab sections from the handout:
   - purpose
   - instruments and reagents
   - principles
   - steps
6. Plan the output as:

```text
旋光法测定蔗糖转化反应的速率常数/reports/prelab.html
```

7. Stop for user confirmation before writing or revising.

Dry-run result:

- Pass. The task can be identified as a prelab-writing task.
- Pass. The module has enough visible materials to prepare a prelab outline.
- Pass. The missing `reference/` folder is not a blocker; it should be suggested only if the user wants external supporting references.
- Pass. The expected output target is `reports/prelab.html`.
- Pass. No formal result, conclusion, error discussion, calculation, fitting, or figure should be generated in the prelab stage.

## Simulated Request 2: Data Processing

User intent:

```text
处理旋光法实验数据，计算速率常数和半衰期。
```

Visible state:

- No `analysis/provisional_raw_data.csv`.
- No `analysis/verified_raw_data.csv`.
- No confirmed raw data source in the experiment folder.

Expected `lab-report-writing` behavior:

1. Refuse to calculate or fit.
2. Route the task to `lab-report-analysis`.
3. Explain that raw data must first be transcribed and confirmed.
4. Require the analysis chain to produce confirmed outputs before writing result discussion.

Dry-run result:

- Pass. This request is outside `lab-report-writing` authority.
- Pass. The task must be delegated to `lab-report-analysis`.
- Pass. No calculation, fitting, error-analysis calculation, or conclusion may be produced before confirmed raw data exists.

## Simulated Request 3: Figure Generation

User intent:

```text
绘制 ln((alpha_t - alpha_inf)/(alpha_0 - alpha_inf)) 与 t 的关系图。
```

Visible state:

- No `analysis/summary_data.csv`.
- No `analysis/figure_input_specification.md`.
- No confirmed fitted parameters.

Expected `lab-report-writing` behavior:

1. Refuse to draw or export the figure.
2. Route data preparation and fitting to `lab-report-analysis`.
3. Route final plotting to `nature-figure` only after confirmed data and figure input specification exist.

Dry-run result:

- Pass. Figure generation is outside `lab-report-writing` authority.
- Pass. Fitting must not be performed by the writing module.
- Pass. The figure module must not receive unconfirmed raw data.

## Simulated Request 4: Result Discussion

User intent:

```text
帮我写实验结果讨论。
```

Visible state:

- No confirmed analysis outputs.
- No approved figures.

Expected `lab-report-writing` behavior:

1. Stop before writing a formal result discussion.
2. Ask for or route to confirmed analysis outputs from `lab-report-analysis`.
3. Avoid inventing rate constants, half-life, literature values, relative errors, uncertainty, or experimental observations.

Dry-run result:

- Pass. The module must not write formal result discussion without confirmed analysis outputs.
- Pass. The module must not invent numerical conclusions.
- Pass. The module may only prepare a placeholder checklist of required confirmed inputs.

## Boundary Verdict

The dry-run passes the first PR boundary goals:

- `lab-report-writing` recognizes prelab writing tasks.
- `lab-report-writing` can use handout and template materials for prelab writing.
- `lab-report-writing` suggests `reference/` inside the current experiment folder for authoritative supporting materials.
- `lab-report-writing` targets `reports/prelab.html` for prelab HTML output.
- Raw-data transcription, confirmation, calculation, fitting, and error-analysis calculation are delegated to `lab-report-analysis`.
- Figure generation and export are delegated to `nature-figure`.
- Writing does not modify confirmed data, refit curves, draw figures, or invent conclusions.

## Remaining Risks

- `lab-report-analysis` has not yet been enhanced with every data-analysis rule extracted from old `lab-report`; that should be a later PR if needed.
- `nature-figure` is still a publication-grade figure skill and may be heavier than undergraduate lab reports need; a future lightweight figure module may still be useful.
- The local `.agents/skills/lab-report` compatibility entry is not tracked by GitHub. It is a local runtime aid only.
