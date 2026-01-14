import csv

import barcode
from barcode.writer import ImageWriter

from src.helpers.PDF import images_to_pdf
from src.osHelper import is_it_directory


def generate_13_barcode(isbn, output):
    options = {
        "module_width": 0.3,
        "module_height": 12.0,
        "font_size": 10,
        "text_distance": 6.0,
        "quiet_zone": 2,
    }
    isbn_barcode = barcode.get("isbn13", isbn, writer=ImageWriter())

    filename = output + str(isbn)
    filename = isbn_barcode.save(filename, options=options)

    return filename


def generate_10_barcode(isbn, output):
    options = {
        "module_width": 0.3,
        "module_height": 15.0,
        "font_size": 10,
        "text_distance": 6.0,
        "quiet_zone": 2,
    }

    isbn_barcode = barcode.get("Gs1_128", isbn, writer=ImageWriter())

    filename = output + str(isbn)
    filename = isbn_barcode.save(filename, options=options)

    return filename


def generate_KVM_barcode(isbn, output):
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


def form_csv_to_pdf(input_csv, output_csv):
    rows = []

    with open(input_csv, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows_list = list(reader)
        for row in rows_list:
            rows.append(row["Atspauzdinti"])

    imiges_to_pdf_hart(output_csv, rows)


def form_buffer_to_pdf(buffer_list, output_csv):
    imiges_to_pdf_hart(output_csv, buffer_list)


def imiges_to_pdf_hart(output_csv, rows: list[str]):
    filenameArray = []

    for row in rows:
        caches = "caches/BarCode/"
        is_it_directory(caches)

        if len(row) != 13:
            filenameArray.append(generate_10_barcode(row, caches))

        else:
            filenameArray.append(generate_13_barcode(row, caches))

    images_to_pdf(filenameArray, output_csv)
