import turtle

def draw_circle(d_len, d_angle):
    for i in range(int(360/d_angle)):
        turtle.forward(d_len)
        turtle.left(d_len)

turtle.penup()
turtle.back(200)
turtle.pendown()
turtle.left(90)
for i in range(5):
    draw_circle_half(1, 1)
    draw_circle_half(0.5, 2)
a=input()