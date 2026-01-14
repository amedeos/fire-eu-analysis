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
    ax1.legend(loc="lower left", fontsize=10, ncol=2)
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
    ax2.legend(loc="lower left", fontsize=10)
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

    logger.info("All plots generated successfully!")
    return 0


if __name__ == "__main__":
    exit(main())
