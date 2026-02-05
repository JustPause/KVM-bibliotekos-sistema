import datetime
import tempfile

from src.helpers.pdf import images_to_pdf
from src.isbn_print import generate_KVM_barcode
from src.logger import logger


def barcode_generator(num: int, output_pdf: str):
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
