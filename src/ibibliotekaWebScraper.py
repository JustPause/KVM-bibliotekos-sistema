from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import csv

driver=None

def iBibliotekaScraper(isbn): 
    global driver
    options = Options()
    
    if(driver==None):
        print("Bandoma susijukti su iBiblioteka")
        
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get("https://ibiblioteka.lt/metis/publication")
        
        print("Susijukta su iBiblioteka")
        
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "mat-input-0"))
        )
        
        WebDriverWait(driver, 30).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
        )
        
        print("Spinner init gone ")
    
    print("Kodas kurio ieskau - " + str(isbn))

    search_box = driver.find_element(By.ID, "mat-input-0")
    search_box.clear()             
    search_box.send_keys(str(isbn))
    search_button = driver.find_element(By.CLASS_NAME,"c-btn--cta")
    search_button.click()
    
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
    )
    
    print("Spinner search gone")
    
    data = driver.find_element(By.CLASS_NAME,"c-page-top__main")
    rezultataiSK = data.find_element(By.CLASS_NAME,"ng-star-inserted")

    sk = rezultataiSK.text
    sk = int(sk.split(":")[1].strip())
    
    print("Kiek rasta knygu su isbn: " + str(sk)) 
    
    if(sk == 0):
        r_dict = {}
        r_dict["Autorius"]="---"
        r_dict["Pavadinimas"]= '---'
        r_dict["Metai"]= '---'
        r_dict["isbn"]=isbn 
        
        print()
        
        return [False,r_dict]
    
    results = driver.find_element(By.CLASS_NAME,"c-data-table")
    numberOfObj = results.find_elements(By.TAG_NAME,"tr")
    data = numberOfObj[0].find_element(By.CLASS_NAME, "c-result-item__data")
    rows = data.find_elements(By.TAG_NAME,"p")   
    row_dict = {}
        
    for row in rows:
        key, value = row.text.split(":", 1)
            
        if(key=="Publikavimo duomenys"):
            key="Metai"
            
        key = key.strip()
        value = value.strip()
        if(key=="Metai"):
            value = re.findall(r'(\d{4})', value)[0]
                
        row_dict[key] = value
        
    row_dict["isbn"] = isbn
        
    print()
        
    return [True,row_dict]
 
def IBibliotekosPaieska(input_csv, output_csv):
    fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]

    with open(input_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        newrows = list()
        wrongrows = list()
        lenth = len(rows)
             
        for index, row in enumerate(rows):
            print(str(int((index / lenth) * 100)) + "%")
            try:
                data=iBibliotekaScraper(row["isbn"])
                if(data[0]):
                    newrows.append( data[1] )
                else:
                    wrongrows.append( data[1] )
                                
            except Exception as e:
                print(f"Klaida: - {e}")
            
        driver.quit()  
        
        PalyginimasSuPagrindineLentelia(newrows)

    print("wrongrows")
    print(wrongrows)
    print("end - wrongrows")

    newrows.extend(wrongrows)
    
    PasalintiDublikuotasEilutes(newrows)

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(newrows)

def IBibliotekosPaieskaTiesiogiai():
    fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]
    
            for index, row in enumerate(rows):
            print(str(int((index / lenth) * 100)) + "%")
            try:
                data=iBibliotekaScraper(row["isbn"])
                if(data[0]):
                    newrows.append( data[1] )
                else:
                    wrongrows.append( data[1] )
                                
            except Exception as e:
                print(f"Klaida: - {e}")
            
        driver.quit()  

def PalyginimasSuPagrindineLentelia(inputRows):
    with open("csv/Bibliotekos Knygos - VIsos knygos.csv", 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        for iRow in inputRows:
            for index2,oRow in enumerate(rows):
                if ((iRow["Pavadinimas"] == oRow["Pavadinimas"] and oRow["Kodas"] == '')):
                    rows[index2]["Kodas"] = iRow["isbn"]
                            
    with open("csv/Bibliotekos Knygos - VIsos knygos.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Autorius", "Pavadinimas", "Metai", "Kodas"], extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)                    
        
def PasalintiDublikuotasEilutes(inputRows: list):
    with open("csv/Bibliotekos Knygos - VIsos knygos.csv", 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for index1,iRow in enumerate(inputRows):
        for index2,oRow in enumerate(rows):
            if (iRow["Pavadinimas"] == oRow["Pavadinimas"]):
                
                try:
                    inputRows.pop(index1)
                except:
                    pass