# Ablation: window placement x training procedure (tanh network)

Relative L2 error: median (min–max across seeds), and seeds with error <= 5%. Basic = fresh init, fixed budget, no resampling/retries/clipping. Extras = warm-start, residual-based resampling, width-scaled budget, L-BFGS retries, gradient clipping.

| config                             | mu=10                            | mu=20                          | mu=30                         |
|:-----------------------------------|:---------------------------------|:-------------------------------|:------------------------------|
| Uniform windows + Basic training   | 0.8 (0.72–0.95), 0/3 ok          | 2.1 (1.2–4.1), 0/3 ok          | 1.2 (0.91–1.3), 0/3 ok        |
| Uniform windows + Extras training  | 0.78 (0.0089–1), 1/3 ok          | 0.51 (0.22–0.68), 0/3 ok       | 0.59 (0.59–1), 0/3 ok         |
| Adaptive windows + Basic training  | 0.00025 (0.00024–0.0009), 3/3 ok | 0.001 (0.00027–0.0014), 3/3 ok | 0.06 (0.0084–0.066), 1/3 ok   |
| Adaptive windows + Extras training | 0.00085 (0.00081–0.0011), 3/3 ok | 0.0045 (0.001–0.0099), 3/3 ok  | 0.0039 (0.0036–0.004), 3/3 ok |

## Median training time (s)

| config                             |   mu=10 |   mu=20 |   mu=30 |
|:-----------------------------------|--------:|--------:|--------:|
| Uniform windows + Basic training   |     417 |     800 |    1101 |
| Uniform windows + Extras training  |     727 |    1035 |    1631 |
| Adaptive windows + Basic training  |     679 |     749 |     943 |
| Adaptive windows + Extras training |     845 |    1124 |    1528 |

## Median total gradient evaluations (where recorded)

| config                             |   mu=10 |   mu=20 |   mu=30 |
|:-----------------------------------|--------:|--------:|--------:|
| Uniform windows + Basic training   |     nan |     nan |     nan |
| Uniform windows + Extras training  |   71003 |   94687 |  153893 |
| Adaptive windows + Basic training  |     nan |     nan |     nan |
| Adaptive windows + Extras training |     nan |     nan |     nan |

## Per-seed relative L2 error

| placement   | training   |   mu | seeds_rel_L2                                |
|:------------|:-----------|-----:|:--------------------------------------------|
| Uniform     | Basic      |   10 | 42: 0.952, 123: 0.725, 2026: 0.799          |
| Uniform     | Basic      |   20 | 42: 4.14, 123: 2.11, 2026: 1.16             |
| Uniform     | Basic      |   30 | 42: 1.23, 123: 0.909, 2026: 1.3             |
| Uniform     | Extras     |   10 | 42: 1.04, 123: 0.00889, 2026: 0.78          |
| Uniform     | Extras     |   20 | 42: 0.677, 123: 0.514, 2026: 0.218          |
| Uniform     | Extras     |   30 | 42: 1.04, 123: 0.586, 2026: 0.59            |
| Adaptive    | Basic      |   10 | 42: 0.000899, 123: 0.000239, 2026: 0.000246 |
| Adaptive    | Basic      |   20 | 42: 0.00135, 123: 0.00102, 2026: 0.000266   |
| Adaptive    | Basic      |   30 | 42: 0.00836, 123: 0.0595, 2026: 0.0662      |
| Adaptive    | Extras     |   10 | 42: 0.000813, 123: 0.00108, 2026: 0.000845  |
| Adaptive    | Extras     |   20 | 42: 0.00105, 123: 0.00987, 2026: 0.00452    |
| Adaptive    | Extras     |   30 | 42: 0.00362, 123: 0.00395, 2026: 0.00387    |
