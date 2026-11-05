#!/usr/bin/env bash
# Zet het gekozen ontwerp (klassiek) online bij Cloudflare (een Worker met alleen bestanden), zodat de klant het kan bekijken en
# er via de reviewtool opmerkingen bij kan zetten. Alleen klassiek gaat mee, de rest van de repo niet. Het hoofdadres stuurt door
# naar klassiek, met ?review=CODE erbij: de links van de reviewtool wijzen naar het hoofdadres.
# Eenmalig vooraf: npx wrangler login
set -euo pipefail
cd "$(dirname "$0")/.."
uit=.online
rm -rf "$uit"
mkdir -p "$uit/claude"
cp -r claude/klassiek "$uit/claude/"
cat > "$uit/index.html" <<'HTML'
<!doctype html><meta charset="utf-8"><title>ATO Advies &amp; Onderhoud</title>
<script>location.replace("claude/klassiek/" + location.search + location.hash)</script>
<p><a href="claude/klassiek/">Naar de website</a></p>
HTML
# Geen zoekmachines: dit zijn ontwerpen, nog geen echte site.
printf 'User-agent: *\nDisallow: /\n' > "$uit/robots.txt"
printf '/*\n  X-Robots-Tag: noindex\n' > "$uit/_headers"
npx --yes wrangler@4.149.0 deploy --assets "$uit" --name ato-advies --compatibility-date 2026-10-01
# Adres: https://ato-advies.reviewlayer.workers.dev
