---
title: "Vinkvalitetsanalyse – BI"
weight: 7
---

Et business intelligence-projekt der analyserer kemiske egenskaber i rød- og hvidvin for at identificere, hvad der driver oplevet kvalitet. Projektet gennemfører hele data science-arbejdsgangen fra dataindsamling og rensning til statistisk validering og konklusion.

Analysen viser, at alkohol er den stærkeste kvalitetsprediktor, mens flygtig syre er den primære negativ faktor. Hvidvine indeholder i gennemsnit højere alkohol- og syreindhold end rødvine — på trods af den gængse opfattelse.

## Metode

- Hypotesetestning med statistiske T-tests
- Feature-analyse og fjernelse af redundante variable (densitet, total SO2)
- Sammenligning af tre normaliseringsmetoder — robust scaling fungerede bedst til outlier-tunge data

**Teknologier:** Python · Pandas · NumPy · SciPy · Scikit-learn · Matplotlib · Seaborn

<a href="https://github.com/AsgerSH/SP1-Wine-Analysis" target="_blank" rel="noreferrer">Se på GitHub</a>
