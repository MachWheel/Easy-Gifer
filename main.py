# coding=utf-8
import logging.config

from PySimpleGUI import Window

from app.application import Application
from app.elements import MAIN_WINDOW
from resources.messages import DRAWN, STARTED, INITIALIZING


def main(app: Application, view: Window):
    log = logging.getLogger(__name__)
    log.debug(STARTED)
    while True:
        log.debug(DRAWN(view))
        running_status = app.running()
        if running_status == 'done':
            break

if __name__ == "__main__":
    logging.config.fileConfig("resources/configs/log_config.ini")
    logging.debug(INITIALIZING)
    main(Application(), MAIN_WINDOW())
