from os import startfile
from os.path import splitext, realpath

import ffmpeg

from app.views import DONE_POPUP


class Gifer:
    def __init__(self, inputs):
        self.video_in = inputs["-VIDEO_IN-"]
        self.start_at = inputs["-START_IN-"]
        self.duration = inputs["-LEN_IN-"]
        self.speed = inputs["-SPEED_SLIDER-"]
        self.gif_out = f"{splitext(self.video_in)[0]}.gif"
        self.stream = None

    def start(self):
        self.stream = ffmpeg.input(self.video_in)
        self.trim()
        self.set_speed()
        self.make()
        self.terminate()

    def trim(self):
        if self.duration == '00:00:00':
            return
        self.process(
            self.stream.trim(start=self.start_at, duration=self.duration)
        )

    def process(self, stream):
        self.stream = stream

    def set_speed(self):
        speed = 0.25 / self.speed
        self.process(
            self.stream.filter('setpts', f'(PTS-STARTPTS)*{speed}')
        )

    def make(self):
        self.process(
            ffmpeg.output(self.stream, self.gif_out)
        )
        ffmpeg.run(self.stream, overwrite_output=True)

    def terminate(self):
        if DONE_POPUP():
            startfile(realpath(self.gif_out))
            return
