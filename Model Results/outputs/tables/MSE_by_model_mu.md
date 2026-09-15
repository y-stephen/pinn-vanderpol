# MSE by model and mu

Values are the median, min–max range across seeds for models with more than one run per mu (Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN); all other models are single-seed.

| model                         |       0.1 |       1.0 |       5.0 |      10.0 |        20.0 |       30.0 |        40.0 |    50.0 |
|:------------------------------|----------:|----------:|----------:|----------:|------------:|-----------:|------------:|--------:|
| Original PINN                 | 7.092e-11 | 4.781e-10 | 0.1448    | 3.092     | nan         | nan        | nan         | nan     |
| Window PINN                   | 1.246e-09 | 7.1e-09   | 1.056e-08 | 2.396     | nan         | nan        | nan         | nan     |
| SIREN PINN                    | 9.217e-10 | 3.256e-10 | 5.224e-08 | 0.7678    | nan         | nan        | nan         | nan     |
| Fourier Feature PINN          | 1.186e-09 | 2.115e-10 | 6.886e-08 | 0.6321    | nan         | nan        | nan         | nan     |
| Adaptive Window PINN          | 4.394e-10 | 3.2e-10   | 2.086e-08 | 1.89e-06  |   5.705e-05 |   4.25e-05 |   0.0007315 |   1.737 |
| Adaptive SIREN PINN           | 4.464e-10 | 8.929e-10 | 3.054e-08 | 2.2e-05   |   0.04211   |   3.16     |   7.465     |   6.444 |
| Adaptive Fourier Feature PINN | 5.449e-10 | 1.074e-09 | 2.857e-08 | 3.681e-06 |   0.000247  |   7.913    |   4.974     |   7.584 |
