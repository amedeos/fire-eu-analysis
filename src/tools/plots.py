#!/usr/bin/env python3
"""
Generate analysis plots from ANALYSIS_REGISTRY.csv data.

Creates visualizations for Safe Withdrawal Rate analysis including:
- Success rate comparisons across withdrawal rates, allocations, indices
- Final value distributions
- Risk/return trade-offs
- Depletion year analysis

Supports all equity indices (MSCI World, ACWI, Europe, EMU) and
all withdrawal rates (3%, 3.5%, 4%).
"""

import argparse
import logging
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import seaborn as sns

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Set style for all plots
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("husl")

# Figure size constants
FIGSIZE_WIDE = (14, 6)
FIGSIZE_SQUARE = (10, 8)
FIGSIZE_TALL = (10, 12)
FIGSIZE_GRID_2x2 = (14, 12)
FIGSIZE_GRID_1x3 = (18, 6)

# Consistent color schemes
EQUITY_COLORS = {
    "MSCI World": "#2ecc71",
    "MSCI ACWI": "#3498db",
    "MSCI Europe": "#e74c3c",
    "MSCI EMU": "#9b59b6"
}
EQUITY_MARKERS = {
    "MSCI World": "o",
    "MSCI ACWI": "s",
    "MSCI Europe": "^",
    "MSCI EMU": "D"
}
WR_COLORS = {3.0: "#27ae60", 3.5: "#f39c12", 4.0: "#e74c3c"}
WR_LINESTYLES = {3.0: "-", 3.5: "--", 4.0: ":"}
BOND_COLORS = {"Bund": "#3498db", "BTP": "#e74c3c", "Bund+BTP": "#9b59b6"}

# Standard index order
INDEX_ORDER = ["MSCI World", "MSCI ACWI", "MSCI Europe", "MSCI EMU"]
GLOBAL_INDICES = ["MSCI World", "MSCI ACWI"]
EUROPEAN_INDICES = ["MSCI Europe", "MSCI EMU"]


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load and prepare data from CSV."""
    df = pd.read_csv(csv_path)

    # Exclude STOXX 600 data (03xx notebooks) - different data period
    df = df[df["Equity"] != "STOXX 600"].copy()

    # Extract equity percentage from allocation string
    df["Equity_Pct"] = df["Allocation"].apply(
        lambda x: int(str(x).split("/")[0]) if "/" in str(x) else int(x)
    )

    # Create readable labels
    df["Portfolio"] = df["Equity"] + " + " + df["Bond"].fillna("-")
    df["WR_Label"] = df["WR"].apply(lambda x: f"{x:g}%")

    return df


# =============================================================================
# PLOT 01: Summary Matrix - Key Decision Heatmap
# =============================================================================

def plot_01_success_rate_summary_matrix(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 01: Success Rate Summary Matrix (60/40 Bund portfolios).
    Key decision matrix showing success rates for all indices × all WRs.
    """
    fig, ax = plt.subplots(figsize=(10, 7))

    # Filter to 60/40 Bund allocation
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Summary Matrix plot")
        plt.close()
        return

    # Pivot to create summary table
    pivot = subset.pivot_table(
        index="Equity",
        columns="WR",
        values="Success_Rate",
        aggfunc="mean"
    )

    # Order indices and columns
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])
    pivot = pivot.reindex(columns=sorted(pivot.columns))

    # Create heatmap
    sns.heatmap(
        pivot,
        annot=True,
        fmt=".1f",
        cmap="RdYlGn",
        center=80,
        vmin=55,
        vmax=100,
        ax=ax,
        cbar_kws={"label": "Success Rate (%)"},
        annot_kws={"size": 16, "weight": "bold"},
        linewidths=3,
        linecolor="white",
    )

    ax.set_xlabel("Withdrawal Rate (%)", fontsize=14)
    ax.set_ylabel("Equity Index", fontsize=14)
    ax.set_title("Success Rate Summary: 60/40 Portfolios with Bund\n"
                 "Key Decision Matrix for European Investors",
                 fontsize=16, fontweight="bold")
    ax.set_xticklabels([f"{float(x.get_text()):g}%" for x in ax.get_xticklabels()], fontsize=13)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=13, rotation=0)

    plt.tight_layout()
    plt.savefig(output_dir / "01_success_rate_summary_matrix.png", dpi=150)
    plt.close()
    logger.info("Generated: 01_success_rate_summary_matrix.png")


# =============================================================================
# PLOT 01b: Summary Matrix - Bund+BTP Mix
# =============================================================================

def plot_01b_success_rate_summary_matrix_bundbtp(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 01b: Success Rate Summary Matrix (60/20/20 Bund+BTP portfolios).
    Key decision matrix showing success rates for all indices × all WRs with mixed bonds.
    """
    fig, ax = plt.subplots(figsize=(10, 7))

    # Filter to 60% equity with Bund+BTP allocation
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund+BTP")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Summary Matrix Bund+BTP plot")
        plt.close()
        return

    # Pivot to create summary table
    pivot = subset.pivot_table(
        index="Equity",
        columns="WR",
        values="Success_Rate",
        aggfunc="mean"
    )

    # Order indices and columns
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])
    pivot = pivot.reindex(columns=sorted(pivot.columns))

    # Create heatmap
    sns.heatmap(
        pivot,
        annot=True,
        fmt=".1f",
        cmap="RdYlGn",
        center=80,
        vmin=55,
        vmax=100,
        ax=ax,
        cbar_kws={"label": "Success Rate (%)"},
        annot_kws={"size": 16, "weight": "bold"},
        linewidths=3,
        linecolor="white",
    )

    ax.set_xlabel("Withdrawal Rate (%)", fontsize=14)
    ax.set_ylabel("Equity Index", fontsize=14)
    ax.set_title("Success Rate Summary: 60/20/20 Portfolios with Bund+BTP\n"
                 "Key Decision Matrix for European Investors",
                 fontsize=16, fontweight="bold")
    ax.set_xticklabels([f"{float(x.get_text()):g}%" for x in ax.get_xticklabels()], fontsize=13)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=13, rotation=0)

    plt.tight_layout()
    plt.savefig(output_dir / "01b_success_rate_summary_matrix_bundbtp.png", dpi=150)
    plt.close()
    logger.info("Generated: 01b_success_rate_summary_matrix_bundbtp.png")


# =============================================================================
# PLOT 02: Success Rate vs Withdrawal Rate (All Indices)
# =============================================================================

def plot_02_success_rate_by_wr_all_indices(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 02: Success Rate vs Withdrawal Rate for all indices.
    Line plot showing how success rate degrades as WR increases.
    """
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to 60/40 allocation with Bund
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Success Rate vs WR plot")
        plt.close()
        return

    for equity in INDEX_ORDER:
        eq_data = subset[subset["Equity"] == equity].sort_values("WR")
        if eq_data.empty:
            continue
        ax.plot(eq_data["WR"], eq_data["Success_Rate"],
                marker=EQUITY_MARKERS.get(equity, "o"),
                markersize=12, linewidth=3,
                color=EQUITY_COLORS.get(equity),
                label=equity)

    ax.set_xlabel("Withdrawal Rate (%)", fontsize=13)
    ax.set_ylabel("Success Rate (%)", fontsize=13)
    ax.set_title("Success Rate vs Withdrawal Rate by Equity Index\n"
                 "(60/40 Allocation with German Bund)",
                 fontsize=14, fontweight="bold")
    ax.set_xlim(2.8, 4.2)
    ax.set_ylim(55, 100)
    ax.set_xticks([3.0, 3.5, 4.0])
    ax.set_xticklabels(["3.0%", "3.5%", "4.0%"], fontsize=12)
    ax.legend(loc="lower left", fontsize=12)
    ax.grid(True, alpha=0.3)

    # Add reference lines
    ax.axhline(y=95, color="darkgreen", linestyle=":", alpha=0.6, linewidth=1.5)
    ax.axhline(y=90, color="green", linestyle=":", alpha=0.6, linewidth=1.5)
    ax.axhline(y=80, color="orange", linestyle=":", alpha=0.6, linewidth=1.5)

    # Add annotations for reference lines
    ax.text(4.15, 95, "95%", fontsize=10, color="darkgreen", va="center")
    ax.text(4.15, 90, "90%", fontsize=10, color="green", va="center")
    ax.text(4.15, 80, "80%", fontsize=10, color="orange", va="center")

    plt.tight_layout()
    plt.savefig(output_dir / "02_success_rate_by_wr_all_indices.png", dpi=150)
    plt.close()
    logger.info("Generated: 02_success_rate_by_wr_all_indices.png")


# =============================================================================
# PLOT 03: Success Rate vs Allocation Grid (4 panels)
# =============================================================================

def plot_03_success_rate_by_allocation_grid(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 03: Success Rate vs Equity Allocation for all indices and WRs.
    Grid of 4 panels (one per index) showing allocation sensitivity.
    """
    fig, axes = plt.subplots(2, 2, figsize=FIGSIZE_GRID_2x2)
    axes = axes.flatten()

    for ax, equity in zip(axes, INDEX_ORDER):
        # Filter to this equity index and Bund
        mask = (df["Equity"] == equity) & (df["Bond"] == "Bund")
        subset = df[mask].copy()

        if subset.empty:
            ax.set_title(f"{equity}\n(No data)", fontsize=12)
            ax.set_visible(False)
            continue

        for wr in sorted(subset["WR"].unique()):
            wr_data = subset[subset["WR"] == wr].sort_values("Equity_Pct")
            if wr_data.empty:
                continue
            ax.plot(wr_data["Equity_Pct"], wr_data["Success_Rate"],
                    marker="o", markersize=8, linewidth=2.5,
                    color=WR_COLORS.get(wr, "gray"),
                    linestyle=WR_LINESTYLES.get(wr, "-"),
                    label=f"{wr:g}% WR")

        ax.set_xlabel("Equity Allocation (%)", fontsize=11)
        ax.set_ylabel("Success Rate (%)", fontsize=11)
        ax.set_title(f"{equity} + Bund", fontsize=13, fontweight="bold",
                     color=EQUITY_COLORS.get(equity, "black"))
        ax.set_xlim(55, 105)
        ax.set_ylim(50, 100)
        ax.legend(loc="lower left", fontsize=10)
        ax.grid(True, alpha=0.3)

        # Add reference lines
        ax.axhline(y=90, color="green", linestyle=":", alpha=0.4, linewidth=1)
        ax.axhline(y=80, color="orange", linestyle=":", alpha=0.4, linewidth=1)

    fig.suptitle("Success Rate vs Equity Allocation\n"
                 "Impact of Withdrawal Rate by Equity Index (with Bund)",
                 fontsize=15, fontweight="bold", y=1.02)

    plt.tight_layout()
    plt.savefig(output_dir / "03_success_rate_by_allocation_grid.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 03_success_rate_by_allocation_grid.png")


# =============================================================================
# PLOT 04: Global vs European Comparison
# =============================================================================

def plot_04_global_vs_european_comparison(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 04: Global (World, ACWI) vs European (Europe, EMU) comparison.
    Side-by-side grouped bars + gap analysis.
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Filter to 60/40 Bund allocation
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Global vs European plot")
        plt.close()
        return

    withdrawal_rates = sorted(subset["WR"].unique())

    # Left plot: Grouped bar chart
    ax1 = axes[0]
    x = np.arange(len(withdrawal_rates))
    width = 0.18

    all_indices = GLOBAL_INDICES + EUROPEAN_INDICES
    for i, equity in enumerate(all_indices):
        eq_data = subset[subset["Equity"] == equity].sort_values("WR")
        if eq_data.empty:
            continue
        offset = (i - 1.5) * width
        bars = ax1.bar(x + offset, eq_data["Success_Rate"], width,
                       label=equity, color=EQUITY_COLORS.get(equity))
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                     f"{height:.0f}", ha="center", va="bottom", fontsize=9)

    ax1.set_xlabel("Withdrawal Rate", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("Success Rate: Global vs European Indices\n(60/40 with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels([f"{wr:g}%" for wr in withdrawal_rates], fontsize=11)
    ax1.set_ylim(50, 100)
    ax1.legend(loc="upper right", fontsize=10, ncol=2)
    ax1.grid(True, alpha=0.3, axis="y")

    # Right plot: Gap analysis (Global avg - European avg)
    ax2 = axes[1]

    gaps = []
    global_avgs = []
    european_avgs = []
    for wr in withdrawal_rates:
        wr_data = subset[subset["WR"] == wr]
        global_avg = wr_data[wr_data["Equity"].isin(GLOBAL_INDICES)]["Success_Rate"].mean()
        european_avg = wr_data[wr_data["Equity"].isin(EUROPEAN_INDICES)]["Success_Rate"].mean()
        gaps.append(global_avg - european_avg)
        global_avgs.append(global_avg)
        european_avgs.append(european_avg)

    bar_width = 0.35
    x2 = np.arange(len(withdrawal_rates))

    bars_global = ax2.bar(x2 - bar_width/2, global_avgs, bar_width,
                          label="Global (World+ACWI)", color="#2ecc71", alpha=0.8)
    bars_european = ax2.bar(x2 + bar_width/2, european_avgs, bar_width,
                            label="European (Europe+EMU)", color="#e74c3c", alpha=0.8)

    ax2.set_xlabel("Withdrawal Rate", fontsize=12)
    ax2.set_ylabel("Average Success Rate (%)", fontsize=12)
    ax2.set_title("Global vs European Average\n(Gap in percentage points)",
                  fontsize=13, fontweight="bold")
    ax2.set_xticks(x2)
    ax2.set_xticklabels([f"{wr:g}%" for wr in withdrawal_rates], fontsize=11)
    ax2.set_ylim(50, 100)
    ax2.legend(loc="upper right", fontsize=10)
    ax2.grid(True, alpha=0.3, axis="y")

    # Add gap annotations
    for i, (wr, gap) in enumerate(zip(withdrawal_rates, gaps)):
        y_pos = max(global_avgs[i], european_avgs[i]) + 3
        ax2.annotate(f"Gap: +{gap:.1f}pp", xy=(i, y_pos), ha="center",
                     fontsize=11, fontweight="bold", color="#2c3e50")

    plt.tight_layout()
    plt.savefig(output_dir / "04_global_vs_european_comparison.png", dpi=150)
    plt.close()
    logger.info("Generated: 04_global_vs_european_comparison.png")


# =============================================================================
# PLOT 05: Heatmap Grid by Withdrawal Rate
# =============================================================================

def plot_05_heatmap_grid_by_wr(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 05: Heatmaps of Success Rate for each WR.
    3 panels showing how success rates vary by index and allocation.
    """
    withdrawal_rates = sorted(df["WR"].unique())
    n_wr = len(withdrawal_rates)

    if n_wr == 0:
        logger.warning("No withdrawal rates found for Heatmap Grid plot")
        return

    fig, axes = plt.subplots(1, n_wr, figsize=(7 * n_wr, 7))
    if n_wr == 1:
        axes = [axes]

    for ax, wr in zip(axes, withdrawal_rates):
        # Filter to single-bond portfolios (Bund) for this WR
        mask = (df["WR"] == wr) & (df["Bond"] == "Bund")
        subset = df[mask].copy()

        if subset.empty:
            ax.set_title(f"{wr:g}% WR\n(No data)")
            continue

        # Create pivot: rows = Equity Index, columns = Equity %
        pivot = subset.pivot_table(
            index="Equity", columns="Equity_Pct", values="Success_Rate", aggfunc="mean"
        )

        # Order indices
        pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])

        sns.heatmap(
            pivot,
            annot=True,
            fmt=".1f",
            cmap="RdYlGn",
            center=75,
            vmin=50,
            vmax=100,
            ax=ax,
            cbar_kws={"label": "Success Rate (%)", "shrink": 0.8},
            annot_kws={"size": 11},
            linewidths=1,
            linecolor="white",
        )

        ax.set_xlabel("Equity Allocation (%)", fontsize=12)
        ax.set_ylabel("Equity Index" if ax == axes[0] else "", fontsize=12)
        ax.set_title(f"{wr:g}% Withdrawal Rate", fontsize=14, fontweight="bold")

    fig.suptitle("Success Rate by Equity Index and Allocation\n"
                 "(Portfolios with German Bund)",
                 fontsize=16, fontweight="bold", y=1.03)

    plt.tight_layout()
    plt.savefig(output_dir / "05_heatmap_grid_by_wr.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 05_heatmap_grid_by_wr.png")


