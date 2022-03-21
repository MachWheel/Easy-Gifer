import logging
from os import startfile
from os.path import splitext, realpath

import ffmpeg

from app.elements import DONE_POPUP
from resources.messages import FINISHED


class Gifer:
    def __init__(self, video_in: str):
        self.log = logging.getLogger(__name__)
        self.stream = ffmpeg.input(video_in)
        self.gif_out = f"{splitext(video_in)[0]}.gif"

    def trim(self, start: str, duration: str):
        if duration == '00:00:00':
            return
        self.stream = self.stream.trim(
            start=start, duration=duration
        )

    def set_speed(self, speed_in: float):
        speed = 0.25 / speed_in
        self.stream = self.stream.filter(
            'setpts', f'(PTS-STARTPTS)*{speed}'
        )

    def make(self):
        self.stream = ffmpeg.output(self.stream, self.gif_out)
        ffmpeg.run(self.stream, overwrite_output=True)

    def terminate(self):
        if DONE_POPUP():
            startfile(realpath(self.gif_out))
            self.log.debug(FINISHED)
            return
