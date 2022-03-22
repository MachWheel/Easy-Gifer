# coding=utf-8

import webbrowser
from os.path import isfile

from PySimpleGUI import read_all_windows, WIN_CLOSED

from app.elements import INFO_POPUP
from app.gifer import Gifer
from resources.names import DONATE_LINK


class Controller:
    def __init__(self, window):
        self.view = window

    @staticmethod
    def read_events():
        window, event, values = read_all_windows()

        if event == "-START_BTN-":
            video_in = values["-VIDEO_IN-"]
            if not video_in or not isfile(video_in):
                return
            work = Gifer(inputs=values)
            work.start()
            return 'done'

        if event == '-TRIM_CHECK-':
            start_at = window['-START_IN-']
            duration = window['-LEN_IN-']
            if not values['-TRIM_CHECK-']:
                value = '00:00:00'
                start_at.update(value=value, disabled=True)
                duration.update(value=value, disabled=True)
            else:
                start_at.update(disabled=False)
                duration.update(disabled=False)

        if event == '-SPEED_SLIDER-':
            speed_set = window['-SPEED_TEXT-']
            speed_set.update(f"{values['-SPEED_SLIDER-']}x")

        if event == "-INFO_BTN-":
            window.hide()
            if INFO_POPUP() == 'Yes':
                webbrowser.open(DONATE_LINK, new=0)
            window.un_hide()

        if event == WIN_CLOSED:
            return 'done'
