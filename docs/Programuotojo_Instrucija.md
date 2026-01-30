# Programa Barkodas

###### Versija: 0.1.0 
###### Data: 2026 01 21
	
Programa leidžia lengviau atlikti darbus bibliotekos **Google Sheets** lentelėse. Ji sukurta specifiškai pagal **Kauno Valdorfo mokyklos** reikalavimus, todėl gali nebūti idealiai pritaikyta kitoms bibliotekų sistemoms. Tačiau, suprantant **kodą**, galima nesunkiai pridėti bet kokį norimą funkcionalumą.

Programa leidžia bibliotekos administratoriui (-ei):

- Atlikti knygų inventorizaciją,
- Kurti barkodus ir paruošti juos spausdinimui,
- Vykdyti knygų išdavimą ir grąžinimą.

## Auditorija

Programa skirta paprastam naudotojui - *galutiniam vartotojui*. Pagrindinis tikslas - būti kuo *paprastesnei*, *aiškesnei* ir *lengvai naudojamai* šiai naudotojų grupei.

## Sisteminiai reikalavimai

Programa geriausiai ištestuota **Linux (Linux 6.12)** aplinkoje, ypač **Debian** ir **Manjaro** sistemose.

- RAM naudojimas kartais gali siekti iki **3 GB**, ypač naudojant automatinę knygų surašymo sistemą.
- Rekomenduojama turėti bent **4 GB RAM**.
- Procesorius gali būti vidutinio našumo - svarbu, kad palaikytų operacinės sistemos funkcionalumą.
- Disko vietos poreikis nedidelis - **apie 2 GB**.
- Programa daug duomenų kompiuteryje nesaugo.

## Ideigimas

Diegiant programą reikės naudotis terminalu ir keliomis pagalbinėmis programomis.

Svarbiausia:

- **Python 3** su **python3-dev**
- **build-essential**

Programa naudoja šias sistemas ir bibliotekas:

## Sistemos

### wxPython

Reikalingos bibliotekos:

> libgtk-3-dev
> libglib2.0-dev
> libsm-dev
> libnotify-dev
> libwebkit2gtk-4.1-dev
> libjpeg-dev
> libtiff-dev
> libpng-dev
> libexpat1-dev
> libcurl4-openssl-dev

### Pillow

> libjpeg-dev
> zlib1g-dev
> libtiff-dev
> libfreetype6-dev
> liblcms2-dev
> libwebp-dev

### ReportLab

> libfreetype6-dev

### Python

> Python 3.9 - naujausia versija

### Selenium, viena is narsykliu

> Google Chrome,
> Chromium,
> Firefox,
> Microsoft Edge

### Internetas & SSL

Naudojamos bibliotekos:

> google-api-*
> requests
> oauthlib
> urllib3

## Diegimo vadovas

Yra keli būdai gauti programą: per Git, per naršyklę arba naudojant terminalą. Alternatyvus būdas pateiktas šioje [nuorodoje](https://github.com/JustPause/KVM-bibliotekos-sistema)

```sh
git clone https://github.com/JustPause/KVM-bibliotekos-sistema.git
```

Rekomenduojama visas priklausomybes diegti **virtualioje aplinkoje**:

```sh
python3 -m venv .venv 
source .vvenv/bin/activate
pip3 install -r requirements.txt
```

Jeigu diegimas pavyko, programą galima paleisti **GUI** režimu:

```sh
python3 ./pagrindinis.py --gui     
```

## Programos sukūrimas (build)

Norint sukurti atskirą vykdomąjį failą, reikia paleisti:

```sh
python3 ./build.py
```

Prisijungimas yra labai svarbus - be jo neveiks ryšys su **Google Sheets** lentelėmis.

Sukūrimo metu aplanke **dist/** turėtų atsirasti vienas vykdomasis failas.

## Greitas paleidimas (Quick Start)

Visa komanda vienu kartu:

```sh
git clone https://github.com/JustPause/KVM-bibliotekos-sistema.git
python3 -m venv .venv 
source .vvenv/bin/activate
pip3 install -r requirements.txt
python3 ./build.py
```

Gautas failas bus aplanke dist/.

# TODO
- Pagrindinių funkcijų aprašymas
	- Skyrius po skyriaus: kas daroma, kaip naudotis, pavyzdinės užduotys su veiksmų seka ir ekrano pavyzdžiais.

## konfigūracija ir nustatymai
Visa pagrindinė konfigūracija yra faile: 

```sh
config/.env/sheet.json
```

Failas ```config.json``` pateikia autoriaus kontaktus bei pagrindinius programos nustatymus.

## Saugumas ir privatumas

Aukšto lygio saugumo nėra. Svarbiausia:

- neviešinti **Google API** rakto,
- saugoti prisijungimo duomenis.

## Licenzija

GPL-3 [LICENSE](LICENSE.md)

## Kontaktai ir pagalba
Butu gerai tiesie i [GitHub](https://github.com/JustPause/KVM-bibliotekos-sistema)

O as *Justinas Stankūnas* esu pasiekemeas *IamJustStan@hotmail.com*
