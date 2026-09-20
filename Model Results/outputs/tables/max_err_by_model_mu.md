# Max Error (L-inf) by model and mu

Values are the median, min–max range across seeds for models with more than one run per mu (Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN); all other models are single-seed.

| model                         |       0.1 |       1.0 |       5.0 |    10.0 |     20.0 |     30.0 |    40.0 |    50.0 |
|:------------------------------|----------:|----------:|----------:|--------:|---------:|---------:|--------:|--------:|
| Standard PINN                 | 1.834e-05 | 5.51e-05  | 1.983     | 3.023   | nan      | nan      | nan     | nan     |
| Window PINN                   | 7.382e-05 | 0.0001853 | 0.0006182 | 3.504   | nan      | nan      | nan     | nan     |
| SIREN PINN                    | 4.997e-05 | 4.738e-05 | 0.001128  | 2.851   | nan      | nan      | nan     | nan     |
| Fourier Feature PINN          | 7.058e-05 | 3.556e-05 | 0.001251  | 2.967   | nan      | nan      | nan     | nan     |
| Adaptive Window PINN          | 3.935e-05 | 3.081e-05 | 0.0009144 | 0.01711 |   0.1797 |   0.2167 |   1.093 |   3.398 |
| Adaptive SIREN PINN           | 3.414e-05 | 8.829e-05 | 0.001102  | 0.05479 |   2.637  |   3.613  |   4.548 |   4.324 |
| Adaptive Fourier Feature PINN | 4.472e-05 | 7.57e-05  | 0.0009601 | 0.01988 |   0.3534 |   3.886  |   3.965 |   4.005 |
