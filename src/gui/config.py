import configparser
from pathlib import Path


class ConfigFile:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = Path("config/config.conf")

        if config_path.exists():
            self.config.read(config_path)
        else:
            raise FileNotFoundError("config.conf not found")

    def get_user_data(self, name: str):
        return self.config["userData"][name]

    def set_user_data(self, name: str, path: str):
        self.config["userData"][name] = path

        with open("config.conf", "w") as f:
            self.config.write(f)

    def get_default_data(self, name: str):
        return self.config["DEFAULT"][name]
