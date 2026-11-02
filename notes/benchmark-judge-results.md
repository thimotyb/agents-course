# Judge benchmark results (to cite in M11, no re-run needed)

Source: `building-llm-applications/ch14/bench/` (commit a7059b9; raw per-ticket data in `bench/results/*.json`, table in `bench/RESULTS.md`).
Date: 2026-11-02. Dataset: 120 synthetic support tickets (100 template-built + 20 hand-written tricky), no personal data.
Three questions per ticket in one call: team (choice of 3), urgent (noul), refund (noul).
Metrics from the probability of the predicted class: ECE = expected calibration error (10 bins), acc@c = accuracy when p >= 0.7.

<!-- BENCH:START -->

> Partial runs present: all backends are compared on the same 49 tickets (ids 0..48). Failed tickets are excluded from the accuracy columns and counted in the errors column.


### team

| backend | n | acc | ECE | Brier | conf | acc@c | cov@c |
|---|---|---|---|---|---|---|---|
| deepseek-v4-flash | 49 | 0.88 | 0.076 | 0.175 | 0.88 | 0.91 | 0.90 |
| gemma-12b | 49 | 0.77 | 0.233 | 0.435 | 0.92 | 0.77 | 1.00 |
| jev-1.14.0 | 49 | 0.90 | 0.077 | 0.147 | 0.91 | 0.97 | 0.82 |
| xgboost-tfidf | 49 | 0.98 | 0.077 | 0.029 | 0.92 | 1.00 | 0.94 |

### urgent

| backend | n | acc | ECE | Brier | conf | acc@c | cov@c |
|---|---|---|---|---|---|---|---|
| deepseek-v4-flash | 49 | 0.98 | 0.063 | 0.026 | 0.94 | 1.00 | 0.98 |
| gemma-12b | 49 | 0.85 | 0.096 | 0.214 | 0.90 | 0.85 | 1.00 |
| jev-1.14.0 | 49 | 0.98 | 0.132 | 0.051 | 0.87 | 1.00 | 0.94 |
| xgboost-tfidf | 49 | 0.94 | 0.091 | 0.086 | 0.90 | 0.98 | 0.92 |

### refund

| backend | n | acc | ECE | Brier | conf | acc@c | cov@c |
|---|---|---|---|---|---|---|---|
| deepseek-v4-flash | 49 | 1.00 | 0.031 | 0.005 | 0.97 | 1.00 | 1.00 |
| gemma-12b | 49 | 0.94 | 0.048 | 0.089 | 0.98 | 0.94 | 1.00 |
| jev-1.14.0 | 49 | 1.00 | 0.043 | 0.006 | 0.96 | 1.00 | 1.00 |
| xgboost-tfidf | 49 | 0.98 | 0.035 | 0.051 | 0.94 | 0.98 | 0.98 |

### Speed and cost (all three questions per ticket in one call)

| backend | errors | mean latency / ticket | total cost | note |
|---|---|---|---|---|
| deepseek-v4-flash | 0 | 2219 ms | $0.0078 | deepseek/deepseek-v4-flash |
| gemma-12b | 2 | 16073 ms | $0.0000 | PARTIAL: 49 of 120 tickets, 2 failed (counted as errors) |
| jev-1.14.0 | 0 | 194 ms | $0.0008 | jev-latest |
| xgboost-tfidf | 0 | 0 ms | $0.0000 | 5-fold CV; trained on ~80% of the labelled tickets, needs labels per task |
<!-- BENCH:END -->

## Caveats to state in the course
- **Two result sets**: the full-set run (120 tickets: Jev, DeepSeek, XGBoost) is in `building-llm-applications/ch14/bench/results` history (commit a7059b9, summary in the earlier table: Jev team acc 0.91 / ECE 0.032, DeepSeek 0.87 / 0.063, XGBoost 0.86 / 0.076). The table above compares ALL backends on the same first 49 tickets, because gemma-12b was interrupted.
- gemma-12b covers only 49 of 120 tickets (ids 0..48, template-built only: the 20 hand-written tricky tickets are NOT included), and 2 tickets failed (the model never answered `refund` on "I do not want a refund" tickets, even when re-asked). On this subset XGBoost is favoured (team acc 0.98 vs 0.86 on the full set).
- Synthetic, template-heavy dataset; few tickets: differences of a few points are not significant. Some `team` errors may come from ambiguous labels (not audited).
- Jev is under-confident on `urgent` (conf 0.87 vs acc 0.98): calibrate thresholds per task.
- XGBoost fails on negations ("no rush") on the full set (urgent acc 0.87).
- **gemma-12b (local) is over-confident**: on `team` conf 0.92 but acc 0.77 (ECE 0.233), and it is never uncertain (cov@c 1.00), so a threshold-based router would never escalate its mistakes. It is also ~16 s/ticket vs 0.19 s for Jev and 2.2 s for DeepSeek. Do not use a general local LLM as a self-judge without calibration.

## Pending
- Remaining 71 tickets for gemma-12b (not run; no extrapolation is made) and OpenDecider-small/nano (backend written, never run against the real package).
- Refresh this file with: `bench/report.py --md bench/RESULTS.md --notes ../../agents-course/notes/benchmark-judge-results.md` (from `building-llm-applications/ch14`, with `agents-course` next to it).
