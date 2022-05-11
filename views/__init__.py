import PySimpleGUI as sg

from ._gui import (
    MAIN_TEXT, MAIN_CONTROLS, TRIM_FRAME,
    SPEED_FRAME, INFO_BTN, txt, style
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
        [sg.Text(txt.EXPORTING, key='-TXT-', font='Default 12 bold')],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color='#ff009b'
        )]
    ]
    return sg.Window(txt.EXPORTING, layout, keep_on_top=True)


def INFO_POPUP():
    return sg.popup_yes_no(txt.INFO, font=style.F_14, no_titlebar=True)


def DONE_POPUP():
    return sg.popup_ok(txt.DONE, font=style.F_14, no_titlebar=True)


def ERROR_POPUP(msg: str):
    msg = f"\n{msg}\n"
    return sg.popup_error(msg, font=style.F_14)
