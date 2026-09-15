# Number of Windows by model and mu

Values are the median, min–max range across seeds for models with more than one run per mu (Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN); all other models are single-seed.

| model                         |   0.1 |   1.0 |   5.0 |   10.0 |   20.0 |   30.0 |   40.0 |   50.0 |
|:------------------------------|------:|------:|------:|-------:|-------:|-------:|-------:|-------:|
| Original PINN                 |     1 |     1 |     1 |      1 |    nan |    nan |    nan |    nan |
| Window PINN                   |     4 |     4 |     7 |     11 |    nan |    nan |    nan |    nan |
| SIREN PINN                    |     4 |     4 |     7 |     11 |    nan |    nan |    nan |    nan |
| Fourier Feature PINN          |     4 |     4 |     7 |     11 |    nan |    nan |    nan |    nan |
| Adaptive Window PINN          |    10 |    10 |    12 |     15 |     21 |     28 |     33 |     39 |
| Adaptive SIREN PINN           |    10 |    10 |    12 |     15 |     21 |     28 |     33 |     39 |
| Adaptive Fourier Feature PINN |    10 |    10 |    12 |     15 |     21 |     28 |     33 |     39 |
