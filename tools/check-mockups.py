#!/usr/bin/env python3
"""Controleert de mockups: teksten gelijk aan content/nl.json, links en bestanden kloppen.

Gebruik: python3 tools/check-mockups.py [klassiek] [modern]
"""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOCKUPS = ROOT / "claude"
REQUIRED = [
    'lang="nl"',
    'name="viewport"',
    'href="tel:+31621193640"',
    'href="https://wa.me/31621193640"',
    'href="mailto:atoadvies@live.nl"',
]
# Sleutels die in elke versie moeten staan; de rest van nl.json is optioneel per versie.
REQUIRED_KEYS = (
    ["meta.title", "brand.name", "hero.title", "hero.lead", "hero.call", "hero.whatsapp"]
    + [f"services.s{i}.{part}" for i in range(1, 7) for part in ("title", "text")]
    + ["beforeafter.before", "beforeafter.after", "beforeafter.note"]
    + ["why.p1", "why.p2", "why.p3", "area.place1", "area.place2", "area.place3"]
    + ["contact.title", "contact.call", "contact.whatsapp", "contact.mail", "footer.kvk"]
)


def flatten(node, prefix=""):
    for key, value in node.items():
        path = f"{prefix}{key}"
        if isinstance(value, dict):
            yield from flatten(value, path + ".")
        else:
            yield path, value


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []  # (sleutel, tekst)
        self.files = []  # lokale src/href
        self.key = None
        self.buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "data-i18n-content" in a:
            self.found.append((a["data-i18n-content"], a.get("content", "")))
        if "data-i18n" in a:
            self.key, self.buf = a["data-i18n"], []
        for name in ("src", "href"):
            ref = a.get(name, "")
            if ref and not ref.startswith(("http", "tel:", "mailto:", "#", "data:")):
                self.files.append(ref)

    def handle_data(self, data):
        if self.key:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if self.key:
            self.found.append((self.key, " ".join("".join(self.buf).split())))
            self.key = None


def check(version, content):
    errors = []
    path = MOCKUPS / version / "index.html"
    if not path.exists():
        return [f"{path} bestaat niet"]
    html = path.read_text(encoding="utf-8")
    page = Page()
    page.feed(html)
    errors += [f"ontbreekt: {needle}" for needle in REQUIRED if needle not in html]
    for key, text in page.found:
        if key not in content:
            errors.append(f"onbekende sleutel: {key}")
        elif text != content[key]:
            errors.append(f"tekst wijkt af bij {key}: {text!r}")
    used = {key for key, _ in page.found}
    errors += [f"sleutel niet gebruikt: {key}" for key in REQUIRED_KEYS if key not in used]
    for ref in page.files:
        if not (path.parent / ref.split("?")[0]).exists():
            errors.append(f"bestand bestaat niet: {ref}")
    return errors


def main():
    content = dict(flatten(json.loads((ROOT / "content" / "nl.json").read_text(encoding="utf-8"))))
    failed = False
    for version in sys.argv[1:] or ["klassiek", "modern"]:
        errors = check(version, content)
        failed = failed or bool(errors)
        print(f"{version}: {'OK' if not errors else f'{len(errors)} fout(en)'}")
        for error in errors:
            print(f"  - {error}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
