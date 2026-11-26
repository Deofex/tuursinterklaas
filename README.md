# Sinterklaasavond — persoonlijke pagina's

Een statische website met een persoonlijke boodschap en optionele Spotify-embed per gast. De site gebruikt gewone HTML, CSS en JavaScript; Python is alleen nodig voor de lokale preview.

## Gastgegevens aanpassen

Open `data/gasten.json`. Elk gastrecord heeft dezelfde velden: `id`, `name`, `spotifyUrl` en `theme`. Alleen de persoonlijke waarden en het thema of achtergrondpad verschillen. De portretfoto's en de volgorde op de hoofdpagina staan in `js/app.js`. Het gedeelde rijm staat apart in `data/rijmtekst.txt`:

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

Pas `data/rijmtekst.txt` aan om het rijm voor iedereen tegelijk te wijzigen. Regelafbrekingen worden op de pagina behouden. Iedere gast heeft een eigen kleurpalet in `theme`; vul het pad naar een afbeelding in `images/` in bij `backgroundImage` (gebruik `null` zolang er geen achtergrondafbeelding is). Alle Spotify-spelers gebruiken de donkere weergave; deel-links worden automatisch omgezet in een embed. Playlist-links zijn ook geschikt.

QR-links zien er zo uit:

- `https://jouw-site.example/?voor=tim`
- `https://jouw-site.example/?voor=jose`

De links werken pas publiek nadat de website is gehost. Maak voor elke gast een QR-code met de bijbehorende URL.
De hoofdpagina zonder `voor` toont automatisch een aanklikbaar overzicht van alle gasten uit `data/gasten.json`.

## Lokaal bekijken

Voer in deze projectmap uit:

```bash
python3 scripts/preview.py
```

Open daarna `http://localhost:8000/` voor het gastenoverzicht, of `http://localhost:8000/?voor=tim` voor een persoonlijke pagina. Stop de preview met `Ctrl+C`. Alleen `index.html` rechtstreeks openen werkt niet goed, omdat de browser het JSON-bestand dan kan blokkeren.

## Responsive ontwerp

De pagina past zich aan mobiel, laptop, portrait en landscape aan. De inhoud mag scrollen; de layout forceert geen vaste schermhoogte.

## Hosting en privacy

Voor GitHub Pages kies je bij **Settings → Pages → Build and deployment** de bron **Deploy from a branch**, met branch `main` en map `/(root)`. GitHub publiceert dan de bestanden automatisch na iedere push. Ook andere statische hosts kunnen de bestanden `index.html`, `css/`, `js/` en `data/` serveren. `scripts/` is alleen voor lokaal gebruik.

`data/gasten.json` wordt publiek meegestuurd met de website. Zet er geen wachtwoorden, geheime informatie of gegevens in die niet openbaar mogen zijn. Een QR-code is een link, geen toegangsbeveiliging.