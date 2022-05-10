from concurrent.futures import ThreadPoolExecutor

import ffmpeg

from app.options import Options
from app.task_progress import TASK_PROGRESS


class Gifer:
    @staticmethod
    def run(options: Options) -> str:
        with ThreadPoolExecutor() as e:
            task = e.submit(Gifer._convert, options)
            TASK_PROGRESS(task)
            output = task.result()
        return output

    @staticmethod
    def _convert(options: Options):
        output_file = options.output_file
        stream = ffmpeg.input(options.input_file)
        if options.duration != '00:00:00':
            trim_args = options.start_at, options.duration
            stream = Gifer._trim(trim_args, stream)
        stream = Gifer._set_speed(options.gif_speed, stream)
        Gifer._make_file(output_file, stream)
        return output_file

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
        ffmpeg.run(stream, overwrite_output=True, quiet=True)
