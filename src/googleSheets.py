import os.path
from datetime import datetime
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.config import Config
from src.helpers.utils import get_fieldnames

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def connect_to_sheet() -> Any:
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    token = "src/.env/token.json"
    client_secret = "src/.env/client_secret.json"
    creds = None
    sheet = None

    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
            creds = flow.run_local_server(
                port=0, access_type="offline", prompt="consent"
            )
        with open(token, "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()

        return sheet

    except HttpError as err:
        print(err)

        return None


def __get_data(sheet, sheet_id, sheet_range) -> list[str] | None:
    result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    values = result.get("values", [])

    if not values:
        print("No data found.")
        return None

    return values


def __padding_row_data(row, padding_needed):
    data = list(row)
    for _ in range(padding_needed):
        data.append("")

    return data


def __padding_row_data_v2(rows: list[list[str]], reqerd_len):
    data = list()

    for row in rows:
        for _ in range(reqerd_len - len(row)):
            row.append("")

        data.append(row)

    return data


def get_sheet_rows(rage_with_cata=False):
    sheet_id, rage, rage_with_catalog, range_template = Config().congig_json()

    sheet = connect_to_sheet()
    if rage_with_cata:
        rows = __get_data(sheet, sheet_id, rage_with_catalog)
    else:
        rows = __get_data(sheet, sheet_id, rage)

    if rows is None:
        raise ValueError("rows cannot be None")

    heads = rows[0]
    rows = rows[1:]

    working_sheet = list()

    for row in rows:
        if len(row) > len(heads):
            raise IndexError

        padding_needed = len(heads) - len(row)
        data = __padding_row_data(row, padding_needed)
        data_dict = making_dictionary_pairs(heads, data)
        working_sheet.append(data_dict)

    return working_sheet


def get_book_row_with_id(id):
    config = Config()

    sheet_id = config.get_sheet_id()
    sheet_range = config.get_range_template()

    f_sheet_range = sheet_range.format(row=id)

    sheet = connect_to_sheet()
    return sheet.values().get(spreadsheetId=sheet_id, range=f_sheet_range).execute()


def get_isbn(isnb):
    config = Config()

    sheet_id = config.get_sheet_id()
    sheet_range = config.get_range_template()

    f_sheet_range = sheet_range.format(row=id)

    sheet = connect_to_sheet()
    return sheet.values().get(spreadsheetId=sheet_id, range=f_sheet_range).execute()


def get_isbn_collom():
    config = Config()

    sheet_id = config.get_sheet_id()
    sheet_range = config.get_rage_isbn_collom()

    sheet = connect_to_sheet()

    rows = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    rows = rows["values"]

    # heads = rows[0]
    rows = rows[1:]

    return rows


def get_all_data():
    config = Config()

    sheet_id = config.get_sheet_id()
    sheet_range = config.get_rage_all()

    sheet = connect_to_sheet()

    rows = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    rows = rows["values"]

    heads = rows[0]
    rows = rows[1:]

    edited_rows = __padding_row_data_v2(rows, len(heads))

    return edited_rows


def set_book_isnb_in_sheet(rowid: int, newData: dict[str, str]):
    sheet_id, _, _, range_template = Config().congig_json()

    sheet = connect_to_sheet()

    rowid = rowid + 2  # one is head, one is counting form 0 but sheet counts form 1

    if sheet is None:
        raise ValueError("sheet object is None")

    sheet_result = (
        sheet.values().get(spreadsheetId=sheet_id, range=range_template).execute()
    )

    sheet_values = list(sheet_result.get("values", [])[0])
    returnValues = dict()
    fieldnames = get_fieldnames()

    for index in range(len(fieldnames) - len(sheet_values)):
        sheet_values.append("---")

    returnValues = [
        newData["Autorius"],
        newData["Pavadinimas"],
        newData["Metai"],
        newData["isbn"],
    ]

    return set_row(rowid, returnValues)


def get_korteles_ir_naudotojei():
    config = Config()
    sheet_id = config.get_sheet_id()
    rage = config.get_rage_asmeniniai_duomenys()
    sheet = connect_to_sheet()

    return __get_data(sheet, sheet_id, rage)


def set_vardas(rowid, data):
    config = Config()

    id = config.get_sheet_id()
    rage_vardas = config.get_rage_vardas()
    rage_data = config.get_rage_data()

    rage_vardas = rage_vardas.format(row=rowid)
    rage_data = rage_data.format(row=rowid)

    execute_googleSheet(data, id, rage_vardas)

    today_date = datetime.today().strftime("%Y-%m-%d")
    result_data = execute_googleSheet(today_date, id, rage_data)
    return result_data


def set_korteles_id(rowid, data):
    config = Config()

    id = config.get_sheet_id()
    rage_korteles = config.get_rage_korteles()
    rage_data = config.get_rage_data()

    rage_korteles = rage_korteles.format(row=rowid)
    rage_data = rage_data.format(row=rowid)

    execute_googleSheet(data, id, rage_korteles)

    today_date = datetime.today().strftime("%Y-%m-%d")
    result_data = execute_googleSheet(today_date, id, rage_data)
    return result_data


def execute_googleSheet(data, sheet_id, range):
    sheet = connect_to_sheet()
    values = [
        [data],
    ]

    body = {"values": values}

    result = (
        sheet.values()
        .update(
            spreadsheetId=sheet_id,
            range=range,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )

    return result


def set_row(rowid, data):
    sheet_id, rage, rage_with_catalog, range_template = Config().congig_json()

    range_with_row = range_template.format(row=rowid)

    sheet = connect_to_sheet()
    values = [
        [data],
    ]

    body = {"values": values}

    result = (
        sheet.values()
        .update(
            spreadsheetId=sheet_id,
            range=range_with_row,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )

    return result


def getFormula(id, config):
    formula = f"""=IFERROR(QUERY(ARRAYFORMULA(TEXT(IMPORTRANGE("https://docs.google.com/spreadsheets/d/{config.get_card_table_id()}"; "{config.get_card_table_name()}"); "0")); "SELECT Col1; Col4 WHERE Col6 = '" & IF(H{id} = ""; "-"; H{id}) & "' OR Col5 = '" & IF(H{id} = ""; "-"; H{id}) & "'"); "-")"""
    return formula


def set_row_retruning_book(id):
    config = Config()
    sheet = connect_to_sheet()

    sheet_id = config.get_sheet_id()
    rage = config.get_rage_asmeniniai_duomenys_row_plius_data()

    rage = rage.format(row=id)

    formula = getFormula(id, config)

    data = ["", formula, "", ""]
    values = [data]
    body = {"values": values}

    result = (
        sheet.values()
        .update(
            spreadsheetId=sheet_id,
            range=rage,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )

    return result


def append_rows(rows: list[str]):
    config = Config()
    sheet_id, rage, rage_with_catalog, range_template = config.congig_json()

    sheet = connect_to_sheet()

    # userCheckFunc = userCheckFunc.format(row)

    # rows.append("").append("").append("").append(userCheckFunc)

    body = {"values": rows}

    result = (
        sheet.values()
        .append(
            spreadsheetId=sheet_id,
            range=rage_with_catalog,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )
    rowNumber = (
        str(result["updates"]["updatedRange"]).split("!")[1].split(":")[0].strip("A")
    )

    rage_func = config.get_rage_func().format(row=rowNumber)

    formula = getFormula(id, config)

    body = {"values": [[formula]]}

    result = (
        sheet.values()
        .append(
            spreadsheetId=sheet_id,
            range=rage_func,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )

    return result


def making_dictionary_pairs(heads, data):
    result = {}

    for i in range(len(heads)):
        result[heads[i]] = data[i]
    return result
