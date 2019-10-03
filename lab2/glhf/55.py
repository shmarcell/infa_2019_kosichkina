from turtle import *
n=10
for i in range(10):
    forward(n)
    left(90)
    forward(n)
    left(90)
    forward(n)
    left(90)
    forward(n)
    penup()
    forward(10)
    left(90)
    backward(10)
    n += 20
    pendown()
