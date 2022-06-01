import PySimpleGUI as sg

import assets
from assets import txt, style, icons


def VIDEO_INPUT() -> sg.Input:
    return sg.Input(
        k='-VIDEO_IN-',
        size=(30, 4),
        expand_x=True,
        font=style.F_14,
        enable_events=True
    )


def BROWSE_BTN() -> sg.Button:
    return sg.Button(
        button_type=sg.BUTTON_TYPE_BROWSE_FILE,
        image_data=icons.FOLDER(),
        button_color=style.BTN_COLOR(),
        border_width=0,
        target='-VIDEO_IN-',
        tooltip=txt.BROWSE_TOOLTIP
    )


def START_BTN() -> sg.Button:
    return sg.Button(
        button_type=sg.BUTTON_TYPE_READ_FORM,
        image_data=icons.START(),
        button_color=style.BTN_COLOR(),
        border_width=0,
        tooltip=txt.START_TOOLTIP,
        key="-START_BTN-"
    )


def INFO_BTN() -> sg.Button:
    return sg.Button(
        image_data=assets.icons.INFO(),
        button_color=assets.style.BTN_COLOR(),
        border_width=0,
        key="-INFO_BTN-",
        enable_events=True,
        p=(5, 5)
    )


def _time_input(mode: str) -> tuple:
    time_input = sg.Input(
        k=f'-{mode.upper()}_IN-',
        size=(3, 4),
        font=style.F_11_B,
        disabled=True,
        default_text="00",
        justification='center',
        disabled_readonly_background_color=style.BG_COLOR(),
    )
    input_display = sg.Text(f'{mode}', font=style.F_9_B)
    return time_input, input_display


def START_TIME_INPUTS() -> tuple:
    check = sg.Checkbox(
        text=txt.START_AT,
        font=style.F_11_B,
        default=False,
        key='-TRIM_CHECK-',
        enable_events=True
    )
    hour = _time_input('hour')
    minute = _time_input('minute')
    second = _time_input('second')
    return check, sg.P(), *hour, sg.P(), *minute, sg.P(), *second


def DURATION_SLIDER():
    return (
        sg.T(txt.DURATION, font=style.F_11_B),
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
        sg.T(txt.DEFAULT_DURATION, key='-DURATION_TXT-', font=style.F_11_B),
    )


def SPEED_SLIDER() -> list:
    display = sg.Text(
        txt.SPEED_DISPLAY,
        font=style.F_11_B,
        key='-SPEED_TEXT-'
    )
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
    return [display, slider]
