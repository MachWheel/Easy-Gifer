import os

import assets

class Options:
    def __init__(self, form: dict):
        self.input_path = _parse_file(form)
        self.start_time = _parse_start_time(form)
        self.duration = _parse_duration(form)
        self.gif_speed = _parse_speed(form)
        self.output_path = _out_from_in(self.input_path)


def _parse_start_time(form) -> str:
    try:
        hh, mm, ss = (int(val) for val in form['start'])
    except ValueError:
        raise ValueError(assets.msgs.INVALID_TRIM)
    return f"{hh:02d}:{mm:02d}:{ss:02d}"

def _parse_file(form) -> str:
    file = form['input_path']
    if not (file and os.path.isfile(file)):
        raise ValueError(assets.msgs.INVALID_FILE)
    return file

def _parse_speed(form) -> float:
    spd = form['gif_speed']
    return round(0.25 / spd, 2)

def _parse_duration(form) -> str:
    ss = form['duration']
    return f"00:00:{ss:02d}"

def _out_from_in(file) -> str:
    out_path = f'{os.path.splitext(file)[0]}.gif'
    return out_path
