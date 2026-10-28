# Evaluating Physics-Informed Neural Network Variants for Nonlinear Dynamical Systems

[![DOI](https://zenodo.org/badge/1372118206.svg)](https://doi.org/10.5281/zenodo.22847682)

Code and results for *"Evaluating Physics-Informed Neural Network Variants for Nonlinear Dynamical Systems: A Multi-Seed Reliability Study of the Van der Pol Oscillator."*

This project benchmarks seven Physics-Informed Neural Network (PINN) configurations. They combine three network architectures (plain tanh, SIREN, Fourier-feature) with three temporal-decomposition strategies (none, uniform windowing, adaptive windowing). Each is tested against a high-precision RK45 reference solution of the Van der Pol oscillator at stiffness levels $\mu = 0.1$ to $50$.

The three adaptive models and the uniform-window tanh model are repeated across three random seeds at high stiffness. A 2×2 ablation then separates the two parts of the adaptive framework: where windows are placed and how each window is trained.

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
│   ├── Ablation A (Uniform + Extras)/
│   ├── Ablation B (Adaptive + Basic)/
│   ├── Base PINN Architecture.ipynb
│   └── Van der Pol Oscillator Visualizer Graph.ipynb
└── model results/
    ├── outputs/
    │   ├── plots/
    │   ├── tables/
    │   └── pinn_results_tidy.csv
    ├── model_results.json
    └── model_results.py
```

Each folder has its own README with details: [`code/README.md`](code/README.md) and [`model results/README.md`](model%20results/README.md).

## Models Evaluated

"Original PINN" in this repository is the model called **Standard PINN** in the paper.

| Model | Architecture | Window placement | Training | Seeds |
|---|---|---|---|---|
| Original (Standard) PINN | tanh MLP | None (single domain, soft IC) | Basic | 42 |
| Window PINN | tanh MLP | Uniform (width 2.0) | Basic | 42; plus 123 and 2026 at $\mu = 10, 20, 30$ |
| SIREN PINN | SIREN ($\omega_0 = 10$) | Uniform | Basic | 42 |
| Fourier Feature PINN | Random Fourier features | Uniform | Basic | 42 |
| Adaptive Window PINN | tanh MLP | Adaptive (reference-informed) | Extras | 42; plus 123 and 2026 at $\mu = 10$–$50$ |
| Adaptive SIREN PINN | SIREN ($\omega_0 = 10$) | Adaptive | Extras | same as above |
| Adaptive Fourier Feature PINN | Random Fourier features | Adaptive | Extras | same as above |
| Ablation A | tanh MLP | Uniform (width 2.0) | Extras | 42, 123, 2026 at $\mu = 10, 20, 30$ |
| Ablation B | tanh MLP | Adaptive | Basic | 42, 123, 2026 at $\mu = 10, 20, 30$ |

**Basic training:** each window is freshly initialized, uses 2,000 collocation points, and trains for 3,000 Adam epochs plus up to 2,000 L-BFGS iterations. There's no resampling, retries or gradient clipping.

**Training extras:**
- warm-starting from the previous window
- residual-based collocation resampling (80% residual-weighted, 20% uniform)
- a training budget that scales up with window width (up to 3× points and 2× Adam epochs)
- up to two L-BFGS retries for windows whose loss stays above $10^{-4}$
- gradient-norm clipping at 10.0

The four tanh models form the 2×2 ablation:

| | Basic training | Training extras |
|---|---|---|
| **Uniform placement** | Window PINN | Ablation A |
| **Adaptive placement** | Ablation B | Adaptive Window PINN |

## Requirements

- Python 3.10+
- torch (double precision; CUDA optional)
- numpy, scipy, pandas, matplotlib, tabulate

```bash
pip install torch numpy scipy pandas matplotlib tabulate
```

The notebooks were developed and run on Google Colab (NVIDIA T4 GPU). They also run on CPU, but training takes much longer, especially for the high-$\mu$ adaptive runs. Training times in the paper were measured on Colab and are indicative only.

## Reproducing the Results

1. Run the notebook(s) in `code/` for the model(s) and $\mu$ value(s) of interest. Put its results to `model results/model_results.json`.
2. Run `model results/model_results.py` to regenerate the summary tables and figures (relative L2 error vs. $\mu$, accuracy-vs-cost, physics-residual analysis) from `model_results.json`.

## Citation

If you use this code or data, please cite the paper and the archived version of this repository on Zenodo:

```bibtex
Citation TBA
```

## Data and Code Availability

This repository is archived on Zenodo, linked above and in the paper.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.