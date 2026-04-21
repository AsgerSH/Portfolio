---
title: "Uge 3"
weight: 3
---

## Mandag – 20. april

Mandagens undervisning handlede om at integrere AI-assistenter direkte i sin arbejdsproces som udvikler — konkret ved at koble Claude eller Cursor ind i sin terminal eller IDE og lære at bruge dem effektivt som kodepartner.

For at lære det i praksis kom en rigtig kunde ind: ejeren af meditationswebsitet **Scenius**, som gerne ville have en quiz tilføjet til sit site. Vi fik projektet beskrevet i detaljer og fik at vide, hvad der skulle implementeres.

Slutresultatet er en React + Vite-app med fem quizmoduler om meditationens grundprincipper:

1. Om meditation — og at vælge ikke at have et problem
2. Om at være stille
3. Om at være afspændt *(ease of being)*
4. Om at være opmærksom og lysvågen
5. Om at lade alting være

Hvert modul indeholder seks spørgsmål med multiple choice-svar. Quizindholdet er skrevet i Markdown og parses dynamisk, og brugerens fremskridt gemmes i `localStorage` så man kan fortsætte, hvor man slap.

<div style="margin: 1.5rem 0;">
  <iframe
    src="https://asgersh.github.io/SceniusQuiz/"
    width="100%"
    height="480"
    style="border: 1px solid #e2e8f0; border-radius: 12px; display: block;"
    loading="lazy"
  ></iframe>
  <p style="margin-top: 0.5rem; font-size: 0.85rem; color: #94a3b8; text-align: center;">
    Interaktiv preview — eller åbn den på <a href="https://asgersh.github.io/SceniusQuiz/" target="_blank">asgersh.github.io/SceniusQuiz</a>
  </p>
</div>

## Fredag – 24. april

Indhold tilføjes fredag efter skoledagen. Vi lover det bliver mere spændende end denne sætning.
