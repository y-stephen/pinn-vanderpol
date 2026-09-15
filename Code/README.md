# Code

This folder contains the notebooks used to train and evaluate the Physics-Informed Neural Network variants for the Van der Pol oscillator.

## Notebook Organization

The notebooks are grouped by model family and temporal-windowing strategy:

- Original PINN/: vanilla tanh MLP without temporal windowing
- Window PINN/: vanilla MLP with uniform time windows
- SIREN PINN/: SIREN network with uniform time windows
- Fourier Feature PINN/: random Fourier-feature network with uniform time windows
- Adaptive Window PINN/: vanilla MLP with adaptive time windows
- Adaptive SIREN PINN/: SIREN network with adaptive time windows
- Adaptive Fourier Feature PINN/: random Fourier-feature network with adaptive time windows

Each model folder contains notebooks for the tested stiffness values, $\mu$. The adaptive model folders also contain `Seed` subfolders for the repeated multi-seed experiments.

## What the Notebooks Do

Each notebook defines the model, trains it with Adam followed by L-BFGS, computes an RK45 reference solution, and evaluates prediction and metrics.

visualization.ipynb plots the RK45 reference solution, including its time series and phase portrait, for a selected $\mu$ value.