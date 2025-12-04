import os
import tempfile
import unittest
from src.barcodeKurimas import barcode_generator

class TestBarcodeGenerator(unittest.TestCase):
    def test_barcode_generator_zero(self):
        path = os.path.join(os.getcwd(),self.output_dir,"test_zero.pdf")
        barcode_generator(0,path)

    def test_barcode_generator_one(self):
        path = os.path.join(os.getcwd(),self.output_dir,"test_one.pdf")
        barcode_generator(1,path)
        
    def test_barcode_generator_hundred(self):
        path = os.path.join(os.getcwd(),self.output_dir,"test_hundred.pdf")
        barcode_generator(100,path)
    
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.output_dir = self.tmpdir.name 
    
    def tearDown(self):
        self.tmpdir.cleanup() 