fieldnames = ["Autorius", "Pavadinimas", "Metai", "isbn"]


def get_fieldnames() -> list[str]:
    return fieldnames


def get_fieldnames_extra() -> list[str]:
    fieldnames.append("Kategorija")
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

    # print(data)

    return data


def addingColumsHeaders(dataView):
    fieldnames = get_fieldnames()

    for field in fieldnames:
        dataView.AppendTextColumn(field)

    cols = dataView.GetColumns()

    width = dataView.GetClientSize().width
    col_width = width // len(cols)

    for col in cols:
        col.SetWidth(col_width)
