import wx
from main import Pagrindinis

if __name__ == "__main__":
    app = wx.App(False)
    frame = Pagrindinis(None)
    frame.Show()
    app.MainLoop()