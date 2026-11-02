# Judge benchmark results (to cite in M11, no re-run needed)

Source: `building-llm-applications/ch14/bench/` (commit a7059b9; raw per-ticket data in `bench/results/*.json`, table in `bench/RESULTS.md`).
Date: 2026-11-02. Dataset: 120 synthetic support tickets (100 template-built + 20 hand-written tricky), no personal data.
Three questions per ticket in one call: team (choice of 3), urgent (noul), refund (noul).
Metrics from the probability of the predicted class: ECE = expected calibration error (10 bins), acc@c = accuracy when p >= 0.7.

| Task | Backend | acc | ECE | Brier | conf | acc@c | cov@c |
|---|---|---|---|---|---|---|---|
| team | deepseek-v4-flash | 0.87 | 0.063 | 0.153 | 0.87 | 0.93 | 0.88 |
| team | jev-1.14.0 | 0.91 | 0.032 | 0.114 | 0.93 | 0.97 | 0.88 |
| team | xgboost-tfidf | 0.86 | 0.076 | 0.196 | 0.89 | 0.91 | 0.90 |
| urgent | deepseek-v4-flash | 0.98 | 0.063 | 0.023 | 0.94 | 1.00 | 0.98 |
| urgent | jev-1.14.0 | 0.99 | 0.128 | 0.055 | 0.86 | 1.00 | 0.93 |
| urgent | xgboost-tfidf | 0.87 | 0.055 | 0.196 | 0.89 | 0.92 | 0.88 |
| refund | deepseek-v4-flash | 1.00 | 0.033 | 0.007 | 0.97 | 1.00 | 1.00 |
| refund | jev-1.14.0 | 0.99 | 0.047 | 0.012 | 0.96 | 1.00 | 0.99 |
| refund | xgboost-tfidf | 0.97 | 0.033 | 0.063 | 0.95 | 0.97 | 0.99 |

| Backend | mean latency / ticket | total cost (120 tickets) |
|---|---|---|
| deepseek-v4-flash | 2057 ms | $0.0202 |
| jev-1.14.0 (API reports 1.14.0; alias jev-latest) | 187 ms | $0.0020 |
| xgboost-tfidf (5-fold CV, needs labels per task) | ~0 ms | $0 |

## Caveats to state in the course
- Synthetic, template-heavy dataset favours XGBoost; 120 tickets: differences of a few points are not significant.
- Some `team` errors may come from ambiguous labels (not audited).
- Jev is under-confident on `urgent` (conf 0.86 vs acc 0.99): calibrate thresholds per task.
- XGBoost fails on negations ("no rush"): urgent acc 0.87.

## Pending (other machine, GPU)
gemma 12b and OpenDecider-small: run `bench/run_bench.py` with `--label gemma-12b` / `opendecider-small`, then `bench/report.py --md bench/RESULTS.md`, and append rows here.
