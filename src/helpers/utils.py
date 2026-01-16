fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]


def get_fieldnames():
    return fieldnames


def fromDicToArray(dict):
    data = [
        dict[fieldnames[0]],
        dict[fieldnames[1]],
        dict[fieldnames[2]],
        dict[fieldnames[3]],
    ]

    return data


def fromDicToArrayAddCatalog(dict, catalog):
    data = [
        dict[fieldnames[0]],
        dict[fieldnames[1]],
        dict[fieldnames[2]],
        dict[fieldnames[3]],
        catalog,
    ]

    print(data)

    return data
