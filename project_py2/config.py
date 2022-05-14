from pygame import font

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
font.init()
FONT = font.SysFont(name='Arial', size=40, bold=True)
BLACK = (0, 0, 0)  # черный цвет
button = ["PLAY", "SCORE", "QUIT"]  # Список кнопок в config
BUTTON_COL = (133, 253, 249)
BUTTON_PRESSED_COL = (133, 253, 150)
BUTTON_SIZE = (160, 40)
