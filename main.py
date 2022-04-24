from app.controller import Controller
from app.views import MAIN_WINDOW


def main(app: Controller):
    while True:
        status = app.read_events()
        if status == 'done':
            break

if __name__ == "__main__":
    main(Controller(MAIN_WINDOW()))
