# Programa Barkodas

###### Versija: 0.1.0 
###### Data: 2026 01 21

Programa leidžia lengviau atlikti darbus bibliotekos Google Sheets lentelėse. Ji sukurta speciškai pagal Kauno Valdorfo mokyklos reikalavimus, todėl gali nebūti idealiai pritaikyta kitoms bibliotekų sistemoms. Tačiau, suprantant kodą, galima nesunkiai pridėti bet kokį norimą funkcionalumą.
Paleidus naudotojo aplikaciją turėtų būti galima matyti šviesų langą su šone esančiu valdymo langu. Ten galima rasti pagrindines programos funkcijas.
Langą galima išplėsti ir susimažinti.
Mano rekomenduojama knygų surašymo metodologija:
- Suskirstyti knygas į su barkodais ir be barkodų.
- Tada pereiti prie knygų be barkodų ir peržiūrėti pagal ISBN kodą viduje ir be kodo.

<!-- start ISBN Kodu atspauzdinimas -->

# ISBN kodo atspausdinimas

Šis lapas duoda galimybę sukurti barkodus knygoms, kurios jų neturi. Pagal surastą skaitinį kodą sukuria barkodus, kuriuos galima užklijuoti ant knygos su klijais, kai juos atspausdinsi.

<!-- end ISBN Kodu atspauzdinimas -->
<!-- start Kurti naujus barkodus -->

# Kurti naujus barkodus

Programa leidžia pagal pasirinkimą sukurti daugybę barkodų knygoms, kurios neturi nei barkodo, nei ISBN kodo. Sukuriami lapai, kuriuos atspausdinus, susmulkinus ir užklijavus, galima ranka surašyti į lentelę.

<!-- end Kurti naujus barkodus -->
<!-- start Klaveturos / Skaitituvo -->

# Klaviatūros / Skaitytuvo

Šis langas duoda galimybę tiesiai iš kompiuterio per iBiblioteką įrašyti duomenis į lentelę, kuri yra Google Sheets. Kadangi planavau, kad bus dedama į kažkokią katalogą, pridėjau galimybę pasirinkti, kaip tą katalogą pavadinti. Taip pat yra 2 mygtukai: „Skaityti be išvedimo“ ir „Tęsti“. Jie skiriasi tuo, ar naudos CSV failą, ar ne. Jei knyga bus nerasta, ji pasirodys kaip ---, o kitu atveju gali būti įrašyta į CSV failą ir duoti rankiniam surašymui, kurį poto galima bus patogiai įgyvendinti per „CSV duomenų perkėlimą“.
<!-- end Klaveturos / Skaitituvo  -->
<!-- start Sukurit nauja CSV -->

# Sukurti naują CSV

Čia, jei nori patogiau ranka surašinėti į kompiuteryje esantį dokumentą arba duoti kitam asmeniui suvesti, galima duoti jam tuščią dokumentą, kurį lengvai bus galima įkelti į Google Sheets lentelę.

<!-- end Sukurit nauja CSV -->
<!-- start CSV duomenu perdavimas i google -->

# CSV duomenų perdavimas į Google

Šis langas leidžia paimti struktūrizuotus duomenis iš CSV failo ir įkelti į Google Sheets. Labai svarbu, kad stulpelių pavadinimai nebūtų pakeisti, nes kitaip programa pradės rašyti klaidingai.

<!-- end CSV duomenu perdavimas i google -->
<!-- start Google sheets patikrinimas -->

# Google Sheets patikrinimas

Šis langas man bent jau lėtai užsikrauna, bet kai užsikrauna, gali pasakyti, ar knyga yra lentelėje, ar ne. Pagal poreikį galiu pridėti ir pavadinimo paiešką.

<!-- end Google sheets patikrinimas -->
<!-- start Isdavimas -->

# Išdavimas

Tai langas leidžiantis įrašyti, kokią knygą norima išduoti, ir kurią mokinį ar darbuotoją pasiima knygą. Programa atnaujina tos knygos duomenis ir prideda išdavimo datą. Jei naudotojo kortelės nėra, galima išduoti pagal vardą ir klasę. Jei knyga pagal barkodą nerandama, galima ją pridėti rankiniu būdu. Po neteisingo įvedimo atsidaro papildomas langas.

<!-- end Isdavimas -->
<!-- start Grazinimas -->

# Grąžinimas

Langas duoda galimybę grąžinti knygas, turint knygos barkodą. Galima pamatyti tos knygos būseną ir spausti „Tęsti“, jei ji teisinga. Lentelėje bus pašalintas naudotojo kodas arba vardas ir įrašyta grąžinimo data.

<!-- end Grazinimas -->