# Twee ATO-mockups

Open `index.html` in de browser om beide richtingen te vergelijken.

- **Werkplaats** (`werkplaats/index.html`): oranje, zwart, compacte typografie en een lijst van werkzaamheden. Elke werkzaamheid opent WhatsApp met een passend conceptbericht.
- **Kust** (`kust/index.html`): frisgroen, ruime typografie, woningfotografie en uitklapbare werkzaamheden.

Beide hebben in het contactblok een offerte-hulp: de bezoeker kiest klus, plaats en moment, en de WhatsApp-knop opent met een bericht waarin die keuzes al staan. Zonder JavaScript blijft de hulp verborgen en werkt de knop als gewone WhatsApp-link.

Beide zijn zelfstandige HTML/CSS-mockups. Elke map bevat eigen foto’s, lettertypes en een klein script voor de voor/na-schuif. Ze werken zonder installatie, bouwstap of internetverbinding. Bellen, WhatsApp en mail gebruiken de bijbehorende apps en verbinding.

De contactgegevens en de zes diensten komen uit `../whatsapp.md` en `../content/nl.json`. De foto’s zijn eigen werk van ATO, aangeleverd op 9 oktober 2026; zie `assets/BRONNEN.md`. De voor/na-schuif toont twee foto’s van hetzelfde kozijn. Daaronder staat een projectenoverzicht waarin de bezoeker per klus tussen voor, tijdens en na wisselt en op soort werk filtert. Die sectie en de foto’s komen uit `../tools/projecten-bouwen.py` en `../tools/fotos-exporteren.py`.

Foto’s en lokale fonts worden met de bestanden meegeleverd. Fontlicenties staan bij de assets. Er zijn geen reviews, garantietermijnen, openingstijden of ervaringsjaren toegevoegd.

## Controle

De browsercontrole staat in `.qa/check.cjs`; de benodigde Playwright-installatie bevindt zich uitsluitend in `.qa/`. Uitvoeren vanuit `Codex/`:

```sh
TMPDIR="$PWD/.cache/tmp" node .qa/check.cjs
TMPDIR="$PWD/.cache/tmp" node .qa/focus-check.cjs
```

Deze controle gebruikt de aanwezige Google Chrome-installatie. De pagina’s worden als lokale bestanden getest op 1440, 768, 390 en 360 pixels, met toetsenbordbediening van de schuif, uitklappers, contactlinks en lokaal geladen foto’s en fonts. Screenshots staan in `previews/` en de uitkomsten in `.qa/report.json` en `.qa/focus-report.json`. De tweede controle verifieert de focuscontrastwaarden van knoppen en schuiven.

De bestaande `klassiek/`- en `modern/`-mappen buiten `Codex/` blijven de oorspronkelijke ontwerpen. Alle nieuwe bestanden staan binnen `Codex/`.
