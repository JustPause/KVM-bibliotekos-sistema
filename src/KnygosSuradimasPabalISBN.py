import re
import csv

while True:
    with open("csv/Knygos_Su_Viskuom.csv", 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        isbnCount=0
        PavadinimasCount=0
        isbn = input()
        for index, row in enumerate(rows):  
            if(row["isbn"]==isbn):
                print(row)