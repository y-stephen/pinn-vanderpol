# Relative L2 error: seed robustness (mean/std/min/max across seeds)

Seeds used: 42, 123, 2026. cv_pct = std / mean * 100.

| model                         |   mu |   n_seeds |      mean |         std |       min |       max |   cv_pct |
|:------------------------------|-----:|----------:|----------:|------------:|----------:|----------:|---------:|
| Adaptive Window PINN          |  0.1 |         1 | 2.506e-05 | nan         | 2.506e-05 | 2.506e-05 |  nan     |
| Adaptive Window PINN          |  1   |         1 | 1.383e-05 | nan         | 1.383e-05 | 1.383e-05 |  nan     |
| Adaptive Window PINN          |  5   |         1 | 9.444e-05 | nan         | 9.444e-05 | 9.444e-05 |  nan     |
| Adaptive Window PINN          | 10   |         3 | 0.0009126 |   0.000145  | 0.0008134 | 0.001079  |   15.89  |
| Adaptive Window PINN          | 20   |         3 | 0.005144  |   0.004443  | 0.001048  | 0.009868  |   86.37  |
| Adaptive Window PINN          | 30   |         3 | 0.003812  |   0.0001735 | 0.003617  | 0.00395   |    4.552 |
| Adaptive Window PINN          | 40   |         3 | 0.3271    |   0.5416    | 0.01279   | 0.9525    |  165.6   |
| Adaptive Window PINN          | 50   |         3 | 0.7873    |   0.1446    | 0.6477    | 0.9365    |   18.37  |
| Adaptive SIREN PINN           |  0.1 |         1 | 2.526e-05 | nan         | 2.526e-05 | 2.526e-05 |  nan     |
| Adaptive SIREN PINN           |  1   |         1 | 2.311e-05 | nan         | 2.311e-05 | 2.311e-05 |  nan     |
| Adaptive SIREN PINN           |  5   |         1 | 0.0001143 | nan         | 0.0001143 | 0.0001143 |  nan     |
| Adaptive SIREN PINN           | 10   |         3 | 0.01203   |   0.01778   | 0.0006888 | 0.03252   |  147.8   |
| Adaptive SIREN PINN           | 20   |         3 | 0.5151    |   0.7006    | 0.09872   | 1.324     |  136     |
| Adaptive SIREN PINN           | 30   |         3 | 0.9634    |   0.3641    | 0.5622    | 1.273     |   37.8   |
| Adaptive SIREN PINN           | 40   |         3 | 1.569     |   0.1136    | 1.44      | 1.653     |    7.239 |
| Adaptive SIREN PINN           | 50   |         3 | 3.334     |   4.377     | 0.1733    | 8.33      |  131.3   |
| Adaptive Fourier Feature PINN |  0.1 |         1 | 2.791e-05 | nan         | 2.791e-05 | 2.791e-05 |  nan     |
| Adaptive Fourier Feature PINN |  1   |         1 | 2.535e-05 | nan         | 2.535e-05 | 2.535e-05 |  nan     |
| Adaptive Fourier Feature PINN |  5   |         1 | 0.0001105 | nan         | 0.0001105 | 0.0001105 |  nan     |
| Adaptive Fourier Feature PINN | 10   |         3 | 0.001307  |   0.0003754 | 0.001011  | 0.001729  |   28.73  |
| Adaptive Fourier Feature PINN | 20   |         3 | 0.01063   |   0.002408  | 0.009078  | 0.0134    |   22.66  |
| Adaptive Fourier Feature PINN | 30   |         3 | 1.362     |   0.5485    | 0.7286    | 1.688     |   40.28  |
| Adaptive Fourier Feature PINN | 40   |         3 | 1.421     |   0.3984    | 1.083     | 1.86      |   28.04  |
| Adaptive Fourier Feature PINN | 50   |         3 | 1.573     |   0.2138    | 1.338     | 1.756     |   13.59  |
