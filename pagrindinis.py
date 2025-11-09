import os
from InquirerPy import prompt,inquirer
from InquirerPy.validator import EmptyInputValidator, PathValidator
from src.ISBNNumerioISpausdinima import to_csv_file
from src.KnygosSuradimasPabalISBN import scanner
from src.ibibliotekaWebScraper import SurasytiPoVienaEilute
from src.barcodeKurimas import barcode_generator

# Joku komentaru del Anglu ir Lietuviu kalbos naudojimo. Nors tai nepagal visas taisykles, angla kalbiai neskaitys sio kodo

Klausimai = [
    "Brūkšninio kodo kūrimas",
    "Knygų rašymas į iBiblioteką pagal ISBN",
    "ISBN iš CSV į PDF",
    "Lėtesnė knygų paieška (Knygos_Su_Viskuom)",
    "Lėtesnė knygų paieška (Bibliotekos Knygos - VIsos knygos)"
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
            validate=PathValidator(is_file=False, is_dir=False, message="Nurodykite teisingą failo kelią"),
            only_files=True,
        ).execute()

        barcode_generator(int(integer_val), src_path)
    case 1: # Knygų rašymas į iBiblioteką pagal ISBN

        home_path = os.path.join(os.getcwd(), "csv")

        src_path = inquirer.filepath(
            message="Pasirinkite is kurio failo bus imami duomenys:",
            default=os.path.join(home_path, "Knygos_Be_Barkodo.csv"),
            validate=PathValidator(is_file=False, is_dir=False, message="Nurodykite teisingą failo kelią"),
            only_files=True,
        ).execute()
  
        dest_path = inquirer.filepath(
            message="Pasirinkite i kurio faila bus idedami duomenys:",
            default=os.path.join(home_path, "Knygos_Su_Viskuom.csv"),
            validate=PathValidator(is_file=False, is_dir=False, message="Nurodykite teisingą failo kelią"),
            only_files=True,
        ).execute()

        SurasytiPoVienaEilute(src_path,dest_path)
        
    case 2: # ISBN iš CSV į PDF

        home_path = os.path.join(os.getcwd(), "csv")

        src_path = inquirer.filepath(
            message="Pasirinkite is kurio failo bus imami duomenys:",
            default=os.path.join(home_path, "Knygos_Be_Barkodo.csv"),
            validate=PathValidator(is_file=False, is_dir=False, message="Nurodykite teisingą failo kelią"),
            only_files=True,
        ).execute()
  
        dest_path = inquirer.filepath(
            message="Pasirinkite vietą ir pavadinimą būsimo failo:",
            default=os.path.abspath(os.path.join(home_path, "../pdfs/SpausdinimoLapas-ISBN.pdf")),
        ).execute()

        to_csv_file(src_path,dest_path)
        
    case 3: # Lėtesnė knygų paieška
        print("Paruosta Skanuoti")
        
        scanner("Knygos_Su_Viskuom.csv")
        
    case 4: # Lėtesnė knygų paieška
        print("Paruosta Skanuoti")
        
        scanner("Bibliotekos Knygos - VIsos knygos.csv")
        
    case _: # (｡･ˇ_ˇ･｡) 
        raise ValueError("Kaip? (pasirinkimo klaida)")