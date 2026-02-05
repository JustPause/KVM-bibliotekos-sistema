import csv
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import override

import wx

import src.gui.wxformbuilder as wxformbuilder
from src.barcode_generator import generator_barcodes, imiges_to_pdf
from src.config import Config
from src.google_sheets import (
    append_rows,
    get_all_data,
    get_sheet_rows,
    set_korteles_id,
    set_row_retruning_book,
    set_vardas,
)
from src.gui.wx_helpers.extra import (
    file_dialog_with_extension,
    ne_sekmingai,
    show_invalid_path_error,
)
from src.helpers.utils import (
    adding_colums_headers,
    from_dic_to_array,
    from_dic_to_array_add_catalog,
    get_fieldnames,
    get_fieldnames_extra,
)
from src.ibiblioteka_connection import iBibliotekos_paieska_tiesiogiai_core
from src.logger import logger
from src.os_helper import (
    get_correct_extension,
    git_build_number,
    is_file_empty,
    is_it_an_validate_path,
)
from src.threads import BackgroundWorker


class Pagrindinis(wxformbuilder.Pagrindinis):
    def __init__(self, parent):
        super().__init__(parent)
        self.Config = Config()

    @override
    def img_path(self, bitmap_path):
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        bitmap_path = os.path.join(base_path, "src", "gui", bitmap_path)

        return bitmap_path


class ISBNkoduAtspauzdinimas(wxformbuilder.ISBNkoduAtspauzdinimas):
    def __init__(self, parent):
        super().__init__(parent)
        self.Config = Config()
        ISBNkoduAtspauzdinimas = self.Config.get_user_data("ISNBkoduAtspauzdinimas")

        self.textCtrl1.SetValue(ISBNkoduAtspauzdinimas)

    @override
    def selecting_path(self, event) -> None:
        path = file_dialog_with_extension(self, "pdf", False)

        self.Config.set_user_data("ISNBkoduAtspauzdinimas", path)
        self.textCtrl1.SetValue(path)

    @override
    def next(self, event):
        rows = []

        path = self.textCtrl1.GetValue()

        for row in range(self.table.GetNumberRows()):
            value = self.table.GetCellValue(row, 0)

            if value != "":
                rows.append(value)

        worker = BackgroundWorker(self, "Ieškoma", "Kantrybės, ieškoma")

        if len(rows) != 0:
            worker.runBackgroundTesk(imiges_to_pdf, path, rows)
            show_invalid_path_error(self)
        else:
            ne_sekmingai("Parasykite bent viena eilute")


class KurtiNaujusBarkodus(wxformbuilder.KurtiNaujusBarkodus):
    def __init__(self, parent):
        super().__init__(parent)
        self.Config = Config()

        KurtiNaujusBarkodus = self.Config.get_user_data("kurtinaujusbarkodus")
        self.inputText1.SetValue(KurtiNaujusBarkodus)

    @override
    def selecting_path(self, event):
        path = file_dialog_with_extension(self, "pdf", False)

        self.Config.set_user_data("kurtinaujusbarkodus", path)
        self.inputText1.SetValue(path)

    @override
    def next(self, event):
        dest_path = self.inputText1.GetValue()
        count = self.inputText2.GetValue()

        worker = BackgroundWorker(self, "Ieškoma", "Kantrybės, ieškoma")

        try:
            worker.runBackgroundTesk(generator_barcodes, int(count), dest_path)
            show_invalid_path_error(self)
        except ValueError:
            ne_sekmingai("Kažkas nepavyko")


