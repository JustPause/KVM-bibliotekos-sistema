import argparse
import os
import sys

from InquirerPy.prompts.filepath import FilePathPrompt
from InquirerPy.resolver import prompt
from InquirerPy.validator import PathValidator

from src.barcode_kurimas import barcode_generator
from src.book_finding_by_isbn import scanner
from src.ensure import Ensure
from src.gui.graphical_user_interface import run
from src.ibiblioteka_connection import (
    iBibliotekos_paieska,
    iBibliotekos_paieska_tiesiogiai,
)
from src.isbn_print import form_csv_to_pdf
from src.logger import logger
from src.os_helper import get_correct_extension, git_build_number


class MainClass:
    QUESTIONS = [
        "Brūkšninio kodo kūrimas",
        "Knygų rašymas į iBiblioteką pagal ISBN CSV",
        "Knygų rašymas į iBiblioteką pagal ISBN Scanner",
        "ISBN iš CSV į PDF",
        "Lėtesnė knygų paieška",
        # "Lėtesnė knygų paieška (Bibliotekos Knygos - VIsos knygos)",
        # "Suvedimas pagal pavadinima"
    ]

    ERRORTEXTFILE = "Nurodykite teisingą failo kelią"
    ERRORTEXTINCORECTUSE = (
        "Kai naudojamas -S/--webScraper, privaloma nurodyti -o/--output"
    )
    ERRORTEXTINCORECTUSEGENERATE = (
        "Kai naudojamas -G/--generate, privaloma nurodyti -o/--output"
    )
    ERRORTEXTINCORECTUSEISBN = "Kai naudojamas -I/--isbnPdf, privaloma nurodyti -o/--output ir privaloma nurodyti -i/--input"

    def __init__(self) -> None:
        """OKAY"""
        pass

    def _prompting(self):
        """A prompt formatter and handler for user selection"""
        QUESTIONS_FUNCTION = [
            {
                "type": "list",
                "name": "veiksmas",
                "message": "Pasirinkite, kokią funkciją norite atlikti:",
                "choices": self.QUESTIONS,
            }
        ]

        result = prompt(QUESTIONS_FUNCTION)
        chooce_index: int = self.QUESTIONS.index(str(result["veiksmas"]))

        match chooce_index:
            case 0:  # Brūkšninio kodo kūrimas
                from src.actions.main_action import (
                    get_dest_path,
                    get_number_of_barcodes,
                )

                number_of_barcodes = get_number_of_barcodes()

                dest_path = get_dest_path("pdfs", "BarkodaiSpauzdinimui.pdf")

                barcode_generator(int(number_of_barcodes), dest_path)

            case 1:  # Knygų rašymas į iBiblioteką pagal ISBN CSV
                from src.actions.main_action import get_dest_path, get_src_path

                src_path = get_src_path("csv", "Knygos_Be_Barkodo.csv")

                dest_path = get_dest_path("csv", "Knygos_Su_Viskuom.csv")

                dest_path = get_correct_extension(dest_path, ".csv")

                iBibliotekos_paieska(src_path, dest_path)

            case 2:  # Knygų rašymas į iBiblioteką pagal ISBN Scanner
                home_path = os.path.join(os.getcwd(), "csv")

                dest_path = self._run_prompt(
                    FilePathPrompt(
                        message="Pasirinkite i kurio faila bus idedami duomenys:",
                        default=os.path.join(home_path, "Knygos_Su_Viskuom.csv"),
                        transformer=Ensure.ensure_csv,
                        invalid_message=self.ERRORTEXTFILE,
                        validate=Ensure.ensure_not_dir,
                    )
                )

                dest_path = get_correct_extension(dest_path, ".csv")

                iBibliotekos_paieska_tiesiogiai(dest_path)

            case 3:  # ISBN iš CSV į PDF
                home_path = os.getcwd()

                src_path = self._run_prompt(
                    FilePathPrompt(
                        message="Pasirinkite is kurio failo bus imami duomenys:",
                        default=os.path.join(home_path, "csv/Knygos_Be_Barkodo.csv"),
                        validate=PathValidator(
                            is_file=True, message=self.ERRORTEXTFILE
                        ),
                        only_files=True,
                    )
                )

                dest_path = self._run_prompt(
                    FilePathPrompt(
                        message="Pasirinkite vietą ir pavadinimą būsimo failo:",
                        default=os.path.abspath(
                            os.path.join(home_path, "pdfs/SpausdinimoLapas-ISBN.pdf")
                        ),
                        transformer=Ensure.ensure_pdf,
                        invalid_message=self.ERRORTEXTFILE,
                        validate=Ensure.ensure_not_dir,
                    )
                )

                dest_path = get_correct_extension(dest_path, ".pdf")

                form_csv_to_pdf(src_path, dest_path)

            case 4:  # Lėtesnė knygų paieška
                logger.info("Paruosta Skanuoti - irasykytia ISBN")

                # scanner("csv/output_csv.csv")

            case _:  # (｡･ˇ_ˇ･｡)
                raise ValueError("Kaip? (pasirinkimo klaida)")

    def _adding_argumants(self, parser):
        ARGUMENTS = [
            ({"arguments": ["-h", "--help"]}, {"action": "store_true"}),
            ({"arguments": ["-v", "--version"]}, {"action": "store_true"}),
            ({"arguments": ["-S", "--webScraper"]}, {"action": "store_true"}),
            (
                {"arguments": ["-G", "--generate"]},
                {},
            ),
            ({"arguments": ["-I", "--isbnPdf"]}, {"action": "store_true"}),
            ({"arguments": ["-C", "--check"]}, {"action": "store_true"}),
            ({"arguments": ["-i", "--input"]}, {"help": "Input file path"}),
            ({"arguments": ["-o", "--output"]}, {"help": "Output file path"}),
            ({"arguments": ["--gui"]}, {"action": "store_true"}),
        ]

        group = parser.add_argument_group("Pasirinkimai")
        ReadMe = self._get_data_form_read_me()

        for arguments, action in ARGUMENTS:
            arguments_value = arguments["arguments"]
            action_value = action.get("action", None)
            arguments_str = ", ".join(arguments_value)

            group.add_argument(
                *arguments_value,
                action=action_value,
                help=ReadMe.get(arguments_str),
            )

    def _handels_args(self, parser, args):
        """Handles user selection and leads the user to the funcion that he selected made"""
        if args.help:
            parser.print_help()

        elif args.gui:
            self._local_run()

        elif args.version:
            import configparser

            build = git_build_number()
            config = configparser.ConfigParser()
            config.read("config.conf")
            version = config["DEFAULT"]["version"]

            logger.info(f"{version}+{build}")
        elif args.webScraper and not args.output:
            parser.error(self.ERRORTEXTINCORECTUSE)

        elif args.webScraper:
            src_path = args.input
            dest_path = args.output

            if args.input:
                iBibliotekos_paieska(src_path, dest_path)
            else:
                iBibliotekos_paieska_tiesiogiai(dest_path)

        elif args.generate and not args.output:
            parser.error(self.ERRORTEXTINCORECTUSEGENERATE)

        elif args.generate:
            dest_path = args.output
            dest_path = get_correct_extension(dest_path, ".pdf")
            barcode_generator(int(args.generate), dest_path)

        elif args.isbnPdf and not args.output and not args.input:
            parser.error(self.ERRORTEXTINCORECTUSEISBN)

        elif args.isbnPdf:
            src_path = args.input

            dest_path = args.output
            dest_path = get_correct_extension(dest_path, ".pdf")

            if args.input:
                form_csv_to_pdf(src_path, dest_path)

        elif args.check:
            dest_path = args.output
            scanner(dest_path)
            if args.output:
                scanner(dest_path)
            else:
                scanner()

        elif args.input:
            pass

    def main(self):
        """_main place where the app starts. _mainly used to detect if any arguments exist on execution and reacts accordingly"""

        argv = sys.argv[1:]
        argv_count = len(argv)

        if argv_count == 0:
            self._prompting()

        else:
            parser = argparse.ArgumentParser(
                prog="Barkodas",
                usage="Barkodas [pasirinkimas] [failas]",
                description="Bibliotekos knygų valdymo sistema. Programa jungiasi prie Google Sheets ir padeda vartotojams valdyti knygas.",
                add_help=False,
            )

            self._adding_argumants(parser)

            self._handels_args(parser, parser.parse_args())

    @staticmethod
    def _local_run():
        run()

    @staticmethod
    def _get_data_form_read_me():
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

        return options


if __name__ == "__main__":
    app = MainClass()
    app.main()
