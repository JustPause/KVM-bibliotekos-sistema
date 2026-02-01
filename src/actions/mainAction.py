import os
import sys
from functools import partial

from InquirerPy.prompts.filepath import FilePathPrompt
from InquirerPy.prompts.number import NumberPrompt
from InquirerPy.validator import EmptyInputValidator, PathValidator

from src.ensure import Ensure


def get_number_of_barcodes():
    number_of_barcodes = _run_prompt(
        NumberPrompt(
            message="Kiek barkodu sukurti (Vienamia lapia telpa 50 kodu):",
            min_allowed=1,
            max_allowed=10 * 5 * 10,
            validate=EmptyInputValidator(),
        )
    )
    return number_of_barcodes


def get_dest_path(ext: str, default: str):
    home_path = os.path.join(os.getcwd(), ext)
    transformer = partial(Ensure.ensure_extension, ext=ext)
    dest_path = _run_prompt(
        FilePathPrompt(
            message="Pasirinkite vietą ir pavadinimą būsimo failo:",
            default=os.path.abspath(os.path.join(home_path, default)),
            transformer=transformer,
            invalid_message="Nurodykite teisingą failo kelią",
            validate=Ensure.ensure_not_dir,
        )
    )

    if not dest_path.endswith(ext):
        if "." in os.path.basename(dest_path):
            dest_path = dest_path.rsplit(".", 1)[0]
        dest_path += ext

    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    return dest_path


def get_src_path(ext: str, src: str):
    home_path = os.path.join(os.getcwd(), ext)
    src_path = _run_prompt(
        FilePathPrompt(
            message="Pasirinkite is kurio failo bus imami duomenys:",
            default=os.path.join(home_path, "Knygos_Be_Barkodo.csv"),
            validate=PathValidator(
                is_file=False, is_dir=False, message="Nurodykite teisingą failo kelią"
            ),
            only_files=True,
        )
    )
    return src_path


def _run_prompt(prompt):
    """Specifically for the prompt library, to handle CTRL+C presses"""

    try:
        return prompt.execute()
    except KeyboardInterrupt:
        print("\nIšeinama…")
        sys.exit(0)
