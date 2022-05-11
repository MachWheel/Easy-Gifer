import PySimpleGUI as sg

from . import txt, icons, fonts, partial

sg.theme(txt.APP_THEME)
BTN_COLOR = sg.theme_background_color(), sg.theme_background_color()

def MAIN_TEXT() -> sg.Text:
    pad = (10, 10), (20, 10)
    return sg.T(txt.SELECT_VIDEO, font=fonts.F_14_B, p=pad)


def MAIN_CONTROLS() -> tuple:
    BROWSE_BTN = sg.Button(
        button_type=sg.BUTTON_TYPE_BROWSE_FILE,
        image_data=icons.FOLDER(),
        button_color=BTN_COLOR,
        border_width=0,
        target='-VIDEO_IN-',
        tooltip=txt.BROWSE_TOOLTIP
    )
    INPUT_VIDEO = sg.Input(
        k='-VIDEO_IN-',
        size=(30, 4),
        expand_x=True,
        font=fonts.F_14
    )
    START_BTN = sg.Button(
        button_type=sg.BUTTON_TYPE_READ_FORM,
        image_data=icons.START(),
        button_color=BTN_COLOR,
        border_width=0,
        tooltip=txt.START_TOOLTIP,
        key="-START_BTN-"
    )
    return BROWSE_BTN, INPUT_VIDEO, START_BTN


def TRIM_FRAME() -> sg.Frame:
    sep = sg.HSep(p=(5, 15), color=sg.theme_background_color())
    layout = [
        [sg.VPush()],
        [*partial.TRIM_START_AT(), sg.Push()],
        [sep],
        [*partial.TRIM_DURATION_SLIDER()],
        [sg.VPush()],
    ]
    return sg.Frame(
        title=txt.TRIM,
        layout=layout,
        pad=(0, 15),
        relief=sg.RELIEF_RAISED,
        expand_x=True,
        element_justification='left',
        font=fonts.F_11_B
    )


def SPEED_FRAME() -> sg.Frame:
    return sg.Frame(
        title='Change speed?',
        layout=[partial.SPEED_SLIDER()],
        expand_x=True,
        expand_y=True,
        font=fonts.F_11_B,
        relief=sg.RELIEF_RAISED,
        vertical_alignment='top'
    )


def INFO_BTN() -> sg.Button:
    return sg.Button(
        image_data=icons.INFO(),
        button_color=BTN_COLOR,
        border_width=0,
        key="-INFO_BTN-",
        enable_events=True
    )
