# Handoff — website ATO Advies & Onderhoud

Website voor de vader van Melvin (timmerbedrijf, Voorne aan Zee). Laatst bijgewerkt: 5 november 2026.

## Nieuwe foto's verwerkt (5 november 2026)

De klant stuurde een tweede Drive-map ("Fotos website 2", 20 foto's; overzicht in `docs/foto-inventaris.md`, onderaan). Verwerkt in alle drie de ontwerpen via de twee fotoscripts: vier nieuwe klussen (paal bij de voordeur, nieuwe achterdeur, deur in een glazen pui, doorgeefluik). Daarbij acht bruikbare klussen uit de eerste levering die nog niet op de site stonden; nu 18 in totaal, de soorten werk door elkaar. Wat er niet op staat en waarom: `docs/foto-inventaris.md`, onderaan. In klassiek toont de schuif bij "Waarom" nu de paal voor en na (opmerking 17). Daarmee zijn 10, 11, 12 en 17 af; alleen 7 (het nieuwe e-mailadres) wacht nog. Niet gebruikt: de pui-foto's (interieur van de klant door het glas) en de detailfoto's van de groene deur. Gecontroleerd: `check-mockups.py`, `.qa/check.cjs` (filter op houtrot verwacht nu 3 klussen) en `.qa/focus-check.cjs` groen; klassiek met `Codex/.qa/check-klassiek.cjs` (server op poort 8765 nodig) op 1440, 768, 390 en 360 px (alle 41 projectfoto's laden, geen zijwaarts scrollen, schuif, stappen en filter) en in Chrome bekeken. Op een telefoon is het projectenoverzicht nu lang (18 kaarten onder elkaar). **Online sinds 5 november, alleen klassiek** (Tims keuze: "ik hoef alleen klassiek te hebben"). Het hoofdadres stuurt door naar `/claude/klassiek/` met `?review=CODE` erbij; kust en werkplaats geven online 404. Live nagekeken met `check-klassiek.cjs` tegen het live adres. Reviewtool bijgewerkt: op Tims verzoek alle verwerkte opmerkingen verwijderd (1–6 en 8–18, met hun twee antwoorden); alleen 7 (e-mailadres, doen we later) staat er nog. Kopie van alles vóór het verwijderen: `fotos-aangeleverd/reviewtool-backup-2026-11-05.json` (buiten git). Via de Worker met de klantcode nagekeken: 1 opmerking over.

## Opmerkingen van de klant (23 oktober 2026)

De klant heeft 18 opmerkingen bij **Klassiek** gezet; ze staan met de stand van elk punt in `docs/review-opmerkingen.md`. Verwerkt: contact via e-mail in plaats van WhatsApp (de offerte-hulp zet nu een e-mail klaar, de vraag "Wanneer?" is weg), de teksten, het blok "Voor en na" weg (de schuif staat nu in "Waarom") en drie klussen eruit (topgevel, achterdeur, dorpel; ook in kust en werkplaats, want ze komen uit één lijst). Wachtte op de klant: het nieuwe e-mailadres (nog steeds) en de nieuwe foto's (binnen op 5 november, zie hierboven).

Staat online sinds 23 oktober (gecontroleerd op de live site).

## Online met de reviewtool (15 oktober 2026)

- **Adres:** https://ato-advies.reviewlayer.workers.dev (Cloudflare, een Worker met alleen bestanden). Sinds 5 november staat alleen klassiek online (eerder de keuzepagina en de drie ontwerpen), de rest van de repo niet. Zoekmachines worden geweerd (`robots.txt` en `X-Robots-Tag`).
- **Opnieuw online zetten** na een wijziging: `bash tools/online-zetten.sh` (eenmalig vooraf `npx wrangler login`, in een gewone terminal).
- **Reviewen:** de vier pagina's hebben de scriptregel van de reviewtool. Het project heet "ATO Advies & Onderhoud" en hangt aan dit adres. De links (voor de klant en voor Tim, los of in de werkruimte) vraag je op in `~/work/personal/website-review-tool`: `set -a; . ./.env; set +a; npm run project -- list` (Git Bash).
- **Zonder code in de link** doet de scriptregel niets; ook lokaal via `file://` merk je er niets van.
- Cloudflare Pages lukte niet ("Asset too large"); daarom een Worker. Gezien in Chrome: de balk op de keuzepagina, geen balk in de drie kleine voorbeelden.

