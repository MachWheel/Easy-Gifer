from os import startfile
from os.path import realpath

import ffmpeg

from app.options import Options
from app.views import DONE_POPUP


class Gifer:
    @staticmethod
    def start(options: Options):
        stream = ffmpeg.input(options.input_file)
        if options.duration != '00:00:00':
            trim_args = options.start_at, options.duration
            stream = Gifer._trim(trim_args, stream)
        stream = Gifer._set_speed(options.gif_speed, stream)
        Gifer._make_file(options.output_file, stream)
        Gifer._open_file(options.output_file)

    @staticmethod
    def _trim(options, stream):
        return stream.trim(start=options[0], duration=options[1])

    @staticmethod
    def _set_speed(gif_speed, stream):
        speed = 0.25 / gif_speed
        return stream.filter('setpts', f'(PTS-STARTPTS)*{speed}')

    @staticmethod
    def _make_file(output_file, stream):
        stream = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream, overwrite_output=True)

    @staticmethod
    def _open_file(output_file):
        if DONE_POPUP():
            startfile(realpath(output_file))
            return
