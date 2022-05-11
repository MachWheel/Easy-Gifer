import PySimpleGUI as sg

import views._gui.style
import views._gui.txt
from ._gui import (
    MAIN_TEXT, MAIN_CONTROLS, TRIM_FRAME,
    SPEED_FRAME, INFO_BTN, fonts, txt, msgs, style
)


def MAIN_WINDOW():
    return sg.Window(
        txt.APP_TITLE,
        [
            [MAIN_TEXT()],
            [*MAIN_CONTROLS()],
            [TRIM_FRAME()],
            [SPEED_FRAME(), INFO_BTN()]
        ], finalize=True
    )


def PROGRESS_POPUP(bar_end=100):
    layout = [
        [sg.Text(views._gui.txt.EXPORTING, key='-TXT-', font='Default 12 bold')],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color='#ff009b'
        )]
    ]
    return sg.Window(views._gui.txt.EXPORTING, layout, keep_on_top=True)


def INFO_POPUP():
    return sg.popup_yes_no(views._gui.txt.INFO, font=views._gui.style.F_14, no_titlebar=True)


def DONE_POPUP():
    return sg.popup_ok(views._gui.txt.DONE, font=views._gui.style.F_14, no_titlebar=True)


def ERROR_POPUP(msg: str):
    msg = f"\n{msg}\n"
    return sg.popup_error(msg, font=views._gui.style.F_14)
