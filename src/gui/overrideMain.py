import csv
import os
import sys
import src.gui.wxformbuilder as wxformbuilder
import wx

from typing import override
from src.barcodeKurimas import barcode_generator
from src.googleSheets import get_sheet_rows
from src.gui.config import ConfigFile
from src.helpers.utils import get_fieldnames
from src.ibibliotekaConnection import iBibliotekos_paieska_tiesiogiai_core
from src.ISBNPrint import form_buffer_to_pdf
from src.osHelper import get_correct_extension, git_build_number


def NeSekmingai(text):
    wx.MessageBox(text, "Rezultatas", wx.OK | wx.ICON_INFORMATION)


def Sekmingai():
    wx.MessageBox("Sėkmingai pavyko", "Rezultatas", wx.OK | wx.ICON_INFORMATION)


def FileDialogWithExtesion(self, extension, overwrite=True):
    path = ""

    with wx.FileDialog(
        self,
        "Pasirinkite lokaciją",
        wildcard=f"Lentelė (*.{extension})|*.{extension}",
        style=wx.FD_SAVE | (wx.FD_OVERWRITE_PROMPT if overwrite else 0),
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

    @override
    def img_path(self, bitmap_path):
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        bitmap_path = os.path.join(base_path, "src", "gui", bitmap_path)

        return bitmap_path


class ISNBkoduAtspauzdinimas(wxformbuilder.ISNBkoduAtspauzdinimas):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()
        ISNBkoduAtspauzdinimas = self.configFile.getUserData("ISNBkoduAtspauzdinimas")

        self.textCtrl1.SetValue(ISNBkoduAtspauzdinimas)

    @override
    def SelectingPath(self, event) -> None:
        path = FileDialogWithExtesion(self, "pdf")

        self.configFile.setUserData("isnbkoduatspauzdinimas", path)
        self.textCtrl1.SetValue(path)

    @override
    def next(self, event):
        rows = []

        for row in range(self.table.GetNumberRows()):
            value = self.table.GetCellValue(row, 0)

            if value != "":
                rows.append(value)

        if len(rows) != 0:
            form_buffer_to_pdf(rows, self.textCtrl1.GetValue())
            Sekmingai()
        else:
            NeSekmingai("Parasykite bent viena eilute")


class KurtiNaujusBarkodus(wxformbuilder.KurtiNaujusBarkodus):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()

        KurtiNaujusBarkodus = self.configFile.getUserData("kurtinaujusbarkodus")

        self.inputText1.SetValue(KurtiNaujusBarkodus)

    @override
    def SelectingPath(self, event):
        path = FileDialogWithExtesion(self, "pdf")

        self.configFile.setUserData("kurtinaujusbarkodus", path)
        self.inputText1.SetValue(path)

    @override
    def next(self, event):
        dest_path = self.inputText1.GetValue()
        count = self.inputText2.GetValue()

        try:
            barcode_generator(int(count), dest_path)
            Sekmingai()
        except ValueError:
            NeSekmingai("Kažkas nepavyko")

        event.Skip()


class IsCSV(wxformbuilder.IsCSV):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()

        csviskur = self.configFile.getUserData("duomenuperkelimas")

        self.textCtrl1.SetValue(csviskur)

    @override
    def SelectingPathDuomenuPerkelimas(self, event):
        path = FileDialogWithExtesion(self, "csv", False)

        self.configFile.setUserData("duomenuperkelimas", path)
        self.textCtrl1.SetValue(path)

    @override
    def next(self, event):
        path = self.textCtrl1.GetValue()
        rows = None

        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        print(rows)
        sheet_rows = get_sheet_rows()
        fieldnames = get_fieldnames()

        for row in rows:
            for index, sheet_row in enumerate(sheet_rows):
                if row[fieldnames[1]] == sheet_row[fieldnames[1]]:
                    tmp_index = index + 2

                    dlg = PromptForReplacementDialog(self, sheet_row, row)
                    print(str(tmp_index) + " - " + row[fieldnames[1]])

                    dlg.ShowModal()
                    # dlg.Destroy()

        print("DONE")
        # request=append_rows([[1,2,3,4],[5,6,7,8]])

        # print(request)


class SukurtiCSV(wxformbuilder.SukurtiCSV):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()

        csvikur = self.configFile.getUserData("lentelessukurimas")

        self.textCtrl1.SetValue(csvikur)

    def SelectingPathKur(self, event):
        path = FileDialogWithExtesion(self, "pdf")

        self.configFile.setUserData("lentelessukurimas", path)

    @override
    def next(self, event):
        path = self.textCtrl1.GetValue()

        path = get_correct_extension(path, ".csv")

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=get_fieldnames(), extrasaction="ignore"
            )
            writer.writeheader()


