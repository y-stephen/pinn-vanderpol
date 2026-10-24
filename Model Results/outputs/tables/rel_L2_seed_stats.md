# Relative L2 error: seed robustness (mean/std/min/max across seeds)

Seeds used: 42, 123, 2026. cv_pct = std / mean * 100. n_fail = seeds with relative L2 error > 5%.

| model                         |   mu |   n_seeds |      mean |       std |       min |       max |   n_fail |   cv_pct |
|:------------------------------|-----:|----------:|----------:|----------:|----------:|----------:|---------:|---------:|
| Window PINN                   |   10 |         3 | 0.8254    | 0.1157    | 0.7249    | 0.9519    |        3 |   14.02  |
| Window PINN                   |   20 |         3 | 2.471     | 1.525     | 1.16      | 4.145     |        3 |   61.73  |
| Window PINN                   |   30 |         3 | 1.144     | 0.2064    | 0.9089    | 1.297     |        3 |   18.05  |
| Adaptive Window PINN          |   10 |         3 | 0.0009126 | 0.000145  | 0.0008134 | 0.001079  |        0 |   15.89  |
| Adaptive Window PINN          |   20 |         3 | 0.005144  | 0.004443  | 0.001048  | 0.009868  |        0 |   86.37  |
| Adaptive Window PINN          |   30 |         3 | 0.003812  | 0.0001735 | 0.003617  | 0.00395   |        0 |    4.552 |
| Adaptive Window PINN          |   40 |         3 | 0.3271    | 0.5416    | 0.01279   | 0.9525    |        1 |  165.6   |
| Adaptive Window PINN          |   50 |         3 | 0.7873    | 0.1446    | 0.6477    | 0.9365    |        3 |   18.37  |
| Adaptive SIREN PINN           |   10 |         3 | 0.01203   | 0.01778   | 0.0006888 | 0.03252   |        0 |  147.8   |
| Adaptive SIREN PINN           |   20 |         3 | 0.5151    | 0.7006    | 0.09872   | 1.324     |        3 |  136     |
| Adaptive SIREN PINN           |   30 |         3 | 0.9634    | 0.3641    | 0.5622    | 1.273     |        3 |   37.8   |
| Adaptive SIREN PINN           |   40 |         3 | 1.569     | 0.1136    | 1.44      | 1.653     |        3 |    7.239 |
| Adaptive SIREN PINN           |   50 |         3 | 3.334     | 4.377     | 0.1733    | 8.33      |        3 |  131.3   |
| Adaptive Fourier Feature PINN |   10 |         3 | 0.001307  | 0.0003754 | 0.001011  | 0.001729  |        0 |   28.73  |
| Adaptive Fourier Feature PINN |   20 |         3 | 0.01063   | 0.002408  | 0.009078  | 0.0134    |        0 |   22.66  |
| Adaptive Fourier Feature PINN |   30 |         3 | 1.362     | 0.5485    | 0.7286    | 1.688     |        3 |   40.28  |
| Adaptive Fourier Feature PINN |   40 |         3 | 1.421     | 0.3984    | 1.083     | 1.86      |        3 |   28.04  |
| Adaptive Fourier Feature PINN |   50 |         3 | 1.573     | 0.2138    | 1.338     | 1.756     |        3 |   13.59  |
| Ablation A: Uniform + Extras  |   10 |         3 | 0.61      | 0.5367    | 0.008891  | 1.041     |        2 |   87.98  |
| Ablation A: Uniform + Extras  |   20 |         3 | 0.4699    | 0.2325    | 0.2184    | 0.6769    |        3 |   49.47  |
| Ablation A: Uniform + Extras  |   30 |         3 | 0.7378    | 0.2591    | 0.586     | 1.037     |        3 |   35.12  |
| Ablation B: Adaptive + Basic  |   10 |         3 | 0.0004613 | 0.000379  | 0.0002392 | 0.0008989 |        0 |   82.14  |
| Ablation B: Adaptive + Basic  |   20 |         3 | 0.0008785 | 0.0005565 | 0.0002664 | 0.001354  |        0 |   63.35  |
| Ablation B: Adaptive + Basic  |   30 |         3 | 0.04469   | 0.03164   | 0.008359  | 0.06618   |        2 |   70.8   |
