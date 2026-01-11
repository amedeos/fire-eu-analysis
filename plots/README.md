# Analysis Plots

Visualizzazioni generate da `src/tools/plots.py` a partire dai dati di `ANALYSIS_REGISTRY.csv`.

**Nota:** I dati STOXX Europe 600 (notebook 03xx) sono esclusi da tutti i plot.

---

## 01 - Success Rate vs Withdrawal Rate

![01_success_rate_vs_wr.png](01_success_rate_vs_wr.png)

**Descrizione:** Confronto diretto dell'impatto del withdrawal rate (3%, 3.5%, 4%) sul success rate per i portafogli MSCI World + Bund.

**Dati:** MSCI World + Bund, allocazioni 60/40, 70/30, 80/20, 90/10

**Insight principali:**
- Il passaggio da 4% a 3% WR aumenta il success rate di ~17-19 punti percentuali
- A parità di WR, allocazioni più conservative (60/40) tendono ad avere success rate leggermente superiori
- Il 3% WR garantisce success rate >90% per tutte le allocazioni

---

## 02 - Success Rate vs Allocation

![02_success_rate_vs_allocation.png](02_success_rate_vs_allocation.png)

**Descrizione:** Come varia il success rate al variare della percentuale di equity nel portafoglio (da 60% a 100%).

**Dati:** Tutti gli indici equity con bond singoli, 4% WR

**Insight principali:**
- Non esiste una relazione lineare tra % equity e success rate
- Per gli indici globali (World, ACWI), allocazioni moderate (60-70%) tendono a performare meglio
- Per gli indici europei, il pattern è meno definito
- Il 100% equity non è necessariamente la scelta ottimale

---

## 03 - Success Rate by Equity Index

![03_success_rate_by_equity_index.png](03_success_rate_by_equity_index.png)

**Descrizione:** Confronto del success rate tra i diversi indici azionari a parità di altre condizioni.

**Dati:** Allocazione 60/40, Bund, 4% WR

**Insight principali:**
- MSCI World performa meglio (78.3%)
- MSCI ACWI è secondo (77.0%)
- Gli indici puramente europei (Europe, EMU) hanno success rate significativamente inferiori (~61-65%)
- La diversificazione geografica globale migliora la sostenibilità del portafoglio

---

## 04 - Success Rate by Bond Type

![04_success_rate_by_bond_type.png](04_success_rate_by_bond_type.png)

**Descrizione:** Confronto tra diversi tipi di obbligazioni (Bund tedesco, BTP italiano, mix) a parità di indice equity.

**Dati:** MSCI World, 4% WR, varie allocazioni

**Insight principali:**
- I BTP italiani tendono a generare success rate superiori rispetto ai Bund tedeschi
- Il mix Bund+BTP offre risultati intermedi
- La differenza è più marcata per allocazioni con maggiore peso obbligazionario
- Il maggior rendimento dei BTP compensa il rischio di credito nel periodo analizzato (2000-2025)

---

## 05 - Heatmap Success Rate

![05_heatmap_success_rate.png](05_heatmap_success_rate.png)

**Descrizione:** Visione d'insieme di tutte le combinazioni portafoglio/allocazione in un'unica heatmap.

**Dati:** Tutti i portafogli con bond singoli, 4% WR

**Insight principali:**
- Colori verdi = success rate elevato (>80%)
- Colori rossi = success rate basso (<60%)
- Permette di identificare rapidamente le combinazioni ottimali
- I portafogli con indici globali dominano la parte superiore (success rate più alti)

---

## 06 - Final Value Distribution

![06_final_value_distribution.png](06_final_value_distribution.png)

**Descrizione:** Distribuzione dei valori finali del portafoglio dopo 30 anni, mostrando mediana, media e intervallo P5-P95.

**Dati:** MSCI World + Bund, 4% WR

**Insight principali:**
- La media è sempre superiore alla mediana (distribuzione asimmetrica positiva)
- L'intervallo P5-P95 si amplia con allocazioni più aggressive
- Allocazioni più aggressive generano valori finali mediani più alti ma con maggiore dispersione
- Il P5 (worst case) può essere €0 per allocazioni aggressive (portafoglio esaurito)

---

## 07 - Risk/Return Trade-off

![07_risk_return_tradeoff.png](07_risk_return_tradeoff.png)

**Descrizione:** Scatter plot che mostra il trade-off tra success rate (sicurezza) e valore finale mediano (rendimento).

**Dati:** Tutti i portafogli, 4% WR

**Insight principali:**
- Ogni punto rappresenta un portafoglio
- Quadrante in alto a destra = portafogli ottimali (alto success rate E alto valore finale)
- I portafogli con indici globali (World, ACWI) si posizionano meglio
- Esiste un trade-off: portafogli più aggressivi hanno valori finali più alti ma success rate inferiori

---

## 08 - Depletion Year Analysis

![08_depletion_year_analysis.png](08_depletion_year_analysis.png)

**Descrizione:** Analisi degli scenari falliti: in quale anno il portafoglio si esaurisce.

**Dati:** Portafogli con simulazioni fallite, 4% WR

**Pannello sinistro:** Media dell'anno di depletion per indice equity
**Pannello destro:** Min, Mean, Median depletion year per MSCI World

**Insight principali:**
- Il depletion avviene tipicamente tra l'anno 22 e 27 (su orizzonte 30 anni)
- Il worst case (Min) può essere già all'anno 7-14 per portafogli aggressivi
- Gli indici europei hanno depletion year leggermente anticipati
- Utile per capire "quanto tempo ho" in caso di scenario avverso

---

## 09 - WR Comparison Summary

![09_wr_comparison_summary.png](09_wr_comparison_summary.png)

**Descrizione:** Riepilogo dell'impatto del withdrawal rate su success rate e valore finale mediano.

**Dati:** MSCI World + Bund 60/40, tutti i WR disponibili

**Insight principali:**
- Doppio asse Y: success rate (blu) e valore finale mediano (verde)
- WR più bassi = success rate più alti MA valori finali più alti (più capitale residuo)
- Il 3% WR lascia un capitale mediano di ~€1.85M dopo 30 anni
- Il 4% WR lascia un capitale mediano di ~€0.9M dopo 30 anni
- Trade-off tra "sicurezza" e "godimento del capitale"

---

## Rigenerazione dei Plot

Per rigenerare tutti i plot:

```bash
./venv/bin/python src/tools/plots.py
```

Opzioni disponibili:
- `--input FILE`: Specifica un file CSV diverso
- `--output-dir DIR`: Specifica una directory di output diversa
- `-v`: Modalità verbose

---

## Note Metodologiche

- **Periodo dati:** 2000-2025
- **Simulazioni:** 100,000 Monte Carlo con block bootstrap (blocchi da 6 mesi)
- **Orizzonte:** 30 anni
- **Success rate:** % di simulazioni in cui il portafoglio sopravvive 30 anni
- **Inflazione:** HICP Euro Area (aggiustamento lagged)
