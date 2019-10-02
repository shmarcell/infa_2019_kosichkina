#!/usr/bin/python3

from pyrob.api import *


@task
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    f=12 
    for i in range(6):
        for p in range(f):
            move_down()
            fill_cell()
        move_right()
        fill_cell()
        f=f-1
        for k in range(f):
            move_up()
            fill_cell()
        f=f-1
        move_right()
        move_down()
        fill_cell()
    move_down()
    for n in range(12):
        move_left()


if __name__ == '__main__':
    run_tasks()
