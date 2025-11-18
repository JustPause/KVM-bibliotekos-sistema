import csv

def scanner(file):
    fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]
    while True:
        with open(f"csv/{file}", 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            isbn = input()
            found=True
            for index, row in enumerate(rows):  
                if (row.get("isbn") == isbn or row.get("Kodas") == isbn):
                    print(row["Pavadinimas"])
                    found = False
                    
            if found:
                print("save to output_csv.csv as emtey - "+ str(isbn))
                with open("csv/output_csv.csv", 'a', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames = fieldnames, extrasaction='ignore')
                    writer.writerow({
                        "Autorius": "",
                        "Pavadinimas": "",
                        "Metai": "",
                        "isbn": isbn
                    })