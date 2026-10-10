# Handoff — website ATO Advies & Onderhoud

Website voor de vader van Melvin (timmerbedrijf, Voorne aan Zee). Laatst bijgewerkt: 10 oktober 2026.

## Stand

Er liggen drie ontwerpen voor de homepage waaruit Melvins vader moet kiezen. Open `index.html` in de hoofdmap: een keuzepagina voor de klant met van elk ontwerp een levend voorbeeld en een knop naar het hele ontwerp.

| Ontwerp | Map | Gemaakt door |
| --- | --- | --- |
| Klassiek (blauw, opbouw van dehoutrotreparateur.nl) | `claude/klassiek/` | Claude |
| Werkplaats (oranje en zwart) | `Codex/werkplaats/` | Codex |
| Kust (frisgroen) | `Codex/kust/` | Codex |

Alle drie hebben: echte foto's van eigen werk, een voor/na-schuif (kozijnhoek met houtrot), een projectenoverzicht met negen klussen (wisselen tussen voor, tijdens en na; filter op soort werk) en een offerte-hulp die een WhatsApp-bericht klaarzet.

Verder in de repo:
- `claude/ideeen/`: schetspagina met vijf interactieve ideeën. Gekozen: klikbaar huis (nog niet ingebouwd), offerte-hulp (ingebouwd) en voor/na-galerij (ingebouwd als projectenoverzicht).
- `claude/modern/`: afgevallen ontwerp, staat er nog.
- `docs/foto-inventaris.md`: alle 83 aangeleverde foto's, gegroepeerd in 21 klussen.
- `Werkzaamheden.jpeg`: de flyer van het bedrijf met de zes diensten, het telefoonnummer en het e-mailadres.
- `fotos-aangeleverd/`: de originele foto's en uitsneden. Staat buiten git (356 MB, met adressen en personen). De bron is de Drive-map van Melvin.
- `whatsapp.md`: het gesprek met Melvin over de wensen. Staat ook buiten git.

Controleren:
```sh
python3 tools/check-mockups.py                              # klassiek: teksten, links, bestanden
cd Codex && TMPDIR="$PWD/.cache/tmp" node .qa/check.cjs     # kust en werkplaats in de browser
```
Beide slaagden op 10 oktober na de laatste wijziging. Alle vier de pagina's zijn op 10 oktober in Chrome als telefoon (360 en 390 px) bekeken: geen zijwaarts scrollen, grotere tikvlakken voor Voor/Tijdens/Na en de navigatie, invoervelden minstens 16 px. Foto's opnieuw maken: `python3 tools/fotos-exporteren.py`, daarna `python3 tools/projecten-bouwen.py`.

## Besluiten

- Gewone HTML en CSS, geen bouwstap. Elke ontwerpmap staat op zichzelf: geen verwijzingen naar bestanden daarbuiten (dat laadde niet in Safari).
- Lettertypes worden lokaal meegeleverd; er gaat niets naar Google.
- Alle tekst van klassiek staat in `content/nl.json` met `data-i18n`-sleutels in de HTML, als voorbereiding op een beheersysteem. De Codex-ontwerpen hebben hun eigen teksten.
- Foto's: opnamegegevens verwijderd, huisnummers buiten beeld of onleesbaar, geen herkenbare mensen of interieurs van klanten.
- Beloftes als garantietermijn, openingstijden en reviews staan er niet op zolang de eigenaar ze niet heeft bevestigd.
- Geen Motion-bibliotheek en geen 3D-effecten.
- Geen commits met Claude als medeauteur.
- De repo staat privé op GitHub: https://github.com/t1mvdploeg/website-jerry. Privé omdat er foto's van huizen van klanten in staan.

## Open punten

- **Safari:** alles is alleen in Chrome getest. Tim kijkt in Safari en heeft nog niet bevestigd dat de foto's en de knoppen daar werken.
- **Beheersysteem:** Decap CMS zoals in `web-oostenrijk` leunt op Git Gateway van Netlify, en dat is afgeschreven. Eerste kandidaat is Pages CMS, nog niet getest. De repo staat nu op GitHub, dus de proef kan.
- **Schuif is onscherp:** de houtrotfoto's (IMG_4110 t/m 4116) zijn schermafbeeldingen.
- **Plaatsnamen per klus ontbreken;** ze zitten niet in de foto's.
- **Klikbaar huis:** in welk ontwerp, en mag het de dienstenlijst vervangen?
- **Teksten** zijn een eerste opzet en niet door de eigenaar nagekeken.
- **Omvang:** de git-map is ruim 30 MB doordat de foto's in drie ontwerpen staan.

## Voor Tim

1. De drie ontwerpen in Safari bekijken en melden wat niet werkt.
2. Melvins vader laten kiezen tussen klassiek, werkplaats en kust.
3. Bij Melvin opvragen: de originele houtrotfoto's, de plaats per klus, wat er bij de woning met dakkapel is gedaan, en of de klanten weten dat hun huis op de site komt.
4. Beslissen: mag `claude/modern/` weg, en moeten `fotos-aangeleverd/` en `whatsapp.md` ook naar GitHub?

## Volgende stap

Na de keuze van het ontwerp: de twee andere ontwerpen verwijderen, losse pagina's toevoegen (diensten, projecten, over ons, contact), het klikbare huis inbouwen als Tim dat wil, en het beheersysteem aansluiten.
