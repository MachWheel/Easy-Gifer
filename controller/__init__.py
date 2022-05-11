import webbrowser
from os import startfile
from os.path import realpath

from PySimpleGUI import read_all_windows, WIN_CLOSED

from views import DONE_POPUP, INFO_POPUP
from ._config import DONATE_LINK
from .gifer import Gifer
from .options_form import OptionsForm


class Controller:
    def __init__(self, window):
        self.view = window
        self.options = OptionsForm(window)


    def read_events(self):
        window, event, values = read_all_windows()

        if event == "-START_BTN-":
            if not self.options.validate():
                return
            window.hide()
            output = Gifer.run(self.options)
            if DONE_POPUP():
                startfile(realpath(output))
            window.un_hide()
            return

        if event == '-TRIM_CHECK-':
            self.options.update_trim_state()

        if event == '-DURATION_SLIDER-':
            self.options.update_duration(values)

        if event == '-SPEED_SLIDER-':
            self.options.update_speed(values)

        if event == "-INFO_BTN-":
            self.show_donate()

        if event == WIN_CLOSED:
            return 'done'


    def show_donate(self):
        self.view.hide()
        if INFO_POPUP() == 'Yes':
            webbrowser.open(DONATE_LINK, new=0)
        self.view.un_hide()
