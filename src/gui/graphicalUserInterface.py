import os
import wx
import gettext
from main import Pagrindinis,Testing

class Pagrindinis_updatedPath(Pagrindinis):
    def img_path(self, bitmap_path):
        return os.path.join("src", "gui", bitmap_path)

class GUI(wx.Frame):
    def __init__(self, parent):    
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = gettext.gettext(u"Pagrindinis"), pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE )
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.testing = Testing(self)
        mainSizer.Add(self.testing, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
        self.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = GUI(None)
    frame.Show()
    app.MainLoop()