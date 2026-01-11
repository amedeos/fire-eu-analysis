# Notebooks in the src directory

This directory contains Jupyter notebooks for financial data analysis and Monte Carlo simulations to calculate the Safe Withdrawal Rate (SWR).

## Notebook Naming Convention

| Prefix | Category | Description |
|--------|----------|-------------|
| `00xx` | Data Preparation | Data extraction and preprocessing |
| `01xx` | MSCI World (4% WR) | Simulations with MSCI World NET index |
| `02xx` | MSCI ACWI (4% WR) | Simulations with MSCI ACWI NET index |
| `03xx` | STOXX SXXGR (4% WR) | Simulations with STOXX Europe 600 GR index |
| `04xx` | MSCI Europe (4% WR) | Simulations with MSCI Europe NET index |
| `05xx` | MSCI EMU (4% WR) | Simulations with MSCI EMU NET index |
| `06xx` | MSCI World (3% WR) | Simulations with MSCI World NET index, 3% withdrawal rate |
| `07xx` | MSCI World (3.5% WR) | Simulations with MSCI World NET index, 3.5% withdrawal rate |

## Data Extraction and Preparation Notebooks (00xx)

| Notebook | Description |
|----------|-------------|
| [0001_hicp_midx.ipynb](0001_hicp_midx.ipynb) | Extracts HICP (Harmonised Index of Consumer Prices) data from Eurostat for various European countries (Italy, Germany, France, Spain, UK, etc.) with base 1996=100. Generates individual and combined plots. |
| [0002_msci.ipynb](0002_msci.ipynb) | Downloads MSCI indices (ACWI, World, Europe, EMU and individual countries) from GitHub, filling missing days using backward fill. |
| [0003_bdi.ipynb](0003_bdi.ipynb) | Extracts 10-year BTP benchmark (MFN_BMK.M.020.922.0.EUR.210) monthly and daily data from Banca d'Italia. |
| [0004_bund.ipynb](0004_bund.ipynb) | Extracts daily 10-year German Bund yields (BBSIS) from Bundesbank. |
| [0005_oat.ipynb](0005_oat.ipynb) | Extracts daily and monthly 10-year French OAT yields from Banque de France. |
| [0006_ecb.ipynb](0006_ecb.ipynb) | Extracts long-term interest rates (10 years) from ECB for Italy, Germany and France. |
| [0007_oat_ecb.ipynb](0007_oat_ecb.ipynb) | Analysis and backcasting of French OAT yields using ECB data to extend the historical series to the 2000-2004 period. |
| [0008_oat_fr10.ipynb](0008_oat_fr10.ipynb) | Analysis and backcasting of French OAT yields using FR10YT_RR data to extend the historical series to the 2000-2004 period. |
| [0009_stoxx_sxxgr.ipynb](0009_stoxx_sxxgr.ipynb) | Downloads and merges STOXX Europe 600 (SXXGR) data from Yahoo Finance (1986-2015) and Investing.com (2012-2025). |
| [0010_istat_foi.ipynb](0010_istat_foi.ipynb) | Downloads and merges FOI (consumer price index for blue and white-collar worker households) data from ISTAT with splicing to base 1995=100. |
| [0011_istat_nic.ipynb](0011_istat_nic.ipynb) | Extracts and merges NIC (national consumer price index) data from ISTAT for the period 1996-2025. |

## Monte Carlo Simulation Notebooks (Block Bootstrap)

These notebooks perform Monte Carlo simulations using block bootstrap methodology to analyze the Safe Withdrawal Rate (SWR) over a 30-year horizon.

### MSCI World + Bund Portfolios (01xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0100_block_notax_i_hicp_m_world_b_de_6040.ipynb](0100_block_notax_i_hicp_m_world_b_de_6040.ipynb) | 60% MSCI World + 40% Bund | SWR simulation with Euro area HICP inflation |
| [0101_block_notax_i_hicp_m_world_b_de_7030.ipynb](0101_block_notax_i_hicp_m_world_b_de_7030.ipynb) | 70% MSCI World + 30% Bund | SWR simulation with Euro area HICP inflation |
| [0102_block_notax_i_hicp_m_world_b_de_8020.ipynb](0102_block_notax_i_hicp_m_world_b_de_8020.ipynb) | 80% MSCI World + 20% Bund | SWR simulation with Euro area HICP inflation |
| [0103_block_notax_i_hicp_m_world_b_de_9010.ipynb](0103_block_notax_i_hicp_m_world_b_de_9010.ipynb) | 90% MSCI World + 10% Bund | SWR simulation with Euro area HICP inflation |
| [0104_block_notax_i_hicp_m_world_b_de_1000.ipynb](0104_block_notax_i_hicp_m_world_b_de_1000.ipynb) | 100% MSCI World | SWR simulation with Euro area HICP inflation |

