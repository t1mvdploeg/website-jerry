#!/usr/bin/env python3
"""Maakt van de aangeleverde foto's de uitsneden voor de website.

Gebruik: python3 tools/fotos-exporteren.py
Leest fotos-aangeleverd/origineel/ en schrijft naar fotos-aangeleverd/web/. De uitvoer bevat geen
opnamegegevens (datum, toestel) meer. Huisnummers en naambordjes vallen buiten de uitsneden.
"""
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "fotos-aangeleverd" / "origineel"
VOL = ROOT / "fotos-aangeleverd" / "jpg-vol"
OUT = ROOT / "fotos-aangeleverd" / "web"
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)


def laad(stam):
    """Opent een origineel als RGB, rechtop. HEIC gaat eerst via sips naar jpg."""
    bron = next(SRC.glob(stam + "*"))
    if bron.suffix.lower() == ".heic":
        VOL.mkdir(parents=True, exist_ok=True)
        jpg = VOL / (bron.stem + ".jpg")
        if not jpg.exists():
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92", str(bron), "--out", str(jpg)],
                           check=True, capture_output=True)
        bron = jpg
    return ImageOps.exif_transpose(Image.open(bron)).convert("RGB")


def bewaar(im, naam, maat):
    im = im.resize(maat, Image.LANCZOS) if im.size != maat else im
    im.save(OUT / naam, "JPEG", quality=78, optimize=True, progressive=True)  # zonder exif


# Huisnummers die niet buiten de uitsnede te houden zijn: (x0, y0, x1, y1) als deel van de foto.
ONLEESBAAR = {"IMG_3411": (0.09, 0.18, 0.235, 0.245), "IMG_3389": (0.09, 0.288, 0.235, 0.35)}


def vierkant(stam, cx, cy, s=1.0):
    """Vierkante uitsnede rond (cx, cy), met zijde s keer de korte kant."""
    im = laad(stam)
    if stam in ONLEESBAAR:
        x0, y0, x1, y1 = ONLEESBAAR[stam]
        box = (int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height))
        im.paste(im.crop(box).filter(ImageFilter.GaussianBlur((box[2] - box[0]) / 5)), box)
    zijde = int(min(im.size) * s)
    x = min(max(int(cx * im.width - zijde / 2), 0), im.width - zijde)
    y = min(max(int(cy * im.height - zijde / 2), 0), im.height - zijde)
    return im.crop((x, y, x + zijde, y + zijde))


def strook(stam, x0, y0, breedte, verhouding):
    """Uitsnede vanaf (x0, y0) met de gegeven breedte (deel van de foto) en verhouding breed:hoog."""
    im = laad(stam)
    w = int(breedte * im.width)
    h = int(w / verhouding)
    x, y = int(x0 * im.width), int(y0 * im.height)
    assert x + w <= im.width and y + h <= im.height, (stam, im.size, x, y, w, h)
    return im.crop((x, y, x + w, y + h))


# ---------- Projecten: vierkante foto's per stap ----------
# (bestandsnaam, bron, midden-x, midden-y, zijde)
PROJECTEN = [
    ("schuur-voor", "b0ea30db", 0.47, 0.5, 1.0),
    ("schuur-tijdens", "IMG_2019", 0.5, 0.5, 1.0),
    ("schuur-na", "IMG_2044", 0.5, 0.515, 1.0),
    ("kozijnen-tijdens", "IMG_0405", 0.5, 0.5, 1.0),
    ("kozijnen-na", "IMG_0401", 0.5, 0.47, 1.0),
    ("topgevel-tijdens", "IMG_1838", 0.5, 0.40, 1.0),
    ("topgevel-na", "IMG_1841", 0.5, 0.42, 1.0),
    ("achterdeur-tijdens", "IMG_3389", 0.5, 0.5, 1.0),
    ("achterdeur-na", "IMG_3411", 0.5, 0.45, 1.0),
    ("zolder-voor", "IMG_2948", 0.5, 0.5, 1.0),
    ("zolder-tijdens", "IMG_2973", 0.5, 0.5, 1.0),
    ("zolder-na", "IMG_2988", 0.5, 0.5, 1.0),
    ("luifel-voor", "IMG_4088", 0.55, 0.38, 0.62),
    ("luifel-na", "IMG_4093", 0.45, 0.29, 0.60),
    ("kantoor-voor", "IMG_2526", 0.5, 0.5, 1.0),
    ("kantoor-tijdens", "IMG_2538", 0.5, 0.5, 1.0),
    ("kantoor-na", "IMG_2596", 0.45, 0.5, 1.0),
    ("dorpel-tijdens", "IMG_1932", 0.5, 0.5, 1.0),
    ("dorpel-na", "IMG_1936", 0.55, 0.5, 1.0),
]
for naam, stam, cx, cy, s in PROJECTEN:
    bewaar(vierkant(stam, cx, cy, s), f"{naam}.jpg", (800, 800))

