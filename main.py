import importlib.util
import os

from controller import Application
from views import MAIN_WINDOW


def close_splash():
    """Closes the application loading splash screen."""
    if '_PYIBoot_SPLASH' in os.environ:
        if not importlib.util.find_spec("pyi_splash"):
            return
        import pyi_splash
        pyi_splash.close()


def main(app: Application):
    while True:
        status = app.read_events()
        if status == 'done':
            break


if __name__ == "__main__":
    close_splash()
    main(Application(MAIN_WINDOW()))
