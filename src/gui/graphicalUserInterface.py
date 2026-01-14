from typing import override

import wx

from src.gui.gui import GUI
from src.ibibliotekaConnection import kill_drive


class Barkodas(wx.App):
    @override
    def OnExit(self):
        print("App is quitting! Do cleanup here")

        kill_drive()

        return 0


def run():
    app = Barkodas(False)
    frame = GUI(None)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    run()
