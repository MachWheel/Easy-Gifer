from concurrent.futures import ThreadPoolExecutor, Future

import ffmpeg

import views
import model
import assets


class Gifer:
    @staticmethod
    def run(options: model.Options) -> str:
        with ThreadPoolExecutor() as e:
            task = e.submit(Gifer._convert, options)
            SHOW_TASK_PROGRESS(task)
            output = task.result()
        return output

    @staticmethod
    def _convert(options: model.Options):
        output_file = options.output_path
        stream = ffmpeg.input(options.input_path)
        if options.duration != '00:00:00':
            trim_args = options.start_time, options.duration
            stream = Gifer._trim(trim_args, stream)
        stream = Gifer._set_speed(options.gif_speed, stream)
        Gifer._make_file(output_file, stream)
        return output_file

    @staticmethod
    def _trim(options, stream):
        return stream.trim(start=options[0], duration=options[1])

    @staticmethod
    def _set_speed(gif_speed, stream):
        return stream.filter('setpts', f'(PTS-STARTPTS)*{gif_speed}')

    @staticmethod
    def _make_file(output_file, stream):
        stream = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream, overwrite_output=True, quiet=True)


def SHOW_TASK_PROGRESS(task: Future[str]):
    bar_end, reload_i, i = 100, 99, 0
    view = views.PROGRESS_POPUP(bar_end=bar_end)
    while task.running():
        view.read(timeout=10)
        if i == reload_i:
            i = 0
            msg = assets.msgs.SLOW_EXPORTING()
            view['-TXT-'].update(msg)
        view['-PROG-'].update(current_count=(i + 1))
        i += 1
    view.close()
