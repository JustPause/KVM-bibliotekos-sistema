import configparser
import os
import sys
import wx

from src.ISBNPrint import form_buffer_to_pdf
from src.ibibliotekaConnection import iBibliotekos_paieska_tiesiogiai_core
from src.helpers.utils import get_fieldnames
from src.osHelper import git_build_number
from src.barcodeKurimas import barcode_generator

import src.gui.wxformbuilder as wxformbuilder

class Pagrindinis(wxformbuilder.Pagrindinis):
    def img_path( self, bitmap_path ):
        
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
            
        bitmap_path = os.path.join(base_path, "src","gui",bitmap_path)
        
        return bitmap_path
    pass

class ISNBkoduAtspauzdinimas(wxformbuilder.ISNBkoduAtspauzdinimas):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.config = configparser.ConfigParser()
        self.config.read("config.conf")
        
        ISNBkoduAtspauzdinimasIKur = self.config["userData"]["ISNBkoduAtspauzdinimasIKur"]
        
        ISNBkoduAtspauzdinimasIKur = os.path.expanduser("~") if ISNBkoduAtspauzdinimasIKur == "" else ISNBkoduAtspauzdinimasIKur
                
        self.m_textCtrl3.SetValue(ISNBkoduAtspauzdinimasIKur)
        
    def SelectingCSVPath(self, event):
        path = ""
        
        with wx.FileDialog(
            self,
            "Pasirinkitia lokacija",
            wildcard="Lentelė (*.csv)|*.csv",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as dlg:
            
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                
        self.config["userData"]["ISNBkoduAtspauzdinimasIKur"] = path

        with open("config.conf", "w") as f:
            self.config.write(f)
            
        self.m_textCtrl3.SetValue(path)
    
    def next( self, event ):
        print("working")
        rows=[]
        
        for row in range(self.m_grid1.GetNumberRows()):
            
            value= self.m_grid1.GetCellValue(row, 0)
            
            if value != "":
                rows.append( value )
        print("Path: "+self.m_textCtrl3.GetValue())
        print("data[0]: "+rows[0])
            
        form_buffer_to_pdf(rows,self.m_textCtrl3.GetValue())


class KurtiNaujusBarkodus(wxformbuilder.KurtiNaujusBarkodus):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetNewPath()
        
    def SetNewPath(self):
        self.m_textCtrl3.SetValue(os.path.join(os.getcwd(), "pdfs", "BarkodaiSpauzdinimui.pdf"))
    
    def next( self, event ):
        dest_path=self.m_textCtrl3.GetValue()
        count=self.m_textCtrl2.GetValue()
        
        print(dest_path)
        print(count)
        
        try:
            barcode_generator(int(count), dest_path)
            wx.MessageBox(
                "Sėkmingai pavyko",
                "Rezultatas",
                wx.OK | wx.ICON_INFORMATION
            )
        except:
            wx.MessageBox(
                "Kažkas nepavyko",
                "Rezultatas",
                wx.OK | wx.ICON_INFORMATION
            )
        event.Skip()
    

class IsCSV(wxformbuilder.IsCSV):
    pass

class IsKlavetūrosSkaitytuvo(wxformbuilder.IsKlavetūrosSkaitytuvo):
    def file_free_scan(self, event):
        wx.CallAfter(
            lambda: self.GetParent().ReplacePanelNext(IsKlavetūrosSkaitytuvoEkranas)
        )

        event.Skip()
    def next(self, event):    
        pass
        
class IsKlavetūrosSkaitytuvoEkranas(wxformbuilder.IsKlavetūrosSkaitytuvoEkranas):    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.addingColumsHeaders(self.m_dataViewListCtrl1)
        
    def Enter(self, event): 
        data = iBibliotekos_paieska_tiesiogiai_core( event.GetString() ) 
        fieldnames = get_fieldnames()
        
        self.m_dataViewListCtrl1.AppendItem([data[fieldnames[0]], data[fieldnames[1]], data[fieldnames[2]], data[fieldnames[3]]])
        
        self.m_textCtrl9.SetValue("")
        self.m_textCtrl9.SetFocus()
    
    @staticmethod   
    def addingColumsHeaders(dataView):
        
        fieldnames = get_fieldnames()
        
        for field in fieldnames:
            dataView.AppendTextColumn(field)
            
        cols = dataView.GetColumns()

        width = dataView.GetClientSize().width
        col_width = width // len(cols)

        for col in cols:
            col.SetWidth(col_width)


class IeskotiPagalPavadinima(wxformbuilder.IeskotiPagalPavadinima):
    pass

class Patikrinti(wxformbuilder.Patikrinti):
    pass

class SideBar(wxformbuilder.SideBar):
 
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        full_version=self.VersionAndBuild()
        self.m_staticText29.SetLabel(full_version)

    def VersionAndBuild(self):
        import configparser
        
        build = git_build_number()
        config = configparser.ConfigParser()
        config.read("config.conf")
        version = config["DEFAULT"]["version"]
        
        return f"vesrija - {version}+{build}"
        
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
        
    def version(self, event):
        import configparser

        config = configparser.ConfigParser()
        config.read("config.conf")
        developer = config["helpMessige"]["developer"]
        email = config["helpMessige"]["email"]
        repoURL = config["helpMessige"]["repoURL"]
        wx.MessageBox(
            "Programa sukurė: " + developer + 
            "\nMane galite pasiekti: " + email + 
            "\nRepositorjia turetu buti: " + repoURL,
                "Programuotojo kontaktai",
                wx.OK | wx.ICON_INFORMATION
            )
        

