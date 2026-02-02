import gettext
from typing import override

import wx

from src.gui.override_main import Pagrindinis, SideBar
from src.ibiblioteka_connection import kill_drive


class GUI(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=gettext.gettext("Pagrindinis"),
            pos=wx.DefaultPosition,
            size=wx.Size(1280, 740),
            style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE,
        )

        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sideBar = SideBar(self)
        self.mainPanel = Pagrindinis(self)

        self.mainSizer.Add(self.sideBar, 0, wx.EXPAND, 0)
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(self.mainSizer)
        self.Layout()

    def replace_panel(self, MainPanelClass) -> None:
        self.mainSizer.Detach(self.mainPanel)

        self.mainPanel.Destroy()
        self.mainPanel = MainPanelClass(self)
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(self.mainSizer)
        self.Layout()

    def replace_panel_next(self, MainPanelClass, path=None):
        self.mainSizer.Detach(self.mainPanel)

        self.mainPanel.Destroy()
        self.mainPanel = MainPanelClass(self, path)
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(self.mainSizer)
        self.Layout()

    def replace_panel_catalog(self, MainPanelClass, catalog, path=None):
        self.mainSizer.Detach(self.mainPanel)

        self.mainPanel.Destroy()
        self.mainPanel = MainPanelClass(self, catalog, path)
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(self.mainSizer)
        self.Layout()


class Barkodas(wx.App):
    @override
    def OnExit(self):
        print("Pragrama isjungema: Duomenis pravalomi. uzdaromi langai")

        kill_drive()

        return 0


def run():
    app = Barkodas(False)
    frame = GUI(None)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    run()
