# Code

This folder contains the notebooks used to train and evaluate the Physics-Informed Neural Network (PINN) variants for the Van der Pol oscillator.

## Notebook Organization

The notebooks are grouped by model:

- **Original PINN/** (the paper's *Standard PINN*): a tanh MLP over the whole domain, with no temporal windowing and a soft initial-condition loss.
- **Window PINN/:** a tanh MLP with uniform time windows (width 2.0) and basic training.
- **SIREN PINN/:** a SIREN network with uniform windows and basic training. $\omega_0 = 10$ is fixed, and each window is freshly initialized, with no warm-start.
- **Fourier Feature PINN/:** a random Fourier-feature network with uniform windows and basic training. Each window draws its own frequency matrix $B$.
- **Adaptive Window PINN/:** a tanh MLP with adaptive, reference-informed windows and the training extras.
- **Adaptive SIREN PINN/:** a SIREN network with adaptive windows and the training extras.
- **Adaptive Fourier Feature PINN/:** a random Fourier-feature network with adaptive windows and the training extras. One $B$ is shared across all windows.
- **Ablation A (Uniform + Extras)/:** a tanh MLP with uniform windows and the training extras. It's identical to the Adaptive Window PINN except that the window edges use the uniform rule from Window PINN.
- **Ablation B (Adaptive + Basic)/:** a tanh MLP with adaptive windows and basic training. It's identical to Window PINN except that the window edges come from the adaptive placement algorithm.

Each model folder contains notebooks for the $\mu$ values tested. The Seed subfolders hold the repeated multi-seed runs (seeds 123 and 2026) for:
- the adaptive models
- Window PINN
- the two ablation models

### Training procedures

**Basic training** (Window, SIREN, Fourier, Ablation B):
- fresh Xavier (or SIREN) initialization in every window
- 2,000 uniformly random collocation points
- Adam (3,000 epochs, learning rate $10^{-3}$), then L-BFGS (up to 2,000 iterations, strong-Wolfe line search)

**Training extras** (all adaptive models and Ablation A) add:
- warm-starting each window from the previous window's weights
- residual-based collocation resampling every 500 Adam epochs and before L-BFGS (80% residual-weighted, 20% uniform)
- a budget that scales up with window width: $2000 \cdot \mathrm{clip}(w/\bar w, 1, 3)$ points and $3000 \cdot \mathrm{clip}(w/\bar w, 1, 2)$ Adam epochs, with L-BFGS not scaled
- up to two extra L-BFGS passes for windows whose final loss is above $10^{-4}$
- gradient-norm clipping at 10.0 during Adam

**Adaptive placement:**
- Window edges come from equidistributing the monitor function $m(t) = 0.4\,|x'|/\max|x'| + 0.6\,|x''|/\max|x''|$, computed from an RK45 solution.
- The target is 10 windows, with a minimum width of 0.15.
- Windows wider than 3.0 are split, which gives 10, 10, 12, 15, 21, 28, 33 and 39 windows at $\mu = 0.1, 1, 5, 10, 20, 30, 40, 50$.

**Uniform placement:** width 2.0, with $N = \mathrm{round}(T_\text{final}/2)$ and the last edge set to $T_\text{final}$. This gives 4, 4, 7, 11, 20 and 29 windows at $\mu = 0.1, 1, 5, 10, 20, 30$.

The Fourier notebooks still contain the $\sigma$/mapping-size grid-search code ($\sigma \in \{0.5, 1, 2, 5, 10, 20, 30\}$, $m \in \{12, 16, 32\}$). Every reported Fourier run used $m = 32$ and $\sigma = 0.5$.

## What the Notebooks Do

Each notebook defines the model, trains it with Adam followed by L-BFGS, computes an RK45 reference solution, and evaluates prediction and metrics.

Base PINN Architecture.ipynb contains the shared structure and classes for the base PINN models that the other model notebooks build on.

Van der Pol Oscillator Visualizer Graph.ipynb plots the RK45 reference solution, including its time series and phase portrait, for a selected $\mu$ value.