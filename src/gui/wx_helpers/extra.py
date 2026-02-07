import os

import wx

from src.etc.os_helper import get_correct_extension_ending


def show_error_dialog(text) -> None:
    wx.MessageBox(text, "Rezultatas", wx.OK | wx.ICON_INFORMATION)


def show_success(parent) -> None:
    """Display success message."""
    wx.MessageBox("Sėkmingai pavyko", "Rezultatas", wx.OK | wx.ICON_INFORMATION, parent)
    parent.SetFocus


def show_invalid_path_error() -> None:
    """Display warning for invalid file path."""
    wx.MessageBox(
        "Ar failas tikrai ten?",
        "Klaidingas failo takas",
        wx.ICON_WARNING | wx.OK,
    )


def file_dialog_with_extension(
    self,
    extension: str,
    old_path: str,
    overwrite: bool,
) -> str:
    """
    Opens a file save dialog and returns the selected path with correct extension.

    Args:
        extension: File extension without the dot (e.g., 'csv')
        old_path: Path to return if dialog is cancelled
        overwrite: Whether to prompt on overwrite

    Returns:
        Selected file path or old_path if cancelled
    """
    style = wx.FD_SAVE
    if overwrite:
        style |= wx.FD_OVERWRITE_PROMPT

    with wx.FileDialog(
        self,
        "Pasirinkite lokaciją",
        wildcard=f"Lentelė (*.{extension})|*.{extension}",
        style=style,
    ) as dlg:
        if dlg.ShowModal() == wx.ID_OK:
            return get_correct_extension_ending(dlg.GetPath(), extension)

    return old_path
