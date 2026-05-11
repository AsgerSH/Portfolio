---
title: "Uge 4"
weight: 4
---

## Mandag – 27. april

Mandagens undervisning handlede om implementationen af vores LLM-drevne applikation. Vi gik i dybden med de konkrete valg man skal træffe: rubric-design, promptstruktur, backend-arkitektur og API-kald — og hvordan de hænger sammen i et sammenhængende system.

Derefter gik vi i gang med at bygge. Mit projekt er et AI-drevet rapportvurderingsværktøj, der bruger Claude API til at evaluere studenterrapporter mod en defineret rubric. Backend er deployet på Render, og frontenden kører på GitHub Pages.

<div style="margin: 1.5rem 0;">
  <iframe
    src="https://asgersh.github.io/AI-rapportvurderings-tool/"
    width="100%"
    height="520"
    style="border: 1px solid #e2e8f0; border-radius: 12px; display: block;"
    loading="lazy"
  ></iframe>
  <p style="margin-top: 0.5rem; font-size: 0.85rem; color: #94a3b8; text-align: center;">
    Interaktiv preview — eller åbn den på <a href="https://asgersh.github.io/AI-rapportvurderings-tool/" target="_blank">asgersh.github.io/AI-rapportvurderings-tool</a>
  </p>
</div>

## Fredag – 1. maj

Dagens tema var **Spec Driven Development** og de juridiske og etiske dimensioner af AI-drevet softwareudvikling.

Vi blev introduceret til systemudviklingsmetoder tilpasset en verden, hvor kodeagenter skriver størstedelen af koden. Kerneidéen er at bruge *specifikationer* som det styrende artefakt gennem hele processen — fra krav og design til implementering og review. I stedet for at hoppe direkte til kode handler det om at nedbryde features i klare opgaver, flows og acceptkriterier, som en kodeagent kan arbejde struktureret ud fra. Det skaber en meget mere forudsigelig og reviewbar udviklingsproces.

Vi læste også Peter Naur, en pioner inden for datalogi, der allerede i 1985 introducerede begrebet **"Programming as Theory Building"** — idéen om at det væsentligste ved programmering ikke er koden i sig selv, men den mentale model (teorien) som udviklerne bygger op om systemet. Det er interessant at sætte op mod AI-drevet udvikling: hvad sker der med den teori, når kodeagenter genererer store dele af koden? Hvem ejer egentlig forståelsen af systemet?

Den juridiske del dækkede GDPR, EU's AI-forordning, bias i modeller og spørgsmålet om ansvarlighed — hvem hæfter, når en AI-drevet løsning gør noget forkert?

Dagen sluttede med en snak om AI-dilemmaet og de første halvanden time af dokumentarfilmen **The AI Dilemma**. Det, der sidder mest fast, er tempoet — tingene bevæger sig så hurtigt, at lovgivning og etiske rammer konstant løber bagefter. Filmen berørte også et konkret og lidt ubehageligt punkt: at AI-modeller trænes på og kan tilgå stort set alt på internettet, inklusiv indhold der er ulovligt eller skadeligt. Det er ikke et abstrakt problem — det er en reel udfordring, som industrien ikke har et godt svar på endnu.
