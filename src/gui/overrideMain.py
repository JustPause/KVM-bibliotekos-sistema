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
from src.helpers.utils import (
    addingColumsHeaders,
    fromDicToArray,
    fromDicToArrayAddCatalog,
    get_fieldnames,
    get_fieldnames_extra,
)
from src.ibibliotekaConnection import iBibliotekos_paieska_tiesiogiai_core
from src.ISBNPrint import form_buffer_to_pdf
from src.osHelper import (
    get_correct_extension,
    get_correct_extension_ending,
    git_build_number,
    is_file_empty,
    is_it_an_validate_path,
)
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

            path = get_correct_extension_ending(path, extension)

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
        path = FileDialogWithExtesion(self, "pdf", False)

        self.configFile.setUserData("ISNBkoduAtspauzdinimas", path)
        self.textCtrl1.SetValue(path)

    @override
    def next(self, event):
        rows = []

        path = self.textCtrl1.GetValue()

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
        path = FileDialogWithExtesion(self, "pdf", False)

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
    def SelectingPath(self, event):
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

        with open(path, "r", newline="", encoding="UTF-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        sheet_rows = get_sheet_rows()
        fieldnames = get_fieldnames()

        returnRows = []

        for row in rows:
            for index, sheet_row in enumerate(sheet_rows):
                if "Kodas" in sheet_row:
                    sheet_row["isbn"] = sheet_row.pop("Kodas")

                if row[fieldnames[1]] == sheet_row[fieldnames[1]]:
                    # tmp_index = index + 2

                    pfrd = PromptForReplacementDialog(
                        self, old_row=sheet_row, new_row=row
                    )

                    pfrd.ShowModal()

                    row = {
                        "Autorius": "---",
                        "Pavadinimas": "---",
                        "Metai": "---",
                        "isbn": "---",
                    }
                    break
            returnRows.append(fromDicToArray(row))

        request = append_rows(returnRows)

        print(request)


class SukurtiCSV(wxformbuilder.SukurtiCSV):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()

        csvikur = self.configFile.getUserData("lentelessukurimas")

        self.textCtrl1.SetValue(csvikur)

    @override
    def SelectingPath(self, event):
        path = FileDialogWithExtesion(self, "csv", False)

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

        Sekmingai()


class IsKlaveturosSkaitytuvo(wxformbuilder.IsKlaveturosSkaitytuvo):
    def __init__(self, parent):
        super().__init__(parent)
        self.configFile = ConfigFile()
        IsKlaveturosSkaitytuvo = self.configFile.getUserData("isklaveturosskaitytuvo")
        self.textCtrl1.SetValue(IsKlaveturosSkaitytuvo)

    def update_panel(self, catalog, path=None) -> None:
        parent = self.GetParent()
        if path is None:
            parent.ReplacePanelCatalog(IsKlaveturosSkaitytuvoEkranas, catalog)
        else:
            parent.ReplacePanelCatalog(IsKlaveturosSkaitytuvoEkranas, catalog, path)

    @override
    def file_free_scan(self, event):
        catalog = self.textCtrl2.GetValue()
        wx.CallAfter(self.update_panel, catalog)

        event.Skip()

    @override
    def next(self, event):
        path = self.textCtrl1.GetValue()
        catalog = self.textCtrl2.GetValue()

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
        addingColumsHeaders(self.dataViewList)

    @override
    def Enter(self, event):
        worker = BackgroundWorker(self, "Ieskoma", "Kantrybes, ieskoma")

        def paieska():
            return iBibliotekos_paieska_tiesiogiai_core(event.GetString())

        def on_pabaigimo(result):
            self.dataViewList.AppendItem(fromDicToArray(result))

            if self.path:
                l_result = fromDicToArrayAddCatalog(result, self.catalog)
                loc_result = l_result

                if (
                    l_result[0] == "---"
                    and l_result[1] == "---"
                    and l_result[2] == "---"
                ):
                    fieldnames = get_fieldnames()

                    with open(self.path, "a", newline="", encoding="utf-8") as f:
                        writer = csv.DictWriter(
                            f, fieldnames=fieldnames, extrasaction="ignore"
                        )

                        if is_file_empty(self.path):
                            writer.writeheader()
                        writer.writerow(
                            {
                                fieldnames[0]: "",
                                fieldnames[1]: "",
                                fieldnames[2]: "",
                                fieldnames[3]: l_result[3],
                            }
                        )

                        NeSekmingai(
                            "Knygos nera, gerai butu padeti i sona kad poto surasyti"
                        )
                else:
                    append_rows([loc_result])
            else:
                append_rows([fromDicToArrayAddCatalog(result, self.catalog)])

        worker.run(work_func=paieska, on_done=on_pabaigimo)

        self.ISBN.SetValue("")
        self.ISBN.SetFocus()


class Patikrinti(wxformbuilder.Patikrinti):
    def __init__(self, parent):
        super().__init__(parent)
        self.executor = ThreadPoolExecutor()
        # self.rows_promise = self.executor.submit(get_sheet_rows)
        self.sheet_rows = get_sheet_rows(True)
        self.fieldnames = get_fieldnames()

        addingColumsHeaders(self.history_table)

    @override
    def Enter(self, event):
        isbn = self.ISBN_window_input.GetValue()
        found = False

        for row in self.sheet_rows:
            if row["Kodas"] == isbn:
                found = True
                edited_row = dict(row)
                edited_row["isbn"] = edited_row.pop("Kodas")

                fieldnames_extra = get_fieldnames_extra()

                self.autorius_output.SetLabel(edited_row[fieldnames_extra[0]])
                self.pavadinimas_output.SetLabel(edited_row[fieldnames_extra[1]])
                self.metai_output.SetLabel(edited_row[fieldnames_extra[2]])
                self.isbn_output.SetLabel(edited_row[fieldnames_extra[3]])
                self.katalogas_output.SetLabel(edited_row[fieldnames_extra[4]])

                edited_row.pop("Kategorija")

                self.history_table.AppendItem(fromDicToArray(edited_row))
        if not found:
            text = "Nerasta"
            self.autorius_output.SetLabel(text)
            self.pavadinimas_output.SetLabel(text)
            self.metai_output.SetLabel(text)
            self.isbn_output.SetLabel(text)
            self.katalogas_output.SetLabel("TODO")

        self.ISBN_window_input.SetValue("")
        self.ISBN_window_input.SetFocus()


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
            {
                "Class": ISNBkoduAtspauzdinimas,
                "Label": "ISBN kodu atspauždinimas",
            },
            {"Class": IsCSV, "Label": "CSV duomenu perkelimas"},
            {"Class": SukurtiCSV, "Label": "CSV lenteles sukurimas"},
            {
                "Class": IsKlaveturosSkaitytuvo,
                "Label": "Klaviatūros / Skaitytuvo",
            },
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
    def __init__(self, parent):
        super().__init__(parent)
        self.sheet_rows = get_sheet_rows()
        self.filenames = list(self.sheet_rows[0].keys())

        self.knygaData = None
        self.row_id = None

    def ShowInputBoxes(self, bool: bool):
        self.AutoriusLable.Show(bool)
        self.AutoriusInput.Show(bool)

        self.PavadinimasLable.Show(bool)
        self.PavadinimasInput.Show(bool)

        self.MetaiLable.Show(bool)
        self.MetaiInput.Show(bool)

        self.ISBNLable.Show(bool)
        self.ISBNInput.Show(bool)

    @override
    def EnterISBN(self, event):
        KngosISBNInput = self.KngosISBNInput.GetValue()

        manual_ISBN_input = True
        manual_User_input = False

        self.ShowInputBoxes(False)

        for index, row in enumerate(self.sheet_rows):
            if KngosISBNInput in row[self.filenames[3]]:
                self.KngosISBNRezult.SetLabel(
                    "Surasta knyga" + " " + row[self.filenames[1]]
                )
                self.KngosISBNRezult.Show(True)
                self.Layout()
                self.knygaData = row
                manual_ISBN_input = False
                self.row_id = index
                break

        if manual_ISBN_input:
            self.knygaData = None

            self.KngosISBNRezult.SetLabel("Nesekminga")
            self.KngosISBNRezult.Show(True)

            self.ShowInputBoxes(True)

            self.Layout()

    @override
    def Isduoti_button(self, event):
        if self.knygaData is None:
            self.knygaData = [
                self.AutoriusInput.GetValue(),
                self.PavadinimasInput.GetValue(),
                self.MetaiInput.GetValue(),
                self.ISBNInput.GetValue(),
            ]

        # ---

        korelesInput = self.KorelesInput.GetValue()

        if korelesInput == "":
            print("manual")
            korelesInput = (
                self.VardasInput.GetValue() + " " + self.KlaseInput.GetValue()
            )

        # ---

        manual_User_input = not self.KorelesInput.Enabled

        # ---

        if self.row_id is not None:
            id = self.row_id + 2
            print("lenteles id: " + str(id))
            print(self.knygaData)

            print(
                "Gavejas: "
                + korelesInput
                + " "
                + "Manual input: "
                + str(manual_User_input)
            )
        else:
            print("Prideti knyga")
            print(self.knygaData)

            print(
                "Gavejas: "
                + korelesInput
                + " "
                + "Manual input: "
                + str(manual_User_input)
            )

        # if KortelesData is Valid && ISBNData is Valid
        # -> append data
        # -> Sentd to google sheet

    @override
    def Pakeisti_button(self, event):
        if self.KorelesInput.Enabled:
            self.KorelesInput.SetValue("")

            self.KorelesInput.Enable(False)

            self.VardasInput.Enable(True)
            self.KlaseInput.Enable(True)
        else:
            self.VardasInput.SetValue("")
            self.KlaseInput.SetValue("")

            self.KorelesInput.Enable(True)

            self.VardasInput.Enable(False)
            self.KlaseInput.Enable(False)


class Grazinimas(wxformbuilder.Gazinimas):
    def __init__(self, parent):
        super().__init__(parent)


class PromtForReplacment(wxformbuilder.PromtForReplacment):
    def __init__(self, parent, old_row, new_row):
        super().__init__(parent)

        fieldnames = get_fieldnames()

        self.old_text_autorius.SetLabel(old_row[fieldnames[0]])
        self.old_text_pavadinimas.SetLabel(old_row[fieldnames[1]])
        self.old_text_metai.SetLabel(old_row[fieldnames[2]])
        self.old_text_isbn.SetLabel(old_row[fieldnames[3]])

        self.new_text_autorius.SetLabel(new_row[fieldnames[0]])
        self.new_text_pavadinimas.SetLabel(new_row[fieldnames[1]])
        self.new_text_metai.SetLabel(new_row[fieldnames[2]])
        self.new_text_isbn.SetLabel(new_row[fieldnames[3]])


class PromptForReplacementDialog(wx.Dialog):
    def __init__(self, parent, old_row, new_row):
        super().__init__(
            parent,
            title="Replace existing row?",
            style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP,
        )

        panel = PromtForReplacment(self, old_row, new_row)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizerAndFit(sizer)
