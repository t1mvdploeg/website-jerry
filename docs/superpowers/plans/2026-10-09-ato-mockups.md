# Twee mockups ATO Advies & Onderhoud: implementatieplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Twee homepages voor ATO Advies & Onderhoud, een klassieke en een moderne, die Melvins vader naast elkaar kan vergelijken.

**Architecture:** Twee losse mappen met elk een `index.html` en `style.css`, zonder bouwstap. Alle tekst komt uit één bron, `content/nl.json`; in de HTML staat dezelfde tekst uitgeschreven met een `data-i18n`-sleutel erbij, zodat later Decap CMS erop aangesloten kan worden. Taak 1 en 2 raken elkaars bestanden niet en lopen tegelijk.

**Tech Stack:** HTML, CSS, een paar regels JavaScript. Alleen in `modern/`: Motion en Lenis via een script-tag. Phosphor Icons als SVG in de pagina. Google Fonts.

**Spec:** `docs/superpowers/specs/2026-10-09-ato-mockups-design.md`

## Global Constraints

- Tekst: letterlijk uit `content/nl.json`. Elk tekstelement krijgt `data-i18n="<sleutel>"` en bevat alleen platte tekst, geen tags erin. Meta-omschrijving: `data-i18n-content="meta.desc"`. Geen tekst verzinnen die niet in het bestand staat; ontbreekt er iets, voeg het toe aan `content/nl.json` en meld het.
- Links: `tel:+31621193640`, `https://wa.me/31621193640`, `mailto:atoadvies@live.nl`.
- Sectie-id's: `diensten`, `voor-na`, `waarom`, `werkgebied`, `contact`.
- Foto's: alleen uit `../fotos/tijdelijk/` (`hero.jpg`, `voorna.jpg`, `gevel.jpg`, `deur.jpg`, `timmerman.jpg`, `hout.jpg`). `Werkzaamheden.jpeg` wordt niet gebruikt. Elke `<img>` heeft `alt`, `width` en `height`; alles onder het openingsbeeld `loading="lazy"`.
- `<html lang="nl">`, viewport-meta, één `<h1>`, koppen in volgorde.
- De pagina werkt als je `index.html` dubbelklikt (`file://`): alleen relatieve paden, geen `fetch`.
- Werkt op 360 px en 1440 px breed zonder horizontaal scrollen.
- Tekstcontrast minimaal 4,5:1; knoppen en links hebben een zichtbare focusrand.
- Niet Inter als lettertype. Geen emoji als icoon.
- Niet committen; dat gebeurt in taak 3.

## Review Focus

1. Smalle telefoon (360 px): lange woorden als "Gevelbekleding" en "Houtrotherstel" mogen niet buiten hun tegel lopen. Controle: schermafbeelding op 360 px in taak 1 en 2.
2. JavaScript uit of CDN onbereikbaar (alleen `modern/`): alle tekst en foto's blijven zichtbaar. Controle: taak 2 stap 4.
3. "Minder beweging" aan in het systeem: geen animaties, geen Lenis. Controle: taak 2 stap 4.
4. Toetsenbord: de voor/na-schuif reageert op pijltjestoetsen en toont focus. Controle: taak 1 en 2, stap met de schuif.
5. Aanraken op telefoon: over de schuif heen omlaag scrollen blijft mogelijk (`touch-action: pan-y`).
6. Openen via `file://` vanuit de submap: foto's laden via `../fotos/`. Controle: `tools/check-mockups.py` meldt elk pad dat niet bestaat.

---

## Gedeeld: de voor/na-schuif

Beide versies gebruiken deze opbouw. De vormgeving eromheen (hoeken, labels, greep) is per versie vrij.

```html
<figure class="ba" style="--pos:50%">
  <img class="ba-after" src="../fotos/tijdelijk/voorna.jpg" alt="Kozijn na het werk" width="1800" height="1200">
  <img class="ba-before" src="../fotos/tijdelijk/voorna.jpg" alt="" aria-hidden="true" width="1800" height="1200">
  <span class="ba-label ba-label-before" data-i18n="beforeafter.before">Voor</span>
  <span class="ba-label ba-label-after" data-i18n="beforeafter.after">Na</span>
  <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Schuif tussen voor en na">
</figure>
```

```css
.ba { position: relative; overflow: hidden; }
.ba img { display: block; width: 100%; height: 100%; object-fit: cover; }
.ba-before {
  position: absolute; inset: 0;
  clip-path: inset(0 calc(100% - var(--pos)) 0 0);
  /* ponytail: zelfde foto met filter als plaatshouder; filter weg zodra er een echte voor-foto is */
  filter: grayscale(.6) sepia(.35) contrast(.85) brightness(.9);
}
.ba::after { content: ""; position: absolute; top: 0; bottom: 0; left: var(--pos); width: 2px; background: #fff; pointer-events: none; }
.ba-range { position: absolute; inset: 0; width: 100%; height: 100%; margin: 0; opacity: 0; cursor: ew-resize; touch-action: pan-y; }
.ba:has(.ba-range:focus-visible) { outline: 3px solid currentColor; outline-offset: 3px; }
```

