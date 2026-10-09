---
name: "ATO — twee zelfstandige ontwerpwerelden"
description: "Werkplaats en Kust: twee afzonderlijke, lokaal te openen ontwerpvoorstellen."
colors:
  werkplaats-orange: "#f36c36"
  werkplaats-ink: "#211e1b"
  werkplaats-paper: "#f2f3f3"
  werkplaats-muted: "#60564f"
  werkplaats-line: "#cac4b9"
  werkplaats-button-hover: "#473830"
  kust-forest: "#184f3c"
  kust-forest-dark: "#103e2f"
  kust-mint: "#e4f0e8"
  kust-white: "#fcfdf9"
  kust-ink: "#203d32"
  kust-muted: "#4f695c"
  kust-line: "#c8d7cd"
typography:
  werkplaats-display:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(70px,7vw,96px)"
    fontWeight: 700
    lineHeight: 0.96
    letterSpacing: "-0.015em"
  werkplaats-headline:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(48px,5.6vw,80px)"
    fontWeight: 700
    lineHeight: 0.96
    letterSpacing: "-0.015em"
  werkplaats-body:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  werkplaats-button:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "15px"
    fontWeight: 600
  kust-display:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "clamp(56px,6.3vw,88px)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.04em"
  kust-headline:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "clamp(34px,3.4vw,48px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  kust-body:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
  kust-button:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "15px"
    fontWeight: 500
rounded:
  werkplaats-square: "0px"
  kust-button: "6px"
  kust-photo: "14px"
spacing:
  werkplaats-gutter: "clamp(24px,5vw,80px)"
  kust-gutter: "clamp(24px,5vw,72px)"
  section-desktop: "100px"
  werkplaats-section-mobile: "64px"
  kust-section-mobile: "65px"
components:
  werkplaats-button:
    backgroundColor: "{colors.werkplaats-ink}"
    textColor: "{colors.werkplaats-paper}"
    typography: "{typography.werkplaats-button}"
    rounded: "{rounded.werkplaats-square}"
    padding: "15px 21px"
  werkplaats-button-hover:
    backgroundColor: "{colors.werkplaats-button-hover}"
  werkplaats-nav:
    backgroundColor: "{colors.werkplaats-ink}"
    textColor: "{colors.werkplaats-paper}"
  werkplaats-service:
    textColor: "{colors.werkplaats-ink}"
    padding: "25px 4px"
  werkplaats-range:
    height: "32px"
  kust-button:
    backgroundColor: "{colors.kust-forest}"
    textColor: "{colors.kust-white}"
    typography: "{typography.kust-button}"
    rounded: "{rounded.kust-button}"
    padding: "14px 23px"
  kust-button-hover:
    backgroundColor: "{colors.kust-forest-dark}"
  kust-button-light:
    backgroundColor: "{colors.kust-mint}"
    textColor: "{colors.kust-forest}"
    typography: "{typography.kust-button}"
    rounded: "{rounded.kust-button}"
    padding: "14px 23px"
  kust-button-light-hover:
    backgroundColor: "{colors.kust-white}"
  kust-nav:
    textColor: "{colors.kust-ink}"
  kust-details:
    textColor: "{colors.kust-ink}"
    padding: "20px 0"
  kust-range:
    height: "32px"
  kust-intro-panel:
    backgroundColor: "{colors.kust-forest}"
    textColor: "{colors.kust-white}"
    rounded: "{rounded.kust-photo}"
    padding: "34px"
---

# Design System: ATO — twee zelfstandige ontwerpwerelden

## Overview

**Creative North Star: "Werkplaats / Kust — twee afzonderlijke werelden"**

Werkplaats is direct en ambachtelijk: signaaloranje, houtskool, smalle stevige kapitalen en een close-up van handen aan het werk. Rechte hoeken, open dienstenregels en uitgesproken lichte en donkere vlakken bepalen de identiteit. Het ontwerp wijkt visueel af van de bestaande klassieke blauwe en warme sierletter-mockups.

Kust is rustig en toegankelijk: bosgroen, zacht mint, luchtige DM Sans-koppen en woningfotografie. Afgeronde fotokaders, een groene intro naast de woningfoto en native diensten-uitklappers richten de aandacht op de vraag van de huiseigenaar. Beide voorstellen zijn bewust zelfstandige alternatieven; er is geen gekozen winnaar of gemengde ATO-huisstijl.

**Key Characteristics:**
- Werkplaats: stevige kapitalen, rechte hoeken, oranje opening en volledig zichtbare diensten.
- Kust: groene toonvlakken, ruime witruimte, zachte fotokaders en native uitklappers.
- Beide: lokale fonts en foto's, directe contactlinks, zichtbare focus en eerlijk gemarkeerd stockbeeld.

