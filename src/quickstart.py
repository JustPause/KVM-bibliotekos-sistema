import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    token = "src/.env/token.json"
    client_secret = "src/.env/client_secret.json"
    creds = None
    sheet = None
    sheet_id = None
    rage = None

    with open("src/.env/sheet.json", 'r') as sheet_json:
        sheet = json.load(sheet_json)

        # sheet = json.loads(sheet_json)
        print(sheet["sheet_id"])
        sheet_id = sheet["sheet_id"]
        sheet_range = sheet["rage"]

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
        result = (
            sheet.values()
            .get(spreadsheetId=sheet_id, range=sheet_range)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        print("Name, Major:")
        for row in values:
            print(row)
    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()