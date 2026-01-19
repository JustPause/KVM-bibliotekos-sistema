
import os.path
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


def get_data(sheet, sheet_id, sheet_range) -> list[str] | None:
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


def get_sheet_rows(rage_with_cata=False):
    sheet_id, rage, rage_with_catalog, range_template = Config.congig_json()

    sheet = connect_to_sheet()
    if rage_with_cata:
        rows = get_data(sheet, sheet_id, rage_with_catalog)
    else:
        rows = get_data(sheet, sheet_id, rage)

    if rows is None:
        raise ValueError("rows cannot be None")

    heads = rows[0]
    rows = rows[1:-1]

    working_sheet = list()

    for row in rows:
        if len(row) > len(heads):
            raise IndexError

        padding_needed = len(heads) - len(row)
        data = __padding_row_data(row, padding_needed)
        data_dict = making_dictionary_pairs(heads, data)
        working_sheet.append(data_dict)
    return working_sheet





def set_book_isnb_in_sheet(rowid: int, newData: dict[str, str]):
    sheet_id, _, _, range_template = Config.congig_json()

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


def set_vardas(rowid, returnValues):
    # Paraso i J Stulpeli
    # Paraso i K Stulpeli data

    pass


def set_korteles_id(rowid, returnValues):
    # Paraso i H Stulpeli
    # Paraso i K Stulpeli data

    pass


def set_row(rowid, returnValues):
    sheet_id, rage, rage_with_catalog, range_template = Config.congig_json()

    range_with_row = range_template.format(row=rowid)

    sheet = connect_to_sheet()
    values = [
        [returnValues],
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


def append_rows(rows):
    sheet_id, rage, rage_with_catalog, range_template = Config.congig_json()

    sheet = connect_to_sheet()

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

    return result["updates"]


def making_dictionary_pairs(heads, data):
    result = {}

    for i in range(len(heads)):
        result[heads[i]] = data[i]
    return result
