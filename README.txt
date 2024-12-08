# INF161 prosjekt
## Filer
-prosjekt.ipynb, filen hvor utforskende datanalyse, variabelutvinning og datamodellering skjer
-model.pkl, filen hvor modellen er lagret
-trasnformations.py, filen for hjelpefunksjoner som er fra prosjekt.ipynb
    Merk at trasnformations.py ikke har noen "nye" funksjoner, men kreves for å importere funksjonene til app.py
-app.py, filen som oppdaterer nettsiden, og er den man må kjøre for at nettsiden skal fungere
-index.html, filen som ansvarlig for skjemaet som brukes på nettsiden, HTML Forms

## Datapakker som kreves for å kjøre all kode
-numpy
-pandas
-flask
-waitress
-sklearn
-scipy
-plotly
-pickle

## Kjøring av nettside (app.py)
-påse først at cmd er "prosjekt"-mappen
-deretter fra terminalen skriv "python app.py"
-gå inn på lokal nettside http://localhost:8080/

prosjekt.ipynb kjøres som normalt
prosjekt.ipynb trenger ikke å kjøres på forhånd for å kjøre nettsiden, da modellen er allerede er lagret i "model.pkl".