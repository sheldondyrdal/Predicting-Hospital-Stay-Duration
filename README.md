# Predicting Hospital Stay Duration
This project is part of the course "Introduction to Data Science (INF161)" at the University of Bergen (UiB). The project is written in Norwegian.

## Databeskrivelse

Dette datasettet omfatter 8261 individuelt kritisk syke pasienter fra 5 medisinske sentre i USA, registrert i periodene 1989-1991 og 1992-1994.

Hver rad er journal data for innlagte pasienter som oppfylte inklusjons- og eksklusjonskriteriene for ni sykdomskategorier: akutt respirasjonssvikt, kronisk obstruktiv lungesykdom, hjertesvikt, leversykdom, koma, tykktarmskreft, lungekreft, multiple organsvikt med malignitet og multiple organsvikt med sepsis.

Det er 4 datasett (antall pasienter, antall variabler):
- sykehusdata (7740, 3)
- informasjon om sykdomsalvorlighet (4, 20)
- fysiologiske data (7740, 15)
- demografiske data (7742, 6)

**Sykehusdata**

| Variabelnavn   | Rolle               | Type         | Beskrivelse                                             |
|----------------|---------------------|--------------|---------------------------------------------------------|
| pasient_id     | ID                  | Heltall      |                                                         |
| sykehusdød     | Funksjonsvariabel   | Binær        | Død på sykehuset                                        |
| oppholdslengde | Responsvariabel     | Kontinuerlig | Antall dager fra studieinngang til utskrivelse          |




**Sykdomsalvorlighet**

| Variabelnavn                | Rolle            | Type               | Beskrivelse                                                                                                                                                                                                                          |
|-----------------------------|------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pasient_id                  | ID               | Heltall |                                                                                                                                                                                                                                      |
| sykdomskategori_id          | ID               | Heltall             |                                                                                                                                                                                                                                      |
| dødsfall                    | Funksjonsvariabel| Kontinuerlig | Dødsfall på ethvert tidspunkt frem til National Death Index (NDI) data den 31. desember 1994. Noen pasienter skrives ut før slutten av studien og følges ikke opp. Forfatterne hentet informasjon om dødsfall.                        |
| sykdom_underkategori        | Funksjonsvariabel| Kategorisk   | Pasientens sykdomsunderkategori blant ARF/MOSF m/Sepsis, CHF, KOLS, Cirrhose, Tykktarmskreft, Koma, Lungekreft, MOSF m/Malig. Tilgjengelig på dag 1.                                                                                                    |
| sykdom_kategori             | Funksjonsvariabel| Kategorisk          | Pasientens sykdomskategori blant "ARF/MOSF", "KOLS/CHF/Cirrhose", "Kreft", "Koma". Tilgjengelig på dag 1.                                                                                                                                                  |
| antall_komorbiditeter       | Funksjonsvariabel| Kontinuerlig | Antall samtidige sykdommer (eller komorbiditeter) hos pasienten. Verdiene er ordinale, med høyere verdier som indikerer verre tilstand og lavere overlevelseschanser. Tilgjengelig på dag 1.                                                                |
| koma_score                  | Funksjonsvariabel| Kontinuerlig | SUPPORT dag 1 Koma-score basert på Glasgow-skalaen (gitt av en modell). Tilgjengelig på dag 1.                                                                                                                                                         |
| adl_pasient                 | Funksjonsvariabel| Kategorisk   | Indeks for daglige funksjonsaktiviteter (ADL) til pasienten, utfylt av pasienten på dag 7. Høyere verdier indikerer større sjanse for overlevelse.                                                                   |
| adl_stedfortreder           | Funksjonsvariabel| Kontinuerlig | Indeks for daglige funksjonsaktiviteter (ADL) til pasienten, utfylt av en stedfortreder (f.eks. familiemedlem) dag 1. Høyere verdier indikerer større sjanse for overlevelse.                                                |
| fysiologisk_score           | Funksjonsvariabel| Kontinuerlig | SUPPORT fysiologisk score på dag 1 (gitt av en modell).                                                                                                                                                                        |
| apache_fysiologisk_score    | Funksjonsvariabel| Kontinuerlig | APACHE III dag 1 fysiologisk score (uten koma, imp bun, uout for ph1).                                                                                                                                                              |
| overlevelsesestimat_2mnd    | Funksjonsvariabel| Kontinuerlig | SUPPORT-modellens 2-måneders overlevelsesestimat på dag 1 (gitt av en modell).                                                                                                                                                  |
| overlevelsesestimat_6mnd    | Funksjonsvariabel| Kontinuerlig | SUPPORT-modellens 6-måneders overlevelsesestimat på dag 1 (gitt av en modell).                                                                                                                                                  |
| diabetes                    | Funksjonsvariabel| Heltall | Om pasienten har diabetes (1) eller ikke (0). Tilgjengelig på dag 1.                                                                                                                                                |
| demens                      | Funksjonsvariabel| Kontinuerlig | Om pasienten har demens (1) eller ikke (0). Tilgjengelig på dag 1.                                                                                                                                                     |
| kreft                       | Funksjonsvariabel| Kategorisk   | Om pasienten har kreft ("yes"), om den har spredt seg (metastatic), eller om den er frisk ("no"). Tilgjengelig på dag 1.                                                                                                                                        |
| lege_overlevelsesestimat_2mnd| Funksjonsvariabel| Kontinuerlig | Legens 2-måneders overlevelsesestimat for pasienten. Tilgjengelig på dag 1.                                                                                                                                                                                 |
| lege_overlevelsesestimat_6mnd| Funksjonsvariabel| Kontinuerlig   | Legens 6-måneders overlevelsesestimat for pasienten. Tilgjengelig på dag 1.                                                                                                                                                                                 |
| dnr_status                  | Funksjonsvariabel| Kategorisk   | Om pasienten har en ikke-gjenopplivingsordre (DNR) eller ikke. Mulige verdier er "dnr ved innleggelse", "dnr før innleggelse", "mangler", "ingen dnr".                                                                                                   |
| dnr_dag                     | Funksjonsvariabel| Kontinuerlig | Dag for DNR-ordre (<0 hvis før studie, 0 ved innleggelse, NA hvis det ble oppgitt etter innleggelse).                                                                                                                                                                                              |




