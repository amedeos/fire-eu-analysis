# Notebooks in the src directory

This directory contains Jupyter notebooks for financial data analysis and Monte Carlo simulations to calculate the Safe Withdrawal Rate (SWR).

## Data Extraction and Preparation Notebooks

| Notebook | Description |
|----------|-------------|
| [01_hicp_midx.ipynb](01_hicp_midx.ipynb) | Extracts HICP (Harmonised Index of Consumer Prices) data from Eurostat for various European countries (Italy, Germany, France, Spain, UK, etc.) with base 1996=100. Generates individual and combined plots. |
| [02_msci.ipynb](02_msci.ipynb) | Downloads MSCI indices (ACWI, World, Europe, EMU and individual countries) from GitHub, filling missing days using backward fill. |
| [03_bdi.ipynb](03_bdi.ipynb) | Extracts 10-year BTP benchmark (MFN_BMK.M.020.922.0.EUR.210) monthly and daily data from Banca d'Italia. |
| [04_bund.ipynb](04_bund.ipynb) | Extracts daily 10-year German Bund yields (BBSIS) from Bundesbank. |
| [05_oat.ipynb](05_oat.ipynb) | Extracts daily and monthly 10-year French OAT yields from Banque de France. |
| [06_ecb.ipynb](06_ecb.ipynb) | Extracts long-term interest rates (10 years) from ECB for Italy, Germany and France. |
| [07_oat_ecb.ipynb](07_oat_ecb.ipynb) | Analysis and backcasting of French OAT yields using ECB data to extend the historical series to the 2000-2004 period. |
| [08_oat_fr10.ipynb](08_oat_fr10.ipynb) | Analysis and backcasting of French OAT yields using FR10YT_RR data to extend the historical series to the 2000-2004 period. |
| [09_stoxx_sxxgr.ipynb](09_stoxx_sxxgr.ipynb) | Downloads and merges STOXX Europe 600 (SXXGR) data from Yahoo Finance (1986-2015) and Investing.com (2012-2025). |
| [10_istat_foi.ipynb](10_istat_foi.ipynb) | Downloads and merges FOI (consumer price index for blue and white-collar worker households) data from ISTAT with splicing to base 1995=100. |
| [11_istat_nic.ipynb](11_istat_nic.ipynb) | Extracts and merges NIC (national consumer price index) data from ISTAT for the period 1996-2025. |

## Monte Carlo Simulation Notebooks (Block Bootstrap)

These notebooks perform Monte Carlo simulations using block bootstrap methodology to analyze the Safe Withdrawal Rate (SWR) over a 30-year horizon.

### MSCI World + Bund Portfolios (No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [20_block_notax_i_hicp_m_world_b_de_6040.ipynb](20_block_notax_i_hicp_m_world_b_de_6040.ipynb) | 60% MSCI World + 40% Bund | SWR simulation with Euro area HICP inflation |
| [21_block_notax_i_hicp_m_world_b_de_7030.ipynb](21_block_notax_i_hicp_m_world_b_de_7030.ipynb) | 70% MSCI World + 30% Bund | SWR simulation with Euro area HICP inflation |
| [22_block_notax_i_hicp_m_world_b_de_8020.ipynb](22_block_notax_i_hicp_m_world_b_de_8020.ipynb) | 80% MSCI World + 20% Bund | SWR simulation with Euro area HICP inflation |
| [23_block_notax_i_hicp_m_world_b_de_9010.ipynb](23_block_notax_i_hicp_m_world_b_de_9010.ipynb) | 90% MSCI World + 10% Bund | SWR simulation with Euro area HICP inflation |
| [24_block_notax_i_hicp_m_world_b_de_1000.ipynb](24_block_notax_i_hicp_m_world_b_de_1000.ipynb) | 100% MSCI World | SWR simulation with Euro area HICP inflation |

### MSCI World + BTP Portfolios (No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [25_block_notax_i_hicp_m_world_b_it_6040.ipynb](25_block_notax_i_hicp_m_world_b_it_6040.ipynb) | 60% MSCI World + 40% BTP | SWR simulation with Euro area HICP inflation |
| [26_block_notax_i_hicp_m_world_b_it_7030.ipynb](26_block_notax_i_hicp_m_world_b_it_7030.ipynb) | 70% MSCI World + 30% BTP | SWR simulation with Euro area HICP inflation |
| [27_block_notax_i_hicp_m_world_b_it_8020.ipynb](27_block_notax_i_hicp_m_world_b_it_8020.ipynb) | 80% MSCI World + 20% BTP | SWR simulation with Euro area HICP inflation |
| [28_block_notax_i_hicp_m_world_b_it_9010.ipynb](28_block_notax_i_hicp_m_world_b_it_9010.ipynb) | 90% MSCI World + 10% BTP | SWR simulation with Euro area HICP inflation |

