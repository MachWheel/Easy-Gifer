import PySimpleGUI as sg

import assets
from . import controls


def HEADING() -> sg.Text:
    pad = (10, 10), (20, 10)
    return sg.Text(
        assets.txt.SELECT_VIDEO,
        font=assets.style.F_14_B,
        p=pad
    )


def VIDEO_BROWSER() -> tuple:
    return (
        controls.BROWSE_BTN(),
        controls.VIDEO_INPUT(),
        controls.START_BTN()
    )

##################################################################################

def CONTROLS_ROW():
    layout = [
        [TRIM_FRAME()],
        [SPEED_FRAME(), controls.INFO_BTN()]
    ]
    return sg.Column(
        layout=layout,
        key='-CONTROLS_ROW-',
        size=(450, None),
        element_justification='center',
        vertical_alignment='center'
    )


def TRIM_FRAME() -> sg.Frame:
    sep = sg.HSep(pad=(5, 15), color=assets.style.BG_COLOR())
    layout = [
        [sg.VPush()],
        [*controls.START_TIME_INPUTS(), sg.Push()],
        [sep],
        [*controls.DURATION_SLIDER()],
        [sg.VPush()],
    ]
    return sg.Frame(
        title=assets.txt.TRIM,
        layout=layout,
        pad=(0, 15),
        relief=sg.RELIEF_RAISED,
        expand_x=True,
        element_justification='left',
        font=assets.style.F_11_B,
        size=(430, 130)
    )


def SPEED_FRAME() -> sg.Frame:
    return sg.Frame(
        title='Change speed?',
        layout=[controls.SPEED_SLIDER()],
        expand_x=True,
        expand_y=True,
        font=assets.style.F_11_B,
        relief=sg.RELIEF_RAISED,
        vertical_alignment='top',
        size=(375, 65),
        p=(5, 5)
    )


##################################################################################

def PROGRESS_BAR(bar_end: int):
    return [
        [sg.T(assets.txt.EXPORTING, key='-TXT-', font='Default 12 bold')],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color='#ff009b'
        )]
    ]
