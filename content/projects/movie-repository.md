---
title: "Dansk Film Repository"
weight: 5
---

Et backend-system der henter og persisterer danske film fra de seneste fem år via TMDb API'en. Systemet giver mulighed for at søge og filtrere på film, skuespillere, instruktører og genrer — og identificerer automatisk de højest vurderede og mest populære titler.

Projektet er bygget i løbet af en struktureret fem-dages sprint og demonstrerer integration mod en ekstern API, JPA-baseret datapersistering og testning med containere.

## Funktioner

- Henter danske film fra TMDb og gemmer dem i en lokal database
- Fuldt CRUD-interface på filmdata
- Søgning på titel, genre, skuespiller og instruktør
- Identificerer top-vurderede og mest populære film
- Testet med JUnit og Testcontainers

**Teknologier:** Java · JPA · Lombok · Java Streams · JUnit · Testcontainers · Maven

<a href="https://github.com/AsgerSH/SP-1_Movie_Repository" target="_blank" rel="noreferrer">Se på GitHub</a>
