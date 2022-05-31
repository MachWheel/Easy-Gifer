from controller import Application
from views import MAIN_WINDOW


def main(app: Application):
    while True:
        status = app.read_events()
        if status == 'done':
            break

if __name__ == "__main__":
    main(Application(MAIN_WINDOW()))
