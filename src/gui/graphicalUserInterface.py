import os
import wx
import gettext

from overrideMain import ISNBkoduAtspauzdinimas, Pagrindinis, SideBar

class GUI(wx.Frame):
    def __init__(self, parent):    
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = gettext.gettext(u"Pagrindinis"), pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE )
        
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.sideBar = SideBar(self)
        self.mainPanel = Pagrindinis(self)
        
        self.mainSizer.Add(self.sideBar, 0, wx.EXPAND, 0)
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)
        
        self.SetSizer(self.mainSizer)
        self.Layout()

    def ReplacePanel(self):     
        # self.mainSizer.Detach(self.sideBar)
        self.mainSizer.Detach(self.mainPanel)
        
        # self.sideBar.Destroy()
        self.mainPanel.Destroy()

        # self.sideBar = SideBar(self)
        self.mainPanel = ISNBkoduAtspauzdinimas(self)
        
        # self.mainSizer.Add(self.sideBar, 0, wx.EXPAND, 0)
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(self.mainSizer)
        self.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = GUI(None)
    frame.Show()
    app.MainLoop()