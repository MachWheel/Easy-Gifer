from os.path import isfile, splitext


class Options:
    def __init__(self, values):
        input_file = values["-VIDEO_IN-"]
        if not _validate_input(input_file):
            raise ValueError('Invalid input video file')
        self.input_file = input_file
        self.output_file = _gif_path(input_file)
        self.start_at = values["-START_IN-"]
        self.duration = values["-LEN_IN-"]
        self.gif_speed = values["-SPEED_SLIDER-"]


def _validate_input(input_file):
    return input_file and isfile(input_file)

def _gif_path(input_file):
    return f'{splitext(input_file)[0]}.gif'
