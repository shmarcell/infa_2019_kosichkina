#!/usr/bin/python3

from pyrob.api import *


@task
def task_4_3():
    move_right()
    for n in range(6):
        for i in range(27):
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        for i in range(27):
            fill_cell()
            move_left()
        fill_cell()
        move_down()


if __name__ == '__main__':
    run_tasks()
