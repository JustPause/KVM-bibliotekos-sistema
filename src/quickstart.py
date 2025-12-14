import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def connect_to_sheet():
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
            creds = flow.run_local_server(port=0, access_type='offline', prompt='consent')
        with open(token, "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        
        return sheet
        
    except HttpError as err:
        print(err)
        
        return None

def get_data(sheet,sheet_id,sheet_range):

    result = (
            sheet.values()
            .get(spreadsheetId=sheet_id, range=sheet_range)
            .execute()
        )
    values = result.get("values", [])

    if not values:
        print("No data found.")
        return None
    
    return values

def padding_row_data(row, local_range):
    data = list(row)
                
    for i in range(local_range):
        data.append("")
    return data

def get_sheet_rows():
    with open("src/.env/sheet.json", 'r') as sheet_json:
        sheet = json.load(sheet_json)

        sheet_id = sheet["sheet_id"]
    
    sheet = connect_to_sheet()
    rows = getData(sheet,sheet_id,"VIsos knygos!A:D")[0:10]
    heads = rows[0]
    rows = rows[1:-1]
    
    working_sheet = list()
    
    for row in rows:
        match len(row):
            case 1:      
                working_sheet.append(padding_row_data(row,4-1))
                
            case 2:
                working_sheet.append(padding_row_data(row,4-2))
                
            case 3:
                working_sheet.append(padding_row_data(row,4-3))
                
            case 4:
                working_sheet.append(padding_row_data(row,4-4))
                
            case _:
                raise IndexError
    
    return working_sheet