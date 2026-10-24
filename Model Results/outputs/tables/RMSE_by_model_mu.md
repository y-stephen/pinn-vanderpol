# RMSE by model and mu

Where a model has more than one seed at a mu (Window PINN, Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN, Ablation A: Uniform + Extras, Ablation B: Adaptive + Basic), values are the median, min–max range across seeds; all other cells are single-seed.

| model                         |         0.1 |         1.0 |         5.0 |      10.0 |       20.0 |       30.0 |      40.0 |    50.0 |
|:------------------------------|------------:|------------:|------------:|----------:|-----------:|-----------:|----------:|--------:|
| Standard PINN                 |   8.421e-06 |   2.186e-05 |   0.3805    | 1.758     | nan        | nan        | nan       | nan     |
| Window PINN                   |   3.53e-05  |   8.426e-05 |   0.0001028 | 1.3       |   3.524    |   2.064    | nan       | nan     |
| SIREN PINN                    |   1.465e-05 |   5.436e-05 |   0.0007638 | 0.8843    | nan        | nan        | nan       | nan     |
| Fourier Feature PINN          |   3.444e-05 |   1.454e-05 |   0.0002624 | 0.7951    | nan        | nan        | nan       | nan     |
| Adaptive Window PINN          |   2.096e-05 |   1.789e-05 |   0.0001444 | 0.001375  |   0.007553 |   0.006519 |   0.02705 |   1.318 |
| Adaptive SIREN PINN           |   2.113e-05 |   2.988e-05 |   0.0001748 | 0.00469   |   0.2052   |   1.778    |   2.732   |   2.539 |
| Adaptive Fourier Feature PINN |   2.334e-05 |   3.277e-05 |   0.000169  | 0.001919  |   0.01572  |   2.813    |   2.23    |   2.754 |
| Ablation A: Uniform + Extras  | nan         | nan         | nan         | 1.269     |   0.8599   |   0.995    | nan       | nan     |
| Ablation B: Adaptive + Basic  | nan         | nan         | nan         | 0.0003999 |   0.001697 |   0.1003   | nan       | nan     |