### MSCI World + BTP Portfolios (01xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0105_block_notax_i_hicp_m_world_b_it_6040.ipynb](0105_block_notax_i_hicp_m_world_b_it_6040.ipynb) | 60% MSCI World + 40% BTP | SWR simulation with Euro area HICP inflation |
| [0106_block_notax_i_hicp_m_world_b_it_7030.ipynb](0106_block_notax_i_hicp_m_world_b_it_7030.ipynb) | 70% MSCI World + 30% BTP | SWR simulation with Euro area HICP inflation |
| [0107_block_notax_i_hicp_m_world_b_it_8020.ipynb](0107_block_notax_i_hicp_m_world_b_it_8020.ipynb) | 80% MSCI World + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0108_block_notax_i_hicp_m_world_b_it_9010.ipynb](0108_block_notax_i_hicp_m_world_b_it_9010.ipynb) | 90% MSCI World + 10% BTP | SWR simulation with Euro area HICP inflation |

### MSCI World + Bund + BTP Portfolios (01xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0109_block_notax_i_hicp_m_world_b_deit_602020.ipynb](0109_block_notax_i_hicp_m_world_b_deit_602020.ipynb) | 60% MSCI World + 20% Bund + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0110_block_notax_i_hicp_m_world_b_deit_701515.ipynb](0110_block_notax_i_hicp_m_world_b_deit_701515.ipynb) | 70% MSCI World + 15% Bund + 15% BTP | SWR simulation with Euro area HICP inflation |
| [0111_block_notax_i_hicp_m_world_b_deit_801010.ipynb](0111_block_notax_i_hicp_m_world_b_deit_801010.ipynb) | 80% MSCI World + 10% Bund + 10% BTP | SWR simulation with Euro area HICP inflation |
| [0112_block_notax_i_hicp_m_world_b_deit_900505.ipynb](0112_block_notax_i_hicp_m_world_b_deit_900505.ipynb) | 90% MSCI World + 5% Bund + 5% BTP | SWR simulation with Euro area HICP inflation |

### MSCI ACWI + Bund Portfolios (02xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0200_block_notax_i_hicp_m_acwi_b_de_6040.ipynb](0200_block_notax_i_hicp_m_acwi_b_de_6040.ipynb) | 60% MSCI ACWI + 40% Bund | SWR simulation with Euro area HICP inflation |
| [0201_block_notax_i_hicp_m_acwi_b_de_7030.ipynb](0201_block_notax_i_hicp_m_acwi_b_de_7030.ipynb) | 70% MSCI ACWI + 30% Bund | SWR simulation with Euro area HICP inflation |
| [0202_block_notax_i_hicp_m_acwi_b_de_8020.ipynb](0202_block_notax_i_hicp_m_acwi_b_de_8020.ipynb) | 80% MSCI ACWI + 20% Bund | SWR simulation with Euro area HICP inflation |
| [0203_block_notax_i_hicp_m_acwi_b_de_9010.ipynb](0203_block_notax_i_hicp_m_acwi_b_de_9010.ipynb) | 90% MSCI ACWI + 10% Bund | SWR simulation with Euro area HICP inflation |
| [0204_block_notax_i_hicp_m_acwi_b_de_1000.ipynb](0204_block_notax_i_hicp_m_acwi_b_de_1000.ipynb) | 100% MSCI ACWI | SWR simulation with Euro area HICP inflation |

### MSCI ACWI + BTP Portfolios (02xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0205_block_notax_i_hicp_m_acwi_b_it_6040.ipynb](0205_block_notax_i_hicp_m_acwi_b_it_6040.ipynb) | 60% MSCI ACWI + 40% BTP | SWR simulation with Euro area HICP inflation |
| [0206_block_notax_i_hicp_m_acwi_b_it_7030.ipynb](0206_block_notax_i_hicp_m_acwi_b_it_7030.ipynb) | 70% MSCI ACWI + 30% BTP | SWR simulation with Euro area HICP inflation |
| [0207_block_notax_i_hicp_m_acwi_b_it_8020.ipynb](0207_block_notax_i_hicp_m_acwi_b_it_8020.ipynb) | 80% MSCI ACWI + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0208_block_notax_i_hicp_m_acwi_b_it_9010.ipynb](0208_block_notax_i_hicp_m_acwi_b_it_9010.ipynb) | 90% MSCI ACWI + 10% BTP | SWR simulation with Euro area HICP inflation |

