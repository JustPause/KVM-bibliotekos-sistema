import re
import csv

def scanner(file):
    while True:
        with open(f"csv/{file}", 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            isbn = input()
            for index, row in enumerate(rows):  
                if (row.get("isbn") == isbn or row.get("Kodas") == isbn):
                    print(row["Pavadinimas"] + " " +row.get("Komentarai"))