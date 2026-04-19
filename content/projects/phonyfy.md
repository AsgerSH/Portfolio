---
title: "Phonyfy – Spotify-klon"
weight: 1
---

Phonyfy er et eksamensprojekt fra 3. semester, der kombinerer en Java-backend og et React-frontend til en fungerende musik-streaming applikation — inspireret af Spotify.

## Backend

Bygget i Java med Javalin som web-framework. Systemet håndterer autentificering via JWT med rollebaseret adgangskontrol (USER og ADMIN), og eksponerer et fuldt REST API til sange, kunstnere, albums og playlists.

Deployment er håndteret med Docker og Caddy som reverse proxy, og projektet har automatiseret CI/CD via GitHub Actions.

**Teknologier:** Java · Javalin · JPA · JWT · JUnit · RestAssured · Docker · Caddy · GitHub Actions

<a href="https://github.com/AsgerSH/AJ-phonyfy" target="_blank" rel="noreferrer">Se backend på GitHub</a>

## Frontend

React/Vite-frontend bygget som 3. semesters frontend-eksamen. Fokus på komponentbaseret arkitektur, modulær kodestruktur og moderne udviklingsworkflow med Hot Module Replacement.

**Teknologier:** React · Vite · JavaScript (ES6+) · ESLint

<a href="https://github.com/AsgerSH/Phonyfy-frontend-SP3" target="_blank" rel="noreferrer">Se frontend på GitHub</a>

**Udviklere:** Asger Storgaard Høffner · Jonas Outzen
