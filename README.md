# KVM-bibliotekos-sistema

Mano uzduotis buvo sukurti progrma knygu apdirbimui ir sudejimui i didiji pagrindinei **Google sheets** lentelia, Tam sukurta Yra **WebScraper.py** pagal ideja tai yra programa kuri gauna lentelia **(.csv)** ir is jos beskaito po viena eilu ir issiesko [**iBibliotekos**](https://ibiblioteka.lt/metis/) svetaines. Gautus rezultatus sudeda i nauja faila (nes taip buvo patogiau perdeti duomenis). Kury poto reiks perdeti ididi **Google sheets** dokumenta.

Andtroji veda buvo kaikurios knygos neturi savo **barkodo**, nei **isbn**. Tai jas yra saliginai nepatogu suskanuoti. Del to jiems reikia sukurti barkoda Failia **LaisviBarkodai.csv** yra laisvi kodai kuruos galima atspauzdinti, yra taip pat yra galimybe tiesei i **pdf** faila exportuoti

Paskurinis funcionalumas bet patsai nuobodziausias, yra knygu su **isbn** bet be barkodu surasimas. Kaikurtos knugos yra [**iBibliotekos**](https://ibiblioteka.lt/metis/) bet dalis nera. Taigi toks kngoms reikia sukurti barkodus ir juo zulipinrti. Bet norint atspauztini ant **4a** lapo. kita problema yra popieriaus taupimas kad kuo daugiau iskaitomu barkodu ant lapo sudeti dar kita beda kad kai turi 80 knygu ir 80 barkodu kai zinoti greitai kur ka klijuoti, mano sprendimas kombinuoti su pavadinimu knygos, Cia ateina **ISBNGenotator.py** sis failas turetu pagves duomenis is **.csv** failo, atskirti kur yra 10 simboliu kuris buvo naudotis iki 2007 ir 13 kurie naudojami iki dabar. Su jais sudaro **pdf** ir ji galima atspauzdinti ir uzklijuoti

## Kad paleisti

Noreint paleisti programa bent ant linux sistemos reikia sukurti python vitual aplinka, Tai padaryti galima su

## Kokios python bibliotekos naudojemos

- reportlab 
- python-barcode 
- selenium 
- pillow

### python WebScraper.py

```python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Tada viskas turetu buti susiinstaliavia

```python
python Pagrindinis.py
```

## Panaudojimas ir nustatimai

Yra galimybe pagreitinti darbus su **runtime variable**

```python
python Pagrindinis.py [Nustatimai]
```
<!-- Options -->

    -h, --help      Atspauzdinia sia lentelia
    -v, --version   Versija

    -S              WebScraper pasiemant duomenis is iBiliotekos ir juos sudedant i lentelia
    -G              Sugeneruoja Lentelia barcodu tekstu

    -i              CSV failas sis kurio paiimti nuomenis
    -o              CSV failas i kury surasyti nuomenis

<!-- Options -->

### Pavizdys

```python
python Pagrindinis.py -S -i ./csv/Knygos.csv -o ./csv/Knygos_perasityos.csv
```

## ToDo

- [ ] Main failas kuris leidzia valdyti kitus metodus, ir ju skirtingus metodus
- [ ] Panaudojemi metodai turetu buti pasiekemi ir askirti i savo faila, kaip qr codu surasimas i pdf fiala