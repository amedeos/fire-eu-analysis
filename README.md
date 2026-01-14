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

## 🧩 Project Overview

This repository contains the code, processed data (when allowed), and statistical analyses developed for the thesis *"Retirement-oriented wealth management: the 4% rule and the FIRE (Financial Independence, Retire Early) movement. A European and Italian case study."*

The goal is to assess the sustainability of withdrawal rate strategies—especially the 4% rule—using historical simulations, stochastic modelling, and risk metrics applied to European markets.

---

## 📈 Key Results

Summary of Monte Carlo simulation results (100,000 runs, 30-year horizon, block bootstrap):

### Success Rates by Index and Withdrawal Rate (60/40 with Bund)

| Equity Index | 3% WR | 3.5% WR | 4% WR |
|--------------|-------|---------|-------|
| MSCI World | 95.8% | 89.1% | 78.3% |
| MSCI ACWI | 95.3% | 88.1% | 77.0% |
| MSCI Europe | 90.1% | 79.2% | 65.0% |
| MSCI EMU | 86.2% | 74.7% | 60.9% |

### Bond Strategy Comparison (60% Equity, 4% WR)

| Bond Type | MSCI World | MSCI Europe | Advantage |
|-----------|------------|-------------|-----------|
| Bund | 78.3% | 65.0% | Baseline |
| BTP | 80.5% | 67.9% | +2% |
| Bund+BTP Mix | 79.9% | 66.8% | +1.5% |

**Key findings:**
1. **The 4% rule doesn't work well in Europe** - success rates are 65-80% vs US ~95%
2. **3-3.5% WR is more appropriate** for European investors
3. **Global diversification matters** - World/ACWI outperform Europe/EMU by 10-15%
4. **BTP outperforms Bund** at higher WRs due to yield advantage (+2%)
5. **Allocation matters less than WR** - 60/40 to 80/20 have similar outcomes
6. **Home bias is costly** - European-only portfolios have significantly lower success rates

For complete results, see [ANALYSIS_REGISTRY.md](ANALYSIS_REGISTRY.md).

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [src/README.md](src/README.md) | Complete list of Jupyter notebooks with descriptions and naming conventions |
| [ANALYSIS_REGISTRY.md](ANALYSIS_REGISTRY.md) | Summary table of simulation results (success rates, final values, depletion years) |
| [ANALYSIS_REGISTRY.csv](ANALYSIS_REGISTRY.csv) | Same data in CSV format for further analysis |
| [plots/README.md](plots/README.md) | Documentation for 34 analysis plots with key insights |

---

## 📁 Repository Structure

```
fire-eu-analysis/
│
├── data/                    # Raw and processed datasets
│   ├── msci/                # MSCI index data
│   ├── bdi/                 # Banca d'Italia (BTP yields)
│   ├── bund/                # Bundesbank (Bund yields)
│   ├── oat/                 # French OAT yields
│   ├── eurostat/            # HICP inflation data
│   ├── istat/               # Italian inflation (FOI, NIC)
│   └── stoxx/               # STOXX Europe 600 data
│
├── src/                     # Jupyter notebooks
│   ├── 00xx_*.ipynb         # Data extraction and preprocessing
│   ├── 01xx_*.ipynb         # MSCI World simulations (4% WR)
│   ├── 02xx_*.ipynb         # MSCI ACWI simulations (4% WR)
│   ├── 03xx_*.ipynb         # STOXX Europe 600 simulations (4% WR)
│   ├── 04xx_*.ipynb         # MSCI Europe simulations (4% WR)
│   ├── 05xx_*.ipynb         # MSCI EMU simulations (4% WR)
│   ├── 06xx_*.ipynb         # MSCI World simulations (3% WR)
│   ├── 07xx_*.ipynb         # MSCI World simulations (3.5% WR)
│   ├── 08xx_*.ipynb         # MSCI ACWI simulations (3% WR)
│   ├── 09xx_*.ipynb         # MSCI ACWI simulations (3.5% WR)
│   ├── 10xx_*.ipynb         # MSCI Europe simulations (3% WR)
│   ├── 11xx_*.ipynb         # MSCI Europe simulations (3.5% WR)
│   ├── 12xx_*.ipynb         # MSCI EMU simulations (3% WR)
│   ├── 13xx_*.ipynb         # MSCI EMU simulations (3.5% WR)
│   └── tools/               # Utility scripts
│       ├── buildtable.py    # Generate ANALYSIS_REGISTRY.md/.csv
│       └── plots.py         # Generate 34 analysis plots
│
├── plots/                   # 34 generated analysis plots
│   ├── 01-08_*.png          # General analysis (success rates, heatmaps)
│   ├── 09-14_*.png          # Depletion analysis (when portfolios fail)
│   ├── 15-20_*.png          # 4% WR specific analysis
│   ├── 21-26_*.png          # 3% WR specific analysis
│   ├── 27-32_*.png          # 3.5% WR specific analysis
│   └── 33-34_*.png          # Optimal bond strategy analysis
│
├── fire.sh                  # Podman container management script
├── ANALYSIS_REGISTRY.md     # Auto-generated results summary
├── ANALYSIS_REGISTRY.csv    # Results in CSV format
└── README.md
```

