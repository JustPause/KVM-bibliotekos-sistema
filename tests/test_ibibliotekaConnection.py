import csv
import tempfile
import unittest

from src.ibibliotekaConnection import iBiblioteka_scraper, iBibliotekos_paieska, kill_drive

isbn_array=[
    ["995543578x"], ["998614359x"], ["998659703x"], ["KVM251027025"], ["5790007279"], ["5899425733"], ["5899500190"], ["7986879477"], ["9886140013"], ["9955061030"], ["9955082461"], ["9955088699"], ["9786094253515"]
]
ats_array =[
    {'Autorius': 'Ziedonis, Imants (1933–2013)', 'Pavadinimas': 'Spalvotosios pasakos', 'Metai': '2006', 'isbn': '995543578x'},
    {'Autorius': '---', 'Pavadinimas': '---', 'Metai': '---', 'isbn': '998614359x'},
    {'Autorius': 'Pietaris, Vincas (1850–1902)', 'Pavadinimas': 'Lapės gyvenimas ir mirtis', 'Metai': '1996', 'isbn': '998659703x'},
    {'Autorius': '---', 'Pavadinimas': '---', 'Metai': '---', 'isbn': 'KVM251027025'},
    {'Autorius': 'Hauff, Wilhelm (1802–1827)', 'Pavadinimas': 'Pasakos', 'Metai': '1993', 'isbn': '5790007279'},
    {'Autorius': '', 'Pavadinimas': 'Saliamono žiedas', 'Metai': '1991', 'isbn': '5899425733'},
    {'Autorius': '', 'Pavadinimas': 'Žemė ir jos gėrybės', 'Metai': '1992', 'isbn': '5899500190'},
    {'Autorius': '---', 'Pavadinimas': '---', 'Metai': '---', 'isbn': '7986879477'},
    {'Autorius': '---', 'Pavadinimas': '---', 'Metai': '---', 'isbn': '9886140013'},
    {'Autorius': '', 'Pavadinimas': 'Vilkas ir septyni ožiukai ir kitos pasakos', 'Metai': '2003', 'isbn': '9955061030'},
    {'Autorius': 'Zanini, Giuseppe', 'Pavadinimas': 'Istorija', 'Metai': '2003', 'isbn': '9955082461'},
    {'Autorius': 'Knister', 'Pavadinimas': 'Ragana Lilė tampa sekle', 'Metai': '2005', 'isbn': '9955088699'},
    {'Pavadinimas': 'Mėnraštis „Aušra“', 'Metai': '2023', 'Autorius': '', 'isbn': '9786094253515'}
]
class TestIbibliotekaSusija(unittest.TestCase):
    def test_iBiblioteka_scraper(self):
        data=iBiblioteka_scraper(9786094875786)
        kill_drive()
        
        self.assertEqual(data.get("Pavadinimas"),"Papasakok apie gražų mūsų gyvenimą")
        self.assertEqual(data.get("Autorius"),"Sikorskienė, Vaiva")
        self.assertEqual(data.get("Metai"),"2025")
        self.assertEqual(data.get("isbn"),9786094875786)
        
    def test_IBibliotekosPaieska(self):
        self.tmpInput = tempfile.NamedTemporaryFile(delete=False).name
        self.tmpOutput = tempfile.NamedTemporaryFile(delete=False).name
        self.tmpEmpty = tempfile.NamedTemporaryFile(delete=False).name
        
        with open(self.tmpInput, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["isbn"])
            writer.writerows(isbn_array)

        iBibliotekos_paieska(self.tmpInput, self.tmpOutput)
        
        with open(self.tmpOutput, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            for index,row in enumerate(rows):
                self.assertEqual(row.get('Autorius'), ats_array[index].get('Autorius'))
                self.assertEqual(row.get('Pavadinimas'), ats_array[index].get('Pavadinimas'))
                self.assertEqual(row.get('Metai'), ats_array[index].get('Metai'))
                self.assertEqual(row.get('isbn'), ats_array[index].get('isbn'))
                
    def test_PalyginimasSuPagrindineLentelia(self):
        # TO if no table exists

        # if dublicat exists

        # if evrtihin is okay
        pass