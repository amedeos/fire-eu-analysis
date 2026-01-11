#!/usr/bin/env python3
"""
Generate analysis plots from ANALYSIS_REGISTRY.csv data.

Creates visualizations for Safe Withdrawal Rate analysis including:
- Success rate comparisons across withdrawal rates, allocations, indices
- Final value distributions
- Risk/return trade-offs
- Depletion year analysis
"""

import argparse
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Set style for all plots
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("husl")

# Figure size constants
FIGSIZE_WIDE = (12, 6)
FIGSIZE_SQUARE = (10, 8)
FIGSIZE_TALL = (10, 10)


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load and prepare data from CSV."""
    df = pd.read_csv(csv_path)

    # Exclude STOXX 600 data (03xx notebooks)
    df = df[df["Equity"] != "STOXX 600"].copy()

    # Extract equity percentage from allocation string
    df["Equity_Pct"] = df["Allocation"].apply(
        lambda x: int(str(x).split("/")[0]) if "/" in str(x) else int(x)
    )

    # Create readable labels
    df["Portfolio"] = df["Equity"] + " + " + df["Bond"].fillna("-")
    df["WR_Label"] = df["WR"].apply(lambda x: f"{x:g}%")

    return df


def plot_success_rate_vs_withdrawal_rate(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 1: Success Rate vs Withdrawal Rate for same portfolios."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to MSCI World + Bund portfolios (available in all WR)
    mask = (df["Equity"] == "MSCI World") & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Success Rate vs WR plot")
        return

    # Pivot for grouped bar chart
    pivot = subset.pivot(index="Allocation", columns="WR", values="Success_Rate")
    pivot = pivot.sort_index(key=lambda x: x.map(lambda v: int(str(v).split("/")[0])))

    pivot.plot(kind="bar", ax=ax, width=0.8)

    ax.set_xlabel("Portfolio Allocation (Equity/Bond)", fontsize=12)
    ax.set_ylabel("Success Rate (%)", fontsize=12)
    ax.set_title("Success Rate vs Withdrawal Rate\n(MSCI World + Bund Portfolios)", fontsize=14)
    ax.set_ylim(0, 100)
    ax.legend(title="Withdrawal Rate", labels=[f"{wr:g}%" for wr in pivot.columns])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

    # Add value labels on bars
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", fontsize=8)

    plt.tight_layout()
    plt.savefig(output_dir / "01_success_rate_vs_wr.png", dpi=150)
    plt.close()
    logger.info("Generated: 01_success_rate_vs_wr.png")


def plot_success_rate_vs_allocation(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 2: Success Rate vs Equity Allocation."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to 4% WR and single-bond portfolios for clarity
    mask = (df["WR"] == 4.0) & (~df["Bond"].str.contains(r"\+", na=False))
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Success Rate vs Allocation plot")
        return

    # Group by Equity index and Bond type
    for (equity, bond), group in subset.groupby(["Equity", "Bond"]):
        group_sorted = group.sort_values("Equity_Pct")
        label = f"{equity} + {bond}" if pd.notna(bond) and bond != "-" else equity
        ax.plot(
            group_sorted["Equity_Pct"],
            group_sorted["Success_Rate"],
            marker="o",
            linewidth=2,
            markersize=8,
            label=label,
        )

    ax.set_xlabel("Equity Allocation (%)", fontsize=12)
    ax.set_ylabel("Success Rate (%)", fontsize=12)
    ax.set_title("Success Rate vs Equity Allocation (4% WR)", fontsize=14)
    ax.set_xlim(55, 105)
    ax.set_ylim(50, 100)
    ax.legend(loc="lower left", fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "02_success_rate_vs_allocation.png", dpi=150)
    plt.close()
    logger.info("Generated: 02_success_rate_vs_allocation.png")


def plot_success_rate_by_equity_index(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 3: Success Rate comparison across Equity Indices."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to 4% WR, 60/40 allocation, Bund only
    mask = (df["WR"] == 4.0) & (df["Equity_Pct"] == 60) & (df["Bond"] == "Bund")
    subset = df[mask].copy()

    if subset.empty:
        # Try with any 60/40 allocation
        mask = (df["WR"] == 4.0) & (df["Equity_Pct"] == 60)
        subset = df[mask].drop_duplicates(subset=["Equity"]).copy()

    if subset.empty:
        logger.warning("No data for Equity Index comparison plot")
        return

    # Sort by success rate
    subset = subset.sort_values("Success_Rate", ascending=True)

    colors = sns.color_palette("viridis", len(subset))
    bars = ax.barh(subset["Equity"], subset["Success_Rate"], color=colors)

    ax.set_xlabel("Success Rate (%)", fontsize=12)
    ax.set_ylabel("Equity Index", fontsize=12)
    ax.set_title("Success Rate by Equity Index\n(60/40 Allocation, 4% WR, Bund)", fontsize=14)
    ax.set_xlim(0, 100)

    # Add value labels
    for bar, val in zip(bars, subset["Success_Rate"]):
        ax.text(val + 1, bar.get_y() + bar.get_height() / 2, f"{val:.1f}%", va="center")

    plt.tight_layout()
    plt.savefig(output_dir / "03_success_rate_by_equity_index.png", dpi=150)
    plt.close()
    logger.info("Generated: 03_success_rate_by_equity_index.png")


def plot_success_rate_by_bond_type(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 4: Success Rate comparison across Bond Types."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to MSCI World, 4% WR
    mask = (df["Equity"] == "MSCI World") & (df["WR"] == 4.0)
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Bond Type comparison plot")
        return

    # Pivot for grouped bar chart
    pivot = subset.pivot(index="Allocation", columns="Bond", values="Success_Rate")

    # Sort allocations
    alloc_order = ["60/40", "60/20/20", "70/30", "70/15/15", "80/20", "80/10/10",
                   "90/10", "90/5/5", "100"]
    pivot = pivot.reindex([a for a in alloc_order if a in pivot.index])

    pivot.plot(kind="bar", ax=ax, width=0.8)

    ax.set_xlabel("Portfolio Allocation", fontsize=12)
    ax.set_ylabel("Success Rate (%)", fontsize=12)
    ax.set_title("Success Rate by Bond Type\n(MSCI World, 4% WR)", fontsize=14)
    ax.set_ylim(70, 85)
    ax.legend(title="Bond Type")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig(output_dir / "04_success_rate_by_bond_type.png", dpi=150)
    plt.close()
    logger.info("Generated: 04_success_rate_by_bond_type.png")


def plot_heatmap_success_rate(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 5: Heatmap of Success Rate (Equity % vs Bond Type)."""
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)

    # Filter to 4% WR, single-bond portfolios
    mask = (df["WR"] == 4.0) & (~df["Bond"].str.contains(r"\+", na=False))
    subset = df[mask].copy()

    if subset.empty:
        logger.warning("No data for Heatmap plot")
        return

    # Create pivot table: rows = Equity Index + Bond, columns = Equity %
    subset["Row_Label"] = subset["Equity"] + " + " + subset["Bond"].fillna("-")
    pivot = subset.pivot_table(
        index="Row_Label", columns="Equity_Pct", values="Success_Rate", aggfunc="mean"
    )

    # Sort by mean success rate
    pivot = pivot.loc[pivot.mean(axis=1).sort_values(ascending=False).index]

    sns.heatmap(
        pivot,
        annot=True,
        fmt=".1f",
        cmap="RdYlGn",
        center=75,
        vmin=50,
        vmax=100,
        ax=ax,
        cbar_kws={"label": "Success Rate (%)"},
    )

    ax.set_xlabel("Equity Allocation (%)", fontsize=12)
    ax.set_ylabel("Portfolio (Equity + Bond)", fontsize=12)
    ax.set_title("Success Rate Heatmap (4% WR)", fontsize=14)

    plt.tight_layout()
    plt.savefig(output_dir / "05_heatmap_success_rate.png", dpi=150)
    plt.close()
    logger.info("Generated: 05_heatmap_success_rate.png")


