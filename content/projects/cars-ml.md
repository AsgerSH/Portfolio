---
title: "Brugtbilsanalyse – ML"
weight: 6
---

En maskinlæringsanalyse af det danske brugtbilsmarked med fokus på prisfastsættelse og markeds-segmentering. Projektet anvender tre forskellige ML-modeller og identificerer de vigtigste faktorer bag bilpriser.

Ford dominerer det danske marked, og analysen viser en geografisk prisforskel på 17% mellem Køben­havn og det nordlige Danmark. Klassificeringsmodellen opnår 91% præcision på tværs af segmenter.

## Modeller og resultater

- **Lineær regression** til prispredikering (~60% forklaret varians)
- **KMeans clustering** til markeds­segmentering (k=3)
- **Random Forest Classifier** til kategorisering af køretøjer (91% accuracy)

De primære prisdrivere er: kilometerstand, alder, motorvolumen og mærke/model.

**Teknologier:** Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn

<a href="https://github.com/AsgerSH/SP2-BusinessIntelligence-Cars" target="_blank" rel="noreferrer">Se på GitHub</a>