```html
<script>
  document.querySelectorAll(".ba-range").forEach((range) =>
    range.addEventListener("input", () => range.parentElement.style.setProperty("--pos", range.value + "%")));
</script>
```

Gebruik de echte `width` en `height` van `voorna.jpg` (`sips -g pixelWidth -g pixelHeight`).

## Gedeeld: bekijken zonder browserextensie

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT="/Users/timvanderploeg/Desktop/Projecten/Prive/Main/website-jerry"
OUT="<jouw scratchpad>"
"$CHROME" --headless=new --user-data-dir="$OUT/profiel" --hide-scrollbars --virtual-time-budget=6000 \
  --window-size=1440,900 --screenshot="$OUT/klassiek-1440-top.png" "file://$ROOT/klassiek/index.html"
```

- Per sectie een schermafbeelding door het anker achter de URL te zetten (`...index.html#diensten`). Geen venster van duizenden pixels hoog: dan klopt `100vh` niet.
- Telefoonbreedte: Chrome gaat niet smaller dan ongeveer 500 px. Maak in je scratchpad een hulppagina met `<iframe src="file://.../index.html#diensten" style="width:360px;height:780px;border:0">` en maak daar een schermafbeelding van.
- Verklein een afbeelding met `sips -Z 1200` voordat je hem met Read bekijkt.

---

### Task 1: Versie A, klassiek

**Files:**
- Create: `klassiek/index.html`, `klassiek/style.css`

**Interfaces:**
- Consumes: `content/nl.json`, `fotos/tijdelijk/*.jpg`, `tools/check-mockups.py`, de schuif hierboven.
- Produces: een pagina die `python3 tools/check-mockups.py klassiek` doorstaat.

Richting: de opbouw van dehoutrotreparateur.nl, rustig en vertrouwd. Lichte achtergrond, blauw `#1D5A8A` als hoofdkleur (eigen tint, niet het `#2b7bb9` van het voorbeeld), tekst `#2B2F33`, lichte vlakken `#F3F6F9`. Koppen Montserrat 700, broodtekst Lato. Geen animaties; het enige script is dat van de schuif.

Volgorde van de pagina:
1. Bovenbalk: `brand.name` met `brand.tagline`, links naar de secties (`nav.*`), telefoonknop (`brand.phone`). Op telefoon: naam en telefoonknop, navigatielinks mogen weg.
2. Openingsbeeld met `hero.jpg`: `hero.kicker`, `hero.title` (de `h1`), `hero.lead`, knoppen `hero.call` en `hero.whatsapp`.
3. Rij met vier vertrouwensblokjes (`trust.t1` tot `trust.t4`), elk met een Phosphor-icoon.
4. `#diensten`: `services.title`, `services.lead`, zes kaarten (`services.s1` tot `s6`) met icoon, drie naast elkaar op breed scherm, één op telefoon.
5. `#waarom`: `why.title`, `why.text` en de drie punten (`why.p1` tot `p3`) met vinkjes, naast een foto (`timmerman.jpg`).
6. `#voor-na`: `beforeafter.title`, `beforeafter.lead`, de schuif, eronder `beforeafter.note`.
7. `#werkgebied`: `area.title`, `area.text`, de drie plaatsen (`area.place1` tot `3`) als lijst, `area.sub`.
8. `#contact`: `contact.title`, `contact.text`, drie knoppen (`contact.call`, `contact.whatsapp`, `contact.mail`).
9. Onderbalk: `brand.name`, `brand.tagline`, `footer.kvk`, `footer.area`, telefoon en mail.

- [ ] **Step 1: Controle draaien, die moet falen**

Run: `python3 tools/check-mockups.py klassiek`
Expected: `klassiek: 1 fout(en)` met "bestaat niet".

- [ ] **Step 2: Iconen ophalen**

Phosphor-SVG's staan op `https://unpkg.com/@phosphor-icons/core@2.1.1/assets/regular/<naam>.svg`. Haal ze met curl op en plak de SVG in de HTML met `aria-hidden="true"` en `fill="currentColor"`. Namen die passen: `door`, `wall`, `ruler`, `wrench`, `key`, `hammer`, `seal-check`, `lightning`, `file-text`, `map-pin`, `phone`, `whatsapp-logo`, `envelope-simple`, `check`. Bestaat een naam niet, kies een andere uit dezelfde set.

- [ ] **Step 3: `klassiek/index.html` en `klassiek/style.css` schrijven** volgens de volgorde hierboven en de Global Constraints.

- [ ] **Step 4: Controle draaien, die moet slagen**

Run: `python3 tools/check-mockups.py klassiek`
Expected: `klassiek: OK`

- [ ] **Step 5: Bekijken op 1440 px en 360 px**, per sectie. Herstel wat buiten beeld loopt, overlapt of slecht leesbaar is. Controleer dat de greep van de schuif op 50% staat en dat de labels "Voor" en "Na" leesbaar zijn.

