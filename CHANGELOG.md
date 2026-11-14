# Release-log – Minigolf

## v0.14 – 14. november 2026
Fælles highscore, klar til at blive tændt.
- Når der er sat en database-adresse i src/online.js, sendes scoren til en fælles liste, og highscore-skærmen får en knap, Alle spillere, med de 10 bedste pr. bane
- Kan scoren ikke sendes, huskes den og sendes næste gang
- Uden adresse er alt som før: highscoren ligger kun på enheden
- Serveren er en gratis Firebase Realtime Database. Reglerne ligger i firebase-rules.json, og opsætningen står i README

## v0.13 – 14. november 2026
20 baner, brugernavn på highscoren og mere liv på banen.
- 14 nye baner, så der er 20 faste baner plus Tilfældig bane. Parken, Lysningen, Kystvejen, Dalen, Mosen, Klitterne, Havnen, Højderyggen, Fjorden, Mølleåen, Stenbruddet, Vulkanen, Kæmpen og Mesterskabet. Hver har sit eget præg og sin græsfarve
- Banerne står i banevælgeren fra let til svær, med 1–5 stjerner. Listen kan rulles
- Når runden er slut, vælger man et brugernavn (hver spiller sit), og så kommer scoren på banens highscore. Navnet huskes til næste gang. Man kan springe over
- Highscorelisterne gemmes nu pr. banenavn, og de gamle lister er flyttet med
- Et kamerasving fra hullet tilbage til udslaget ved start af hvert hul
- Sommerfugle og fugle, der flyver henover banen
- Bolden hopper på kanten af hullet, inden den falder i
- Tilfældig bane har stadig ingen highscore

## v0.12 – 14. november 2026
Mere niveauforskel: banerne er ikke længere en lige stigning fra let til svær.
- Hvert hul får en sværhedsværdi ud fra længde, stigninger, toppe, bunkere, vand, pæle og især alt, der bevæger sig
- Hullerne på de genererede baner lægges i en rytme: blød start, et hårdt hul tidligt, et pusterum, en top før slutningen og et finalehul, der er hårdt men ikke det hårdeste
- Hver bane har fået stjerner i banevælgeren: Engen 1, Bakkerne 2, Klassikeren og Skrænten 3, Bjerget 4 og Slugten 5. Tilfældige baner får stjerner efter stil
- Bakkerne er gjort lidt lettere og stilen Hård tydeligt sværere (længere, flere porte, bunkere, vand og pæle), så der er et rigtigt spring mellem trinene
- Highscorelisterne på de genererede baner er nulstillet, fordi hullernes rækkefølge er ændret

## v0.11 – 14. november 2026
Skudbaren er ikke længere sløv i bunden.
- Det mindste skud har nu fart nok til at rulle cirka 35 px i stedet for at næsten stå stille, og kurven op mod fuld kraft er fladere
- Tæt på hullet er skuddet stadig blødt, så korte put er lette at styre

## v0.10 – 14. november 2026
Kun rigtige lyde, ingen syntetiske.
- Alle syntetiserede lyde er fjernet. Spillet bruger kun rigtige optagelser: slag, bold i hul, træ- og metalslag og publikum
- Publikum efter hullet følger resultatet: hul i ét er højest og længst, derefter eagle, birdie og par. Bogey er lavt og kort, og værre end bogey er stille
- Lyde uden optagelse er stille indtil videre: vand, sand, rør, vindmølle, knapper og suk
- Optagelserne ligger i src/snd.js og bliver bygget ind i siden, så hver version stadig er én fil

## v0.9 – 14. november 2026
Rigtige lydoptagelser (udgivet fra en anden samtale, taget med her).
- Optagelser af køllen mod bolden og bolden i hul, træ- og metalslag (Kenney, CC0) og publikum (WebbFilmsUK, CC BY 4.0)

## v0.8 – 14. november 2026
Bedre lyde, lettere vindmøller, rækværk på broer og bolden triller i vandet.
- Nye lyde, alle syntetiserede i spillet (ingen lydfiler): slag med køllens klik og bolden, bolden der falder i koppen og rasler rundt, plask med sprøjt og bobler
- Klapsalver og tilråb efter niveau: hul i ét (kraftig klapsalve og jubel), eagle eller bedre, birdie, par (høflig applaus), bogey (tynd applaus og et skuffet suk) og værre (suk). Slutskærmen har samme slags klapsalve efter hele runden
- Vindmøller er lettere: færre og langsommere vinger, og de genererede møller er lidt mindre
- Broer har sider, som bolden preller af på, så den ikke ryger i vandet fra siden
- Når bolden rammer vand, triller den lidt videre, bliver blå og synker i stedet for at forsvinde

## v0.7 – 12. november 2026
Tilfældig bane, sværere baner og en strammere kant på hullet.
- Ny bane nr. 7: Tilfældig bane. Spillet laver 18 helt nye huller, hver gang du trykker Ny bane (ca. 16 ms)
- Seks stilarter: Blandet, Bakket, Snoet, Åben, Vand og Hård
- Banekode (fx H213601): samme kode giver altid de samme 18 huller. Skriv en kode ind for at spille en bane igen eller sende den videre
- Hurtigt tjek af alle genererede huller: er der fri vej fra start til hul, ellers laves et nyt hul
- Ingen highscore på tilfældige baner. Slutskærmen viser banekoden
- Sværere baner: smallere fairways, flere bunkere, damme og pæle, og nye bevægelige forhindringer på de genererede huller (skydeporte og vindmøller på de brede fairways)
- Hullets kant er strammere: bolden tipper kun i, hvis den ligger eller triller helt tæt på (cirka 2 px uden for kanten, før 9 px), og den skal ramme hullet langsommere
- De fem lange baner er lavet om igen, og highscorelisterne på dem er nulstillet

