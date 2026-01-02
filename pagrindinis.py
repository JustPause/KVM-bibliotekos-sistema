import os
import sys
from InquirerPy import prompt,inquirer
from InquirerPy.validator import EmptyInputValidator, PathValidator
from src.osHelper import git_build_number
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
                                usage="Barkodas [pasirinkimas] [failas]",
                                description='Bibliotekos knygų valdymo sistema. Programa jungiasi prie Google Sheets ir padeda vartotojams valdyti knygas.',
                                add_help=False,
            )
            group = parser.add_argument_group('Pasirinkimai') 
            
            ReadMe=self.getDataFormReadMe()
                    
            group.add_argument('-h', '--help', action='store_true', help=ReadMe.get('-h, --help'))
            group.add_argument('-v', '--version', action='store_true', help=ReadMe.get('-v, --version'))
            group.add_argument('-S', '--webScraper', action='store_true', help=ReadMe.get('-S, --webScraper'))
            group.add_argument('-G', '--generate', action='store_true', help=ReadMe.get('-G, --generate'))
            group.add_argument('-I', '--isbnPdf', action='store_true', help=ReadMe.get('-I, --isbnPdf'))
            group.add_argument('-C', '--check', action='store_true', help=ReadMe.get('-C, --check'))
            group.add_argument('-i', '--input', help=ReadMe.get('-i, --input'))
            group.add_argument('-o', '--output', help=ReadMe.get('-o, --output'))
            group.add_argument('--gui', action='store_true', help=ReadMe.get('--gui'))

            args = parser.parse_args()
            
            if args.help:
                parser.print_help()
            
            if args.gui:
                self.local_run()
            
            if args.version:
                import configparser
        
                build = git_build_number()
                config = configparser.ConfigParser()
                config.read("config.conf")
                version = config["DEFAULT"]["version"]
                
                print( f"{version}+{build}" )
            if args.webScraper and not args.output:
                parser.error("Kai naudojamas -S/--webScraper, privaloma nurodyti -o/--output")
            elif args.webScraper:
                src_path = args.input  # can be None
                dest_path = args.output
                
                if args.input:
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
            
    @staticmethod
    def getDataFormReadMe():
        import re
        
        table_lines = []
        in_table = False

        with open("README.md", encoding="utf-8") as f:
            for lines in f:
                if "Start_Helptable" in lines:
                    in_table = True
                    continue
                if "End_Helptable" in lines:
                    in_table = False
                    break
                if in_table:
                    table_lines.append(lines.rstrip())
                    
        table_lines = [line.strip() for line in table_lines if line.strip()] 
        options = {}

        for line in table_lines[2:]:
            parts = line.split("|")
            if len(parts) < 3:
                continue
            flag = parts[1].strip().strip("`")
            description = parts[2].strip()
            options[flag] = description

        # for flag, desc in options.items():
        #     print(flag, ":", desc)
        return options
            

if __name__ == "__main__":
    app = MainClass()      # create an instance
    app.main()   
    