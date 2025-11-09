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

    if(driver==None):

        options = Options()
        print("Bandoma susijukti su iBiblioteka")
        
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)
        driver.get("https://ibiblioteka.lt/metis/publication")
        print("Susijukta su iBiblioteka")
        
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "mat-input-0"))
        )
        
        WebDriverWait(driver, 10).until_not(
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
        r_dict["Autorius"]="ranka surasyti"
        r_dict["Pavadinimas"]= ''
        r_dict["Metai"]= ''
        r_dict["isbn"]=isbn 
        return r_dict
    
    results=driver.find_element(By.CLASS_NAME,"c-data-table")

    numberOfObj=results.find_elements(By.TAG_NAME,"tr")

    for index,each in enumerate(numberOfObj):
        data = each.find_element(By.CLASS_NAME, "c-result-item__data")
        
        rows=data.find_elements(By.TAG_NAME,"p")
        
        
        
        print("Indexas kury panaudojau " + str(index))
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
        return row_dict

def SurasytiPoVienaEilute(input_csv, output_csv):
    fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn","Komentarai"]

    with open(input_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        lenth = len(rows)
             
        for index, row in enumerate(rows):
            print(str(int((index / lenth) * 100)) + "%")
            try:
                NewRow = iBibliotekaScraper(row["isbn"])
                NewRow["Komentarai"] = PatikrinimasArKnygaYraPagrindinejaBibliotekosLenteleja(NewRow)
            except Exception as e:
                print(f"Klaida: {rows[index]} - {e}")
                NewRow = rows[index]
            
            print(NewRow)
            rows[index] = NewRow

        driver.quit()  

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

def PatikrinimasArKnygaYraPagrindinejaBibliotekosLenteleja(inputRow):
    with open("csv/Bibliotekos Knygos - VIsos knygos.csv", 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        isbnCount=0
        PavadinimasCount=0

        for index, row in enumerate(rows):  
            if((inputRow["Pavadinimas"]!="") and (row["Pavadinimas"]==inputRow["Pavadinimas"])):
                PavadinimasCount = PavadinimasCount +1
                
            if((inputRow["isbn"] != "") and (row["Kodas"] == inputRow["isbn"])):
                isbnCount = isbnCount +1
        
        if(PavadinimasCount!=0 and isbnCount!=0 and PavadinimasCount==isbnCount):
            return "Jau yra " + str(PavadinimasCount) + " Tai praleisti reikia"
        
        elif(PavadinimasCount!=0):
            sutvarikimas(inputRow)
            return"Yra pavadinimas, bet ne kodas - Reikia perdeti is lenteles"
        
        
        elif(isbnCount!=0):
            return"Yra keli su tuom paciu isbn - Reikia pasalinti"
        
        else:
            return "Reikia uzrasyti i lentelia"
        
def sutvarikimas(forin_row):
    with open("csv/Bibliotekos Knygos - VIsos knygos.csv", 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        for index, row in enumerate(rows):
            if( row["Pavadinimas"]==forin_row["Pavadinimas"]):
                with open("csv/Bibliotekos Knygos - tik dublikuotos.csv", "a", newline="", encoding="utf-8") as f_2:
                    writer = csv.DictWriter(f_2, fieldnames=["Autorius", "Pavadinimas", "Metai", "isbn","Komentarai"], extrasaction='ignore')
                    forin_row["Komentarai"] = "index: " + str(index+2)
                    writer.writerow(forin_row)

                    