## v0.6 – 12. november 2026
Større variation på de fem lange baner, og bolden triller selv det sidste stykke i hul.
- Alle 90 huller på de fem lange baner er lavet om. Hvert hul har nu sit eget forløb i stedet for at være en spejlvendt eller omvendt udgave af en fast form
- Fire slags fairways: smalle og snoede, brede alléer og to mellemting, med skrå genveje og 45-graders hjørner
- Åbne huller uden fairway: Ottekanten, Sekskanten, Timeglasset, Tragten, Øen og Vulkanen
- Nyt på de lange baner: damme, broer over vand og pæle, ud over stigninger, fald, runde toppe, skåle og bunkere
- Banerne har tydeligere særpræg: Engen er kort og åben, Bakkerne har toppe og skåle, Skrænten stigninger og fald, Slugten er smal og snoet med sand og pæle, Bjerget er lang med vand og broer
- Hullets kant: ligger eller triller bolden helt tæt på hullet, tipper den selv det sidste stykke i
- Par på de lange baner er strammet og følger hullets længde
- Highscorelisterne fra v0.5 er uændrede i formatet, men banerne er nye, så gamle tider på de lange baner kan ikke sammenlignes

## v0.5 – 12. november 2026
Seks baner med 18 huller hver, i alt 108 huller.
- Banevælger: vælg bane, før runden starter. Hver bane viser sit par og sin bedste runde
- Klassikeren (par 58): de kendte huller med vindmøller, rør, bomme og porte, nu 18 i alt med Slangen, Bjergryggen og Tinderne
- Fem nye lange baner: Engen (par 60), Bakkerne (par 73), Skrænten (par 78), Slugten (par 80) og Bjerget (par 68)
- De nye baner har længere huller med vinkler og knæk, stigninger, fald, runde toppe, skåle ved hullet og enkelte bunkere, men ingen bevægelige forhindringer
- Hver bane har sin egen blanding: Bakkerne har flest runde toppe, Skrænten flest stigninger og fald, Slugten mest sand
- Hullerne på hver bane er ordnet, så de korte og lette kommer først
- Highscore pr. bane. Listerne fra v0.4 starter forfra, fordi banerne er nye
- Scorekortet deler de 18 huller i to halvdele

## v0.4 – 11. november 2026
Flere huller, lyd, flere spillere, bedre sigte og highscore.
- 15 huller: seks nye (Bulerne, To broer, Møllebakken, Vulkanen, Slalom og Rørposten). Banens par er nu 46
- Lyd: slag, bande, sand, plask, rør, vindmølle, bom og port, bold i hul og en lille fanfare. Kan slås fra i menuen og i pausen
- 1–4 spillere på samme telefon: navne, hver sin boldfarve, ét slag ad gangen, og de ventende bolde vises gennemsigtige
- Sigtelinjen viser første afslag på banden
- Blødere kraftkurve og automatisk præcisionsput tæt på hullet
- Fortryd: træk tilbage til ringen, hvor fingeren startede, og slip
- Highscore med de ti bedste runder (navn, slag og dato), gemt på enheden. Erstatter "bedste runde"
- Scorekortet er delt i to halvdele og viser alle spillere

## v0.3 – 11. november 2026
Ny grafik: lys, materialer og bakker med højde.
- Bløde skygger, der bliver lysere længere fra bander, klodser og bro, og en mørk kontaktskygge ved foden
- Sollys fra øverste venstre hjørne: varm solside og kølig skyggeside på alle bander og klodser
- Bander og klodser er lavet af planker med åretegning, samlinger og søm
- Filt med struktur, slidt felt ved tee og nedtrådt filt ved hullet
- Ramper har kam, fod og højdelinjer, og niveauet over eller under rampen er lidt lysere eller mørkere
- Høje er skyggelagt efter solen med højdekurver og kaster selv en blød skygge
- Bolden bliver lidt større og får længere skygge, når den ligger højt
- Sand med revne riller og sænket kant, vand med dybde ved bredden
- Det faste i banen tegnes én gang pr. hul, så spillet stadig kører flydende

## v0.2 – 11. november 2026
Mere avanceret bane og ny grafik.
- Bander og klodser tegnes med højde, sider og skygger
- Bakker: rampe (Bakken, Finalen) og høje (Broen, Finalen)
- Bevægelige forhindringer: vindmølle, svingende bom og skydeport, som også kan skubbe til en bold, der ligger stille
- Rør, der sender bolden over en mur, og bro over vandgraven
- Seks huller er nye eller bygget om: Bakken, Vindmøllen, Broen, Røret, Bommen og Porten
- Bolden ruller med prikker og glans, efterlader spor i græsset og giver sandsprøjt og vandplask
- Omgivelser: eng, træer, buske, blomster, sten, hegn og et lille hus
- Kameraet zoomer ind ved hullet
- Bedste runde starter forfra, fordi banen er ny

## v0.1 – 11. november 2026
Første udgave med kernefunktionerne.
- 9 huller set ovenfra med par på hvert hul
- Træk-og-slip-styring med sigtelinje og kraftmåler
- Boldfysik med bander, skrå vægge og klodser
- Sand (bremser) og vand (ét strafslag, bolden lægges tilbage)
- Maks. 8 slag pr. hul
- Scorekort, bedste runde gemmes
- Pause, start hullet forfra og fuld skærm
- Ingen lyd endnu
