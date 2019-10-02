#!/usr/bin/python3

from pyrob.api import *

def can_move(v_move, h_move):
    if h_move == 1:
        h_can = not wall_is_on_the_right()
    else:
        h_can = not wall_is_on_the_left()
    if v_move == 1:
        v_can = not wall_is_above()
    else:
        v_can = not wall_is_beneath()
    return h_can or v_can

def move_if_can(v_move, h_move):
    if h_move == 1 and not wall_is_on_the_right():
        move_right()
    elif h_move == -1 and not wall_is_on_the_left():
        move_left()
    if v_move == 1 and not wall_is_above():
        move_up()
    elif v_move == -1 and not wall_is_beneath():
        move_down()


@task
def task_8_21():
    if wall_is_above():
        v_move = -1
    else:
        v_move = 1
    if wall_is_on_the_left():
        h_move = 1
    else:
        h_move = -1
    while can_move(v_move, h_move):
        move_if_can(v_move, h_move)


if __name__ == '__main__':
    run_tasks()
