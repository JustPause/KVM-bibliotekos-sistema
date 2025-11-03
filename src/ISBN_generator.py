import csv
from reportlab.graphics.barcode import eanbc
from barcode import EAN13
from reportlab.lib.units import mm
from reportlab.graphics import renderPM
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Group
from reportlab.lib.pagesizes import A4
import barcode
from barcode.writer import ImageWriter

filepath = "caches/BarCode/"

def generate_13_barcode(isbn):
    main_barcode = eanbc.Ean13BarcodeWidget(isbn)
    
    main_barcode.barHeight = 20 * mm 
    main_barcode.humanReadable = True 
    
    filename=filepath+ str(isbn) +".png"
    
    drawing = Drawing(35 * mm, 20 * mm)
    drawing.add(main_barcode, name="isbn")

    renderPM.drawToFile(drawing, filename, fmt="PNG",dpi=600)
    
    return filename
    
def generate_10_barcode(isbn):
    
    options = {
        "module_width": 0.4,     
        "module_height": 20.0,    
        "font_size": 12,          
        "text_distance": 6.0,     
        "quiet_zone": 6.5,        
        "background": "white",    
        "foreground": "black",    
        "write_text": True,       
    }
    
    main_barcode = barcode.get("code128", isbn, writer=ImageWriter())

    filename = filepath + str(isbn)

    return main_barcode.save(filename, options)    
    
    
def images_to_pdf(image_files):
    output_pdf="pdfs/SpauzdinimoLapas_ISBN.pdf"
    canvasC = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    cols = 5
    spacing_mm = 2
    barcode_width_mm = ((width * 25.4 / 72)/cols)-(spacing_mm*2)
    barcode_height_mm = 24
    spacing = 3 * mm
    col_counter = 0

    x_margin = spacing_mm * mm
    y_margin = spacing_mm * mm
    barcode_width = barcode_width_mm * mm
    barcode_height = barcode_height_mm * mm
    x = x_margin
    y = height - y_margin

    for img_file in image_files:
        canvasC.drawImage(img_file, x, y, width=barcode_width, height=barcode_height)

        col_counter =col_counter+ 1
        x += barcode_width + spacing

        if col_counter >= cols:
            col_counter = 0
            x = x_margin
            y -= (barcode_height + spacing)
            
            if y < y_margin:
                canvasC.showPage()
                y = height - y_margin - barcode_height
    canvasC.save()
    
with open('csv/Barcodes.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    
    filenameArray=[] 
    for index, row in enumerate(rows):
        isbn_corect = row['isbn']
        
        if len(isbn_corect)!=13:
           filenameArray.append( generate_10_barcode(isbn_corect) )
           print("10_barcode")
           
        else:
           filenameArray.append( generate_13_barcode(isbn_corect) )
           print("13_barcode")
    
    images_to_pdf(filenameArray) 
    