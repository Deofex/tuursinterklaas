# Sinterklaasavond — persoonlijke pagina's

Een statische website met een persoonlijke boodschap en optionele Spotify-embed per gast. De site gebruikt gewone HTML, CSS en JavaScript; Python is alleen nodig voor de lokale preview.

## Gastgegevens aanpassen

Open `data/gasten.json`. Elk gastrecord heeft dezelfde velden: `id`, `name`, `spotifyUrl` en `theme`. Alleen de persoonlijke waarden en het thema of achtergrondpad verschillen. Het gedeelde rijm staat apart in `data/rijmtekst.txt`:

```json
{
	"id": "tim",
	"name": "Tim",
	"spotifyUrl": "https://open.spotify.com/track/...",
	"theme": {
		"backgroundImage": "images/tim.jpg",
		"backgroundColor": "#49372c",
		"backgroundDeep": "#201a20",
		"glow": "rgb(237 185 116 / 35%)",
		"card": "rgb(255 246 229 / 86%)",
		"heading": "#633f2b",
		"text": "#35271f",
		"accent": "#a34a34",
		"border": "rgb(231 187 126 / 72%)"
	}
}
```

Pas `data/rijmtekst.txt` aan om het rijm voor iedereen tegelijk te wijzigen. Regelafbrekingen worden op de pagina behouden. Iedere gast heeft een eigen kleurpalet in `theme`; voeg een gegenereerde afbeelding toe aan `images/` en vul het pad in bij `backgroundImage` (gebruik `null` zolang er geen afbeelding is). Alleen Brigit heeft nu een achtergrondbestand. Alle Spotify-spelers gebruiken de donkere weergave; deel-links worden automatisch omgezet in een embed. Playlist-links zijn ook geschikt.

QR-links zien er zo uit:

- `https://jouw-site.example/?voor=tim`
- `https://jouw-site.example/?voor=jose`

De links werken pas publiek nadat de website is gehost. Maak voor elke gast een QR-code met de bijbehorende URL.

## Lokaal bekijken

Voer in deze projectmap uit:

```bash
python3 scripts/preview.py
```

Open daarna `http://localhost:8000/?voor=tim`. Stop de preview met `Ctrl+C`. Alleen `index.html` rechtstreeks openen werkt niet goed, omdat de browser het JSON-bestand dan kan blokkeren.

## Responsive ontwerp

De pagina past zich aan mobiel, laptop, portrait en landscape aan. De inhoud mag scrollen; de layout forceert geen vaste schermhoogte.

## Hosting en privacy

Upload `index.html`, `css/`, `js/` en `data/` naar een statische host, bijvoorbeeld S3, GitHub Pages of Cloudflare Pages. `scripts/` is alleen voor lokaal gebruik.

`data/gasten.json` wordt publiek meegestuurd met de website. Zet er geen wachtwoorden, geheime informatie of gegevens in die niet openbaar mogen zijn. Een QR-code is een link, geen toegangsbeveiliging.