import os
import json
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()

DATA_PATH = os.path.join(SCRIPT_DIR, "model_results.json")


def load_raw_data(path: str = DATA_PATH):
    with open(path, "r") as f:
        return json.load(f)


RAW_DATA = load_raw_data()

MODEL_ORDER = [
    "Original PINN",
    "Window PINN",
    "SIREN PINN",
    "Fourier Feature PINN",
    "Adaptive Window PINN",
    "Adaptive SIREN PINN",
    "Adaptive Fourier Feature PINN",
]
 
MODEL_STYLE = {
    "Original PINN": dict(color="#7f7f7f", marker="o", linestyle="--"),
    "Window PINN": dict(color="#1f77b4", marker="o", linestyle="--"),
    "SIREN PINN": dict(color="#2ca02c", marker="o", linestyle="--"),
    "Fourier Feature PINN": dict(color="#d62728", marker="o", linestyle="--"),
    "Adaptive Window PINN": dict(color="#1f77b4", marker="s", linestyle="-"),
    "Adaptive SIREN PINN": dict(color="#2ca02c", marker="s", linestyle="-"),
    "Adaptive Fourier Feature PINN": dict(color="#d62728", marker="s", linestyle="-"),
}
 
MULTI_SEED_MODELS = ["Adaptive Window PINN", "Adaptive SIREN PINN", "Adaptive Fourier Feature PINN"]
SEED_COLORS = {42: "#444444", 123: "#e08214", 2026: "#8073ac"}

AGG_CENTER = "median"
AGG_SPREAD = "range"


def _agg_desc(center: str = AGG_CENTER, spread: str = AGG_SPREAD) -> str:
    center_str = {"median": "median", "mean": "mean", "geometric": "geometric mean"}.get(center, center)
    spread_str = {"range": "min\u2013max range", "std": "\u00b11 std", "geometric": "\u00d7\u00f7 geometric std"}.get(spread, spread)
    return f"{center_str}, {spread_str}"
 
METRIC_LABELS = {
    "rel_L2": "Relative L2 Error",
    "MSE": "MSE",
    "RMSE": "RMSE",
    "MAE": "MAE",
    "max_err": "Max Error (L-inf)",
    "final_train_loss": "Final Training Loss",
    "mean_phys_residual": "Mean Physics Residual",
    "train_time_s": "Training Time (s)",
    "windows": "Number of Windows",
}
 
OUT_DIR = os.path.join(SCRIPT_DIR, "outputs")
TABLE_DIR = os.path.join(OUT_DIR, "tables")
PLOT_DIR = os.path.join(OUT_DIR, "plots")
 
 
def build_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(RAW_DATA)
    df["model"] = pd.Categorical(df["model"], categories=MODEL_ORDER, ordered=True)
    df = df.sort_values(["model", "mu", "seed"]).reset_index(drop=True)
    return df
 
 
def _log_groupby_mean_std(df: pd.DataFrame, metric_cols, group_cols=("model", "mu")):
    log_vals = df[metric_cols].where(df[metric_cols] > 0).apply(np.log)
    log_vals[list(group_cols)] = df[list(group_cols)]
    grouped = log_vals.groupby(list(group_cols), observed=True)[metric_cols]
    return grouped.mean(), grouped.std()


def build_agg_dataframe(df: pd.DataFrame, center: str = AGG_CENTER, spread: str = AGG_SPREAD) -> pd.DataFrame:
    metric_cols = ["MSE", "rel_L2", "final_train_loss", "mean_phys_residual", "train_time_s", "MAE", "max_err", "RMSE"]
    metric_cols = [c for c in metric_cols if c in df.columns]
    g = df.groupby(["model", "mu"], observed=True)

    if center == "median":
        center_df = g[metric_cols].median()
    elif center == "mean":
        center_df = g[metric_cols].mean()
    elif center == "geometric":
        log_mean, _ = _log_groupby_mean_std(df, metric_cols)
        center_df = np.exp(log_mean)
    else:
        raise ValueError(f"Unknown AGG_CENTER: {center!r}")

    if spread == "range":
        lo_df = g[metric_cols].min().rename(columns={c: f"{c}_lo" for c in metric_cols})
        hi_df = g[metric_cols].max().rename(columns={c: f"{c}_hi" for c in metric_cols})
    elif spread == "std":
        std_df = g[metric_cols].std()
        lo_df = (center_df - std_df).rename(columns={c: f"{c}_lo" for c in metric_cols})
        hi_df = (center_df + std_df).rename(columns={c: f"{c}_hi" for c in metric_cols})
    elif spread == "geometric":
        _, log_std = _log_groupby_mean_std(df, metric_cols)
        gstd_factor = np.exp(log_std)
        lo_df = (center_df / gstd_factor).rename(columns={c: f"{c}_lo" for c in metric_cols})
        hi_df = (center_df * gstd_factor).rename(columns={c: f"{c}_hi" for c in metric_cols})
    else:
        raise ValueError(f"Unknown AGG_SPREAD: {spread!r}")

    n_seeds = g["seed"].nunique().rename("n_seeds")
    agg = center_df.join(lo_df).join(hi_df).join(n_seeds)
    if "windows" in df.columns:
        agg = agg.join(g["windows"].mean().rename("windows"))
    agg = agg.reset_index()
    agg["model"] = pd.Categorical(agg["model"], categories=MODEL_ORDER, ordered=True)
    agg = agg.sort_values(["model", "mu"]).reset_index(drop=True)
    return agg

