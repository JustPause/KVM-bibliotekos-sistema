import csv
import os
import barcode

from reportlab.graphics.barcode import eanbc
from reportlab.lib.units import mm
from reportlab.graphics import renderPM
from reportlab.graphics.shapes import Drawing
from barcode.writer import ImageWriter
from src.helpers.PDF import images_to_pdf, print_labels_on_sheet

filepath ="caches/BarCode/"

def dir_check(filep):

    filepath = filep

    if not os.path.exists(filepath):
        os.makedirs(filepath)

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
        "module_width": 0.6,     
        "module_height": 20.0,    
        "font_size": 10,          
        "text_distance": 6.0,     
        "quiet_zone": 1,        
        "background": "white",    
        "foreground": "black",    
        "write_text": True,       
    }
    
    main_barcode = barcode.get("code128", isbn, writer=ImageWriter())
    
    filename = filepath + str(isbn)

    return main_barcode.save(filename, options)    

def generate_KVM_barcode(isbn):
    
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
    filename = filepath + str(isbn)
    return main_barcode.save(filename, options)   
    
def to_csv_file(BarcodesPath):
    with open(BarcodesPath, 'r', newline='', encoding='utf-8') as f:
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
        
        images_to_pdf(filenameArray, "SpauzdinimoLapas-ISBN") 
       
# to_csv_file("csv/Knygos_Su_Viskuom.csv")