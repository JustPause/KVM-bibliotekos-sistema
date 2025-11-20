import csv
import datetime
import os
from src.ISBNNumerioISpausdinima import generate_KVM_barcode
from src.helpers.PDF import images_to_pdf 

def barcode_generator(num:int, output_pdf:str):    
    fieldnames = ["isbn"]
    
    filenameArray=[] 

    if not os.path.exists("caches/BarCode/"):
        os.makedirs("caches/BarCode/")

    for index in range(num):
        print(str(int((index / num) * 100)) + "%")
        
        filenameArray.append( generate_KVM_barcode("KVM" + datetime.datetime.today().strftime('%y%m%d') + str(index).zfill(3)))
    
    if not os.path.exists(output_pdf):
        folder = os.path.dirname(output_pdf)
        os.makedirs(folder, exist_ok = True)

    images_to_pdf(filenameArray,output_pdf)

# barcode_generator(10, "csv/Knygos_Su_Viskuom.csv")