from graph import *

penColor(255,0,255)
penSize(5)
brushColor("blue")
rectangle(100, 100, 300, 200)
brushColor("yellow")
polygon([(100,100), (200,50),
         (300,100), (100,100)])
penColor("white")
brushColor("green")
circle(200, 150, 50)

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
rectangle (x1, y1, x2, y2)
h = (x2 - x1) / (N + 1)
x = x1 + h
for i in range(N):
  line(x, y1, x, y2)
  x += h

run()
