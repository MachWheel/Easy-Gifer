from os.path import isfile, splitext

import PySimpleGUI as sg

from views import ERROR_POPUP
from ._config import (
    DFT_DURATION, DFT_DURATION_VAL, DFT_DURATION_TXT,
    MAX_DURATION, MAX_DURATION_VAL, MAX_DURATION_TXT,
    DFT_TIME
)
from ._msgs import (
    INVALID_FILE, INVALID_TRIM, INVALID_TIME
)


class OptionsForm:
    def __init__(self, view):
        self.duration = 0
        self.gif_speed = 0.25
        self._video_input = view["-VIDEO_IN-"]
        self._trim_check = view["-TRIM_CHECK-"]
        self._s_hour = view["-HOUR_IN-"]
        self._s_minute = view["-MINUTE_IN-"]
        self._s_second = view["-SECOND_IN-"]
        self._duration_slider = view["-DURATION_SLIDER-"]
        self._duration_display = view["-DURATION_TXT-"]
        self._speed_slider = view["-SPEED_SLIDER-"]
        self._speed_display = view['-SPEED_TEXT-']

    @property
    def input_path(self) -> str:
        return self._video_input.get()

    @property
    def output_path(self) -> str:
        return f'{splitext(self.input_path)[0]}.gif'
    
    @property
    def start_at(self) -> str:
        hour = int(self._s_hour.get())
        minute = int(self._s_minute.get())
        sec = int(self._s_second.get())
        return f"{hour:02d}:{minute:02d}:{sec:02d}"

    def update_speed(self, values) -> None:
        speed = values['-SPEED_SLIDER-']
        speed_txt = f"{speed}x"
        self.gif_speed = round(0.25 / speed, 2)
        self._speed_display.update(speed_txt)

    def update_duration(self, values) -> None:
        secs = int(values['-DURATION_SLIDER-'])
        txt = f"{secs:02d} Second{'s' if secs != 1 else ' '}"
        self.duration = f"00:00:{secs:02d}"
        self._duration_display.update(txt)

    def update_trim_state(self) -> None:
        state = self._trim_check.get()
        colors = (sg.theme_element_text_color(), 'yellow')
        color = colors[state]
        inputs = [self._s_hour, self._s_minute, self._s_second]
        if state:
            [inp.update(disabled=False, text_color=color) for inp in inputs]
            self._enable_duration(color)
        else:
            [inp.update(DFT_TIME, disabled=True, text_color=color) for inp in inputs]
            self._reset_duration(color)

    def validate(self) -> bool:
        input_path = self.input_path
        if not (input_path and isfile(input_path)):
            ERROR_POPUP(INVALID_FILE)
            return False
        if not self._trim_check.get():
            return True
        t_inputs = [self._s_hour, self._s_minute, self._s_second]
        try:
            [int(t_input.get()) for t_input in t_inputs]
        except ValueError:
            ERROR_POPUP(INVALID_TRIM)
            return False
        start_at = self.start_at
        if len(start_at) != 8:
            ERROR_POPUP(INVALID_TIME(start_at))
            return False
        else:
            return True

    def _enable_duration(self, color: str):
        self.duration = DFT_DURATION
        self._duration_slider.update(DFT_DURATION_VAL, disabled=False)
        self._duration_display(DFT_DURATION_TXT, text_color=color)

    def _reset_duration(self, color: str):
        self.duration = MAX_DURATION
        self._duration_slider.update(MAX_DURATION_VAL, disabled=True)
        self._duration_display(MAX_DURATION_TXT, text_color=color)