- [ ] **Step 6: Terugmelden** welke lettertypes en iconen zijn gebruikt, wat is gecontroleerd en wat niet lukte.

### Task 2: Versie B, modern

**Files:**
- Create: `modern/index.html`, `modern/style.css`

**Interfaces:**
- Consumes: `content/nl.json`, `fotos/tijdelijk/*.jpg`, `tools/check-mockups.py`, de schuif hierboven.
- Produces: een pagina die `python3 tools/check-mockups.py modern` doorstaat.

Richting: de sfeer van een interieur- of architectenbureau, zoals formwork.framer.website en build-co.framer.website. Warm gebroken wit `#F7F5F0` en warm donkerbruin `#2B2524` wisselen per sectie af; één houtkleur rond `#B07A45` als accent, spaarzaam. Let op: die houtkleur haalt op gebroken wit geen 4,5:1, gebruik hem daar dus alleen voor lijnen, vlakken en grote cijfers, niet voor gewone tekst. Koppen in een sierlijke schreefletter van Google Fonts, broodtekst Manrope. Grote foto's, ruime marges, weinig tekst per sectie. Gebruik de skill `frontend-design:frontend-design` voor de vormgeving.

Volgorde van de pagina:
1. Bovenbalk: `brand.name`, links (`nav.services`, `nav.area`, `nav.contact`), telefoonknop (`brand.phone`).
2. Openingsbeeld: links `hero.kicker`, `hero.title` (de `h1`), `hero.lead` en de knoppen `hero.call` en `hero.whatsapp`; rechts de voor/na-schuif als blikvanger met `beforeafter.note` eronder. Op telefoon onder elkaar, tekst eerst. Dit blok krijgt ook `id="voor-na"`.
3. `#waarom`: `why.title`, `why.text` en de drie punten (`why.p1` tot `p3`), met `hout.jpg` of `timmerman.jpg` groot ernaast.
4. `#diensten`: `services.title`, `services.lead`, zes tegels (`services.s1` tot `s6`) in een raster; `gevel.jpg` en `deur.jpg` mogen als grote beelden in of bij het raster.
5. `#werkgebied`: `area.title`, `area.text`, de drie plaatsen groot gezet (`area.place1` tot `3`), `area.sub`.
6. `#contact`: `contact.title`, `contact.text`, knoppen (`contact.call`, `contact.whatsapp`, `contact.mail`), op de donkere kleur.
7. Onderbalk: `brand.name`, `brand.tagline`, `footer.kvk`, `footer.area`.

Beweging:
- Motion en Lenis via jsDelivr of unpkg met een vast versienummer in de URL. Controleer met `curl -sI` dat elke URL 200 geeft voordat je hem gebruikt.
- Elementen zijn standaard zichtbaar. Het script verbergt ze pas vlak voordat het ze laat inkomen, zodat de pagina compleet is als het script niet laadt.
- Alles achter `if (!matchMedia("(prefers-reduced-motion: reduce)").matches)`.
- Rustig: korte fade met een paar pixels verschuiving bij het in beeld komen. Geen parallax, geen tekst die letter voor letter verschijnt.

- [ ] **Step 1: Controle draaien, die moet falen**

Run: `python3 tools/check-mockups.py modern`
Expected: `modern: 1 fout(en)` met "bestaat niet".

- [ ] **Step 2: Iconen ophalen** zoals in taak 1 stap 2 (zelfde bron en namen: `https://unpkg.com/@phosphor-icons/core@2.1.1/assets/regular/<naam>.svg`, als SVG in de HTML met `aria-hidden="true"` en `fill="currentColor"`). In deze versie mogen de tegels ook een cijfer (01 tot 06) in plaats van een icoon krijgen; de knoppen houden een icoon.

- [ ] **Step 3: `modern/index.html` en `modern/style.css` schrijven** volgens de volgorde hierboven en de Global Constraints.

- [ ] **Step 4: Controles draaien**

Run: `python3 tools/check-mockups.py modern`
Expected: `modern: OK`

Maak daarna een schermafbeelding met `--blink-settings=scriptEnabled=false` erbij: alle tekst en foto's moeten zichtbaar zijn. Maak er ook een met `--force-prefers-reduced-motion`: de pagina moet er hetzelfde uitzien als de eindtoestand, zonder half ingekomen elementen.

- [ ] **Step 5: Bekijken op 1440 px en 360 px**, per sectie. Herstel wat buiten beeld loopt, overlapt of slecht leesbaar is. Controleer dat de greep van de schuif op 50% staat en dat de labels "Voor" en "Na" leesbaar zijn.

- [ ] **Step 6: Terugmelden** welke lettertypes, iconen en bibliotheekversies zijn gebruikt, wat is gecontroleerd en wat niet lukte.

### Task 3: Eindcontrole en vastleggen (hoofdsessie)

- [ ] `python3 tools/check-mockups.py` geeft voor beide versies OK.
- [ ] Beide pagina's bekeken op 1440 px en 360 px.
- [ ] Eén commit met `klassiek/`, `modern/`, `fotos/`, `content/`, `tools/` en dit plan.
