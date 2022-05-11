import PySimpleGUI as sg

from ._elements import (
    MAIN_TEXT, TRIM_FRAME, SPEED_FRAME,
    INFO_BTN, MAIN_CONTROLS
)
from ._labels import APP_TITLE
from ._msgs import DONE_MSG, INFO_MSG, EXPORTING_MSG
from ._style import F_14


def MAIN_WINDOW():
    return sg.Window(
        APP_TITLE,
        [
            [MAIN_TEXT()],
            [*MAIN_CONTROLS()],
            [TRIM_FRAME()],
            [SPEED_FRAME(), INFO_BTN()]
        ], finalize=True
    )


def PROGRESS_POPUP(bar_end=100):
    layout = [
        [sg.Text(EXPORTING_MSG, key='-TXT-', font='Default 12 bold')],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color='#ff009b'
        )]
    ]
    return sg.Window(EXPORTING_MSG, layout, keep_on_top=True)


def INFO_POPUP():
    return sg.popup_yes_no(INFO_MSG, font=F_14, no_titlebar=True)


def DONE_POPUP():
    return sg.popup_ok(DONE_MSG, font=F_14, no_titlebar=True)


def ERROR_POPUP(msg: str):
    msg = f"\n{msg}\n"
    return sg.popup_error(msg, font=F_14)