# De stijl naast het raam: schermafbeeldingen, dus de zwarte rand en de knoppen vallen buiten de uitsnede.
for naam, stam, y in (("stijl-voor", "IMG_4112", 700), ("stijl-tijdens", "IMG_4113", 700), ("stijl-na", "IMG_4114", 794)):
    im = laad(stam)
    bewaar(im.crop((0, y, 1206, y + 1206)), f"{naam}.jpg", (800, 800))


# ---------- Kozijnhoek: drie schermafbeeldingen op elkaar gelegd ----------
def geel_kader(im):
    """Linker-, boven- en onderrand van het gele raamhout, als houvast om de foto's gelijk te leggen."""
    px = im.load()
    xs, ys = [], []
    for y in range(140, im.height, 3):
        for x in range(0, im.width, 3):
            r, g, b = px[x, y]
            if r > 190 and g > 160 and b < 110:
                xs.append(x)
                ys.append(y)
    xs.sort()
    ys.sort()
    return xs[len(xs) // 50], ys[len(ys) // 50], ys[-len(ys) // 50]


def onderrand(im):
    """Eerste rij van de zwarte balk onderaan de schermafbeelding."""
    grijs = im.convert("L")
    for y in range(im.height - 1, 0, -1):
        if max(grijs.crop((0, y, im.width, y + 1)).getdata()) > 40:
            return y - 6
    return im.height


hoek = {}
for stap, stam in (("voor", "IMG_4110"), ("tijdens", "IMG_4111"), ("na", "IMG_4116")):
    im = laad(stam)
    x0, y0, y1 = geel_kader(im)
    hoek[stap] = {"im": im, "x0": x0, "y0": y0, "h": y1 - y0, "onder": onderrand(im)}
ref = hoek["voor"]["h"]
# Gezamenlijk beeldveld in de maat van de voor-foto, met het gele kader linksboven als nulpunt.
links = max(-d["x0"] * ref / d["h"] for d in hoek.values())
rechts = min((d["im"].width - d["x0"]) * ref / d["h"] for d in hoek.values())
boven = max((140 - d["y0"]) * ref / d["h"] for d in hoek.values())
onder = min((d["onder"] - d["y0"]) * ref / d["h"] for d in hoek.values())
breed = rechts - links
print(f"kozijnhoek: gezamenlijk veld {breed:.0f} x {onder - boven:.0f}; kaderhoogtes", {k: d["h"] for k, d in hoek.items()})


def hoek_uitsnede(d, verhouding, y_midden):
    """Uitsnede over de volle gezamenlijke breedte; y_midden is de plek van de onderkant van het gele kader."""
    hoog = breed / verhouding
    y = min(max(ref - hoog * y_midden, boven), onder - hoog)
    s = d["h"] / ref
    box = tuple(int(v) for v in (d["x0"] + links * s, d["y0"] + y * s, d["x0"] + rechts * s, d["y0"] + (y + hoog) * s))
    return d["im"].crop(box)


for stap, d in hoek.items():
    bewaar(hoek_uitsnede(d, 4 / 3, 0.32), f"kozijnhoek-{stap}-breed.jpg", (1200, 900))

# ---------- Grote beelden ----------
bewaar(strook("IMG_0472", 0.14, 0.03, 0.86, 3 / 2), "rij-kozijnen.jpg", (1800, 1200))      # nieuwe kozijnen, donkere baksteen
bewaar(strook("IMG_1717", 0.0, 0.25, 1.0, 4 / 3), "herstel-hoek.jpg", (1600, 1200))        # nieuw hout in een hoek
bewaar(strook("IMG_2086", 0.0, 0.08, 1.0, 16 / 9), "rijwoning.jpg", (2000, 1125))          # woning met nieuwe kozijnen
bewaar(strook("IMG_3406", 0.0, 0.30, 1.0, 3 / 2), "slot-detail.jpg", (1500, 1000))         # veiligheidsslot van dichtbij
bewaar(strook("IMG_1838", 0.0, 0.0, 1.0, 3 / 4), "topgevel-werk.jpg", (1500, 2000))        # topgevel in uitvoering

totaal = sum(p.stat().st_size for p in OUT.glob("*.jpg"))
print(len(list(OUT.glob("*.jpg"))), "bestanden,", round(totaal / 1e6, 1), "MB")
