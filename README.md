# KVM Bibliotekos Sistema

Mano užduotis buvo sukurti programą knygų apdorojimui ir jų suvedimui į pagrindinę **Google Sheets** lentelę.
Tam buvo sukurta programa **WebScraper.py**. Pagal idėją, ši programa gauna lentelę **(.csv)**, iš jos perskaito po vieną eilutę ir pagal pateiktą informaciją ieško duomenų svetainėje [**iBiblioteka**](https://ibiblioteka.lt/metis/).
Gauti rezultatai išsaugomi naujame faile (taip patogiau perkelti duomenis į pagrindinę lentelę). Šis naujas failas vėliau importuojamas į didįjį **Google Sheets** dokumentą.

---

## Antroji dalis

Kai kurios knygos neturi savo **barkodo** arba **ISBN**. Tokias knygas nepatogu skenuoti, todėl joms reikia sugeneruoti barkodą.
Faile **LaisviBarkodai.csv** yra pateikti laisvi kodai, kuriuos galima atspausdinti, taip pat yra galimybė juos eksportuoti tiesiai į **PDF** failą.

---

## Trečiasis funkcionalumas

Paskutinis, bet labai svarbus funkcionalumas – tai knygų, turinčių **ISBN**, bet neturinčių barkodų, suradimas.
Kai kurios knygos randamos [**iBibliotekoje**](https://ibiblioteka.lt/metis/), tačiau dalies ten nėra.
Tokiems įrašams reikia sugeneruoti barkodus ir juos atspausdinti, kad būtų galima užklijuoti ant knygų.

Kita problema – popieriaus taupymas: reikia sudėti kuo daugiau barkodų ant vieno **A4** lapo, bet tuo pačiu turėti galimybę žinoti, kuris barkodas priklauso kuriai knygai.
Mano sprendimas – generuoti barkodus kartu su knygos pavadinimu.
Tai atlieka programa **ISBNGenotator.py** – ji paima duomenis iš **.csv** failo, atskiria, kur yra 10 simbolių senasis ISBN (iki 2007 m.) ir 13 simbolių naujasis, sugeneruoja **PDF** failą, kurį galima atspausdinti ir priklijuoti.

---

## Naudojimo instrucija

[Naudojimo_Instrucija](./naudojimo_Instrucija.md)

---

## Kaip paleisti

Norint paleisti programą (pvz., Linux sistemoje), reikia sukurti Python virtualią aplinką:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Kai viskas susiinstaliuos, paleidžiama taip:

```bash
python3 pagrindinis.py
```

## Priklausomybės / Dependencies

### Naudojamos Python bibliotekos

* **reportlab** - PDF generavimui
* **python-barcode** - barkodų kūrimui
* **selenium** - duomenų nuskaitymui iš svetainės
* **pillow** - paveikslėlių apdorojimui
* **InquirerPy** - Python CLI UI

### Google fonts

* Inter
* Playfair_Display

## Su Kompoliavimas

Veikia ir win in linux :D

```bash
python3 ./build.py
```

## Testai

```bash
python3 -m unittest discover -s tests
```

## Panaudojimas ir nustatymai

Yra galimybė pagreitinti darbą naudojant **komandų eilutės nustatymus (runtime variables):**

```bash
python3 pagrindinis.py [Nustatymai]
```

### Galimos parinktys
<!-- Start_Helptable -->
| Parinktis          | Aprašymas                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| `-h, --help`       | Parodo pagalbos lentelę                                                                                  |
| `-v, --version`    | Parodo versiją                                                                                           |
| `-S, --webScraper` | Paleidžia „WebScraper“ modulį, kuris paima duomenis iš iBibliotekos ir surašo juos į lentelę             |
| `-G, --generate`   | Sugeneruoja lentelę su brūkšninių kodų tekstais, leidžia pasirinkti, kiek norima brūkšninių kodų (1–100) |
| `-I, --isbnPdf`    | Surašytus ISBN kodus paverčia lengvai spausdinama brūkšninių kodų matrica                                |
| `-C, --check`      | Tikrina knygų duomenis ir ar teisingai užklijuoti brūkšniniai kodai                                      |
| `-i, --input`      | Įvedimo failas                                                                                           |
| `-o, --output`     | išvedimo failas                                                                                          |
| `--gui`            | Paleisti grafinę vartotojo sąsają                                                                        |
<!-- End_Helptable -->

### Pavyzdys

```bash
python3 pagrindinis.py -S -i ./csv/Knygos.csv -o ./csv/Knygos_perasityos.csv
```

## TODO GUI

* [ ] Įvedus pavadinimą ir metus, galima duoti pasirinkimą naudotojui, kad pasirinktų kurią knygą
* [ ] Duoti galimybę skenavimo metu pataisyti ISBN kodą
* [ ] Gavęs knygą be barkodo ir ISBN, naudotojas turėtų galėti įrašyti pavadinimą ir metus, ir gauti autorių bei ISBN kodą. Po to iš atskiros lentelės turėtų būti galima paimti ISBN kodą ir jį atspausdinti
* [x] Pasibandyti padaryti API bendravimą tarp funkcijų ir lentelės
* [x] Padaryti GUI

## Kas padaryta

* [x] "Brūkšninio kodo kūrimas",
* [ ] "Knygų rašymas į iBiblioteką pagal ISBN CSV",
* [ ] "Knygų rašymas į iBiblioteką pagal ISBN Scanner",
* [ ] "ISBN iš CSV į PDF",
* [ ] "Lėtesnė knygų paieška (Knygos_Su_Viskuom)",
* [ ] "Lėtesnė knygų paieška (Bibliotekos Knygos - VIsos knygos)",
* [ ] "Suvedimas pagal pavadinima"
* [x] prideti versijos parodima kamputija su mano duomenimis

* [ ] prideti buksinio kodu genervimo sistemai vietoje cash i temp dir ikelima kaip per test aplinka yra padaryta
* [ ] Kodas kurio ieskau - 123 , python3 ./pagrindinis.py -S -o ./tests/file.csv -> add filert to only show knygos
* [ ] Padaryti naudotojo instrucija, kad galeima butu visada paziureti ir zinoti kaip kas veikia. Kaip dokumnetacija tik naudotojui
* [ ] I build.py priedeti md to pdf formatavima
* [ ] pridegti sugrazinimo sistema

### Darbo lentele

Kas kur turetu buti, koki funcionaluma turi tureti **cli** aplikacija ir **gui** palikacija

| versija | webScraper | generate | isbnPdf | check | input | output | gui | comentaas                                             |
| ------- | ---------- | -------- | ------- | ----- | ----- | ------ | --- | ----------------------------------------------------- |
| x       |            |          |         |       |       |        |     | versija                                               |
|         | x          |          |         |       |       |        |     | Skanavimas is klaveturos / Scannerio                  |
|         | x          |          |         |       | x     |        |     | Skanavimas is failo                                   |
|         |            | x        |         |       |       | x      |     | Sugeneravimas nauju barkodu                           |
|         |            |          | x       |       | x     | x      |     | is exel i pdf kad atspauzdintu                        |
|         |            |          |         | x     |       |        |     | patikrina ar yra google sheets                        |
|         |            |          |         | x     |       | x      |     | patikrina ar yra google sheets jei nera suraso i exel |
| x       |            |          |         |       |       |        | x   | parodyti versija                                      |
|         | x          |          |         |       |       |        | x   | Skanavimas is klaveturos / Scannerio                  |
|         |            | x        |         |       |       | x      | x   | Sugeneravimas nauju barkodu                           |
|         |            |          | x       |       |       | x      | x   | Is buffer kuri iraso programai veikent                |
|         |            |          |         | x     |       | x      | x   | patikrinti ar yra google sheets                       |
