# Ontwerp: twee mockups voor ATO Advies & Onderhoud

Datum: 9 oktober 2026

## Doel

Melvins vader kiest uit twee versies van een homepage welke richting zijn website krijgt. Beide versies groeien daarna uit tot een volledige site; dat valt buiten dit ontwerp.

Een bezoeker moet in één oogopslag zien wat ATO doet en in welke regio, en daarna bellen of een WhatsApp-bericht sturen voor een vrijblijvende offerte.

## Vaste gegevens

- Naam: ATO Advies & Onderhoud, timmerwerken
- Telefoon: 06-21193640 (`tel:+31621193640`, WhatsApp `https://wa.me/31621193640`)
- E-mail: atoadvies@live.nl
- KvK: 24486625
- Werkgebied: Voorne aan Zee, Spijkenisse, Ouddorp
- Diensten:
  1. Ramen en deuren vervangen
  2. Gevelbekleding (Trespa of multiplex)
  3. Boeilijsten vervangen (diverse materialen)
  4. Houtrotherstel aan kozijnen
  5. Hang- en sluitwerk vervangen
  6. Overig timmerwerk
- Beloftes: gediplomeerd en verzekerd, snelle service, vrijblijvende offerte

Andere beloftes (garantietermijn, offerte binnen 24 uur, openingstijden, reviews) komen er niet op zolang Melvins vader ze niet heeft bevestigd.

## Onderdelen van beide versies

In deze volgorde, tenzij bij de versie anders staat:

1. Bovenbalk: bedrijfsnaam in letters en het telefoonnummer als knop.
2. Openingsbeeld: kop, één zin, knoppen "Bel" en "WhatsApp".
3. Diensten: de zes diensten, elk met een icoon en één regel uitleg.
4. Voor/na: één voorbeeld met een schuif over de foto.
5. Waarom ATO: de drie beloftes.
6. Werkgebied: de drie plaatsnamen in tekst, geen kaart.
7. Contact: bellen, WhatsApp, mail.
8. Onderbalk: naam, KvK-nummer, contactgegevens.

## Versie A: Klassiek (`claude/klassiek/`)

Gebaseerd op de opbouw van dehoutrotreparateur.nl, de site die Melvins vader mooi vindt.

- Lichte achtergrond, blauw als hoofdkleur in een eigen tint, donkergrijze tekst.
- Stevige schreefloze koppen, rustige broodtekst.
- Onder het openingsbeeld een rij van vier vertrouwensblokjes: gediplomeerd en verzekerd, snelle service, vrijblijvende offerte, lokaal in Voorne aan Zee.
- Geen animaties en geen JavaScript behalve de voor/na-schuif.
- Teksten zijn eigen teksten. Van de voorbeeldsite komt alleen de opbouw; het bedrijf werkt in dezelfde regio.

## Versie B: Modern (`claude/modern/`)

Richting gekozen door Tim uit drie voorbeelden: buildCo (build-co.framer.website), ForgeBuilt (forgebuilt.framer.website) en Formwork (formwork.framer.website). Wat die drie delen en wat versie B overneemt: warme, rustige kleuren, sierlijke koppen, grote foto's en veel ruimte. Het is de sfeer van een interieur- of architectenbureau, niet stoer of industrieel.

