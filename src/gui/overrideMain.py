import wx
import wxformbuilder

class Pagrindinis(wxformbuilder.Pagrindinis): 
    pass

class ISNBkoduAtspauzdinimas(wxformbuilder.ISNBkoduAtspauzdinimas):
    pass

class KurtiNaujusBarkodus(wxformbuilder.KurtiNaujusBarkodus):
    pass

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
        

