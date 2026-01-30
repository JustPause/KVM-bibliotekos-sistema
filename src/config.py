import json


class Config:
    def __init__(self) -> None:
        self.sheet = "config/.env/sheet.json"

    def congig_json(self) -> tuple[str, str, str, str]:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)

            sheet_id = sheet["sheet_id"]
            rage = sheet["rage"]
            rage_with_catalog = sheet["rage_with_catalog"]
            range_template = ["range_template"]
        return sheet_id, rage, rage_with_catalog, str(range_template)

    def get_sheet_id(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["sheet_id"]

    def get_rage_isbn_collom(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_isbn_collom"]

    def get_rage_vardas(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_vardas"]

    def get_rage_all(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_all"]

    def get_rage(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage"]

    def get_rage_with_catalog(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_with_catalog"]

    def get_range_template(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["range_template"]

    def get_rage_korteles(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_korteles"]

    def get_rage_asmeniniai_duomenys(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_asmeniniai_duomenys"]

    def get_rage_asmeniniai_duomenys_row_plius_data(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_asmeniniai_duomenys_row_plius_data"]

    def get_rage_visos_korteles(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_visos_korteles"]

    def get_rage_data(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_data"]

    def get_rage_func(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["rage_func"]

    def get_card_table_id(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["card_table_id"]

    def get_card_table_name(self) -> str:
        with open(self.sheet, "r") as sheet_json:
            sheet = json.load(sheet_json)
            return sheet["card_table_name"]
