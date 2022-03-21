import base64

def START():
    with open("resources/graphics/start.png", "rb") as png_file:
        return base64.b64encode(png_file.read())


def FOLDER():
    with open("resources/graphics/folder.png", "rb") as png_file:
        return base64.b64encode(png_file.read())

def INFO():
    with open("resources/graphics/info.png", "rb") as png_file:
        return base64.b64encode(png_file.read())
