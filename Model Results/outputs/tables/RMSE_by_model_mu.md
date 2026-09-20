# RMSE by model and mu

Values are the median, min–max range across seeds for models with more than one run per mu (Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN); all other models are single-seed.

| model                         |       0.1 |       1.0 |       5.0 |     10.0 |       20.0 |       30.0 |      40.0 |    50.0 |
|:------------------------------|----------:|----------:|----------:|---------:|-----------:|-----------:|----------:|--------:|
| Standard PINN                 | 8.421e-06 | 2.186e-05 | 0.3805    | 1.758    | nan        | nan        | nan       | nan     |
| Window PINN                   | 3.53e-05  | 8.426e-05 | 0.0001028 | 1.548    | nan        | nan        | nan       | nan     |
| SIREN PINN                    | 3.036e-05 | 1.804e-05 | 0.0002286 | 0.8762   | nan        | nan        | nan       | nan     |
| Fourier Feature PINN          | 3.444e-05 | 1.454e-05 | 0.0002624 | 0.7951   | nan        | nan        | nan       | nan     |
| Adaptive Window PINN          | 2.096e-05 | 1.789e-05 | 0.0001444 | 0.001375 |   0.007553 |   0.006519 |   0.02705 |   1.318 |
| Adaptive SIREN PINN           | 2.113e-05 | 2.988e-05 | 0.0001748 | 0.00469  |   0.2052   |   1.778    |   2.732   |   2.539 |
| Adaptive Fourier Feature PINN | 2.334e-05 | 3.277e-05 | 0.000169  | 0.001919 |   0.01572  |   2.813    |   2.23    |   2.754 |
