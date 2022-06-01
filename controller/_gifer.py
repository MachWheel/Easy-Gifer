from concurrent.futures import ThreadPoolExecutor, Future

import ffmpeg

import assets
import model
import views


class Gifer:
    def __init__(self, options: model.Options):
        self.options = options

    def run(self) -> str:
        with ThreadPoolExecutor() as e:
            task = e.submit(self._convert)
            _show_progress(task)
            output = task.result()
        return output

    @property
    def _trim_set(self) -> bool:
        return self.options.duration != '00:00:00'

    @property
    def _stream_input(self):
        return ffmpeg.input(self.options.input_path)

    def _convert(self):
        args = self.options
        output_file = args.output_path
        stream = self._stream_input
        if self._trim_set:
            stream = _trim(args, stream)
        stream = _set_speed(args.gif_speed, stream)
        _make_file(output_file, stream)
        return output_file


def _trim(options: model.Options, stream):
    return stream.trim(start=options.start_time, duration=options.duration)

def _set_speed(gif_speed, stream):
    return stream.filter('setpts', f'(PTS-STARTPTS)*{gif_speed}')

def _make_file(output_file, stream):
    stream = ffmpeg.output(stream, output_file)
    ffmpeg.run(stream, overwrite_output=True, quiet=True)

def _show_progress(task: Future[str]):
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
