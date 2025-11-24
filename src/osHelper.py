import os

def ArYraDirectorija(output_pdf):
    if not os.path.exists(output_pdf):
        folder = os.path.dirname(output_pdf)
        os.makedirs(folder, exist_ok = True)