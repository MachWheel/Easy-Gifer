import PySimpleGUI as sg

from . import _icons
from ._labels import (
    START_TOOLTIP, BROWSE_TOOLTIP,
    SELECT_VIDEO, START_AT, DURATION,
    SPEED_DISPLAY, TRIM, DEFAULT_DURATION
)
from ._style import (
    F_14, F_14_B, F_11_B, F_9_B, APP_THEME
)

sg.theme(APP_THEME)
BTN_COLOR = sg.theme_background_color(), sg.theme_background_color()

def MAIN_TEXT() -> sg.Text:
    pad = (10, 10), (20, 10)
    return sg.Text(SELECT_VIDEO, font=F_14_B, p=pad)


def MAIN_CONTROLS() -> tuple:
    BROWSE_BTN = sg.Button(
        button_type=sg.BUTTON_TYPE_BROWSE_FILE,
        image_data=_icons.FOLDER(),
        button_color=BTN_COLOR,
        border_width=0,
        target='-VIDEO_IN-',
        tooltip=BROWSE_TOOLTIP
    )
    INPUT_VIDEO = sg.Input(
        k='-VIDEO_IN-',
        size=(30, 4),
        expand_x=True,
        font=F_14
    )
    START_BTN = sg.Button(
        button_type=sg.BUTTON_TYPE_READ_FORM,
        image_data=_icons.START(),
        button_color=BTN_COLOR,
        border_width=0,
        tooltip=START_TOOLTIP,
        key="-START_BTN-"
    )
    return BROWSE_BTN, INPUT_VIDEO, START_BTN


def TRIM_FRAME() -> sg.Frame:
    sep = sg.HSep(p=(5, 15), color=sg.theme_background_color())
    layout = [
        [sg.VPush()],
        [*_TRIM_START_AT(), sg.Push()],
        [sep],
        [*_TRIM_DURATION_SLIDER()],
        [sg.VPush()],
    ]
    return sg.Frame(
        title=TRIM,
        layout=layout,
        pad=(0, 15),
        relief=sg.RELIEF_RAISED,
        expand_x=True,
        element_justification='left',
        font=F_11_B
    )


def SPEED_FRAME() -> sg.Frame:
    return sg.Frame(
        title='Change speed?',
        layout=[_SPEED_SLIDER()],
        expand_x=True,
        expand_y=True,
        font=F_11_B,
        relief=sg.RELIEF_RAISED,
        vertical_alignment='top'
    )


def INFO_BTN() -> sg.Button:
    return sg.Button(
        image_data=_icons.INFO(),
        button_color=BTN_COLOR,
        border_width=0,
        key="-INFO_BTN-",
        enable_events=True
    )


def _TRIM_TIME_INPUT(mode: str) -> tuple:
    time_input = sg.Input(
        k=f'-{mode.upper()}_IN-',
        size=(3, 4),
        font=F_11_B,
        disabled=True,
        default_text="00",
        justification='center',
        disabled_readonly_background_color=sg.DEFAULT_BACKGROUND_COLOR,
    )
    input_display = sg.T(f'{mode}', font=F_9_B)
    return time_input, input_display


def _TRIM_START_AT() -> tuple:
    check = sg.Checkbox(
        text=START_AT,
        font=F_11_B,
        default=False,
        key='-TRIM_CHECK-',
        enable_events=True
    )
    hour = _TRIM_TIME_INPUT('hour')
    minute = _TRIM_TIME_INPUT('minute')
    second = _TRIM_TIME_INPUT('second')
    return check, sg.P(), *hour, sg.P(), *minute, sg.P(), *second


def _TRIM_DURATION_SLIDER():
    return (
        sg.T(DURATION, font=F_11_B),
        sg.Slider(
            range=(1, 59),
            default_value=59,
            resolution=1,
            key='-DURATION_SLIDER-',
            orientation='horizontal',
            disable_number_display=True,
            enable_events=True,
            expand_x=True,
            disabled=True
        ),
        sg.T(DEFAULT_DURATION, key='-DURATION_TXT-', font=F_11_B),
    )


def _SPEED_SLIDER() -> list:
    txt = sg.T(SPEED_DISPLAY, font=F_11_B, key='-SPEED_TEXT-')
    slider = sg.Slider(
        range=(0.1, 3),
        default_value=1,
        resolution=0.1,
        orientation='horizontal',
        disable_number_display=True,
        expand_x=True,
        key='-SPEED_SLIDER-',
        enable_events=True,
        p=(10, 10)
    )
    return [txt, slider]