- Warm gebroken wit (rond #F7F5F0) en warm donkerbruin-antraciet (rond #2B2524) wisselen elkaar per sectie af. Eén houtkleur als accent, spaarzaam gebruikt.
- Koppen in een sierlijke schreefletter, broodtekst schreefloos.
- Grote foto's, ruime marges, weinig tekst per sectie.
- De voor/na-schuif staat in het openingsbeeld als blikvanger; onderdeel 4 vervalt daardoor als losse sectie.
- Diensten als tegels in een raster.
- Rustige animaties bij het laden en scrollen in gewone CSS, en soepel scrollen met Lenis via een script-tag. Wie in zijn systeem "minder beweging" heeft aangezet, krijgt geen animaties.
- Motion is bij het bouwen vervallen: het script verborg de inhoud en liet die door de bibliotheek terugkomen, en dat eindigde met elementen die tot nul gekrompen waren. In CSS kan de inhoud niet verborgen blijven hangen. In browsers zonder `animation-timeline` (nu nog Firefox) staat de inhoud stil in beeld.

## Techniek

- Per versie een eigen map met `index.html` en `style.css`. Geen bouwstap, geen npm.
- Elke versie heeft zijn eigen map `fotos/`, zodat de map op zichzelf werkt. Een gedeelde map buiten de versie laadde niet in Safari bij het openen als los bestand, en zou ook breken als elke versie apart online komt.
- Voor/na-schuif: twee foto's over elkaar, een `<input type="range">` bepaalt hoeveel van de bovenste zichtbaar is. Werkt met muis, vinger en toetsenbord. Geen library.
- Iconen: Phosphor Icons, als SVG in de pagina gezet.
- Lettertypes via Google Fonts. Niet Inter.
- Beide pagina's werken op telefoonbreedte (360 px) en op een computerscherm.

## Voorbereid op zelf teksten aanpassen

Beide volledige sites krijgen later hetzelfde beheersysteem als `web-oostenrijk`: Decap CMS op `/admin/`, met alle teksten in `content/nl.json`. Melvins vader past daar zelf tekst aan en kan foto's uploaden. De opzet uit `web-oostenrijk` (`admin/`, `tools/build-admin-config.py`, de lader in `index.html`) wordt hergebruikt; vertalen vervalt, want er is één taal.

Open punt (9 oktober 2026): Decap CMS slaat wijzigingen in `web-oostenrijk` op via Git Gateway van Netlify. Netlify noemt Git Gateway in zijn eigen documentatie deprecated: bestaande sites blijven werken, nieuwe configuraties worden afgeraden en fouten worden niet meer hersteld. Voor ATO zou het een nieuwe configuratie zijn. Welk beheersysteem het wordt, is daarom nog niet besloten; Pages CMS (uitnodigen per e-mail, geen GitHub-account nodig) is de eerste kandidaat en moet eerst met een proef worden getest. `content/nl.json` en de `data-i18n`-sleutels blijven in elk geval bruikbaar.

In de mockups staat de tekst nog gewoon in de HTML. Elk stuk tekst dat later aanpasbaar moet zijn krijgt wel al een `data-i18n`-sleutel met dezelfde naamgeving als in `web-oostenrijk`, zodat aansluiten geen verbouwing wordt.

## Tijdelijk beeld

- Rechtenvrije stockfoto's (Unsplash of Pexels) in `fotos/tijdelijk/` binnen elke versie, met een `BRONNEN.md` waarin per foto de herkomst staat.
- De AI-foto's van de flyer worden niet gebruikt.
- Geen beeldmerk; de naam staat in letters.

## Keuzes na de mockups (9 oktober 2026)

- `claude/modern` valt af.
- Van de vijf interactieve proefjes in `claude/ideeen/` wil Tim het klikbare huis (idee 1) en de offerte-hulp via WhatsApp (idee 2).
- De voor/na-galerij (idee 3) alleen als Melvins vader echte voor- en na-foto's van hetzelfde werk heeft. Zonder zulke paren wordt het een gewone projectgalerij.
- Postcodecheck (idee 4) en gevelkleur kiezen (idee 5) zijn niet gekozen.

## Buiten dit ontwerp

- Losse pagina's (diensten, projecten, over ons, contact).
- Het beheersysteem zelf (Decap CMS, GitHub-repo, Netlify-login).
- Contactformulier.
- Domeinnaam, hosting en livegang.
- Echte foto's, logo, reviews, juridische pagina's.

## Controle

Beide pagina's in de browser bekijken op 360 px en 1440 px breed: alle onderdelen zichtbaar, niets loopt buiten beeld, de schuif werkt, de bel-, WhatsApp- en mailknoppen hebben de juiste link.
