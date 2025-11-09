from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def images_to_pdf(image_files, output_pdf="pdfs/SpauzdinimoLapas.pdf"):

    canvasC = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    cols = 5
    spacing_mm = 2
    barcode_width_mm = ((width * 25.4 / 72)/cols) - (spacing_mm * 2)
    barcode_height_mm = 24
    spacing = 3 * mm
    col_counter = 0

    x_margin = (spacing_mm+3) * mm
    y_margin = spacing_mm * mm
    barcode_width = barcode_width_mm * mm
    barcode_height = barcode_height_mm * mm

    x = x_margin
    y = height - y_margin - barcode_height

    for img_file in image_files:
        canvasC.drawImage(img_file, x, y, width=barcode_width, height=barcode_height)

        col_counter += 1
        x += barcode_width + spacing

        if col_counter >= cols:
            col_counter = 0
            x = x_margin
            y -= (barcode_height + spacing)
            
            if y < y_margin:
                canvasC.showPage()
                y = height - y_margin - barcode_height

    canvasC.save()