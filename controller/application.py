import os
import webbrowser

import PySimpleGUI as sg

import assets
import model
import views
from ._form import Form
from ._gifer import Gifer


class Application:
    def __init__(self, window):
        self.view: sg.Window = window
        self.form = Form(window)

    def read_events(self):
        event, values = self.view.read(timeout=10)

        if event == "-VIDEO_IN-":
            self.form.controls_state(values)

        if event == "-START_BTN-":
            options = self.read_form()
            if not options:
                return
            self.run_gifer(options)

        if event == '-TRIM_CHECK-':
            self.form.update_trim_state()

        if event == '-DURATION_SLIDER-':
            self.form.update_duration(values)

        if event == '-SPEED_SLIDER-':
            self.form.update_speed(values)

        if event == "-INFO_BTN-":
            self.show_donate()

        if event == sg.WIN_CLOSED:
            return 'done'

    def read_form(self) -> model.Options | None:
        try:
            options = model.Options(self.form.data)
        except ValueError as err:
            views.ERROR_POPUP(str(err))
            return None
        return options

    def run_gifer(self, options):
        self.view.hide()
        gifer = Gifer(options)
        output = gifer.run()
        if views.DONE_POPUP():
            os.startfile(os.path.realpath(output))
        self.view.un_hide()

    def show_donate(self):
        self.view.hide()
        if views.INFO_POPUP() == 'Yes':
            webbrowser.open(assets.cfg.DONATE_LINK, new=0)
        self.view.un_hide()
