# Programa Barkodas

###### versija: 0.1.0 
###### Data: 2026 01 21
	
Programa leidzia lengviau atlikti darbus bibliotekos google sheet leteliai. Programa yra padaryta sesifiskai pagal Kauno Valdorfo mokyklos reikalavimus, del to galimai nebutu tobulai pritaikia kitoms bibliotekos sistemoms, bet suprantant **koda** galima prisideti koki tik nori fincianaluma. Programa leidiza bibliotekos administratoriai (-ui), atlikti knygu surasima, barkodu sukurima ir paruosima atspauzdinti, isdavima bei sugrazinima.

## Auditorija

Programa yra skirta paprastam naudotojui vadinamam **galutins vartotojas**, programos tikslas yra buti suprantamai ir parastai siai zmoniu grupei.

## Sisteminiai reikalavimai

Programa geriausiai istestuota ant **Linux (Linux 6.12)**, **Debian** ir **Manjaro**. Programa kartais isoka iki 3 GB ram naudojumo, kai naudojema automatine knygu surasimo sistema. Del to rekomaneuoja buti bent 4GB ram. Procesoriaus nereikia galingo gal tik modrnaus kad palaikytu operacines sitemos funcionaluma. Bendros vietos nereikia daug, bent 2GB butu patenkinama. programa daug duomenu neisaugo kompiuterija

## Ideigimas

Ideigent programa reikes pasinaudoti terminalu, bei keliomis programomis. Pati sverbiausia **Python3** programa, su **python3-dev** palaikimu, systema taip pat turetu tureti **build-essential**. programa naudotoja:

## Sistemos

### wxPython

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

> Python 3.9 – naujausia versija

### Selenium, viena is narsykliu

> Google Chrome,
> Chromium,
> Firefox,
> Microsoft Edge

### Internetas & SSL

> google-api-*
> requests
> oauthlib
> urllib3

## Diegimo vadovas

yra keli budai gauti programa viens per git kitas, per narsykle arba terminalo alternatva [nuorodoje](https://github.com/JustPause/KVM-bibliotekos-sistema)

```sh
git clone https://github.com/JustPause/KVM-bibliotekos-sistema.git
```

šaltinio koda (source code) galima patartina per terminala atsisiusti pagalbines biblioetelas, man bent reikalaja sukurti vituralia aplinka visoms salutinems bibliotekoms

```sh
python3 -m venv .venv 
source .vvenv/bin/activate
pip3 install -r requirements.txt
```

Jei sekmingai vakyko vadinasi galima paleisti programa ir paziurtei kaip ji atrodo, tai galima padaryti su komanda

```sh
python3 ./pagrindinis.py --gui     
```

Norint sudaryti atskira programa reiketu panaudoti
Prisijungimas labai svarbus nes be jo nevieks susijungimas su google sheets lentelia

```sh
python3 ./build.py
```

naujemia aplankalia **dist** turetu buti vienas norimas failas. 

## Greitas paleidimas (Quick Start)

Taigi greita komanda viskam greitai padaryti
aplankalia **dist** turetu buti vienas norimas failas

```sh
git clone https://github.com/JustPause/KVM-bibliotekos-sistema.git
python3 -m venv .venv 
source .vvenv/bin/activate
pip3 install -r requirements.txt
python3 ./build.py
```

# TODO
- Pagrindinių funkcijų aprašymas
	- Skyrius po skyriaus: kas daroma, kaip naudotis, pavyzdinės užduotys su veiksmų seka ir ekrano pavyzdžiais.

## konfigūracija ir nustatymai
Visa konfigutacija yra ```sh src/.env/sheet.json```
Kitas config.json failas tesiog duoda mano kontaktus ir pragramos konfiguracija kur nusistato beveikent. 

## Saugumas ir privatumas
Daug saugumo nera, tesiog reikia neaviesinta savo google api rakto ir pagrinde viskas

## Licenzija
GPL-3

## Kontaktai ir pagalba
Butu gerai tiesie i [GitHub](https://github.com/JustPause/KVM-bibliotekos-sistema)

O as *Justinas Stankūnas* esu pasiekemeas *IamJustStan@hotmail.com*