# =============================================================================
# PLOT 06: Bond Comparison Grid
# =============================================================================

def plot_06_bond_comparison_grid(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 06: Bond type comparison (Bund vs BTP vs Mix) for all indices.
    Grid of 4 panels showing bond impact at 4% WR.
    """
    fig, axes = plt.subplots(2, 2, figsize=FIGSIZE_GRID_2x2)
    axes = axes.flatten()

    for ax, equity in zip(axes, INDEX_ORDER):
        # Filter to this equity index at 4% WR
        mask = (df["Equity"] == equity) & (df["WR"] == 4.0)
        subset = df[mask].copy()

        if subset.empty:
            ax.set_title(f"{equity}\n(No data)", fontsize=12)
            continue

        # Group by bond type
        for bond in ["Bund", "BTP", "Bund+BTP"]:
            bond_data = subset[subset["Bond"] == bond].sort_values("Equity_Pct")
            if bond_data.empty:
                continue
            ax.plot(bond_data["Equity_Pct"], bond_data["Success_Rate"],
                    marker="o", markersize=8, linewidth=2.5,
                    color=BOND_COLORS.get(bond, "gray"),
                    label=bond)

        ax.set_xlabel("Equity Allocation (%)", fontsize=11)
        ax.set_ylabel("Success Rate (%)", fontsize=11)
        ax.set_title(f"{equity} (4% WR)", fontsize=13, fontweight="bold",
                     color=EQUITY_COLORS.get(equity, "black"))
        ax.set_xlim(55, 105)
        ax.set_ylim(50, 85)
        ax.legend(loc="lower left", fontsize=10)
        ax.grid(True, alpha=0.3)

    fig.suptitle("Success Rate by Bond Type\n"
                 "Bund vs BTP vs Mixed Bond Portfolio (4% WR)",
                 fontsize=15, fontweight="bold", y=1.02)

    plt.tight_layout()
    plt.savefig(output_dir / "06_bond_comparison_grid.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 06_bond_comparison_grid.png")


# =============================================================================
# PLOT 07: Risk/Return Scatter Plot
# =============================================================================

def plot_07_risk_return_scatter(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 07: Risk/Return Trade-off scatter plot.
    Shows all portfolios colored by WR and shaped by equity index.
    """
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)

    # Filter to single-bond portfolios (Bund)
    mask = df["Bond"] == "Bund"
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Risk/Return Scatter plot")
        plt.close()
        return

    # Plot each combination
    for wr in sorted(subset["WR"].unique()):
        for equity in INDEX_ORDER:
            data = subset[(subset["WR"] == wr) & (subset["Equity"] == equity)]
            if data.empty:
                continue
            ax.scatter(
                data["Success_Rate"],
                data["Median_Final"] / 1e6,
                c=WR_COLORS.get(wr, "gray"),
                marker=EQUITY_MARKERS.get(equity, "o"),
                s=120,
                alpha=0.75,
                edgecolors="white",
                linewidth=1,
            )

    # Create custom legend
    wr_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                         markersize=12, label=f"{wr:g}% WR")
                  for wr, c in sorted(WR_COLORS.items())]
    index_handles = [Line2D([0], [0], marker=m, color="gray", markersize=12,
                            linestyle="None", label=eq)
                     for eq, m in EQUITY_MARKERS.items() if eq in INDEX_ORDER]

    legend1 = ax.legend(handles=wr_handles, loc="upper left", fontsize=10,
                        title="Withdrawal Rate", title_fontsize=11)
    ax.add_artist(legend1)
    ax.legend(handles=index_handles, loc="lower right", fontsize=10,
              title="Equity Index", title_fontsize=11)

    ax.set_xlabel("Success Rate (%)", fontsize=13)
    ax.set_ylabel("Median Final Value (€ millions)", fontsize=13)
    ax.set_title("Risk/Return Trade-off: Success Rate vs Final Portfolio Value\n"
                 "(Higher is better on both axes)",
                 fontsize=14, fontweight="bold")
    ax.grid(True, alpha=0.3)

    # Add quadrant reference
    ax.axvline(x=80, color="orange", linestyle=":", alpha=0.5, linewidth=1.5)
    ax.axhline(y=1.0, color="gray", linestyle="--", alpha=0.5, linewidth=1.5)
    ax.text(81, 0.1, "80% threshold", fontsize=9, color="orange", alpha=0.8)
    ax.text(55, 1.05, "Initial €1M", fontsize=9, color="gray", alpha=0.8)

    plt.tight_layout()
    plt.savefig(output_dir / "07_risk_return_scatter.png", dpi=150)
    plt.close()
    logger.info("Generated: 07_risk_return_scatter.png")


# =============================================================================
# PLOT 08: Final Value Distribution
# =============================================================================

