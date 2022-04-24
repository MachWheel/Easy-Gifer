import webbrowser

from PySimpleGUI import read_all_windows, WIN_CLOSED

from app.options import Options
from app.views import INFO_POPUP
from app.gifer import Gifer
from resources.labels import DONATE_LINK


class Controller:
    def __init__(self, window):
        self.view = window

    @staticmethod
    def read_events():
        window, event, values = read_all_windows()

        if event == "-START_BTN-":
            options = Options(values)
            Gifer.start(options)
            return

        if event == '-TRIM_CHECK-':
            Controller.change_trim_state(window, values)

        if event == '-SPEED_SLIDER-':
            Controller.speed_changed(window, values)

        if event == "-INFO_BTN-":
            Controller.view_donate(window)

        if event == WIN_CLOSED:
            return 'done'

    @staticmethod
    def speed_changed(window, values):
        speed_input = window['-SPEED_TEXT-']
        speed_input.update(f"{values['-SPEED_SLIDER-']}x")
        return

    @staticmethod
    def view_donate(window):
        window.hide()
        if INFO_POPUP() == 'Yes':
            webbrowser.open(DONATE_LINK, new=0)
        window.un_hide()

    @staticmethod
    def change_trim_state(window, values):
        start_field = window['-START_IN-']
        duration_input = window['-LEN_IN-']
        if not values['-TRIM_CHECK-']:
            value = '00:00:00'
            start_field.update(value, disabled=True)
            duration_input.update(value, disabled=True)
        else:
            start_field.update(disabled=False)
            duration_input.update(disabled=False)
