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
    rows = get_data(sheet,sheet_id,"VIsos knygos!A:D")
    heads = rows[0]
    rows = rows[1:-1]
    
    working_sheet = list()
    
    for row in rows:
        match len(row):
            case 1:  
                data= padding_row_data(row,4-1)
                data_dict =	making_dictionary_pairs(heads, data)    
                working_sheet.append(data_dict)
                
            case 2:
                data= padding_row_data(row,4-2)
                data_dict =	making_dictionary_pairs(heads, data)      
                working_sheet.append(data_dict)
                
            case 3:
                data= padding_row_data(row,4-3)
                data_dict =	making_dictionary_pairs(heads, data)    
                working_sheet.append(data_dict)
                
            case 4:
                data= padding_row_data(row,4-4)
                data_dict =	making_dictionary_pairs(heads, data)    
                working_sheet.append(data_dict)
                
            case _:
                raise IndexError
    
    return working_sheet

def making_dictionary_pairs(heads, data):
    return {
        heads[0]: data[0],
        heads[1]: data[1],
        heads[2]: data[2],
        heads[3]: data[3]
    }