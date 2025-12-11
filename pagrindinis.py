import os
from InquirerPy import prompt,inquirer
from InquirerPy.validator import EmptyInputValidator, PathValidator
from src.ISBNSpausdinima import to_csv_file
from src.KnygosSuradimasPabalISBN import scanner
from src.ibibliotekaSusija import iBibliotekosPaieska,iBibliotekosPaieskaTiesiogiai
from src.barcodeKurimas import barcode_generator

# Joku komentaru del Anglu ir Lietuviu kalbos naudojimo. Nors tai nepagal visas taisykles, angla kalbiai neskaitys sio kodo

Klausimai = [
    "Brūkšninio kodo kūrimas",
    "Knygų rašymas į iBiblioteką pagal ISBN CSV",
    "Knygų rašymas į iBiblioteką pagal ISBN Scanner",
    "ISBN iš CSV į PDF",
    "Lėtesnė knygų paieška (Knygos_Su_Viskuom)",
    "Lėtesnė knygų paieška (Bibliotekos Knygos - VIsos knygos)",
    # "Suvedimas pagal pavadinima"
]

suformatuotiKlausimai = [
    {
        "type": "list",
        "name": "veiksmas",
        "message": "Pasirinkite, kokią funkciją norite atlikti:",
        "choices": Klausimai,
    }
]

klaidos="Nurodykite teisingą failo kelią"

def returningCorrectExtension(path,ending):
    path = str(path)

    if not path.endswith(ending):
        if "." in os.path.basename(path):  # only strip extension from filename
            path = path.rsplit(".", 1)[0]
        path += ending

    directory = os.path.dirname(path)
    if directory:  # avoids calling makedirs("") 
        os.makedirs(directory, exist_ok=True)

    return path

result = prompt(suformatuotiKlausimai)
pasirinkimoIndexas = Klausimai.index(result['veiksmas'])

match pasirinkimoIndexas:
    
    case 0: # Brūkšninio kodo kūrimas

        integer_val = inquirer.number(
            message="Kiek barkodu sukurti (Vienamia lapia telpa 50 kodu):",
            min_allowed=1,
            max_allowed=10*5*10,
            validate=EmptyInputValidator(),
        ).execute()

        home_path = os.path.join(os.getcwd(), "pdfs")

        dest_path = inquirer.filepath(
            message="Pasirinkite vietą ir pavadinimą būsimo failo:",
            default=os.path.abspath(os.path.join(home_path, "BarkodaiSpauzdinimui.pdf")),
        ).execute()

        barcode_generator(int(integer_val), dest_path)
    
    case 1: # Knygų rašymas į iBiblioteką pagal ISBN CSV

        home_path = os.path.join(os.getcwd(), "csv")
        
        src_path = inquirer.filepath(
            message="Pasirinkite is kurio failo bus imami duomenys:",
            default=os.path.join(home_path, "Knygos_Be_Barkodo.csv"),
            validate=PathValidator(is_file=False, is_dir=False, message=klaidos),
            only_files=True,
        ).execute()
                
        dest_path = inquirer.filepath(
            message="Pasirinkite i kurio faila bus idedami duomenys:",
            default=os.path.join(home_path, "Knygos_Su_Viskuom.csv"),
            transformer=lambda path: path + ".csv" if not path.endswith(".csv") else path,
            invalid_message=klaidos,
            validate=lambda path: not os.path.isdir(path),
        ).execute()
        
        empty_path = inquirer.filepath(
            message="Pasirinkite i kurio faila bus idedami duomenys kurie bus nerasti:",
            default=os.path.join(home_path, "Empty.csv"),
            transformer=lambda path: path + ".csv" if not path.endswith(".csv") else path,
            invalid_message=klaidos,
            validate=lambda path: not os.path.isdir(path),
        ).execute()
        
        returningCorrectExtension(dest_path,".csv")

        iBibliotekosPaieska(src_path, dest_path, empty_path, 'a')
        
    case 2: # Knygų rašymas į iBiblioteką pagal ISBN Scanner

        home_path = os.path.join(os.getcwd(), "csv")

        dest_path = inquirer.filepath(
            message="Pasirinkite i kurio faila bus idedami duomenys:",
            default=os.path.join(home_path, "Knygos_Su_Viskuom.csv"),
            transformer=lambda path: path + ".csv" if not path.endswith(".csv") else path,
            invalid_message=klaidos,
            validate=lambda path: not os.path.isdir(path),
        ).execute()

        returningCorrectExtension(dest_path,".csv")

        iBibliotekosPaieskaTiesiogiai(dest_path)   
        
    case 3: # ISBN iš CSV į PDF

        home_path = os.getcwd()

        src_path = inquirer.filepath(
            message="Pasirinkite is kurio failo bus imami duomenys:",
            default=os.path.join(home_path, "csv/Knygos_Be_Barkodo.csv"),
            validate=PathValidator(is_file=True, message="Nurodykite teisingą failo kelią"),
            only_files=True,
        ).execute()

        dest_path = inquirer.filepath(
            message="Pasirinkite vietą ir pavadinimą būsimo failo:",
            default=os.path.abspath(os.path.join(home_path, "pdfs/SpausdinimoLapas-ISBN.pdf")),
            transformer=lambda path: path + ".pdf" if not path.endswith(".pdf") else path,
            invalid_message="Nurodykite teisingą failo kelią",
            validate=lambda path: not os.path.isdir(path),
        ).execute()
        
        dest_path = returningCorrectExtension(dest_path, ".pdf")


        to_csv_file(src_path,dest_path)
        
    case 4: # Lėtesnė knygų paieška
        
        print("Paruosta Skanuoti")
        
        scanner("Knygos_Su_Viskuom.csv")
        
    case 5: # Lėtesnė knygų paieška
        
        print("Paruosta Skanuoti")
        
        scanner("Bibliotekos Knygos - VIsos knygos.csv")
        
    # case 6: # Suvedimas pagal pavadinima
        
    #     print("Parasykitia pavadinima, ir jei imanoma metus")
        
    #     surasimasPavadinimoIrMetu("Bibliotekos Knygos - VIsos knygos.csv")
        
    case _: # (｡･ˇ_ˇ･｡) 
        raise ValueError("Kaip? (pasirinkimo klaida)")
