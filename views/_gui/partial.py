import PySimpleGUI as sg

from . import txt, fonts


def TRIM_TIME_INPUT(mode: str) -> tuple:
    time_input = sg.Input(
        k=f'-{mode.upper()}_IN-',
        size=(3, 4),
        font=fonts.F_11_B,
        disabled=True,
        default_text="00",
        justification='center',
        disabled_readonly_background_color=sg.DEFAULT_BACKGROUND_COLOR,
    )
    input_display = sg.T(f'{mode}', font=fonts.F_9_B)
    return time_input, input_display


def TRIM_START_AT() -> tuple:
    check = sg.Checkbox(
        text=txt.START_AT,
        font=fonts.F_11_B,
        default=False,
        key='-TRIM_CHECK-',
        enable_events=True
    )
    hour = TRIM_TIME_INPUT('hour')
    minute = TRIM_TIME_INPUT('minute')
    second = TRIM_TIME_INPUT('second')
    return check, sg.P(), *hour, sg.P(), *minute, sg.P(), *second


def TRIM_DURATION_SLIDER():
    return (
        sg.T(txt.DURATION, font=fonts.F_11_B),
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
        sg.T(txt.DEFAULT_DURATION, key='-DURATION_TXT-', font=fonts.F_11_B),
    )


def SPEED_SLIDER() -> list:
    display = sg.T(txt.SPEED_DISPLAY, font=fonts.F_11_B, key='-SPEED_TEXT-')
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
