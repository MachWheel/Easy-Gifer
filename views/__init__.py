import PySimpleGUI as sg

from . import _ui
import assets


def MAIN_WINDOW():
    return sg.Window(
        assets.txt.APP_TITLE,
        [
            [_ui.HEADING()],
            [*_ui.VIDEO_BROWSER()],
            [_ui.TRIM_FRAME()],
            [_ui.SPEED_FRAME(), _ui.INFO()]
        ], finalize=True, icon=assets.icons.LOGO()
    )


def PROGRESS_POPUP(bar_end=100):
    layout = [
        [sg.T(assets.txt.EXPORTING, key='-TXT-', font='Default 12 bold')],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color='#ff009b'
        )]
    ]
    return sg.Window(
        title=assets.txt.EXPORTING,
        layout=layout,
        keep_on_top=True,
        icon=assets.icons.LOGO()
    )


def INFO_POPUP():
    return sg.popup_yes_no(
        assets.txt.INFO,
        font=assets.style.F_14,
        no_titlebar=True,
        keep_on_top=True,
        icon=assets.icons.LOGO()
    )


def DONE_POPUP():
    return sg.popup_ok(
        assets.txt.DONE,
        font=assets.style.F_14,
        no_titlebar=True,
        keep_on_top=True,
        icon=assets.icons.LOGO()
    )


def ERROR_POPUP(msg: str):
    msg = f"\n{msg}\n"
    return sg.popup_error(
        msg,
        font=assets.style.F_14,
        keep_on_top=True,
        icon=assets.icons.LOGO()
    )
