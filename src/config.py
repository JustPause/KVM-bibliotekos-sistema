import json


class Config:
    def congig_json(self) -> tuple[str, str, str, str]:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)

            sheet_id = sheet["sheet_id"]
            rage = sheet["rage"]
            rage_with_catalog = sheet["rage_with_catalog"]
            range_template = ["range_template"]
        return sheet_id, rage, rage_with_catalog, str(range_template)

    def get_sheet_id(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["sheet_id"]

    def get_rage(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage"]

    def get_rage_with_catalog(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_with_catalog"]

    def get_range_template(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["range_template"]

    def get_rage_korteles(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_korteles"]

    def get_rage_vardas(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_vardas"]

    def get_rage_data(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_data"]

    def get_rage_func(self) -> str:
        with open("src/.env/sheet.json", "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_func"]
