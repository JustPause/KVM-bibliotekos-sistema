import sys
import os

if sys.platform.startswith("win"):
    add_data = ".\\src\\gui\\img\\Vector.png;src/gui/img"
else:
    add_data = "./src/gui/img/Vector.png:src/gui/img"

os.system(f'pyinstaller --onefile --icon=./src/gui/img/barcode_scanner_4249.ico --add-data "{add_data}" --clean pagrindinis_gui.py')
