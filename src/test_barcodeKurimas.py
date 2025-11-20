import os
import unittest
from src.barcodeKurimas import barcode_generator

class TestBarcodeGenerator(unittest.TestCase):
    def test_barcode_generator_zero(self):
        path = os.path.join(os.getcwd(), "pdfs","test","test_zero.pdf")
        barcode_generator(0,path)

    def test_barcode_generator_one(self):
        path = os.path.join(os.getcwd(), "pdfs","test","test_one.pdf")
        barcode_generator(1,path)
        
    def test_barcode_generator_hundred(self):
        path = os.path.join(os.getcwd(), "pdfs","test","test_hundred.pdf")
        barcode_generator(100,path)
        
    def test_barcode_generator_thousand(self):
        path = os.path.join(os.getcwd(), "pdfs","test","test_thousand.pdf")
        barcode_generator(1000,path)