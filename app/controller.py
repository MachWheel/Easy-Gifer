# coding=utf-8

import logging
import webbrowser

from PySimpleGUI import read_all_windows, WIN_CLOSED

from app.elements import INFO_POPUP
from resources.names import DONATE_LINK


class Controller:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    @staticmethod
    def read_events(app):
        window, event, values = read_all_windows()

        if event == "-START_BTN-":
            video_in = values["-VIDEO_IN-"]
            if not video_in:
                return
            start = values['-START_IN-']
            duration = values['-LEN_IN-']
            speed = values['-SPEED_SLIDER-']
            options = (start, duration, speed)
            app.start(video_in, options)

        if event == '-TRIM_CHECK-':
            if not values['-TRIM_CHECK-']:
                value = '00:00:00'
                window['-START_IN-'].update(value=value, disabled=True)
                window['-LEN_IN-'].update(value=value, disabled=True)
            else:
                window['-START_IN-'].update(disabled=False)
                window['-LEN_IN-'].update(disabled=False)

        if event == '-SPEED_SLIDER-':
            window['-SPEED_TEXT-'].update(
                f"{values['-SPEED_SLIDER-']}x"
            )

        if event == "-INFO_BTN-":
            window.hide()
            if INFO_POPUP() == 'Yes':
                webbrowser.open(DONATE_LINK, new=0)
            window.un_hide()

        if event == WIN_CLOSED:
            return 'done'
