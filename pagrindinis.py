import os
from InquirerPy import prompt,inquirer
from InquirerPy.validator import EmptyInputValidator, PathValidator
from src.ibibliotekaWebScraper import SurasytiPoVienaEilute
from src.barcodeKurimas import barcode_generator

# Joku komentaru del Anglu ir Lietuviu kalbos naudojimo. Nors tai nepagal visas taisykles, angla kalbiai neskaitys sio kodo

Klausimai = [
    "Brūkšninio kodo kūrimas",
    "Knygų rašymas į iBiblioteką pagal ISBN",
    "ISBN iš CSV į PDF",
    "Lėtesnė knygų paieška"
]

suformatuotiKlausimai = [
    {
        "type": "list",
        "name": "veiksmas",
        "message": "Pasirinkite, kokią funkciją norite atlikti:",
        "choices": Klausimai,
    }
]

result = prompt(suformatuotiKlausimai)
pasirinkimoIndexas = Klausimai.index(result['veiksmas'])

match pasirinkimoIndexas:
    case 0: # Brūkšninio kodo kūrimas

        integer_val = inquirer.number(
            message="Kiek barkodu sukurti:",
            min_allowed=1,
            max_allowed=10*5*10,
            validate=EmptyInputValidator(),
        ).execute()

        home_path = os.path.join(os.getcwd(), "csv", "Knygos_Be_Barkodo.csv")
  
        src_path = inquirer.filepath(
            message="Pasirinkite is kurio failo bus imami duomenys:",
            default=home_path,
            validate=PathValidator(),
            only_files=True,
        ).execute()

        barcode_generator(int(integer_val), src_path)
    case 1: # Knygų rašymas į iBiblioteką pagal ISBN

        home_path = os.path.join(os.getcwd(), "csv")

        src_path = inquirer.filepath(
            message="Pasirinkite is kurio failo bus imami duomenys:",
            default=os.path.join(home_path, "Knygos_Be_Barkodo.csv"),
            validate=PathValidator(),
            only_files=True,
        ).execute()
  
        dest_path = inquirer.filepath(
            message="Pasirinkite i kurio faila bus idedami duomenys:",
            default=os.path.join(home_path, "Knygos_Su_Viskuom.csv"),
            validate=PathValidator(),
            only_files=True,
        ).execute()

        SurasytiPoVienaEilute(src_path,dest_path)
    case 2: # ISBN iš CSV į PDF
        print(pasirinkimoIndexas)
    case 3: # Lėtesnė knygų paieška
        print(pasirinkimoIndexas)
    case _: # (｡･ˇ_ˇ･｡) 
        raise ValueError("Kaip? (pasirinkimo klaida)")