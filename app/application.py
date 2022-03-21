# coding=utf-8

import logging
from os.path import isfile

from resources.messages import STARTED
from .controller import Controller
from .gifer import Gifer


class Application:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.controller = Controller()

    def running(self):
        return self.controller.read_events(self)

    def start(self, video_in: str, options: tuple):
        if not isfile(video_in):
            return
        self.log.info(STARTED)
        start, duration, speed = options
        giffer = Gifer(video_in)
        giffer.trim(start, duration)
        giffer.set_speed(speed)
        giffer.make()
        giffer.terminate()
