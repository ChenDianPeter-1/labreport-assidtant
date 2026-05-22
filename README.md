# Lab Report Master Skill

This repository tracks one Codex skill:

```text
.agents/skills/lab-report-master/
```

`lab-report-master` is an integrated workflow skill for material physical
chemistry undergraduate lab reports. It coordinates:

- prelab report generation
- raw-data review and confirmation
- source-backed data analysis
- calculation-chain review
- figure handoff to `nature-figure` with Python
- postlab report generation
- embedded reviewer checks
- appendix figures/tables DOCX generation

## Repository Scope

The repository intentionally ignores everything except:

- `.agents/skills/lab-report-master/**`
- `.gitignore`
- `README.md`
- `CHANGELOG.md`

Local experiment data, generated reports, archived materials, and other skills
are not tracked.

## Skill Entry Flow

On startup, the skill first locates the experiment directory. If the user did
not specify one, it asks for the directory.

Then it checks:

```text
<experiment>/analysis/workflow_state.json
```

If no state file exists, the user chooses:

```text
1. 预习报告
2. 直接数据分析
```

If a state file exists, the skill summarizes the current stage and asks whether
to continue from that point.

## Key Principle

The skill follows:

```text
知之为知之，不知为不知。
```

It must stop and ask when data, formulas, units, source requirements, plotting
rules, or conclusions are unclear.

## Maintained Path

The active skill entry point is:

```text
.agents/skills/lab-report-master/SKILL.md
```

