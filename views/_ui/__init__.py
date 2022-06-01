import PySimpleGUI as sg

from . import controls
import assets


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


def TRIM_FRAME() -> sg.Frame:
    sep = sg.HSep(pad=(5, 15), color=assets.style.BG_COLOR())
    layout = [
        [sg.VPush()],
        [*controls.TRIM_START_AT(), sg.Push()],
        [sep],
        [*controls.TRIM_DURATION_SLIDER()],
        [sg.VPush()],
    ]
    return sg.Frame(
        title=assets.txt.TRIM,
        layout=layout,
        pad=(0, 15),
        relief=sg.RELIEF_RAISED,
        expand_x=True,
        element_justification='left',
        font=assets.style.F_11_B
    )


def SPEED_FRAME() -> sg.Frame:
    return sg.Frame(
        title='Change speed?',
        layout=[controls.SPEED_SLIDER()],
        expand_x=True,
        expand_y=True,
        font=assets.style.F_11_B,
        relief=sg.RELIEF_RAISED,
        vertical_alignment='top'
    )


def INFO() -> sg.Button:
    return sg.Button(
        image_data=assets.icons.INFO(),
        button_color=assets.style.BTN_COLOR(),
        border_width=0,
        key="-INFO_BTN-",
        enable_events=True
    )

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
