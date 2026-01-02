import os
import sys
from InquirerPy import prompt,inquirer
from InquirerPy.validator import EmptyInputValidator, PathValidator
from src.ibibliotekaConnection import iBibliotekos_paieska,iBibliotekos_paieska_tiesiogiai
from src.barcodeKurimas import barcode_generator
from src.ISBNPrint import to_csv_file
from src.bookFindingByISBN import scanner
import argparse

from src.gui.graphicalUserInterface import run

# Joku komentaru del Anglu ir Lietuviu kalbos naudojimo. Nors tai nepagal visas taisykles, angla kalbiai neskaitys sio kodo

class MainClass():

    KLAUSIMAI = [
        "Brūkšninio kodo kūrimas",
        "Knygų rašymas į iBiblioteką pagal ISBN CSV",
        "Knygų rašymas į iBiblioteką pagal ISBN Scanner",
        "ISBN iš CSV į PDF",
        "Lėtesnė knygų paieška",
        # "Lėtesnė knygų paieška (Bibliotekos Knygos - VIsos knygos)",
        # "Suvedimas pagal pavadinima"
    ]

    KLAUSIMU_FORMUOTE = [
        {
            "type": "list",
            "name": "veiksmas",
            "message": "Pasirinkite, kokią funkciją norite atlikti:",
            "choices": KLAUSIMAI,
        }
    ]

    klaidos="Nurodykite teisingą failo kelią"
    @staticmethod
    def get_correct_extension(path,ending):
        path = str(path)

        if not path.endswith(ending):
            if "." in os.path.basename(path):  # only strip extension from filename
                path = path.rsplit(".", 1)[0]
            path += ending

        directory = os.path.dirname(path)
        if directory:  # avoids calling makedirs("") 
            os.makedirs(directory, exist_ok=True)

        return path

    def prompting(self):
        result = prompt(self.KLAUSIMU_FORMUOTE)
        pasirinkimo_indexas = self.KLAUSIMAI.index(result['veiksmas'])

        match pasirinkimo_indexas:
            
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
                    validate=PathValidator(is_file=False, is_dir=False, message=self.klaidos),
                    only_files=True,
                ).execute()
                        
                dest_path = inquirer.filepath(
                    message="Pasirinkite i kurio faila bus idedami duomenys:",
                    default=os.path.join(home_path, "Knygos_Su_Viskuom.csv"),
                    transformer=lambda path: path + ".csv" if not path.endswith(".csv") else path,
                    invalid_message=self.klaidos,
                    validate=lambda path: not os.path.isdir(path),
                ).execute()
                
                dest_path=self.get_correct_extension(dest_path,".csv")

                iBibliotekos_paieska(src_path, dest_path)
                
            case 2: # Knygų rašymas į iBiblioteką pagal ISBN Scanner

                home_path = os.path.join(os.getcwd(), "csv")

                dest_path = inquirer.filepath(
                    message="Pasirinkite i kurio faila bus idedami duomenys:",
                    default=os.path.join(home_path, "Knygos_Su_Viskuom.csv"),
                    transformer=lambda path: path + ".csv" if not path.endswith(".csv") else path,
                    invalid_message=self.klaidos,
                    validate=lambda path: not os.path.isdir(path),
                ).execute()

                dest_path=self.get_correct_extension(dest_path,".csv")

                iBibliotekos_paieska_tiesiogiai(dest_path)   
                
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
                
                dest_path = self.get_correct_extension(dest_path, ".pdf")

                to_csv_file(src_path,dest_path)
                
            case 4: # Lėtesnė knygų paieška
                
                print("Paruosta Skanuoti - irasykytia ISBN")
                
                scanner("csv/output_csv.csv")
            
            case _: # (｡･ˇ_ˇ･｡) 
                raise ValueError("Kaip? (pasirinkimo klaida)")
    @staticmethod
    def local_run():
        run()
    
    def main(self):
        argv = sys.argv[1:]
        argv_count= len(argv)

        if(argv_count==0):
            self.prompting()

        else:
            parser = argparse.ArgumentParser(
                                prog='Barkodas',
                                description='A library book management system. The program connects to Google Sheets and helps users manage books.'
            )
            
            parser.add_argument('-v', '--version', action='store_true', help='Show program version')
            parser.add_argument('-S', '--webScraper', action='store_true', help='Enable web scraper')
            parser.add_argument('-G', '--generate', action='store_true', help='Generate data')
            parser.add_argument('-I', '--isbnPdf', action='store_true', help='Create PDF using ISBN')
            parser.add_argument('-C', '--check', action='store_true', help='Check book availability')
            parser.add_argument('-i', '--input', help='Input file')
            parser.add_argument('--gui', action='store_true', help='Launch graphical user interface')
            
            args = parser.parse_args()
            
            if args.gui:
                self.local_run()
            
            if args.version:
                print('version')
             
            elif args.webScraper:
                if args.output:
                    iBibliotekos_paieska(src_path, dest_path)
                else:
                    iBibliotekos_paieska_tiesiogiai(dest_path) 
                  
            elif args.generate:
                barcode_generator(int(integer_val), dest_path)
            
            elif args.isbnPdf:
                dest_path = self.get_correct_extension(dest_path, ".pdf")
                to_csv_file(src_path,dest_path)
            
            elif args.check:
                pass
            
            elif args.input:
                pass
                
            else:
                print("END")
            
if __name__ == "__main__":
    app = MainClass()      # create an instance
    app.main()   