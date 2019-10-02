#!/usr/bin/python3

from pyrob.api import *


@task
def task_6_6():
    k=0
    while not wall_is_on_the_right():
        move_right()
        k=k+1
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
    for i in range(k):
        move_left()


if __name__ == '__main__':
    run_tasks()
