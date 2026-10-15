#!/usr/bin/env bash
# Zet de keuzepagina en de drie ontwerpen online bij Cloudflare (een Worker met alleen bestanden), zodat de klant ze kan bekijken en
# er via de reviewtool opmerkingen bij kan zetten. Alleen deze vier pagina's gaan mee, de rest van de repo niet.
# Eenmalig vooraf: npx wrangler login
set -euo pipefail
cd "$(dirname "$0")/.."
uit=.online
rm -rf "$uit"
mkdir -p "$uit/claude" "$uit/Codex"
cp index.html "$uit/"
cp -r claude/klassiek "$uit/claude/"
cp -r Codex/kust Codex/werkplaats "$uit/Codex/"
# Geen zoekmachines: dit zijn ontwerpen, nog geen echte site.
printf 'User-agent: *\nDisallow: /\n' > "$uit/robots.txt"
printf '/*\n  X-Robots-Tag: noindex\n' > "$uit/_headers"
npx --yes wrangler@4.149.0 deploy --assets "$uit" --name ato-advies --compatibility-date 2026-10-01
# Adres: https://ato-advies.reviewlayer.workers.dev
