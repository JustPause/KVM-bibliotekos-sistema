import configparser
import json
import os


class Config:
    def __init__(self) -> None:
        """Initialize config manager and create files if missing."""
        self.config_dir = "config"
        self.config_path = os.path.join(self.config_dir, "config.conf")
        self.sheet_path = os.path.join(self.config_dir, ".env", "sheet.json")

        self.config = configparser.ConfigParser()

        self._ensure_config_exists()
        self._ensure_sheet_exists()

    def _ensure_config_exists(self) -> None:
        """Create config file with defaults if it doesn't exist."""
        if os.path.exists(self.config_path):
            self.config.read(self.config_path)
        else:
            os.makedirs(self.config_dir, exist_ok=True)
            self._create_default_config()

    def _create_default_config(self) -> None:
        """Write default config to file."""
        self.config["userData"] = {
            "isnbkoduatspauzdinimas": os.path.join(
                os.getcwd(), "pdfs", "isnb_koduat_spauzdinimas.pdf"
            ),
            "kurtinaujusbarkodus": os.path.join(
                os.getcwd(), "pdfs", "kurti_naujus_barkodus.pdf"
            ),
            "isklaveturosskaitytuvo": os.path.join(
                os.getcwd(), "csv", "is_klaveturos_skaitytuvo.csv"
            ),
            "ieskotipagalpavadinima": os.path.join(
                os.getcwd(), "pdfs", "ieskoti_pagal_pavadinima.pdf"
            ),
            "lentelessukurimas": os.path.join(os.getcwd(), "csv", "Testavimas.csv"),
            "duomenuperkelimas": os.path.join(os.getcwd(), "csv", "Testavimas.csv"),
        }
        with open(self.config_path, "w") as f:
            self.config.write(f)

    def _ensure_sheet_exists(self) -> None:
        """Create sheet.json if it doesn't exist."""
        if os.path.exists(self.sheet_path):
            pass
        else:
            sheet_dir = os.path.dirname(self.sheet_path)
            os.makedirs(sheet_dir, exist_ok=True)
            with open(self.sheet_path, "w") as f:
                f.write("{}")

    def load_config_json(self) -> tuple[str, str, str, str]:
        """Load configuration from sheet.json file.

        Returns:
            Tuple of (sheet_id, range, range_with_catalog, range_template)
        """
        with open(self.sheet_path, "r") as sheet_json:
            sheet = json.load(sheet_json)

        return (
            sheet["sheet_id"],
            sheet["range"],
            sheet["range_with_catalog"],
            sheet["range_template"],
        )

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

    # The config.conf file

    def get_user_data(self, name: str):
        return self.config["userData"][name]

    def set_user_data(self, name: str, path: str):
        self.config["userData"][name] = path

        with open("config/config.conf", "w") as f:
            self.config.write(f)

    def get_default_data(self, name: str):
        return self.config["DEFAULT"][name]