def plot_08_final_value_distribution(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 08: Final Value Distribution for all indices (60/40 Bund, 4% WR).
    Shows P5, Median, Mean, P95 ranges.
    """
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to 60/40 Bund at 4% WR
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund") & (df["WR"] == 4.0)
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Final Value Distribution plot")
        plt.close()
        return

    # Order by index
    subset = subset.set_index("Equity").reindex(INDEX_ORDER).dropna().reset_index()

    x = np.arange(len(subset))

    # Convert to millions
    medians = subset["Median_Final"] / 1e6
    means = subset["Mean_Final"] / 1e6
    p5 = subset["P5_Final"] / 1e6
    p95 = subset["P95_Final"] / 1e6

    # Error bar plot
    colors_list = [EQUITY_COLORS.get(eq, "gray") for eq in subset["Equity"]]

    for i, (med, p5_val, p95_val, mean_val, color) in enumerate(zip(medians, p5, p95, means, colors_list)):
        ax.errorbar(
            i, med,
            yerr=[[med - p5_val], [p95_val - med]],
            fmt="o",
            markersize=14,
            capsize=8,
            capthick=2.5,
            color=color,
            ecolor=color,
            elinewidth=2.5,
        )
        ax.scatter(i, mean_val, marker="D", s=100, color=color, zorder=5,
                   edgecolors="white", linewidth=1.5)

    ax.set_xticks(x)
    ax.set_xticklabels(subset["Equity"], fontsize=12)
    ax.set_xlabel("Equity Index", fontsize=13)
    ax.set_ylabel("Final Portfolio Value (€ millions)", fontsize=13)
    ax.set_title("Final Portfolio Value Distribution by Equity Index\n"
                 "(60/40 with Bund, 4% WR | Circle=Median, Diamond=Mean, Bars=P5-P95)",
                 fontsize=14, fontweight="bold")
    ax.grid(True, alpha=0.3)

    # Add horizontal line at initial value
    ax.axhline(y=1.0, color="gray", linestyle="--", alpha=0.6, linewidth=1.5)
    ax.text(len(subset) - 0.5, 1.05, "Initial €1M", fontsize=10, color="gray")

    plt.tight_layout()
    plt.savefig(output_dir / "08_final_value_distribution.png", dpi=150)
    plt.close()
    logger.info("Generated: 08_final_value_distribution.png")


# =============================================================================
# PLOT 09: Depletion Year Analysis
# =============================================================================

def plot_09_depletion_year_analysis(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 09: Depletion Year Analysis across all indices and WRs.
    Shows when portfolios fail (for failed scenarios).
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter data with depletion info
    subset = df[df["Mean_Depletion"].notna()].copy()

    if subset.empty:
        logger.warning("No data for Depletion Year Analysis plot")
        plt.close()
        return

    # Left plot: Median Depletion Year by Index and WR (60/40 Bund)
    ax1 = axes[0]
    mask = (subset["Equity_Pct"] == 60) & (subset["Bond"] == "Bund")
    plot_data = subset[mask].copy()

    if not plot_data.empty:
        withdrawal_rates = sorted(plot_data["WR"].unique())
        x = np.arange(len(INDEX_ORDER))
        width = 0.25

        for i, wr in enumerate(withdrawal_rates):
            wr_data = plot_data[plot_data["WR"] == wr].set_index("Equity")
            values = [wr_data.loc[idx, "Median_Depletion"] if idx in wr_data.index else 0
                      for idx in INDEX_ORDER]
            offset = (i - 1) * width
            bars = ax1.bar(x + offset, values, width, label=f"{wr:g}% WR",
                          color=WR_COLORS.get(wr, "gray"), alpha=0.85)

        ax1.set_xticks(x)
        ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=10)
        ax1.set_xlabel("Equity Index", fontsize=12)
        ax1.set_ylabel("Median Depletion Year", fontsize=12)
        ax1.set_title("Median Depletion Year (Failed Scenarios)\n60/40 with Bund",
                      fontsize=13, fontweight="bold")
        ax1.legend(fontsize=10)
        ax1.set_ylim(20, 28)
        ax1.axhline(y=30, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
        ax1.text(0.1, 29.5, "30-year horizon", fontsize=9, color="green")
        ax1.grid(True, alpha=0.3, axis="y")

    # Right plot: Min Depletion Year (worst case) by Index
    ax2 = axes[1]

    # Get min depletion for 4% WR across allocations
    mask_4pct = (subset["WR"] == 4.0) & (subset["Bond"] == "Bund")
    min_depletion = subset[mask_4pct].groupby("Equity")["Min_Depletion"].min()
    min_depletion = min_depletion.reindex(INDEX_ORDER).dropna()

    if not min_depletion.empty:
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in min_depletion.index]
        bars = ax2.barh(min_depletion.index, min_depletion.values, color=colors, alpha=0.85)

        ax2.set_xlabel("Minimum Depletion Year (Worst Case)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("Earliest Portfolio Depletion (4% WR)\nWorst Case Scenario",
                      fontsize=13, fontweight="bold")
        ax2.set_xlim(0, 15)

        # Add value labels
        for bar, val in zip(bars, min_depletion.values):
            ax2.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                     f"Year {val:.0f}", va="center", fontsize=11, fontweight="bold")

        ax2.grid(True, alpha=0.3, axis="x")

    plt.tight_layout()
    plt.savefig(output_dir / "09_depletion_year_analysis.png", dpi=150)
    plt.close()
    logger.info("Generated: 09_depletion_year_analysis.png")


# =============================================================================
# PLOT 10: Depletion Risk Heatmap (Worst Case)
# =============================================================================

def plot_10_depletion_risk_heatmap(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 10: Depletion Risk Heatmap showing Min Depletion Year.
    Worst case scenario - when do portfolios fail in the most adverse conditions?
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Filter to Bund portfolios with depletion data
    mask = (df["Bond"] == "Bund") & (df["Min_Depletion"].notna())
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Depletion Risk Heatmap")
        plt.close()
        return

    # Left: Min Depletion Year (60/40 allocation)
    ax1 = axes[0]
    mask_60 = subset["Equity_Pct"] == 60
    pivot_min = subset[mask_60].pivot_table(
        index="Equity", columns="WR", values="Min_Depletion", aggfunc="min"
    )
    pivot_min = pivot_min.reindex([i for i in INDEX_ORDER if i in pivot_min.index])

    if not pivot_min.empty:
        sns.heatmap(
            pivot_min,
            annot=True,
            fmt=".0f",
            cmap="RdYlGn",
            center=15,
            vmin=5,
            vmax=25,
            ax=ax1,
            cbar_kws={"label": "Year"},
            annot_kws={"size": 14, "weight": "bold"},
            linewidths=2,
            linecolor="white",
        )
        ax1.set_xlabel("Withdrawal Rate (%)", fontsize=12)
        ax1.set_ylabel("Equity Index", fontsize=12)
        ax1.set_title("Earliest Portfolio Depletion (Worst Case)\n60/40 with Bund",
                      fontsize=13, fontweight="bold")
        ax1.set_xticklabels([f"{float(x.get_text()):g}%" for x in ax1.get_xticklabels()], fontsize=11)

    # Right: Median Depletion Year (60/40 allocation)
    ax2 = axes[1]
    pivot_median = subset[mask_60].pivot_table(
        index="Equity", columns="WR", values="Median_Depletion", aggfunc="median"
    )
    pivot_median = pivot_median.reindex([i for i in INDEX_ORDER if i in pivot_median.index])

    if not pivot_median.empty:
        sns.heatmap(
            pivot_median,
            annot=True,
            fmt=".0f",
            cmap="RdYlGn",
            center=25,
            vmin=20,
            vmax=28,
            ax=ax2,
            cbar_kws={"label": "Year"},
            annot_kws={"size": 14, "weight": "bold"},
            linewidths=2,
            linecolor="white",
        )
        ax2.set_xlabel("Withdrawal Rate (%)", fontsize=12)
        ax2.set_ylabel("", fontsize=12)
        ax2.set_title("Median Depletion Year (Failed Scenarios)\n60/40 with Bund",
                      fontsize=13, fontweight="bold")
        ax2.set_xticklabels([f"{float(x.get_text()):g}%" for x in ax2.get_xticklabels()], fontsize=11)

    fig.suptitle("Depletion Year Risk Analysis: When Do Portfolios Fail?",
                 fontsize=15, fontweight="bold", y=1.02)

    plt.tight_layout()
    plt.savefig(output_dir / "10_depletion_risk_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 10_depletion_risk_heatmap.png")


# =============================================================================
# PLOT 11: Depletion Year vs Allocation
# =============================================================================

def plot_11_depletion_vs_allocation(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 11: How equity allocation affects depletion year.
    Does more equity lead to earlier failures?
    """
    fig, axes = plt.subplots(2, 2, figsize=FIGSIZE_GRID_2x2)
    axes = axes.flatten()

    for ax, equity in zip(axes, INDEX_ORDER):
        # Filter to this equity index and Bund, 4% WR
        mask = (df["Equity"] == equity) & (df["Bond"] == "Bund") & (df["Min_Depletion"].notna())
        subset = df[mask].copy()

        if subset.empty:
            ax.set_title(f"{equity}\n(No data)", fontsize=12)
            continue

        for wr in sorted(subset["WR"].unique()):
            wr_data = subset[subset["WR"] == wr].sort_values("Equity_Pct")
            if wr_data.empty:
                continue

            # Plot Min and Median depletion
            ax.fill_between(wr_data["Equity_Pct"],
                           wr_data["Min_Depletion"],
                           wr_data["Median_Depletion"],
                           alpha=0.2, color=WR_COLORS.get(wr, "gray"))
            ax.plot(wr_data["Equity_Pct"], wr_data["Median_Depletion"],
                    marker="o", markersize=6, linewidth=2,
                    color=WR_COLORS.get(wr, "gray"),
                    label=f"{wr:g}% WR (Median)")
            ax.plot(wr_data["Equity_Pct"], wr_data["Min_Depletion"],
                    marker="v", markersize=5, linewidth=1.5,
                    linestyle="--", color=WR_COLORS.get(wr, "gray"),
                    alpha=0.7)

        ax.set_xlabel("Equity Allocation (%)", fontsize=11)
        ax.set_ylabel("Depletion Year", fontsize=11)
        ax.set_title(f"{equity} + Bund", fontsize=13, fontweight="bold",
                     color=EQUITY_COLORS.get(equity, "black"))
        ax.set_xlim(55, 105)
        ax.set_ylim(5, 30)
        ax.legend(loc="lower left", fontsize=9)
        ax.grid(True, alpha=0.3)

        # Reference line at 30 years
        ax.axhline(y=30, color="green", linestyle=":", alpha=0.5, linewidth=1.5)

    fig.suptitle("Depletion Year vs Equity Allocation\n"
                 "(Solid=Median, Dashed=Min, Shaded=Range)",
                 fontsize=15, fontweight="bold", y=1.02)

    plt.tight_layout()
    plt.savefig(output_dir / "11_depletion_vs_allocation.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 11_depletion_vs_allocation.png")


# =============================================================================
# PLOT 12: Depletion Spread Analysis
# =============================================================================

def plot_12_depletion_spread_analysis(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 12: Spread between Mean and Min depletion year.
    Shows how wide the risk tail is - larger spread = more uncertainty.
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 60/40 Bund with depletion data
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund") & (df["Min_Depletion"].notna())
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Depletion Spread Analysis")
        plt.close()
        return

    # Calculate spread (Median - Min)
    subset["Depletion_Spread"] = subset["Median_Depletion"] - subset["Min_Depletion"]

    # Left: Spread by Index and WR
    ax1 = axes[0]
    pivot_spread = subset.pivot_table(
        index="Equity", columns="WR", values="Depletion_Spread", aggfunc="median"
    )
    pivot_spread = pivot_spread.reindex([i for i in INDEX_ORDER if i in pivot_spread.index])

    if not pivot_spread.empty:
        pivot_spread.plot(kind="bar", ax=ax1, width=0.8,
                          color=[WR_COLORS.get(c, "gray") for c in pivot_spread.columns])
        ax1.set_xlabel("Equity Index", fontsize=12)
        ax1.set_ylabel("Spread (Median - Min Depletion Years)", fontsize=12)
        ax1.set_title("Depletion Year Spread by Index\n(Larger = More Uncertainty)",
                      fontsize=13, fontweight="bold")
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=15, ha="right")
        ax1.legend(title="WR", labels=[f"{wr:g}%" for wr in pivot_spread.columns])
        ax1.grid(True, alpha=0.3, axis="y")

    # Right: Visualization of Min vs Median for 4% WR
    ax2 = axes[1]
    subset_4pct = subset[subset["WR"] == 4.0].set_index("Equity").reindex(INDEX_ORDER).dropna()

    if not subset_4pct.empty:
        x = np.arange(len(subset_4pct))
        width = 0.3

        ax2.bar(x - width/2, subset_4pct["Min_Depletion"], width,
                label="Min (Worst Case)", color="#e74c3c", alpha=0.85)
        ax2.bar(x + width/2, subset_4pct["Median_Depletion"], width,
                label="Median", color="#27ae60", alpha=0.85)

        ax2.set_xticks(x)
        ax2.set_xticklabels(subset_4pct.index, rotation=15, ha="right", fontsize=10)
        ax2.set_xlabel("Equity Index", fontsize=12)
        ax2.set_ylabel("Depletion Year", fontsize=12)
        ax2.set_title("Depletion Year: Min vs Median (4% WR)\n60/40 with Bund",
                      fontsize=13, fontweight="bold")
        ax2.legend(fontsize=10)
        ax2.set_ylim(0, 30)
        ax2.axhline(y=30, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
        ax2.grid(True, alpha=0.3, axis="y")

        # Add value labels
        for i, (min_v, med_v) in enumerate(zip(
                subset_4pct["Min_Depletion"],
                subset_4pct["Median_Depletion"])):
            ax2.text(i - width/2, min_v + 0.5, f"{min_v:.0f}", ha="center", fontsize=10)
            ax2.text(i + width/2, med_v + 0.5, f"{med_v:.0f}", ha="center", fontsize=10)

    plt.tight_layout()
    plt.savefig(output_dir / "12_depletion_spread_analysis.png", dpi=150)
    plt.close()
    logger.info("Generated: 12_depletion_spread_analysis.png")


# =============================================================================
# PLOT 13: Failure Rate vs Depletion Year
# =============================================================================

def plot_13_failure_rate_vs_depletion(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 13: Relationship between failure rate and when failures occur.
    Trade-off: do portfolios that fail more often also fail earlier?
    """
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)

    # Filter to Bund portfolios with depletion data
    mask = (df["Bond"] == "Bund") & (df["Median_Depletion"].notna())
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Failure Rate vs Depletion plot")
        plt.close()
        return

    # Calculate failure rate (100 - Success_Rate)
    subset["Failure_Rate"] = 100 - subset["Success_Rate"]

    # Plot each combination
    for wr in sorted(subset["WR"].unique()):
        for equity in INDEX_ORDER:
            data = subset[(subset["WR"] == wr) & (subset["Equity"] == equity)]
            if data.empty:
                continue
            ax.scatter(
                data["Failure_Rate"],
                data["Median_Depletion"],
                c=WR_COLORS.get(wr, "gray"),
                marker=EQUITY_MARKERS.get(equity, "o"),
                s=100,
                alpha=0.75,
                edgecolors="white",
                linewidth=1,
            )

    # Create custom legend
    wr_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                         markersize=12, label=f"{wr:g}% WR")
                  for wr, c in sorted(WR_COLORS.items())]
    index_handles = [Line2D([0], [0], marker=m, color="gray", markersize=12,
                            linestyle="None", label=eq)
                     for eq, m in EQUITY_MARKERS.items() if eq in INDEX_ORDER]

    legend1 = ax.legend(handles=wr_handles, loc="upper right", fontsize=10,
                        title="Withdrawal Rate", title_fontsize=11)
    ax.add_artist(legend1)
    ax.legend(handles=index_handles, loc="lower left", fontsize=10,
              title="Equity Index", title_fontsize=11)

    ax.set_xlabel("Failure Rate (%)", fontsize=13)
    ax.set_ylabel("Median Depletion Year", fontsize=13)
    ax.set_title("Failure Rate vs Median Depletion Year\n"
                 "Do Higher Failure Rates Mean Earlier Failures?",
                 fontsize=14, fontweight="bold")
    ax.grid(True, alpha=0.3)

    # Add trend indication
    ax.axhline(y=25, color="orange", linestyle=":", alpha=0.5, linewidth=1.5)
    ax.axvline(x=20, color="orange", linestyle=":", alpha=0.5, linewidth=1.5)

    # Annotate quadrants
    ax.text(5, 27, "Low Risk\nLate Failure", fontsize=10, color="green",
            ha="center", style="italic", alpha=0.8)
    ax.text(35, 22, "High Risk\nEarly Failure", fontsize=10, color="red",
            ha="center", style="italic", alpha=0.8)

    plt.tight_layout()
    plt.savefig(output_dir / "13_failure_rate_vs_depletion.png", dpi=150)
    plt.close()
    logger.info("Generated: 13_failure_rate_vs_depletion.png")


# =============================================================================
# PLOT 14: Depletion Global vs European Comparison
# =============================================================================

def plot_14_depletion_global_vs_european(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 14: Depletion year comparison between Global and European indices.
    Do European indices fail earlier than global ones?
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Filter to 60/40 Bund with depletion data
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund") & (df["Min_Depletion"].notna())
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Depletion Global vs European plot")
        plt.close()
        return

    withdrawal_rates = sorted(subset["WR"].unique())

    # Calculate averages for global and european
    results = []
    for wr in withdrawal_rates:
        wr_data = subset[subset["WR"] == wr]
        global_min = wr_data[wr_data["Equity"].isin(GLOBAL_INDICES)]["Min_Depletion"].mean()
        global_median = wr_data[wr_data["Equity"].isin(GLOBAL_INDICES)]["Median_Depletion"].mean()
        european_min = wr_data[wr_data["Equity"].isin(EUROPEAN_INDICES)]["Min_Depletion"].mean()
        european_median = wr_data[wr_data["Equity"].isin(EUROPEAN_INDICES)]["Median_Depletion"].mean()
        results.append({
            "WR": wr,
            "Global_Min": global_min, "Global_Median": global_median,
            "European_Min": european_min, "European_Median": european_median
        })

    results_df = pd.DataFrame(results)

    # Left: Min Depletion Comparison
    ax1 = axes[0]
    x = np.arange(len(withdrawal_rates))
    width = 0.35

    bars1 = ax1.bar(x - width/2, results_df["Global_Min"], width,
                    label="Global (World+ACWI)", color="#2ecc71", alpha=0.85)
    bars2 = ax1.bar(x + width/2, results_df["European_Min"], width,
                    label="European (Europe+EMU)", color="#e74c3c", alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels([f"{wr:g}%" for wr in withdrawal_rates], fontsize=11)
    ax1.set_xlabel("Withdrawal Rate", fontsize=12)
    ax1.set_ylabel("Min Depletion Year", fontsize=12)
    ax1.set_title("Earliest Failure (Worst Case)\n60/40 with Bund",
                  fontsize=13, fontweight="bold")
    ax1.legend(fontsize=10)
    ax1.set_ylim(0, 20)
    ax1.grid(True, alpha=0.3, axis="y")

    # Add value labels
    for bar in bars1:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f"{bar.get_height():.0f}", ha="center", fontsize=10)
    for bar in bars2:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f"{bar.get_height():.0f}", ha="center", fontsize=10)

    # Middle: Median Depletion Comparison
    ax2 = axes[1]
    bars3 = ax2.bar(x - width/2, results_df["Global_Median"], width,
                    label="Global", color="#2ecc71", alpha=0.85)
    bars4 = ax2.bar(x + width/2, results_df["European_Median"], width,
                    label="European", color="#e74c3c", alpha=0.85)

    ax2.set_xticks(x)
    ax2.set_xticklabels([f"{wr:g}%" for wr in withdrawal_rates], fontsize=11)
    ax2.set_xlabel("Withdrawal Rate", fontsize=12)
    ax2.set_ylabel("Median Depletion Year", fontsize=12)
    ax2.set_title("Median Failure Year\n60/40 with Bund",
                  fontsize=13, fontweight="bold")
    ax2.legend(fontsize=10)
    ax2.set_ylim(20, 28)
    ax2.grid(True, alpha=0.3, axis="y")
    ax2.axhline(y=30, color="green", linestyle="--", alpha=0.5, linewidth=1.5)

    # Add value labels
    for bar in bars3:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                 f"{bar.get_height():.1f}", ha="center", fontsize=10)
    for bar in bars4:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                 f"{bar.get_height():.1f}", ha="center", fontsize=10)

    # Right: Gap Analysis (Years earlier for European)
    ax3 = axes[2]
    gap_min = results_df["Global_Min"] - results_df["European_Min"]
    gap_median = results_df["Global_Median"] - results_df["European_Median"]

    ax3.bar(x - width/2, gap_min, width, label="Min Gap", color="#3498db", alpha=0.85)
    ax3.bar(x + width/2, gap_median, width, label="Median Gap", color="#9b59b6", alpha=0.85)

    ax3.set_xticks(x)
    ax3.set_xticklabels([f"{wr:g}%" for wr in withdrawal_rates], fontsize=11)
    ax3.set_xlabel("Withdrawal Rate", fontsize=12)
    ax3.set_ylabel("Gap (Years)", fontsize=12)
    ax3.set_title("How Much Earlier European Fails\n(Positive = Global lasts longer)",
                  fontsize=13, fontweight="bold")
    ax3.legend(fontsize=10)
    ax3.axhline(y=0, color="black", linewidth=1)
    ax3.grid(True, alpha=0.3, axis="y")

    # Add value labels
    for i, (g_min, g_median) in enumerate(zip(gap_min, gap_median)):
        ax3.text(i - width/2, g_min + 0.1, f"+{g_min:.1f}", ha="center", fontsize=10)
        ax3.text(i + width/2, g_median + 0.1, f"+{g_median:.1f}", ha="center", fontsize=10)

    fig.suptitle("Depletion Year: Global vs European Indices",
                 fontsize=16, fontweight="bold", y=1.02)

    plt.tight_layout()
    plt.savefig(output_dir / "14_depletion_global_vs_european.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 14_depletion_global_vs_european.png")


# =============================================================================
# PLOT 15: 4% Rule Reality Check
# =============================================================================

def plot_15_4pct_reality_check(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 15: 4% Rule Reality Check - How does the classic 4% rule perform
    across all indices and allocations in Europe?
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Filter to 4% WR only
    subset = df[df["WR"] == 4.0].copy()

    if subset.empty:
        logger.warning("No 4% WR data available")
        plt.close()
        return

    # Top Left: Success Rate by Index and Allocation (Bund only)
    ax1 = axes[0, 0]
    bund_data = subset[subset["Bond"] == "Bund"]

    allocations = sorted(bund_data["Equity_Pct"].unique())
    x = np.arange(len(INDEX_ORDER))
    width = 0.15

    for i, alloc in enumerate(allocations):
        alloc_data = bund_data[bund_data["Equity_Pct"] == alloc].set_index("Equity")
        values = [alloc_data.loc[idx, "Success_Rate"] if idx in alloc_data.index else 0
                  for idx in INDEX_ORDER]
        offset = (i - len(allocations)/2 + 0.5) * width
        ax1.bar(x + offset, values, width, label=f"{alloc}/{100-alloc}",
                alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("4% Rule: Success Rate by Index & Allocation\n(with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.legend(title="Equity/Bond", fontsize=9, ncol=2)
    ax1.set_ylim(50, 100)
    ax1.axhline(y=95, color="green", linestyle="--", alpha=0.7, linewidth=2)
    ax1.text(0.02, 0.95, "US Historical ~95%", transform=ax1.transAxes,
             fontsize=10, color="green", style="italic")
    ax1.grid(True, alpha=0.3, axis="y")

    # Top Right: Gap from US benchmark (95%)
    ax2 = axes[0, 1]
    # Use 60/40 as reference
    ref_data = bund_data[bund_data["Equity_Pct"] == 60].set_index("Equity")
    ref_data = ref_data.reindex(INDEX_ORDER).dropna()

    if not ref_data.empty:
        gap = 95 - ref_data["Success_Rate"]
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in ref_data.index]
        bars = ax2.barh(ref_data.index, gap, color=colors, alpha=0.85)

        ax2.set_xlabel("Gap from US Historical 95% (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("4% Rule: Gap from US Benchmark\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax2.axvline(x=0, color="green", linewidth=2)

        # Add value labels
        for bar, val in zip(bars, gap):
            x_pos = val + 0.5 if val >= 0 else val - 2
            ax2.text(x_pos, bar.get_y() + bar.get_height()/2,
                     f"-{val:.1f}%" if val > 0 else f"+{-val:.1f}%",
                     va="center", fontsize=11, fontweight="bold")
        ax2.grid(True, alpha=0.3, axis="x")

    # Bottom Left: Best vs Worst allocation for each index
    ax3 = axes[1, 0]
    best_worst = []
    for equity in INDEX_ORDER:
        eq_data = bund_data[bund_data["Equity"] == equity]
        if not eq_data.empty:
            best = eq_data.loc[eq_data["Success_Rate"].idxmax()]
            worst = eq_data.loc[eq_data["Success_Rate"].idxmin()]
            best_worst.append({
                "Equity": equity,
                "Best_Rate": best["Success_Rate"],
                "Best_Alloc": f"{int(best['Equity_Pct'])}/{int(100-best['Equity_Pct'])}",
                "Worst_Rate": worst["Success_Rate"],
                "Worst_Alloc": f"{int(worst['Equity_Pct'])}/{int(100-worst['Equity_Pct'])}"
            })

    if best_worst:
        bw_df = pd.DataFrame(best_worst).set_index("Equity")
        x = np.arange(len(bw_df))
        width = 0.35

        bars1 = ax3.bar(x - width/2, bw_df["Best_Rate"], width,
                        label="Best Allocation", color="#27ae60", alpha=0.85)
        bars2 = ax3.bar(x + width/2, bw_df["Worst_Rate"], width,
                        label="Worst Allocation", color="#e74c3c", alpha=0.85)

        ax3.set_xticks(x)
        ax3.set_xticklabels(bw_df.index, rotation=15, ha="right", fontsize=11)
        ax3.set_xlabel("Equity Index", fontsize=12)
        ax3.set_ylabel("Success Rate (%)", fontsize=12)
        ax3.set_title("4% Rule: Best vs Worst Allocation\n(with Bund)",
                      fontsize=13, fontweight="bold")
        ax3.legend(fontsize=10)
        ax3.set_ylim(50, 100)
        ax3.grid(True, alpha=0.3, axis="y")

        # Add allocation labels
        for i, (bar, alloc) in enumerate(zip(bars1, bw_df["Best_Alloc"])):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                     alloc, ha="center", fontsize=9, fontweight="bold")
        for i, (bar, alloc) in enumerate(zip(bars2, bw_df["Worst_Alloc"])):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                     alloc, ha="center", fontsize=9, fontweight="bold")

    # Bottom Right: Summary table as text
    ax4 = axes[1, 1]
    ax4.axis("off")

    # Create summary statistics
    summary_text = "4% RULE EUROPEAN REALITY CHECK\n"
    summary_text += "=" * 45 + "\n\n"
    summary_text += f"US Historical Success Rate: ~95%\n\n"
    summary_text += "European Results (60/40 with Bund):\n"
    summary_text += "-" * 45 + "\n"

    for equity in INDEX_ORDER:
        eq_data = ref_data.loc[equity] if equity in ref_data.index else None
        if eq_data is not None:
            rate = eq_data["Success_Rate"]
            gap = 95 - rate
            status = "✓" if rate >= 90 else "⚠" if rate >= 80 else "✗"
            summary_text += f"{status} {equity:15} {rate:5.1f}%  (gap: -{gap:.1f}%)\n"

    summary_text += "-" * 45 + "\n"
    avg_rate = ref_data["Success_Rate"].mean() if not ref_data.empty else 0
    summary_text += f"\nAverage European: {avg_rate:.1f}%\n"
    summary_text += f"Gap from US:      -{95-avg_rate:.1f}%\n\n"
    summary_text += "Legend: ✓ ≥90%  ⚠ 80-90%  ✗ <80%"

    ax4.text(0.1, 0.95, summary_text, transform=ax4.transAxes,
             fontsize=12, fontfamily="monospace", verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    fig.suptitle("The 4% Rule in Europe: A Reality Check",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "15_4pct_reality_check.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 15_4pct_reality_check.png")


# =============================================================================
# PLOT 16: 4% Allocation Sensitivity
# =============================================================================

def plot_16_4pct_allocation_sensitivity(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 16: How does success rate at 4% WR change with equity allocation?
    Sensitivity curve from conservative to aggressive.
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 4% WR and Bund
    subset = df[(df["WR"] == 4.0) & (df["Bond"] == "Bund")].copy()

    if subset.empty:
        logger.warning("No 4% WR Bund data available")
        plt.close()
        return

    # Left: Line plot - Success rate vs Equity allocation
    ax1 = axes[0]

    for equity in INDEX_ORDER:
        eq_data = subset[subset["Equity"] == equity].sort_values("Equity_Pct")
        if not eq_data.empty:
            ax1.plot(eq_data["Equity_Pct"], eq_data["Success_Rate"],
                     marker="o", linewidth=2.5, markersize=8,
                     color=EQUITY_COLORS.get(equity, "gray"),
                     label=equity, alpha=0.9)

    ax1.set_xlabel("Equity Allocation (%)", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("4% Rule: Sensitivity to Equity Allocation\n(with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.legend(fontsize=10, loc="lower right")
    ax1.set_xlim(55, 105)
    ax1.set_ylim(60, 100)
    ax1.axhline(y=95, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.axhline(y=80, color="orange", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.text(57, 96, "US Historical", fontsize=9, color="green")
    ax1.text(57, 81, "80% threshold", fontsize=9, color="orange")
    ax1.grid(True, alpha=0.3)

    # Right: Heatmap of success rates
    ax2 = axes[1]
    pivot = subset.pivot_table(
        index="Equity", columns="Equity_Pct", values="Success_Rate"
    )
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])

    if not pivot.empty:
        sns.heatmap(
            pivot,
            annot=True,
            fmt=".1f",
            cmap="RdYlGn",
            center=80,
            vmin=60,
            vmax=95,
            ax=ax2,
            cbar_kws={"label": "Success Rate (%)"},
            annot_kws={"size": 11, "weight": "bold"},
            linewidths=2,
            linecolor="white",
        )
        ax2.set_xlabel("Equity Allocation (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("4% Rule: Success Rate Matrix\n(with Bund)",
                      fontsize=13, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_dir / "16_4pct_allocation_sensitivity.png", dpi=150)
    plt.close()
    logger.info("Generated: 16_4pct_allocation_sensitivity.png")


# =============================================================================
# PLOT 17: 4% Worst Case Scenarios
# =============================================================================

def plot_17_4pct_worst_case(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 17: Worst case scenarios at 4% WR - Focus on low percentiles.
    How bad can it get?
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Filter to 4% WR
    subset = df[df["WR"] == 4.0].copy()

    if subset.empty:
        logger.warning("No 4% WR data available")
        plt.close()
        return

    # Top Left: P5 Final Value by Index (60/40 Bund)
    ax1 = axes[0, 0]
    mask = (subset["Equity_Pct"] == 60) & (subset["Bond"] == "Bund")
    data_60 = subset[mask].set_index("Equity").reindex(INDEX_ORDER).dropna()

    if not data_60.empty:
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in data_60.index]
        bars = ax1.barh(data_60.index, data_60["P5_Final"] / 1000, color=colors, alpha=0.85)

        ax1.set_xlabel("5th Percentile Final Value (€ thousands)", fontsize=12)
        ax1.set_ylabel("Equity Index", fontsize=12)
        ax1.set_title("4% Rule: Worst 5% Outcomes\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax1.axvline(x=0, color="red", linewidth=2, linestyle="--")
        ax1.text(5, -0.3, "Portfolio depleted", fontsize=9, color="red")

        # Add value labels
        for bar, val in zip(bars, data_60["P5_Final"]):
            label = f"€{val/1000:,.0f}k" if val > 0 else "Depleted"
            ax1.text(max(val/1000, 0) + 10, bar.get_y() + bar.get_height()/2,
                     label, va="center", fontsize=10, fontweight="bold")
        ax1.grid(True, alpha=0.3, axis="x")
        ax1.set_xlim(-50, max(data_60["P5_Final"]/1000) * 1.3)

    # Top Right: Failed simulations percentage
    ax2 = axes[0, 1]
    if not data_60.empty and "Failed_Pct" in data_60.columns:
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in data_60.index]
        bars = ax2.barh(data_60.index, data_60["Failed_Pct"], color=colors, alpha=0.85)

        ax2.set_xlabel("Portfolio Failure Rate (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("4% Rule: Failure Rate\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax2.axvline(x=5, color="green", linewidth=1.5, linestyle="--", alpha=0.7)
        ax2.text(6, -0.3, "US Historical ~5%", fontsize=9, color="green")

        # Add value labels
        for bar, val in zip(bars, data_60["Failed_Pct"]):
            ax2.text(val + 0.5, bar.get_y() + bar.get_height()/2,
                     f"{val:.1f}%", va="center", fontsize=11, fontweight="bold")
        ax2.grid(True, alpha=0.3, axis="x")

    # Bottom Left: Min Depletion Year (earliest failure)
    ax3 = axes[1, 0]
    if not data_60.empty and "Min_Depletion" in data_60.columns:
        min_dep = data_60["Min_Depletion"].dropna()
        if not min_dep.empty:
            colors = [EQUITY_COLORS.get(eq, "gray") for eq in min_dep.index]
            bars = ax3.barh(min_dep.index, min_dep.values, color=colors, alpha=0.85)

            ax3.set_xlabel("Earliest Depletion Year", fontsize=12)
            ax3.set_ylabel("Equity Index", fontsize=12)
            ax3.set_title("4% Rule: Earliest Failure (Worst Case)\n(60/40 with Bund)",
                          fontsize=13, fontweight="bold")
            ax3.set_xlim(0, 20)
            ax3.axvline(x=10, color="red", linewidth=1.5, linestyle="--", alpha=0.7)
            ax3.text(10.5, -0.3, "10-year mark", fontsize=9, color="red")

            # Add value labels
            for bar, val in zip(bars, min_dep.values):
                ax3.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                         f"Year {val:.0f}", va="center", fontsize=11, fontweight="bold")
            ax3.grid(True, alpha=0.3, axis="x")

    # Bottom Right: Comparison of P5, Median, P95 for 60/40
    ax4 = axes[1, 1]
    if not data_60.empty:
        x = np.arange(len(data_60))
        width = 0.25

        p5 = data_60["P5_Final"] / 1_000_000
        median = data_60["Median_Final"] / 1_000_000
        p95 = data_60["P95_Final"] / 1_000_000

        ax4.bar(x - width, p5, width, label="P5 (Worst 5%)", color="#e74c3c", alpha=0.85)
        ax4.bar(x, median, width, label="Median", color="#f39c12", alpha=0.85)
        ax4.bar(x + width, p95, width, label="P95 (Best 5%)", color="#27ae60", alpha=0.85)

        ax4.set_xticks(x)
        ax4.set_xticklabels(data_60.index, rotation=15, ha="right", fontsize=10)
        ax4.set_xlabel("Equity Index", fontsize=12)
        ax4.set_ylabel("Final Portfolio Value (€ millions)", fontsize=12)
        ax4.set_title("4% Rule: Range of Outcomes\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax4.legend(fontsize=10)
        ax4.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5)
        ax4.text(0.02, 1.05, "Initial €1M", fontsize=9, color="gray")
        ax4.grid(True, alpha=0.3, axis="y")

    fig.suptitle("4% Rule: Worst Case Scenario Analysis",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "17_4pct_worst_case.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 17_4pct_worst_case.png")


# =============================================================================
# PLOT 18: 4% Depletion Timeline
# =============================================================================

def plot_18_4pct_depletion_timeline(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 18: When do portfolios fail at 4%? Distribution of depletion years.
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 4% WR with depletion data
    subset = df[(df["WR"] == 4.0) & (df["Min_Depletion"].notna())].copy()

    if subset.empty:
        logger.warning("No 4% WR depletion data available")
        plt.close()
        return

    # Left: Min vs Median Depletion by Index (60/40 Bund)
    ax1 = axes[0]
    mask = (subset["Equity_Pct"] == 60) & (subset["Bond"] == "Bund")
    data_60 = subset[mask].set_index("Equity").reindex(INDEX_ORDER).dropna()

    if not data_60.empty:
        x = np.arange(len(data_60))
        width = 0.35

        bars1 = ax1.bar(x - width/2, data_60["Min_Depletion"], width,
                        label="Earliest Failure", color="#e74c3c", alpha=0.85)
        bars2 = ax1.bar(x + width/2, data_60["Median_Depletion"], width,
                        label="Median Failure", color="#3498db", alpha=0.85)

        ax1.set_xticks(x)
        ax1.set_xticklabels(data_60.index, rotation=15, ha="right", fontsize=11)
        ax1.set_xlabel("Equity Index", fontsize=12)
        ax1.set_ylabel("Depletion Year", fontsize=12)
        ax1.set_title("4% Rule: When Portfolios Fail\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax1.legend(fontsize=10)
        ax1.set_ylim(0, 32)
        ax1.axhline(y=30, color="green", linestyle="--", alpha=0.7, linewidth=2)
        ax1.text(0.02, 0.97, "30-year horizon", transform=ax1.transAxes,
                 fontsize=9, color="green")
        ax1.grid(True, alpha=0.3, axis="y")

        # Add value labels
        for bar in bars1:
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                     f"{bar.get_height():.0f}", ha="center", fontsize=10)
        for bar in bars2:
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                     f"{bar.get_height():.0f}", ha="center", fontsize=10)

    # Right: Depletion timeline across allocations
    ax2 = axes[1]
    bund_data = subset[subset["Bond"] == "Bund"]

    for equity in INDEX_ORDER:
        eq_data = bund_data[bund_data["Equity"] == equity].sort_values("Equity_Pct")
        if not eq_data.empty:
            ax2.plot(eq_data["Equity_Pct"], eq_data["Median_Depletion"],
                     marker="o", linewidth=2.5, markersize=8,
                     color=EQUITY_COLORS.get(equity, "gray"),
                     label=equity, alpha=0.9)

    ax2.set_xlabel("Equity Allocation (%)", fontsize=12)
    ax2.set_ylabel("Median Depletion Year", fontsize=12)
    ax2.set_title("4% Rule: Median Failure Year by Allocation\n(with Bund)",
                  fontsize=13, fontweight="bold")
    ax2.legend(fontsize=10)
    ax2.set_xlim(55, 105)
    ax2.set_ylim(22, 28)
    ax2.axhline(y=30, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "18_4pct_depletion_timeline.png", dpi=150)
    plt.close()
    logger.info("Generated: 18_4pct_depletion_timeline.png")


# =============================================================================
# PLOT 19: 4% Bond Impact
# =============================================================================

def plot_19_4pct_bond_impact(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 19: How do different bonds affect 4% success rate?
    Bund vs BTP vs Mix comparison.
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 4% WR and 60/40
    subset = df[(df["WR"] == 4.0) & (df["Equity_Pct"] == 60)].copy()

    if subset.empty:
        logger.warning("No 4% WR 60/40 data available")
        plt.close()
        return

    bond_types = subset["Bond"].unique()

    # Define bond colors
    bond_colors = {
        "Bund": "#3498db",
        "BTP": "#e74c3c",
        "Bund/BTP": "#9b59b6",
        "OAT": "#f39c12",
    }

    # Left: Success Rate by Index and Bond Type
    ax1 = axes[0]
    x = np.arange(len(INDEX_ORDER))
    width = 0.2

    for i, bond in enumerate(sorted(bond_types)):
        bond_data = subset[subset["Bond"] == bond].set_index("Equity")
        values = [bond_data.loc[idx, "Success_Rate"] if idx in bond_data.index else 0
                  for idx in INDEX_ORDER]
        offset = (i - len(bond_types)/2 + 0.5) * width
        ax1.bar(x + offset, values, width, label=bond,
                color=bond_colors.get(bond, "gray"), alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("4% Rule: Bond Type Impact\n(60/40 Allocation)",
                  fontsize=13, fontweight="bold")
    ax1.legend(title="Bond Type", fontsize=10)
    ax1.set_ylim(60, 95)
    ax1.grid(True, alpha=0.3, axis="y")

    # Right: Heatmap of success rates
    ax2 = axes[1]
    pivot = subset.pivot_table(
        index="Equity", columns="Bond", values="Success_Rate"
    )
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])

    if not pivot.empty:
        sns.heatmap(
            pivot,
            annot=True,
            fmt=".1f",
            cmap="RdYlGn",
            center=80,
            vmin=65,
            vmax=90,
            ax=ax2,
            cbar_kws={"label": "Success Rate (%)"},
            annot_kws={"size": 12, "weight": "bold"},
            linewidths=2,
            linecolor="white",
        )
        ax2.set_xlabel("Bond Type", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("4% Rule: Bond Impact Matrix\n(60/40 Allocation)",
                      fontsize=13, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_dir / "19_4pct_bond_impact.png", dpi=150)
    plt.close()
    logger.info("Generated: 19_4pct_bond_impact.png")


# =============================================================================
# PLOT 20: 4% Global vs European Gap
# =============================================================================

def plot_20_4pct_global_vs_european_gap(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 20: Quantify the "cost" of investing only in Europe at 4%.
    Global indices vs European indices direct comparison.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Filter to 4% WR and 60/40 Bund
    subset = df[(df["WR"] == 4.0) & (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")].copy()

    if subset.empty:
        logger.warning("No 4% WR 60/40 Bund data available")
        plt.close()
        return

    # Categorize indices
    subset["Category"] = subset["Equity"].apply(
        lambda x: "Global" if x in GLOBAL_INDICES else "European"
    )

    # Top Left: Success Rate Comparison
    ax1 = axes[0, 0]
    global_data = subset[subset["Category"] == "Global"]["Success_Rate"]
    european_data = subset[subset["Category"] == "European"]["Success_Rate"]

    categories = ["Global\n(World, ACWI)", "European\n(Europe, EMU)"]
    means = [global_data.mean() if not global_data.empty else 0,
             european_data.mean() if not european_data.empty else 0]
    colors = ["#27ae60", "#e74c3c"]

    bars = ax1.bar(categories, means, color=colors, alpha=0.85, width=0.6)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("4% Rule: Global vs European\nAverage Success Rate",
                  fontsize=13, fontweight="bold")
    ax1.set_ylim(60, 90)
    ax1.axhline(y=95, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.text(0.02, 0.95, "US Historical ~95%", transform=ax1.transAxes,
             fontsize=9, color="green")

    # Add value labels and gap
    for bar, val in zip(bars, means):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{val:.1f}%", ha="center", fontsize=14, fontweight="bold")

    gap = means[0] - means[1]
    ax1.annotate("", xy=(1, means[1]), xytext=(1, means[0]),
                 arrowprops=dict(arrowstyle="<->", color="black", lw=2))
    ax1.text(1.15, (means[0] + means[1])/2, f"Gap:\n{gap:.1f}%",
             fontsize=11, fontweight="bold", va="center")
    ax1.grid(True, alpha=0.3, axis="y")

    # Top Right: Individual Index Comparison
    ax2 = axes[0, 1]
    data_plot = subset.set_index("Equity").reindex(INDEX_ORDER).dropna()

    if not data_plot.empty:
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in data_plot.index]
        bars = ax2.barh(data_plot.index, data_plot["Success_Rate"], color=colors, alpha=0.85)

        ax2.set_xlabel("Success Rate (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("4% Rule: Individual Index Performance\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax2.set_xlim(60, 90)

        # Add category separator
        ax2.axhline(y=1.5, color="black", linestyle="-", linewidth=2, alpha=0.5)
        ax2.text(61, 2.7, "GLOBAL", fontsize=10, fontweight="bold", alpha=0.7)
        ax2.text(61, 0.3, "EUROPEAN", fontsize=10, fontweight="bold", alpha=0.7)

        # Add value labels
        for bar, val in zip(bars, data_plot["Success_Rate"]):
            ax2.text(val + 0.5, bar.get_y() + bar.get_height()/2,
                     f"{val:.1f}%", va="center", fontsize=11, fontweight="bold")
        ax2.grid(True, alpha=0.3, axis="x")

    # Bottom Left: Median Final Value Comparison
    ax3 = axes[1, 0]
    if not data_plot.empty:
        x = np.arange(len(data_plot))
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in data_plot.index]
        bars = ax3.bar(x, data_plot["Median_Final"] / 1_000_000, color=colors, alpha=0.85)

        ax3.set_xticks(x)
        ax3.set_xticklabels(data_plot.index, rotation=15, ha="right", fontsize=11)
        ax3.set_xlabel("Equity Index", fontsize=12)
        ax3.set_ylabel("Median Final Value (€ millions)", fontsize=12)
        ax3.set_title("4% Rule: Median Final Portfolio Value\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax3.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5, linewidth=1.5)
        ax3.text(0.02, 1.05, "Initial €1M", fontsize=9, color="gray")

        # Add value labels
        for bar in bars:
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                     f"€{bar.get_height():.2f}M", ha="center", fontsize=10, fontweight="bold")
        ax3.grid(True, alpha=0.3, axis="y")

    # Bottom Right: Summary - Cost of European Investing
    ax4 = axes[1, 1]
    ax4.axis("off")

    # Calculate costs
    global_sr = global_data.mean() if not global_data.empty else 0
    european_sr = european_data.mean() if not european_data.empty else 0
    sr_cost = global_sr - european_sr

    global_med = subset[subset["Category"] == "Global"]["Median_Final"].mean()
    european_med = subset[subset["Category"] == "European"]["Median_Final"].mean()
    med_cost = (global_med - european_med) / 1000

    summary_text = "THE COST OF EUROPEAN-ONLY INVESTING\n"
    summary_text += "AT 4% WITHDRAWAL RATE (60/40 with Bund)\n"
    summary_text += "=" * 50 + "\n\n"

    summary_text += "SUCCESS RATE:\n"
    summary_text += f"  Global Average:    {global_sr:.1f}%\n"
    summary_text += f"  European Average:  {european_sr:.1f}%\n"
    summary_text += f"  Cost:              -{sr_cost:.1f} percentage points\n\n"

    summary_text += "MEDIAN FINAL VALUE:\n"
    summary_text += f"  Global Average:    €{global_med/1_000_000:.2f}M\n"
    summary_text += f"  European Average:  €{european_med/1_000_000:.2f}M\n"
    summary_text += f"  Cost:              -€{med_cost:.0f}k\n\n"

    summary_text += "-" * 50 + "\n"
    summary_text += "INTERPRETATION:\n"
    summary_text += f"Investing in European-only indices at 4% WR\n"
    summary_text += f"reduces success probability by ~{sr_cost:.0f}%\n"
    summary_text += f"and median wealth by ~€{med_cost:.0f}k.\n\n"
    summary_text += "Global diversification provides meaningful\n"
    summary_text += "improvements for European investors."

    ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
             fontsize=11, fontfamily="monospace", verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))

    fig.suptitle("4% Rule: The Cost of Home Bias",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "20_4pct_global_vs_european_gap.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 20_4pct_global_vs_european_gap.png")


# =============================================================================
# PLOT 21: 3% Safety Analysis
# =============================================================================

def plot_21_3pct_safety_analysis(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 21: 3% WR Safety Analysis - How safe is the conservative approach?
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Filter to 3% WR only
    subset = df[df["WR"] == 3.0].copy()

    if subset.empty:
        logger.warning("No 3% WR data available")
        plt.close()
        return

    # Top Left: Success Rate by Index and Allocation (Bund only)
    ax1 = axes[0, 0]
    bund_data = subset[subset["Bond"] == "Bund"]

    allocations = sorted(bund_data["Equity_Pct"].unique())
    x = np.arange(len(INDEX_ORDER))
    width = 0.15

    for i, alloc in enumerate(allocations):
        alloc_data = bund_data[bund_data["Equity_Pct"] == alloc].set_index("Equity")
        values = [alloc_data.loc[idx, "Success_Rate"] if idx in alloc_data.index else 0
                  for idx in INDEX_ORDER]
        offset = (i - len(allocations)/2 + 0.5) * width
        ax1.bar(x + offset, values, width, label=f"{alloc}/{100-alloc}", alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("3% Rule: Success Rate by Index & Allocation\n(with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.legend(title="Equity/Bond", fontsize=9, ncol=2)
    ax1.set_ylim(85, 100)
    ax1.axhline(y=95, color="green", linestyle="--", alpha=0.7, linewidth=2)
    ax1.text(0.02, 0.92, "95% target", transform=ax1.transAxes,
             fontsize=10, color="green", style="italic")
    ax1.grid(True, alpha=0.3, axis="y")

    # Top Right: All indices above 95%?
    ax2 = axes[0, 1]
    ref_data = bund_data[bund_data["Equity_Pct"] == 60].set_index("Equity")
    ref_data = ref_data.reindex(INDEX_ORDER).dropna()

    if not ref_data.empty:
        colors = ["#27ae60" if sr >= 95 else "#f39c12" if sr >= 90 else "#e74c3c"
                  for sr in ref_data["Success_Rate"]]
        bars = ax2.barh(ref_data.index, ref_data["Success_Rate"], color=colors, alpha=0.85)

        ax2.set_xlabel("Success Rate (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3% Rule: Safety Check\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax2.axvline(x=95, color="green", linewidth=2, linestyle="--")
        ax2.set_xlim(85, 100)

        # Add value labels
        for bar, val in zip(bars, ref_data["Success_Rate"]):
            status = "✓" if val >= 95 else "⚠"
            ax2.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                     f"{val:.1f}% {status}", va="center", fontsize=11, fontweight="bold")
        ax2.grid(True, alpha=0.3, axis="x")

    # Bottom Left: Comparison 3% vs 4% success rate
    ax3 = axes[1, 0]
    df_4pct = df[(df["WR"] == 4.0) & (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")]
    df_4pct = df_4pct.set_index("Equity").reindex(INDEX_ORDER)

    if not ref_data.empty:
        x = np.arange(len(INDEX_ORDER))
        width = 0.35

        sr_3pct = [ref_data.loc[idx, "Success_Rate"] if idx in ref_data.index else 0
                   for idx in INDEX_ORDER]
        sr_4pct = [df_4pct.loc[idx, "Success_Rate"] if idx in df_4pct.index else 0
                   for idx in INDEX_ORDER]

        ax3.bar(x - width/2, sr_3pct, width, label="3% WR", color="#27ae60", alpha=0.85)
        ax3.bar(x + width/2, sr_4pct, width, label="4% WR", color="#e74c3c", alpha=0.85)

        ax3.set_xticks(x)
        ax3.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
        ax3.set_xlabel("Equity Index", fontsize=12)
        ax3.set_ylabel("Success Rate (%)", fontsize=12)
        ax3.set_title("3% vs 4%: Safety Improvement\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax3.legend(fontsize=10)
        ax3.set_ylim(60, 100)
        ax3.grid(True, alpha=0.3, axis="y")

        # Add improvement labels
        for i, (s3, s4) in enumerate(zip(sr_3pct, sr_4pct)):
            if s3 > 0 and s4 > 0:
                ax3.text(i, max(s3, s4) + 1, f"+{s3-s4:.0f}%",
                         ha="center", fontsize=9, color="green", fontweight="bold")

    # Bottom Right: Summary
    ax4 = axes[1, 1]
    ax4.axis("off")

    summary_text = "3% WITHDRAWAL RATE: SAFETY ANALYSIS\n"
    summary_text += "=" * 45 + "\n\n"

    if not ref_data.empty:
        above_95 = (ref_data["Success_Rate"] >= 95).sum()
        above_90 = (ref_data["Success_Rate"] >= 90).sum()
        avg_rate = ref_data["Success_Rate"].mean()

        summary_text += f"60/40 with Bund Results:\n"
        summary_text += "-" * 45 + "\n"
        summary_text += f"Indices with ≥95% success: {above_95}/{len(ref_data)}\n"
        summary_text += f"Indices with ≥90% success: {above_90}/{len(ref_data)}\n"
        summary_text += f"Average success rate:      {avg_rate:.1f}%\n\n"

        summary_text += "Individual Results:\n"
        for equity in INDEX_ORDER:
            if equity in ref_data.index:
                rate = ref_data.loc[equity, "Success_Rate"]
                status = "✓ SAFE" if rate >= 95 else "⚠ MARGINAL" if rate >= 90 else "✗ RISKY"
                summary_text += f"  {equity:15} {rate:5.1f}%  {status}\n"

    summary_text += "\n" + "-" * 45 + "\n"
    summary_text += "CONCLUSION:\n"
    summary_text += "3% WR provides significantly higher safety\n"
    summary_text += "margins for European investors compared to 4%."

    ax4.text(0.1, 0.95, summary_text, transform=ax4.transAxes,
             fontsize=11, fontfamily="monospace", verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.3))

    fig.suptitle("The 3% Rule: A Safer Approach for Europe",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "21_3pct_safety_analysis.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 21_3pct_safety_analysis.png")


# =============================================================================
# PLOT 22: 3% Allocation Sensitivity
# =============================================================================

def plot_22_3pct_allocation_sensitivity(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 22: How does success rate at 3% WR change with equity allocation?
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 3% WR and Bund
    subset = df[(df["WR"] == 3.0) & (df["Bond"] == "Bund")].copy()

    if subset.empty:
        logger.warning("No 3% WR Bund data available")
        plt.close()
        return

    # Left: Line plot - Success rate vs Equity allocation
    ax1 = axes[0]

    for equity in INDEX_ORDER:
        eq_data = subset[subset["Equity"] == equity].sort_values("Equity_Pct")
        if not eq_data.empty:
            ax1.plot(eq_data["Equity_Pct"], eq_data["Success_Rate"],
                     marker="o", linewidth=2.5, markersize=8,
                     color=EQUITY_COLORS.get(equity, "gray"),
                     label=equity, alpha=0.9)

    ax1.set_xlabel("Equity Allocation (%)", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("3% Rule: Sensitivity to Equity Allocation\n(with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.legend(fontsize=10, loc="lower right")
    ax1.set_xlim(55, 105)
    ax1.set_ylim(88, 100)
    ax1.axhline(y=95, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.text(57, 95.5, "95% target", fontsize=9, color="green")
    ax1.grid(True, alpha=0.3)

    # Right: Heatmap of success rates
    ax2 = axes[1]
    pivot = subset.pivot_table(
        index="Equity", columns="Equity_Pct", values="Success_Rate"
    )
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])

    if not pivot.empty:
        sns.heatmap(
            pivot,
            annot=True,
            fmt=".1f",
            cmap="RdYlGn",
            center=95,
            vmin=88,
            vmax=100,
            ax=ax2,
            cbar_kws={"label": "Success Rate (%)"},
            annot_kws={"size": 11, "weight": "bold"},
            linewidths=2,
            linecolor="white",
        )
        ax2.set_xlabel("Equity Allocation (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3% Rule: Success Rate Matrix\n(with Bund)",
                      fontsize=13, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_dir / "22_3pct_allocation_sensitivity.png", dpi=150)
    plt.close()
    logger.info("Generated: 22_3pct_allocation_sensitivity.png")


# =============================================================================
# PLOT 23: 3% Final Value Trade-off
# =============================================================================

def plot_23_3pct_final_value_tradeoff(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 23: What do you give up in final value with 3% vs 4%?
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter data
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No 60/40 Bund data available")
        plt.close()
        return

    # Left: Median Final Value 3% vs 4%
    ax1 = axes[0]
    data_3pct = subset[subset["WR"] == 3.0].set_index("Equity").reindex(INDEX_ORDER)
    data_4pct = subset[subset["WR"] == 4.0].set_index("Equity").reindex(INDEX_ORDER)

    x = np.arange(len(INDEX_ORDER))
    width = 0.35

    med_3 = [data_3pct.loc[idx, "Median_Final"]/1_000_000 if idx in data_3pct.index else 0
             for idx in INDEX_ORDER]
    med_4 = [data_4pct.loc[idx, "Median_Final"]/1_000_000 if idx in data_4pct.index else 0
             for idx in INDEX_ORDER]

    ax1.bar(x - width/2, med_3, width, label="3% WR", color="#27ae60", alpha=0.85)
    ax1.bar(x + width/2, med_4, width, label="4% WR", color="#e74c3c", alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Median Final Value (€ millions)", fontsize=12)
    ax1.set_title("3% vs 4%: Median Final Portfolio Value\n(60/40 with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.legend(fontsize=10)
    ax1.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5)
    ax1.grid(True, alpha=0.3, axis="y")

    # Right: Extra wealth from lower withdrawal
    ax2 = axes[1]
    extra_wealth = [(m3 - m4) for m3, m4 in zip(med_3, med_4)]
    colors = [EQUITY_COLORS.get(eq, "gray") for eq in INDEX_ORDER]

    bars = ax2.barh(INDEX_ORDER, extra_wealth, color=colors, alpha=0.85)

    ax2.set_xlabel("Extra Final Value with 3% vs 4% (€ millions)", fontsize=12)
    ax2.set_ylabel("Equity Index", fontsize=12)
    ax2.set_title("The Price of Safety: Extra Wealth at 3%\n(60/40 with Bund)",
                  fontsize=13, fontweight="bold")

    # Add value labels
    for bar, val in zip(bars, extra_wealth):
        ax2.text(val + 0.02, bar.get_y() + bar.get_height()/2,
                 f"+€{val:.2f}M", va="center", fontsize=11, fontweight="bold")
    ax2.grid(True, alpha=0.3, axis="x")

    plt.tight_layout()
    plt.savefig(output_dir / "23_3pct_final_value_tradeoff.png", dpi=150)
    plt.close()
    logger.info("Generated: 23_3pct_final_value_tradeoff.png")


# =============================================================================
# PLOT 24: 3% Bond Impact
# =============================================================================

def plot_24_3pct_bond_impact(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 24: How do different bonds affect 3% success rate?
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 3% WR and 60/40
    subset = df[(df["WR"] == 3.0) & (df["Equity_Pct"] == 60)].copy()

    if subset.empty:
        logger.warning("No 3% WR 60/40 data available")
        plt.close()
        return

    bond_types = subset["Bond"].unique()
    bond_colors = {"Bund": "#3498db", "BTP": "#e74c3c", "Bund/BTP": "#9b59b6", "OAT": "#f39c12"}

    # Left: Success Rate by Index and Bond Type
    ax1 = axes[0]
    x = np.arange(len(INDEX_ORDER))
    width = 0.2

    for i, bond in enumerate(sorted(bond_types)):
        bond_data = subset[subset["Bond"] == bond].set_index("Equity")
        values = [bond_data.loc[idx, "Success_Rate"] if idx in bond_data.index else 0
                  for idx in INDEX_ORDER]
        offset = (i - len(bond_types)/2 + 0.5) * width
        ax1.bar(x + offset, values, width, label=bond,
                color=bond_colors.get(bond, "gray"), alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("3% Rule: Bond Type Impact\n(60/40 Allocation)",
                  fontsize=13, fontweight="bold")
    ax1.legend(title="Bond Type", fontsize=10)
    ax1.set_ylim(85, 100)
    ax1.axhline(y=95, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.grid(True, alpha=0.3, axis="y")

    # Right: Heatmap of success rates
    ax2 = axes[1]
    pivot = subset.pivot_table(index="Equity", columns="Bond", values="Success_Rate")
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])

    if not pivot.empty:
        sns.heatmap(
            pivot, annot=True, fmt=".1f", cmap="RdYlGn", center=95,
            vmin=88, vmax=100, ax=ax2, cbar_kws={"label": "Success Rate (%)"},
            annot_kws={"size": 12, "weight": "bold"}, linewidths=2, linecolor="white",
        )
        ax2.set_xlabel("Bond Type", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3% Rule: Bond Impact Matrix\n(60/40 Allocation)",
                      fontsize=13, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_dir / "24_3pct_bond_impact.png", dpi=150)
    plt.close()
    logger.info("Generated: 24_3pct_bond_impact.png")


# =============================================================================
# PLOT 25: 3% Global vs European
# =============================================================================

def plot_25_3pct_global_vs_european(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 25: At 3%, is the Global vs European gap smaller?
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 60/40 Bund
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No 60/40 Bund data available")
        plt.close()
        return

    # Left: Gap comparison at different WRs
    ax1 = axes[0]
    gaps = []
    for wr in [3.0, 3.5, 4.0]:
        wr_data = subset[subset["WR"] == wr]
        global_sr = wr_data[wr_data["Equity"].isin(GLOBAL_INDICES)]["Success_Rate"].mean()
        european_sr = wr_data[wr_data["Equity"].isin(EUROPEAN_INDICES)]["Success_Rate"].mean()
        gaps.append({"WR": f"{wr:g}%", "Gap": global_sr - european_sr if global_sr and european_sr else 0})

    if gaps:
        gap_df = pd.DataFrame(gaps)
        colors = [WR_COLORS.get(float(g["WR"].replace("%", "")), "gray") for g in gaps]
        bars = ax1.bar(gap_df["WR"], gap_df["Gap"], color=colors, alpha=0.85)

        ax1.set_xlabel("Withdrawal Rate", fontsize=12)
        ax1.set_ylabel("Global - European Gap (%)", fontsize=12)
        ax1.set_title("Home Bias Cost at Different WRs\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")

        for bar, val in zip(bars, gap_df["Gap"]):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                     f"{val:.1f}%", ha="center", fontsize=12, fontweight="bold")
        ax1.grid(True, alpha=0.3, axis="y")

    # Right: Success rates at 3%
    ax2 = axes[1]
    data_3pct = subset[subset["WR"] == 3.0].set_index("Equity").reindex(INDEX_ORDER).dropna()

    if not data_3pct.empty:
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in data_3pct.index]
        bars = ax2.barh(data_3pct.index, data_3pct["Success_Rate"], color=colors, alpha=0.85)

        ax2.set_xlabel("Success Rate (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3% Rule: All Indices Performance\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax2.axvline(x=95, color="green", linewidth=2, linestyle="--")
        ax2.set_xlim(88, 100)

        # Add separator
        ax2.axhline(y=1.5, color="black", linestyle="-", linewidth=2, alpha=0.5)
        ax2.text(89, 2.7, "GLOBAL", fontsize=10, fontweight="bold", alpha=0.7)
        ax2.text(89, 0.3, "EUROPEAN", fontsize=10, fontweight="bold", alpha=0.7)

        for bar, val in zip(bars, data_3pct["Success_Rate"]):
            ax2.text(val + 0.2, bar.get_y() + bar.get_height()/2,
                     f"{val:.1f}%", va="center", fontsize=11, fontweight="bold")
        ax2.grid(True, alpha=0.3, axis="x")

    plt.tight_layout()
    plt.savefig(output_dir / "25_3pct_global_vs_european.png", dpi=150)
    plt.close()
    logger.info("Generated: 25_3pct_global_vs_european.png")


# =============================================================================
# PLOT 26: 3% Risk Metrics
# =============================================================================

def plot_26_3pct_risk_metrics(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 26: Risk metrics at 3% - P5, Median, P95 final values.
    """
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)

    # Filter to 3% WR, 60/40 Bund
    mask = (df["WR"] == 3.0) & (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].set_index("Equity").reindex(INDEX_ORDER).dropna()

    if subset.empty:
        logger.warning("No 3% WR 60/40 Bund data available")
        plt.close()
        return

    x = np.arange(len(subset))
    width = 0.25

    p5 = subset["P5_Final"] / 1_000_000
    median = subset["Median_Final"] / 1_000_000
    p95 = subset["P95_Final"] / 1_000_000

    ax.bar(x - width, p5, width, label="P5 (Worst 5%)", color="#e74c3c", alpha=0.85)
    ax.bar(x, median, width, label="Median", color="#f39c12", alpha=0.85)
    ax.bar(x + width, p95, width, label="P95 (Best 5%)", color="#27ae60", alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels(subset.index, rotation=15, ha="right", fontsize=11)
    ax.set_xlabel("Equity Index", fontsize=12)
    ax.set_ylabel("Final Portfolio Value (€ millions)", fontsize=12)
    ax.set_title("3% Rule: Range of Outcomes\n(60/40 with Bund)",
                 fontsize=14, fontweight="bold")
    ax.legend(fontsize=11)
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5, linewidth=1.5)
    ax.text(0.02, 1.1, "Initial €1M", fontsize=10, color="gray")
    ax.grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(output_dir / "26_3pct_risk_metrics.png", dpi=150)
    plt.close()
    logger.info("Generated: 26_3pct_risk_metrics.png")


# =============================================================================
# PLOT 27: 3.5% Sweet Spot Analysis
# =============================================================================

def plot_27_35pct_sweet_spot(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 27: Is 3.5% the sweet spot for European investors?
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Filter to 60/40 Bund
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No 60/40 Bund data available")
        plt.close()
        return

    # Top Left: Success rate comparison across WRs
    ax1 = axes[0, 0]
    for wr in [3.0, 3.5, 4.0]:
        wr_data = subset[subset["WR"] == wr].set_index("Equity").reindex(INDEX_ORDER)
        values = [wr_data.loc[idx, "Success_Rate"] if idx in wr_data.index else 0
                  for idx in INDEX_ORDER]
        x = np.arange(len(INDEX_ORDER))
        width = 0.25
        offset = (wr - 3.5) * width * 2
        ax1.bar(x + offset, values, width, label=f"{wr:g}% WR",
                color=WR_COLORS.get(wr, "gray"), alpha=0.85)

    ax1.set_xticks(np.arange(len(INDEX_ORDER)))
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("Success Rate: 3% vs 3.5% vs 4%\n(60/40 with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.legend(fontsize=10)
    ax1.set_ylim(60, 100)
    ax1.axhline(y=90, color="orange", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.grid(True, alpha=0.3, axis="y")

    # Top Right: 3.5% specific - all indices
    ax2 = axes[0, 1]
    data_35 = subset[subset["WR"] == 3.5].set_index("Equity").reindex(INDEX_ORDER).dropna()

    if not data_35.empty:
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in data_35.index]
        bars = ax2.barh(data_35.index, data_35["Success_Rate"], color=colors, alpha=0.85)

        ax2.set_xlabel("Success Rate (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3.5% Rule: Success Rate\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax2.axvline(x=90, color="orange", linewidth=2, linestyle="--")
        ax2.axvline(x=85, color="red", linewidth=1.5, linestyle="--", alpha=0.5)
        ax2.set_xlim(75, 100)

        for bar, val in zip(bars, data_35["Success_Rate"]):
            status = "✓" if val >= 90 else "⚠" if val >= 85 else "✗"
            ax2.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                     f"{val:.1f}% {status}", va="center", fontsize=11, fontweight="bold")
        ax2.grid(True, alpha=0.3, axis="x")

    # Bottom Left: Trade-off - Success rate vs Final value
    ax3 = axes[1, 0]
    for wr in [3.0, 3.5, 4.0]:
        wr_data = subset[subset["WR"] == wr]
        ax3.scatter(wr_data["Success_Rate"], wr_data["Median_Final"]/1_000_000,
                    c=WR_COLORS.get(wr, "gray"), s=150, alpha=0.75,
                    label=f"{wr:g}% WR", edgecolors="white", linewidth=2)

    ax3.set_xlabel("Success Rate (%)", fontsize=12)
    ax3.set_ylabel("Median Final Value (€ millions)", fontsize=12)
    ax3.set_title("Trade-off: Safety vs Wealth\n(60/40 with Bund)",
                  fontsize=13, fontweight="bold")
    ax3.legend(fontsize=10)
    ax3.axvline(x=90, color="orange", linestyle="--", alpha=0.5, linewidth=1.5)
    ax3.grid(True, alpha=0.3)

    # Bottom Right: Summary
    ax4 = axes[1, 1]
    ax4.axis("off")

    summary_text = "3.5% WR: THE EUROPEAN SWEET SPOT?\n"
    summary_text += "=" * 50 + "\n\n"

    for wr in [3.0, 3.5, 4.0]:
        wr_data = subset[subset["WR"] == wr]
        avg_sr = wr_data["Success_Rate"].mean()
        avg_med = wr_data["Median_Final"].mean() / 1_000_000
        summary_text += f"{wr:g}% WR:\n"
        summary_text += f"  Avg Success Rate:  {avg_sr:.1f}%\n"
        summary_text += f"  Avg Median Value:  €{avg_med:.2f}M\n\n"

    summary_text += "-" * 50 + "\n"
    summary_text += "ANALYSIS:\n"
    summary_text += "3.5% offers a middle ground:\n"
    summary_text += "- Higher income than 3% (+17% more spending)\n"
    summary_text += "- Better safety than 4% (lower failure risk)\n"
    summary_text += "- May be optimal for European investors\n"
    summary_text += "  seeking balance between income and safety"

    ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
             fontsize=11, fontfamily="monospace", verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.5))

    fig.suptitle("3.5% Withdrawal Rate: The European Sweet Spot?",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "27_35pct_sweet_spot.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 27_35pct_sweet_spot.png")


# =============================================================================
# PLOT 28: 3.5% Allocation Sensitivity
# =============================================================================

def plot_28_35pct_allocation_sensitivity(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 28: How does success rate at 3.5% WR change with equity allocation?
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 3.5% WR and Bund
    subset = df[(df["WR"] == 3.5) & (df["Bond"] == "Bund")].copy()

    if subset.empty:
        logger.warning("No 3.5% WR Bund data available")
        plt.close()
        return

    # Left: Line plot
    ax1 = axes[0]
    for equity in INDEX_ORDER:
        eq_data = subset[subset["Equity"] == equity].sort_values("Equity_Pct")
        if not eq_data.empty:
            ax1.plot(eq_data["Equity_Pct"], eq_data["Success_Rate"],
                     marker="o", linewidth=2.5, markersize=8,
                     color=EQUITY_COLORS.get(equity, "gray"),
                     label=equity, alpha=0.9)

    ax1.set_xlabel("Equity Allocation (%)", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("3.5% Rule: Sensitivity to Equity Allocation\n(with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.legend(fontsize=10, loc="lower right")
    ax1.set_xlim(55, 105)
    ax1.set_ylim(75, 100)
    ax1.axhline(y=90, color="orange", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.axhline(y=85, color="red", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.text(57, 90.5, "90% target", fontsize=9, color="orange")
    ax1.grid(True, alpha=0.3)

    # Right: Heatmap
    ax2 = axes[1]
    pivot = subset.pivot_table(index="Equity", columns="Equity_Pct", values="Success_Rate")
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])

    if not pivot.empty:
        sns.heatmap(
            pivot, annot=True, fmt=".1f", cmap="RdYlGn", center=87,
            vmin=75, vmax=98, ax=ax2, cbar_kws={"label": "Success Rate (%)"},
            annot_kws={"size": 11, "weight": "bold"}, linewidths=2, linecolor="white",
        )
        ax2.set_xlabel("Equity Allocation (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3.5% Rule: Success Rate Matrix\n(with Bund)",
                      fontsize=13, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_dir / "28_35pct_allocation_sensitivity.png", dpi=150)
    plt.close()
    logger.info("Generated: 28_35pct_allocation_sensitivity.png")


# =============================================================================
# PLOT 29: 3.5% Bond Impact
# =============================================================================

def plot_29_35pct_bond_impact(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 29: How do different bonds affect 3.5% success rate?
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 3.5% WR and 60/40
    subset = df[(df["WR"] == 3.5) & (df["Equity_Pct"] == 60)].copy()

    if subset.empty:
        logger.warning("No 3.5% WR 60/40 data available")
        plt.close()
        return

    bond_types = subset["Bond"].unique()
    bond_colors = {"Bund": "#3498db", "BTP": "#e74c3c", "Bund/BTP": "#9b59b6", "OAT": "#f39c12"}

    # Left: Bar chart
    ax1 = axes[0]
    x = np.arange(len(INDEX_ORDER))
    width = 0.2

    for i, bond in enumerate(sorted(bond_types)):
        bond_data = subset[subset["Bond"] == bond].set_index("Equity")
        values = [bond_data.loc[idx, "Success_Rate"] if idx in bond_data.index else 0
                  for idx in INDEX_ORDER]
        offset = (i - len(bond_types)/2 + 0.5) * width
        ax1.bar(x + offset, values, width, label=bond,
                color=bond_colors.get(bond, "gray"), alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("3.5% Rule: Bond Type Impact\n(60/40 Allocation)",
                  fontsize=13, fontweight="bold")
    ax1.legend(title="Bond Type", fontsize=10)
    ax1.set_ylim(75, 95)
    ax1.axhline(y=90, color="orange", linestyle="--", alpha=0.5, linewidth=1.5)
    ax1.grid(True, alpha=0.3, axis="y")

    # Right: Heatmap
    ax2 = axes[1]
    pivot = subset.pivot_table(index="Equity", columns="Bond", values="Success_Rate")
    pivot = pivot.reindex([i for i in INDEX_ORDER if i in pivot.index])

    if not pivot.empty:
        sns.heatmap(
            pivot, annot=True, fmt=".1f", cmap="RdYlGn", center=87,
            vmin=75, vmax=95, ax=ax2, cbar_kws={"label": "Success Rate (%)"},
            annot_kws={"size": 12, "weight": "bold"}, linewidths=2, linecolor="white",
        )
        ax2.set_xlabel("Bond Type", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3.5% Rule: Bond Impact Matrix\n(60/40 Allocation)",
                      fontsize=13, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_dir / "29_35pct_bond_impact.png", dpi=150)
    plt.close()
    logger.info("Generated: 29_35pct_bond_impact.png")


# =============================================================================
# PLOT 30: 3.5% Global vs European
# =============================================================================

def plot_30_35pct_global_vs_european(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 30: Global vs European comparison at 3.5%.
    """
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 3.5% WR, 60/40 Bund
    mask = (df["WR"] == 3.5) & (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No 3.5% WR 60/40 Bund data available")
        plt.close()
        return

    subset["Category"] = subset["Equity"].apply(
        lambda x: "Global" if x in GLOBAL_INDICES else "European"
    )

    # Left: Category comparison
    ax1 = axes[0]
    global_sr = subset[subset["Category"] == "Global"]["Success_Rate"].mean()
    european_sr = subset[subset["Category"] == "European"]["Success_Rate"].mean()

    categories = ["Global\n(World, ACWI)", "European\n(Europe, EMU)"]
    means = [global_sr, european_sr]
    colors = ["#27ae60", "#e74c3c"]

    bars = ax1.bar(categories, means, color=colors, alpha=0.85, width=0.6)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("3.5% Rule: Global vs European\n(60/40 with Bund)",
                  fontsize=13, fontweight="bold")
    ax1.set_ylim(75, 95)
    ax1.axhline(y=90, color="orange", linestyle="--", alpha=0.5, linewidth=1.5)

    for bar, val in zip(bars, means):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{val:.1f}%", ha="center", fontsize=14, fontweight="bold")

    gap = global_sr - european_sr
    ax1.annotate("", xy=(1, european_sr), xytext=(1, global_sr),
                 arrowprops=dict(arrowstyle="<->", color="black", lw=2))
    ax1.text(1.15, (global_sr + european_sr)/2, f"Gap:\n{gap:.1f}%",
             fontsize=11, fontweight="bold", va="center")
    ax1.grid(True, alpha=0.3, axis="y")

    # Right: Individual indices
    ax2 = axes[1]
    data_plot = subset.set_index("Equity").reindex(INDEX_ORDER).dropna()

    if not data_plot.empty:
        colors = [EQUITY_COLORS.get(eq, "gray") for eq in data_plot.index]
        bars = ax2.barh(data_plot.index, data_plot["Success_Rate"], color=colors, alpha=0.85)

        ax2.set_xlabel("Success Rate (%)", fontsize=12)
        ax2.set_ylabel("Equity Index", fontsize=12)
        ax2.set_title("3.5% Rule: Individual Index Performance\n(60/40 with Bund)",
                      fontsize=13, fontweight="bold")
        ax2.axvline(x=90, color="orange", linewidth=2, linestyle="--")
        ax2.set_xlim(75, 95)

        ax2.axhline(y=1.5, color="black", linestyle="-", linewidth=2, alpha=0.5)
        ax2.text(76, 2.7, "GLOBAL", fontsize=10, fontweight="bold", alpha=0.7)
        ax2.text(76, 0.3, "EUROPEAN", fontsize=10, fontweight="bold", alpha=0.7)

        for bar, val in zip(bars, data_plot["Success_Rate"]):
            ax2.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                     f"{val:.1f}%", va="center", fontsize=11, fontweight="bold")
        ax2.grid(True, alpha=0.3, axis="x")

    plt.tight_layout()
    plt.savefig(output_dir / "30_35pct_global_vs_european.png", dpi=150)
    plt.close()
    logger.info("Generated: 30_35pct_global_vs_european.png")


# =============================================================================
# PLOT 31: 3.5% Risk Metrics
# =============================================================================

def plot_31_35pct_risk_metrics(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 31: Risk metrics at 3.5% - P5, Median, P95 final values.
    """
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)

    # Filter to 3.5% WR, 60/40 Bund
    mask = (df["WR"] == 3.5) & (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].set_index("Equity").reindex(INDEX_ORDER).dropna()

    if subset.empty:
        logger.warning("No 3.5% WR 60/40 Bund data available")
        plt.close()
        return

    x = np.arange(len(subset))
    width = 0.25

    p5 = subset["P5_Final"] / 1_000_000
    median = subset["Median_Final"] / 1_000_000
    p95 = subset["P95_Final"] / 1_000_000

    ax.bar(x - width, p5, width, label="P5 (Worst 5%)", color="#e74c3c", alpha=0.85)
    ax.bar(x, median, width, label="Median", color="#f39c12", alpha=0.85)
    ax.bar(x + width, p95, width, label="P95 (Best 5%)", color="#27ae60", alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels(subset.index, rotation=15, ha="right", fontsize=11)
    ax.set_xlabel("Equity Index", fontsize=12)
    ax.set_ylabel("Final Portfolio Value (€ millions)", fontsize=12)
    ax.set_title("3.5% Rule: Range of Outcomes\n(60/40 with Bund)",
                 fontsize=14, fontweight="bold")
    ax.legend(fontsize=11)
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5, linewidth=1.5)
    ax.text(0.02, 1.1, "Initial €1M", fontsize=10, color="gray")
    ax.grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(output_dir / "31_35pct_risk_metrics.png", dpi=150)
    plt.close()
    logger.info("Generated: 31_35pct_risk_metrics.png")


# =============================================================================
# PLOT 32: WR Comparison Summary
# =============================================================================

def plot_32_wr_comparison_summary(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 32: Grand summary comparing all three withdrawal rates.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Filter to 60/40 Bund
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No 60/40 Bund data available")
        plt.close()
        return

    # Top Left: Success Rate by WR
    ax1 = axes[0, 0]
    avg_sr = subset.groupby("WR")["Success_Rate"].mean()

    bars = ax1.bar([f"{wr:g}%" for wr in avg_sr.index], avg_sr.values,
                   color=[WR_COLORS.get(wr, "gray") for wr in avg_sr.index], alpha=0.85)
    ax1.set_xlabel("Withdrawal Rate", fontsize=12)
    ax1.set_ylabel("Average Success Rate (%)", fontsize=12)
    ax1.set_title("Average Success Rate by WR\n(60/40 with Bund, All Indices)",
                  fontsize=13, fontweight="bold")
    ax1.set_ylim(70, 100)

    for bar, val in zip(bars, avg_sr.values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{val:.1f}%", ha="center", fontsize=14, fontweight="bold")
    ax1.grid(True, alpha=0.3, axis="y")

    # Top Right: Median Final Value by WR
    ax2 = axes[0, 1]
    avg_med = subset.groupby("WR")["Median_Final"].mean() / 1_000_000

    bars = ax2.bar([f"{wr:g}%" for wr in avg_med.index], avg_med.values,
                   color=[WR_COLORS.get(wr, "gray") for wr in avg_med.index], alpha=0.85)
    ax2.set_xlabel("Withdrawal Rate", fontsize=12)
    ax2.set_ylabel("Average Median Final Value (€ millions)", fontsize=12)
    ax2.set_title("Average Median Final Value by WR\n(60/40 with Bund, All Indices)",
                  fontsize=13, fontweight="bold")
    ax2.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5)

    for bar, val in zip(bars, avg_med.values):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                 f"€{val:.2f}M", ha="center", fontsize=12, fontweight="bold")
    ax2.grid(True, alpha=0.3, axis="y")

    # Bottom Left: Scatter - Success vs Final Value
    ax3 = axes[1, 0]
    for wr in sorted(subset["WR"].unique()):
        wr_data = subset[subset["WR"] == wr]
        for equity in INDEX_ORDER:
            eq_data = wr_data[wr_data["Equity"] == equity]
            if not eq_data.empty:
                ax3.scatter(
                    eq_data["Success_Rate"],
                    eq_data["Median_Final"] / 1_000_000,
                    c=WR_COLORS.get(wr, "gray"),
                    marker=EQUITY_MARKERS.get(equity, "o"),
                    s=150, alpha=0.75, edgecolors="white", linewidth=1.5
                )

    # Custom legend
    wr_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                         markersize=12, label=f"{wr:g}% WR")
                  for wr, c in sorted(WR_COLORS.items())]
    legend1 = ax3.legend(handles=wr_handles, loc="upper left", fontsize=10,
                         title="Withdrawal Rate")
    ax3.add_artist(legend1)

    ax3.set_xlabel("Success Rate (%)", fontsize=12)
    ax3.set_ylabel("Median Final Value (€ millions)", fontsize=12)
    ax3.set_title("Trade-off: Success Rate vs Final Value\n(60/40 with Bund)",
                  fontsize=13, fontweight="bold")
    ax3.grid(True, alpha=0.3)

    # Bottom Right: Summary table
    ax4 = axes[1, 1]
    ax4.axis("off")

    summary_text = "WITHDRAWAL RATE COMPARISON SUMMARY\n"
    summary_text += "(60/40 Portfolio with Bund)\n"
    summary_text += "=" * 55 + "\n\n"

    summary_text += f"{'WR':<8} {'Success':<12} {'Median Value':<15} {'Recommendation':<20}\n"
    summary_text += "-" * 55 + "\n"

    recommendations = {
        3.0: "Very Safe - Conservative",
        3.5: "Balanced - Sweet Spot?",
        4.0: "Traditional - Higher Risk"
    }

    for wr in sorted(subset["WR"].unique()):
        wr_data = subset[subset["WR"] == wr]
        sr = wr_data["Success_Rate"].mean()
        med = wr_data["Median_Final"].mean() / 1_000_000
        rec = recommendations.get(wr, "")
        summary_text += f"{wr:g}%{'':<5} {sr:>5.1f}%{'':<6} €{med:>5.2f}M{'':<7} {rec}\n"

    summary_text += "-" * 55 + "\n\n"
    summary_text += "KEY INSIGHTS:\n"
    summary_text += "• 3% offers highest safety but lower spending\n"
    summary_text += "• 3.5% provides good balance for Europe\n"
    summary_text += "• 4% (US standard) is riskier in Europe\n\n"
    summary_text += "RECOMMENDATION FOR EUROPEAN INVESTORS:\n"
    summary_text += "Consider 3-3.5% WR for better safety margins\n"
    summary_text += "vs the traditional US-based 4% rule."

    ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
             fontsize=11, fontfamily="monospace", verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="lightcyan", alpha=0.5))

    fig.suptitle("Withdrawal Rate Comparison: 3% vs 3.5% vs 4%",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "32_wr_comparison_summary.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 32_wr_comparison_summary.png")


# =============================================================================
# PLOT 32b: WR Comparison Summary - Bund+BTP Mix
# =============================================================================

def plot_32b_wr_comparison_summary_bundbtp(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 32b: Grand summary comparing all three withdrawal rates with Bund+BTP mix.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Filter to 60% equity with Bund+BTP
    mask = (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund+BTP")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No 60/20/20 Bund+BTP data available")
        plt.close()
        return

    # Top Left: Success Rate by WR
    ax1 = axes[0, 0]
    avg_sr = subset.groupby("WR")["Success_Rate"].mean()

    bars = ax1.bar([f"{wr:g}%" for wr in avg_sr.index], avg_sr.values,
                   color=[WR_COLORS.get(wr, "gray") for wr in avg_sr.index], alpha=0.85)
    ax1.set_xlabel("Withdrawal Rate", fontsize=12)
    ax1.set_ylabel("Average Success Rate (%)", fontsize=12)
    ax1.set_title("Average Success Rate by WR\n(60/20/20 with Bund+BTP, All Indices)",
                  fontsize=13, fontweight="bold")
    ax1.set_ylim(70, 100)

    for bar, val in zip(bars, avg_sr.values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{val:.1f}%", ha="center", fontsize=14, fontweight="bold")
    ax1.grid(True, alpha=0.3, axis="y")

    # Top Right: Median Final Value by WR
    ax2 = axes[0, 1]
    avg_med = subset.groupby("WR")["Median_Final"].mean() / 1_000_000

    bars = ax2.bar([f"{wr:g}%" for wr in avg_med.index], avg_med.values,
                   color=[WR_COLORS.get(wr, "gray") for wr in avg_med.index], alpha=0.85)
    ax2.set_xlabel("Withdrawal Rate", fontsize=12)
    ax2.set_ylabel("Average Median Final Value (€ millions)", fontsize=12)
    ax2.set_title("Average Median Final Value by WR\n(60/20/20 with Bund+BTP, All Indices)",
                  fontsize=13, fontweight="bold")
    ax2.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5)

    for bar, val in zip(bars, avg_med.values):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                 f"€{val:.2f}M", ha="center", fontsize=12, fontweight="bold")
    ax2.grid(True, alpha=0.3, axis="y")

    # Bottom Left: Scatter - Success vs Final Value
    ax3 = axes[1, 0]
    for wr in sorted(subset["WR"].unique()):
        wr_data = subset[subset["WR"] == wr]
        for equity in INDEX_ORDER:
            eq_data = wr_data[wr_data["Equity"] == equity]
            if not eq_data.empty:
                ax3.scatter(
                    eq_data["Success_Rate"],
                    eq_data["Median_Final"] / 1_000_000,
                    c=WR_COLORS.get(wr, "gray"),
                    marker=EQUITY_MARKERS.get(equity, "o"),
                    s=150, alpha=0.75, edgecolors="white", linewidth=1.5
                )

    # Custom legend
    wr_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                         markersize=12, label=f"{wr:g}% WR")
                  for wr, c in sorted(WR_COLORS.items())]
    legend1 = ax3.legend(handles=wr_handles, loc="upper left", fontsize=10,
                         title="Withdrawal Rate")
    ax3.add_artist(legend1)

    ax3.set_xlabel("Success Rate (%)", fontsize=12)
    ax3.set_ylabel("Median Final Value (€ millions)", fontsize=12)
    ax3.set_title("Trade-off: Success Rate vs Final Value\n(60/20/20 with Bund+BTP)",
                  fontsize=13, fontweight="bold")
    ax3.grid(True, alpha=0.3)

    # Bottom Right: Summary table
    ax4 = axes[1, 1]
    ax4.axis("off")

    summary_text = "WITHDRAWAL RATE COMPARISON SUMMARY\n"
    summary_text += "(60/20/20 Portfolio with Bund+BTP)\n"
    summary_text += "=" * 55 + "\n\n"

    summary_text += f"{'WR':<8} {'Success':<12} {'Median Value':<15} {'Recommendation':<20}\n"
    summary_text += "-" * 55 + "\n"

    recommendations = {
        3.0: "Very Safe - Conservative",
        3.5: "Balanced - Sweet Spot?",
        4.0: "Traditional - Higher Risk"
    }

    for wr in sorted(subset["WR"].unique()):
        wr_data = subset[subset["WR"] == wr]
        sr = wr_data["Success_Rate"].mean()
        med = wr_data["Median_Final"].mean() / 1_000_000
        rec = recommendations.get(wr, "")
        summary_text += f"{wr:g}%{'':<5} {sr:>5.1f}%{'':<6} €{med:>5.2f}M{'':<7} {rec}\n"

    summary_text += "-" * 55 + "\n\n"
    summary_text += "KEY INSIGHTS:\n"
    summary_text += "• 3% offers highest safety but lower spending\n"
    summary_text += "• 3.5% provides good balance for Europe\n"
    summary_text += "• 4% (US standard) is riskier in Europe\n\n"
    summary_text += "RECOMMENDATION FOR EUROPEAN INVESTORS:\n"
    summary_text += "Consider 3-3.5% WR for better safety margins\n"
    summary_text += "vs the traditional US-based 4% rule."

    ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
             fontsize=11, fontfamily="monospace", verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="lightcyan", alpha=0.5))

    fig.suptitle("Withdrawal Rate Comparison: 3% vs 3.5% vs 4% (Bund+BTP)",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "32b_wr_comparison_summary_bundbtp.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 32b_wr_comparison_summary_bundbtp.png")


