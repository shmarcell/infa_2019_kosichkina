import turtle
import math

def draw_circle(d_len, d_angle):
    for i in range(int(360/d_angle)):
        turtle.forward(d_len)
        turtle.left(d_len)

for i in range(1, 4, 1):
    draw_circle(1, 1)
    turtle.left(180)
    draw_circle(1, 1)
    turtle.right(120)
a= input()