### MSCI World + Bund + BTP Portfolios (No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [30_block_notax_i_hicp_m_world_b_deit_602020.ipynb](30_block_notax_i_hicp_m_world_b_deit_602020.ipynb) | 60% MSCI World + 20% Bund + 20% BTP | SWR simulation with Euro area HICP inflation |
| [31_block_notax_i_hicp_m_world_b_deit_701515.ipynb](31_block_notax_i_hicp_m_world_b_deit_701515.ipynb) | 70% MSCI World + 15% Bund + 15% BTP | SWR simulation with Euro area HICP inflation |
| [32_block_notax_i_hicp_m_world_b_deit_801010.ipynb](32_block_notax_i_hicp_m_world_b_deit_801010.ipynb) | 80% MSCI World + 10% Bund + 10% BTP | SWR simulation with Euro area HICP inflation |
| [33_block_notax_i_hicp_m_world_b_deit_900505.ipynb](33_block_notax_i_hicp_m_world_b_deit_900505.ipynb) | 90% MSCI World + 5% Bund + 5% BTP | SWR simulation with Euro area HICP inflation |

### MSCI ACWI + Bund Portfolios (No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [34_block_notax_i_hicp_m_acwi_b_de_6040.ipynb](34_block_notax_i_hicp_m_acwi_b_de_6040.ipynb) | 60% MSCI ACWI + 40% Bund | SWR simulation with Euro area HICP inflation |
| [35_block_notax_i_hicp_m_acwi_b_de_7030.ipynb](35_block_notax_i_hicp_m_acwi_b_de_7030.ipynb) | 70% MSCI ACWI + 30% Bund | SWR simulation with Euro area HICP inflation |
| [36_block_notax_i_hicp_m_acwi_b_de_8020.ipynb](36_block_notax_i_hicp_m_acwi_b_de_8020.ipynb) | 80% MSCI ACWI + 20% Bund | SWR simulation with Euro area HICP inflation |
| [37_block_notax_i_hicp_m_acwi_b_de_9010.ipynb](37_block_notax_i_hicp_m_acwi_b_de_9010.ipynb) | 90% MSCI ACWI + 10% Bund | SWR simulation with Euro area HICP inflation |
| [38_block_notax_i_hicp_m_acwi_b_de_1000.ipynb](38_block_notax_i_hicp_m_acwi_b_de_1000.ipynb) | 100% MSCI ACWI | SWR simulation with Euro area HICP inflation |

### MSCI ACWI + BTP Portfolios (No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [39_block_notax_i_hicp_m_acwi_b_it_6040.ipynb](39_block_notax_i_hicp_m_acwi_b_it_6040.ipynb) | 60% MSCI ACWI + 40% BTP | SWR simulation with Euro area HICP inflation |
| [40_block_notax_i_hicp_m_acwi_b_it_7030.ipynb](40_block_notax_i_hicp_m_acwi_b_it_7030.ipynb) | 70% MSCI ACWI + 30% BTP | SWR simulation with Euro area HICP inflation |
| [41_block_notax_i_hicp_m_acwi_b_it_8020.ipynb](41_block_notax_i_hicp_m_acwi_b_it_8020.ipynb) | 80% MSCI ACWI + 20% BTP | SWR simulation with Euro area HICP inflation |
| [42_block_notax_i_hicp_m_acwi_b_it_9010.ipynb](42_block_notax_i_hicp_m_acwi_b_it_9010.ipynb) | 90% MSCI ACWI + 10% BTP | SWR simulation with Euro area HICP inflation |

### MSCI ACWI + Bund + BTP Portfolios (No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [43_block_notax_i_hicp_m_acwi_b_deit_602020.ipynb](43_block_notax_i_hicp_m_acwi_b_deit_602020.ipynb) | 60% MSCI ACWI + 20% Bund + 20% BTP | SWR simulation with Euro area HICP inflation |
| [44_block_notax_i_hicp_m_acwi_b_deit_701515.ipynb](44_block_notax_i_hicp_m_acwi_b_deit_701515.ipynb) | 70% MSCI ACWI + 15% Bund + 15% BTP | SWR simulation with Euro area HICP inflation |
| [45_block_notax_i_hicp_m_acwi_b_deit_801010.ipynb](45_block_notax_i_hicp_m_acwi_b_deit_801010.ipynb) | 80% MSCI ACWI + 10% Bund + 10% BTP | SWR simulation with Euro area HICP inflation |
| [46_block_notax_i_hicp_m_acwi_b_deit_900505.ipynb](46_block_notax_i_hicp_m_acwi_b_deit_900505.ipynb) | 90% MSCI ACWI + 5% Bund + 5% BTP | SWR simulation with Euro area HICP inflation |

## Simulation Methodology

### Block Bootstrap
The simulations use the **block bootstrap** methodology which preserves temporal structure and correlations in financial data:
1. Sampling **consecutive blocks** of historical data (default: 6 months)
2. Randomly concatenating blocks to create simulated future scenarios
3. Maintaining serial correlation and regime persistence

### Key Features
- **100,000 simulations** for robust statistical estimates
- **Time horizon**: 30 years
- **Inflation adjustment**: withdrawals adjusted with Euro area HICP
- **Calendar days**: calculations based on 365 days/year
- **No taxation**: withdrawals are not subject to capital gains tax

### Simulation Outputs
- Success rate (probability that the portfolio survives 30 years)
- Portfolio evolution with percentile bands (5th, 25th, 50th, 75th, 95th)
- Sensitivity analysis for different withdrawal rates (2%-5%)
- Distribution of depletion years for failed scenarios
