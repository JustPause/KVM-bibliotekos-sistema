import os
import wx
from main import Pagrindinis,SideBar

class Pagrindinis_updatedPath(Pagrindinis):
    def img_path(self, bitmap_path):
        return os.path.join("src", "gui", bitmap_path)

if __name__ == "__main__":
    app = wx.App(False)
    frame = Pagrindinis_updatedPath(None)
    frame.Show()
    app.MainLoop()