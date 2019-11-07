
import tkinter as tk
from random import randrange
from math import sin, cos, pi
import os

# Window size
WIN_WIDTH = 700
WIN_HEIGHT = 700

# Create main window
root = tk.Tk()
root.geometry(str(WIN_WIDTH) + 'x' + str(WIN_HEIGHT))

# Create canvas on window
canvas = tk.Canvas(root, width=WIN_WIDTH, height=WIN_HEIGHT, bg='white')
canvas.pack()

# Integer in python are non-changable and
# will be more usefull to store all game variable in single list
# so I prefer create list for game score(and may be game mode {menu/game/score_list})
GAME_SCORE = 0
GAME_MODE = 1
GAME_MODE_MAIN_MENU = 0
GAME_MODE_GAME = 1
GAME_MODE_SAVE_SCORE = 2
GAME_MODE_SHOW_SCORE = 3
GAME_TIME_DEFAULT = 2
GAME_TIME_CURRENT = 3
GAME_SAVEFILE = 4
game_settings = [0, GAME_MODE_MAIN_MENU, 1000, 0, 'best_players.hirianov_top']

# Circle is tuple
# (x, y, radius, color, time, vx, vy)
# x - circle x position
# y - circle y position
# radius - circle radius
# color - circle color
# time - game_tiks count until destroy
# vx - circle x velocity
# vy - circle y velocity

# Constants for more easy work with circle parameters
CIRCLE_X = 0
CIRCLE_Y = 1
CIRCLE_RAD = 2
CIRCLE_COLOR = 3
CIRCLE_TIME = 4
CIRCLE_VX = 5
CIRCLE_VY = 6
# List of all targets
circles_list = []

# From this colors will be select random color for circle
# Score poinst on target hit increment = (colors_list.id(color) + 1)
colors_list = ['red', 'magenta', 'yellow', 'green', 'cyan', 'blue']


def add_circle(x=-1, y=-1, radius=-1, color=-1, time=-1, vx=-1, vy=-1):
    """
        Create circle with parameters(if params not defined, they will be defined randomly)
        and add it to circles_list
    """
    radius = randrange(12, 20) if radius == -1 else radius
    x = randrange(radius, WIN_WIDTH - radius) if x == -1 else x
    y = randrange(radius, WIN_HEIGHT - radius) if y == -1 else y
    v = randrange(5, 10) * (randrange(0, 1) - 1)
    time = len(colors_list) - 3 + randrange(0, 14) / 5 - 0.01
    angle = randrange(0, 359) / 180 * pi
    vx = v * cos(angle) if vx == -1 else vx
    vy = v * sin(angle) if vy == -1 else vy
    circles_list.append([x, y, radius, 'blue', time, vx, vy])


def update_circle(circle):
    """
        circle.x += circle.vx
        circle.y += circle.vy
    """
    circle[CIRCLE_X] += circle[CIRCLE_VX]
    circle[CIRCLE_Y] += circle[CIRCLE_VY]

    circle[CIRCLE_TIME] -= 0.08
    circle[CIRCLE_COLOR] = colors_list[int(circle[CIRCLE_TIME])]

    # horisontal collision with window border
    if (circle[CIRCLE_X] < circle[CIRCLE_RAD]) or (circle[CIRCLE_X] > WIN_WIDTH - circle[CIRCLE_RAD]):
        circle[CIRCLE_VX] *= -randrange(5, 15) / 10
        circle[CIRCLE_X] += circle[CIRCLE_VX]

    # vertical collision with window border
    if (circle[CIRCLE_Y] < circle[CIRCLE_RAD]) or (circle[CIRCLE_Y] > WIN_HEIGHT - circle[CIRCLE_RAD]):
        circle[CIRCLE_VY] *= -randrange(5, 15) / 10
        circle[CIRCLE_Y] += circle[CIRCLE_VY]


def draw_circle(circle):
    """
        Draw circle on window
    """
    x = circle[CIRCLE_X]
    y = circle[CIRCLE_Y]
    radius = circle[CIRCLE_RAD]
    color = circle[CIRCLE_COLOR]
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline=color)


