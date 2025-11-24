import datetime
from src.osHelper import ArYraDirectorija
from src.ISBNSpausdinima import generate_KVM_barcode
from src.helpers.PDF import images_to_pdf 

def barcode_generator(num:int, output_pdf:str):    
    filenameArray=[] 
    caches = "caches/BarCode/"

    ArYraDirectorija(caches)
    ArYraDirectorija(output_pdf)

    for index in range(num):
        print(str(int((index / num) * 100)) + "%")
        
        filenameArray.append( 
            generate_KVM_barcode(
                "KVM" +
                datetime.datetime.today().strftime('%y%m%d') +
                str(index).zfill(3),caches
            )
        )
    
    images_to_pdf(filenameArray,output_pdf)

# barcode_generator(10, "csv/Knygos_Su_Viskuom.csv")