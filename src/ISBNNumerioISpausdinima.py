import csv
import os
import barcode
import treepoem

from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
from src.helpers.PDF import images_to_pdf

filepath ="caches/BarCode/"

def dir_check(filep):

    filepath = filep

    if not os.path.exists(filepath):
        os.makedirs(filepath)



def generate_13_barcode(isbn):
    WRITER_OPTIONS = {
    'module_width': 0.3,   
    'module_height': 12.0,  
    'font_size': 10,        
    'text_distance': 6.0,   
    'quiet_zone': 2,     
}
    isbn_barcode = barcode.get('isbn13', isbn, writer=ImageWriter())

    filename = filepath + str(isbn)
    filename = isbn_barcode.save(filename,options=WRITER_OPTIONS)
    
    return filename
    
def generate_10_barcode(isbn):
    WRITER_OPTIONS = {
    'module_width': 0.3,   
    'module_height': 15.0,  
    'font_size': 10,        
    'text_distance': 6.0,   
    'quiet_zone': 2,     
}
    isbn_barcode = barcode.get('Gs1_128', isbn, writer=ImageWriter())

    filename = filepath + str(isbn)
    filename = isbn_barcode.save(filename,options=WRITER_OPTIONS)

    return filename

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
    
def to_csv_file(input_csv, output_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        filenameArray=[] 
        for index, row in enumerate(rows):
            isbn_corect = row['Atspauzdinti']
            
            # print(int(isbn_corect) / 10000000000 )
            if len(isbn_corect)!=13:
                filenameArray.append( generate_10_barcode(isbn_corect) )
                print("10_barcode")
            
            else:
                filenameArray.append( generate_13_barcode(isbn_corect) )
                print("13_barcode")
        
        images_to_pdf(filenameArray, output_csv) 
       
# to_csv_file("csv/Knygos_Su_Viskuom.csv")