class IsKlaveturosSkaitytuvo(wxformbuilder.IsKlaveturosSkaitytuvo):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()
        IsKlaveturosSkaitytuvo = self.configFile.getUserData("kurtinaujusbarkodus")
        self.textCtrl1.SetValue(IsKlaveturosSkaitytuvo)

    def update_panel(self ,path=None) -> None:
        parent = self.GetParent()
        if path is None:
            parent.ReplacePanelNext(IsKlaveturosSkaitytuvoEkranas)
        else:
            parent.ReplacePanelNext(IsKlaveturosSkaitytuvoEkranas, path)

    @override
    def file_free_scan(self, event):
        wx.CallAfter(self.update_panel)

        event.Skip()

    @override
    def next(self, event):
        path = self.textCtrl1.GetValue()

        wx.CallAfter(self.update_panel, path)
        event.Skip()

    @override
    def SelectingPath(self, event):
        path = FileDialogWithExtesion(self, "csv")

        self.configFile.setUserData("isklaveturosskaitytuvo", path)
        self.textCtrl1.SetValue(path)


class IsKlaveturosSkaitytuvoEkranas(wxformbuilder.IsKlaveturosSkaitytuvoEkranas):
    def __init__(self, parent, path=None):
        super().__init__(parent)

        self.path = path

        self.addingColumsHeaders(self.dataViewList)

    @override
    def Enter(self, event):
        loud = ThinkingDialog(self)
        loud.Show()

        data = iBibliotekos_paieska_tiesiogiai_core(event.GetString())

        loud.Destroy()

        fieldnames = get_fieldnames()

        self.dataViewList.AppendItem(
            [
                data[fieldnames[0]],
                data[fieldnames[1]],
                data[fieldnames[2]],
                data[fieldnames[3]],
            ]
        )

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

        full_version = self.VersionAndBuild()
        self.versija.SetLabel(full_version)

    def VersionAndBuild(self):
        import configparser

        build = git_build_number()
        config = configparser.ConfigParser()
        config.read("config.conf")
        version = config["DEFAULT"]["version"]

        return f"vesrija - {version}+{build}"

    def __PikingLable(self, Lable):
        CLASS_NAME_AND_LABLES = [
            {"Class": KurtiNaujusBarkodus, "Label": "Kurti naujus barkodus"},
            {"Class": ISNBkoduAtspauzdinimas, "Label": "ISNB kodu atspauzdinimas"},
            {"Class": IsCSV, "Label": "CSV duomenu perkelimas"},
            {"Class": SukurtiCSV, "Label": "CSV lenteles sukurimas"},
            {"Class": IsKlaveturosSkaitytuvo, "Label": "Klavetūros / Skaitytuvo"},
            {"Class": Patikrinti, "Label": "Google sheets lentėja"},
            {"Class": Isdavimas, "Label": "Išdavimas"},
            {"Class": Grazinimas, "Label": "Sugrazinimas"},
        ]

        for classlable in CLASS_NAME_AND_LABLES:
            if classlable["Label"] == Lable:
                return classlable["Class"]

        return None

    @override
    def Click(self, event):
        btnLabel = event.GetEventObject().GetLabel()
        btnClickClass = self.__PikingLable(btnLabel)
        
        self.GetParent().ReplacePanel(btnClickClass)
        
        event.Skip()

    @override
    def version(self, event):
        import configparser

        config = configparser.ConfigParser()
        config.read("config.conf")
        developer = config["helpMessige"]["developer"]
        email = config["helpMessige"]["email"]
        repoURL = config["helpMessige"]["repoURL"]
        wx.MessageBox(
            "Programa sukurė: "
            + developer
            + "\nMane galite pasiekti: "
            + email
            + "\nRepositorjia turetu buti: "
            + repoURL,
            "Programuotojo kontaktai",
            wx.OK | wx.ICON_INFORMATION,
        )


class Isdavimas(wxformbuilder.Isdavimas):
    pass


class Grazinimas(wxformbuilder.Gazinimas):
    pass


class PromptForReplacementDialog(wx.Dialog):
    def __init__(self, parent, sheet_row, row):
        super().__init__(
            parent,
            title="Replace existing row?",
            style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP,
        )

        panel = wxformbuilder.PromtForReplacment(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizerAndFit(sizer)
