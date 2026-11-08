#!/usr/bin/env python3
"""Zet het projectenoverzicht in klassiek, vanuit één lijst met klussen.

Gebruik: python3 tools/projecten-bouwen.py
Kopieert de foto's uit fotos-aangeleverd/web/ naar klassiek en schrijft de sectie tussen de
markeringen <!-- projecten:start --> en <!-- projecten:end -->. Opnieuw draaien vervangt de sectie.
De opmaak staat in de stylesheet, het gedrag in het script van de pagina.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "fotos-aangeleverd" / "web"

DIENSTEN = {
    "houtrot": "Houtrotherstel",
    "boeilijsten": "Boeilijsten",
    "ramen": "Ramen en deuren",
    "gevel": "Gevelbekleding",
    "sluitwerk": "Hang- en sluitwerk",
    "overig": "Overig timmerwerk",
}
STAPPEN = {"voor": "Voor", "tijdens": "Tijdens", "na": "Na"}

# (bestandsnaam, titel, dienst, {stap: beschrijving van de foto})
PROJECTEN = [
    ("achterdeur", "Nieuwe achterdeur", "ramen", {
        "voor": "Oude groene achterdeur met houtrot", "na": "Nieuwe witte achterdeur"}),
    ("entree", "Toegangsdeur gemaakt in kozijn", "ramen", {
        "voor": "Glazen pui zonder deur", "tijdens": "Opening in de pui voor de nieuwe deur", "na": "Pui met de nieuwe deur"}),
    ("luik", "Doorgeefluik in een kantoorwand", "overig", {
        "voor": "Dichte wand in een kantoor", "tijdens": "Opening uitgezaagd in de wand", "na": "Afgewerkt luik met vensterbank"}),
    ("wand", "Kantoorwand met deur", "overig", {
        "tijdens": "Frame van de nieuwe wand", "na": "Afgewerkte wand met deur"}),
    ("voordeur", "Nieuwe voordeur", "ramen", {
        "tijdens": "Nieuwe deur klaar om te plaatsen", "na": "Nieuwe witte voordeur in een rood kozijn"}),
    ("rijwoning", "Van uitzetramen naar stolpramen", "ramen", {
        "tijdens": "Steiger voor de gevel van een rijwoning", "na": "Rijwoning met nieuwe kozijnen"}),
    ("schuur", "Schuur met nieuwe boeilijsten", "boeilijsten", {
        "voor": "Schuur met verweerde dakrand", "tijdens": "Dakrand met nieuwe latten en folie", "na": "Schuur met nieuwe witte windveren"}),
    ("stijl", "Houtrot in kozijn", "houtrot", {
        "voor": "Verrotte stijl naast een raam", "tijdens": "Nieuw hout ingezet naast het raam", "na": "Stijl hersteld en geschilderd"}),
    ("kozijnen", "Nieuwe kozijnen", "ramen", {
        "tijdens": "Oud kozijn uit de gevel gehaald", "na": "Nieuw kozijn met roedeverdeling in donkere baksteen"}),
    ("pui", "Van openslaande deuren naar vast glas met borstwering", "ramen", {
        "voor": "Openslaande tuindeuren", "tijdens": "Opening met de nieuwe borstwering", "na": "Vast glas met een borstwering eronder"}),
    ("luifel", "Luifel boven de voordeur", "boeilijsten", {
        "voor": "Luifel met open onderkant", "na": "Luifel met nieuwe witte bekleding"}),
    ("zolder", "Installatie op zolder weggewerkt", "overig", {
        "voor": "Zolder met open installatie", "tijdens": "Houten wand rond de installatie", "na": "Afgewerkte wand met deuren"}),
    ("kantoor", "Scheidingswand in een kantoor", "overig", {
        "voor": "Open kantoorruimte", "tijdens": "Metalen frame van de wand", "na": "Afgewerkte wand met deur"}),
]
# Omschrijving onder de titel; zonder omschrijving staat daar de soort werk.
OMSCHRIJVING = {"schuur": "Gedeelte dakbeschot, boeilijsten en windveren vervangen"}
VOLGORDE = ["kozijnen", "pui", "achterdeur", "schuur", "stijl", "entree", "luik", "luifel",
            "voordeur", "zolder", "rijwoning", "kantoor", "wand"]
PROJECTEN.sort(key=lambda p: VOLGORDE.index(p[0]))

ONTWERPEN = {
    "klassiek": {
        "map": ROOT / "claude" / "klassiek", "fotos": "fotos/projecten", "i18n": True,
        "voor": '<section class="sec sec-alt" id="werkgebied">',
        "open": '<section class="sec" id="projecten">\n  <div class="wrap">\n    <div class="head">\n      <h2{t}>{titel}</h2>\n      <p class="sub"{l}>{lead}</p>\n    </div>',
        "sluit": "  </div>\n</section>",
        "titel": "Recent werk", "lead": "Kies per klus tussen voor, tijdens en na.",
    },
}

START, EIND = "<!-- projecten:start -->", "<!-- projecten:end -->"


def esc(t):
    return t.replace("&", "&amp;").replace('"', "&quot;")


def sectie(o):
    def k(sleutel):
        return f' data-i18n="{sleutel}"' if o["i18n"] else ""

    regels = [o["open"].format(titel=o["titel"], lead=o["lead"], t=k("projects.title"), l=k("projects.lead"))]
    gebruikt = [d for d in DIENSTEN if any(p[2] == d for p in PROJECTEN)]
    knoppen = [f'<button type="button" aria-pressed="true" data-dienst=""{k("projects.all")}>Alles</button>']
    knoppen += [f'<button type="button" aria-pressed="false" data-dienst="{d}"{k("projects.d." + d)}>{DIENSTEN[d]}</button>' for d in gebruikt]
    regels.append(f'<div class="werk-filter" data-werk-filter role="group" aria-label="Filter op soort werk" hidden>{"".join(knoppen)}</div>')
    regels.append('<ul class="werk-lijst">')
    for naam, titel, dienst, stappen in PROJECTEN:
        knoppen = "".join(
            f'<button type="button" aria-pressed="{"true" if s == "na" else "false"}" data-src="{o["fotos"]}/{naam}-{s}.jpg" data-alt="{esc(alt)}"{k("projects.step." + s)}>{STAPPEN[s]}</button>'
            for s, alt in stappen.items())
        regels.append(
            f'<li class="werk" data-dienst="{dienst}"><div class="werk-beeld">'
            f'<img src="{o["fotos"]}/{naam}-na.jpg" alt="{esc(stappen["na"])}" width="800" height="800" loading="lazy" data-werk-img>'
            f'<div class="werk-stappen" data-werk-stappen role="group" aria-label="Kies een foto van deze klus" hidden>{knoppen}</div></div>'
            f'<div class="werk-tekst"><h3{k("projects.p." + naam)}>{esc(titel)}</h3><p{k(("projects.o." + naam) if naam in OMSCHRIJVING else ("projects.d." + dienst))}>{esc(OMSCHRIJVING.get(naam, DIENSTEN[dienst]))}</p></div></li>')
    regels.append("</ul>")
    regels.append(o["sluit"])
    return START + "\n" + "\n".join(regels) + "\n" + EIND + "\n"


def main():
    # Teksten voor het beheersysteem: alleen het klassieke ontwerp leest ze via data-i18n.
    cp = ROOT / "content" / "nl.json"
    content = json.loads(cp.read_text(encoding="utf-8"))
    k = ONTWERPEN["klassiek"]
    content["projects"] = {
        "title": k["titel"], "lead": k["lead"], "all": "Alles", "step": STAPPEN, "d": DIENSTEN,
        "p": {naam: titel for naam, titel, _, _ in PROJECTEN}, "o": OMSCHRIJVING,
    }
    cp.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for naam, o in ONTWERPEN.items():
        doel = o["map"] / o["fotos"]
        if doel.exists():
            shutil.rmtree(doel)
        doel.mkdir(parents=True)
        for stam, _, _, stappen in PROJECTEN:
            for s in stappen:
                shutil.copy2(WEB / f"{stam}-{s}.jpg", doel / f"{stam}-{s}.jpg")
        pad = o["map"] / "index.html"
        html = pad.read_text(encoding="utf-8")
        if START in html:
            html = html[:html.index(START)] + sectie(o) + html[html.index(EIND) + len(EIND) + 1:]
        else:
            plek = html.index(o["voor"])
            plek = html.rfind("\n", 0, plek) + 1
            html = html[:plek] + sectie(o) + html[plek:]
        pad.write_text(html, encoding="utf-8")
        print(naam, "bijgewerkt:", len(PROJECTEN), "klussen,", sum(len(p[3]) for p in PROJECTEN), "foto's")


if __name__ == "__main__":
    main()
