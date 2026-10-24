# MAE by model and mu

Where a model has more than one seed at a mu (Window PINN, Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN, Ablation A: Uniform + Extras, Ablation B: Adaptive + Basic), values are the median, min–max range across seeds; all other cells are single-seed.

| model                         |         0.1 |         1.0 |         5.0 |      10.0 |        20.0 |        30.0 |       40.0 |     50.0 |
|:------------------------------|------------:|------------:|------------:|----------:|------------:|------------:|-----------:|---------:|
| Standard PINN                 |   6.603e-06 |   1.66e-05  |   0.1648    | 1.601     | nan         | nan         | nan        | nan      |
| Window PINN                   |   2.963e-05 |   7.053e-05 |   4.623e-05 | 0.7145    |   2.615     |   1.561     | nan        | nan      |
| SIREN PINN                    |   1.279e-05 |   4.349e-05 |   0.0003107 | 0.3719    | nan         | nan         | nan        | nan      |
| Fourier Feature PINN          |   2.754e-05 |   1.161e-05 |   0.0001256 | 0.291     | nan         | nan         | nan        | nan      |
| Adaptive Window PINN          |   1.727e-05 |   1.577e-05 |   5.558e-05 | 0.0003234 |   0.0008732 |   0.0005516 |   0.002834 |   0.6968 |
| Adaptive SIREN PINN           |   1.686e-05 |   1.845e-05 |   6.58e-05  | 0.00115   |   0.08319   |   1.161     |   2.213    |   2.028  |
| Adaptive Fourier Feature PINN |   1.885e-05 |   2.659e-05 |   7.544e-05 | 0.0004579 |   0.001921  |   2.49      |   1.644    |   2.38   |
| Ablation A: Uniform + Extras  | nan         | nan         | nan         | 0.9083    |   0.3191    |   0.3895    | nan        | nan      |
| Ablation B: Adaptive + Basic  | nan         | nan         | nan         | 8.932e-05 |   0.0002383 |   0.0096    | nan        | nan      |
