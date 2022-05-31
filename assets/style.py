import PySimpleGUI as sg

APP_THEME = "DarkBlue"
sg.theme(APP_THEME)

def BTN_COLOR() -> tuple:
    return sg.theme_background_color(), sg.theme_background_color()

def BG_COLOR():
    return sg.theme_background_color()

def STATE_COLOR(state):
    colors = 'yellow', sg.theme_element_text_color()
    return colors[state]

#  FONTS:  ################
F_14 = "Default 14"
F_14_B = "Default 14 bold"
F_11_B = "Default 11 bold"
F_9_B = "Default 9 bold"
