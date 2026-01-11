# Analysis Registry

> Auto-generated from notebooks on 2026-01-11 18:08:13

## Methodology Summary

| Parameter | Value |
|-----------|-------|
| Simulation method | Block Bootstrap |
| Block size | 6 months |
| N. simulations | 100,000 |
| Time horizon | 30 years |
| Inflation adjustment | Lagged (t-1) |
| Return aggregation | Growth factor method |

---

## Summary Table

| ID | Equity | Bond | Allocation | Inflation | Tax | WR | Success Rate | Median Final | Mean Final | Median Depletion | Mean Depletion | Min Depletion |
|----|--------|------|------------|-----------|-----|----|--------------|--------------|------------|------------------|----------------|---------------|
| 0100 | MSCI World | Bund | 60/40 | HICP_EU | No Tax | 4% | 78.35% | €899,494 | €1,381,636 | 26 | 25.3 | 12 |
| 0101 | MSCI World | Bund | 70/30 | HICP_EU | No Tax | 4% | 78.17% | €1,097,975 | €1,807,516 | 25 | 24.6 | 11 |
| 0102 | MSCI World | Bund | 80/20 | HICP_EU | No Tax | 4% | 77.33% | €1,282,788 | €2,308,728 | 24 | 23.9 | 10 |
| 0103 | MSCI World | Bund | 90/10 | HICP_EU | No Tax | 4% | 76.23% | €1,444,403 | €2,895,666 | 24 | 23.2 | 9 |
| 0104 | MSCI World | - | 100 | HICP_EU | No Tax | 4% | 74.86% | €1,580,517 | €3,580,714 | 23 | 22.5 | 8 |
| 0105 | MSCI World | BTP | 60/40 | HICP_EU | No Tax | 4% | 80.46% | €1,188,838 | €1,848,342 | 25 | 25.0 | 12 |
| 0106 | MSCI World | BTP | 70/30 | HICP_EU | No Tax | 4% | 79.68% | €1,333,558 | €2,212,797 | 25 | 24.4 | 11 |
| 0107 | MSCI World | BTP | 80/20 | HICP_EU | No Tax | 4% | 78.32% | €1,447,769 | €2,620,960 | 24 | 23.8 | 9 |
| 0108 | MSCI World | BTP | 90/10 | HICP_EU | No Tax | 4% | 76.73% | €1,530,097 | €3,075,857 | 24 | 23.2 | 8 |
| 0109 | MSCI World | Bund+BTP | 60/20/20 | HICP_EU | No Tax | 4% | 79.87% | €1,054,239 | €1,606,661 | 26 | 25.2 | 12 |
| 0110 | MSCI World | Bund+BTP | 70/15/15 | HICP_EU | No Tax | 4% | 79.15% | €1,221,866 | €2,005,033 | 25 | 24.5 | 11 |
| 0111 | MSCI World | Bund+BTP | 80/10/10 | HICP_EU | No Tax | 4% | 77.94% | €1,367,482 | €2,462,334 | 24 | 23.9 | 10 |
| 0112 | MSCI World | Bund+BTP | 90/5/5 | HICP_EU | No Tax | 4% | 76.50% | €1,489,272 | €2,985,057 | 24 | 23.2 | 8 |
| 0200 | MSCI ACWI | Bund | 60/40 | HICP_EU | No Tax | 4% | 76.97% | €837,272 | €1,318,952 | 26 | 25.2 | 12 |
| 0201 | MSCI ACWI | Bund | 70/30 | HICP_EU | No Tax | 4% | 76.77% | €1,017,984 | €1,724,778 | 25 | 24.6 | 11 |
| 0202 | MSCI ACWI | Bund | 80/20 | HICP_EU | No Tax | 4% | 75.99% | €1,187,717 | €2,202,664 | 24 | 23.9 | 10 |
| 0203 | MSCI ACWI | Bund | 90/10 | HICP_EU | No Tax | 4% | 74.93% | €1,334,669 | €2,762,741 | 24 | 23.1 | 9 |
| 0204 | MSCI ACWI | - | 100 | HICP_EU | No Tax | 4% | 73.63% | €1,458,183 | €3,417,091 | 23 | 22.5 | 8 |
| 0205 | MSCI ACWI | BTP | 60/40 | HICP_EU | No Tax | 4% | 79.18% | €1,113,314 | €1,772,350 | 25 | 24.9 | 12 |
| 0206 | MSCI ACWI | BTP | 70/30 | HICP_EU | No Tax | 4% | 78.35% | €1,243,429 | €2,117,440 | 25 | 24.3 | 11 |
| 0207 | MSCI ACWI | BTP | 80/20 | HICP_EU | No Tax | 4% | 77.02% | €1,344,157 | €2,504,514 | 24 | 23.7 | 9 |
| 0208 | MSCI ACWI | BTP | 90/10 | HICP_EU | No Tax | 4% | 75.40% | €1,416,403 | €2,936,635 | 23 | 23.1 | 8 |
| 0209 | MSCI ACWI | Bund+BTP | 60/20/20 | HICP_EU | No Tax | 4% | 78.53% | €983,413 | €1,537,335 | 26 | 25.1 | 12 |
| 0210 | MSCI ACWI | Bund+BTP | 70/15/15 | HICP_EU | No Tax | 4% | 77.77% | €1,133,975 | €1,916,017 | 25 | 24.4 | 11 |
| 0211 | MSCI ACWI | Bund+BTP | 80/10/10 | HICP_EU | No Tax | 4% | 76.60% | €1,268,338 | €2,351,093 | 24 | 23.8 | 10 |
| 0212 | MSCI ACWI | Bund+BTP | 90/5/5 | HICP_EU | No Tax | 4% | 75.18% | €1,376,308 | €2,848,998 | 24 | 23.1 | 8 |
| 0300 | STOXX 600 | Bund | 60/40 | HICP_EU | No Tax | 4% | 81.95% | €3,924,453 | €9,919,297 | 22 | 21.7 | 8 |
| 0301 | STOXX 600 | Bund | 70/30 | HICP_EU | No Tax | 4% | 80.23% | €4,723,474 | €15,380,633 | 21 | 20.6 | 7 |
| 0302 | STOXX 600 | Bund | 80/20 | HICP_EU | No Tax | 4% | 78.25% | €5,456,359 | €23,798,822 | 19 | 19.6 | 6 |
| 0303 | STOXX 600 | Bund | 90/10 | HICP_EU | No Tax | 4% | 76.23% | €6,078,578 | €36,903,053 | 18 | 18.8 | 6 |
| 0304 | STOXX 600 | - | 100 | HICP_EU | No Tax | 4% | 88.09% | €11,025,784 | €26,753,425 | 21 | 21.1 | 7 |
| 0400 | MSCI Europe | Bund | 60/40 | HICP_EU | No Tax | 4% | 65.00% | €384,577 | €878,249 | 25 | 24.7 | 11 |
| 0401 | MSCI Europe | Bund | 70/30 | HICP_EU | No Tax | 4% | 63.92% | €428,468 | €1,115,627 | 24 | 23.9 | 10 |
| 0402 | MSCI Europe | Bund | 80/20 | HICP_EU | No Tax | 4% | 62.52% | €447,219 | €1,381,899 | 23 | 23.1 | 9 |
| 0403 | MSCI Europe | Bund | 90/10 | HICP_EU | No Tax | 4% | 60.85% | €434,461 | €1,678,483 | 23 | 22.3 | 8 |
| 0404 | MSCI Europe | - | 100 | HICP_EU | No Tax | 4% | 58.97% | €393,783 | €2,007,341 | 22 | 21.6 | 7 |
| 0405 | MSCI Europe | BTP | 60/40 | HICP_EU | No Tax | 4% | 67.85% | €566,126 | €1,227,077 | 25 | 24.2 | 11 |
| 0406 | MSCI Europe | BTP | 70/30 | HICP_EU | No Tax | 4% | 66.00% | €562,083 | €1,404,050 | 24 | 23.6 | 10 |
| 0407 | MSCI Europe | BTP | 80/20 | HICP_EU | No Tax | 4% | 63.73% | €532,579 | €1,593,587 | 23 | 22.9 | 9 |
| 0408 | MSCI Europe | BTP | 90/10 | HICP_EU | No Tax | 4% | 61.41% | €472,065 | €1,794,887 | 22 | 22.2 | 8 |
| 0409 | MSCI Europe | Bund+BTP | 60/20/20 | HICP_EU | No Tax | 4% | 66.80% | €482,433 | €1,045,166 | 25 | 24.5 | 11 |
| 0410 | MSCI Europe | Bund+BTP | 70/15/15 | HICP_EU | No Tax | 4% | 65.16% | €498,546 | €1,255,451 | 24 | 23.8 | 10 |
| 0411 | MSCI Europe | Bund+BTP | 80/10/10 | HICP_EU | No Tax | 4% | 63.22% | €490,738 | €1,485,709 | 23 | 23.0 | 9 |
| 0412 | MSCI Europe | Bund+BTP | 90/5/5 | HICP_EU | No Tax | 4% | 61.19% | €453,207 | €1,736,154 | 22 | 22.3 | 8 |
| 0500 | MSCI EMU | Bund | 60/40 | HICP_EU | No Tax | 4% | 60.88% | €294,456 | €891,975 | 24 | 24.1 | 11 |
| 0501 | MSCI EMU | Bund | 70/30 | HICP_EU | No Tax | 4% | 59.51% | €301,911 | €1,132,049 | 23 | 23.2 | 10 |
| 0502 | MSCI EMU | Bund | 80/20 | HICP_EU | No Tax | 4% | 57.72% | €278,820 | €1,400,590 | 23 | 22.4 | 8 |
| 0503 | MSCI EMU | Bund | 90/10 | HICP_EU | No Tax | 4% | 55.78% | €231,278 | €1,698,954 | 22 | 21.6 | 7 |
| 0504 | MSCI EMU | - | 100 | HICP_EU | No Tax | 4% | 53.57% | €156,499 | €2,028,953 | 21 | 20.8 | 6 |
| 0505 | MSCI EMU | BTP | 60/40 | HICP_EU | No Tax | 4% | 63.57% | €442,670 | €1,250,384 | 24 | 23.5 | 10 |
| 0506 | MSCI EMU | BTP | 70/30 | HICP_EU | No Tax | 4% | 61.27% | €408,498 | €1,429,125 | 23 | 22.9 | 9 |
| 0507 | MSCI EMU | BTP | 80/20 | HICP_EU | No Tax | 4% | 58.78% | €347,077 | €1,619,083 | 22 | 22.2 | 8 |
| 0508 | MSCI EMU | BTP | 90/10 | HICP_EU | No Tax | 4% | 56.22% | €260,847 | €1,819,311 | 22 | 21.5 | 7 |
| 0509 | MSCI EMU | Bund+BTP | 60/20/20 | HICP_EU | No Tax | 4% | 62.52% | €375,056 | €1,063,453 | 24 | 23.8 | 10 |
| 0510 | MSCI EMU | Bund+BTP | 70/15/15 | HICP_EU | No Tax | 4% | 60.54% | €358,693 | €1,276,027 | 23 | 23.1 | 9 |
| 0511 | MSCI EMU | Bund+BTP | 80/10/10 | HICP_EU | No Tax | 4% | 58.31% | €315,216 | €1,507,696 | 22 | 22.3 | 8 |
| 0512 | MSCI EMU | Bund+BTP | 90/5/5 | HICP_EU | No Tax | 4% | 56.00% | €245,658 | €1,758,570 | 22 | 21.5 | 7 |
| 0600 | MSCI World | Bund | 60/40 | HICP_EU | No Tax | 3% | 95.82% | €1,850,878 | €2,301,669 | 27 | 26.7 | 14 |
| 0601 | MSCI World | Bund | 70/30 | HICP_EU | No Tax | 3% | 94.43% | €2,096,234 | €2,798,778 | 27 | 26.0 | 13 |
| 0602 | MSCI World | Bund | 80/20 | HICP_EU | No Tax | 3% | 92.75% | €2,331,297 | €3,376,173 | 26 | 25.3 | 12 |
| 0603 | MSCI World | Bund | 90/10 | HICP_EU | No Tax | 3% | 90.99% | €2,540,817 | €4,045,800 | 25 | 24.6 | 11 |
| 0604 | MSCI World | - | 100 | HICP_EU | No Tax | 3% | 89.11% | €2,724,769 | €4,821,149 | 24 | 23.9 | 9 |
| 0605 | MSCI World | BTP | 60/40 | HICP_EU | No Tax | 3% | 95.71% | €2,210,116 | €2,864,884 | 27 | 26.2 | 14 |
| 0606 | MSCI World | BTP | 70/30 | HICP_EU | No Tax | 3% | 94.48% | €2,391,411 | €3,283,781 | 26 | 25.7 | 13 |
| 0607 | MSCI World | BTP | 80/20 | HICP_EU | No Tax | 3% | 92.88% | €2,536,276 | €3,746,867 | 26 | 25.2 | 12 |
| 0608 | MSCI World | BTP | 90/10 | HICP_EU | No Tax | 3% | 91.10% | €2,653,424 | €4,258,044 | 25 | 24.5 | 11 |
| 0609 | MSCI World | Bund+BTP | 60/20/20 | HICP_EU | No Tax | 3% | 95.91% | €2,038,282 | €2,576,896 | 27 | 26.5 | 14 |
| 0610 | MSCI World | Bund+BTP | 70/15/15 | HICP_EU | No Tax | 3% | 94.54% | €2,250,315 | €3,037,100 | 26 | 25.9 | 13 |
| 0611 | MSCI World | Bund+BTP | 80/10/10 | HICP_EU | No Tax | 3% | 92.83% | €2,435,778 | €3,559,366 | 26 | 25.3 | 12 |
| 0612 | MSCI World | Bund+BTP | 90/5/5 | HICP_EU | No Tax | 3% | 91.05% | €2,599,385 | €4,151,293 | 25 | 24.6 | 11 |
| 0700 | MSCI World | Bund | 60/40 | HICP_EU | No Tax | 3.5% | 89.08% | €1,371,863 | €1,823,449 | 27 | 26.1 | 13 |
| 0701 | MSCI World | Bund | 70/30 | HICP_EU | No Tax | 3.5% | 87.74% | €1,594,504 | €2,285,406 | 26 | 25.4 | 12 |
| 0702 | MSCI World | Bund | 80/20 | HICP_EU | No Tax | 3.5% | 92.75% | €2,331,297 | €3,376,173 | 26 | 25.3 | 12 |
| 0703 | MSCI World | Bund | 90/10 | HICP_EU | No Tax | 3.5% | 90.99% | €2,540,817 | €4,045,800 | 25 | 24.6 | 11 |
| 0704 | MSCI World | - | 100 | HICP_EU | No Tax | 3.5% | 89.11% | €2,724,769 | €4,821,149 | 24 | 23.9 | 9 |
| 0705 | MSCI World | BTP | 60/40 | HICP_EU | No Tax | 3.5% | 95.71% | €2,210,116 | €2,864,884 | 27 | 26.2 | 14 |
| 0706 | MSCI World | BTP | 70/30 | HICP_EU | No Tax | 3.5% | 94.48% | €2,391,411 | €3,283,781 | 26 | 25.7 | 13 |
| 0707 | MSCI World | BTP | 80/20 | HICP_EU | No Tax | 3.5% | 92.88% | €2,536,276 | €3,746,867 | 26 | 25.2 | 12 |
| 0708 | MSCI World | BTP | 90/10 | HICP_EU | No Tax | 3.5% | 91.10% | €2,653,424 | €4,258,044 | 25 | 24.5 | 11 |
| 0709 | MSCI World | Bund+BTP | 60/20/20 | HICP_EU | No Tax | 3.5% | 95.91% | €2,038,282 | €2,576,896 | 27 | 26.5 | 14 |
| 0710 | MSCI World | Bund+BTP | 70/15/15 | HICP_EU | No Tax | 3.5% | 94.54% | €2,250,315 | €3,037,100 | 26 | 25.9 | 13 |
| 0711 | MSCI World | Bund+BTP | 80/10/10 | HICP_EU | No Tax | 3.5% | 92.83% | €2,435,778 | €3,559,366 | 26 | 25.3 | 12 |
| 0712 | MSCI World | Bund+BTP | 90/5/5 | HICP_EU | No Tax | 3.5% | 91.05% | €2,599,385 | €4,151,293 | 25 | 24.6 | 11 |

