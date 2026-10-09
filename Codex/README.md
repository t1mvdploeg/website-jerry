# Twee ATO-mockups

Open `index.html` in de browser om beide richtingen te vergelijken.

- **Werkplaats** (`werkplaats/index.html`): oranje, zwart, compacte typografie en een lijst van werkzaamheden. Elke werkzaamheid opent WhatsApp met een passend conceptbericht.
- **Kust** (`kust/index.html`): frisgroen, ruime typografie, woningfotografie en uitklapbare werkzaamheden.

Beide zijn zelfstandige HTML/CSS-mockups. Elke map bevat eigen foto’s, lettertypes en een klein script voor de voor/na-schuif. Ze werken zonder installatie, bouwstap of internetverbinding. Bellen, WhatsApp en mail gebruiken de bijbehorende apps en verbinding.

De contactgegevens en de zes diensten komen uit `../whatsapp.md` en `../content/nl.json`. Stockfoto’s zijn op de pagina’s gemarkeerd en hebben bronvermeldingen in `assets/BRONNEN.md`. De voor/na-schuif gebruikt dezelfde stockfoto met een filter en is een technische demonstratie. Echte projectfoto’s moeten nog worden aangeleverd.

Foto’s en lokale fonts worden met de bestanden meegeleverd. Fontlicenties staan bij de assets. Er zijn geen reviews, garantietermijnen, openingstijden of ervaringsjaren toegevoegd.

## Controle

De browsercontrole staat in `.qa/check.cjs`; de benodigde Playwright-installatie bevindt zich uitsluitend in `.qa/`. Uitvoeren vanuit `Codex/`:

```sh
TMPDIR="$PWD/.cache/tmp" node .qa/check.cjs
TMPDIR="$PWD/.cache/tmp" node .qa/focus-check.cjs
```

Deze controle gebruikt de aanwezige Google Chrome-installatie. De pagina’s worden als lokale bestanden getest op 1440, 768, 390 en 360 pixels, met toetsenbordbediening van de schuif, uitklappers, contactlinks en lokaal geladen foto’s en fonts. Screenshots staan in `previews/` en de uitkomsten in `.qa/report.json` en `.qa/focus-report.json`. De tweede controle verifieert de focuscontrastwaarden van knoppen en schuiven.

De bestaande `klassiek/`- en `modern/`-mappen buiten `Codex/` blijven de oorspronkelijke ontwerpen. Alle nieuwe bestanden staan binnen `Codex/`.
