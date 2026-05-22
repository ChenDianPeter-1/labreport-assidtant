# Analysis Report Rules

`analysis_report.html` combines:

- confirmed raw-data summary
- data-processing basis
- formula sources
- unit conversions
- calculation chain
- calculation-chain logic review
- physical-quantity dependency order
- known-to-unknown derivation notes
- intermediate tables
- fitting results
- error analysis
- final analysis results
- conclusion boundaries
- figure list and plotting rules
- nature-figure prompt summary
- embedded reviewer results

Show summary first. Put detailed calculations and review details in collapsible
sections.

If the analysis depends on an unknown formula, unit, or fitting rule, stop.

## Calculation-Chain Logic

The analysis report must let the reviewer verify whether the calculation follows
human reasoning order:

```text
known physical quantities -> unknown physical quantities -> final result
```

Include:

- a list of initial known quantities and their sources
- a dependency-ordered calculation chain
- a table showing each physical quantity, first appearance, source, and later use
- a note confirming that later-derived quantities do not appear earlier
- reviewer findings for any "used before derived" problem

If a quantity appears before its source or derivation is established, mark the
analysis as blocked.