### MSCI ACWI + Bund + BTP Portfolios (02xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0209_block_notax_i_hicp_m_acwi_b_deit_602020.ipynb](0209_block_notax_i_hicp_m_acwi_b_deit_602020.ipynb) | 60% MSCI ACWI + 20% Bund + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0210_block_notax_i_hicp_m_acwi_b_deit_701515.ipynb](0210_block_notax_i_hicp_m_acwi_b_deit_701515.ipynb) | 70% MSCI ACWI + 15% Bund + 15% BTP | SWR simulation with Euro area HICP inflation |
| [0211_block_notax_i_hicp_m_acwi_b_deit_801010.ipynb](0211_block_notax_i_hicp_m_acwi_b_deit_801010.ipynb) | 80% MSCI ACWI + 10% Bund + 10% BTP | SWR simulation with Euro area HICP inflation |
| [0212_block_notax_i_hicp_m_acwi_b_deit_900505.ipynb](0212_block_notax_i_hicp_m_acwi_b_deit_900505.ipynb) | 90% MSCI ACWI + 5% Bund + 5% BTP | SWR simulation with Euro area HICP inflation |

### STOXX Europe 600 + Bund Portfolios (03xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0300_block_notax_i_hicp_s_e600_b_de_6040.ipynb](0300_block_notax_i_hicp_s_e600_b_de_6040.ipynb) | 60% STOXX 600 + 40% Bund | SWR simulation with Euro area HICP inflation |
| [0301_block_notax_i_hicp_s_e600_b_de_7030.ipynb](0301_block_notax_i_hicp_s_e600_b_de_7030.ipynb) | 70% STOXX 600 + 30% Bund | SWR simulation with Euro area HICP inflation |
| [0302_block_notax_i_hicp_s_e600_b_de_8020.ipynb](0302_block_notax_i_hicp_s_e600_b_de_8020.ipynb) | 80% STOXX 600 + 20% Bund | SWR simulation with Euro area HICP inflation |
| [0303_block_notax_i_hicp_s_e600_b_de_9010.ipynb](0303_block_notax_i_hicp_s_e600_b_de_9010.ipynb) | 90% STOXX 600 + 10% Bund | SWR simulation with Euro area HICP inflation |
| [0304_block_notax_i_hicp_s_e600_b_de_1000.ipynb](0304_block_notax_i_hicp_s_e600_b_de_1000.ipynb) | 100% STOXX 600 | SWR simulation with Euro area HICP inflation |

### MSCI Europe + Bund Portfolios (04xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0400_block_notax_i_hicp_m_europe_b_de_6040.ipynb](0400_block_notax_i_hicp_m_europe_b_de_6040.ipynb) | 60% MSCI Europe + 40% Bund | SWR simulation with Euro area HICP inflation |
| [0401_block_notax_i_hicp_m_europe_b_de_7030.ipynb](0401_block_notax_i_hicp_m_europe_b_de_7030.ipynb) | 70% MSCI Europe + 30% Bund | SWR simulation with Euro area HICP inflation |
| [0402_block_notax_i_hicp_m_europe_b_de_8020.ipynb](0402_block_notax_i_hicp_m_europe_b_de_8020.ipynb) | 80% MSCI Europe + 20% Bund | SWR simulation with Euro area HICP inflation |
| [0403_block_notax_i_hicp_m_europe_b_de_9010.ipynb](0403_block_notax_i_hicp_m_europe_b_de_9010.ipynb) | 90% MSCI Europe + 10% Bund | SWR simulation with Euro area HICP inflation |
| [0404_block_notax_i_hicp_m_europe_b_de_1000.ipynb](0404_block_notax_i_hicp_m_europe_b_de_1000.ipynb) | 100% MSCI Europe | SWR simulation with Euro area HICP inflation |