FORM-record: gegenereerde direction/persuade-seed `f6bca61c`, toegewezen index 7. De concrete opdracht vroeg twee zelfstandige lokale HTML-mockups. Daarom zijn twee werelden direct in code uitgewerkt vanuit bestaande productfeiten en de gegeven ontwerpvrijheid. Er was geen kaartselectie door de gebruiker, goedgekeurde beeldcompositie of gekozen QUALITY BAR-kaart; de seed is geen gebruikerskeuze. De afgeronde implementaties bepalen de onderstaande regels.

## Colors

De frontmatter is de normatieve bron voor de kleuren; de voorvoegsels houden beide paletten gescheiden.

### Primary
- **Werkplaats signaaloranje:** opening, contactsluiting, pictogramaccenten en vergelijkingsschuif.
- **Kust bosgroen:** koppen, primaire contactknoppen, introvlak en contactsluiting. De donkerdere variant is de hoverkleur van de primaire knop.

### Secondary
- **Kust zacht mint:** opening, werkgebied, stapnummers en de lichte contactknop.

### Neutral
- **Werkplaats houtskool / koel papier:** tegengestelde tekst- en achtergrondrollen in navigatie, diensten en vergelijking. Gedempte tekst en lijnkleur ondersteunen open lijsten.
- **Kust bijna-wit / groene inkt:** pagina en lopende tekst. Gedempt groen en een lichte groene lijnkleur ondersteunen toelichting en uitklappers.

**The Separate Worlds Rule.** Gebruik op een vervolgscherm één volledig palet; meng de oranje Werkplaats-identiteit niet met de zachte Kust-vormen.

## Typography

**Display Font:** Werkplaats gebruikt lokaal Barlow Condensed, met sans-serif als fallback. Kust gebruikt lokaal DM Sans.

**Body Font:** Beide gebruiken lokaal DM Sans, met sans-serif als fallback; het lokale variabele font dekt gewichten 400–700.

### Hierarchy
- **Werkplaats:** display en sectiekoppen gebruiken de frontmatterrollen, hoofdletters en gewicht 700. Dienstenkoppen zijn 36px; gewone titels 22–23px. Body is 17px/1.6, hero-intro 18px/1.55, toelichtingen 15px en metadata 12–14px. De contactkop heeft een eigen schaal tot 92px.
- **Kust:** display en sectiekoppen gebruiken de frontmatterrollen, gewicht 500 en normale zinsvorm. Gewone titels zijn 23px/1.25, diensten-uitklappers 26px, body 17px/1.65, toelichtingen 15–16px en metadata 12–14px. De introkaart gebruikt 35px/1.12; de contactkop schaalt tot 60px.
- **Leeslengte:** lopende tekst ligt meestal rond 33–45ch; diensttoelichtingen kunnen tot 53–54ch lopen.

**The Type Contrast Rule.** Werkplaats ontleent kracht aan compacte Barlow-kapitalen; Kust aan ruimere DM Sans-zinskoppen. Behoud dit verschil.

## Layout

### Werkplaats

Een schermbrede gridopening (1.08fr / 1fr) zet het typografische statement naast de werkfoto. De sticky houtskoolnavigatie en donkere vertrouwensregel kaderen de opening. Secties gebruiken de frontmatter-gutter en doorgaans 100px verticale ruimte. De diensten vormen open regels met titel, toelichting en pijl; vergelijking, werkgebied en contact gebruiken tweekoloms grids. De aanpak heeft drie kolommen.

Bij 1000px worden tussenruimtes en koppen compacter; secties krijgen 76px verticale ruimte. Bij 700px worden de hoofdgrids één kolom, de foto komt onder de tekst en de navigatie vormt een tweede rij. De diensten blijven volledig leesbaar; titels en tekst delen één kolom met de pijl ernaast. Secties hebben dan 24px zijruimte en 64px verticale ruimte. De stappen worden een verticale route. De hero schaalt tussen 72px en 96px, gewone sectiekoppen zijn 56px. Boven 1700px groeien de secties tot 120px verticale ruimte.

### Kust

Een gecentreerde inhoudsbreedte (maximaal 1280px) gebruikt de eigen frontmatter-gutter. De niet-sticky navigatie staat op bijna-wit. Een typografische bovenrij (1.45fr / 1fr) gaat vooraf aan een panoramische woningfoto en groene intro (1.9fr / 1fr). Diensten, vergelijking en werkgebied gebruiken ruime tweekoloms grids; de aanpak drie kolommen. Gewone secties hebben 100px verticale ruimte.

Bij 1100px worden gaten, navigatie en hero compacter. Bij 780px vormt de navigatie een tweede rij, komen hero, diensten, stappen en werkgebied onder elkaar en verdwijnt alleen de ondersteunende dienstenfoto. Alle zes uitklappers blijven bereikbaar. De vergelijking zet de uitleg vóór de foto. Secties krijgen doorgaans 65px verticale ruimte; de hero schaalt tussen 46px en 70px, sectiekoppen zijn 36px en de contactkop 46px.

## Elevation & Depth

Beide werelden gebruiken geen schaduwen. Diepte ontstaat door foto's, contrasterende toonvlakken, lijnscheidingen en bij Kust het afsnijden van foto's binnen zachte kaders. Werkplaats is vlak en recht; Kust is vlak met zachtere contouren. Geen zwevende kaartlaag toevoegen.