class IsCSV(wxformbuilder.IsCSV):
    def __init__(self, parent):
        super().__init__(parent)
        self.Config = Config()

        csviskur = self.Config.get_user_data("duomenuperkelimas")

        self.textCtrl1.SetValue(csviskur)

    @override
    def selecting_path(self, event):
        path = file_dialog_with_extension(self, "csv", False)

        self.Config.set_user_data("duomenuperkelimas", path)
        self.textCtrl1.SetValue(path)

    @override
    def next(self, event):
        path = self.textCtrl1.GetValue()
        worker = BackgroundWorker(self, "Ieškoma", "Kantrybės, ieškoma")
        if not is_it_an_validate_path(path):
            show_invalid_path_error()
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
            returnRows.append(from_dic_to_array(row))

        worker.runBackgroundTesk(append_rows, returnRows)

        show_invalid_path_error(self)


class SukurtiCSV(wxformbuilder.SukurtiCSV):
    def __init__(self, parent):
        super().__init__(parent)
        self.Config = Config()

        path = self.Config.get_user_data("lentelessukurimas")

        self.textCtrl1.SetValue(path)

    @override
    def selecting_path(self, event):
        path = file_dialog_with_extension(self, "csv", False)

        self.Config.set_user_data("lentelessukurimas", path)

        self.textCtrl1.SetValue(path)

    @override
    def next(self, event):
        path = self.textCtrl1.GetValue()

        path = get_correct_extension(path, ".csv")

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=get_fieldnames(), extrasaction="ignore"
            )
            writer.writeheader()

        show_invalid_path_error(self)


class IsKlaveturosSkaitytuvo(wxformbuilder.IsKlaveturosSkaitytuvo):
    def __init__(self, parent):
        super().__init__(parent)
        self.Config = Config()
        IsKlaveturosSkaitytuvo = self.Config.get_user_data("isklaveturosskaitytuvo")
        self.textCtrl1.SetValue(IsKlaveturosSkaitytuvo)

    def update_panel(self, catalog, path=None) -> None:
        parent = self.GetParent()
        if path is None:
            parent.replace_panel_catalog(IsKlaveturosSkaitytuvoEkranas, catalog)
        else:
            parent.replace_panel_catalog(IsKlaveturosSkaitytuvoEkranas, catalog, path)

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
    def selecting_path(self, event):
        path = file_dialog_with_extension(self, "csv", True)

        self.Config.set_user_data("isklaveturosskaitytuvo", path)
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
        adding_colums_headers(self.dataViewList)

    @override
    def enter(self, event):
        worker = BackgroundWorker(self, "Ieškoma", "Kantrybės, ieškoma")

        def paieska():
            return iBibliotekos_paieska_tiesiogiai_core(event.GetString())

        def on_pabaigimo(result):
            self.dataViewList.AppendItem(from_dic_to_array(result))

            if self.path:
                l_result = from_dic_to_array_add_catalog(result, self.catalog)
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

                        ne_sekmingai(
                            "Knygos nera, gerai butu padeti i sona kad poto surasyti"
                        )
                else:
                    r = append_rows([loc_result])
                    logger.info(r)
            else:
                r = append_rows([from_dic_to_array_add_catalog(result, self.catalog)])
                logger.info(r)

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

        adding_colums_headers(self.history_table)

    @override
    def enter(self, event):
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

                self.history_table.AppendItem(from_dic_to_array(edited_row))
        if not found:
            text = "Nerasta"
            self.autorius_output.SetLabel(text)
            self.pavadinimas_output.SetLabel(text)
            self.metai_output.SetLabel(text)
            self.isbn_output.SetLabel(text)
            self.katalogas_output.SetLabel(text)

        self.ISBN_window_input.SetValue("")
        self.ISBN_window_input.SetFocus()