### MSCI Europe + BTP Portfolios (04xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0405_block_notax_i_hicp_m_europe_b_it_6040.ipynb](0405_block_notax_i_hicp_m_europe_b_it_6040.ipynb) | 60% MSCI Europe + 40% BTP | SWR simulation with Euro area HICP inflation |
| [0406_block_notax_i_hicp_m_europe_b_it_7030.ipynb](0406_block_notax_i_hicp_m_europe_b_it_7030.ipynb) | 70% MSCI Europe + 30% BTP | SWR simulation with Euro area HICP inflation |
| [0407_block_notax_i_hicp_m_europe_b_it_8020.ipynb](0407_block_notax_i_hicp_m_europe_b_it_8020.ipynb) | 80% MSCI Europe + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0408_block_notax_i_hicp_m_europe_b_it_9010.ipynb](0408_block_notax_i_hicp_m_europe_b_it_9010.ipynb) | 90% MSCI Europe + 10% BTP | SWR simulation with Euro area HICP inflation |

### MSCI Europe + Bund + BTP Portfolios (04xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0409_block_notax_i_hicp_m_europe_b_deit_602020.ipynb](0409_block_notax_i_hicp_m_europe_b_deit_602020.ipynb) | 60% MSCI Europe + 20% Bund + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0410_block_notax_i_hicp_m_europe_b_deit_701515.ipynb](0410_block_notax_i_hicp_m_europe_b_deit_701515.ipynb) | 70% MSCI Europe + 15% Bund + 15% BTP | SWR simulation with Euro area HICP inflation |
| [0411_block_notax_i_hicp_m_europe_b_deit_801010.ipynb](0411_block_notax_i_hicp_m_europe_b_deit_801010.ipynb) | 80% MSCI Europe + 10% Bund + 10% BTP | SWR simulation with Euro area HICP inflation |
| [0412_block_notax_i_hicp_m_europe_b_deit_900505.ipynb](0412_block_notax_i_hicp_m_europe_b_deit_900505.ipynb) | 90% MSCI Europe + 5% Bund + 5% BTP | SWR simulation with Euro area HICP inflation |

### MSCI EMU + Bund Portfolios (05xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0500_block_notax_i_hicp_m_emu_b_de_6040.ipynb](0500_block_notax_i_hicp_m_emu_b_de_6040.ipynb) | 60% MSCI EMU + 40% Bund | SWR simulation with Euro area HICP inflation |
| [0501_block_notax_i_hicp_m_emu_b_de_7030.ipynb](0501_block_notax_i_hicp_m_emu_b_de_7030.ipynb) | 70% MSCI EMU + 30% Bund | SWR simulation with Euro area HICP inflation |
| [0502_block_notax_i_hicp_m_emu_b_de_8020.ipynb](0502_block_notax_i_hicp_m_emu_b_de_8020.ipynb) | 80% MSCI EMU + 20% Bund | SWR simulation with Euro area HICP inflation |
| [0503_block_notax_i_hicp_m_emu_b_de_9010.ipynb](0503_block_notax_i_hicp_m_emu_b_de_9010.ipynb) | 90% MSCI EMU + 10% Bund | SWR simulation with Euro area HICP inflation |
| [0504_block_notax_i_hicp_m_emu_b_de_1000.ipynb](0504_block_notax_i_hicp_m_emu_b_de_1000.ipynb) | 100% MSCI EMU | SWR simulation with Euro area HICP inflation |

### MSCI EMU + BTP Portfolios (05xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0505_block_notax_i_hicp_m_emu_b_it_6040.ipynb](0505_block_notax_i_hicp_m_emu_b_it_6040.ipynb) | 60% MSCI EMU + 40% BTP | SWR simulation with Euro area HICP inflation |
| [0506_block_notax_i_hicp_m_emu_b_it_7030.ipynb](0506_block_notax_i_hicp_m_emu_b_it_7030.ipynb) | 70% MSCI EMU + 30% BTP | SWR simulation with Euro area HICP inflation |
| [0507_block_notax_i_hicp_m_emu_b_it_8020.ipynb](0507_block_notax_i_hicp_m_emu_b_it_8020.ipynb) | 80% MSCI EMU + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0508_block_notax_i_hicp_m_emu_b_it_9010.ipynb](0508_block_notax_i_hicp_m_emu_b_it_9010.ipynb) | 90% MSCI EMU + 10% BTP | SWR simulation with Euro area HICP inflation |

