from turtle import *
from math import *

def move_from_to(cur_pos, new_pos):
    dx = new_pos[0] - cur_pos[0]
    dy = new_pos[1] - cur_pos[1]
    angle = math.atan2(dy, dx)/math.pi*180
    len = math.sqrt(dx*dx + dy*dy)
    left(angle)
    forward(len)
    right(angle)

def draw_circle(r, p_count) :
    d_angle = 2*math.pi/p_count
