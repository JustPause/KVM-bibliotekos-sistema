# KVM Bibliotekos Sistema

KVM Bibliotekos Sistema - tai Python pagrindu sukurta **CLI / GUI aplikacija**, skirta
bibliotekų knygų duomenų apdorojimui, barkodų generavimui ir integracijai su
**Google Sheets** bei **iBiblioteka** sistema.

Projektas skirtas realiam bibliotekos darbui: knygų skenavimui, ISBN tvarkymui
ir efektyviam barkodų spausdinimui.

## Ką ši sistema daro?

- Nuskaito knygų duomenis iš CSV arba skanerio
- Ieško knygų informacijos iBiblioteka svetainėje
- Generuoja barkodus knygoms su arba be ISBN
- Kuria PDF failus, optimizuotus A4 spausdinimui
- Tikrina duomenų atitikimą Google Sheets
- Palaiko CLI ir GUI režimus

## Greitas paleidimas

### Repositorijos konavimas

```bash
git clone https://github.com/JustPause/KVM-bibliotekos-sistema.git
cd KVM-bibliotekos-sistema
```

### Virtualios aplinkos sukūrimas

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Google sujungimas

Kadangi programa daug naudoja **Google Sheets API**, reikia suteikti jai prieigą. Tai galima padaryti sekant **Authorize credentials for a desktop application** instrukciją svetainėje:  
<https://developers.google.com/workspace/sheets/api/quickstart/python>

Atsisiuntus, reikia įdėti failą į ```RepoHome/config/.env/sheet.json.```. Ten turėtų būti **client_secret.json**.

### Su kongiguravimas

Taip pat dar reikia sukonfigūruoti **sheet.json**:
```json
{
  "sheet_id": "lentelės id",
  "range_template": "Lapo pavadinimas!A{row}:D{row}",
  "rage": "Lapo pavadinimas!A:D",
  "rage_with_catalog": "Lapo pavadinimas!A:I",
  "rage_isbn_collom": "Lapo pavadinimas!D:D",
  "rage_all": "Lapo pavadinimas!A:K",

  "rage_korteles": "Lapo pavadinimas!H{row}:H{row}",
  "rage_isbn": "Lapo pavadinimas!D{row}:D{row}",
  "rage_vardas": "Lapo pavadinimas!J{row}:J{row}",
  "rage_data": "Lapo pavadinimas!K{row}:K{row}",
  "rage_func": "Lapo pavadinimas!I{row}:I{row}",

  "card_table_id": "kortelių sistemos ID",
  "card_table_name": "Lapo pavadinimas!A:F",

  "rage_asmeniniai_duomenys": "Lapo pavadinimas!H:J",
  "rage_asmeniniai_duomenys_row": "Lapo pavadinimas!H{row}:J{row}",
  "rage_asmeniniai_duomenys_row_plius_data": "Lapo pavadinimas!H{row}:K{row}"
}
```

Su laiku turėtų būti galima padaryti, kad nereikėtų tiek daug suvesti ranka.

Šis JSON failas gyvens: ```RepoHome/config/.env/sheet.json```

### Programos paleidimas

```bash
python3 pagrindinis.py
```

Norint pamatyti GUI 

```bash
python3 pagrindinis.py --gui
```

---

## CLI naudojimas

```bash
python3 pagrindinis.py [parinktys]
```

### Galimos parinktys
<!-- Start_Helptable -->
| Parinktis | Aprašymas |
|----------|----------|
| `-h, --help` | Parodo pagalbos informaciją |
| `-v, --version` | Parodo programos versiją |
| `-S, --webScraper` | Nuskaito duomenis iš iBiblioteka |
| `-G, --generate` | Generuoja naujus barkodus |
| `-I, --isbnPdf` | Konvertuoja ISBN CSV į PDF |
| `-C, --check` | Tikrina duomenis su Google Sheets |
| `-i, --input` | Įvedimo failas |
| `-o, --output` | Išvedimo failas |
| `--gui` | Paleidžia grafinę sąsają |
<!-- End_Helptable -->


### Pavyzdys

```bash
python3 pagrindinis.py -S -i ./csv/Knygos.csv -o ./csv/Knygos_parsitytos.csv
```

---

## Testavimas

```bash
python3 -m unittest discover -s tests
```

---

## Priklausomybės

### Python bibliotekos
- `reportlab` - PDF generavimui
- `python-barcode` - barkodų kūrimui
- `selenium` - duomenų nuskaitymui iš svetainės
- `pillow` - paveikslėlių apdorojimui
- `InquirerPy` - CLI vartotojo sąsaja

### Šriftai
- Inter
- Playfair Display
 
## Roadmap / TODO

- [ ] ISBN taisymas skenavimo metu
- [ ] Knygų be ISBN atpažinimas pagal pavadinimą
- [ ] API integracija su Google Sheets
- [ ] PDF naudotojo dokumentacija
- [x] GUI realizacija

---

## Autorius

**Justinas**  
Projektas skirtas bibliotekos darbo automatizavimui ir procesų optimizavimui.
