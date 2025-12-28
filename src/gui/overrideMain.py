import wx
import wxformbuilder

class SideBar(wxformbuilder.SideBar): 
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def Click(self, event):
        print("Button was clicked!")
        
        event.Skip()
        

class Pagrindinis(wxformbuilder.Pagrindinis): 
    pass

class ISNBkoduAtspauzdinimas(wxformbuilder.ISNBkoduAtspauzdinimas):
    pass