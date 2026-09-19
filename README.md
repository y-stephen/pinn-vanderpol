# Evaluating Physics-Informed Neural Network Variants for Nonlinear Dynamical Systems

Code and results for *"Evaluating Physics-Informed Neural Network Variants for Nonlinear Dynamical Systems: A Multi-Seed Reliability Study of the Van der Pol Oscillator."*

This project benchmarks seven Physics-Informed Neural Network (PINN) configurations, combining three network architectures (plain/Vanilla, SIREN, Fourier-feature) with three temporal-decomposition strategies (none, uniform windowing, adaptive windowing). We test them against a high-precision RK45 reference solution of the Van der Pol oscillator, across stiffness levels $\mu = 0.1$ to $50$. The three adaptively-windowed models are additionally repeated across three random seeds at $\mu \geq 10$ to test how reproducible the observed architectural differences are.


## Repository Structure

```
.
├── code/
│   ├── Original PINN/
│   ├── Window PINN/
│   ├── SIREN PINN/
│   ├── Fourier Feature PINN/
│   ├── Adaptive Window PINN/
│   ├── Adaptive SIREN PINN/
│   ├── Adaptive Fourier Feature PINN/
│   └── visualization.ipynb
└── model results/
    ├── outputs/
    │   ├── plots/
    │   ├── tables/
    │   ├── pinn_results_tidy.csv
    ├── model_results.json
    └── model_results.py
```

See the README in each folder for details: [`code/README.md`](code/README.md), [`model results/README.md`](model%20results/README.md).

## Models Evaluated

| Model | Architecture | Windowing |
|---|---|---|
| Original PINN | Vanilla (tanh MLP) | None (soft IC constraint) |
| Window PINN | Vanilla | Uniform |
| SIREN PINN | SIREN | Uniform |
| Fourier Feature PINN | Random Fourier features | Uniform |
| Adaptive Window PINN | Vanilla | Adaptive |
| Adaptive SIREN PINN | SIREN | Adaptive |
| Adaptive Fourier Feature PINN | Random Fourier features | Adaptive |

The three non-adaptive baselines and the low-stiffness sweep ($\mu \leq 10$) use a single seed (42). The three adaptive models are additionally re-run at $\mu = 10, 20, 30, 40, 50$ with seeds 123 and 2026 for a multi-seed reliability comparison.

## Requirements

- Python 3.10+
- `torch` (double precision; CUDA optional)
- `numpy`, `scipy`, `pandas`, `matplotlib`

```bash
pip install torch numpy scipy pandas matplotlib
```

The notebooks were developed and run on Google Colab (NVIDIA T4 GPU); they will also run on CPU, with longer training times, particularly for the adaptive high-$\mu$ runs.

## Reproducing the Results

1. Run the notebook(s) in `code/` for the model(s) and $\mu$ value(s) of interest. Put its results to `model results/model_results.json`.
2. Run `model results/model_results.py` to regenerate the summary tables and figures (relative L2 error vs. $\mu$, accuracy-vs-cost, physics-residual analysis) from `model_results.json`.

## Reference Solution

The ground-truth solution used for error comparison is generated with SciPy's `solve_ivp` (RK45, `rtol=1e-10`, `atol=1e-12`, max step $0.05$), evaluated on a fixed grid shared by all PINN variants for a given $\mu$.


## Citation

If you use this code or data, please cite the associated paper and, if applicable, the archived version of this repository on Zenodo:

```
[citation details to be added after proceedings]
```

## Data and Code Availability

This repository is archived on Zenodo. See the paper's "Code Availability" section for the DOI.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.