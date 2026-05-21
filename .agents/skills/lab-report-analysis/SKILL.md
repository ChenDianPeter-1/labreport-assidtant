---
name: lab-report-analysis
description: >
  Analyze undergraduate laboratory-report data from experiment handouts, raw-data
  images, experiment notes, and report templates. Use whenever the user asks to
  process lab data, transcribe measurements from images, build calculation tables,
  fit curves, extract parameters, prepare report-ready tables/results, or draft
  error analysis for a laboratory report. This skill must be used before formal
  calculations when raw measurements originate from images, because the workflow
  requires a user verification checkpoint for the transcribed raw data. Use this
  skill when the user wants auditable review HTML pages before calculations,
  fitting, plotting, or report handoff.
---

# Lab Report Analysis

Use this skill to turn experiment materials into a trustworthy analysis chain for
an undergraduate laboratory report.

The skill is responsible for the data-analysis layer only:

```text
raw materials -> verified raw-data table -> calculations -> fitted results
-> report-ready tables / figure inputs / result drafts
```

It is not a pre-lab-report skill and not a generic paper-writing skill.

## Core stance

- Current experiment materials come first.
- Build a traceable calculation chain before writing conclusions.
- When raw measurements come from images, transcription is only provisional until the user confirms it.
- Do not invent observations, raw values, formulas, fitted results, uncertainty, or certainty.
- Separate data analysis from final figure polishing and prose polishing.
- Prefer the current experiment folder over unrelated materials elsewhere.
- Ignore archived materials unless the user explicitly asks to use them.
- Work in reviewable stages rather than rushing from raw data to final conclusions.
- Prefer a clear experiment-folder hierarchy over a flat pile of mixed outputs.
- Treat CSV files as reproducible machine-readable data sources and HTML review
  files as the human-facing audit interface. The user should mainly inspect the
  HTML, while downstream scripts should read the confirmed CSV/Markdown artifacts.

## Scope

This skill handles:

- reading current-experiment handouts, notes, templates, and raw-data images when needed for analysis
- extracting and structuring raw measurements
- creating provisional and verified raw-data CSVs
- creating human-readable review HTML pages for each user-verification gate
- building calculation chains
- performing report-oriented data analysis and fitting
- preparing report-ready tables, result summaries, error-analysis scaffolds, and a `nature-figure` handoff package

This skill does not handle:

- pre-lab report drafting
- final scientific figure design, visual encoding, layout, styling, and export, which belong to `nature-figure`
- full report-section drafting, which belongs to `nature-writing`
- final language refinement, which belongs to `nature-polishing`

## Entry layer

Before analysis:

1. identify the experiment name
2. inspect the current experiment folder and check whether the core materials are present:
   - experiment handout
   - raw-data images or another explicit raw-data source
   - experiment notes, when available
   - report template
3. identify the required analysis outputs:
   - calculations
   - fitted parameters
   - tables
   - figures
   - error analysis
4. list missing inputs that would block reliable analysis
5. ask the user whether there are any additional materials or instructions not yet visible in the folder, such as teacher comments, oral requirements, formula corrections, grading emphasis, or preferred conventions

Do not silently assume the visible folder is complete. If the experiment identity, required outputs, raw-data source, or user-supplied extra instructions are still unclear, expose the gap before proceeding.

## File placement plan

Before creating multiple outputs, propose a folder layout that keeps source materials, analysis artifacts, figures, scripts, and reports separate. Prefer this default structure unless the user already has a better local convention:

