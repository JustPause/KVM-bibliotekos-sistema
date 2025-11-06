from InquirerPy import prompt

klausimai = [
    {
        "type": "list",
        "name": "veiksmas",
        "message": "Pasirinkite, kokią funkciją norite atlikti:",
        "choices": [
            "Brūkšninio kodo kūrimas",
            "Knygų rašymas į iBiblioteką pagal ISBN",
            "ISBN iš CSV į PDF",
            "Lėtesnė knygų paieška"
        ],
    }
]

result = prompt(klausimai)

print(f"You selected: {result['veiksmas']}")