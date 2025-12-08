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
from src.Progresas import Progresas

driver=None
search_box=None

fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]

def iBibliotekaScraper(isbn): 
    if(driver==None): 
        susijuntiSuDriver()
    
    print("Kodas kurio ieskau - " + str(isbn))

    search_box = driver.find_element(By.ID, "mat-input-0")
    search_box.clear()             
    search_box.send_keys(str(isbn))
    search_button = driver.find_element(By.CLASS_NAME,"c-btn--cta")
    search_button.click()
    
    r_dict=dataExtracotr(isbn)
    
    print(r_dict)
    print()
        
    return r_dict

def dataExtracotr(isbn):
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
        
    for x in range(sk):
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

def susijuntiSuDriver():
    global driver, search_box
    progresas = Progresas(3)
    options = Options()
        
    progresas.zingsnis("Bandoma susijukti su iBiblioteka")
        
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://ibiblioteka.lt/metis/publication")

    progresas.zingsnis("Susijukta su iBiblioteka")
        
    search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "mat-input-0"))
        )
        
    WebDriverWait(driver, 30).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
        )
        
    progresas.zingsnis("Pasiruosia priimti duomenis")

def inputFormUser(isbn):
    
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

def iBibliotekosPaieska(input_csv, output_csv, emtey_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        nrows = list()
        wrows = list()
        lenth = len(rows)
        
        for index, row in enumerate(rows):
            print(str(int((index / lenth) * 100)) + "%")
        
            data=iBibliotekaScraper(row["isbn"])
            
            if(data[ fieldnames[ 1 ] ] == "---"):
                nrows.append( data )
                
            else:
                nrows.append( data )

        if(driver): 
            killinDrive()
        
        # nrows=PalyginimasSuPagrindineLentelia(nrows)

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(nrows)

def iBibliotekosPaieskaTiesiogiai(output_csv, test=False):

    global driver
        
    susijuntiSuDriver()

    while True:
        isbn = ""
        if not test:
            isbn = inquirer.text(message="ISBN:").execute()
        isbn = str(isbn)
        
        data=iBibliotekaScraper(isbn)

        # data=PalyginimasSuPagrindineLentelia(data)

        with open(output_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames = fieldnames, extrasaction='ignore')
            writer.writerow(data) 

def duomenuIsgavimas(isbn):
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
    )
    
    print("Spinner search gone")
    
    data = driver.find_element(By.CLASS_NAME,"c-page-top__main")
    rezultataiSK = data.find_element(By.CLASS_NAME,"ng-star-inserted")
    
    sk = rezultataiSK.text
    sk = int(sk.split(":")[1].strip())
    
    print("Kiek rasta knygu su isbn: " + str(sk)) 
    
    data = duomenuApdirbinas(sk,isbn)
        
    print(data)
            
    if sk==0:
        data = inputFormUser(isbn)
        print(data)
        # TODO Pataisti funcionaluma kad galima butu irastyti duomenis nes dabar jie isiraso neteinsingi
        # TODO Pataisyti Loop, kad kai irasai is naujo ISNB nuskaunuoti bibleioka

        # except Exception as e:
        #     print(f"Klaida: - {e}")

def duomenuApdirbinas(sk,isbn):
    if(sk == 0):
        r_dict = {}
        r_dict["Autorius"]="---"
        r_dict["Pavadinimas"]= '---'
        r_dict["Metai"]= '---'
        r_dict["isbn"]=isbn 
        
        print()
        
        return r_dict
    
    results = driver.find_element(By.CLASS_NAME,"c-data-table")
    numberOfObj = results.find_elements(By.TAG_NAME,"tr")
    data = numberOfObj[0].find_element(By.CLASS_NAME, "c-result-item__data")
    rows = data.find_elements(By.TAG_NAME,"p")   
    row_dict = {}
        
    for row in rows:
        if row.text=="Susideda iš dalių":
            break
        
        if ':' in row.text:
            key, value = row.text.split(":", 1)
        else:
            key, value = row.text
            
        if(key=="Publikavimo duomenys"):
            key="Metai"
            
        key = key.strip()
        value = value.strip()
        if(key=="Metai"):
            value = re.findall(r'(\d{4})', value)[0]
                
        row_dict[key] = value
        
    row_dict["isbn"] = isbn
        
    return row_dict

