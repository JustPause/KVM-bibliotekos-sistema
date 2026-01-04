import os
import wx
import gettext

from src.ibibliotekaConnection import kill_drive
from src.gui.overrideMain import ISNBkoduAtspauzdinimas, Pagrindinis, SideBar

class GUI(wx.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, title="Barkodas")
        
    def __init__(self, parent):    
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = gettext.gettext(u"Pagrindinis"), pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE )
        
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.sideBar = SideBar(self)
        self.mainPanel = Pagrindinis(self)
        
        self.mainSizer.Add(self.sideBar, 0, wx.EXPAND, 0)
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)
        
        self.SetSizer(self.mainSizer)
        self.Layout()

    def ReplacePanel(self, mainPanelClass):     
        self.mainSizer.Detach(self.mainPanel)

        self.mainPanel.Destroy()
        self.mainPanel = mainPanelClass(self)  
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(self.mainSizer)
        self.Layout()

    def ReplacePanelNext(self, mainPanelClass):             
        self.mainSizer.Detach(self.mainPanel)

        self.mainPanel.Destroy()
        self.mainPanel = mainPanelClass(self)  
        self.mainSizer.Add(self.mainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(self.mainSizer)
        self.Layout()
        
class Barkodas(wx.App):
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
