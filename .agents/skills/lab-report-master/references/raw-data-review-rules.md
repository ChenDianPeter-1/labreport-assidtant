# Raw Data Review Rules

`raw_data_review.html` is the only user-facing raw-data confirmation page.

It must provide:

- editable table cells
- per-row confirmation
- `全部确认`
- save/export `review_state.json`
- save/export `verified_raw_data.csv`

Transcription constraints:

- Start from the user-provided raw-data table skeleton.
- Do not semantically rename physical quantities.
- Keep physical quantity labels mostly Chinese and close to the raw record.
- Do not add remarks/notes columns unless strictly necessary for ambiguity.
- Keep review table minimal and compact. Do not include confidence scores or
  bulky metadata.

The downstream analysis reads only:

```text
analysis/raw-data/verified_raw_data.csv
```

Never calculate from raw images after confirmation. Never calculate before
confirmation.