def _asymmetric_yerr(y, lo, hi):
    y = np.asarray(y, dtype=float)
    lo = np.asarray(lo, dtype=float)
    hi = np.asarray(hi, dtype=float)
    lo = np.where(np.isnan(lo), y, lo)
    hi = np.where(np.isnan(hi), y, hi)
    lower = np.clip(y - lo, a_min=0, a_max=None)
    upper = np.clip(hi - y, a_min=0, a_max=None)
    return np.vstack([lower, upper])


def _errorbar_or_line(ax, x, y, y_lo, y_hi, label, style):
    style = dict(style)
    color = style.pop("color", None)
    marker = style.pop("marker", "o")
    linestyle = style.pop("linestyle", "-")
    has_range = y_lo is not None and y_hi is not None
    yerr = _asymmetric_yerr(y, y_lo, y_hi) if has_range else None
    has_err = yerr is not None and np.isfinite(yerr).any() and (yerr > 0).any()
    if has_err:
        ax.errorbar(x, y, yerr=yerr, label=label, color=color, marker=marker,
                     linestyle=linestyle, linewidth=1.8, markersize=6,
                     capsize=3, elinewidth=1, **style)
    else:
        ax.plot(x, y, label=label, color=color, marker=marker, linestyle=linestyle,
                 linewidth=1.8, markersize=6, **style)
 
 
def make_pivot_tables(agg: pd.DataFrame):
    os.makedirs(TABLE_DIR, exist_ok=True)
    metrics = ["rel_L2", "MSE", "RMSE", "MAE", "max_err", "mean_phys_residual", "train_time_s", "windows"]
    for metric in metrics:
        pivot = agg.pivot_table(index="model", columns="mu", values=metric, observed=True, aggfunc="mean")
        pivot = pivot.reindex(MODEL_ORDER)
        csv_path = os.path.join(TABLE_DIR, f"{metric}_by_model_mu.csv")
        md_path = os.path.join(TABLE_DIR, f"{metric}_by_model_mu.md")
        pivot.to_csv(csv_path)
        with open(md_path, "w") as f:
            f.write(f"# {METRIC_LABELS.get(metric, metric)} by model and mu\n\n")
            f.write(f"Values are the {_agg_desc()} across seeds for models with more than one run "
                    f"per mu ({', '.join(MULTI_SEED_MODELS)}); all other models are single-seed.\n\n")
            f.write(pivot.to_markdown(floatfmt=".4g"))
            f.write("\n")
    print(f"Wrote {len(metrics)} pivot tables to {TABLE_DIR}")
 
 
def make_seed_stats_table(df: pd.DataFrame):
    os.makedirs(TABLE_DIR, exist_ok=True)
    sub = df[df["model"].isin(MULTI_SEED_MODELS)]
    stats = (
        sub.groupby(["model", "mu"], observed=True)["rel_L2"]
        .agg(n_seeds="count", mean="mean", std="std", min="min", max="max")
        .reset_index()
    )
    stats["cv_pct"] = 100 * stats["std"] / stats["mean"]
    stats = stats.sort_values(["model", "mu"])
    csv_path = os.path.join(TABLE_DIR, "rel_L2_seed_stats.csv")
    md_path = os.path.join(TABLE_DIR, "rel_L2_seed_stats.md")
    stats.to_csv(csv_path, index=False)
    with open(md_path, "w") as f:
        f.write("# Relative L2 error: seed robustness (mean/std/min/max across seeds)\n\n")
        f.write("Seeds used: 42, 123, 2026. cv_pct = std / mean * 100.\n\n")
        f.write(stats.to_markdown(index=False, floatfmt=".4g"))
        f.write("\n")
    print(f"Wrote seed robustness table to {csv_path}")
    return stats
 
