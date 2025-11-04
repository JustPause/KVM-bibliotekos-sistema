import csv
from datetime import datetime
from ISBN_generator import generate_KVM_barcode
from PDF import images_to_pdf 

def barcode_generator(num:int, output_csv:str):
    if(num<0 or num>1000):
        print("Reikia kad sugeneruojami kodai butu maziau 100 ir daugiau 0")
        return
    
    fieldnames = ["isbn"]
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        filenameArray=[] 
        for index in range(num):
            filenameArray.append( generate_KVM_barcode("KVM" + datetime.today().strftime('%y%m%d') + str(index).zfill(3)))
            writer.writerow({"isbn": "KVM" + datetime.today().strftime('%y%m%d') + str(index).zfill(3)})
            
        images_to_pdf(filenameArray,"SpauzdintiKVM")
        
        
    
barcode_generator(10, "csv/BarKodai_Knygoms_Be_Barkodu.csv")