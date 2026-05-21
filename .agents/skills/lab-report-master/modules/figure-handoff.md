# Figure Handoff Module

Use this module after formal analysis is complete and before calling
`nature-figure`.

This module prepares plotting materials only. It must not formally draw final
figures.

Outputs:

```text
analysis/figure-handoff/figure_input_specification.md
analysis/figure-handoff/plotting_constraints.md
analysis/figure-handoff/nature_figure_prompt.md
```

## Authority

Figure requirements come from `source/`. `reference/` may improve visual choices
or figure organization, but must not change data, units, formulas, fitted
parameters, or conclusions.

## figure_input_specification.md

For every planned figure, write:

- figure purpose
- x-axis variable
- x-axis unit
- y-axis variable
- y-axis unit
- data source file
- whether fitting is needed
- fitting method
- parameters to label
- experimental conclusion supported by the figure

## plotting_constraints.md

State:

- units must follow `source/`
- figure numbering and title rules
- axis format
- whether regression equation and `R²` should be shown
- whether error bars are needed
- whether multiple groups are needed
- `nature-figure` must not modify confirmed data
- `nature-figure` must not refit or change conclusions

## nature_figure_prompt.md

Write a direct prompt for `nature-figure`. It must include:

- use Python
- do not ask `Python or R?`
- read the specified data files
- output figures to `figures/`
- save reproducible plotting scripts to `scripts/`
- do not modify confirmed raw data
- do not recalculate
- do not refit
- do not remove outliers
- do not change approved fitted parameters or conclusions

## Handoff Rule

After the user says `审查通过`, pass the contents of these three files to
`nature-figure` automatically. Do not ask the user to copy text manually.

If the handoff files are missing, incomplete, or inconsistent with
`analysis_report.html`, stop and fix the handoff before plotting.

Before invoking `nature-figure`, update `analysis/workflow_state.json`:

```json
{
  "current_stage": "analysis_report_approved",
  "analysis_report_approved": true,
  "last_recommended_next_step": "自动调用 nature-figure，使用 Python 生成正式图形。"
}
```

After `nature-figure` finishes, verify every required figure exists in
`figures/`. Then update:

```json
{
  "current_stage": "figures_completed",
  "figures_dir": "figures",
  "figures_completed": true,
  "last_recommended_next_step": "生成 reports/postlab_report.html。"
}
```

