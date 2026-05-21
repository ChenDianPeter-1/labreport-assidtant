# Raw Data Review Rules

`raw_data_review.html` is the only user-facing raw-data confirmation page.

It must provide:

- editable table cells
- per-row confirmation
- `全部确认`
- save/export `review_state.json`
- save/export `verified_raw_data.csv`

The downstream analysis reads only:

```text
analysis/raw-data/verified_raw_data.csv
```

Never calculate from raw images after confirmation. Never calculate before
confirmation.

