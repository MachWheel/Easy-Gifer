from random import choice

INVALID_FILE = 'Invalid file selected.'
INVALID_TRIM = f'Invalid trim start time typed.'

def INVALID_TIME(start_at: str):
    return f'Invalid trim start time typed:\n{start_at}'

def SLOW_EXPORTING() -> str:
    return choice([
        "This might take some time...",
        "Sorry to keep you waiting...",
        "Holy ****! That's a huge file...",
        "That's a huge file you have huh...",
        "Still going...",
        "Try choosing a smaller duration next time...",
    ])
