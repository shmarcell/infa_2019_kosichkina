from turtle import *

def draw_koch_line(length, depth):
    if depth == 0:
        forward(length)
    else:
        draw_koch_line(length/3, depth-1)
        left(60)
        draw_koch_line(length/3, depth-1)
        right(120)
        draw_koch_line(length/3, depth-1)
        left(60)
        draw_koch_line(length/3, depth-1)



def draw_snowflake(l, depth):
    a = (3)**(1/2)*l
    penup()
    left(90)
    forward(l)
    right(90+60)
    pendown()

    draw_koch_line(a, depth)
    right(120)
    draw_koch_line(a, depth)
    right(120)
    draw_koch_line(a, depth)

    right(120+30)
    penup()
    forward(l)
    left(90)
depth=int(input())
shape('turtle')

draw_snowflake(200,depth)