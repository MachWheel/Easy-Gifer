import PySimpleGUI as sg

from . import controls
from assets import txt, icons, style


def HEADING() -> sg.Text:
    pad = (10, 10), (20, 10)
    return sg.Text(
        txt.SELECT_VIDEO,
        font=style.F_14_B,
        p=pad
    )


def VIDEO_BROWSER() -> tuple:
    return (
        controls.BROWSE_BTN(),
        controls.VIDEO_INPUT(),
        controls.START_BTN()
    )


def TRIM_FRAME() -> sg.Frame:
    sep = sg.HSep(pad=(5, 15), color=style.BG_COLOR())
    layout = [
        [sg.VPush()],
        [*controls.TRIM_START_AT(), sg.Push()],
        [sep],
        [*controls.TRIM_DURATION_SLIDER()],
        [sg.VPush()],
    ]
    return sg.Frame(
        title=txt.TRIM,
        layout=layout,
        pad=(0, 15),
        relief=sg.RELIEF_RAISED,
        expand_x=True,
        element_justification='left',
        font=style.F_11_B
    )


def SPEED_FRAME() -> sg.Frame:
    return sg.Frame(
        title='Change speed?',
        layout=[controls.SPEED_SLIDER()],
        expand_x=True,
        expand_y=True,
        font=style.F_11_B,
        relief=sg.RELIEF_RAISED,
        vertical_alignment='top'
    )


def INFO() -> sg.Button:
    return sg.Button(
        image_data=icons.INFO(),
        button_color=style.BTN_COLOR(),
        border_width=0,
        key="-INFO_BTN-",
        enable_events=True
    )
