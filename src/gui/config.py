import configparser
import os


class ConfigFile:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.conf")

    def getUserData(self, name: str):
        return self.config["userData"][name]

    def setUserData(self, name: str, path: str):
        self.config["userData"][name] = path

        with open("config.conf", "w") as f:
            self.config.write(f)
