#!/usr/bin/env python3
"""Build an editable raw-data review HTML page from a provisional CSV.

The generated HTML lets the user edit cells, confirm rows, confirm all rows, and
save/export:

- review_state.json
- verified_raw_data.csv

The page uses the File System Access API when available and falls back to
downloads when direct saving is unavailable.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = list(reader.fieldnames or [])
        rows = [dict(row) for row in reader]
    if not headers:
        raise SystemExit(f"No CSV headers found: {path}")
    return headers, rows


def build_html(headers: list[str], rows: list[dict[str, str]], csv_name: str) -> str:
    header_cells = "\n".join(f"<th>{html.escape(h)}</th>" for h in headers)
    body_rows = []
    for index, row in enumerate(rows):
        cells = "\n".join(
            f'<td contenteditable="true" tabindex="0" data-field="{html.escape(h)}">{html.escape(row.get(h, ""))}</td>'
            for h in headers
        )
        body_rows.append(
            f"""
<tr data-row="{index}" data-confirmed="false">
  <td class="status">待确认</td>
  {cells}
  <td><button type="button" onclick="confirmRow({index})">确认本行</button></td>
</tr>"""
        )

    rows_html = "\n".join(body_rows)
    headers_json = json.dumps(headers, ensure_ascii=False)

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>原始数据审核</title>
  <style>
    body {{ font-family: "Microsoft YaHei", Arial, sans-serif; margin: 32px; color: #222; }}
    h1 {{ font-size: 24px; }}
    .toolbar {{ margin: 16px 0; display: flex; gap: 8px; flex-wrap: wrap; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 14px; }}
    th, td {{ border: 1px solid #bbb; padding: 6px 8px; vertical-align: top; }}
    th {{ background: #f3f3f3; }}
    td[contenteditable="true"] {{ background: #fffdf3; }}
    tr[data-confirmed="true"] {{ background: #f4fff4; }}
    .status {{ white-space: nowrap; font-weight: 600; }}
    button {{ padding: 6px 10px; cursor: pointer; }}
    details {{ margin-top: 18px; }}
    code {{ background: #f3f3f3; padding: 1px 4px; }}
    @media print {{ .toolbar, button, details {{ display: none; }} body {{ margin: 16px; }} }}
  </style>
</head>
<body>
  <h1>原始数据审核</h1>
  <p>来源表：<code>{html.escape(csv_name)}</code></p>
  <p>请直接编辑表格中的错误值，逐行确认，或使用“全部确认”。保存后，后续计算只读取 <code>verified_raw_data.csv</code>。</p>

  <div class="toolbar">
    <button type="button" onclick="confirmAll()">全部确认</button>
    <button type="button" onclick="chooseSaveDirectory()">选择保存目录并开启自动保存</button>
    <button type="button" onclick="saveReviewState()">保存 review_state.json</button>
    <button type="button" onclick="saveVerifiedCsv()">保存 verified_raw_data.csv</button>
  </div>

  <table id="rawTable">
    <thead>
      <tr>
        <th>确认状态</th>
        {header_cells}
        <th>操作</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <details>
    <summary>保存说明</summary>
    <p>推荐先点击“选择保存目录并开启自动保存”，选择本实验的 <code>analysis/raw-data/</code> 文件夹。之后每次确认行或全部确认，页面会尝试自动保存 <code>review_state.json</code>；当所有行确认后，也会自动保存 <code>verified_raw_data.csv</code>。</p>
    <p>如果浏览器不允许直接写入文件夹，请使用手动保存按钮；若浏览器只能下载文件，请把下载得到的两个文件移动到 <code>analysis/raw-data/</code> 后，再告诉 Codex：“我审查好了”。</p>
    <p>表格支持用方向键在可编辑单元格之间移动。编辑内容会临时保存在当前浏览器页面中，但正式后续计算仍以保存出的 <code>verified_raw_data.csv</code> 为准。</p>
  </details>

<script>
const HEADERS = {headers_json};
const STORAGE_KEY = "raw-data-review:" + location.pathname;
let directoryHandle = null;
let autosaveEnabled = false;

function confirmRow(index) {{
  const row = document.querySelector(`tr[data-row="${{index}}"]`);
  row.dataset.confirmed = "true";
  row.querySelector(".status").textContent = "已确认";
  persistDraft();
  autoSaveOutputs();
}}

function confirmAll() {{
  document.querySelectorAll("tbody tr").forEach((row) => confirmRow(row.dataset.row));
}}

function collectRows() {{
  return Array.from(document.querySelectorAll("tbody tr")).map((row, index) => {{
    const values = {{}};
    HEADERS.forEach((h) => {{
      const cell = row.querySelector(`[data-field="${{CSS.escape(h)}}"]`);
      values[h] = cell ? cell.textContent.trim() : "";
    }});
    return {{ index, confirmed: row.dataset.confirmed === "true", values }};
  }});
}}

function csvEscape(value) {{
  const text = String(value ?? "");
  if (/[",\\n\\r]/.test(text)) return '"' + text.replaceAll('"', '""') + '"';
  return text;
}}

function makeCsv(rows) {{
  const lines = [HEADERS.map(csvEscape).join(",")];
  rows.forEach((row) => {{
    lines.push(HEADERS.map((h) => csvEscape(row.values[h])).join(","));
  }});
  return "\\ufeff" + lines.join("\\n");
}}

async function chooseSaveDirectory() {{
  if (!window.showDirectoryPicker) {{
    alert("当前浏览器不支持直接选择保存目录，请继续使用手动保存或下载方式。");
    return;
  }}
  directoryHandle = await window.showDirectoryPicker();
  autosaveEnabled = true;
  alert("已开启自动保存。请确认目录是 analysis/raw-data/。");
  await autoSaveOutputs();
}}

async function saveTextToDirectory(suggestedName, text) {{
  if (!directoryHandle) return false;
  const handle = await directoryHandle.getFileHandle(suggestedName, {{ create: true }});
  const writable = await handle.createWritable();
  await writable.write(text);
  await writable.close();
  return true;
}}

async function saveText(suggestedName, text, mime, quiet = false) {{
  if (directoryHandle) {{
    await saveTextToDirectory(suggestedName, text);
    if (!quiet) alert(`已保存 ${{suggestedName}}`);
    return;
  }}
  if (window.showSaveFilePicker) {{
    const handle = await window.showSaveFilePicker({{
      suggestedName,
      types: [{{ description: "Data file", accept: {{ [mime]: [suggestedName.slice(suggestedName.lastIndexOf("."))] }} }}],
    }});
    const writable = await handle.createWritable();
    await writable.write(text);
    await writable.close();
    if (!quiet) alert(`已保存 ${{suggestedName}}`);
  }} else {{
    const blob = new Blob([text], {{ type: mime }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = suggestedName;
    a.click();
    URL.revokeObjectURL(url);
  }}
}}

async function saveReviewState() {{
  const rows = collectRows();
  const state = {{
    saved_at: new Date().toISOString(),
    total_rows: rows.length,
    confirmed_rows: rows.filter((r) => r.confirmed).length,
    rows: rows.map((r) => ({{ index: r.index, confirmed: r.confirmed }})),
  }};
  await saveText("review_state.json", JSON.stringify(state, null, 2), "application/json");
}}

async function saveVerifiedCsv() {{
  const rows = collectRows();
  const unconfirmed = rows.filter((r) => !r.confirmed);
  if (unconfirmed.length) {{
    alert(`还有 ${{unconfirmed.length}} 行未确认。请确认全部数据后再保存 verified_raw_data.csv。`);
    return;
  }}
  await saveText("verified_raw_data.csv", makeCsv(rows), "text/csv");
}}

async function autoSaveOutputs() {{
  if (!autosaveEnabled || !directoryHandle) return;
  const rows = collectRows();
  const state = {{
    saved_at: new Date().toISOString(),
    total_rows: rows.length,
    confirmed_rows: rows.filter((r) => r.confirmed).length,
    rows: rows.map((r) => ({{ index: r.index, confirmed: r.confirmed }})),
  }};
  await saveText("review_state.json", JSON.stringify(state, null, 2), "application/json", true);
  if (rows.every((r) => r.confirmed)) {{
    await saveText("verified_raw_data.csv", makeCsv(rows), "text/csv", true);
  }}
}}

function persistDraft() {{
  localStorage.setItem(STORAGE_KEY, JSON.stringify(collectRows()));
}}

function restoreDraft() {{
  const saved = localStorage.getItem(STORAGE_KEY);
  if (!saved) return;
  try {{
    const rows = JSON.parse(saved);
    rows.forEach((savedRow) => {{
      const row = document.querySelector(`tr[data-row="${{savedRow.index}}"]`);
      if (!row) return;
      row.dataset.confirmed = savedRow.confirmed ? "true" : "false";
      row.querySelector(".status").textContent = savedRow.confirmed ? "已确认" : "待确认";
      HEADERS.forEach((h) => {{
        const cell = row.querySelector(`[data-field="${{CSS.escape(h)}}"]`);
        if (cell && savedRow.values && savedRow.values[h] !== undefined) cell.textContent = savedRow.values[h];
      }});
    }});
  }} catch (error) {{
    console.warn("无法恢复本地草稿", error);
  }}
}}

function moveCell(cell, dRow, dCol) {{
  const row = cell.closest("tr");
  const rows = Array.from(document.querySelectorAll("tbody tr"));
  const cells = Array.from(row.querySelectorAll('td[contenteditable="true"]'));
  const rowIndex = rows.indexOf(row);
  const colIndex = cells.indexOf(cell);
  const nextRow = rows[Math.max(0, Math.min(rows.length - 1, rowIndex + dRow))];
  if (!nextRow) return;
  const nextCells = Array.from(nextRow.querySelectorAll('td[contenteditable="true"]'));
  const nextCell = nextCells[Math.max(0, Math.min(nextCells.length - 1, colIndex + dCol))];
  if (nextCell) nextCell.focus();
}}

document.addEventListener("keydown", (event) => {{
  const cell = event.target.closest?.('td[contenteditable="true"]');
  if (!cell) return;
  if (event.key === "ArrowUp") {{ event.preventDefault(); moveCell(cell, -1, 0); }}
  if (event.key === "ArrowDown") {{ event.preventDefault(); moveCell(cell, 1, 0); }}
  if (event.key === "ArrowLeft" && window.getSelection().toString() === "") {{ moveCell(cell, 0, -1); }}
  if (event.key === "ArrowRight" && window.getSelection().toString() === "") {{ moveCell(cell, 0, 1); }}
}});

document.addEventListener("input", (event) => {{
  if (event.target.closest?.('td[contenteditable="true"]')) persistDraft();
}});

restoreDraft();
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to provisional_raw_data.csv")
    parser.add_argument("--out", required=True, help="Path to raw_data_review.html")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    out_path = Path(args.out)
    headers, rows = read_csv(csv_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_html(headers, rows, csv_path.name), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()