def write_tidy_csv(df: pd.DataFrame):
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "pinn_results_tidy.csv")
    df.to_csv(path, index=False)
    print(f"Wrote results table to {path}")
 
def _new_fig():
    fig, ax = plt.subplots(figsize=(8, 5.5))
    return fig, ax
 
def plot_metric_vs_mu(agg: pd.DataFrame, metric: str, logy: bool = True, filename: str = None, models=None, title_suffix=""):
    os.makedirs(PLOT_DIR, exist_ok=True)
    models = models or MODEL_ORDER
    lo_col, hi_col = f"{metric}_lo", f"{metric}_hi"
    fig, ax = _new_fig()
    for model in models:
        sub = agg[(agg["model"] == model) & agg[metric].notna()].sort_values("mu")
        if sub.empty:
            continue
        style = MODEL_STYLE.get(model, {})
        y_lo = sub[lo_col].to_numpy() if lo_col in sub.columns else None
        y_hi = sub[hi_col].to_numpy() if hi_col in sub.columns else None
        _errorbar_or_line(ax, sub["mu"], sub[metric], y_lo, y_hi, model, style)
    ax.set_xlabel("mu (nonlinear damping / stiffness)")
    ax.set_ylabel(METRIC_LABELS.get(metric, metric))
    if logy:
        ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_title(f"{METRIC_LABELS.get(metric, metric)} vs mu ({_agg_desc()} across seeds){title_suffix}")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8, loc="best")
    fig.tight_layout()
    filename = filename or f"{metric}_vs_mu.png"
    path = os.path.join(PLOT_DIR, filename)
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Wrote {path}")
 
 
def plot_family_comparison(agg: pd.DataFrame, metric: str, family_models, family: str, logy: bool = True):
    os.makedirs(PLOT_DIR, exist_ok=True)
    lo_col, hi_col = f"{metric}_lo", f"{metric}_hi"
    sub_all = agg[agg["model"].isin(family_models) & agg[metric].notna()]
    if sub_all.empty:
        return
    fig, ax = _new_fig()
    for model in family_models:
        sub = sub_all[sub_all["model"] == model].sort_values("mu")
        if sub.empty:
            continue
        style = MODEL_STYLE.get(model, {})
        y_lo = sub[lo_col].to_numpy() if lo_col in sub.columns else None
        y_hi = sub[hi_col].to_numpy() if hi_col in sub.columns else None
        _errorbar_or_line(ax, sub["mu"], sub[metric], y_lo, y_hi, model, style)
    ax.set_xlabel("mu (nonlinear damping / stiffness)")
    ax.set_ylabel(METRIC_LABELS.get(metric, metric))
    if logy:
        ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_title(f"{family}: non-adaptive vs adaptive — {METRIC_LABELS.get(metric, metric)} ({_agg_desc()} across seeds)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8, loc="best")
    fig.tight_layout()
    fname = f"family_{family.lower()}_{metric}.png"
    path = os.path.join(PLOT_DIR, fname)
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Wrote {path}")
 
 
def plot_accuracy_vs_cost(agg: pd.DataFrame):
    os.makedirs(PLOT_DIR, exist_ok=True)
    fig, ax = _new_fig()
    for model in MODEL_ORDER:
        sub = agg[(agg["model"] == model) & agg["rel_L2"].notna() & agg["train_time_s"].notna()]
        if sub.empty:
            continue
        style = MODEL_STYLE.get(model, {})
        sizes = 25 + 8 * sub["mu"].apply(lambda m: math.log10(m + 1) * 10)
        ax.scatter(sub["train_time_s"], sub["rel_L2"], label=model, color=style.get("color"),
                   marker=style.get("marker", "o"), s=sizes, alpha=0.85, edgecolors="black", linewidths=0.4)
    ax.set_xlabel("Training Time (s)")
    ax.set_ylabel("Relative L2 Error")
    ax.set_yscale("log")
    ax.set_title("Accuracy vs. Computational Cost (seed-averaged)\n(point size grows with mu)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8, loc="best")
    fig.tight_layout()
    path = os.path.join(PLOT_DIR, "accuracy_vs_cost.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Wrote {path}")
 
 
def plot_seed_robustness(df: pd.DataFrame):
    os.makedirs(PLOT_DIR, exist_ok=True)
    fig, axes = plt.subplots(1, len(MULTI_SEED_MODELS), figsize=(7 * len(MULTI_SEED_MODELS), 5.5), sharey=True)
    if len(MULTI_SEED_MODELS) == 1:
        axes = [axes]
    for ax, model in zip(axes, MULTI_SEED_MODELS):
        sub = df[df["model"] == model]
        for seed, sub_seed in sub.groupby("seed"):
            sub_seed = sub_seed.sort_values("mu")
            ax.plot(sub_seed["mu"], sub_seed["rel_L2"], marker="o", linewidth=1.2,
                    color=SEED_COLORS.get(seed, None), alpha=0.6, label=f"seed={seed}")
        mid_stats = (
            sub.groupby("mu", observed=True)["rel_L2"]
            .agg(median="median", lo="min", hi="max")
            .reset_index()
            .sort_values("mu")
        )
        yerr = _asymmetric_yerr(mid_stats["median"], mid_stats["lo"], mid_stats["hi"])
        ax.errorbar(mid_stats["mu"], mid_stats["median"], yerr=yerr, marker="s",
                    linewidth=2.5, linestyle="--", color="black", capsize=4,
                    elinewidth=1.2, label="median (min\u2013max)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("mu")
        ax.set_title(model)
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(fontsize=8, loc="best")
    axes[0].set_ylabel("Relative L2 Error")
    fig.suptitle("Seed robustness: relative L2 error across seeds (42, 123, 2026), black = median (min\u2013max)")
    fig.tight_layout()
    path = os.path.join(PLOT_DIR, "seed_robustness_rel_L2.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Wrote {path}")
 
 
def make_all_plots(df: pd.DataFrame, agg: pd.DataFrame):
    plot_metric_vs_mu(agg, "rel_L2")
    plot_metric_vs_mu(agg, "MSE")
    plot_metric_vs_mu(agg, "train_time_s")
    plot_metric_vs_mu(agg, "mean_phys_residual")
    plot_metric_vs_mu(agg, "windows", logy=False, filename="windows_vs_mu.png")
 
    families = {
        "Vanilla": ["Original PINN", "Window PINN", "Adaptive Window PINN"],
        "SIREN": ["SIREN PINN", "Adaptive SIREN PINN"],
        "Fourier": ["Fourier Feature PINN", "Adaptive Fourier Feature PINN"],
    }
    for family, models in families.items():
        plot_family_comparison(agg, "rel_L2", models, family)
        plot_family_comparison(agg, "train_time_s", models, family, logy=False)
 
    plot_accuracy_vs_cost(agg)
    plot_seed_robustness(df)
 
 
def print_summary(df: pd.DataFrame, agg: pd.DataFrame):
    print("Coverage (distinct mu values per model)")
    coverage = df.groupby("model", observed=True)["mu"].apply(lambda s: sorted(s.unique().tolist()))
    for model in MODEL_ORDER:
        print(f"  {model:32s}: mu = {coverage.get(model, [])}")
 
    print("\nSeed counts per model/mu (only shown where > 1)")
    seed_counts = df.groupby(["model", "mu"], observed=True)["seed"].nunique()
    multi = seed_counts[seed_counts > 1]
    for (model, mu), n in multi.items():
        print(f"  {model:32s} mu={mu:>5}: {n} seeds")
 
    print(f"\nBest relative L2 error per mu (lowest wins, {_agg_desc()} across seeds)")
    common_mus = sorted(agg["mu"].unique())
    for mu in common_mus:
        sub = agg[(agg["mu"] == mu) & agg["rel_L2"].notna()]
        if sub.empty:
            continue
        best = sub.loc[sub["rel_L2"].idxmin()]
        print(f"  mu={mu:>5}: {best['model']:32s} rel_L2={best['rel_L2']:.3e}")
 
 
def main():
    df = build_dataframe()
    agg = build_agg_dataframe(df)
    write_tidy_csv(df)
    make_pivot_tables(agg)
    make_seed_stats_table(df)
    make_all_plots(df, agg)
    print_summary(df, agg)
    print(f"\nAll outputs written under: {OUT_DIR}")
 
 
main()