# Button is tuple
# (x, y, size, name, color)
# x - button center x position
# y - button center y position
# size - button size
#   button width = 4*size
#   button height = 2*size
#   (button is rectangle)
# name - button name
# color - button color
BUTTON_X = 0
BUTTON_Y = 1
BUTTON_SIZE = 2
BUTTON_NAME = 3
BUTTON_COLOR = 4
buttons_list = []


def add_button(x, y, size, name, color):
    buttons_list.append((x, y, size, name, color))


def draw_button(button):
    x = button[BUTTON_X]
    y = button[BUTTON_Y]
    size = button[BUTTON_SIZE]
    name = button[BUTTON_NAME]
    color = button[BUTTON_COLOR]
    canvas.create_rectangle(x - 2 * size, y - size, x + 2 * size, y + size, fill=color, outline='black')
    canvas.create_text(x, y, font='Arial 16', justify='center', text=name)


def start_new_game(circles_count=4):
    """
        Set game vars for starting new game
    """
    game_settings[GAME_SCORE] = 0
    game_settings[GAME_TIME_CURRENT] = game_settings[GAME_TIME_DEFAULT]

    circles_list.clear()
    for i in range(circles_count):
        add_circle()


def main_menu_on_click(event):
    """
        IN MAIN MENU
        Left moust button click
    """
    for b in buttons_list:
        bx = b[BUTTON_X]
        by = b[BUTTON_Y]
        size = b[BUTTON_SIZE]
        name = b[BUTTON_NAME]
        if (bx - 2 * size <= event.x) and (bx + 2 * size >= event.x) and (by - size <= event.y) and (
                by + size >= event.y):
            if name == 'Start':
                start_new_game()
                game_settings[GAME_MODE] = GAME_MODE_GAME
            if name == 'Scorelist':
                game_settings[GAME_MODE] = GAME_MODE_SHOW_SCORE


def main_menu_loop():
    """
        Draw & update game menu
    """
    # window clear
    canvas.delete('all')

    for b in buttons_list:
        draw_button(b)

    canvas.create_text(WIN_WIDTH / 2, 10, font='Arial 16', text='Last score: ' + str(game_settings[GAME_SCORE]))


def game_on_click(event):
    """
        IN GAME MODE
        Left mouse button click
    """
    for i in range(len(circles_list) - 1, -1, -1):
        if (event.x - circles_list[i][CIRCLE_X]) ** 2 + (event.y - circles_list[i][CIRCLE_Y]) ** 2 <= circles_list[i][
            CIRCLE_RAD] ** 2:
            game_settings[GAME_SCORE] += (colors_list.index(circles_list[i][CIRCLE_COLOR]) + 1)
            circles_list.remove(circles_list[i])


def game_loop():
    """
        Main game loop
        Exec always(each delay)
    """
    # window clear
    canvas.delete('all')

    if game_settings[GAME_TIME_CURRENT] % 15 == 0:
        add_circle()

    for i in range(len(circles_list) - 1, -1, -1):
        update_circle(circles_list[i])
        if circles_list[i][CIRCLE_TIME] <= 0:
            circles_list.remove(circles_list[i])

    for c in circles_list:
        draw_circle(c)

    # Check if game end
    if game_settings[GAME_TIME_CURRENT] == 0:
        game_settings[GAME_MODE] = GAME_MODE_SAVE_SCORE

    game_settings[GAME_TIME_CURRENT] -= 1

    canvas.create_text(WIN_WIDTH / 2, 10, font='Arial 16', text='Score: ' + str(game_settings[GAME_SCORE]))
    canvas.create_text(WIN_WIDTH / 6 * 5, 10, font='Arial 16',
                       text='Time Left: ' + str(game_settings[GAME_TIME_CURRENT]))


def save_score(name, score):
    """
        Save score to file
    """
    lines = []

    if os.path.isfile(game_settings[GAME_SAVEFILE]):
        f = open(game_settings[GAME_SAVEFILE], 'r+')
        for l in f:
            lines.append(l)
        f.close()

    lines.append(name + ': ' + str(score))

    lines.sort(key=lambda s: int(s.split()[1]), reverse=True)

    f = open(game_settings[GAME_SAVEFILE], 'w+')
    for l in lines:
        f.write(l.rstrip('\n') + '\n')
    f.close()


keyboard_buttons = []


