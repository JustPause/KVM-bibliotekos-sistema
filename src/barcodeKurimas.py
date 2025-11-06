import csv
import datetime
from src.ISBNNumerioISpausdinima import generate_KVM_barcode,dir_check
from src.helpers.PDF import images_to_pdf 

def barcode_generator(num:int, output_csv:str):
    if(num<0 or num>(10*5*10)):
        print("Reikia kad sugeneruojami kodai butu maziau 100 ir daugiau 0")
        return
    
    fieldnames = ["isbn"]
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        filenameArray=[] 

        dir_check("caches/BarCode/")

        for index in range(num):
            print(str(int((index / num) * 100)) + "%")
            filenameArray.append( generate_KVM_barcode("KVM" + datetime.datetime.today().strftime('%y%m%d') + str(index).zfill(3)))
            writer.writerow({"isbn": "KVM" + datetime.datetime.today().strftime('%y%m%d') + str(index).zfill(3)})

        dir_check("pdfs/")

        images_to_pdf(filenameArray,"SpauzdintiKVM")
        
        
    
# barcode_generator(10, "csv/Knygos_Su_Viskuom.csv")