# =============================================================================
# PLOT 33: Optimal Bond Strategy
# =============================================================================

def plot_33_optimal_bond_strategy(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 33: Which bond strategy is optimal? Bund vs BTP vs Mix comparison.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Define bond colors
    bond_colors = {"Bund": "#3498db", "BTP": "#e74c3c", "Bund+BTP": "#9b59b6"}

    # Prepare data for 60% equity portfolios
    # Bund and BTP use 60/40, Mix uses 60/20/20
    def get_bond_data(wr):
        results = []
        for equity in INDEX_ORDER:
            row = {"Equity": equity, "WR": wr}
            # Bund 60/40
            bund = df[(df["Equity"] == equity) & (df["WR"] == wr) &
                      (df["Bond"] == "Bund") & (df["Allocation"] == "60/40")]
            row["Bund"] = bund["Success_Rate"].values[0] if len(bund) > 0 else None

            # BTP 60/40
            btp = df[(df["Equity"] == equity) & (df["WR"] == wr) &
                     (df["Bond"] == "BTP") & (df["Allocation"] == "60/40")]
            row["BTP"] = btp["Success_Rate"].values[0] if len(btp) > 0 else None

            # Mix 60/20/20
            mix = df[(df["Equity"] == equity) & (df["WR"] == wr) &
                     (df["Bond"] == "Bund+BTP") & (df["Allocation"] == "60/20/20")]
            row["Bund+BTP"] = mix["Success_Rate"].values[0] if len(mix) > 0 else None

            results.append(row)
        return pd.DataFrame(results)

    # Top Left: Success Rate by Bond Type at 4% WR
    ax1 = axes[0, 0]
    data_4pct = get_bond_data(4.0)

    x = np.arange(len(INDEX_ORDER))
    width = 0.25

    for i, bond in enumerate(["Bund", "BTP", "Bund+BTP"]):
        values = data_4pct[bond].fillna(0).values
        offset = (i - 1) * width
        ax1.bar(x + offset, values, width, label=bond,
                color=bond_colors[bond], alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Success Rate (%)", fontsize=12)
    ax1.set_title("Bond Strategy Comparison at 4% WR\n(60% Equity)",
                  fontsize=13, fontweight="bold")
    ax1.legend(title="Bond Type", fontsize=10)
    ax1.set_ylim(55, 85)
    ax1.grid(True, alpha=0.3, axis="y")

    # Highlight winner
    for i, equity in enumerate(INDEX_ORDER):
        row = data_4pct[data_4pct["Equity"] == equity].iloc[0]
        rates = {"Bund": row["Bund"], "BTP": row["BTP"], "Bund+BTP": row["Bund+BTP"]}
        valid = {k: v for k, v in rates.items() if pd.notna(v)}
        if valid:
            winner = max(valid, key=valid.get)
            ax1.text(i, max(valid.values()) + 0.8, "*", ha="center",
                     fontsize=14, color=bond_colors[winner], fontweight="bold")

    # Top Right: Winner by WR
    ax2 = axes[0, 1]
    summary_data = []
    for wr in [3.0, 3.5, 4.0]:
        wr_data = get_bond_data(wr)
        for bond in ["Bund", "BTP", "Bund+BTP"]:
            avg = wr_data[bond].mean()
            if pd.notna(avg):
                summary_data.append({"WR": f"{wr:g}%", "Bond": bond, "Avg_SR": avg})

    summary_df = pd.DataFrame(summary_data)
    pivot = summary_df.pivot(index="Bond", columns="WR", values="Avg_SR")
    pivot = pivot[["3%", "3.5%", "4%"]]  # Order columns

    pivot.plot(kind="bar", ax=ax2, color=[WR_COLORS[3.0], WR_COLORS[3.5], WR_COLORS[4.0]],
               alpha=0.85, width=0.8)
    ax2.set_xlabel("Bond Type", fontsize=12)
    ax2.set_ylabel("Average Success Rate (%)", fontsize=12)
    ax2.set_title("Average Success Rate by Bond & WR\n(All Indices, 60% Equity)",
                  fontsize=13, fontweight="bold")
    ax2.legend(title="WR", fontsize=10)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)
    ax2.grid(True, alpha=0.3, axis="y")

    # Bottom Left: Difference from Bund (BTP advantage)
    ax3 = axes[1, 0]
    diff_data = []
    for wr in [3.0, 3.5, 4.0]:
        wr_data = get_bond_data(wr)
        for equity in INDEX_ORDER:
            row = wr_data[wr_data["Equity"] == equity].iloc[0]
            if pd.notna(row["Bund"]) and pd.notna(row["BTP"]):
                diff_data.append({
                    "WR": wr, "Equity": equity,
                    "BTP_vs_Bund": row["BTP"] - row["Bund"],
                    "Mix_vs_Bund": row["Bund+BTP"] - row["Bund"] if pd.notna(row["Bund+BTP"]) else None
                })

    diff_df = pd.DataFrame(diff_data)

    for wr in [3.0, 3.5, 4.0]:
        wr_diff = diff_df[diff_df["WR"] == wr]
        if not wr_diff.empty:
            ax3.scatter(wr_diff["Equity"], wr_diff["BTP_vs_Bund"],
                        c=WR_COLORS[wr], s=150, alpha=0.8, label=f"{wr:g}% WR",
                        edgecolors="white", linewidth=1.5)

    ax3.axhline(y=0, color="black", linewidth=1.5)
    ax3.set_xlabel("Equity Index", fontsize=12)
    ax3.set_ylabel("BTP Advantage vs Bund (%)", fontsize=12)
    ax3.set_title("BTP Performance Advantage over Bund\n(Positive = BTP better)",
                  fontsize=13, fontweight="bold")
    ax3.legend(fontsize=10)
    ax3.tick_params(axis="x", rotation=15)
    ax3.grid(True, alpha=0.3)

    # Add annotation
    ax3.fill_between(ax3.get_xlim(), 0, 5, alpha=0.1, color="green")
    ax3.fill_between(ax3.get_xlim(), -5, 0, alpha=0.1, color="red")
    ax3.text(0.02, 0.95, "BTP better", transform=ax3.transAxes,
             fontsize=9, color="green", style="italic")
    ax3.text(0.02, 0.05, "Bund better", transform=ax3.transAxes,
             fontsize=9, color="red", style="italic")

    # Bottom Right: Summary and Recommendation
    ax4 = axes[1, 1]
    ax4.axis("off")

    summary_text = "OPTIMAL BOND STRATEGY ANALYSIS\n"
    summary_text += "=" * 50 + "\n\n"

    summary_text += "FINDINGS BY WITHDRAWAL RATE:\n"
    summary_text += "-" * 50 + "\n"

    for wr in [3.0, 3.5, 4.0]:
        wr_data = get_bond_data(wr)
        bund_avg = wr_data["Bund"].mean()
        btp_avg = wr_data["BTP"].mean()
        mix_avg = wr_data["Bund+BTP"].mean()

        best = "Mix" if mix_avg >= max(bund_avg, btp_avg) else ("BTP" if btp_avg > bund_avg else "Bund")
        diff = max(btp_avg, mix_avg) - bund_avg

        summary_text += f"\n{wr:g}% WR:\n"
        summary_text += f"  Bund:     {bund_avg:.1f}%\n"
        summary_text += f"  BTP:      {btp_avg:.1f}%\n"
        summary_text += f"  Mix:      {mix_avg:.1f}%\n"
        summary_text += f"  Winner:   {best} (+{diff:.1f}% vs Bund)\n"

    summary_text += "\n" + "-" * 50 + "\n"
    summary_text += "RECOMMENDATION:\n"
    summary_text += "At higher WRs (3.5-4%), BTP or Mix\n"
    summary_text += "outperforms pure Bund by 1-2%.\n"
    summary_text += "Higher BTP yield compensates for\n"
    summary_text += "withdrawal pressure at aggressive WRs.\n\n"
    summary_text += "At conservative 3% WR, differences\n"
    summary_text += "are minimal - all strategies viable."

    ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
             fontsize=10, fontfamily="monospace", verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.5))

    fig.suptitle("Optimal Bond Strategy: Bund vs BTP vs Mix",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "33_optimal_bond_strategy.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 33_optimal_bond_strategy.png")