def PalyginimasSuPagrindineLentelia(inputRows):
    with open("csv/Bibliotekos Knygos - VIsos knygos.csv", 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        dublicaterows= []

        for iRow in inputRows:
            for oRow in rows:
                if ((iRow["Pavadinimas"] == oRow["Pavadinimas"] and oRow["Kodas"] == '')):
                    dublicaterows.append({"Pavadinimas":iRow["Pavadinimas"], "isnb":oRow["Kodas"]})
                    rows.pop()
                if ((iRow["Pavadinimas"] == oRow["Pavadinimas"])):
                    dublicaterows.append({"Pavadinimas":iRow["Pavadinimas"], "isnb":""})
                    rows.pop()
        return rows

def inputFormUserBePavadinimo(pavadinimas = "", metai=""):
    
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

def surasimasPavadinimoIrMetu(dest_path):
    
    try:
        global driver
        options = Options()
        fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]
        
        print("Bandoma susijukti su iBiblioteka")
            
        # options.add_argument("--headless")
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
        
        while True:
            # Pavadinimas = inquirer.text(message="Pavadinimas:").execute()
            # Metai       = inquirer.text(message="Metai:").execute()
            Pavadinimas = "Džiunglės"#"Gaidžio kalnas"
            isbn = ""
            steps = 3
            step = 0
            
            driver.find_element(By.CSS_SELECTOR,".mdc-button.mat-mdc-button.c-btn--secondary.rounded-0.w-100.mat-unthemed.mat-mdc-button-base").click()
            driver.find_element(By.CSS_SELECTOR,".cookie-agreement__button").click()
            
            search_box = driver.find_element(By.ID, "mat-input-0")    
            
            search_box.clear()             
            search_box.send_keys(Pavadinimas)

            driver.find_element(By.ID, "mat-select-value-0").click()
            driver.find_element(By.ID, "mat-option-1").click()
            
            WebDriverWait(driver, 5).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cdk-overlay-backdrop.cdk-overlay-transparent-backdrop.cdk-overlay-backdrop-showing"))
            )
            
            driver.find_element(By.CLASS_NAME,"c-btn--cta").click()
            
            WebDriverWait(driver, 10).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
            )

            step=step+1
            print("Spinner search gone " +str(steps)+"/"+str(step))
            
            sideBar = driver.find_element(By.CLASS_NAME,"c-multicolumn-page__side-content")
            sideBarElements = sideBar.find_elements(By.CSS_SELECTOR,".c-filter-box.ng-untouched.ng-pristine.ng-valid")
            
            for element in sideBarElements:
                element_span=element.find_element(By.CLASS_NAME, "btn-label")
                
                if element_span.text == "Forma":
                    breaking=True
                    
                    element.find_element(By.CLASS_NAME, "mdc-label").click()
                    element.find_element(By.CSS_SELECTOR,".c-btn--secondary.h-btn-small").click()
                    
                    break
            if not breaking:
                print("Nera Forma - ")
            

            numbering = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".page-selection.ng-star-inserted")
                )
            )
                        
            conting = numbering.find_element(By.ID,"mat-select-3")
            
            # WebDriverWait(driver, 10).until_not(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, ".cdk-overlay-backdrop.cdk-overlay-transparent-backdrop.cdk-overlay-backdrop-showing"))
            # )
            
            conting.click()

            cdk_overlay = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "cdk-overlay-4"))
            )
            
            span100 = cdk_overlay.find_element(
                By.XPATH,
                "//span[text()='100']"
            )
            
            span100.click()
                
            WebDriverWait(driver, 10).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner-background.active"))
            )
            
            data = driver.find_element(By.CLASS_NAME,"c-data-table")
            rezultataiSK = driver.find_element(By.CLASS_NAME,"c-page-top__main").find_element(By.CLASS_NAME,"ng-star-inserted")
            
            sk = rezultataiSK.text
            sk = int(sk.split(":")[1].strip())
            
            visosDuomenis = data.find_elements(By.CLASS_NAME,"c-result-item__data")
            grazinimas=[]
            for vienaKnyga in visosDuomenis:
                eilutes=vienaKnyga.find_elements(By.CLASS_NAME,"ng-star-inserted")
                
                rezultatas={}
                
                for eilute in eilutes:
                    dalys = eilute.text.split(":")
                    
                    key = dalys[0].strip()
                    value = ":".join(dalys[1:]).strip()
                    
                    if not key or not value:
                        continue

                    if key not in rezultatas:
                        rezultatas[key] = value
                    grazinimas.append(rezultatas)
            
            # if sk==0:
            #     row=inputFormUser(isbn)
            #     data = [True,{'Autorius': row[0], 'Pavadinimas':  row[1], 'Metai':  row[2], 'isbn': row[3]}]
            # print("Kiek rasta knygu su isbn: " + str(sk)) 
            
            PaklaustiNaudotojoApieTinkamaKnyga(grazinimas,dest_path)
            killinDrive()
            # data = duomenuApdirbinas(sk,isbn)
    except KeyboardInterrupt:
        killinDrive()
        print("KeyboardInterrupt")

def PaklaustiNaudotojoApieTinkamaKnyga(data,output_csv):
    
    choices = []
    for book in data:
        tekstas={"Autorius":"---", "Pavadinimas":"---", "Metai":"---", "isbn":"---"}
        choices.append(tekstas)
    
    knyga = inquirer.select(
        message="Pasirinkite kuri knyga:",
        choices=choices,
        multiselect=True,
        transformer=lambda result: f"{len(result)} pasirinkta",
    ).execute()
    
    fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]
    with open(output_csv, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = fieldnames, extrasaction='ignore')
        print(data)
        writer.writerows(data) 
        
def killinDrive():
    if(driver!=None): 
        driver.quit()