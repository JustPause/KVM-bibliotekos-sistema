import csv
import datetime
import tempfile

from src.actions.barcode_action import (
    generate_Gs1_128_barcode,
    generate_isbn13_barcode,
    generate_KVM_barcode,
)
from src.etc.logger import logger
from src.helpers.pdf import images_to_pdf


def generator_barcodes(num: int, output_pdf: str) -> None:
    """
    Generates `number` of KVM barcodes and compiles them into a single PDF.

    Args:
        num (int): Number of barcodes to generate.
        output_pdf (str): Path to save the generated PDF.
    """

    with tempfile.TemporaryDirectory() as output_dir:
        filename_array = []

        for index in range(num):
            barcode_id = f"KVM{datetime.datetime.today():%y%m%d}{index:03d}"

            try:
                path = generate_KVM_barcode(barcode_id, output_dir)
                filename_array.append(path)

                progress = int(((index + 1) / num) * 100)
                logger.info(f"Progresas: {progress}% ({index + 1}/{num})")

            except Exception as e:
                logger.error(f"Error generating barcode {barcode_id}: {e}")

        images_to_pdf(filename_array, output_pdf)


def form_csv_to_pdf(input_csv: str, output_pdf: str) -> None:
    """
    Reads a CSV file, extracts values from the 'Atspauzdinti' column,
    and passes them to the 'imiges_to_pdf' function to generate a PDF.

    Args:
        input_csv (str): Path to the source CSV file.
        output_pdf (str): Path where the resulting PDF will be saved.
    """

    rows = []

    with open(input_csv, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows_list = list(reader)
        for row in rows_list:
            rows.append(row["Atspauzdinti"])

    imiges_to_pdf(output_pdf, rows)


def imiges_to_pdf(output_pdf: str, rows: list[str]) -> None:
    """
    Generates barcode images from a list of data values and compiles them
    into a single PDF file.

    Args:
        output_pdf (str): Path to save the generated PDF.
        rows (list[str]): List of data strings to encode as barcodes.
    """

    with tempfile.TemporaryDirectory() as output_dir:
        filename_array = []

        for row in rows:
            try:
                if len(row) != 13:
                    filename_array.append(generate_Gs1_128_barcode(row, output_dir))

                else:
                    filename_array.append(generate_isbn13_barcode(row, output_dir))

            except Exception as e:
                logger.error(f"Error generating barcode {row}: {e}")

        images_to_pdf(filename_array, output_pdf)
