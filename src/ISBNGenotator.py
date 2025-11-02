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

# import time
# import barcode
# from barcode.writer import ImageWriter

# def download_isbn_barcode(isbn, output_filename):    
#     isbn_barcode = barcode.get('isbn13', isbn, writer=ImageWriter())

#     # Custom style settings

#     isbn_barcode.save("BarCode/"+output_filename)

filenameArray=[]    

def generate_13_barcode(isbn):
    # --- Create main EAN-13 barcode ---
    main_barcode = eanbc.Ean13BarcodeWidget(isbn)
    
    main_barcode.barHeight = 20 * mm 
    main_barcode.humanReadable = True 
    
    filename="BarCode/"+ str(isbn) +".png"
    
    # --- Create drawing canvas ---
    drawing = Drawing(35 * mm, 20 * mm)
    drawing.add(main_barcode, name="isbn")

    renderPM.drawToFile(drawing, filename, fmt="PNG",dpi=600)
    filenameArray.append(filename)
    
def generate_10_barcode(isbn):
    
    options = {
        "module_width": 0.4,      # Width of each barcode module
        "module_height": 20.0,    # Height of the barcode bars
        "font_size": 12,          # Size of human-readable text
        "text_distance": 6.0,     # Space between the barcode and the text
        "quiet_zone": 6.5,        # Blank space on either side of barcode
        "background": "white",    # Background color
        "foreground": "black",    # Bar color
        "write_text": True,       # Whether to print text under the barcode
    }
    # --- Create the Code128 barcode object ---
    main_barcode = barcode.get("code128", isbn, writer=ImageWriter())

    filename = "BarCode/" + str(isbn)

    # --- Save the barcode image ---
    filename=main_barcode.save(filename, options)    
    filenameArray.append(filename)
    
    
def images_to_pdf(image_files):
    output_pdf="BarCode/combined.pdf"
    canvasC = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    cols=5
    spacing_mm=2
    barcode_width_mm=((width * 25.4 / 72)/cols)-(spacing_mm*2)
    barcode_height_mm=26

    x_margin = spacing_mm * mm
    y_margin = spacing_mm * mm
    barcode_width = barcode_width_mm * mm
    barcode_height = barcode_height_mm * mm
    x = x_margin
    y = height - y_margin

    max_height = 30 * mm  # approximate barcode height
    spacing = 5 * mm      # space between barcodes
    
    col_counter=0

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
    
with open('Barcodes.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    
    for index, row in enumerate(rows):
        isbn_corect = row['ISBN']
        
        if len(isbn_corect)!=13:
            generate_10_barcode(isbn_corect)
           
        else:
            generate_13_barcode(isbn_corect)
        # isbn_corect=textwrap.wrap(isbn_corect, 12)[0]
        # suma=0
        # for i in range(0, len(isbn_corect)):
        #     if(i%2):
        #         suma=suma+int(isbn_corect[i])*3
        #     else:
        #         suma=suma+int(isbn_corect[i])*1
        # check=suma%10
         
        # isbn = isbn_corect
        # generate_bookland_barcode(isbn)
    
    images_to_pdf(filenameArray) 
    