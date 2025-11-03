import csv
from datetime import datetime

def barcode_generator(num:int, output_csv:str):
    if(num<0 or num>1000):
        print("Reikia kad sugeneruojami kodai butu maziau 100 ir daugiau 0")
        return
    
    fieldnames = ["isbn"]
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for index in range(num):
            writer.writerow({"isbn": "KVM" + datetime.today().strftime('%y%m%d') + str(index).zfill(3)})
        
        
    
# barcode_generator(10, "csv/BarKodai_Knygoms_Be_Barkodu.csv")