def add_key(x, y, size, name, color):
    """
        Add key button to keyboard
    """
    keyboard_buttons.append((x, y, size, name, color))


save_name = ''


def save_score_on_click(event):
    """
        SAVE_SCORE state
        on_click function
    """
    global save_name
    for k in keyboard_buttons:
        x = k[BUTTON_X]
        y = k[BUTTON_Y]
        size = k[BUTTON_SIZE]
        name = k[BUTTON_NAME]
        if (x - 2 * size <= event.x) and (x + 2 * size >= event.x) and (y - size <= event.y) and (y + size >= event.y):
            if name == 'Del':
                save_name = save_name[:-1]
            elif name == 'Esc':
                game_settings[GAME_MODE] = GAME_MODE_MAIN_MENU
            elif name == 'Ok':
                save_score(save_name, game_settings[GAME_SCORE])
                game_settings[GAME_MODE] = GAME_MODE_MAIN_MENU
            else:
                save_name += name


def save_score_loop():
    """
        SAVE_SCORE sate
        loop
    """
    global save_name
    if len(keyboard_buttons) == 0:
        eng_letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Del Esc Ok'.split()
        size = WIN_WIDTH / 6 * 5 / 50
        save_name = ''
        for i in range(3):
            for j in range(10):
                if (i * 10 + j) >= len(eng_letters):
                    break
                add_key(WIN_WIDTH / 12 + 2 * size + j * 5 * size, WIN_HEIGHT / 2 + i * 3 * size, size,
                        eng_letters[i * 10 + j], 'yellow')

    canvas.delete('all')

    canvas.create_text(WIN_WIDTH / 2, WIN_HEIGHT / 5, font='Arial 20', text='Save your score:')

    canvas.create_text(WIN_WIDTH / 2, WIN_HEIGHT / 3, font='Arial 40', text=save_name)

    for k in keyboard_buttons:
        draw_button(k)


def get_score_list():
    """
        Read score from file and return as list
    """
    score_list = []

    if os.path.isfile(game_settings[GAME_SAVEFILE]):
        f = open(game_settings[GAME_SAVEFILE], 'r+')
        for l in f:
            score_list.append(l)
        f.close()

    return score_list


score_list_cache = []


def show_score_on_click(event):
    """
        SHOW_SCORE state
        on_click
    """
    score_list_cache.clear()
    game_settings[GAME_MODE] = GAME_MODE_MAIN_MENU


def show_score_loop():
    """
        SHOW_SCORE sate
        loop
    """
    global score_list_cache
    if len(score_list_cache) == 0:
        score_list_cache = get_score_list()

    canvas.delete('all')

    for i in range(len(score_list_cache)):
        canvas.create_text(WIN_WIDTH / 2, WIN_HEIGHT / 10 + 20 * i, font='Arial 10', text=score_list_cache[i])


def main_on_click(event):
    """
        Call specific on_click function for each state
    """
    if game_settings[GAME_MODE] == GAME_MODE_MAIN_MENU:
        main_menu_on_click(event)
    elif game_settings[GAME_MODE] == GAME_MODE_GAME:
        game_on_click(event)
    elif game_settings[GAME_MODE] == GAME_MODE_SAVE_SCORE:
        save_score_on_click(event)
    elif game_settings[GAME_MODE] == GAME_MODE_SHOW_SCORE:
        show_score_on_click(event)


delay = 50


def main_loop():
    """
        Call specific loop function for each state
    """
    if game_settings[GAME_MODE] == GAME_MODE_MAIN_MENU:
        main_menu_loop()
    elif game_settings[GAME_MODE] == GAME_MODE_GAME:
        game_loop()
    elif game_settings[GAME_MODE] == GAME_MODE_SAVE_SCORE:
        save_score_loop()
    elif game_settings[GAME_MODE] == GAME_MODE_SHOW_SCORE:
        show_score_loop()

    # set timer to execute game_loop(this func) after delay
    root.after(delay, main_loop)


# Main menu settings
size = WIN_HEIGHT / 32
add_button(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 1.5 * size, size, 'Start', 'green')
add_button(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 1.5 * size, size, 'Scorelist', 'yellow')

# Start game
root.bind('<Button-1>', main_on_click)
root.after(delay, main_loop)
root.mainloop()