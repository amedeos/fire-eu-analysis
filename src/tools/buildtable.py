#!/usr/bin/env python3
"""
Build ANALYSIS_REGISTRY.md from notebook outputs.

Scans all notebooks in src/ with prefixes 01xx, 02xx, 03xx, 04xx, etc.
and extracts simulation results to generate a comprehensive registry.
"""

import argparse
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import nbformat

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class NotebookData:
    """Data extracted from a single notebook."""

    notebook_id: str
    notebook_name: str
    description: str = ""
    tax_status: str = ""
    equity_index: str = ""
    equity_weight: float = 0.0
    bonds: list[tuple[str, float]] = field(default_factory=list)
    inflation_series: str = ""
    data_from: str = ""
    data_to: str = ""
    n_simulations: int = 0
    block_size_months: int = 0
    withdrawal_rate: float = 0.0
    success_rate: float = 0.0
    median_final_value: int = 0
    mean_final_value: int = 0
    p5_final_value: int = 0
    p95_final_value: int = 0
    failed_simulations: int = 0
    failed_simulations_pct: float = 0.0
    median_depletion_year: int | None = None
    mean_depletion_year: float | None = None
    min_depletion_year: int | None = None


# Mapping of asset codes to display names
EQUITY_DISPLAY_NAMES = {
    "MSCI_WORLD": "MSCI World",
    "MSCI_ACWI": "MSCI ACWI",
    "STOXX_600": "STOXX 600",
    "STOXX_SXXGR": "STOXX 600",
    "MSCI_EUROPE": "MSCI Europe",
    "MSCI_EMU": "MSCI EMU",
}

BOND_DISPLAY_NAMES = {
    "BUND_10Y": "Bund 10Y",
    "BTP_10Y": "BTP 10Y",
    "OAT_10Y": "OAT 10Y",
}

INFLATION_DISPLAY_NAMES = {
    "HICP_EU": "HICP Euro Area",
    "HICP_IT": "HICP Italy",
    "FOI_IT": "FOI Italy",
    "NIC_IT": "NIC Italy",
}

# Mapping of notebook prefixes to equity index families
FAMILY_NAMES = {
    "01": "MSCI World NET",
    "02": "MSCI ACWI NET",
    "03": "STOXX Europe 600",
    "04": "MSCI Europe NET",
    "05": "MSCI EMU NET",
    "06": "MSCI World NET (3% WR)",
}


def parse_currency(value: str) -> int:
    """Parse a currency string like '€1,234,567' or '1,234,567' to int."""
    cleaned = re.sub(r"[€,\s]", "", value)
    return int(cleaned)