## Shapes

Werkplaats heeft rechte hoeken voor knoppen, foto's en vergelijkingslabels. De schuifgreep is een vierkant met een donkere rand. Kust gebruikt de frontmatterradii voor knoppen en foto's/introvlak; vergelijkingslabels hebben 4px hoeken. Stapnummers en de ronde schuifgreep hebben een cirkelvorm (50%). Beide gebruiken dunne lijnscheidingen en inline SVG-lijnpictogrammen.

## Components

### Buttons

Werkplaats gebruikt een rechte houtskoolknop met papierkleurige tekst, gewicht 600, minimaal 54px hoogte en de frontmatterpadding. Hover verandert de achtergrond naar het warmere donkere token; tekstlinks verschuiven hun pijl 4px. Op mobiel krijgt de knop 14px tekst en 14px 18px padding.

Kust gebruikt een bosgroene knop met bijna-witte tekst, gewicht 500, minimaal 52px hoogte en de frontmatterpadding/radius. Hover gebruikt het donkerdere groene token. De contactvariant gebruikt mint met bosgroene tekst; hover wordt bijna-wit. Contactlinks blijven gewone WhatsApp-, telefoon- en e-mailankers.

Focus gebruikt een lijn van 3px met 5px afstand. De Werkplaats-knop krijgt houtskool als focuskleur op oranje; de range krijgt oranje op de donkere vergelijkingssectie. Kust gebruikt bosgroen voor de primaire knop en range op lichte vlakken, en bijna-wit voor de lichte contactknop op bosgroen. Overige interactieve elementen gebruiken hun huidige tekstkleur. De knoppen hebben kleurtransities van 200ms.

### Cards / Containers

Werkplaats gebruikt open regels en volle sectievlakken. Kust heeft een groene intro met het fotokaderradius en 34px padding (26px bij 1100px, 28px bij 780px); dit is een begeleidend vlak naast de foto, geen dienstenkaartrooster. Beide vergelijkingsbeelden hebben een 4:3-verhouding en eerlijk zichtbare demolabels.

### Inputs / Fields

Er zijn geen tekstvelden. De native range bij iedere vergelijking heeft een gekoppeld label, een bereik van 0–100 en de eigen accentkleur. JavaScript verandert de clipping en aria-valuetext bij invoer. Zonder scripts blijven het beeld op 50%, de demo-uitleg en alle pagina-inhoud zichtbaar; de visuele vergelijking beweegt dan niet mee. Op mobiel komt de range onder het label op volle beschikbare breedte.

### Navigation

Werkplaats heeft sticky donkere navigatie, papierkleurige links en oranje hovertekst. Kust heeft niet-sticky lichte navigatie; links krijgen een onderstreping bij hover. Beide houden op mobiel alle drie ankerlinks in een tweede rij en een direct bereikbare belknop. Een skip-link verschijnt bij toetsenbordfocus.

### Signature Components

- **Werkplaats open dienstenlijst:** zes volledige ankerregels, elk met een gericht WhatsApp-conceptbericht. Hover verandert achtergrond en dienstenkop; de tekst blijft zichtbaar zonder scripts.
- **Kust native diensten-uitklappers:** zes details/summary-elementen, de eerste aanvankelijk open. Meerdere mogen tegelijk open zijn. De plus draait 45 graden bij openen; de conceptberichtlink staat in de uitklapinhoud. De werking is native en vereist geen JavaScript.
- **Vergelijkingsdemo:** dezelfde stockfoto verschijnt ongefilterd en digitaal gefilterd. Dit is geen bewijs van uitgevoerd ATO-werk. Werkplaats gebruikt een vierkante oranje greep; Kust een ronde lichte greep.
- **Fotobeweging:** alleen bij no-preference krijgt de openingsfoto een eenmalige settle-animatie (900ms, cubic-bezier(.16,1,.3,1)) en de pagina soepel scrollen. Reduced motion schakelt deze twee effecten uit; de korte hovertransities blijven aanwezig.

## Do's and Don'ts

### Do:
- **Do** houd Werkplaats en Kust als zelfstandige alternatieven met hun eigen palet, typografie en vormen.
- **Do** behoud de volledig zichtbare Werkplaats-diensten en de native Kust-uitklappers als afzonderlijke interactiepatronen.
- **Do** gebruik lokale fonts en foto's, zichtbare focus, gekoppelde range-labels en correcte contactlinks.
- **Do** vermeld stockbeeld en de gefilterde vergelijkingsdemo eerlijk; echte projectfoto's volgen later.

### Don't:
- **Don't** behandel één voorstel als winnaar of maak ongemerkt één gemengde huisstijl.
- **Don't** voeg schaduwkaarten toe aan de vlakke secties of vervang open dienstenregels door een kaartrooster.
- **Don't** presenteer de demovergelijking als een echt resultaat of voeg fictieve reviews, garanties of ervaringsjaren toe.