```text
experiment/
+-- source/
+-- analysis/
+-- figures/
+-- scripts/
`-- reports/
```

Recommended placement:

- `source/`: experiment handout, original raw-data images or machine exports, experiment records, and report templates
- `analysis/`: `provisional_raw_data.csv`, `verified_raw_data.csv`, `processed_data.csv`, `summary_data.csv`, `figure_input_specification.md`, `plotting_constraints.md`, review HTML pages such as `raw_data_review.html`, `calculation_chain_review.html`, `analysis_results_review.html`, `figure_handoff_review.html`, and optional `analysis_notes.md`
- `figures/`: figure outputs
- `scripts/`: reproducible analysis or plotting scripts
- `reports/`: report drafts and final report files

If the experiment folder is already messy or flat, first propose a reorganization plan and ask for approval before moving existing files. Do not scatter new outputs into the experiment root unless the user explicitly prefers that layout.

When the user approves reorganization, place existing files by function rather than by file type alone:

- keep source materials unchanged and move them into `source/`
- keep derived analysis artifacts in `analysis/`
- keep figure assets in `figures/`
- keep reusable scripts in `scripts/`
- keep final or near-final deliverables in `reports/`

Do not rename source files just to make them prettier unless the user asks. Preserve traceability first; improve naming only when it removes genuine ambiguity.

Before moving files, show a concise before/after map when the reorganization is non-trivial. After moving files, report the final structure so the user can confirm that the folder now matches their working style.

## Raw-data verification gate

When raw measurements originate from images:

1. transcribe the values into a structured raw-data table
2. preserve units, sample labels, repetitions, and remarks
3. mark any uncertain, blurry, or ambiguous entries explicitly
4. export the table as `provisional_raw_data.csv`
5. generate `raw_data_review.html` as the primary user-facing review page
6. present the HTML path to the user and briefly summarize what needs checking

`raw_data_review.html` must make the review easier than reading CSV directly and
must support user edits during review:

- show the transcribed table with clear headers, units, sample/condition labels,
  trial labels, and notes
- highlight uncertain, blurry, suspicious, or inferred entries
- include the source image/file names or record locations for traceability
- include a short "what to check" list and the current review status
- make raw-data value, unit, include/exclude, confidence, and note cells editable
  with `contenteditable`, form inputs, or another direct in-page editing affordance
- include an in-page "export edited CSV" or "copy edited CSV" mechanism so the
  user's edits can become the next `provisional_raw_data.csv`
- visibly explain that editing the HTML alone does not confirm the data until
  the edited CSV/table is exported, copied back, or explicitly confirmed in chat

Do not rely on HTML as the canonical downstream data source. The editable HTML is
the review surface; the confirmed CSV remains the downstream data source.

Do not proceed to derived calculations, curve fitting, plotting, interpretation, or report conclusions until the user explicitly confirms that the transcribed raw data are correct.

After confirmation, preserve the approved table as `verified_raw_data.csv` and use that file as the fixed raw-data source for downstream analysis. If the user corrects any value, update `provisional_raw_data.csv` first, refresh `raw_data_review.html`, then regenerate `verified_raw_data.csv` only after confirmation.

The intended user experience is:

```text
raw image / record -> provisional_raw_data.csv + raw_data_review.html
user reviews the HTML -> verified_raw_data.csv
verified_raw_data.csv -> all calculations, fitting, and plotting inputs
```

Avoid making the user manage both CSVs. In conversation, treat `raw_data_review.html`
as the review surface and mention `verified_raw_data.csv` as the locked downstream
input after confirmation. Keep `provisional_raw_data.csv` as an internal, auditable
draft artifact.

## Stage gates

Pause after every major stage and let the user review before continuing:

1. after raw-data transcription, with `analysis/raw_data_review.html`
2. after the calculation chain is proposed, with `analysis/calculation_chain_review.html`
3. after the main data processing / fitting results are produced, with `analysis/analysis_results_review.html`
4. before packaging report-ready tables, prose scaffolds, or plotting handoff, with `analysis/figure_handoff_review.html` when figures are required

At each pause, state:

- what was completed
- which HTML review file to open
- what should be checked for both correctness and fit with the user's requirement
- what will happen next if the user confirms

Use the checkpoint to ask whether the current result is not only correct, but also matches what the user wanted from this stage.

### Review HTML standard

Every review HTML file should be a compact audit panel, not a polished final
report. Prefer simple local HTML that can be opened directly, with no server.
For Chinese undergraduate lab-report workflows, the review HTML should use
Chinese for user-facing titles, section names, instructions, checklist items,
status labels, and result explanations by default. Stable machine-readable
field names, filenames, code identifiers, and CSV headers may remain in English
when that improves reproducibility, but they should be surrounded by Chinese
explanations so the page is comfortable to review.
Each review page should include:

- the stage name and status, such as "待确认" or "已确认"
- source files and generated files relevant to this stage
- the table, formula chain, results summary, or figure handoff package being reviewed
- highlighted uncertainties, assumptions, missing inputs, or suspicious entries
- reference use, including which reference notes/files informed this stage and
  which reference files were not used
- an explicit checklist of what the user should verify
- a short "next step after confirmation" section

Use `provisional_*` files for draft artifacts and `verified_*` or `confirmed_*`
files only after user confirmation. Do not let a review HTML page become the
only copy of data that downstream analysis depends on.

For `raw_data_review.html`, the page is not acceptable if it is read-only. It
must provide an editable data table and a way to export or copy the edited table
as CSV. Later review pages such as `calculation_chain_review.html` and
`analysis_results_review.html` may be read-only when they are purely explanatory,
but they should still provide clear places for the user to identify corrections
or assumptions to change.

## Experiment reference learning

Experiment folders may contain a `reference/` directory with external teaching
materials, textbook excerpts, standards, papers, or notes. These references can
help the agent understand method background, formula choices, expected data
structure, and error-analysis vocabulary, but they must not override the current
experiment handout or confirmed data.

At Stage 1, inspect experiment references in this order:

1. list every file in `experiment/reference/`
2. read `experiment/reference/reference-notes.md` first, if it exists
3. check whether every non-note reference file is mentioned or clearly covered
   by `reference-notes.md`
4. classify each covered reference as one or more of:
   - method background
   - formula or calculation-chain support
   - standard condition or theoretical expectation
   - possible error-source vocabulary
   - not suitable for current analysis
5. record the classification in the Stage 1 summary or review HTML

Do not blindly read every PDF just because it exists. Use `reference-notes.md`
as the index first, then open only the specific referenced files needed for the
current analysis question.

### When `reference-notes.md` is incomplete

If `reference-notes.md` does not exist, is stale, or does not account for every
file in `reference/`, do not silently continue as if the references were fully
learned. Create or update an audit note, preferably
`analysis/reference_index_audit.md`, with:

- all files found in `reference/`
- files already covered by `reference-notes.md`
- files missing from the notes
- files mentioned in the notes but absent from disk
- a proposed action for each gap

Use this decision path:

1. If the missing files look irrelevant, duplicated, or obviously out of scope,
   list them as "candidate ignore" and ask the user to confirm ignoring them.
2. If the missing files look potentially relevant to formulas, calculations,
   standards, or error discussion, pause and ask whether to inspect and add them
   to `reference-notes.md` before analysis continues.
3. If the user says the reference set is complete despite gaps, continue but
   state the limitation in the Stage 1 review HTML.
4. If a reference conflicts with the current experiment handout, prefer the
   handout, record the conflict, and ask before using the external source in the
   calculation chain.

External literature values, textbook values, or standard-condition values from
`reference/` must not be used directly to calculate relative error, uncertainty,
or final conclusions unless the user explicitly confirms that comparison and the
analysis workflow records how the external value enters the calculation chain.

Each stage review HTML should include a small "Reference use" section when
references affected the stage. It should state which reference notes or files
were used, what they supported, and which reference files were not used.

## Workflow

### Stage 1: Confirm inputs and read the experiment materials

- Check whether the required materials are present.
- Ask whether the user has extra instructions or materials that should shape the analysis.
- Confirm or propose the file-placement plan before creating a growing set of outputs.
- If the existing experiment folder is already flat or mixed, propose a before/after reorganization map and wait for approval before moving old files.
- Inspect `reference/`, read `reference/reference-notes.md` first when present,
  and verify that the notes account for all reference files before relying on
  them.
- If the reference index is incomplete, create `analysis/reference_index_audit.md`
  and pause or limit reference use according to the gap severity.
- Read the handout, notes, template, and raw-data images as needed for data analysis.
- Extract:
  - experiment objective relevant to analysis
  - required calculations
  - required figures
  - formulas provided by the course materials
- Extract from covered references only the method background, formula support,
  standard-condition context, or error-source vocabulary relevant to the current
  analysis.
- Prefer formulas and conventions from the current experiment materials.
- If a required formula is absent, say so and distinguish course-provided rules from external assumptions.

### Stage 2: Transcribe and structure raw data

- Read the raw-data images carefully.
- Convert the measurements into a structured table.
- Preserve the original measurement meaning:
  - condition
  - sample
  - trial
  - observed value
  - unit
  - notes
- Flag illegible or suspicious entries instead of silently guessing.
- Export `provisional_raw_data.csv` before any downstream analysis.
- Generate `raw_data_review.html` for user review; make it the main thing the
  user opens, while keeping the CSV for reproducibility. The HTML must be
  editable and able to export or copy edited CSV content.
- Pause for user verification.

### Stage 3: Build the calculation chain

After the user confirms the raw data:

- list the target quantities that must be obtained
- write the formula chain in the order actually used
- define every symbol and unit
- perform unit conversions explicitly
- keep intermediate quantities visible enough for review
- note where fitted parameters enter later calculations
- generate `calculation_chain_review.html`
- pause for user review before executing the full downstream analysis

The goal is not merely to produce answers, but to make the calculation path auditable.

### Stage 4: Analyze the data

After the user confirms the calculation chain:

- calculate averages, transformed variables, and derived quantities
- identify suspicious deviations or outliers
- choose the fitting form required by the experiment
- report key fitted quantities
- assess whether the results support the intended experimental conclusion
- distinguish:
  - random error
  - systematic error
  - data limitations
  - interpretation limits
- generate `analysis_results_review.html`
- pause for user review before packaging final report-ready components

Do not overstate a conclusion that the data only weakly support.

### Stage 5: Prepare report-ready outputs

After the user confirms the analysis results, produce only the components supported by the confirmed data:

1. analysis-task summary
2. confirmed raw-data summary
3. calculation chain
4. intermediate calculation table
5. report-ready tables
6. figure-input specification
7. fitted-result summary
8. draft result statements
9. error-analysis scaffold
10. conclusion boundary
11. `nature-figure` handoff package, when figures are required
12. `figure_handoff_review.html`, when figures are required

Place each file in the approved folder hierarchy rather than defaulting to the experiment root.

## Output contract

### Before raw-data verification

Return only:

- what needs to be analyzed
- the `raw_data_review.html` path as the primary review surface
- the transcribed raw-data table, briefly summarized in the chat when useful
- any uncertain entries
- the exported `provisional_raw_data.csv`
- the request for user confirmation

Do not include downstream calculations yet.

### After raw-data verification but before calculation-chain approval

Return only:

- the target quantities
- the proposed formula chain
- the unit-conversion logic
- the questions or assumptions that need review
- the `calculation_chain_review.html` path
- the request for user confirmation

### After calculation-chain approval but before final packaging

Return only:

- the processed data summary
- fitted results
- suspicious points or limitations
- the provisional interpretation
- the `analysis_results_review.html` path
- the request for user confirmation

### After analysis approval

Return, in this order when applicable:

1. **Analysis goal**
2. **Confirmed raw data**
3. **Calculation chain**
4. **Intermediate calculations**
5. **Report-ready tables**
6. **Figure-input specification**
7. **Key results**
8. **Error analysis**
9. **Conclusion boundary**
10. **`nature-figure` handoff package**, when figures are required
11. **Review HTML files**
    - `raw_data_review.html`
    - `calculation_chain_review.html`
    - `analysis_results_review.html`
    - `figure_handoff_review.html`, when figures are required
12. **Recommended next handoff**
    - `nature-figure`
    - `nature-writing`
    - `nature-polishing`

## Figure-input specification and `nature-figure` handoff

For each required figure, specify:

- figure purpose
- x-axis variable and unit
- y-axis variable and unit
- data series
- fit type, if any
- parameter to extract
- what conclusion the figure should support

This skill prepares the scientific logic and data package for the figure. Final visual design, layout, styling, and export belong to `nature-figure`.

### `nature-figure` handoff package

After analysis approval, when figures are required, prepare a handoff package containing:

- `verified_raw_data.csv`
- `processed_data.csv` when derived or transformed values are needed for plotting
- `summary_data.csv` when means, SD/SEM, `n`, fitted parameters, or summary statistics are needed
- `figure_input_specification.md`
- `plotting_constraints.md`
- optional `analysis_notes.md` when brief context would prevent misreading the approved analysis
- `figure_handoff_review.html` so the user can inspect exactly what will be sent
  to `nature-figure` before plotting begins

`nature-figure` should receive enough context to draw the figure without having to reinterpret the experiment.

When handing off to `nature-figure`, verified data tables, processed data tables, and approved calculation results should be treated as fixed inputs. `nature-figure` may inspect the package for plotting feasibility, but should not alter raw values, recalculate approved target quantities, remove outliers, or change the approved interpretation unless it first reports a clear inconsistency.

## Handoff boundaries

- `lab-report-analysis` decides what data, derived values, fits, and conclusions are scientifically supported.
- `nature-figure` decides visual encoding, typography, layout, export formats, and publication-style polish.
- `nature-writing` drafts report sections only after the analysis chain is approved.
- `nature-polishing` refines language only after the result logic is sound.

## Report-writing handoff

When the analysis is complete:

- use `nature-writing` if the user wants full report sections drafted from the results
- use `nature-polishing` if the user already has prose and wants it refined
- do not polish wording before the calculation chain and result logic are sound

## Success criteria

This skill succeeds when:

- the starting material set has been checked and any missing or extra user instructions have been surfaced
- raw measurements are traceable to the source materials
- ambiguous values are marked before confirmation
- formulas and unit conversions are auditable
- fitted or calculated results are reproducible
- report-ready tables match confirmed data
- figure inputs are ready for `nature-figure` without requiring it to reinterpret the experiment
- generated files are placed in a clear hierarchy that the user can continue using without cleanup

## Quality checks

### Before raw-data verification

Check that:

- all visible raw values have been transcribed
- units are preserved
- sample labels and trial labels are retained
- ambiguous entries are marked
- `raw_data_review.html` exists and is easier for the user to audit than the CSV alone
- `provisional_raw_data.csv` and `raw_data_review.html` show the same values and units
- raw-data cells in `raw_data_review.html` are editable
- the page provides an export/copy path for edited CSV
- the page explains how user edits flow back into `provisional_raw_data.csv` and
  then into `verified_raw_data.csv` after confirmation
- user-facing review HTML text is in the user's working language, normally
  Chinese for this lab-report workflow; English should be limited to filenames,
  stable CSV fields, code identifiers, and formulas

### After raw-data verification

Check that:

- units are consistent
- formulas match the current experiment materials
- conversions are explicit
- significant figures are consistent
- fitted parameters have physical meaning
- random and systematic errors are not conflated
- tables and figure inputs match the report requirements
- conclusions stay within the support of the data
- each stage that needs user confirmation has a corresponding review HTML file
- downstream calculations read confirmed CSV/Markdown artifacts, not the HTML page

## When to open extra files

| File | Open when |
|---|---|
| `references/report-workflow.md` | You need the stage boundaries for this data-analysis-only workflow |
| `references/raw-data-verification.md` | Raw measurements come from images or manual transcription |
| `references/data-analysis-checklist.md` | You are about to perform calculations, fitting, or error analysis |
| `references/output-templates.md` | You need report-ready table, result, figure-input, or error-analysis formats |

## Default interaction pattern

Use this sequence unless the user clearly asks for a narrower task:

```text
1. inspect materials and ask whether any extra instructions are missing
2. propose or confirm the file-placement plan
3. transcribe raw data
4. create `raw_data_review.html` and ask user to verify both correctness and fit with the requirement
5. propose calculation chain
6. create `calculation_chain_review.html` and ask user to verify both correctness and fit with the requirement
7. analyze confirmed data
8. create `analysis_results_review.html` and ask user to verify both correctness and fit with the requirement
9. prepare report components and, when figures are required, `figure_handoff_review.html` in the approved hierarchy
```

The most important rule is simple:

```text
No confirmed raw data -> no formal downstream analysis
```