**fysiologiske data**
| Variabelnavn       | Rolle            | Type        | Beskrivelse                                                                                                                                                                                   |
|-------------------|------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pasient_id        | ID               | Heltall     |                                                                                                                                                                                               |
| blodtrykk         | Funksjonsvariabel| Kontinuerlig| Gjennomsnittlig arterielt blodtrykk hos pasienten, målt på dag 1.                                                                                                                                                                    |
| hvite_blodlegemer | Funksjonsvariabel| Kontinuerlig| Antall hvite blodlegemer (i tusen) målt på dag 1.                                                                                                                                              |
| hjertefrekvens    | Funksjonsvariabel| Kontinuerlig| Pasientens hjertefrekvens målt på dag 1.                                                                                                                                                       |
| respirasjonsfrekvens | Funksjonsvariabel| Kontinuerlig| Pasientens respirasjonsfrekvens målt på dag 1.                                                                                                                                               |
| kroppstemperatur  | Funksjonsvariabel| Kontinuerlig| Kroppstemperatur i Celsius-grader målt på dag 1.                                                                                                                                               |
| lungefunksjon     | Funksjonsvariabel| Kontinuerlig| \(PaO_2/FiO_2\) forhold målt på dag 1. Forholdet mellom arterielt oksygen partialtrykk (PaO2 i mmHg) og fraksjonert inspirert oksygen (FiO2 uttrykt som en fraksjon). Ofte brukt klinisk indikator på hypoksemi, selv om dets diagnostiske nytteverdi er kontroversiell. Spesifikke verdier kan assosieres med forskjellige nivåer av dødelighet. Det kan være verdt å vurdere å kategorisere disse verdiene etter noen intervaller: [litfl.com/pao2-fio2-ratio/](https://litfl.com/pao2-fio2-ratio/) |
| serumalbumin      | Funksjonsvariabel| Kontinuerlig| Serum albuminnivåer målt på dag 1. Albumin er et protein i blodet. Høyt albumin indikerer dehydrering. Lavt albumin kan tyde på lever- og nyresvikt, underernæring, og økt dødsrisiko.                                                                                                                                                            |
| bilirubin         | Funksjonsvariabel| Kontinuerlig| Bilirubinnivåer målt på dag 7. Nivåene måles for å vurdere leverfunksjon og opphopning i kroppen.                                                                                                                                                                |
| kreatinin         | Funksjonsvariabel| Kontinuerlig| Serumkreatininnivåer målt på dag 1. Nivåene måles for å vurdere nyrefunksjon og hvordan kroppen filtrerer avfall.                                                                                                                                                            |
| natrium           | Funksjonsvariabel| Kontinuerlig| Serum natriumkonsentrasjon målt på dag 1. Nivåene måles for å sjekke kroppens væskebalanse og funksjon av nyrer.                                                                                                                                                      |
| blod_ph           | Funksjonsvariabel| Kontinuerlig| Arteriell blod-pH at day 1. Blodets pH er vanligvis mellom 7,35 og 7,45. Unormale resultater kan skyldes lungesykdom, nyresykdom, metabolske sykdommer, eller medisiner. Hode- eller nakkeskader eller andre skader som påvirker pusting kan også føre til unormale resultater. |
| glukose           | Funksjonsvariabel| Heltall     | Glukosenivåer målt på dag 1. Nivåene måles for å vurdere energinivå og blodsukkerkontroll i kroppen.                                                                                                                                                                   |
| blodurea_nitrogen | Funksjonsvariabel| Heltall     | Blodurea-nitrogennivåer målt på dag 1. Blodurea-nitrogen er et avfallsstoff. Nivået måles for å sjekke nyrefunksjon og hvordan kroppen fjerner avfall.                                                                                                                                                         |
| urinmengde        | Funksjonsvariabel| Heltall     | Urinmengde målt på dag.  1.                                                                                                                                                                     |



**Demografisk data**

| Variabelnavn  | Rolle            | Type        | Beskrivelse   |
|---------------|------------------|-------------|------------------------------------------------------------------------------------------------------------------|
| pasient_id    | ID               | Heltall     |                                                                                                                  |
| alder         | Funksjonsvariabel| Kontinuerlig| Pasientenes alder i år.                                                                                           |
| kjønn         | Funksjonsvariabel| Kategorisk  | Pasientens kjønn. Oppførte verdier er {mann, kvinne}.                                                            |
| utdanning     | Funksjonsvariabel| Kategorisk  | Antall år med utdanning                                                                                          |
| inntekt       | Funksjonsvariabel| Kategorisk  | Pasientens inntekt. Oppførte verdier er {"$11-$25k", "$25-$50k", ">$50k", "under $11k"}.                         |
| etnisitet     | Funksjonsvariabel| Kategorisk  | Pasientens etnisitet. Oppførte verdier er {asiatisk, svart, latinsk, mangler, annen, hvit}.                      |



Kilde: [https://archive.ics.uci.edu/dataset/880/support2](https://archive.ics.uci.edu/dataset/880/support2). I tillfelle at det er forskjeller mellom kilden og denne versjonen, så er det denne versjonen som gjelder for prosjektet. 