### MSCI EMU + Bund + BTP Portfolios (05xx, No Tax)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0509_block_notax_i_hicp_m_emu_b_deit_602020.ipynb](0509_block_notax_i_hicp_m_emu_b_deit_602020.ipynb) | 60% MSCI EMU + 20% Bund + 20% BTP | SWR simulation with Euro area HICP inflation |
| [0510_block_notax_i_hicp_m_emu_b_deit_701515.ipynb](0510_block_notax_i_hicp_m_emu_b_deit_701515.ipynb) | 70% MSCI EMU + 15% Bund + 15% BTP | SWR simulation with Euro area HICP inflation |
| [0511_block_notax_i_hicp_m_emu_b_deit_801010.ipynb](0511_block_notax_i_hicp_m_emu_b_deit_801010.ipynb) | 80% MSCI EMU + 10% Bund + 10% BTP | SWR simulation with Euro area HICP inflation |
| [0512_block_notax_i_hicp_m_emu_b_deit_900505.ipynb](0512_block_notax_i_hicp_m_emu_b_deit_900505.ipynb) | 90% MSCI EMU + 5% Bund + 5% BTP | SWR simulation with Euro area HICP inflation |

### MSCI World + Bund Portfolios (06xx, No Tax, 3% WR)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0600_block_notax_i_hicp_3_m_world_b_de_6040.ipynb](0600_block_notax_i_hicp_3_m_world_b_de_6040.ipynb) | 60% MSCI World + 40% Bund | 3% SWR simulation with Euro area HICP inflation |
| [0601_block_notax_i_hicp_3_m_world_b_de_7030.ipynb](0601_block_notax_i_hicp_3_m_world_b_de_7030.ipynb) | 70% MSCI World + 30% Bund | 3% SWR simulation with Euro area HICP inflation |
| [0602_block_notax_i_hicp_3_m_world_b_de_8020.ipynb](0602_block_notax_i_hicp_3_m_world_b_de_8020.ipynb) | 80% MSCI World + 20% Bund | 3% SWR simulation with Euro area HICP inflation |
| [0603_block_notax_i_hicp_3_m_world_b_de_9010.ipynb](0603_block_notax_i_hicp_3_m_world_b_de_9010.ipynb) | 90% MSCI World + 10% Bund | 3% SWR simulation with Euro area HICP inflation |
| [0604_block_notax_i_hicp_3_m_world_b_de_1000.ipynb](0604_block_notax_i_hicp_3_m_world_b_de_1000.ipynb) | 100% MSCI World | 3% SWR simulation with Euro area HICP inflation |

### MSCI World + BTP Portfolios (06xx, No Tax, 3% WR)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0605_block_notax_i_hicp_3_m_world_b_it_6040.ipynb](0605_block_notax_i_hicp_3_m_world_b_it_6040.ipynb) | 60% MSCI World + 40% BTP | 3% SWR simulation with Euro area HICP inflation |
| [0606_block_notax_i_hicp_3_m_world_b_it_7030.ipynb](0606_block_notax_i_hicp_3_m_world_b_it_7030.ipynb) | 70% MSCI World + 30% BTP | 3% SWR simulation with Euro area HICP inflation |
| [0607_block_notax_i_hicp_3_m_world_b_it_8020.ipynb](0607_block_notax_i_hicp_3_m_world_b_it_8020.ipynb) | 80% MSCI World + 20% BTP | 3% SWR simulation with Euro area HICP inflation |
| [0608_block_notax_i_hicp_3_m_world_b_it_9010.ipynb](0608_block_notax_i_hicp_3_m_world_b_it_9010.ipynb) | 90% MSCI World + 10% BTP | 3% SWR simulation with Euro area HICP inflation |

### MSCI World + Bund + BTP Portfolios (06xx, No Tax, 3% WR)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0609_block_notax_i_hicp_3_m_world_b_deit_602020.ipynb](0609_block_notax_i_hicp_3_m_world_b_deit_602020.ipynb) | 60% MSCI World + 20% Bund + 20% BTP | 3% SWR simulation with Euro area HICP inflation |
| [0610_block_notax_i_hicp_3_m_world_b_deit_701515.ipynb](0610_block_notax_i_hicp_3_m_world_b_deit_701515.ipynb) | 70% MSCI World + 15% Bund + 15% BTP | 3% SWR simulation with Euro area HICP inflation |
| [0611_block_notax_i_hicp_3_m_world_b_deit_801010.ipynb](0611_block_notax_i_hicp_3_m_world_b_deit_801010.ipynb) | 80% MSCI World + 10% Bund + 10% BTP | 3% SWR simulation with Euro area HICP inflation |
| [0612_block_notax_i_hicp_3_m_world_b_deit_900505.ipynb](0612_block_notax_i_hicp_3_m_world_b_deit_900505.ipynb) | 90% MSCI World + 5% Bund + 5% BTP | 3% SWR simulation with Euro area HICP inflation |

