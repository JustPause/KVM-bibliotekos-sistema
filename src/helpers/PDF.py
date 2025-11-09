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
    
def print_labels_on_sheet(image_files, output_pdf="labels_on_APLI_paper"):
    output_pdf = "pdfs/" + output_pdf + ".pdf"
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    cols = 5
    label_width_mm = 38.0
    label_height_mm = 21.2

    left_margin_mm = 5.0     
    top_margin_mm = 13.0     
    h_spacing_mm = 2.0       
    v_spacing_mm = 0.0       

    label_width = label_width_mm * mm
    label_height = label_height_mm * mm
    left_margin = left_margin_mm * mm
    top_margin = top_margin_mm * mm
    h_spacing = h_spacing_mm * mm
    v_spacing = v_spacing_mm * mm

    col_counter = 0
    x = left_margin
    y = height - top_margin - label_height

    for img_file in image_files:
        c.drawImage(
            img_file,
            x,
            y,
            width=label_width,
            height=label_height,
            preserveAspectRatio=True,
            anchor='c'
        )

        col_counter += 1
        x += label_width + h_spacing

        if col_counter >= cols:
            col_counter = 0
            x = left_margin
            y -= (label_height + v_spacing)

            if y < 0:
                c.showPage()
                y = height - top_margin - label_height

    c.save()