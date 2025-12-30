import os
import wx
import src.gui.wxformbuilder as wxformbuilder

class Pagrindinis(wxformbuilder.Pagrindinis):
    def img_path( self, bitmap_path ):
        
        bitmap_path=os.path.join("src","gui",bitmap_path)
        return bitmap_path
    pass

class ISNBkoduAtspauzdinimas(wxformbuilder.ISNBkoduAtspauzdinimas):
    pass

class KurtiNaujusBarkodus(wxformbuilder.KurtiNaujusBarkodus):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetNewPath()
        
    def SetNewPath(self):
        self.m_textCtrl3.SetValue("New text on startup")
    

class IsCSV(wxformbuilder.IsCSV):
    pass

class IsKlavetūrosSkaitytuvo(wxformbuilder.IsKlavetūrosSkaitytuvo):
    pass

class IeskotiPagalPavadinima(wxformbuilder.IeskotiPagalPavadinima):
    pass

class Patikrinti(wxformbuilder.Patikrinti):
    pass

class SideBar(wxformbuilder.SideBar):
 
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def __PikingLable(self,Lable):
        CLASS_NAME_AND_LABLES = [
            {  
                "Class": KurtiNaujusBarkodus,
                "Label": "Kurti naujus barkodus"
            },
            {  
                "Class": ISNBkoduAtspauzdinimas,
                "Label": "ISNB kodu atspauzdinimas"
            },
            {  
                "Class": IsCSV,
                "Label": "Iš CSV"
            },
            {  
                "Class": IsKlavetūrosSkaitytuvo,
                "Label": "Iš Klavetūros / Skaitytuvo"
            },
            {  
                "Class": IeskotiPagalPavadinima,
                "Label": "Ieškoti pagal pavadinima"
            },
            {  
                "Class": Patikrinti,
                "Label": "Localioje lenteje"
            }
        ]
        
        for classlable in CLASS_NAME_AND_LABLES:
            if classlable["Label"] == Lable:
                return classlable["Class"]
            
        return None
        
    def Click(self, event):
        btnLabel = event.GetEventObject().GetLabel()
        btnClickClass = self.__PikingLable(btnLabel)
        
        self.GetParent().ReplacePanel(btnClickClass)
        
        event.Skip()
        