### MSCI World + Bund Portfolios (07xx, No Tax, 3.5% WR)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0700_block_notax_i_hicp_35_m_world_b_de_6040.ipynb](0700_block_notax_i_hicp_35_m_world_b_de_6040.ipynb) | 60% MSCI World + 40% Bund | 3.5% SWR simulation with Euro area HICP inflation |
| [0701_block_notax_i_hicp_35_m_world_b_de_7030.ipynb](0701_block_notax_i_hicp_35_m_world_b_de_7030.ipynb) | 70% MSCI World + 30% Bund | 3.5% SWR simulation with Euro area HICP inflation |
| [0702_block_notax_i_hicp_35_m_world_b_de_8020.ipynb](0702_block_notax_i_hicp_35_m_world_b_de_8020.ipynb) | 80% MSCI World + 20% Bund | 3.5% SWR simulation with Euro area HICP inflation |
| [0703_block_notax_i_hicp_35_m_world_b_de_9010.ipynb](0703_block_notax_i_hicp_35_m_world_b_de_9010.ipynb) | 90% MSCI World + 10% Bund | 3.5% SWR simulation with Euro area HICP inflation |
| [0704_block_notax_i_hicp_35_m_world_b_de_1000.ipynb](0704_block_notax_i_hicp_35_m_world_b_de_1000.ipynb) | 100% MSCI World | 3.5% SWR simulation with Euro area HICP inflation |

### MSCI World + BTP Portfolios (07xx, No Tax, 3.5% WR)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0705_block_notax_i_hicp_35_m_world_b_it_6040.ipynb](0705_block_notax_i_hicp_35_m_world_b_it_6040.ipynb) | 60% MSCI World + 40% BTP | 3.5% SWR simulation with Euro area HICP inflation |
| [0706_block_notax_i_hicp_35_m_world_b_it_7030.ipynb](0706_block_notax_i_hicp_35_m_world_b_it_7030.ipynb) | 70% MSCI World + 30% BTP | 3.5% SWR simulation with Euro area HICP inflation |
| [0707_block_notax_i_hicp_35_m_world_b_it_8020.ipynb](0707_block_notax_i_hicp_35_m_world_b_it_8020.ipynb) | 80% MSCI World + 20% BTP | 3.5% SWR simulation with Euro area HICP inflation |
| [0708_block_notax_i_hicp_35_m_world_b_it_9010.ipynb](0708_block_notax_i_hicp_35_m_world_b_it_9010.ipynb) | 90% MSCI World + 10% BTP | 3.5% SWR simulation with Euro area HICP inflation |

### MSCI World + Bund + BTP Portfolios (07xx, No Tax, 3.5% WR)

| Notebook | Allocation | Description |
|----------|-------------|-------------|
| [0709_block_notax_i_hicp_35_m_world_b_deit_602020.ipynb](0709_block_notax_i_hicp_35_m_world_b_deit_602020.ipynb) | 60% MSCI World + 20% Bund + 20% BTP | 3.5% SWR simulation with Euro area HICP inflation |
| [0710_block_notax_i_hicp_35_m_world_b_deit_701515.ipynb](0710_block_notax_i_hicp_35_m_world_b_deit_701515.ipynb) | 70% MSCI World + 15% Bund + 15% BTP | 3.5% SWR simulation with Euro area HICP inflation |
| [0711_block_notax_i_hicp_35_m_world_b_deit_801010.ipynb](0711_block_notax_i_hicp_35_m_world_b_deit_801010.ipynb) | 80% MSCI World + 10% Bund + 10% BTP | 3.5% SWR simulation with Euro area HICP inflation |
| [0712_block_notax_i_hicp_35_m_world_b_deit_900505.ipynb](0712_block_notax_i_hicp_35_m_world_b_deit_900505.ipynb) | 90% MSCI World + 5% Bund + 5% BTP | 3.5% SWR simulation with Euro area HICP inflation |

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
