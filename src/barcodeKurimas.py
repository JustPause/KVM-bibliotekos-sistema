import datetime
from src.osHelper import is_it_directory
from src.ISBNPrint import generate_KVM_barcode
from src.helpers.PDF import images_to_pdf 

def barcode_generator(num:int, output_pdf:str):    
    filename_array=[] 
    caches = "caches/BarCode/"

    is_it_directory(caches)
    is_it_directory(output_pdf)

    for index in range(num):
        print(str(int((index / num) * 100)) + "%")
        
        filename_array.append( 
            generate_KVM_barcode(
                "KVM" +
                datetime.datetime.today().strftime('%y%m%d') +
                str(index).zfill(3),caches
            )
        )
    
    images_to_pdf(filename_array,output_pdf)