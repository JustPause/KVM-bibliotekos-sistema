import os

import barcode
from barcode.writer import ImageWriter

from src.logger import logger


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
    isbn_barcode = barcode.get("isbn13", isbn, writer=ImageWriter())
    output_path = os.path.join(output_dir, str(isbn))
    saved_file = isbn_barcode.save(output_path, options=options)
    logger.debug(f"ISBN13 barcode saved at: {saved_file}")

    return saved_file


def generate_Gs1_128_barcode(isbn: str, output_dir: str) -> str:
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

    isbn_barcode = barcode.get("Gs1_128", isbn, writer=ImageWriter())
    output_path = os.path.join(output_dir, str(isbn))
    saved_file = isbn_barcode.save(output_path, options=options)
    logger.debug(f"GS1-128 barcode saved at: {saved_file}")

    return saved_file


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

    main_barcode = barcode.get("code128", isbn, writer=ImageWriter())
    return main_barcode.save(output + str(isbn), options)
