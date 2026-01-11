<h1 align="center">🔥 FIRE EU Analysis</h1>

<p align="center">
  <em>Quantitative FIRE analysis for European markets</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/python-3.12%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/container-ready-orange" alt="Container Ready">
  <a href="https://github.com/amedeos/fire-eu-analysis/actions">
    <img src="https://github.com/amedeos/fire-eu-analysis/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  </a>
</p>

---

# 📊 FIRE EU Analysis

Quantitative analysis for evaluating the sustainability of the 4% rule and FIRE strategies in Europe and Italy.

## 🧩 Project Overview

This repository contains the code, processed data (when allowed), and statistical analyses developed for the thesis *“Retirement-oriented wealth management: the 4% rule and the FIRE (Financial Independence, Retire Early) movement. A European and Italian case study.”*

The goal is to assess the sustainability of withdrawal rate strategies—especially the 4% rule—using historical simulations, stochastic modelling, and risk metrics applied to European markets.

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [src/README.md](src/README.md) | Complete list of Jupyter notebooks with descriptions and naming conventions |
| [ANALYSIS_REGISTRY.md](ANALYSIS_REGISTRY.md) | Summary table of simulation results (success rates, final values, depletion years) |
| [plots/README.md](plots/README.md) | Documentation for analysis plots with key insights |

---

## 📁 Repository Structure

```
fire-eu-analysis/
│
├── data/                # Raw and processed datasets (large files excluded)
├── src/                 # Jupyter notebooks for exploration and analysis
├── docs/                # Documentation, plots, thesis-related material
├── fire.sh              # Podman-based startup script
└── README.md
```

---

## ▶️ How to Run the Project (Podman Required)

The recommended way to start the analysis environment is through the Podman-based script:

### 1. Requirements

* **Podman** installed on the host
* Optional: GPU support (the script auto-detects it)

### 2. Start the project

```bash
./fire.sh start
```

The script will:

* Detect whether the host supports GPU
* Start the appropriate container (GPU-enabled or CPU-only)
* Launch Jupyter Lab inside the container
* Expose the notebook environment on localhost

A manual override flag is also available inside the script if you want to force GPU or CPU mode.

---

## 📚 Data Sources

The project uses:

* **MSCI** – equity indexes (Europe, EMU, individual countries)
* **STOXX Europe** – complementary equity benchmarks
* **ICE-BofA** – European bond indexes
* **Eurostat** – HICP, income, macroeconomic indicators
* **ISTAT** – Italian inflation
* **Government bonds** – BTP, Bund, OAT (daily or monthly data)
* **UCITS ETFs** – used as proxies when needed

> ⚠️ *Redistribution note:* Some datasets cannot be included due to licensing restrictions.
> Only scripts and derived data (when permitted) are stored in the repository.

---

## 🛠️ Technologies

* **Python 3.12+**
* Main dependencies:

  * `pandas`, `numpy`, `scipy`
  * `matplotlib`, `plotly`
  * `statsmodels`, `arch`
  * `yfinance` or dataset-specific loaders
* **Podman** for a reproducible execution environment
* Optional GPU acceleration for simulations

---

## 🔍 Analyses Included

### Historical Safe Withdrawal Rate (SWR)

* Rolling-window analysis (20–40 years)
* Failure/survival probability of withdrawal strategies
* European market comparison

### Stochastic & Econometric Modelling

* Monte Carlo simulations
* Volatility models (GARCH, etc.)
* Inflation modelling (HICP-based)

### Country-Level Comparison

* Real returns, volatility, inflation differences
* Implications for FIRE feasibility in Europe vs. Italy

### Evaluation of the “4% Rule”

* Suitability in European contexts
* Recommended withdrawal ranges
* Portfolio comparisons (60/40, equity-heavy, fixed income)

---

## 🤝 Contributing

Contributions are welcome, especially improvements to clarity, structure, reproducibility, or data pipelines.

---

## 📄 License — MIT License

This project is released under the **MIT License**, a permissive and widely used open-source license.
It allows reuse, modification, distribution, and commercial usage with minimal restrictions.

---

## 👤 Author

**Amedeo Salvati**
Università Mercatorum – BSc in Statistics and Big Data