# =============================================================================
# PLOT 34: Bond Strategy Deep Dive
# =============================================================================

def plot_34_bond_strategy_deep_dive(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Plot 34: Deep dive into bond strategy - final values and risk metrics.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    bond_colors = {"Bund": "#3498db", "BTP": "#e74c3c", "Bund+BTP": "#9b59b6"}

    # Helper to get comparable data
    def get_comparable_data(wr, metric):
        results = []
        for equity in INDEX_ORDER:
            row = {"Equity": equity}
            # Bund 60/40
            bund = df[(df["Equity"] == equity) & (df["WR"] == wr) &
                      (df["Bond"] == "Bund") & (df["Allocation"] == "60/40")]
            row["Bund"] = bund[metric].values[0] if len(bund) > 0 else None

            # BTP 60/40
            btp = df[(df["Equity"] == equity) & (df["WR"] == wr) &
                     (df["Bond"] == "BTP") & (df["Allocation"] == "60/40")]
            row["BTP"] = btp[metric].values[0] if len(btp) > 0 else None

            # Mix 60/20/20
            mix = df[(df["Equity"] == equity) & (df["WR"] == wr) &
                     (df["Bond"] == "Bund+BTP") & (df["Allocation"] == "60/20/20")]
            row["Bund+BTP"] = mix[metric].values[0] if len(mix) > 0 else None

            results.append(row)
        return pd.DataFrame(results)

    # Top Left: Median Final Value at 4% WR
    ax1 = axes[0, 0]
    data_med = get_comparable_data(4.0, "Median_Final")

    x = np.arange(len(INDEX_ORDER))
    width = 0.25

    for i, bond in enumerate(["Bund", "BTP", "Bund+BTP"]):
        values = (data_med[bond].fillna(0) / 1_000_000).values
        offset = (i - 1) * width
        ax1.bar(x + offset, values, width, label=bond,
                color=bond_colors[bond], alpha=0.85)

    ax1.set_xticks(x)
    ax1.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax1.set_xlabel("Equity Index", fontsize=12)
    ax1.set_ylabel("Median Final Value (M EUR)", fontsize=12)
    ax1.set_title("Median Final Value by Bond Type (4% WR)\n(60% Equity)",
                  fontsize=13, fontweight="bold")
    ax1.legend(title="Bond Type", fontsize=10)
    ax1.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5)
    ax1.grid(True, alpha=0.3, axis="y")

    # Top Right: Failure Rate by Bond Type at 4% WR
    ax2 = axes[0, 1]
    data_fail = get_comparable_data(4.0, "Failed_Pct")

    for i, bond in enumerate(["Bund", "BTP", "Bund+BTP"]):
        values = data_fail[bond].fillna(0).values
        offset = (i - 1) * width
        ax2.bar(x + offset, values, width, label=bond,
                color=bond_colors[bond], alpha=0.85)

    ax2.set_xticks(x)
    ax2.set_xticklabels(INDEX_ORDER, rotation=15, ha="right", fontsize=11)
    ax2.set_xlabel("Equity Index", fontsize=12)
    ax2.set_ylabel("Failure Rate (%)", fontsize=12)
    ax2.set_title("Failure Rate by Bond Type (4% WR)\n(60% Equity - Lower is Better)",
                  fontsize=13, fontweight="bold")
    ax2.legend(title="Bond Type", fontsize=10)
    ax2.axhline(y=20, color="orange", linestyle="--", alpha=0.5, linewidth=1.5)
    ax2.text(0.02, 0.85, "20% threshold", transform=ax2.transAxes, fontsize=9, color="orange")
    ax2.grid(True, alpha=0.3, axis="y")

    # Bottom Left: Success Rate comparison across all WRs (MSCI World only)
    ax3 = axes[1, 0]

    # Get data for MSCI World across WRs
    world_data = []
    for wr in [3.0, 3.5, 4.0]:
        for bond, alloc in [("Bund", "60/40"), ("BTP", "60/40"), ("Bund+BTP", "60/20/20")]:
            row = df[(df["Equity"] == "MSCI World") & (df["WR"] == wr) &
                     (df["Bond"] == bond) & (df["Allocation"] == alloc)]
            if len(row) > 0:
                world_data.append({
                    "WR": f"{wr:g}%", "Bond": bond,
                    "Success_Rate": row["Success_Rate"].values[0]
                })

    world_df = pd.DataFrame(world_data)
    pivot_world = world_df.pivot(index="WR", columns="Bond", values="Success_Rate")
    pivot_world = pivot_world[["Bund", "BTP", "Bund+BTP"]]

    pivot_world.plot(kind="bar", ax=ax3,
                     color=[bond_colors["Bund"], bond_colors["BTP"], bond_colors["Bund+BTP"]],
                     alpha=0.85, width=0.8)
    ax3.set_xlabel("Withdrawal Rate", fontsize=12)
    ax3.set_ylabel("Success Rate (%)", fontsize=12)
    ax3.set_title("MSCI World: Bond Strategy by WR\n(60% Equity)",
                  fontsize=13, fontweight="bold")
    ax3.legend(title="Bond Type", fontsize=10)
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=0)
    ax3.set_ylim(75, 100)
    ax3.grid(True, alpha=0.3, axis="y")

    # Add value labels
    for container in ax3.containers:
        ax3.bar_label(container, fmt="%.1f", fontsize=9)

    # Bottom Right: Risk-adjusted comparison
    ax4 = axes[1, 1]

    # Scatter: Success Rate vs Median Final Value at 4%
    data_sr = get_comparable_data(4.0, "Success_Rate")
    data_med = get_comparable_data(4.0, "Median_Final")

    for bond in ["Bund", "BTP", "Bund+BTP"]:
        for i, equity in enumerate(INDEX_ORDER):
            sr = data_sr[data_sr["Equity"] == equity][bond].values[0]
            med = data_med[data_med["Equity"] == equity][bond].values[0]
            if pd.notna(sr) and pd.notna(med):
                ax4.scatter(sr, med / 1_000_000, c=bond_colors[bond],
                            marker=EQUITY_MARKERS.get(equity, "o"),
                            s=150, alpha=0.75, edgecolors="white", linewidth=1.5)

    # Custom legend
    bond_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                           markersize=12, label=b)
                    for b, c in bond_colors.items()]
    legend1 = ax4.legend(handles=bond_handles, loc="upper left", fontsize=10,
                         title="Bond Type")
    ax4.add_artist(legend1)

    index_handles = [Line2D([0], [0], marker=m, color="gray", markersize=10,
                            linestyle="None", label=eq)
                     for eq, m in EQUITY_MARKERS.items() if eq in INDEX_ORDER]
    ax4.legend(handles=index_handles, loc="lower right", fontsize=9,
               title="Index")

    ax4.set_xlabel("Success Rate (%)", fontsize=12)
    ax4.set_ylabel("Median Final Value (M EUR)", fontsize=12)
    ax4.set_title("Risk vs Return by Bond Type (4% WR)\n(60% Equity)",
                  fontsize=13, fontweight="bold")
    ax4.grid(True, alpha=0.3)

    fig.suptitle("Bond Strategy Deep Dive: Risk and Return Analysis",
                 fontsize=16, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir / "34_bond_strategy_deep_dive.png", dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Generated: 34_bond_strategy_deep_dive.png")


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate analysis plots from ANALYSIS_REGISTRY.csv"
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("ANALYSIS_REGISTRY.csv"),
        help="Input CSV file (default: ANALYSIS_REGISTRY.csv)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("plots"),
        help="Output directory for plots (default: plots/)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    if not args.input.exists():
        logger.error(f"Input file not found: {args.input}")
        return 1

    logger.info(f"Loading data from {args.input}")
    df = load_data(args.input)
    logger.info(f"Loaded {len(df)} records")

    # Generate all plots
    logger.info(f"Generating plots in {args.output_dir}/")

    plot_01_success_rate_summary_matrix(df, args.output_dir)
    plot_01b_success_rate_summary_matrix_bundbtp(df, args.output_dir)
    plot_02_success_rate_by_wr_all_indices(df, args.output_dir)
    plot_03_success_rate_by_allocation_grid(df, args.output_dir)
    plot_04_global_vs_european_comparison(df, args.output_dir)
    plot_05_heatmap_grid_by_wr(df, args.output_dir)
    plot_06_bond_comparison_grid(df, args.output_dir)
    plot_07_risk_return_scatter(df, args.output_dir)
    plot_08_final_value_distribution(df, args.output_dir)
    plot_09_depletion_year_analysis(df, args.output_dir)

    # Depletion-focused plots
    plot_10_depletion_risk_heatmap(df, args.output_dir)
    plot_11_depletion_vs_allocation(df, args.output_dir)
    plot_12_depletion_spread_analysis(df, args.output_dir)
    plot_13_failure_rate_vs_depletion(df, args.output_dir)
    plot_14_depletion_global_vs_european(df, args.output_dir)

    # 4% WR specific plots
    plot_15_4pct_reality_check(df, args.output_dir)
    plot_16_4pct_allocation_sensitivity(df, args.output_dir)
    plot_17_4pct_worst_case(df, args.output_dir)
    plot_18_4pct_depletion_timeline(df, args.output_dir)
    plot_19_4pct_bond_impact(df, args.output_dir)
    plot_20_4pct_global_vs_european_gap(df, args.output_dir)

    # 3% WR specific plots
    plot_21_3pct_safety_analysis(df, args.output_dir)
    plot_22_3pct_allocation_sensitivity(df, args.output_dir)
    plot_23_3pct_final_value_tradeoff(df, args.output_dir)
    plot_24_3pct_bond_impact(df, args.output_dir)
    plot_25_3pct_global_vs_european(df, args.output_dir)
    plot_26_3pct_risk_metrics(df, args.output_dir)

    # 3.5% WR specific plots
    plot_27_35pct_sweet_spot(df, args.output_dir)
    plot_28_35pct_allocation_sensitivity(df, args.output_dir)
    plot_29_35pct_bond_impact(df, args.output_dir)
    plot_30_35pct_global_vs_european(df, args.output_dir)
    plot_31_35pct_risk_metrics(df, args.output_dir)
    plot_32_wr_comparison_summary(df, args.output_dir)
    plot_32b_wr_comparison_summary_bundbtp(df, args.output_dir)

    # Optimal bond strategy plots
    plot_33_optimal_bond_strategy(df, args.output_dir)
    plot_34_bond_strategy_deep_dive(df, args.output_dir)

    logger.info("All plots generated successfully!")
    return 0


if __name__ == "__main__":
    exit(main())