---

## ▶️ How to Run the Project (Podman Required)

The recommended way to start the analysis environment is through the Podman-based script:

### Requirements

* **Podman** installed on the host
* Optional: GPU support (the script auto-detects it)

### Start the project

```bash
./fire.sh start              # Auto-detect GPU/CPU
./fire.sh start --gpu        # Force GPU mode
./fire.sh start --cpu        # Force CPU mode
./fire.sh stop               # Stop container
```

The script will:
- Detect whether the host supports GPU
- Start the appropriate container (GPU-enabled or CPU-only)
- Launch Jupyter Lab inside the container
- Expose the notebook environment on localhost

### Utility Scripts

Run inside the container or via `podman exec`:

```bash
# Generate ANALYSIS_REGISTRY.md and .csv from notebook outputs
python src/tools/buildtable.py

# Generate analysis plots
python src/tools/plots.py
```

---

## 🔬 Simulation Methodology

### Block Bootstrap Monte Carlo

The simulations use **block bootstrap** methodology which preserves temporal structure and correlations in financial data:

1. Sample **consecutive blocks** of historical data (6-month blocks)
2. Randomly concatenate blocks to create simulated 30-year scenarios
3. Maintain serial correlation and regime persistence

### Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Number of simulations | 100,000 |
| Time horizon | 30 years |
| Block size | 6 months |
| Historical data | 2000-2025 |
| Withdrawal rates tested | 3%, 3.5%, 4% |
| Inflation adjustment | HICP Euro Area (lagged) |
| Rebalancing | Annual |

### Portfolio Configurations

- **Equity indices:** MSCI World, MSCI ACWI, MSCI Europe, MSCI EMU
- **Bond instruments:** German Bund 10Y, Italian BTP 10Y, mixed portfolios
- **Allocations:** 60/40, 70/30, 80/20, 90/10, 100/0

---

## 📚 Data Sources

The project uses:

* **MSCI** – equity indices (World, ACWI, Europe, EMU)
* **Eurostat** – HICP inflation data
* **ISTAT** – Italian inflation (FOI, NIC)
* **Bundesbank** – German Bund 10Y yields
* **Banca d'Italia** – Italian BTP 10Y yields
* **Banque de France** – French OAT 10Y yields

> **Note:** Some datasets cannot be included due to licensing restrictions. Only scripts and derived data (when permitted) are stored in the repository.

---

## 🛠️ Technologies

* **Python 3.12+**
* Main dependencies:
  * `pandas`, `numpy`, `scipy` – data manipulation and statistics
  * `matplotlib`, `seaborn` – visualization
  * `statsmodels` – statistical models
  * `joblib` – parallel processing
  * `nbformat` – notebook parsing
* **Podman** for reproducible execution environment
* Optional GPU acceleration for simulations

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
Universitas Mercatorum – BSc in Statistics and Big Data
