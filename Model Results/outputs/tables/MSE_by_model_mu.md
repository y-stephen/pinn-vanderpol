# MSE by model and mu

Where a model has more than one seed at a mu (Window PINN, Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN, Ablation A: Uniform + Extras, Ablation B: Adaptive + Basic), values are the median, min–max range across seeds; all other cells are single-seed.

| model                         |         0.1 |         1.0 |         5.0 |      10.0 |        20.0 |       30.0 |        40.0 |    50.0 |
|:------------------------------|------------:|------------:|------------:|----------:|------------:|-----------:|------------:|--------:|
| Standard PINN                 |   7.092e-11 |   4.781e-10 |   0.1448    | 3.092     | nan         | nan        | nan         | nan     |
| Window PINN                   |   1.246e-09 |   7.1e-09   |   1.056e-08 | 1.69      |  12.42      |   4.26     | nan         | nan     |
| SIREN PINN                    |   2.147e-10 |   2.955e-09 |   5.833e-07 | 0.782     | nan         | nan        | nan         | nan     |
| Fourier Feature PINN          |   1.186e-09 |   2.115e-10 |   6.886e-08 | 0.6321    | nan         | nan        | nan         | nan     |
| Adaptive Window PINN          |   4.394e-10 |   3.2e-10   |   2.086e-08 | 1.89e-06  |   5.705e-05 |   4.25e-05 |   0.0007315 |   1.737 |
| Adaptive SIREN PINN           |   4.464e-10 |   8.929e-10 |   3.054e-08 | 2.2e-05   |   0.04211   |   3.16     |   7.465     |   6.444 |
| Adaptive Fourier Feature PINN |   5.449e-10 |   1.074e-09 |   2.857e-08 | 3.681e-06 |   0.000247  |   7.913    |   4.974     |   7.584 |
| Ablation A: Uniform + Extras  | nan         | nan         | nan         | 1.61      |   0.7395    |   0.9901   | nan         | nan     |
| Ablation B: Adaptive + Basic  | nan         | nan         | nan         | 1.599e-07 |   2.88e-06  |   0.01006  | nan         | nan     |
