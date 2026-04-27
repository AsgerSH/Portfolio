---
title: "AI Rapportvurderingsværktøj"
weight: 0
---

Et AI-drevet værktøj til automatisk vurdering af studenterrapporter baseret på en rubric. Systemet sender rapporten til en LLM og modtager struktureret feedback fordelt på faglige kriterier — som en digital sensor.

Projektet er bygget som del af AIDA-forløbet og er det første eksempel på en LLM-integreret backend-applikation i studiet. Fokus har ligget på promptstruktur, struktureret output og asynkron kommunikation med API'et.

## Funktioner

- Upload eller indsæt rapporttekst til vurdering
- LLM-baseret analyse med struktureret output pr. rubric-kategori
- Backend eksponerer et REST API som frontenden kalder
- Deployment af backend via Render, frontend via GitHub Pages

**Teknologier:** Python · FastAPI · Claude API · GitHub Pages · Render


<a href="https://github.com/AsgerSH/AI-rapportvurderings-tool" target="_blank" rel="noreferrer">Se på GitHub</a> · <a href="https://asgersh.github.io/AI-rapportvurderings-tool/" target="_blank" rel="noreferrer">Åbn deployed version</a>
