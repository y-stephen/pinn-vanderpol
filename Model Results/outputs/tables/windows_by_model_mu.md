# Number of Windows by model and mu

Where a model has more than one seed at a mu (Window PINN, Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN, Ablation A: Uniform + Extras, Ablation B: Adaptive + Basic), values are the median, min–max range across seeds; all other cells are single-seed.

| model                         |   0.1 |   1.0 |   5.0 |   10.0 |   20.0 |   30.0 |   40.0 |   50.0 |
|:------------------------------|------:|------:|------:|-------:|-------:|-------:|-------:|-------:|
| Standard PINN                 |     1 |     1 |     1 |      1 |    nan |    nan |    nan |    nan |
| Window PINN                   |     4 |     4 |     7 |     11 |     20 |     29 |    nan |    nan |
| SIREN PINN                    |     4 |     4 |     7 |     11 |    nan |    nan |    nan |    nan |
| Fourier Feature PINN          |     4 |     4 |     7 |     11 |    nan |    nan |    nan |    nan |
| Adaptive Window PINN          |    10 |    10 |    12 |     15 |     21 |     28 |     33 |     39 |
| Adaptive SIREN PINN           |    10 |    10 |    12 |     15 |     21 |     28 |     33 |     39 |
| Adaptive Fourier Feature PINN |    10 |    10 |    12 |     15 |     21 |     28 |     33 |     39 |
| Ablation A: Uniform + Extras  |   nan |   nan |   nan |     11 |     20 |     29 |    nan |    nan |
| Ablation B: Adaptive + Basic  |   nan |   nan |   nan |     15 |     21 |     28 |    nan |    nan |
