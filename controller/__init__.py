import webbrowser
from os import startfile
from os.path import realpath

from PySimpleGUI import read_all_windows, WIN_CLOSED

from .options import Options
from gifer import Gifer
from views import DONE_POPUP, INFO_POPUP


class Controller:
    def __init__(self, window):
        self.view = window

    @staticmethod
    def read_events():
        window, event, values = read_all_windows()

        if event == "-START_BTN-":
            window.hide()
            selected_options = Options(values)
            output = Gifer.run(selected_options)
            if DONE_POPUP():
                startfile(realpath(output))
            window.un_hide()
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
            webbrowser.open(_DONATE_LINK, new=0)
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

_DONATE_LINK = "https://www.paypal.com/donate/?hosted_button_id=RNDCMNV4YWHX4"
