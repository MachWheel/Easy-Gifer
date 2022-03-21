# coding=utf-8
import PySimpleGUI as sg
from PySimpleGUI import (
    BUTTON_TYPE_READ_FORM, BUTTON_TYPE_BROWSE_FILE
)

from resources import icons
from resources.messages import (
    APP_TITLE, SELECT_FOLDER, INFO_HELP, BROWSE_TOOLTIP,
    START_TOOLTIP, DONE
)
from resources.names import THEME

sg.theme(THEME)

def MAIN_WINDOW():
    return sg.Window(
        APP_TITLE,
        [
            [_MAIN_TEXT],
            [_BROWSE_BTN, _INPUT_VIDEO, _START_BTN],
            [_TRIM_FRAME],
            [_SPEED_SLIDER[0], _SPEED_SLIDER[1],
             _SPEED_SLIDER[2], sg.VSep(p=(7, 0)), _INFO_BTN]

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

def _H_SEP():
    return sg.HSep(p=(10, 20))

_BTN_COLOR = sg.theme_background_color(), sg.theme_background_color()

_MSG_FONT = "Default 14"

_MAIN_TEXT = sg.Text(
    SELECT_FOLDER,
    font="Default 14 bold",
    p=((10, 10), (20, 10))
)

_TRIM_CHECK = sg.Checkbox(
    "TRIM?", font="Default 11 bold",
    default=False, key='-TRIM_CHECK-',
    enable_events=True
)

_BROWSE_BTN = sg.Button(
    button_type=BUTTON_TYPE_BROWSE_FILE,
    image_data=icons.FOLDER(),
    button_color=_BTN_COLOR,
    border_width=0,
    target='-VIDEO_IN-',
    tooltip=BROWSE_TOOLTIP
)

_START_BTN = sg.Button(
    button_type=BUTTON_TYPE_READ_FORM,
    image_data=icons.START(),
    button_color=_BTN_COLOR,
    border_width=0,
    tooltip=START_TOOLTIP,
    key="-START_BTN-"
)

_INPUT_VIDEO = sg.Input(
    k='-VIDEO_IN-',
    size=(30, 4),
    expand_x=True,
    font=_MSG_FONT
)

START = (
    sg.Text('START AT:', font='Default 11 bold'),
    sg.Input(
        k='-START_IN-',
        size=(8, 4),
        font='Default 11 bold',
        disabled=True,
        default_text="00:00:00",
        justification='center',
        disabled_readonly_background_color=sg.DEFAULT_BACKGROUND_COLOR
    )
)

LENGHT = (
    sg.T('DURATION:', font='Default 11 bold'),
    sg.Input(
        k='-LEN_IN-',
        size=(8, 4),
        font='Default 11 bold',
        disabled=True,
        default_text="00:00:00",
        justification='center',
        disabled_readonly_background_color=sg.DEFAULT_BACKGROUND_COLOR
    )
)

_TRIM_FRAME = sg.Frame(
    title='',
    layout=[
        [sg.VPush()],
        [_TRIM_CHECK, sg.VSep(), *START, sg.Push(), *LENGHT, sg.Push()],
        [sg.VPush()],
    ],
    pad=(0, 15), relief=sg.RELIEF_RAISED, expand_x=True
)

_SPEED_SLIDER = (
    sg.T('CHANGE SPEED:', font='Default 11 bold'),
    sg.Slider(
        range=(0.1, 3),
        default_value=1,
        resolution=0.1,
        orientation='horizontal',
        disable_number_display=True,
        expand_x=True,
        key='-SPEED_SLIDER-',
        enable_events=True
    ),
    sg.Text(
        '1.0x',
        font='Default 11 bold',
        key='-SPEED_TEXT-'
    )
)

_INFO_BTN = sg.Button(
    image_data=icons.INFO(),
    button_color=_BTN_COLOR,
    border_width=0,
    key="-INFO_BTN-",
    enable_events=True
)
