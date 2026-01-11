import os
import sys
import wx

from src.ISBNPrint import form_buffer_to_pdf
from src.ibibliotekaConnection import iBibliotekos_paieska_tiesiogiai_core
from src.helpers.utils import get_fieldnames
from src.osHelper import git_build_number
from src.barcodeKurimas import barcode_generator
from src.gui.config import ConfigFile

import src.gui.wxformbuilder as wxformbuilder

def NeSekmingai(text):
    wx.MessageBox(
            text,
            "Rezultatas",
            wx.OK | wx.ICON_INFORMATION
        )

def Sekmingai():
    wx.MessageBox(
            "Sėkmingai pavyko",
            "Rezultatas",
            wx.OK | wx.ICON_INFORMATION
        )
    
def FileDialogWithExtesion(self, extension):
    path = ""
    
    with wx.FileDialog(
        self,
        "Pasirinkite lokaciją",
        wildcard=f"Lentelė (*.{extension})|*.{extension}",
        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    ) as dlg:
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            return path
            
    return os.path.abspath(".")

class ThinkingDialog(wx.Dialog):
    def __init__(self, parent, message="Thinking…"):
        super().__init__(parent, title="Kantrybes", style=wx.DEFAULT_DIALOG_STYLE)

        sizer = wx.BoxSizer(wx.VERTICAL)

        text = wx.StaticText(self, label=message)
        sizer.Add(text, 0, wx.ALL | wx.CENTER, 10)

        self.gauge = wx.Gauge(self, range=100)
        sizer.Add(self.gauge, 0, wx.ALL | wx.EXPAND, 10)

        self.SetSizerAndFit(sizer)

class Pagrindinis(wxformbuilder.Pagrindinis):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()
        
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
        self.configFile = ConfigFile()
        ISNBkoduAtspauzdinimas = self.configFile.getUserData("ISNBkoduAtspauzdinimas")
        
        self.textCtrl1.SetValue(ISNBkoduAtspauzdinimas)
    
    def SelectingPath(self, event):
        path = FileDialogWithExtesion(self,"pdf")

        self.configFile.setUserData("isnbkoduatspauzdinimas", path)
        self.textCtrl1.SetValue(path)
    
    def next( self, event ):
        rows=[]
        
        for row in range(self.table.GetNumberRows()):
            
            value= self.table.GetCellValue(row, 0)
            
            if value != "":
                rows.append( value )

        if len(rows) !=0:
            form_buffer_to_pdf(rows,self.textCtrl1.GetValue())
            Sekmingai()
        else:
            NeSekmingai("Parasykite bent viena eilute")

class KurtiNaujusBarkodus(wxformbuilder.KurtiNaujusBarkodus):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()

        KurtiNaujusBarkodus = self.configFile.getUserData("kurtinaujusbarkodus")

        self.inputText1.SetValue(KurtiNaujusBarkodus)

    def SelectingPath(self, event):
        path = FileDialogWithExtesion(self,"pdf")

        self.configFile.setUserData("kurtinaujusbarkodus", path)
        self.inputText1.SetValue(path)
    
    def next( self, event ):
        dest_path = self.inputText1.GetValue()
        count = self.inputText2.GetValue()
        
        try:
            barcode_generator(int(count), dest_path)
            Sekmingai()
        
        except:
            NeSekmingai("Kažkas nepavyko")
        
        event.Skip()

class IsCSV(wxformbuilder.IsCSV):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()

        csviskur = self.configFile.getUserData("csviskur")

        self.textCtrl1.SetValue(csviskur)

    def SelectingPathIs(self, event):
        path = FileDialogWithExtesion(self,"pdf")

        self.configFile.setUserData("csviskur", path)
        self.textCtrl1.SetValue(path)

    def SelectingPathKur(self, event):
        path = FileDialogWithExtesion(self,"pdf")

        self.configFile.setUserData("csvikur", path)

class SukurtiCSV(wxformbuilder.SukurtiCSV):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()

        csvikur = self.configFile.getUserData("csvikur")

        self.textCtrl1.SetValue(csvikur)

    def SelectingPathIs(self, event):
        path = FileDialogWithExtesion(self,"pdf")

        self.configFile.setUserData("csvikur", path)
        self.textCtrl1.SetValue(path)

    def SelectingPathKur(self, event):
        path = FileDialogWithExtesion(self,"pdf")

        self.configFile.setUserData("csvikur", path)

class IsKlaveturosSkaitytuvo(wxformbuilder.IsKlaveturosSkaitytuvo):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()
        IsKlaveturosSkaitytuvo = self.configFile.getUserData("kurtinaujusbarkodus")
        self.textCtrl1.SetValue(IsKlaveturosSkaitytuvo)
    
    def file_free_scan(self, event):
        wx.CallAfter(
            lambda: self.GetParent().ReplacePanelNext(IsKlaveturosSkaitytuvoEkranas)
        )

        event.Skip()
    def next(self, event):    
        path = self.textCtrl1.GetValue()
        
        wx.CallAfter(
            lambda: self.GetParent().ReplacePanelNext(IsKlaveturosSkaitytuvoEkranas, path)
        )

        event.Skip()

    def SelectingPath(self, event):
        path = FileDialogWithExtesion(self,"csv")

        self.configFile.setUserData("isklaveturosskaitytuvo", path)
        self.textCtrl1.SetValue(path)
    
class IsKlaveturosSkaitytuvoEkranas(wxformbuilder.IsKlaveturosSkaitytuvoEkranas):    
    def __init__(self, parent, path=None):
        super().__init__(parent)
        
        self.path = path
        
        self.addingColumsHeaders(self.dataViewList)
        
    def Enter(self, event): 
        loud = ThinkingDialog(self)
        loud.Show()
        
        data = iBibliotekos_paieska_tiesiogiai_core( event.GetString() ) 
        
        loud.Destroy()
        
        fieldnames = get_fieldnames()
        
        self.dataViewList.AppendItem([data[fieldnames[0]], data[fieldnames[1]], data[fieldnames[2]], data[fieldnames[3]]])
        
        self.ISBN.SetValue("")
        self.ISBN.SetFocus()
    
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

class Patikrinti(wxformbuilder.Patikrinti):
    pass

class SideBar(wxformbuilder.SideBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        full_version=self.VersionAndBuild()
        self.versija.SetLabel(full_version)

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
                "Label": "CSV duomenu perkelimas"
            },
            {  
                "Class": SukurtiCSV,
                "Label": "CSV lenteles sukurimas"
            },
            {  
                "Class": IsKlaveturosSkaitytuvo,
                "Label": "Klavetūros / Skaitytuvo"
            },
            {  
                "Class": Patikrinti,
                "Label": "Google sheets lentėja"
            },
            {  
                "Class": Isdavimas,
                "Label": "Išdavimas"
            },
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
        

class Isdavimas(wxformbuilder.Isdavimas):
    pass