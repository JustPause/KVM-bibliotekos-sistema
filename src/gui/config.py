import configparser
import os

class ConfigFile():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.conf")

    def getUserData(self, name):
        ISNBkoduAtspauzdinimasIKur = self.config["userData"][name]
        return os.path.expanduser("~") if ISNBkoduAtspauzdinimasIKur == "" else ISNBkoduAtspauzdinimasIKur

    def setUserData(self, name, path):
        self.config["userData"][name] = path

        with open("config.conf", "w") as f:
            self.config.write(f)