def extract_notebook_data(notebook_path: Path) -> NotebookData | None:
    """Extract data from a single notebook."""
    try:
        with open(notebook_path, encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
    except Exception as e:
        logger.warning(f"Failed to read {notebook_path.name}: {e}")
        return None

    notebook_name = notebook_path.stem
    notebook_id = notebook_name[:4]

    data = NotebookData(notebook_id=notebook_id, notebook_name=notebook_name)

    # Extract from first markdown cell (title and description)
    if nb.cells and nb.cells[0].cell_type == "markdown":
        first_cell = nb.cells[0].source

        # Extract description from title
        # Pattern: # Safe Withdrawal Rate Analysis: <DESCRIPTION> (No Tax|With Tax)
        title_match = re.search(
            r"#\s*Safe Withdrawal Rate Analysis:\s*(.+?)\s*\((No Tax|With Tax)\)",
            first_cell,
        )
        if title_match:
            data.description = title_match.group(1).strip()
            data.tax_status = title_match.group(2)
        else:
            # Try without tax status in title
            title_match = re.search(
                r"#\s*Safe Withdrawal Rate Analysis:\s*(.+?)(?:\n|$)", first_cell
            )
            if title_match:
                data.description = title_match.group(1).strip()

    # Find code cells with relevant output
    output_text = ""
    depletion_percentiles_text = ""
    depletion_stats_text = ""
    results_text = ""
    for i in range(len(nb.cells) - 1, -1, -1):
        cell = nb.cells[i]
        if cell.cell_type == "code" and cell.outputs:
            for out in cell.outputs:
                if out.output_type == "stream" and hasattr(out, "text"):
                    if "MONTE CARLO SIMULATION SUMMARY" in out.text and not output_text:
                        output_text = out.text
                    if "DEPLETION YEAR PERCENTILES" in out.text and not depletion_percentiles_text:
                        depletion_percentiles_text = out.text
                    if "Basic Depletion Statistics" in out.text and not depletion_stats_text:
                        depletion_stats_text = out.text
                    if "Mean final value" in out.text and not results_text:
                        results_text = out.text

    if not output_text:
        logger.warning(f"No simulation output found in {notebook_path.name}")
        return data

    # Parse simulation output
    _parse_simulation_output(data, output_text)

    # Parse depletion year details if found
    if depletion_percentiles_text:
        _parse_depletion_percentiles(data, depletion_percentiles_text)
    if depletion_stats_text:
        _parse_depletion_stats(data, depletion_stats_text)
    if results_text:
        _parse_results_output(data, results_text)

    return data


def _parse_simulation_output(data: NotebookData, text: str) -> None:
    """Parse the MONTE CARLO SIMULATION SUMMARY output."""

    # Number of simulations
    match = re.search(r"Number of simulations:\s*([\d,]+)", text)
    if match:
        data.n_simulations = int(match.group(1).replace(",", ""))

    # Block size
    match = re.search(r"Block size:\s*(\d+)\s*months?", text)
    if match:
        data.block_size_months = int(match.group(1))

    # Withdrawal rate
    match = re.search(r"Withdrawal rate:\s*([\d.]+)%", text)
    if match:
        data.withdrawal_rate = float(match.group(1))

    # Tax status from output if not found in title
    if not data.tax_status:
        if "tax-free" in text.lower() or "no capital gains tax" in text.lower():
            data.tax_status = "No Tax"
        elif "capital gains tax" in text.lower():
            data.tax_status = "With Tax"

    # Portfolio composition
    composition_match = re.search(
        r"Portfolio composition:\s*((?:\s*-\s*\w+:\s*[\d.]+%\s*)+)", text, re.MULTILINE
    )
    if composition_match:
        assets = re.findall(r"-\s*(\w+):\s*([\d.]+)%", composition_match.group(1))
        for asset, weight in assets:
            weight_float = float(weight)
            # Determine if equity or bond
            if any(eq in asset.upper() for eq in ["MSCI", "STOXX", "ACWI"]):
                data.equity_index = asset
                data.equity_weight = weight_float
            else:
                data.bonds.append((asset, weight_float))

    # Inflation series
    match = re.search(r"Inflation series:\s*(\w+)", text)
    if match:
        data.inflation_series = match.group(1)

    # Historical data period
    match = re.search(r"From:\s*(\d{4}-\d{2}-\d{2})", text)
    if match:
        data.data_from = match.group(1)

    match = re.search(r"To:\s*(\d{4}-\d{2}-\d{2})", text)
    if match:
        data.data_to = match.group(1)

    # Results
    match = re.search(r"Success rate:\s*([\d.]+)%", text)
    if match:
        data.success_rate = float(match.group(1))

    match = re.search(r"Median final value:\s*€([\d,]+)", text)
    if match:
        data.median_final_value = parse_currency(match.group(1))

    match = re.search(r"Mean final value:\s*€([\d,]+)", text)
    if match:
        data.mean_final_value = parse_currency(match.group(1))

    match = re.search(r"P5 final value:\s*€([\d,]+)", text)
    if match:
        data.p5_final_value = parse_currency(match.group(1))

    match = re.search(r"P95 final value:\s*€([\d,]+)", text)
    if match:
        data.p95_final_value = parse_currency(match.group(1))

    match = re.search(r"Failed simulations:\s*([\d,]+)\s*\(([\d.]+)%\)", text)
    if match:
        data.failed_simulations = int(match.group(1).replace(",", ""))
        data.failed_simulations_pct = float(match.group(2))

    match = re.search(r"Median depletion year:\s*(\d+)", text)
    if match:
        data.median_depletion_year = int(match.group(1))

def _parse_depletion_percentiles(data: NotebookData, text: str) -> None:
    """Parse the DEPLETION YEAR PERCENTILES output for min depletion year."""
    match = re.search(r"Min depletion year:\s*(\d+)", text)
    if match:
        data.min_depletion_year = int(match.group(1))


def _parse_depletion_stats(data: NotebookData, text: str) -> None:
    """Parse the Basic Depletion Statistics output for mean depletion year."""
    match = re.search(r"Mean depletion year:\s*([\d.]+)", text)
    if match:
        data.mean_depletion_year = float(match.group(1))


def _parse_results_output(data: NotebookData, text: str) -> None:
    """Parse the Results output for mean final value."""
    match = re.search(r"Mean final value:\s*€([\d,]+)", text)
    if match:
        data.mean_final_value = parse_currency(match.group(1))


def get_display_name(code: str, mapping: dict[str, str]) -> str:
    """Get display name from code, using mapping or returning code as-is."""
    return mapping.get(code, code)


def format_bond_string(bonds: list[tuple[str, float]]) -> str:
    """Format bonds list into a display string."""
    if not bonds:
        return "-"
    parts = []
    for bond, weight in bonds:
        display_name = get_display_name(bond, BOND_DISPLAY_NAMES)
        parts.append(f"{display_name} ({weight:.0f}%)")
    return " + ".join(parts)


def format_bond_short(bonds: list[tuple[str, float]]) -> str:
    """Format bonds list into a short display string for summary table."""
    if not bonds:
        return "-"
    # Extract just bond type abbreviations
    bond_types = []
    for bond, _ in bonds:
        if "BUND" in bond.upper():
            bond_types.append("Bund")
        elif "BTP" in bond.upper():
            bond_types.append("BTP")
        elif "OAT" in bond.upper():
            bond_types.append("OAT")
        else:
            bond_types.append(bond)
    return "+".join(bond_types)


def format_allocation(equity_weight: float, bonds: list[tuple[str, float]]) -> str:
    """Format allocation as string like '60/40' or '60/20/20'."""
    parts = [f"{equity_weight:.0f}"]
    for _, weight in bonds:
        parts.append(f"{weight:.0f}")
    return "/".join(parts)


def format_currency(value: int) -> str:
    """Format integer as currency string."""
    return f"€{value:,}"


def generate_registry(
    notebooks: list[NotebookData], output_path: Path, src_dir: Path
) -> None:
    """Generate the ANALYSIS_REGISTRY.md file."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get common parameters from first notebook
    first_nb = notebooks[0] if notebooks else None
    n_simulations = first_nb.n_simulations if first_nb else 100_000
    block_size = first_nb.block_size_months if first_nb else 6

    lines = [
        "# Analysis Registry",
        "",
        f"> Auto-generated from notebooks on {now}",
        "",
        "## Methodology Summary",
        "",
        "| Parameter | Value |",
        "|-----------|-------|",
        "| Simulation method | Block Bootstrap |",
        f"| Block size | {block_size} months |",
        f"| N. simulations | {n_simulations:,} |",
        "| Time horizon | 30 years |",
        "| Inflation adjustment | Lagged (t-1) |",
        "| Return aggregation | Growth factor method |",
        "",
        "---",
        "",
        "## Summary Table",
        "",
        "| ID | Equity | Bond | Allocation | Inflation | Tax | WR | Success Rate | Median Final | Mean Final | Median Depletion | Mean Depletion | Min Depletion |",
        "|----|--------|------|------------|-----------|-----|----|--------------|--------------|------------|------------------|----------------|---------------|",
    ]

    # Sort notebooks by ID
    sorted_notebooks = sorted(notebooks, key=lambda n: n.notebook_id)

    for nb in sorted_notebooks:
        equity_display = get_display_name(nb.equity_index, EQUITY_DISPLAY_NAMES)
        bond_short = format_bond_short(nb.bonds)
        allocation = format_allocation(nb.equity_weight, nb.bonds)
        median_depletion = (
            str(nb.median_depletion_year) if nb.median_depletion_year else "-"
        )
        mean_depletion = (
            f"{nb.mean_depletion_year:.1f}" if nb.mean_depletion_year else "-"
        )
        min_depletion = str(nb.min_depletion_year) if nb.min_depletion_year else "-"

        wr_display = f"{nb.withdrawal_rate:.0f}%" if nb.withdrawal_rate else "-"
        lines.append(
            f"| {nb.notebook_id} | {equity_display} | {bond_short} | {allocation} | "
            f"{nb.inflation_series} | {nb.tax_status} | {wr_display} | {nb.success_rate:.2f}% | {format_currency(nb.median_final_value)} | "
            f"{format_currency(nb.mean_final_value)} | {median_depletion} | {mean_depletion} | {min_depletion} |"
        )

    lines.extend(["", "---", "", "## Detailed Analysis", ""])

    # Group notebooks by family (01xx, 02xx, etc.)
    families: dict[str, list[NotebookData]] = {}
    for nb in sorted_notebooks:
        family = nb.notebook_id[:2]
        if family not in families:
            families[family] = []
        families[family].append(nb)

    for family_prefix in sorted(families.keys()):
        family_notebooks = families[family_prefix]
        family_name = FAMILY_NAMES.get(family_prefix, f"Family {family_prefix}xx")

        lines.extend([f"### {family_prefix}xx – {family_name}", ""])

        for nb in family_notebooks:
            equity_display = get_display_name(nb.equity_index, EQUITY_DISPLAY_NAMES)
            inflation_display = get_display_name(
                nb.inflation_series, INFLATION_DISPLAY_NAMES
            )
            bond_display = format_bond_string(nb.bonds)

            # Build description from components if not available
            if nb.bonds:
                bond_parts = []
                for bond, weight in nb.bonds:
                    bond_name = get_display_name(bond, BOND_DISPLAY_NAMES)
                    bond_parts.append(f"{bond_name} {weight:.0f}%")
                short_desc = f"{equity_display} {nb.equity_weight:.0f}% + {' + '.join(bond_parts)}"
            else:
                short_desc = f"{equity_display} {nb.equity_weight:.0f}%"

            lines.extend(
                [
                    f"#### {nb.notebook_id} – {short_desc}",
                    "",
                    "| Parameter | Value |",
                    "|-----------|-------|",
                    f"| Notebook | [{nb.notebook_name}.ipynb](src/{nb.notebook_name}.ipynb) |",
                    f"| Description | {nb.description} |",
                    f"| Equity Index | {equity_display} ({nb.equity_weight:.0f}%) |",
                    f"| Bond | {bond_display if nb.bonds else '-'} |",
                    f"| Inflation | {inflation_display} |",
                    f"| Tax Status | {nb.tax_status} |",
                    f"| Data Period | {nb.data_from} → {nb.data_to} |",
                    f"| Simulations | {nb.n_simulations:,} |",
                    f"| Withdrawal Rate | {nb.withdrawal_rate:.1f}% |",
                    "",
                    f"**Results @ {nb.withdrawal_rate:.0f}% WR:**",
                    "",
                    "| Metric | Value |",
                    "|--------|-------|",
                    f"| Success Rate | {nb.success_rate:.2f}% |",
                    f"| Median Final Value | {format_currency(nb.median_final_value)} |",
                    f"| Mean Final Value | {format_currency(nb.mean_final_value)} |",
                    f"| P5 Final Value | {format_currency(nb.p5_final_value)} |",
                    f"| P95 Final Value | {format_currency(nb.p95_final_value)} |",
                    f"| Failed Simulations | {nb.failed_simulations:,} ({nb.failed_simulations_pct:.1f}%) |",
                ]
            )

            if nb.median_depletion_year:
                lines.append(f"| Median Depletion Year | {nb.median_depletion_year} |")
            else:
                lines.append("| Median Depletion Year | - |")

            if nb.mean_depletion_year:
                lines.append(f"| Mean Depletion Year | {nb.mean_depletion_year:.1f} |")
            else:
                lines.append("| Mean Depletion Year | - |")

            if nb.min_depletion_year:
                lines.append(f"| Min Depletion Year | {nb.min_depletion_year} |")
            else:
                lines.append("| Min Depletion Year | - |")

            lines.extend(["", "---", ""])

    # Write to file
    output_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Generated {output_path}")


def find_notebooks(src_dir: Path) -> list[Path]:
    """Find all analysis notebooks (01xx, 02xx, etc., excluding 00xx)."""
    notebooks = []
    for path in sorted(src_dir.glob("*.ipynb")):
        name = path.stem
        # Check if starts with 01-09 (excluding 00)
        if len(name) >= 4 and name[:2].isdigit() and name[:2] != "00":
            notebooks.append(path)
    return notebooks


def main():
    parser = argparse.ArgumentParser(
        description="Generate ANALYSIS_REGISTRY.md from notebook outputs"
    )
    parser.add_argument(
        "--src-dir",
        type=Path,
        default=Path("src"),
        help="Directory containing notebooks (default: src/)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("ANALYSIS_REGISTRY.md"),
        help="Output file path (default: ANALYSIS_REGISTRY.md)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Find notebooks
    notebooks_paths = find_notebooks(args.src_dir)
    if not notebooks_paths:
        logger.error(f"No analysis notebooks found in {args.src_dir}")
        return 1

    logger.info(f"Found {len(notebooks_paths)} notebooks")

    # Extract data from each notebook
    notebooks_data = []
    for path in notebooks_paths:
        logger.debug(f"Processing {path.name}")
        data = extract_notebook_data(path)
        if data:
            notebooks_data.append(data)

    if not notebooks_data:
        logger.error("No valid notebook data extracted")
        return 1

    logger.info(f"Extracted data from {len(notebooks_data)} notebooks")

    # Generate registry
    generate_registry(notebooks_data, args.output, args.src_dir)

    return 0


if __name__ == "__main__":
    exit(main())