## Stand

Er liggen drie ontwerpen voor de homepage waaruit Melvins vader moet kiezen. Open `index.html` in de hoofdmap: een keuzepagina voor de klant met van elk ontwerp een levend voorbeeld en een knop naar het hele ontwerp.

| Ontwerp | Map | Gemaakt door |
| --- | --- | --- |
| Klassiek (blauw, opbouw van dehoutrotreparateur.nl) | `claude/klassiek/` | Claude |
| Werkplaats (oranje en zwart) | `Codex/werkplaats/` | Codex |
| Kust (frisgroen) | `Codex/kust/` | Codex |

Alle drie hebben: echte foto's van eigen werk, een voor/na-schuif (kozijnhoek met houtrot), een projectenoverzicht met zes klussen (wisselen tussen voor, tijdens en na; filter op soort werk) en een offerte-hulp die een WhatsApp-bericht klaarzet (bij klassiek sinds 23 oktober een e-mail).

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
cd Codex && node .qa/check-klassiek.cjs                    # klassiek in de browser (eerst de server op 8765)
```
Beide slaagden op 23 oktober na de laatste wijziging; klassiek is toen ook in Chrome op 1440 en 390 px bekeken. Alle vier de pagina's zijn op 10 oktober in Chrome als telefoon (360 en 390 px) bekeken: geen zijwaarts scrollen, grotere tikvlakken voor Voor/Tijdens/Na en de navigatie, invoervelden minstens 16 px. Foto's opnieuw maken: `python3 tools/fotos-exporteren.py`, daarna `python3 tools/projecten-bouwen.py`.

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
- **Teksten** zijn een eerste opzet en niet door de eigenaar nagekeken. Nieuw op 23 oktober en nog niet door de klant bevestigd: bij "Waarom" de punten "Herstellen waar het kan" en "Netjes opgeruimd na afloop", en bij "Snelle afspraak" de zin "Korte lijnen, u spreekt direct de vakman zelf."
- **Omvang:** de git-map is ruim 30 MB doordat de foto's in drie ontwerpen staan.

## Voor Tim

1. **Reviewtool:** alleen opmerking 7 staat er nog (5 november). Statussen bijwerken kan zonder beheersleutel vanaf de laptop met `npx wrangler d1 execute reviewlayer --remote` in `website-review-tool` (wrangler is daar ingelogd). In `.env` op de laptop staat bij `REVIEW_KEY` geen sleutel maar een link, dus `npm run project -- list` werkt hier niet.
2. Bij de klant opvragen: het nieuwe e-mailadres, of het Klassiek wordt, de plaats per klus, de originele houtrotfoto's, of de klanten weten dat hun huis op de site komt, en akkoord op de nieuwe teksten (zie Open punten).
3. De drie ontwerpen in Safari bekijken en melden wat niet werkt.
4. Beslissen: mag `claude/modern/` weg, en moeten `fotos-aangeleverd/` en `whatsapp.md` ook naar GitHub?

## Volgende stap

Tim koos klassiek; of de twee Codex-ontwerpen (`Codex/`), de keuzepagina (`index.html` in de hoofdmap) en `claude/modern/` uit de repo mogen, heeft hij nog niet gezegd (ze staan niet meer online). Komt het e-mailadres binnen: verwerken volgens `docs/review-opmerkingen.md` (7). Na de keuze van het ontwerp: de twee andere ontwerpen verwijderen, losse pagina's toevoegen (diensten, projecten, over ons, contact), het klikbare huis inbouwen als Tim dat wil, en het beheersysteem aansluiten.
