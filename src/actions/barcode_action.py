import os

import barcode
from barcode.writer import ImageWriter

from src.etc.logger import logger


def generate_isbn13_barcode(isbn: str, output_dir: str) -> str:
    """
    Generates an ISBN-13 barcode image and saves it to the specified directory.

    Args:
        isbn (str): The ISBN-13 code to encode.
        output_dir (str): Path to the directory where the image will be saved.

    Returns:
        str: Full path to the saved barcode image file.
    """

    options = {
        "module_width": 0.3,
        "module_height": 12.0,
        "font_size": 10,
        "text_distance": 6.0,
        "quiet_zone": 2,
    }

    return _generate_barcode("isbn13", isbn, output_dir, options)


def generate_gs1_128_barcode(isbn: str, output_dir: str) -> str:
    """
    Generates an GS1-128 barcode image and saves it to the specified directory.

    Args:
        isbn (str): The GS1-128 code to encode.
        output_dir (str): Path to the directory where the image will be saved.

    Returns:
        str: Full path to the saved barcode image file.
    """

    options = {
        "module_width": 0.3,
        "module_height": 15.0,
        "font_size": 10,
        "text_distance": 6.0,
        "quiet_zone": 2,
    }

    return _generate_barcode("Gs1_128", isbn, output_dir, options)


def generate_KVM_barcode(isbn, output):
    """
    Generate a Code128 barcode image for a given ISBN and save it to a directory.

    Args:
        isbn (str): The identifier to encode in the barcode.
        output_dir (str): Path to the directory where the image will be saved.

    Returns:
        str: The full path to the saved barcode image file.
    """

    options = {
        "module_width": 0.35,
        "module_height": 20.0,
        "font_size": 10,
        "text_distance": 6.0,
        "quiet_zone": 1,
        "background": "white",
        "foreground": "black",
        "write_text": True,
    }

    return _generate_barcode("code128", isbn, output, options)


def _generate_barcode(
    barcode_type: str,
    isbn: str,
    output_dir: str,
    options: dict[str, int | float | str | bool],
) -> str:
    """Generic barcode generator."""
    barcode_obj = barcode.get(barcode_type, isbn, writer=ImageWriter())
    output_path = os.path.join(output_dir, str(isbn))
    saved_file = barcode_obj.save(output_path, options=options)
    logger.debug(f"{barcode_type} barcode saved at: {saved_file}")
    return saved_file
