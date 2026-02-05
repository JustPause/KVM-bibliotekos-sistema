import os
import tempfile
import unittest
from typing import override

from src.barcode_generator import generator_barcodes
from src.logger import logger


class TestBarcodeGenerator(unittest.TestCase):
    def __init__(self):
        super().__init__()

        self.tmpdir = None
        self.output_dir = ""

    def test_barcode_generator_zero(self):
        path = os.path.join(os.getcwd(), self.output_dir, "test_zero.pdf")
        generator_barcodes(0, path)

    def test_barcode_generator_one(self):
        path = os.path.join(os.getcwd(), self.output_dir, "test_one.pdf")
        generator_barcodes(1, path)

    def test_barcode_generator_hundred(self):
        path = os.path.join(os.getcwd(), self.output_dir, "test_hundred.pdf")
        generator_barcodes(100, path)

    @override
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.output_dir = self.tmpdir.name

    @override
    def tearDown(self):
        if self.tmpdir is not None:
            self.tmpdir.cleanup()

        else:
            logger.info("tmpdir yra None")
