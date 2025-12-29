import wx
import wxformbuilder

class Pagrindinis(wxformbuilder.Pagrindinis): 
    pass

class ISNBkoduAtspauzdinimas(wxformbuilder.ISNBkoduAtspauzdinimas):
    pass

class SideBar(wxformbuilder.SideBar):
    CLASS_NAME_AND_LABLES = [
        {  
            "Class": ISNBkoduAtspauzdinimas,
            "Label": "ISNB kodu atspauzdinimas"
        }
    ]
     
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def __PikingLable(self,Lable):
        for classlable in self.CLASS_NAME_AND_LABLES:
            if classlable["Label"] == Lable:
                return classlable["Class"]
        
    def Click(self, event):
        print("Button was clicked!")
        btnLabel = event.GetEventObject().GetLabel()
        btnClickClass=self.__PikingLable(btnLabel)
        self.GetParent().ReplacePanel()
        event.Skip()
        

