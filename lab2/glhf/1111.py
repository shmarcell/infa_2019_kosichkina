import turtle

def draw_circle(d_len, d_angle, rotate_func):
    for i in range(int(360/d_angle)):
        turtle.forward(d_len)
        rotate_func(d_angle)

turtle.left(90)
for i in range(7):
    draw_circle(0.3*i + 1, 2, turtle.left)
    draw_circle(0.3*i + 1, 2, turtle.right)
a=input()