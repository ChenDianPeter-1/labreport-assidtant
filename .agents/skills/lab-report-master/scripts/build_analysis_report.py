#!/usr/bin/env python3
"""Build a simple analysis_report.html from prepared Markdown/CSV artifacts."""

from __future__ import annotations

import argparse
import html
from pathlib import Path


def read_optional(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def esc(text: str) -> str:
    return html.escape(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", required=True, help="Experiment folder")
    parser.add_argument("--out", default=None, help="Output HTML path")
    args = parser.parse_args()

    root = Path(args.experiment)
    out = Path(args.out) if args.out else root / "analysis" / "report" / "analysis_report.html"
    out.parent.mkdir(parents=True, exist_ok=True)

    calculation_chain = read_optional(root / "analysis" / "processed" / "calculation_chain.md")
    figure_spec = read_optional(root / "analysis" / "figure-handoff" / "figure_input_specification.md")
    plotting_constraints = read_optional(root / "analysis" / "figure-handoff" / "plotting_constraints.md")
    figure_prompt = read_optional(root / "analysis" / "figure-handoff" / "nature_figure_prompt.md")

    blockers = []
    for label, rel in [
        ("verified_raw_data.csv", "analysis/raw-data/verified_raw_data.csv"),
        ("processed_data.csv", "analysis/processed/processed_data.csv"),
        ("summary_data.csv", "analysis/processed/summary_data.csv"),
        ("calculation_chain.md", "analysis/processed/calculation_chain.md"),
        ("figure_input_specification.md", "analysis/figure-handoff/figure_input_specification.md"),
        ("plotting_constraints.md", "analysis/figure-handoff/plotting_constraints.md"),
        ("nature_figure_prompt.md", "analysis/figure-handoff/nature_figure_prompt.md"),
    ]:
        if not (root / rel).exists():
            blockers.append(label)

    status = "❌ 存在阻塞项，不能进入作图阶段" if blockers else "✅ 可提交用户审查"
    blocker_html = "".join(f"<li>❌ 缺少 {esc(item)}</li>" for item in blockers) or "<li>✅ 必要文件齐全</li>"

    html_text = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>数据分析与作图计划审核报告</title>
  <style>
    body {{ font-family: "Microsoft YaHei", Arial, sans-serif; margin: 32px; color: #222; }}
    h1 {{ font-size: 24px; }}
    section {{ margin: 20px 0; }}
    pre {{ white-space: pre-wrap; background: #f7f7f7; padding: 12px; border: 1px solid #ddd; }}
    details {{ margin: 10px 0; }}
    .status {{ padding: 10px; background: #f3f3f3; border-left: 4px solid #777; }}
  </style>
</head>
<body>
  <h1>数据分析与作图计划审核报告</h1>
  <p class="status"><strong>总体状态：</strong>{status}</p>
  <section>
    <h2>审查摘要</h2>
    <ul>{blocker_html}</ul>
  </section>
  <section>
    <h2>作图计划摘要</h2>
    <details open><summary>图表输入规格</summary><pre>{esc(figure_spec)}</pre></details>
    <details><summary>作图约束</summary><pre>{esc(plotting_constraints)}</pre></details>
    <details><summary>传给 nature-figure 的提示词</summary><pre>{esc(figure_prompt)}</pre></details>
  </section>
  <section>
    <h2>详细计算过程</h2>
    <details><summary>计算链</summary><pre>{esc(calculation_chain)}</pre></details>
  </section>
  <section class="reviewer-check">
    <h2>reviewer 内嵌审查结果</h2>
    <p><strong>总体状态：</strong>{status}</p>
    <details open><summary>详细审查项</summary><ul>{blocker_html}</ul></details>
  </section>
</body>
</html>
"""
    out.write_text(html_text, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