class SideBar(wxformbuilder.SideBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        full_version = self.VersionAndBuild()
        self.versija.SetLabel(full_version)

    def VersionAndBuild(self):
        build = git_build_number()
        config = Config()
        version = config.get_default_data("version")

        return f"vesrija - {version}+{build}"

    def __PikingLable(self, Lable):
        CLASS_NAME_AND_LABLES = [
            {"Class": KurtiNaujusBarkodus, "Label": "Kurti naujus barkodus"},
            {
                "Class": ISBNkoduAtspauzdinimas,
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
    def click(self, event):
        btnLabel = event.GetEventObject().GetLabel()
        btnClickClass = self.__PikingLable(btnLabel)

        self.GetParent().replace_panel(btnClickClass)

        event.Skip()

    @override
    def version(self, event):
        import configparser

        config = configparser.ConfigParser()
        config.read("config/config.conf")
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
    def enter_isbn(self, event):
        KngosISBNInput = self.KngosISBNInput.GetValue()

        if KngosISBNInput == "":
            return

        manual_ISBN_input = True

        self.ShowInputBoxes(False)
        for index, row in enumerate(self.sheet_rows):
            if KngosISBNInput == row[self.filenames[3]]:
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
    def isduoti_button(self, event):
        if self.knygaData is None:
            self.knygaData = [
                self.AutoriusInput.GetValue(),
                self.PavadinimasInput.GetValue(),
                self.MetaiInput.GetValue(),
                self.ISBNInput.GetValue(),
            ]

            self.AutoriusInput.SetValue("")
            self.PavadinimasInput.SetValue("")
            self.MetaiInput.SetValue("")
            self.ISBNInput.SetValue("")

            if self.knygaData[1] == "":
                ne_sekmingai("Reikia bent pavadinimo")

                return
        # ---

        kortelesInput = self.KortelesInput.GetValue()

        if kortelesInput == "":
            kortelesInput = (
                self.VardasInput.GetValue() + " " + self.KlaseInput.GetValue()
            )

        # ---

        manual_User_input = not self.KortelesInput.Enabled

        # ---

        if self.row_id is not None:
            id = self.row_id + 2

            if manual_User_input:
                set_vardas(id, kortelesInput)
            else:
                set_korteles_id(id, kortelesInput)
        else:
            result = append_rows([self.knygaData])

            id = (
                result["updates"]["updatedRange"].split("!")[1].split(":")[0].strip("I")
            )

            if manual_User_input:
                set_vardas(id, kortelesInput)
            else:
                set_korteles_id(id, kortelesInput)

        self.knygaData = None
        self.row_id = None

        self.KngosISBNInput.SetValue("")
        self.KngosISBNRezult.SetLabel("")

        self.AutoriusInput.SetValue("")
        self.PavadinimasInput.SetValue("")
        self.MetaiInput.SetValue("")
        self.ISBNInput.SetValue("")

        show_invalid_path_error(self)
        # if KortelesData is Valid && ISBNData is Valid
        # -> append data
        # -> Sentd to google sheet

    @override
    def pakeisti_button(self, event):
        if self.KortelesInput.Enabled:
            self.KortelesInput.SetValue("")

            self.KortelesInput.Enable(False)

            self.VardasInput.Enable(True)
            self.KlaseInput.Enable(True)

            self.VardasLable.Enable(True)
            self.KlaseLable.Enable(True)

        else:
            self.VardasInput.SetValue("")
            self.KlaseInput.SetValue("")

            self.KortelesInput.Enable(True)

            self.VardasInput.Enable(False)
            self.KlaseInput.Enable(False)

            self.VardasLable.Enable(False)
            self.KlaseLable.Enable(False)


class Grazinimas(wxformbuilder.Gazinimas):
    def __init__(self, parent):
        super().__init__(parent)
        self.data = get_all_data()
        self.l_index = None

    @override
    def enter(self, event):
        knygos = self.KnygosInput.GetValue()

        bookName = None
        userName = None

        for index, row in enumerate(self.data):
            if knygos == row[3]:
                self.l_index = index + 2
                bookName = row[1]
                userName = row[9]

        self.KnygosStaticText.SetLabel(bookName)
        self.NaudotojoStaticText.SetLabel(userName)

    @override
    def next(self, event):
        set_row_retruning_book(self.l_index)
        show_invalid_path_error(self)


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