def plot_final_value_distribution(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 6: Final Value Distribution (P5, Median, Mean, P95)."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to MSCI World + Bund, 4% WR
    mask = (df["Equity"] == "MSCI World") & (df["Bond"] == "Bund") & (df["WR"] == 4.0)
    subset = df[mask].sort_values("Equity_Pct").copy()

    if subset.empty:
        logger.warning("No data for Final Value Distribution plot")
        return

    x = np.arange(len(subset))
    width = 0.6

    # Plot as error bars with median as center
    medians = subset["Median_Final"] / 1e6  # Convert to millions
    means = subset["Mean_Final"] / 1e6
    p5 = subset["P5_Final"] / 1e6
    p95 = subset["P95_Final"] / 1e6

    # Error bar plot
    ax.errorbar(
        x, medians,
        yerr=[medians - p5, p95 - medians],
        fmt="o",
        markersize=10,
        capsize=5,
        capthick=2,
        color="steelblue",
        ecolor="steelblue",
        label="Median (P5-P95 range)"
    )
    ax.scatter(x, means, marker="D", s=80, color="darkred", zorder=5, label="Mean")

    ax.set_xticks(x)
    ax.set_xticklabels(subset["Allocation"])
    ax.set_xlabel("Portfolio Allocation", fontsize=12)
    ax.set_ylabel("Final Portfolio Value (€ millions)", fontsize=12)
    ax.set_title("Final Value Distribution\n(MSCI World + Bund, 4% WR)", fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Add horizontal line at initial value
    ax.axhline(y=1.0, color="gray", linestyle="--", alpha=0.5, label="Initial €1M")

    plt.tight_layout()
    plt.savefig(output_dir / "06_final_value_distribution.png", dpi=150)
    plt.close()
    logger.info("Generated: 06_final_value_distribution.png")


def plot_risk_return_tradeoff(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 7: Risk/Return Trade-off (Success Rate vs Median Final Value)."""
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)

    # Filter to 4% WR
    subset = df[df["WR"] == 4.0].copy()

    if subset.empty:
        logger.warning("No data for Risk/Return Trade-off plot")
        return

    # Color by equity index
    equity_indices = subset["Equity"].unique()
    colors = dict(zip(equity_indices, sns.color_palette("husl", len(equity_indices))))

    for equity in equity_indices:
        eq_data = subset[subset["Equity"] == equity]
        ax.scatter(
            eq_data["Success_Rate"],
            eq_data["Median_Final"] / 1e6,
            c=[colors[equity]],
            s=100,
            alpha=0.7,
            label=equity,
            edgecolors="white",
            linewidth=0.5,
        )

    ax.set_xlabel("Success Rate (%)", fontsize=12)
    ax.set_ylabel("Median Final Value (€ millions)", fontsize=12)
    ax.set_title("Risk/Return Trade-off (4% WR)\nHigher is better on both axes", fontsize=14)
    ax.legend(title="Equity Index", loc="upper left")
    ax.grid(True, alpha=0.3)

    # Add quadrant lines at median values
    median_sr = subset["Success_Rate"].median()
    median_fv = subset["Median_Final"].median() / 1e6
    ax.axvline(x=median_sr, color="gray", linestyle=":", alpha=0.5)
    ax.axhline(y=median_fv, color="gray", linestyle=":", alpha=0.5)

    plt.tight_layout()
    plt.savefig(output_dir / "07_risk_return_tradeoff.png", dpi=150)
    plt.close()
    logger.info("Generated: 07_risk_return_tradeoff.png")


def plot_depletion_year_analysis(df: pd.DataFrame, output_dir: Path) -> None:
    """Plot 8: Depletion Year Analysis for failed scenarios."""
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    # Filter to 4% WR with depletion data
    subset = df[(df["WR"] == 4.0) & (df["Mean_Depletion"].notna())].copy()

    if subset.empty:
        logger.warning("No data for Depletion Year Analysis plot")
        return

    # Left plot: Mean Depletion Year by Equity Index
    ax1 = axes[0]
    depletion_by_equity = subset.groupby("Equity")["Mean_Depletion"].mean().sort_values()
    bars = ax1.barh(depletion_by_equity.index, depletion_by_equity.values, color="coral")
    ax1.set_xlabel("Mean Depletion Year", fontsize=12)
    ax1.set_ylabel("Equity Index", fontsize=12)
    ax1.set_title("Mean Depletion Year by Equity Index\n(4% WR, Failed Scenarios)", fontsize=12)
    ax1.set_xlim(20, 30)

    for bar, val in zip(bars, depletion_by_equity.values):
        ax1.text(val + 0.2, bar.get_y() + bar.get_height() / 2, f"{val:.1f}", va="center")

    # Right plot: Min vs Mean vs Median Depletion for MSCI World
    ax2 = axes[1]
    msci_world = subset[subset["Equity"] == "MSCI World"].sort_values("Equity_Pct")

    if not msci_world.empty:
        x = np.arange(len(msci_world))
        width = 0.25

        ax2.bar(x - width, msci_world["Min_Depletion"], width, label="Min", color="red", alpha=0.7)
        ax2.bar(x, msci_world["Mean_Depletion"], width, label="Mean", color="orange", alpha=0.7)
        ax2.bar(x + width, msci_world["Median_Depletion"], width, label="Median", color="green", alpha=0.7)

        ax2.set_xticks(x)
        ax2.set_xticklabels(msci_world["Allocation"], rotation=45, ha="right")
        ax2.set_xlabel("Portfolio Allocation", fontsize=12)
        ax2.set_ylabel("Depletion Year", fontsize=12)
        ax2.set_title("Depletion Year Statistics\n(MSCI World, 4% WR)", fontsize=12)
        ax2.legend()
        ax2.set_ylim(0, 30)
        ax2.axhline(y=30, color="gray", linestyle="--", alpha=0.5, label="30-year horizon")

    plt.tight_layout()
    plt.savefig(output_dir / "08_depletion_year_analysis.png", dpi=150)
    plt.close()
    logger.info("Generated: 08_depletion_year_analysis.png")


def plot_wr_comparison_summary(df: pd.DataFrame, output_dir: Path) -> None:
    """Bonus Plot: Summary comparison of all withdrawal rates."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Filter to MSCI World + Bund 60/40 across all WRs
    mask = (
        (df["Equity"] == "MSCI World") &
        (df["Bond"] == "Bund") &
        (df["Allocation"] == "60/40")
    )
    subset = df[mask].sort_values("WR").copy()

    if len(subset) < 2:
        # Try with any MSCI World 60/40
        mask = (df["Equity"] == "MSCI World") & (df["Equity_Pct"] == 60)
        subset = df[mask].drop_duplicates(subset=["WR"]).sort_values("WR").copy()

    if subset.empty:
        logger.warning("No data for WR Comparison Summary plot")
        return

    x = np.arange(len(subset))
    width = 0.35

    # Create twin axis for final value
    ax2 = ax.twinx()

    bars1 = ax.bar(x - width/2, subset["Success_Rate"], width, label="Success Rate", color="steelblue")
    bars2 = ax2.bar(x + width/2, subset["Median_Final"] / 1e6, width, label="Median Final Value", color="darkgreen")

    ax.set_xlabel("Withdrawal Rate", fontsize=12)
    ax.set_ylabel("Success Rate (%)", fontsize=12, color="steelblue")
    ax2.set_ylabel("Median Final Value (€ millions)", fontsize=12, color="darkgreen")
    ax.set_title("Withdrawal Rate Impact Summary\n(MSCI World + Bund 60/40)", fontsize=14)

    ax.set_xticks(x)
    ax.set_xticklabels([f"{wr:g}%" for wr in subset["WR"]])
    ax.set_ylim(0, 100)
    ax.tick_params(axis="y", labelcolor="steelblue")
    ax2.tick_params(axis="y", labelcolor="darkgreen")

    # Add value labels
    for bar, val in zip(bars1, subset["Success_Rate"]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{val:.1f}%",
                ha="center", va="bottom", fontsize=10, color="steelblue")
    for bar, val in zip(bars2, subset["Median_Final"] / 1e6):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f"€{val:.1f}M",
                 ha="center", va="bottom", fontsize=10, color="darkgreen")

    # Combined legend
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="lower left")

    plt.tight_layout()
    plt.savefig(output_dir / "09_wr_comparison_summary.png", dpi=150)
    plt.close()
    logger.info("Generated: 09_wr_comparison_summary.png")


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

    plot_success_rate_vs_withdrawal_rate(df, args.output_dir)
    plot_success_rate_vs_allocation(df, args.output_dir)
    plot_success_rate_by_equity_index(df, args.output_dir)
    plot_success_rate_by_bond_type(df, args.output_dir)
    plot_heatmap_success_rate(df, args.output_dir)
    plot_final_value_distribution(df, args.output_dir)
    plot_risk_return_tradeoff(df, args.output_dir)
    plot_depletion_year_analysis(df, args.output_dir)
    plot_wr_comparison_summary(df, args.output_dir)

    logger.info("All plots generated successfully!")
    return 0


if __name__ == "__main__":
    exit(main())
