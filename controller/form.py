import PySimpleGUI as sg

import assets


class Form:
    def __init__(self, view):
        self._set_duration = assets.cfg.MAX_DURATION
        self._set_speed = assets.cfg.DFT_SPEED
        self._video_input: sg.Input = view["-VIDEO_IN-"]
        self._trim_check: sg.Checkbox = view["-TRIM_CHECK-"]
        self._s_hour: sg.Input = view["-HOUR_IN-"]
        self._s_minute: sg.Input = view["-MINUTE_IN-"]
        self._s_second: sg.Input = view["-SECOND_IN-"]
        self._duration_slider: sg.Slider = view["-DURATION_SLIDER-"]
        self._duration_display: sg.Text = view["-DURATION_TXT-"]
        self._speed_slider: sg.Slider = view["-SPEED_SLIDER-"]
        self._speed_display: sg.Text = view['-SPEED_TEXT-']

    @property
    def data(self):
        hh: str = self._s_hour.get()
        mm: str = self._s_minute.get()
        ss: str = self._s_second.get()
        return {
            'input_path': self._video_input.get(),
            'start': (hh, mm, ss),
            'duration': self._set_duration,
            'gif_speed': self._set_speed
        }

    def update_speed(self, values) -> None:
        value = values['-SPEED_SLIDER-']
        speed_txt = f"{value}x"
        self._set_speed = value
        self._speed_display.update(speed_txt)

    def update_duration(self, values) -> None:
        secs = int(values['-DURATION_SLIDER-'])
        txt = f"{secs:02d} Second"
        txt += 's' if secs != 1 else ' '
        self._set_duration = secs
        self._duration_display.update(txt)

    def update_trim_state(self) -> None:
        checked = self._trim_check.get()
        disable = not checked
        self._start_inputs(disable)
        self._duration_inputs(disable)

    def _start_inputs(self, disable: bool) -> None:
        color = assets.style.STATE_COLOR(disable)
        inputs = [self._s_hour, self._s_minute, self._s_second]
        if disable:
            [i.update(assets.cfg.NO_TIME) for i in inputs]
        [i.update(disabled=disable, text_color=color) for i in inputs]

    def _duration_inputs(self, disable: bool) -> None:
        color = assets.style.STATE_COLOR(disable)
        if disable:
            values = assets.cfg.DISABLED_DURATION
        else:
            values = assets.cfg.ENABLED_DURATION
        self._set_duration = values['duration']
        self._duration_slider.update(values['slider'], disabled=disable)
        self._duration_display(values['display'], text_color=color)
