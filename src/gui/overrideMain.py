import csv
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import override

import wx

import src.gui.wxformbuilder as wxformbuilder
from src.barcodeKurimas import barcode_generator
from src.googleSheets import append_rows, get_sheet_rows
from src.gui.config import ConfigFile
from src.helpers.utils import get_fieldnames,fromDicToArray
from src.ibibliotekaConnection import iBibliotekos_paieska_tiesiogiai_core
from src.ISBNPrint import form_buffer_to_pdf
from src.osHelper import get_correct_extension, git_build_number, is_it_an_validate_path
from src.threads import BackgroundWorker


def NeSekmingai(text) -> None:
    wx.MessageBox(text, "Rezultatas", wx.OK | wx.ICON_INFORMATION)


def Sekmingai() -> None:
    wx.MessageBox("Sėkmingai pavyko", "Rezultatas", wx.OK | wx.ICON_INFORMATION)


def KlaidingasTakas() -> None:
    wx.MessageBox(
        "Ar failas tikrai tenais?",
        "Klaidingas failo takas",
        wx.ICON_WARNING | wx.OK,
    )


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
    def __init__(self, parent, title="Good Name"):
        super().__init__(parent, title=title, size=(250, 150))

        panel = wx.Panel(self)

        self.label = wx.StaticText(
            panel,
            label="Please wait...",
            pos=(25, 20),
        )

        self.gauge = wx.Gauge(
            panel,
            range=100,
            size=(200, 20),
            pos=(25, 60),
        )


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

        path = self.textCtrl1.GetValue()
        if not is_it_an_validate_path(path):
            KlaidingasTakas()
            return

        for row in range(self.table.GetNumberRows()):
            value = self.table.GetCellValue(row, 0)

            if value != "":
                rows.append(value)

        if len(rows) != 0:
            form_buffer_to_pdf(rows, path)
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

        if not is_it_an_validate_path(dest_path):
            KlaidingasTakas()
            return

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

        if not is_it_an_validate_path(path):
            KlaidingasTakas()
            return

        rows = None

        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        sheet_rows = get_sheet_rows()
        fieldnames = get_fieldnames()

        returnRows = []

        for row in rows:
            for index, sheet_row in enumerate(sheet_rows):
                if row[fieldnames[1]] == sheet_row[fieldnames[1]]:
                    tmp_index = index + 2

                    dlg = PromptForReplacementDialog(self, sheet_row, row)
                    print(str(tmp_index) + " - " + row[fieldnames[1]])

                    dlg.ShowModal()

                    row = ["Update", "Update", "Update", "Update"]
                    break
            returnRows.append(fromDicToArray(row))

        # print(returnRows)
        # print([[1, 2, 3, 4], [5, 6, 7, 8]])

        request=append_rows([[1, 2, 3, 4], [5, 6, 7, 8]])

        print(request)


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

        if not is_it_an_validate_path(path):
            KlaidingasTakas()
            return

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

    def update_panel(self, catalog, path=None) -> None:
        parent = self.GetParent()
        if path is None:
            parent.ReplacePanelNext(IsKlaveturosSkaitytuvoEkranas, catalog)
        else:
            parent.ReplacePanelNext(IsKlaveturosSkaitytuvoEkranas, catalog, path)

    @override
    def file_free_scan(self, event):
        catalog = self.textCtrl2.GetValue()
        wx.CallAfter(self.update_panel, catalog)

        event.Skip()

    @override
    def next(self, event):
        path = self.textCtrl1.GetValue()
        catalog = self.textCtrl2.GetValue()

        if not is_it_an_validate_path(path):
            KlaidingasTakas()
            return

        wx.CallAfter(self.update_panel, catalog, path)
        event.Skip()

    @override
    def SelectingPath(self, event):
        path = FileDialogWithExtesion(self, "csv")

        self.configFile.setUserData("isklaveturosskaitytuvo", path)
        self.textCtrl1.SetValue(path)


class IsKlaveturosSkaitytuvoEkranas(wxformbuilder.IsKlaveturosSkaitytuvoEkranas):
    def __init__(
        self,
        parent,
        catalog,
        path=None,
    ):
        super().__init__(parent)
        self.catalog = catalog
        self.path = path
        self.addingColumsHeaders(self.dataViewList)

    @override
    def Enter(self, event):
        worker = BackgroundWorker(self, "Searching", "Please wait...")

        def paieska():
            return iBibliotekos_paieska_tiesiogiai_core(event.GetString())

        def on_pabaigimo(result):
            fieldnames = get_fieldnames()

            self.dataViewList.AppendItem(
                [
                    result[fieldnames[0]],
                    result[fieldnames[1]],
                    result[fieldnames[2]],
                    result[fieldnames[3]],
                ]
            )

            append_rows(
                [
                    [
                        result[fieldnames[0]],
                        result[fieldnames[1]],
                        result[fieldnames[2]],
                        result[fieldnames[3]],
                        self.catalog,
                    ]
                ]
            )

        worker.run(work_func=paieska, on_done=on_pabaigimo)

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
    def __init__(self, parent):
        super().__init__(parent)
        self.executor = ThreadPoolExecutor()
        self.rows_promise = self.executor.submit(get_sheet_rows)


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
            {"Class": ISNBkoduAtspauzdinimas, "Label": "ISBN kodu atspauždinimas"},
            {"Class": IsCSV, "Label": "CSV duomenu perkelimas"},
            {"Class": SukurtiCSV, "Label": "CSV lenteles sukurimas"},
            {"Class": IsKlaveturosSkaitytuvo, "Label": "Klaviatūros / Skaitytuvo"},
            {"Class": Patikrinti, "Label": "Google sheets lentėje"},
            {"Class": Isdavimas, "Label": "Išdavimas"},
            {"Class": Grazinimas, "Label": "Grąžinimas"},
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
