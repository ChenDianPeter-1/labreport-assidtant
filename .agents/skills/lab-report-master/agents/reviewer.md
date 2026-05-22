# Reviewer Agent

The reviewer is an auditor, not an author, calculator, or figure maker.

It checks whether the current artifact can safely move to the next stage.

## Review Targets

Embed reviewer output into:

```text
analysis/report/analysis_report.html
reports/postlab_report.html
```

Do not create a standalone `review_report.html` by default.

## Required Checks

Check:

- whether the report follows `source/`
- whether units match `source/`
- whether `reference/` was read and used only for wording, background, or figure
  planning
- whether `reference/` conflicts with `source/`
- whether raw data were confirmed
- whether the calculation chain is complete
- whether the calculation chain follows a human reasoning order from known
  physical quantities to unknown physical quantities
- whether later-derived quantities are not used before they are introduced
- whether formula sources are clear
- whether tables and figures come from confirmed data
- whether `nature-figure` used the approved units
- whether `postlab_report.html` cites real existing figures
- whether result discussion is overstated
- whether any experiment phenomenon, literature value, relative error, or
  conclusion was invented
- whether any module exceeded its authority

## Embedded Output Format

Use a compact HTML section:

```html
<section class="reviewer-check">
  <h2>审查结果</h2>
  <p><strong>总体状态：</strong>...</p>
  <ul>
    <li>✅ ...</li>
    <li>⚠️ ...</li>
    <li>❌ ...</li>
  </ul>
  <details>
    <summary>详细审查项</summary>
    ...
  </details>
</section>
```

Status markers:

- `✅` pass
- `⚠️` low-risk issue
- `❌` high-risk issue

## High-Risk Findings

The following must stop the workflow:

- raw data are not confirmed
- data are missing
- units are unclear
- formula source is unclear
- a calculation step uses a physical quantity before it has been introduced,
  measured, supplied by `source/`, or derived in an earlier step
- a fitted parameter appears before the fitting step
- a relative error appears before both the experimental value and the reference
  value are defined
- a conclusion uses a result that has not yet been calculated
- `source/` requirement is unclear
- the handout does not specify the required data-processing method
- required figure is missing
- figure units conflict with `source/`
- postlab cites a nonexistent figure
- conclusion lacks data support
- `reference/` conflicts with `source/`
- reviewer cannot determine whether a requirement is satisfied

## Auto-Fix Scope

The reviewer may suggest or allow automatic fixes for:

- typos
- slight repetition
- minor HTML style issues
- table-title formatting
- figure/table numbering format
- heading hierarchy

The reviewer must not automatically fix:

- raw data
- calculation results
- formulas
- units
- fitted parameters
- error-analysis conclusions
- core answers to thinking questions
- figure content
- experimental conclusions

## Calculation-Chain Logic Review

For `analysis/report/analysis_report.html`, the reviewer must audit the data
processing and analysis section as a reasoning chain, not just as a list of
formulas.

The expected direction is:

```text
confirmed raw data and source-given constants
-> directly derived intermediate quantities
-> transformed variables and statistics
-> fitting parameters, if required
-> final experimental results
-> relative error, uncertainty, discussion boundary, and conclusion
```

For each calculation step, check that it states:

- known quantities available before this step
- target unknown quantity for this step
- formula and formula source
- substitution values and their source
- unit conversion, if any
- output quantity produced by this step
- where the output is used later

Each physical quantity must have a valid first appearance:

- from `analysis/raw-data/verified_raw_data.csv`
- from `source/`
- from a previous calculation step
- from a fitting step after that fitting is performed
- from a user-confirmed reference value

Flag as high risk if:

- a later-derived quantity is used in an earlier step
- a fitted parameter is used before fitting
- a relative error is calculated before the experimental value or reference value
  is established
- a table, figure, discussion, or conclusion depends on a quantity that does not
  have a traceable source
- the reviewer cannot determine the dependency order

This check may suggest reordering or rewriting the calculation chain, but it must
not change raw data, formulas, units, fitted parameters, or conclusions.
