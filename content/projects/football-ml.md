---
title: "Fodbold ML – Eksamensanalyse"
weight: 9
---

Et maskinlærings-eksamensprojekt der analyserer fodboldkampes udfald baseret på vejr, hjemmebane-fordel, disciplin og standardsituationer. Resultaterne præsenteres i et interaktivt Streamlit-dashboard — tilgængeligt live på nettet.

Projektet anvender både superviserede og ikke-superviserede teknikker og besvarer tre centrale spørgsmål: hvilke faktorer påvirker kampresultater mest, hvordan forudsiger offensive nøgletal holdsucces, og kan ML identificere taktiske profiler og spillestile?

## Modeller

- **Logistisk regression** til prediktion af kampudfald og "dirty game"-klassificering
- **Random Forest** til feature importance i kampsucces
- **K-Means clustering** til gruppering af hold efter taktisk profil
- **PCA** til dimensionsreduktion og visualisering

**Teknologier:** Python · Streamlit · Pandas · NumPy · Scikit-learn · SciPy · Statsmodels · Matplotlib · Seaborn

<a href="https://footballexam.streamlit.app" target="_blank" rel="noreferrer">Se live demo</a> &nbsp;·&nbsp; <a href="https://github.com/AsgerSH/Football_MachineLearning_exam" target="_blank" rel="noreferrer">Se på GitHub</a>
