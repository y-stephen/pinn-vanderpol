# Training Time (s) by model and mu

Where a model has more than one seed at a mu (Window PINN, Adaptive Window PINN, Adaptive SIREN PINN, Adaptive Fourier Feature PINN, Ablation A: Uniform + Extras, Ablation B: Adaptive + Basic), values are the median, min–max range across seeds; all other cells are single-seed.

| model                         |   0.1 |   1.0 |   5.0 |   10.0 |   20.0 |   30.0 |   40.0 |   50.0 |
|:------------------------------|------:|------:|------:|-------:|-------:|-------:|-------:|-------:|
| Standard PINN                 |  88.9 | 209.3 | 206.3 |  210.8 |  nan   |  nan   |    nan |    nan |
| Window PINN                   | 118.7 | 164.9 | 269.1 |  416.7 |  800   | 1101   |    nan |    nan |
| SIREN PINN                    | 223.6 | 228.3 | 421.8 |  662.8 |  nan   |  nan   |    nan |    nan |
| Fourier Feature PINN          | 227.9 | 249.8 | 468.2 |  697.1 |  nan   |  nan   |    nan |    nan |
| Adaptive Window PINN          | 266.7 | 324.2 | 591.6 |  845.2 | 1124   | 1528   |   1990 |   2383 |
| Adaptive SIREN PINN           | 466.9 | 440   | 701.6 | 1239   | 1834   | 2010   |   1579 |   3494 |
| Adaptive Fourier Feature PINN | 418.1 | 687.9 | 864.2 | 1114   | 1526   | 3006   |   2886 |   3416 |
| Ablation A: Uniform + Extras  | nan   | nan   | nan   |  727.3 | 1035   | 1631   |    nan |    nan |
| Ablation B: Adaptive + Basic  | nan   | nan   | nan   |  679.1 |  748.7 |  943.3 |    nan |    nan |
