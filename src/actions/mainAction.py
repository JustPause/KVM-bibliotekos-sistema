import os
import sys

from InquirerPy.prompts.filepath import FilePathPrompt
from InquirerPy.prompts.number import NumberPrompt
from InquirerPy.validator import EmptyInputValidator


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


def get_dest_path(etc: str, default: str):
    home_path = os.path.join(os.getcwd(), etc)
    dest_path = _run_prompt(
        FilePathPrompt(
            message="Pasirinkite vietą ir pavadinimą būsimo failo:",
            default=os.path.abspath(os.path.join(home_path, default)),
        )
    )
    return dest_path


def _run_prompt(self, prompt):
    """Specifically for the prompt library, to handle CTRL+C presses"""

    try:
        return prompt.execute()
    except KeyboardInterrupt:
        print("\nIšeinama…")
        sys.exit(0)
