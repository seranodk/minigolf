# Minigolf

Et minigolfspil til mobil og browser: 9 huller set ovenfra, hvor man trækker bagud og slipper for at slå. v0.1.

**Spil:** åbn `index.html`, eller slå GitHub Pages til (Settings → Pages → Branch `main`, mappe `/root`). På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## Indhold
- 9 huller med stigende sværhedsgrad og par på hvert hul (banens par er 26)
- Træk-og-slip: længden giver kraft, retningen sigter, og en prikket linje viser retningen
- Bander, som bolden preller af på, skrå vægge og klodser
- Sand, der bremser bolden, og vand, der koster ét strafslag
- Højst 8 slag pr. hul, så ingen sidder fast
- Scorekort efter runden, og den bedste runde gemmes på enheden

## Styring
Sæt fingeren (eller musen) et vilkårligt sted, træk bagud og slip. P eller Esc pauser, F giver fuld skærm.

## Filer
- `index.html` – hele spillet i én fil
- `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` – app-ikon og fuldskærm på mobil
- `CHANGELOG.md` – release-log
- `ROADMAP.md` – idéer, der venter

## Udvikling
Kilden ligger i `src/game.html`. `python3 build.py` bygger `index.html` (GitHub-versionen), `versions/minigolf-vX.Y.html` og artifakt-versionen i `artifact/`. Versionsnummeret står ét sted: konstanten `VERSION` i kilden.

## Versioner
Hver udgave gemmes som `versions/minigolf-vX.Y.html`, og versionen står i titlen og på startskærmen.