---

## Detailed Analysis

### 01xx – MSCI World NET

#### 0100 – MSCI World 60% + Bund 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0100_block_notax_i_hicp_m_world_b_de_6040.ipynb](src/0100_block_notax_i_hicp_m_world_b_de_6040.ipynb) |
| Description | MSCI World 60% + Bund 10Y 40% |
| Equity Index | MSCI World (60%) |
| Bond | Bund 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 78.35% |
| Median Final Value | €899,494 |
| Mean Final Value | €1,381,636 |
| P5 Final Value | €0 |
| P95 Final Value | €4,541,365 |
| Failed Simulations | 21,647 (21.6%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.3 |
| Min Depletion Year | 12 |

---

#### 0101 – MSCI World 70% + Bund 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0101_block_notax_i_hicp_m_world_b_de_7030.ipynb](src/0101_block_notax_i_hicp_m_world_b_de_7030.ipynb) |
| Description | MSCI World 70% + Bund 10Y 30% |
| Equity Index | MSCI World (70%) |
| Bond | Bund 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 78.17% |
| Median Final Value | €1,097,975 |
| Mean Final Value | €1,807,516 |
| P5 Final Value | €0 |
| P95 Final Value | €6,181,313 |
| Failed Simulations | 21,832 (21.8%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.6 |
| Min Depletion Year | 11 |

---

#### 0102 – MSCI World 80% + Bund 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0102_block_notax_i_hicp_m_world_b_de_8020.ipynb](src/0102_block_notax_i_hicp_m_world_b_de_8020.ipynb) |
| Description | MSCI World 80% + Bund 10Y 20% |
| Equity Index | MSCI World (80%) |
| Bond | Bund 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 77.33% |
| Median Final Value | €1,282,788 |
| Mean Final Value | €2,308,728 |
| P5 Final Value | €0 |
| P95 Final Value | €8,270,551 |
| Failed Simulations | 22,669 (22.7%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.9 |
| Min Depletion Year | 10 |

---

#### 0103 – MSCI World 90% + Bund 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0103_block_notax_i_hicp_m_world_b_de_9010.ipynb](src/0103_block_notax_i_hicp_m_world_b_de_9010.ipynb) |
| Description | MSCI World 90% + Bund 10Y 10% |
| Equity Index | MSCI World (90%) |
| Bond | Bund 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 76.23% |
| Median Final Value | €1,444,403 |
| Mean Final Value | €2,895,666 |
| P5 Final Value | €0 |
| P95 Final Value | €10,825,881 |
| Failed Simulations | 23,768 (23.8%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.2 |
| Min Depletion Year | 9 |

---

#### 0104 – MSCI World 100%

| Parameter | Value |
|-----------|-------|
| Notebook | [0104_block_notax_i_hicp_m_world_b_de_1000.ipynb](src/0104_block_notax_i_hicp_m_world_b_de_1000.ipynb) |
| Description | MSCI World 100% |
| Equity Index | MSCI World (100%) |
| Bond | - |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 74.86% |
| Median Final Value | €1,580,517 |
| Mean Final Value | €3,580,714 |
| P5 Final Value | €0 |
| P95 Final Value | €14,008,419 |
| Failed Simulations | 25,138 (25.1%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 22.5 |
| Min Depletion Year | 8 |

---

#### 0105 – MSCI World 60% + BTP 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0105_block_notax_i_hicp_m_world_b_it_6040.ipynb](src/0105_block_notax_i_hicp_m_world_b_it_6040.ipynb) |
| Description | MSCI World 60% + BTP 10Y 40% |
| Equity Index | MSCI World (60%) |
| Bond | BTP 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 80.46% |
| Median Final Value | €1,188,838 |
| Mean Final Value | €1,848,342 |
| P5 Final Value | €0 |
| P95 Final Value | €6,095,223 |
| Failed Simulations | 19,540 (19.5%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 25.0 |
| Min Depletion Year | 12 |

---

#### 0106 – MSCI World 70% + BTP 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0106_block_notax_i_hicp_m_world_b_it_7030.ipynb](src/0106_block_notax_i_hicp_m_world_b_it_7030.ipynb) |
| Description | MSCI World 70% + BTP 10Y 30% |
| Equity Index | MSCI World (70%) |
| Bond | BTP 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 79.68% |
| Median Final Value | €1,333,558 |
| Mean Final Value | €2,212,797 |
| P5 Final Value | €0 |
| P95 Final Value | €7,581,764 |
| Failed Simulations | 20,318 (20.3%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.4 |
| Min Depletion Year | 11 |

---

#### 0107 – MSCI World 80% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0107_block_notax_i_hicp_m_world_b_it_8020.ipynb](src/0107_block_notax_i_hicp_m_world_b_it_8020.ipynb) |
| Description | MSCI World 80% + BTP 10Y 20% |
| Equity Index | MSCI World (80%) |
| Bond | BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 78.32% |
| Median Final Value | €1,447,769 |
| Mean Final Value | €2,620,960 |
| P5 Final Value | €0 |
| P95 Final Value | €9,399,755 |
| Failed Simulations | 21,677 (21.7%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.8 |
| Min Depletion Year | 9 |

---

#### 0108 – MSCI World 90% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0108_block_notax_i_hicp_m_world_b_it_9010.ipynb](src/0108_block_notax_i_hicp_m_world_b_it_9010.ipynb) |
| Description | MSCI World 90% + BTP 10Y 10% |
| Equity Index | MSCI World (90%) |
| Bond | BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 76.73% |
| Median Final Value | €1,530,097 |
| Mean Final Value | €3,075,857 |
| P5 Final Value | €0 |
| P95 Final Value | €11,535,199 |
| Failed Simulations | 23,271 (23.3%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.2 |
| Min Depletion Year | 8 |

---

#### 0109 – MSCI World 60% + Bund 10Y 20% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0109_block_notax_i_hicp_m_world_b_deit_602020.ipynb](src/0109_block_notax_i_hicp_m_world_b_deit_602020.ipynb) |
| Description | MSCI World 60% + Bund 10Y 20% + BTP 10Y 20% |
| Equity Index | MSCI World (60%) |
| Bond | Bund 10Y (20%) + BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 79.87% |
| Median Final Value | €1,054,239 |
| Mean Final Value | €1,606,661 |
| P5 Final Value | €0 |
| P95 Final Value | €5,244,569 |
| Failed Simulations | 20,130 (20.1%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.2 |
| Min Depletion Year | 12 |

---

#### 0110 – MSCI World 70% + Bund 10Y 15% + BTP 10Y 15%

| Parameter | Value |
|-----------|-------|
| Notebook | [0110_block_notax_i_hicp_m_world_b_deit_701515.ipynb](src/0110_block_notax_i_hicp_m_world_b_deit_701515.ipynb) |
| Description | MSCI World 70% + Bund 10Y 15% + BTP 10Y 15% |
| Equity Index | MSCI World (70%) |
| Bond | Bund 10Y (15%) + BTP 10Y (15%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 79.15% |
| Median Final Value | €1,221,866 |
| Mean Final Value | €2,005,033 |
| P5 Final Value | €0 |
| P95 Final Value | €6,843,578 |
| Failed Simulations | 20,847 (20.8%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.5 |
| Min Depletion Year | 11 |

---

#### 0111 – MSCI World 80% + Bund 10Y 10% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0111_block_notax_i_hicp_m_world_b_deit_801010.ipynb](src/0111_block_notax_i_hicp_m_world_b_deit_801010.ipynb) |
| Description | MSCI World 80% + Bund 10Y 10% + BTP 10Y 10% |
| Equity Index | MSCI World (80%) |
| Bond | Bund 10Y (10%) + BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 77.94% |
| Median Final Value | €1,367,482 |
| Mean Final Value | €2,462,334 |
| P5 Final Value | €0 |
| P95 Final Value | €8,832,595 |
| Failed Simulations | 22,057 (22.1%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.9 |
| Min Depletion Year | 10 |

---

#### 0112 – MSCI World 90% + Bund 10Y 5% + BTP 10Y 5%

| Parameter | Value |
|-----------|-------|
| Notebook | [0112_block_notax_i_hicp_m_world_b_deit_900505.ipynb](src/0112_block_notax_i_hicp_m_world_b_deit_900505.ipynb) |
| Description | MSCI World 90% + Bund 10Y 5% + BTP 10Y 5% |
| Equity Index | MSCI World (90%) |
| Bond | Bund 10Y (5%) + BTP 10Y (5%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 76.50% |
| Median Final Value | €1,489,272 |
| Mean Final Value | €2,985,057 |
| P5 Final Value | €0 |
| P95 Final Value | €11,198,818 |
| Failed Simulations | 23,503 (23.5%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.2 |
| Min Depletion Year | 8 |

---

### 02xx – MSCI ACWI NET

#### 0200 – MSCI ACWI 60% + Bund 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0200_block_notax_i_hicp_m_acwi_b_de_6040.ipynb](src/0200_block_notax_i_hicp_m_acwi_b_de_6040.ipynb) |
| Description | MSCI ACWI 60% + Bund 10Y 40% |
| Equity Index | MSCI ACWI (60%) |
| Bond | Bund 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 76.97% |
| Median Final Value | €837,272 |
| Mean Final Value | €1,318,952 |
| P5 Final Value | €0 |
| P95 Final Value | €4,399,692 |
| Failed Simulations | 23,034 (23.0%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.2 |
| Min Depletion Year | 12 |

---

#### 0201 – MSCI ACWI 70% + Bund 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0201_block_notax_i_hicp_m_acwi_b_de_7030.ipynb](src/0201_block_notax_i_hicp_m_acwi_b_de_7030.ipynb) |
| Description | MSCI ACWI 70% + Bund 10Y 30% |
| Equity Index | MSCI ACWI (70%) |
| Bond | Bund 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 76.77% |
| Median Final Value | €1,017,984 |
| Mean Final Value | €1,724,778 |
| P5 Final Value | €0 |
| P95 Final Value | €5,981,103 |
| Failed Simulations | 23,233 (23.2%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.6 |
| Min Depletion Year | 11 |

---

#### 0202 – MSCI ACWI 80% + Bund 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0202_block_notax_i_hicp_m_acwi_b_de_8020.ipynb](src/0202_block_notax_i_hicp_m_acwi_b_de_8020.ipynb) |
| Description | MSCI ACWI 80% + Bund 10Y 20% |
| Equity Index | MSCI ACWI (80%) |
| Bond | Bund 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 75.99% |
| Median Final Value | €1,187,717 |
| Mean Final Value | €2,202,664 |
| P5 Final Value | €0 |
| P95 Final Value | €7,986,124 |
| Failed Simulations | 24,010 (24.0%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.9 |
| Min Depletion Year | 10 |

---

#### 0203 – MSCI ACWI 90% + Bund 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0203_block_notax_i_hicp_m_acwi_b_de_9010.ipynb](src/0203_block_notax_i_hicp_m_acwi_b_de_9010.ipynb) |
| Description | MSCI ACWI 90% + Bund 10Y 10% |
| Equity Index | MSCI ACWI (90%) |
| Bond | Bund 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 74.93% |
| Median Final Value | €1,334,669 |
| Mean Final Value | €2,762,741 |
| P5 Final Value | €0 |
| P95 Final Value | €10,440,302 |
| Failed Simulations | 25,072 (25.1%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.1 |
| Min Depletion Year | 9 |

---

#### 0204 – MSCI ACWI 100%

| Parameter | Value |
|-----------|-------|
| Notebook | [0204_block_notax_i_hicp_m_acwi_b_de_1000.ipynb](src/0204_block_notax_i_hicp_m_acwi_b_de_1000.ipynb) |
| Description | MSCI ACWI 100% |
| Equity Index | MSCI ACWI (100%) |
| Bond | - |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 73.63% |
| Median Final Value | €1,458,183 |
| Mean Final Value | €3,417,091 |
| P5 Final Value | €0 |
| P95 Final Value | €13,470,758 |
| Failed Simulations | 26,370 (26.4%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 22.5 |
| Min Depletion Year | 8 |

---

#### 0205 – MSCI ACWI 60% + BTP 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0205_block_notax_i_hicp_m_acwi_b_it_6040.ipynb](src/0205_block_notax_i_hicp_m_acwi_b_it_6040.ipynb) |
| Description | MSCI ACWI 60% + BTP 10Y 40% |
| Equity Index | MSCI ACWI (60%) |
| Bond | BTP 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 79.18% |
| Median Final Value | €1,113,314 |
| Mean Final Value | €1,772,350 |
| P5 Final Value | €0 |
| P95 Final Value | €5,913,329 |
| Failed Simulations | 20,823 (20.8%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.9 |
| Min Depletion Year | 12 |

---

#### 0206 – MSCI ACWI 70% + BTP 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0206_block_notax_i_hicp_m_acwi_b_it_7030.ipynb](src/0206_block_notax_i_hicp_m_acwi_b_it_7030.ipynb) |
| Description | MSCI ACWI 70% + BTP 10Y 30% |
| Equity Index | MSCI ACWI (70%) |
| Bond | BTP 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 78.35% |
| Median Final Value | €1,243,429 |
| Mean Final Value | €2,117,440 |
| P5 Final Value | €0 |
| P95 Final Value | €7,348,057 |
| Failed Simulations | 21,651 (21.7%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.3 |
| Min Depletion Year | 11 |

---

#### 0207 – MSCI ACWI 80% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0207_block_notax_i_hicp_m_acwi_b_it_8020.ipynb](src/0207_block_notax_i_hicp_m_acwi_b_it_8020.ipynb) |
| Description | MSCI ACWI 80% + BTP 10Y 20% |
| Equity Index | MSCI ACWI (80%) |
| Bond | BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 77.02% |
| Median Final Value | €1,344,157 |
| Mean Final Value | €2,504,514 |
| P5 Final Value | €0 |
| P95 Final Value | €9,079,500 |
| Failed Simulations | 22,977 (23.0%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.7 |
| Min Depletion Year | 9 |

---

#### 0208 – MSCI ACWI 90% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0208_block_notax_i_hicp_m_acwi_b_it_9010.ipynb](src/0208_block_notax_i_hicp_m_acwi_b_it_9010.ipynb) |
| Description | MSCI ACWI 90% + BTP 10Y 10% |
| Equity Index | MSCI ACWI (90%) |
| Bond | BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 75.40% |
| Median Final Value | €1,416,403 |
| Mean Final Value | €2,936,635 |
| P5 Final Value | €0 |
| P95 Final Value | €11,116,477 |
| Failed Simulations | 24,602 (24.6%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 23.1 |
| Min Depletion Year | 8 |

---

#### 0209 – MSCI ACWI 60% + Bund 10Y 20% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0209_block_notax_i_hicp_m_acwi_b_deit_602020.ipynb](src/0209_block_notax_i_hicp_m_acwi_b_deit_602020.ipynb) |
| Description | MSCI ACWI 60% + Bund 10Y 20% + BTP 10Y 20% |
| Equity Index | MSCI ACWI (60%) |
| Bond | Bund 10Y (20%) + BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 78.53% |
| Median Final Value | €983,413 |
| Mean Final Value | €1,537,335 |
| P5 Final Value | €0 |
| P95 Final Value | €5,087,303 |
| Failed Simulations | 21,467 (21.5%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.1 |
| Min Depletion Year | 12 |

---

#### 0210 – MSCI ACWI 70% + Bund 10Y 15% + BTP 10Y 15%

| Parameter | Value |
|-----------|-------|
| Notebook | [0210_block_notax_i_hicp_m_acwi_b_deit_701515.ipynb](src/0210_block_notax_i_hicp_m_acwi_b_deit_701515.ipynb) |
| Description | MSCI ACWI 70% + Bund 10Y 15% + BTP 10Y 15% |
| Equity Index | MSCI ACWI (70%) |
| Bond | Bund 10Y (15%) + BTP 10Y (15%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 77.77% |
| Median Final Value | €1,133,975 |
| Mean Final Value | €1,916,017 |
| P5 Final Value | €0 |
| P95 Final Value | €6,626,916 |
| Failed Simulations | 22,227 (22.2%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.4 |
| Min Depletion Year | 11 |

---

#### 0211 – MSCI ACWI 80% + Bund 10Y 10% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0211_block_notax_i_hicp_m_acwi_b_deit_801010.ipynb](src/0211_block_notax_i_hicp_m_acwi_b_deit_801010.ipynb) |
| Description | MSCI ACWI 80% + Bund 10Y 10% + BTP 10Y 10% |
| Equity Index | MSCI ACWI (80%) |
| Bond | Bund 10Y (10%) + BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 76.60% |
| Median Final Value | €1,268,338 |
| Mean Final Value | €2,351,093 |
| P5 Final Value | €0 |
| P95 Final Value | €8,527,823 |
| Failed Simulations | 23,404 (23.4%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.8 |
| Min Depletion Year | 10 |

---

#### 0212 – MSCI ACWI 90% + Bund 10Y 5% + BTP 10Y 5%

| Parameter | Value |
|-----------|-------|
| Notebook | [0212_block_notax_i_hicp_m_acwi_b_deit_900505.ipynb](src/0212_block_notax_i_hicp_m_acwi_b_deit_900505.ipynb) |
| Description | MSCI ACWI 90% + Bund 10Y 5% + BTP 10Y 5% |
| Equity Index | MSCI ACWI (90%) |
| Bond | Bund 10Y (5%) + BTP 10Y (5%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 75.18% |
| Median Final Value | €1,376,308 |
| Mean Final Value | €2,848,998 |
| P5 Final Value | €0 |
| P95 Final Value | €10,781,621 |
| Failed Simulations | 24,816 (24.8%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.1 |
| Min Depletion Year | 8 |

---

### 03xx – STOXX Europe 600

#### 0300 – STOXX 600 60% + Bund 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0300_block_notax_i_hicp_s_e600_b_de_6040.ipynb](src/0300_block_notax_i_hicp_s_e600_b_de_6040.ipynb) |
| Description | STOXX Europe 600 60% + Bund 10Y 40% |
| Equity Index | STOXX 600 (60%) |
| Bond | Bund 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 1997-08-02 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 81.95% |
| Median Final Value | €3,924,453 |
| Mean Final Value | €9,919,297 |
| P5 Final Value | €0 |
| P95 Final Value | €39,192,568 |
| Failed Simulations | 18,052 (18.1%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 21.7 |
| Min Depletion Year | 8 |

---

#### 0301 – STOXX 600 70% + Bund 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0301_block_notax_i_hicp_s_e600_b_de_7030.ipynb](src/0301_block_notax_i_hicp_s_e600_b_de_7030.ipynb) |
| Description | STOXX Europe 600 70% + Bund 10Y 30% |
| Equity Index | STOXX 600 (70%) |
| Bond | Bund 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 1997-08-02 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 80.23% |
| Median Final Value | €4,723,474 |
| Mean Final Value | €15,380,633 |
| P5 Final Value | €0 |
| P95 Final Value | €63,823,568 |
| Failed Simulations | 19,773 (19.8%) |
| Median Depletion Year | 21 |
| Mean Depletion Year | 20.6 |
| Min Depletion Year | 7 |

---

#### 0302 – STOXX 600 80% + Bund 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0302_block_notax_i_hicp_s_e600_b_de_8020.ipynb](src/0302_block_notax_i_hicp_s_e600_b_de_8020.ipynb) |
| Description | STOXX Europe 600 80% + Bund 10Y 20% |
| Equity Index | STOXX 600 (80%) |
| Bond | Bund 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 1997-08-02 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 78.25% |
| Median Final Value | €5,456,359 |
| Mean Final Value | €23,798,822 |
| P5 Final Value | €0 |
| P95 Final Value | €101,369,495 |
| Failed Simulations | 21,748 (21.7%) |
| Median Depletion Year | 19 |
| Mean Depletion Year | 19.6 |
| Min Depletion Year | 6 |

---

#### 0303 – STOXX 600 90% + Bund 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0303_block_notax_i_hicp_s_e600_b_de_9010.ipynb](src/0303_block_notax_i_hicp_s_e600_b_de_9010.ipynb) |
| Description | STOXX Europe 600 90% + Bund 10Y 10% |
| Equity Index | STOXX 600 (90%) |
| Bond | Bund 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 1997-08-02 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 76.23% |
| Median Final Value | €6,078,578 |
| Mean Final Value | €36,903,053 |
| P5 Final Value | €0 |
| P95 Final Value | €157,034,506 |
| Failed Simulations | 23,765 (23.8%) |
| Median Depletion Year | 18 |
| Mean Depletion Year | 18.8 |
| Min Depletion Year | 6 |

---

#### 0304 – STOXX 600 100%

| Parameter | Value |
|-----------|-------|
| Notebook | [0304_block_notax_i_hicp_s_e600_b_de_1000.ipynb](src/0304_block_notax_i_hicp_s_e600_b_de_1000.ipynb) |
| Description | STOXX Europe 600 100% |
| Equity Index | STOXX 600 (100%) |
| Bond | - |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 1987-01-01 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 88.09% |
| Median Final Value | €11,025,784 |
| Mean Final Value | €26,753,425 |
| P5 Final Value | €0 |
| P95 Final Value | €103,596,483 |
| Failed Simulations | 11,914 (11.9%) |
| Median Depletion Year | 21 |
| Mean Depletion Year | 21.1 |
| Min Depletion Year | 7 |

---

### 04xx – MSCI Europe NET

#### 0400 – MSCI Europe 60% + Bund 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0400_block_notax_i_hicp_m_europe_b_de_6040.ipynb](src/0400_block_notax_i_hicp_m_europe_b_de_6040.ipynb) |
| Description | MSCI Europe 60% + Bund 10Y 40% |
| Equity Index | MSCI Europe (60%) |
| Bond | Bund 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 65.00% |
| Median Final Value | €384,577 |
| Mean Final Value | €878,249 |
| P5 Final Value | €0 |
| P95 Final Value | €3,381,309 |
| Failed Simulations | 34,999 (35.0%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.7 |
| Min Depletion Year | 11 |

---

#### 0401 – MSCI Europe 70% + Bund 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0401_block_notax_i_hicp_m_europe_b_de_7030.ipynb](src/0401_block_notax_i_hicp_m_europe_b_de_7030.ipynb) |
| Description | MSCI Europe 70% + Bund 10Y 30% |
| Equity Index | MSCI Europe (70%) |
| Bond | Bund 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 63.92% |
| Median Final Value | €428,468 |
| Mean Final Value | €1,115,627 |
| P5 Final Value | €0 |
| P95 Final Value | €4,462,032 |
| Failed Simulations | 36,077 (36.1%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.9 |
| Min Depletion Year | 10 |

---

#### 0402 – MSCI Europe 80% + Bund 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0402_block_notax_i_hicp_m_europe_b_de_8020.ipynb](src/0402_block_notax_i_hicp_m_europe_b_de_8020.ipynb) |
| Description | MSCI Europe 80% + Bund 10Y 20% |
| Equity Index | MSCI Europe (80%) |
| Bond | Bund 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 62.52% |
| Median Final Value | €447,219 |
| Mean Final Value | €1,381,899 |
| P5 Final Value | €0 |
| P95 Final Value | €5,758,632 |
| Failed Simulations | 37,477 (37.5%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 23.1 |
| Min Depletion Year | 9 |

---

#### 0403 – MSCI Europe 90% + Bund 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0403_block_notax_i_hicp_m_europe_b_de_9010.ipynb](src/0403_block_notax_i_hicp_m_europe_b_de_9010.ipynb) |
| Description | MSCI Europe 90% + Bund 10Y 10% |
| Equity Index | MSCI Europe (90%) |
| Bond | Bund 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 60.85% |
| Median Final Value | €434,461 |
| Mean Final Value | €1,678,483 |
| P5 Final Value | €0 |
| P95 Final Value | €7,274,934 |
| Failed Simulations | 39,146 (39.1%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 22.3 |
| Min Depletion Year | 8 |

---

#### 0404 – MSCI Europe 100%

| Parameter | Value |
|-----------|-------|
| Notebook | [0404_block_notax_i_hicp_m_europe_b_de_1000.ipynb](src/0404_block_notax_i_hicp_m_europe_b_de_1000.ipynb) |
| Description | MSCI Europe 100% |
| Equity Index | MSCI Europe (100%) |
| Bond | - |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 58.97% |
| Median Final Value | €393,783 |
| Mean Final Value | €2,007,341 |
| P5 Final Value | €0 |
| P95 Final Value | €9,013,865 |
| Failed Simulations | 41,027 (41.0%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 21.6 |
| Min Depletion Year | 7 |

---

#### 0405 – MSCI Europe 60% + BTP 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0405_block_notax_i_hicp_m_europe_b_it_6040.ipynb](src/0405_block_notax_i_hicp_m_europe_b_it_6040.ipynb) |
| Description | MSCI Europe 60% + BTP 10Y 40% |
| Equity Index | MSCI Europe (60%) |
| Bond | BTP 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 67.85% |
| Median Final Value | €566,126 |
| Mean Final Value | €1,227,077 |
| P5 Final Value | €0 |
| P95 Final Value | €4,677,971 |
| Failed Simulations | 32,147 (32.1%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.2 |
| Min Depletion Year | 11 |

---

#### 0406 – MSCI Europe 70% + BTP 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0406_block_notax_i_hicp_m_europe_b_it_7030.ipynb](src/0406_block_notax_i_hicp_m_europe_b_it_7030.ipynb) |
| Description | MSCI Europe 70% + BTP 10Y 30% |
| Equity Index | MSCI Europe (70%) |
| Bond | BTP 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 66.00% |
| Median Final Value | €562,083 |
| Mean Final Value | €1,404,050 |
| P5 Final Value | €0 |
| P95 Final Value | €5,584,709 |
| Failed Simulations | 34,003 (34.0%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.6 |
| Min Depletion Year | 10 |

---

#### 0407 – MSCI Europe 80% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0407_block_notax_i_hicp_m_europe_b_it_8020.ipynb](src/0407_block_notax_i_hicp_m_europe_b_it_8020.ipynb) |
| Description | MSCI Europe 80% + BTP 10Y 20% |
| Equity Index | MSCI Europe (80%) |
| Bond | BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 63.73% |
| Median Final Value | €532,579 |
| Mean Final Value | €1,593,587 |
| P5 Final Value | €0 |
| P95 Final Value | €6,613,002 |
| Failed Simulations | 36,268 (36.3%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 22.9 |
| Min Depletion Year | 9 |

---

#### 0408 – MSCI Europe 90% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0408_block_notax_i_hicp_m_europe_b_it_9010.ipynb](src/0408_block_notax_i_hicp_m_europe_b_it_9010.ipynb) |
| Description | MSCI Europe 90% + BTP 10Y 10% |
| Equity Index | MSCI Europe (90%) |
| Bond | BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 61.41% |
| Median Final Value | €472,065 |
| Mean Final Value | €1,794,887 |
| P5 Final Value | €0 |
| P95 Final Value | €7,769,048 |
| Failed Simulations | 38,585 (38.6%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 22.2 |
| Min Depletion Year | 8 |

---

#### 0409 – MSCI Europe 60% + Bund 10Y 20% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0409_block_notax_i_hicp_m_europe_b_deit_602020.ipynb](src/0409_block_notax_i_hicp_m_europe_b_deit_602020.ipynb) |
| Description | MSCI Europe 60% + Bund 10Y 20% + BTP 10Y 20% |
| Equity Index | MSCI Europe (60%) |
| Bond | Bund 10Y (20%) + BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 66.80% |
| Median Final Value | €482,433 |
| Mean Final Value | €1,045,166 |
| P5 Final Value | €0 |
| P95 Final Value | €3,978,196 |
| Failed Simulations | 33,200 (33.2%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.5 |
| Min Depletion Year | 11 |

---

#### 0410 – MSCI Europe 70% + Bund 10Y 15% + BTP 10Y 15%

| Parameter | Value |
|-----------|-------|
| Notebook | [0410_block_notax_i_hicp_m_europe_b_deit_701515.ipynb](src/0410_block_notax_i_hicp_m_europe_b_deit_701515.ipynb) |
| Description | MSCI Europe 70% + Bund 10Y 15% + BTP 10Y 15% |
| Equity Index | MSCI Europe (70%) |
| Bond | Bund 10Y (15%) + BTP 10Y (15%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 65.16% |
| Median Final Value | €498,546 |
| Mean Final Value | €1,255,451 |
| P5 Final Value | €0 |
| P95 Final Value | €5,003,890 |
| Failed Simulations | 34,842 (34.8%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.8 |
| Min Depletion Year | 10 |

---

#### 0411 – MSCI Europe 80% + Bund 10Y 10% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0411_block_notax_i_hicp_m_europe_b_deit_801010.ipynb](src/0411_block_notax_i_hicp_m_europe_b_deit_801010.ipynb) |
| Description | MSCI Europe 80% + Bund 10Y 10% + BTP 10Y 10% |
| Equity Index | MSCI Europe (80%) |
| Bond | Bund 10Y (10%) + BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 63.22% |
| Median Final Value | €490,738 |
| Mean Final Value | €1,485,709 |
| P5 Final Value | €0 |
| P95 Final Value | €6,179,467 |
| Failed Simulations | 36,782 (36.8%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 23.0 |
| Min Depletion Year | 9 |

---

#### 0412 – MSCI Europe 90% + Bund 10Y 5% + BTP 10Y 5%

| Parameter | Value |
|-----------|-------|
| Notebook | [0412_block_notax_i_hicp_m_europe_b_deit_900505.ipynb](src/0412_block_notax_i_hicp_m_europe_b_deit_900505.ipynb) |
| Description | MSCI Europe 90% + Bund 10Y 5% + BTP 10Y 5% |
| Equity Index | MSCI Europe (90%) |
| Bond | Bund 10Y (5%) + BTP 10Y (5%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 61.19% |
| Median Final Value | €453,207 |
| Mean Final Value | €1,736,154 |
| P5 Final Value | €0 |
| P95 Final Value | €7,520,112 |
| Failed Simulations | 38,808 (38.8%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 22.3 |
| Min Depletion Year | 8 |

---

### 05xx – MSCI EMU NET

#### 0500 – MSCI EMU 60% + Bund 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0500_block_notax_i_hicp_m_emu_b_de_6040.ipynb](src/0500_block_notax_i_hicp_m_emu_b_de_6040.ipynb) |
| Description | MSCI EMU 60% + Bund 10Y 40% |
| Equity Index | MSCI EMU (60%) |
| Bond | Bund 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 60.88% |
| Median Final Value | €294,456 |
| Mean Final Value | €891,975 |
| P5 Final Value | €0 |
| P95 Final Value | €3,651,181 |
| Failed Simulations | 39,123 (39.1%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 24.1 |
| Min Depletion Year | 11 |

---

#### 0501 – MSCI EMU 70% + Bund 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0501_block_notax_i_hicp_m_emu_b_de_7030.ipynb](src/0501_block_notax_i_hicp_m_emu_b_de_7030.ipynb) |
| Description | MSCI EMU 70% + Bund 10Y 30% |
| Equity Index | MSCI EMU (70%) |
| Bond | Bund 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 59.51% |
| Median Final Value | €301,911 |
| Mean Final Value | €1,132,049 |
| P5 Final Value | €0 |
| P95 Final Value | €4,859,156 |
| Failed Simulations | 40,487 (40.5%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 23.2 |
| Min Depletion Year | 10 |

---

#### 0502 – MSCI EMU 80% + Bund 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0502_block_notax_i_hicp_m_emu_b_de_8020.ipynb](src/0502_block_notax_i_hicp_m_emu_b_de_8020.ipynb) |
| Description | MSCI EMU 80% + Bund 10Y 20% |
| Equity Index | MSCI EMU (80%) |
| Bond | Bund 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 57.72% |
| Median Final Value | €278,820 |
| Mean Final Value | €1,400,590 |
| P5 Final Value | €0 |
| P95 Final Value | €6,260,657 |
| Failed Simulations | 42,278 (42.3%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 22.4 |
| Min Depletion Year | 8 |

---

#### 0503 – MSCI EMU 90% + Bund 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0503_block_notax_i_hicp_m_emu_b_de_9010.ipynb](src/0503_block_notax_i_hicp_m_emu_b_de_9010.ipynb) |
| Description | MSCI EMU 90% + Bund 10Y 10% |
| Equity Index | MSCI EMU (90%) |
| Bond | Bund 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 55.78% |
| Median Final Value | €231,278 |
| Mean Final Value | €1,698,954 |
| P5 Final Value | €0 |
| P95 Final Value | €7,863,575 |
| Failed Simulations | 44,218 (44.2%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 21.6 |
| Min Depletion Year | 7 |

---

#### 0504 – MSCI EMU 100%

| Parameter | Value |
|-----------|-------|
| Notebook | [0504_block_notax_i_hicp_m_emu_b_de_1000.ipynb](src/0504_block_notax_i_hicp_m_emu_b_de_1000.ipynb) |
| Description | MSCI EMU 100% |
| Equity Index | MSCI EMU (100%) |
| Bond | - |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 53.57% |
| Median Final Value | €156,499 |
| Mean Final Value | €2,028,953 |
| P5 Final Value | €0 |
| P95 Final Value | €9,649,433 |
| Failed Simulations | 46,431 (46.4%) |
| Median Depletion Year | 21 |
| Mean Depletion Year | 20.8 |
| Min Depletion Year | 6 |

---

#### 0505 – MSCI EMU 60% + BTP 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0505_block_notax_i_hicp_m_emu_b_it_6040.ipynb](src/0505_block_notax_i_hicp_m_emu_b_it_6040.ipynb) |
| Description | MSCI EMU 60% + BTP 10Y 40% |
| Equity Index | MSCI EMU (60%) |
| Bond | BTP 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 63.57% |
| Median Final Value | €442,670 |
| Mean Final Value | €1,250,384 |
| P5 Final Value | €0 |
| P95 Final Value | €5,096,950 |
| Failed Simulations | 36,434 (36.4%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.5 |
| Min Depletion Year | 10 |

---

#### 0506 – MSCI EMU 70% + BTP 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0506_block_notax_i_hicp_m_emu_b_it_7030.ipynb](src/0506_block_notax_i_hicp_m_emu_b_it_7030.ipynb) |
| Description | MSCI EMU 70% + BTP 10Y 30% |
| Equity Index | MSCI EMU (70%) |
| Bond | BTP 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 61.27% |
| Median Final Value | €408,498 |
| Mean Final Value | €1,429,125 |
| P5 Final Value | €0 |
| P95 Final Value | €6,121,198 |
| Failed Simulations | 38,735 (38.7%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 22.9 |
| Min Depletion Year | 9 |

---

#### 0507 – MSCI EMU 80% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0507_block_notax_i_hicp_m_emu_b_it_8020.ipynb](src/0507_block_notax_i_hicp_m_emu_b_it_8020.ipynb) |
| Description | MSCI EMU 80% + BTP 10Y 20% |
| Equity Index | MSCI EMU (80%) |
| Bond | BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 58.78% |
| Median Final Value | €347,077 |
| Mean Final Value | €1,619,083 |
| P5 Final Value | €0 |
| P95 Final Value | €7,206,664 |
| Failed Simulations | 41,216 (41.2%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 22.2 |
| Min Depletion Year | 8 |

---

#### 0508 – MSCI EMU 90% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0508_block_notax_i_hicp_m_emu_b_it_9010.ipynb](src/0508_block_notax_i_hicp_m_emu_b_it_9010.ipynb) |
| Description | MSCI EMU 90% + BTP 10Y 10% |
| Equity Index | MSCI EMU (90%) |
| Bond | BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 56.22% |
| Median Final Value | €260,847 |
| Mean Final Value | €1,819,311 |
| P5 Final Value | €0 |
| P95 Final Value | €8,401,366 |
| Failed Simulations | 43,785 (43.8%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 21.5 |
| Min Depletion Year | 7 |

---

#### 0509 – MSCI EMU 60% + Bund 10Y 20% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0509_block_notax_i_hicp_m_emu_b_deit_602020.ipynb](src/0509_block_notax_i_hicp_m_emu_b_deit_602020.ipynb) |
| Description | MSCI EMU 60% + Bund 10Y 20% + BTP 10Y 20% |
| Equity Index | MSCI EMU (60%) |
| Bond | Bund 10Y (20%) + BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 62.52% |
| Median Final Value | €375,056 |
| Mean Final Value | €1,063,453 |
| P5 Final Value | €0 |
| P95 Final Value | €4,328,587 |
| Failed Simulations | 37,478 (37.5%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.8 |
| Min Depletion Year | 10 |

---

#### 0510 – MSCI EMU 70% + Bund 10Y 15% + BTP 10Y 15%

| Parameter | Value |
|-----------|-------|
| Notebook | [0510_block_notax_i_hicp_m_emu_b_deit_701515.ipynb](src/0510_block_notax_i_hicp_m_emu_b_deit_701515.ipynb) |
| Description | MSCI EMU 70% + Bund 10Y 15% + BTP 10Y 15% |
| Equity Index | MSCI EMU (70%) |
| Bond | Bund 10Y (15%) + BTP 10Y (15%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 60.54% |
| Median Final Value | €358,693 |
| Mean Final Value | €1,276,027 |
| P5 Final Value | €0 |
| P95 Final Value | €5,456,871 |
| Failed Simulations | 39,459 (39.5%) |
| Median Depletion Year | 23 |
| Mean Depletion Year | 23.1 |
| Min Depletion Year | 9 |

---

#### 0511 – MSCI EMU 80% + Bund 10Y 10% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0511_block_notax_i_hicp_m_emu_b_deit_801010.ipynb](src/0511_block_notax_i_hicp_m_emu_b_deit_801010.ipynb) |
| Description | MSCI EMU 80% + Bund 10Y 10% + BTP 10Y 10% |
| Equity Index | MSCI EMU (80%) |
| Bond | Bund 10Y (10%) + BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 58.31% |
| Median Final Value | €315,216 |
| Mean Final Value | €1,507,696 |
| P5 Final Value | €0 |
| P95 Final Value | €6,728,939 |
| Failed Simulations | 41,685 (41.7%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 22.3 |
| Min Depletion Year | 8 |

---

#### 0512 – MSCI EMU 90% + Bund 10Y 5% + BTP 10Y 5%

| Parameter | Value |
|-----------|-------|
| Notebook | [0512_block_notax_i_hicp_m_emu_b_deit_900505.ipynb](src/0512_block_notax_i_hicp_m_emu_b_deit_900505.ipynb) |
| Description | MSCI EMU 90% + Bund 10Y 5% + BTP 10Y 5% |
| Equity Index | MSCI EMU (90%) |
| Bond | Bund 10Y (5%) + BTP 10Y (5%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 4.0% |

**Results @ 4% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 56.00% |
| Median Final Value | €245,658 |
| Mean Final Value | €1,758,570 |
| P5 Final Value | €0 |
| P95 Final Value | €8,126,117 |
| Failed Simulations | 44,000 (44.0%) |
| Median Depletion Year | 22 |
| Mean Depletion Year | 21.5 |
| Min Depletion Year | 7 |

---

### 06xx – MSCI World NET (3% WR)

#### 0600 – MSCI World 60% + Bund 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0600_block_notax_i_hicp_3_m_world_b_de_6040.ipynb](src/0600_block_notax_i_hicp_3_m_world_b_de_6040.ipynb) |
| Description | MSCI World 60% + Bund 10Y 40% |
| Equity Index | MSCI World (60%) |
| Bond | Bund 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 95.82% |
| Median Final Value | €1,850,878 |
| Mean Final Value | €2,301,669 |
| P5 Final Value | €58,916 |
| P95 Final Value | €6,024,803 |
| Failed Simulations | 4,178 (4.2%) |
| Median Depletion Year | 27 |
| Mean Depletion Year | 26.7 |
| Min Depletion Year | 14 |

---

#### 0601 – MSCI World 70% + Bund 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0601_block_notax_i_hicp_3_m_world_b_de_7030.ipynb](src/0601_block_notax_i_hicp_3_m_world_b_de_7030.ipynb) |
| Description | MSCI World 70% + Bund 10Y 30% |
| Equity Index | MSCI World (70%) |
| Bond | Bund 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 94.43% |
| Median Final Value | €2,096,234 |
| Mean Final Value | €2,798,778 |
| P5 Final Value | €0 |
| P95 Final Value | €7,920,764 |
| Failed Simulations | 5,572 (5.6%) |
| Median Depletion Year | 27 |
| Mean Depletion Year | 26.0 |
| Min Depletion Year | 13 |

---

#### 0602 – MSCI World 80% + Bund 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0602_block_notax_i_hicp_3_m_world_b_de_8020.ipynb](src/0602_block_notax_i_hicp_3_m_world_b_de_8020.ipynb) |
| Description | MSCI World 80% + Bund 10Y 20% |
| Equity Index | MSCI World (80%) |
| Bond | Bund 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 92.75% |
| Median Final Value | €2,331,297 |
| Mean Final Value | €3,376,173 |
| P5 Final Value | €0 |
| P95 Final Value | €10,306,788 |
| Failed Simulations | 7,249 (7.2%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.3 |
| Min Depletion Year | 12 |

---

#### 0603 – MSCI World 90% + Bund 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0603_block_notax_i_hicp_3_m_world_b_de_9010.ipynb](src/0603_block_notax_i_hicp_3_m_world_b_de_9010.ipynb) |
| Description | MSCI World 90% + Bund 10Y 10% |
| Equity Index | MSCI World (90%) |
| Bond | Bund 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 90.99% |
| Median Final Value | €2,540,817 |
| Mean Final Value | €4,045,800 |
| P5 Final Value | €0 |
| P95 Final Value | €13,245,858 |
| Failed Simulations | 9,007 (9.0%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.6 |
| Min Depletion Year | 11 |

---

#### 0604 – MSCI World 100%

| Parameter | Value |
|-----------|-------|
| Notebook | [0604_block_notax_i_hicp_3_m_world_b_de_1000.ipynb](src/0604_block_notax_i_hicp_3_m_world_b_de_1000.ipynb) |
| Description | MSCI World 100% |
| Equity Index | MSCI World (100%) |
| Bond | - |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 89.11% |
| Median Final Value | €2,724,769 |
| Mean Final Value | €4,821,149 |
| P5 Final Value | €0 |
| P95 Final Value | €16,775,930 |
| Failed Simulations | 10,892 (10.9%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.9 |
| Min Depletion Year | 9 |

---

#### 0605 – MSCI World 60% + BTP 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0605_block_notax_i_hicp_3_m_world_b_it_6040.ipynb](src/0605_block_notax_i_hicp_3_m_world_b_it_6040.ipynb) |
| Description | MSCI World 60% + BTP 10Y 40% |
| Equity Index | MSCI World (60%) |
| Bond | BTP 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 95.71% |
| Median Final Value | €2,210,116 |
| Mean Final Value | €2,864,884 |
| P5 Final Value | €55,971 |
| P95 Final Value | €7,821,560 |
| Failed Simulations | 4,291 (4.3%) |
| Median Depletion Year | 27 |
| Mean Depletion Year | 26.2 |
| Min Depletion Year | 14 |

---

#### 0606 – MSCI World 70% + BTP 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0606_block_notax_i_hicp_3_m_world_b_it_7030.ipynb](src/0606_block_notax_i_hicp_3_m_world_b_it_7030.ipynb) |
| Description | MSCI World 70% + BTP 10Y 30% |
| Equity Index | MSCI World (70%) |
| Bond | BTP 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 94.48% |
| Median Final Value | €2,391,411 |
| Mean Final Value | €3,283,781 |
| P5 Final Value | €0 |
| P95 Final Value | €9,523,669 |
| Failed Simulations | 5,519 (5.5%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.7 |
| Min Depletion Year | 13 |

---

#### 0607 – MSCI World 80% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0607_block_notax_i_hicp_3_m_world_b_it_8020.ipynb](src/0607_block_notax_i_hicp_3_m_world_b_it_8020.ipynb) |
| Description | MSCI World 80% + BTP 10Y 20% |
| Equity Index | MSCI World (80%) |
| Bond | BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 92.88% |
| Median Final Value | €2,536,276 |
| Mean Final Value | €3,746,867 |
| P5 Final Value | €0 |
| P95 Final Value | €11,567,912 |
| Failed Simulations | 7,123 (7.1%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.2 |
| Min Depletion Year | 12 |

---

#### 0608 – MSCI World 90% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0608_block_notax_i_hicp_3_m_world_b_it_9010.ipynb](src/0608_block_notax_i_hicp_3_m_world_b_it_9010.ipynb) |
| Description | MSCI World 90% + BTP 10Y 10% |
| Equity Index | MSCI World (90%) |
| Bond | BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 91.10% |
| Median Final Value | €2,653,424 |
| Mean Final Value | €4,258,044 |
| P5 Final Value | €0 |
| P95 Final Value | €13,988,541 |
| Failed Simulations | 8,903 (8.9%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.5 |
| Min Depletion Year | 11 |

---

#### 0609 – MSCI World 60% + Bund 10Y 20% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0609_block_notax_i_hicp_3_m_world_b_deit_602020.ipynb](src/0609_block_notax_i_hicp_3_m_world_b_deit_602020.ipynb) |
| Description | MSCI World 60% + Bund 10Y 20% + BTP 10Y 20% |
| Equity Index | MSCI World (60%) |
| Bond | Bund 10Y (20%) + BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 95.91% |
| Median Final Value | €2,038,282 |
| Mean Final Value | €2,576,896 |
| P5 Final Value | €70,092 |
| P95 Final Value | €6,839,761 |
| Failed Simulations | 4,089 (4.1%) |
| Median Depletion Year | 27 |
| Mean Depletion Year | 26.5 |
| Min Depletion Year | 14 |

---

#### 0610 – MSCI World 70% + Bund 10Y 15% + BTP 10Y 15%

| Parameter | Value |
|-----------|-------|
| Notebook | [0610_block_notax_i_hicp_3_m_world_b_deit_701515.ipynb](src/0610_block_notax_i_hicp_3_m_world_b_deit_701515.ipynb) |
| Description | MSCI World 70% + Bund 10Y 15% + BTP 10Y 15% |
| Equity Index | MSCI World (70%) |
| Bond | Bund 10Y (15%) + BTP 10Y (15%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 94.54% |
| Median Final Value | €2,250,315 |
| Mean Final Value | €3,037,100 |
| P5 Final Value | €0 |
| P95 Final Value | €8,671,513 |
| Failed Simulations | 5,463 (5.5%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.9 |
| Min Depletion Year | 13 |

---

#### 0611 – MSCI World 80% + Bund 10Y 10% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0611_block_notax_i_hicp_3_m_world_b_deit_801010.ipynb](src/0611_block_notax_i_hicp_3_m_world_b_deit_801010.ipynb) |
| Description | MSCI World 80% + Bund 10Y 10% + BTP 10Y 10% |
| Equity Index | MSCI World (80%) |
| Bond | Bund 10Y (10%) + BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 92.83% |
| Median Final Value | €2,435,778 |
| Mean Final Value | €3,559,366 |
| P5 Final Value | €0 |
| P95 Final Value | €10,901,537 |
| Failed Simulations | 7,166 (7.2%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.3 |
| Min Depletion Year | 12 |

---

#### 0612 – MSCI World 90% + Bund 10Y 5% + BTP 10Y 5%

| Parameter | Value |
|-----------|-------|
| Notebook | [0612_block_notax_i_hicp_3_m_world_b_deit_900505.ipynb](src/0612_block_notax_i_hicp_3_m_world_b_deit_900505.ipynb) |
| Description | MSCI World 90% + Bund 10Y 5% + BTP 10Y 5% |
| Equity Index | MSCI World (90%) |
| Bond | Bund 10Y (5%) + BTP 10Y (5%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.0% |

**Results @ 3% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 91.05% |
| Median Final Value | €2,599,385 |
| Mean Final Value | €4,151,293 |
| P5 Final Value | €0 |
| P95 Final Value | €13,611,084 |
| Failed Simulations | 8,946 (8.9%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.6 |
| Min Depletion Year | 11 |

---

### 07xx – MSCI World NET (3.5% WR)

#### 0700 – MSCI World 60% + Bund 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0700_block_notax_i_hicp_35_m_world_b_de_6040.ipynb](src/0700_block_notax_i_hicp_35_m_world_b_de_6040.ipynb) |
| Description | MSCI World 60% + Bund 10Y 40% |
| Equity Index | MSCI World (60%) |
| Bond | Bund 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 89.08% |
| Median Final Value | €1,371,863 |
| Mean Final Value | €1,823,449 |
| P5 Final Value | €0 |
| P95 Final Value | €5,279,421 |
| Failed Simulations | 10,924 (10.9%) |
| Median Depletion Year | 27 |
| Mean Depletion Year | 26.1 |
| Min Depletion Year | 13 |

---

#### 0701 – MSCI World 70% + Bund 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0701_block_notax_i_hicp_35_m_world_b_de_7030.ipynb](src/0701_block_notax_i_hicp_35_m_world_b_de_7030.ipynb) |
| Description | MSCI World 70% + Bund 10Y 30% |
| Equity Index | MSCI World (70%) |
| Bond | Bund 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 87.74% |
| Median Final Value | €1,594,504 |
| Mean Final Value | €2,285,406 |
| P5 Final Value | €0 |
| P95 Final Value | €7,043,332 |
| Failed Simulations | 12,261 (12.3%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.4 |
| Min Depletion Year | 12 |

---

#### 0702 – MSCI World 80% + Bund 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0702_block_notax_i_hicp_35_m_world_b_de_8020.ipynb](src/0702_block_notax_i_hicp_35_m_world_b_de_8020.ipynb) |
| Description | MSCI World 80% + Bund 10Y 20% |
| Equity Index | MSCI World (80%) |
| Bond | Bund 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 92.75% |
| Median Final Value | €2,331,297 |
| Mean Final Value | €3,376,173 |
| P5 Final Value | €0 |
| P95 Final Value | €10,306,788 |
| Failed Simulations | 7,249 (7.2%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.3 |
| Min Depletion Year | 12 |

---

#### 0703 – MSCI World 90% + Bund 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0703_block_notax_i_hicp_35_m_world_b_de_9010.ipynb](src/0703_block_notax_i_hicp_35_m_world_b_de_9010.ipynb) |
| Description | MSCI World 90% + Bund 10Y 10% |
| Equity Index | MSCI World (90%) |
| Bond | Bund 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 90.99% |
| Median Final Value | €2,540,817 |
| Mean Final Value | €4,045,800 |
| P5 Final Value | €0 |
| P95 Final Value | €13,245,858 |
| Failed Simulations | 9,007 (9.0%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.6 |
| Min Depletion Year | 11 |

---

#### 0704 – MSCI World 100%

| Parameter | Value |
|-----------|-------|
| Notebook | [0704_block_notax_i_hicp_35_m_world_b_de_1000.ipynb](src/0704_block_notax_i_hicp_35_m_world_b_de_1000.ipynb) |
| Description | MSCI World 100% |
| Equity Index | MSCI World (100%) |
| Bond | - |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 89.11% |
| Median Final Value | €2,724,769 |
| Mean Final Value | €4,821,149 |
| P5 Final Value | €0 |
| P95 Final Value | €16,775,930 |
| Failed Simulations | 10,892 (10.9%) |
| Median Depletion Year | 24 |
| Mean Depletion Year | 23.9 |
| Min Depletion Year | 9 |

---

#### 0705 – MSCI World 60% + BTP 10Y 40%

| Parameter | Value |
|-----------|-------|
| Notebook | [0705_block_notax_i_hicp_35_m_world_b_it_6040.ipynb](src/0705_block_notax_i_hicp_35_m_world_b_it_6040.ipynb) |
| Description | MSCI World 60% + BTP 10Y 40% |
| Equity Index | MSCI World (60%) |
| Bond | BTP 10Y (40%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 95.71% |
| Median Final Value | €2,210,116 |
| Mean Final Value | €2,864,884 |
| P5 Final Value | €55,971 |
| P95 Final Value | €7,821,560 |
| Failed Simulations | 4,291 (4.3%) |
| Median Depletion Year | 27 |
| Mean Depletion Year | 26.2 |
| Min Depletion Year | 14 |

---

#### 0706 – MSCI World 70% + BTP 10Y 30%

| Parameter | Value |
|-----------|-------|
| Notebook | [0706_block_notax_i_hicp_35_m_world_b_it_7030.ipynb](src/0706_block_notax_i_hicp_35_m_world_b_it_7030.ipynb) |
| Description | MSCI World 70% + BTP 10Y 30% |
| Equity Index | MSCI World (70%) |
| Bond | BTP 10Y (30%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 94.48% |
| Median Final Value | €2,391,411 |
| Mean Final Value | €3,283,781 |
| P5 Final Value | €0 |
| P95 Final Value | €9,523,669 |
| Failed Simulations | 5,519 (5.5%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.7 |
| Min Depletion Year | 13 |

---

#### 0707 – MSCI World 80% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0707_block_notax_i_hicp_35_m_world_b_it_8020.ipynb](src/0707_block_notax_i_hicp_35_m_world_b_it_8020.ipynb) |
| Description | MSCI World 80% + BTP 10Y 20% |
| Equity Index | MSCI World (80%) |
| Bond | BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 92.88% |
| Median Final Value | €2,536,276 |
| Mean Final Value | €3,746,867 |
| P5 Final Value | €0 |
| P95 Final Value | €11,567,912 |
| Failed Simulations | 7,123 (7.1%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.2 |
| Min Depletion Year | 12 |

---

#### 0708 – MSCI World 90% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0708_block_notax_i_hicp_35_m_world_b_it_9010.ipynb](src/0708_block_notax_i_hicp_35_m_world_b_it_9010.ipynb) |
| Description | MSCI World 90% + BTP 10Y 10% |
| Equity Index | MSCI World (90%) |
| Bond | BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 91.10% |
| Median Final Value | €2,653,424 |
| Mean Final Value | €4,258,044 |
| P5 Final Value | €0 |
| P95 Final Value | €13,988,541 |
| Failed Simulations | 8,903 (8.9%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.5 |
| Min Depletion Year | 11 |

---

#### 0709 – MSCI World 60% + Bund 10Y 20% + BTP 10Y 20%

| Parameter | Value |
|-----------|-------|
| Notebook | [0709_block_notax_i_hicp_35_m_world_b_deit_602020.ipynb](src/0709_block_notax_i_hicp_35_m_world_b_deit_602020.ipynb) |
| Description | MSCI World 60% + Bund 10Y 20% + BTP 10Y 20% |
| Equity Index | MSCI World (60%) |
| Bond | Bund 10Y (20%) + BTP 10Y (20%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 95.91% |
| Median Final Value | €2,038,282 |
| Mean Final Value | €2,576,896 |
| P5 Final Value | €70,092 |
| P95 Final Value | €6,839,761 |
| Failed Simulations | 4,089 (4.1%) |
| Median Depletion Year | 27 |
| Mean Depletion Year | 26.5 |
| Min Depletion Year | 14 |

---

#### 0710 – MSCI World 70% + Bund 10Y 15% + BTP 10Y 15%

| Parameter | Value |
|-----------|-------|
| Notebook | [0710_block_notax_i_hicp_35_m_world_b_deit_701515.ipynb](src/0710_block_notax_i_hicp_35_m_world_b_deit_701515.ipynb) |
| Description | MSCI World 70% + Bund 10Y 15% + BTP 10Y 15% |
| Equity Index | MSCI World (70%) |
| Bond | Bund 10Y (15%) + BTP 10Y (15%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 94.54% |
| Median Final Value | €2,250,315 |
| Mean Final Value | €3,037,100 |
| P5 Final Value | €0 |
| P95 Final Value | €8,671,513 |
| Failed Simulations | 5,463 (5.5%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.9 |
| Min Depletion Year | 13 |

---

#### 0711 – MSCI World 80% + Bund 10Y 10% + BTP 10Y 10%

| Parameter | Value |
|-----------|-------|
| Notebook | [0711_block_notax_i_hicp_35_m_world_b_deit_801010.ipynb](src/0711_block_notax_i_hicp_35_m_world_b_deit_801010.ipynb) |
| Description | MSCI World 80% + Bund 10Y 10% + BTP 10Y 10% |
| Equity Index | MSCI World (80%) |
| Bond | Bund 10Y (10%) + BTP 10Y (10%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 92.83% |
| Median Final Value | €2,435,778 |
| Mean Final Value | €3,559,366 |
| P5 Final Value | €0 |
| P95 Final Value | €10,901,537 |
| Failed Simulations | 7,166 (7.2%) |
| Median Depletion Year | 26 |
| Mean Depletion Year | 25.3 |
| Min Depletion Year | 12 |

---

#### 0712 – MSCI World 90% + Bund 10Y 5% + BTP 10Y 5%

| Parameter | Value |
|-----------|-------|
| Notebook | [0712_block_notax_i_hicp_35_m_world_b_deit_900505.ipynb](src/0712_block_notax_i_hicp_35_m_world_b_deit_900505.ipynb) |
| Description | MSCI World 90% + Bund 10Y 5% + BTP 10Y 5% |
| Equity Index | MSCI World (90%) |
| Bond | Bund 10Y (5%) + BTP 10Y (5%) |
| Inflation | HICP Euro Area |
| Tax Status | No Tax |
| Data Period | 2000-12-30 → 2025-10-31 |
| Simulations | 100,000 |
| Withdrawal Rate | 3.5% |

**Results @ 3.5% WR:**

| Metric | Value |
|--------|-------|
| Success Rate | 91.05% |
| Median Final Value | €2,599,385 |
| Mean Final Value | €4,151,293 |
| P5 Final Value | €0 |
| P95 Final Value | €13,611,084 |
| Failed Simulations | 8,946 (8.9%) |
| Median Depletion Year | 25 |
| Mean Depletion Year | 24.6 |
| Min Depletion Year | 11 |

---
