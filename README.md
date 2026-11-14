# Minigolf

Et minigolfspil til mobil og browser: 20 baner med 18 huller hver, set ovenfra, hvor man trækker bagud og slipper for at slå. v0.16. Plus en tilfældig bane med banekode.

**Spil:** åbn `index.html`, eller slå GitHub Pages til (Settings → Pages → Branch `main`, mappe `/root`). På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## Indhold
- Seks baner med 18 huller hver (108 huller): Klassikeren med forhindringer og fem lange baner med vinkler, stigninger, fald og runde toppe
- 1–4 spillere på samme telefon med hver sin boldfarve, der skiftes til at slå
- Træk-og-slip: sigtelinjen viser første afslag på banden, korte put slås automatisk blødere, og et træk kan fortrydes
- Lydeffekter, der kan slås fra
- Highscore pr. bane med de ti bedste runder på enheden
- Bander og klodser af planker med søm, højde og bløde skygger i sollys fra venstre
- Filt med struktur og slid ved tee og hul
- Bakker: ramper og høje med højdekurver og pile, der viser hvilken vej det går ned
- Bevægelige forhindringer: vindmølle, svingende bom og skydeport
- Rør, der sender bolden videre, og en bro over vandet
- Sand, der bremser bolden, og vand, der koster ét strafslag
- Rullende bold med glans, spor i græsset, sandsprøjt og vandplask
- Omgivelser med træer, buske, blomster, sten, hegn og et lille hus
- Kameraet zoomer ind, når bolden er tæt på hullet
- Højst 8 slag pr. hul og scorekort efter runden

## Styring
Sæt fingeren (eller musen) et vilkårligt sted, træk bagud og slip. Træk tilbage til ringen for at fortryde. P eller Esc pauser, F giver fuld skærm.

## Filer
- `index.html` – hele spillet i én fil
- `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` – app-ikon og fuldskærm på mobil
- `CHANGELOG.md` – release-log
- `ROADMAP.md` – idéer, der venter

## Udvikling
Kilden ligger i `src/game.html`. `python3 build.py` bygger `index.html` (GitHub-versionen), `versions/minigolf-vX.Y.html` og artifakt-versionen i `artifact/`. Versionsnummeret står ét sted: konstanten `VERSION` i kilden.

## Versioner
Hver udgave gemmes som `versions/minigolf-vX.Y.html`, og versionen står i titlen og på startskærmen.

## Lyde
Kun rigtige optagelser, lagt som base64 MP3 i `src/snd.js` og bygget ind i siden af `build.py`.
- Træ- og metalslag: Kenney, CC0
- Publikum: WebbFilmsUK, CC BY 4.0
- Køllen mod bolden og bolden i hul: kilde og licens skal bekræftes

## Fælles highscore
Uden opsætning ligger highscoren kun på den enhed, man spiller på. Sådan tænder du en fælles liste, gratis og uden egen server:
1. Gå til https://console.firebase.google.com og opret et projekt (Google Analytics kan slås fra)
2. Vælg Build, Realtime Database, Create database, og vælg en region i Europa
3. Under fanen Rules indsætter du indholdet af `firebase-rules.json` og trykker Publish
4. Kopiér databasens adresse øverst på fanen Data, fx `https://minigolf-xxxxx-default-rtdb.europe-west1.firebasedatabase.app`
5. Sæt adressen ind i `src/online.js`, kør `python3 build.py` og push

Reglerne gør, at alle kan læse listen og tilføje en score, men ingen kan ændre eller slette en eksisterende. Navnet må være 1–12 tegn, og totalen skal ligge mellem 18 og 144. Der er ingen login, så en snyder kan stadig sende en falsk score, der opfylder reglerne.
