import csv
import datetime
from src.ISBNNumerioISpausdinima import generate_KVM_barcode,dir_check
from src.helpers.PDF import images_to_pdf 

def barcode_generator(num:int, output_pdf:str):    
    fieldnames = ["isbn"]
    
    filenameArray=[] 

    dir_check("caches/BarCode/")

    for index in range(num):
        print(str(int((index / num) * 100)) + "%")
        
        filenameArray.append( generate_KVM_barcode("KVM" + datetime.datetime.today().strftime('%y%m%d') + str(index).zfill(3)))

    dir_check("pdfs/")

    images_to_pdf(filenameArray,"csv/SpauzdintiKVM.pdf")
        
        
    
# barcode_generator(10, "csv/Knygos_Su_Viskuom.csv")