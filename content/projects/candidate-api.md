---
title: "Candidate Matcher API"
weight: 3
---

Et rekrutteringsplatform-API der matcher kandidater med jobrelevante tekniske kompetencer. Systemet beriger automatisk kompetencedata med markedspopularitet og løninformation fra en ekstern API-kilde, og genererer analytiske rapporter over topkandidater.

Projektet er bygget over otte user stories med fokus på ren arkitektur: adskilte lag for entiteter, DAOs, DTOs og controllers. Sikkerhed er implementeret med JWT, der skelner mellem offentlige endpoints og admin-operationer.

## Funktioner

- CRUD på kandidatprofiler med tilknyttede tekniske kompetencer
- Automatisk kompetenceberiging med popularitets- og løndata
- Filtrering på kompetencekategori (programmeringssprog, databaser, DevOps, frontend m.fl.)
- Analytiske rapporter: topkandidater rangeret efter gennemsnitlig kompetencepopularitet
- JWT-baseret autentificering med rollestyring
- Fuld REST-testdækning med RestAssured

**Teknologier:** Java · Javalin · JPA/Hibernate · JWT · RestAssured · PostgreSQL · Docker

<a href="https://github.com/AsgerSH/Exam-Candidate-Skill-API" target="_blank" rel="noreferrer">Se på GitHub</a>
