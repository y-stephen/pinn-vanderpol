# Mean Physics Residual by model and mu

Values are the median, min–max range across seeds for models with more than one run per mu (Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN); all other models are single-seed.

| model                         |       0.1 |       1.0 |       5.0 |      10.0 |        20.0 |        30.0 |     40.0 |   50.0 |
|:------------------------------|----------:|----------:|----------:|----------:|------------:|------------:|---------:|-------:|
| Original PINN                 | 1.259e-07 | 5.867e-07 | 0.003121  | 0.258     | nan         | nan         | nan      |  nan   |
| Window PINN                   | 5.644e-07 | 7.578e-07 | 1.227e-06 | 3.084     | nan         | nan         | nan      |  nan   |
| SIREN PINN                    | 2.118e-07 | 3.5e-07   | 5.606e-06 | 0.3905    | nan         | nan         | nan      |  nan   |
| Fourier Feature PINN          | 8.071e-07 | 8.294e-07 | 2.699e-06 | 0.5268    | nan         | nan         | nan      |  nan   |
| Adaptive Window PINN          | 1.252e-08 | 9.235e-08 | 9.991e-07 | 6.742e-06 |   3.347e-05 |   4.669e-05 |   0.3172 |  136.4 |
| Adaptive SIREN PINN           | 4.154e-08 | 2.3e-07   | 4.449e-06 | 0.0003008 |  32.55      | 453.1       | 184.2    |  670.3 |
| Adaptive Fourier Feature PINN | 7.192e-08 | 1.314e-07 | 2.524e-06 | 1.362e-05 |   3.839e-05 |  35.63      | 311      |  514.1 |
