from InquirerPy import prompt,inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import csv
from src.osHelper import is_file_empty
from src.progress import Progress

driver=None
search_box=None

fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]

def iBiblioteka_scraper(isbn): 
    if(driver==None): 
        connect_to_driver()
    
    print("Kodas kurio ieskau - " + str(isbn))

    search_box = driver.find_element(By.ID, "mat-input-0")
    search_box.clear()             
    search_box.send_keys(str(isbn))
    search_button = driver.find_element(By.CLASS_NAME,"c-btn--cta")
    search_button.click()
    
    r_dict=data_extracotr(isbn)
    
    print(r_dict)
    print()
        
    return r_dict

def data_extracotr(isbn):
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
    )
    
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
                
        return r_dict
    
    results = driver.find_element(By.CLASS_NAME,"c-data-table")
    numberOfObj = results.find_elements(By.TAG_NAME,"tr")
    
    corectrow=0

    for x in range(len(numberOfObj)):
        infoLine = numberOfObj[x].find_element(By.CSS_SELECTOR, ".c-result-item__info.h-tablet-portrait-hide")
        infoLinespam=infoLine.find_elements(By.CLASS_NAME, "ng-star-inserted")
        key, value = infoLinespam[1].text.split(":", 1)
        value = value.strip()
        if(value=="SPAUSDINTINIS"):
            corectrow=x
    
    data = numberOfObj[corectrow].find_element(By.CLASS_NAME, "c-result-item__data")
    rows = data.find_elements(By.TAG_NAME,"p")   
    row_dict = {}
        
    for row in rows:
        if(row.text.strip()=="Susideda iš dalių" or row.text.strip()==""):
            break
        
        key, value = row.text.split(":", 1)
            
        if(key=="Publikavimo duomenys"):
            key="Metai"
            
        key = key.strip()
        value = value.strip()
        if(key=="Metai"):
            years = re.findall(r'\d{4}', value)
            value = years[0] if years else ""
                
        row_dict[key] = value
        
    row_dict["isbn"] = isbn
    
    return row_dict

def connect_to_driver():
    global driver, search_box
    progress = Progress(3)
    options = Options()
        
    progress.progress("Bandoma susijukti su iBiblioteka")
        
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://ibiblioteka.lt/metis/publication")

    progress.progress("Susijukta su iBiblioteka")
        
    search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "mat-input-0"))
        )
        
    WebDriverWait(driver, 30).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
        )
        
    progress.progress("Pasiruosia priimti duomenis")

def input_form_user(isbn):
    
    local_isbn = isbn
    
    while True:
        Autorius    = inquirer.text(message="Autorius:").execute()
        Pavadinimas = inquirer.text(message="Pavadinimas:").execute()
        Metai       = inquirer.text(message="Metai:").execute()
        proceed   = inquirer.select(
            message="Choose one option:",
            choices=["Testi", "Bandyti dar kart", "Pataisyti ISNB"],
        ).execute()

        if proceed == "Testi":
            break
        elif proceed == "Pataisyti ISNB":
            local_isbn = inquirer.text(message="Naujas ISNB:").execute()
            
    r_dict = {}
    r_dict["Autorius"]=Autorius
    r_dict["Pavadinimas"]= Pavadinimas
    r_dict["Metai"]= Metai
    r_dict["isbn"]=local_isbn 
    return r_dict

def iBibliotekos_paieska(input_csv, output_csv, emtey_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        nrows = list()
        wrows = list()
        lenth = len(rows)
        
        for index, row in enumerate(rows):
            print(str(int((index / lenth) * 100)) + "%")
        
            data=iBiblioteka_scraper(row["isbn"])
            
            if(data[ fieldnames[ 1 ] ] == "---"):
                nrows.append( data )
                
            else:
                if not conpare_with_main_sheet( data ):
                    nrows.append( data )
        
    with open(output_csv, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(nrows)

def iBibliotekos_paieska_tiesiogiai(output_csv):

    global driver
        
    connect_to_driver()

    while True:
        isbn = inquirer.text(message="ISBN:").execute()
        isbn = str(isbn)
        
        if(isbn.lower() == 'q'): 
            kill_drive()
            break

        data = iBiblioteka_scraper(isbn)

        if conpare_with_main_sheet(data):
            continue
        
        file_empty = is_file_empty(output_csv)

        with open(output_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames = fieldnames, extrasaction='ignore')

            if file_empty:
                writer.writeheader()
            writer.writerow(data) 

def conpare_with_main_sheet(inputRows : list):

    # if is_file_empty("csv/Bibliotekos Knygos - VIsos knygos.csv"):
    #     print("Ikleti is pagrindines lenteles csv faila")
    #     return

    # with open("csv/Bibliotekos Knygos - VIsos knygos.csv", 'r', newline='', encoding='utf-8') as f:
    #     rows = list(csv.DictReader(f))
    #     dublicaterows= []

    #     for oRow in rows:
    #         if ((inputRows["Pavadinimas"] == oRow["Pavadinimas"] and oRow["Kodas"] == '')):
    #             dublicaterows.append({"Pavadinimas":inputRows["Pavadinimas"], "isnb":oRow["Kodas"]})
    #             return True
    #         if ((inputRows["Pavadinimas"] == oRow["Pavadinimas"])):
    #             dublicaterows.append({"Pavadinimas":inputRows["Pavadinimas"], "isnb":""})
    #             return True
    #     return False
    return False

def input_form_user(pavadinimas = "", metai=""):
    
    while True:
        Autorius    = inquirer.text(message="Autorius:").execute()
        Pavadinimas = inquirer.text(message="Pavadinimas:",  default=pavadinimas).execute()
        Metai       = inquirer.text(message="Metai:", default=metai).execute()
        ISBN        = inquirer.text(message="ISBN:", default=metai).execute()
        proceed     = inquirer.select(
            message="Choose one option:",
            choices=["Testi", "Bandyti dar kart"]
        ).execute()

        if proceed == "Testi":
            break
            
    return [Autorius,Pavadinimas,Metai,ISBN]

def kill_drive():
    if(driver!=None): 
        driver.quit()