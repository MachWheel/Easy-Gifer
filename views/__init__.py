import PySimpleGUI as sg

from views._elements import (
    _MSG_FONT, _MAIN_TEXT, _BROWSE_BTN,
    _INPUT_VIDEO, _TRIM_FRAME, _SPEED_SLIDER,
    _INFO_BTN, _START_BTN
)
from views._labels import APP_TITLE
from views._msgs import DONE, INFO_HELP


def MAIN_WINDOW():
    return sg.Window(
        APP_TITLE,
        [
            [_MAIN_TEXT],
            [_BROWSE_BTN, _INPUT_VIDEO, _START_BTN],
            [_TRIM_FRAME],
            [*_SPEED_SLIDER, sg.VSep(p=(7, 0)), _INFO_BTN]

        ], finalize=True

    )


def INFO_POPUP():
    return sg.popup_yes_no(INFO_HELP,
                           font=_MSG_FONT,
                           no_titlebar=True)


def DONE_POPUP():
    return sg.popup_ok(DONE,
                       font=_MSG_FONT,
                       no_titlebar=True)


def PROGRESS_POPUP(bar_end=100):
    txt = 'Exporting GIF file...'
    layout = [
        [sg.Text(txt, key='-TXT-', font='Default 12 bold')],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color='#ff009b'
        )]
    ]
    return sg.Window('Exporting GIF file...', layout, keep_on_top=True)
