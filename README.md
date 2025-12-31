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

---

## Naudojamos Python bibliotekos

* **reportlab** - PDF generavimui
* **python-barcode** - barkodų kūrimui
* **selenium** - duomenų nuskaitymui iš svetainės
* **pillow** - paveikslėlių apdorojimui
* **InquirerPy** - Python CLI UI

---

## Panaudojimas ir nustatymai

Yra galimybė pagreitinti darbą naudojant **komandų eilutės nustatymus (runtime variables):**

```bash
python3 pagrindinis.py [Nustatymai]
```

### Galimos parinktys

| Parinktis       | Aprašymas                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| `-h, --help`    | Parodo pagalbos lentelę                                                                                  |
| `-v, --version` | Parodo versiją                                                                                           |
| `-S`            | Paleidžia „WebScraper“ modulį, kuris paima duomenis iš iBibliotekos ir surašo juos į lentelę             |
| `-G`            | Sugeneruoja lentelę su brūkšninių kodų tekstais, leidžia pasirinkti, kiek norima brūkšninių kodų (1–100) |
| `-I`            | Surašytus ISBN kodus paverčia lengvai spausdinama brūkšninių kodų matrica                                |
| `-F`            | Tikrina knygų duomenis ir ar teisingai užklijuoti brūkšniniai kodai                                      |
| `-i`            | Nurodo įvesties CSV failą                                                                                |
| `-o`            | Nurodo išvesties CSV failą                                                                               |
| `--gui`         | Paledzia naudotojo aplinka                                                                               |

---

### Pavyzdys

```bash
python3 pagrindinis.py -S -i ./csv/Knygos.csv -o ./csv/Knygos_perasityos.csv
```

---

## Su Kompoliavimas

```bash
pyinstaller ./pagrindinis.py
```

## TODO

* Apmasyti funcionaluma kuris leistu is vienos lenteles sulieti lentelias, pagrinde perasant isnb koda pagal autoriu ir pavadinima
* Knygu ieskojimas pagal pavadinima, su galimybe patikslinti su data
* Ivedus pavadinima ir metus  galima duoti pasirinkima nnaudotojui kad pasirinktu kuri knyga
* Duoti galimybe kai skanuoja pataisyti ISNB koda
* Gaves knyga be bakrodo ir ISNB Nautotojas turetu galeti irastyti pavadinima, metus. Ir gauti autoriu ir isnb koda. Poto is atskiros lenteles turima galeti paiimti isnb koda ir ji atspauzdinti
* Padaryti GUI
* Apmasyti funcionaluma kuris leistu is vienos lenteles sulieti lentelias, pagrinde perasant isnb koda pagal autoriu ir pavadinima
* Knygu ieskojimas pagal pavadinima, su galimybe patikslinti su data
* Ivedus pavadinima ir metus  galima duoti pasirinkima nnaudotojui kad pasirinktu kuri knyga
* Duoti galimybe kai skanuoja pataisyti ISNB koda
* Gaves knyga be bakrodo ir ISNB Nautotojas turetu galeti irastyti pavadinima, metus. Ir gauti autoriu ir isnb koda. Poto is atskiros lenteles turima galeti paiimti isnb koda ir ji atspauzdinti
* Pasibandyti padaryti API bendravima tarp funciju ir lenteles
* Padaryti GUI

## Kas padaryta

* [x] "Brūkšninio kodo kūrimas",
* [ ] "Knygų rašymas į iBiblioteką pagal ISBN CSV",
* [ ] "Knygų rašymas į iBiblioteką pagal ISBN Scanner",
* [ ] "ISBN iš CSV į PDF",
* [ ] "Lėtesnė knygų paieška (Knygos_Su_Viskuom)",
* [ ] "Lėtesnė knygų paieška (Bibliotekos Knygos - VIsos knygos)",
* [ ] "Suvedimas pagal pavadinima"

* prideti buksinio kodu genervimo sistemai vietoje cash i temp dir ikelima kaip per test aplinka yra padaryta

## Dependense

### Google fonts

* Inter
*+ Playfair_Display
