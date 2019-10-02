from graph import *
#thomas has never seen such shit before
def ellipse(x, y, a, b, clr):
    penColor(clr)
    brushColor(clr)
    moveTo(x - a, y - b)
    X = -a
    Y = -b
    for i in range(2 * b):
        for ii in range(2 * a):
            if X ** 2 / a ** 2 + Y ** 2 / b ** 2 <= 1:
                point(x + X, y + Y)
            X = X + 1
            moveTo(X + x, Y + y)
        X = -a
        Y = Y + 1
        moveTo(x - a, y + Y)

brushColor("blue")
rectangle(0, 0, 500, 300)
brushColor("green")
rectangle(500, 300, 0, 600)

penSize(0)

# gurl
# triangle
brushColor("pink")
polygon([(225,225), (250,300),
         (200,300), (225,225)])
# armsright
line(230, 240, 250, 250)
line(250, 250, 265, 230)
line(220, 240, 185, 265)
# legsright
line(215, 300, 215, 340)
line(230, 300, 230, 340)
line(215, 340, 205, 340)
line(230, 340, 240, 340)
#rightface
brushColor("beige")
circle(225, 220, 15)

# gurl
# triangle
brushColor("pink")
polygon([(305,225), (330,300),
         (280,300), (305,225)])
# armsright
line(300, 240, 280, 250)
line(280, 250, 265, 230)
line(310, 240, 345, 265)
# legsright
line(295, 300, 295, 340)
line(310, 300, 310, 340)
line(295, 340, 285, 340)
line(310, 340, 320, 340)
#rightface
brushColor("beige")
circle(305, 220, 15)



# boi
# ellipse
ellipse(143,265,17,40, "grey")
# legsleft
line(135, 300, 125, 340)
line(150, 300, 150, 340)
line(125, 340, 115, 340)
line(150, 340, 160, 340)
# armsleft
line(185, 265, 150, 240)
line(95, 265, 130, 240)
# leftface
brushColor("beige")
circle(140, 220, 15)


# boi
# ellipse
ellipse(393,265,17,40, "grey")
# legsleft
line(385, 300, 375, 340)
line(400, 300, 400, 340)
line(375, 340, 365, 340)
line(400, 340, 410, 340)
# armsleft
line(435, 265, 400, 240)
line(345, 265, 380, 240)
# leftface
brushColor("beige")
circle(390, 220, 15)









# side objects
# heart
line(83, 220, 98, 268)
brushColor("red")
circle(80, 196, 8)
circle(70, 200, 8)
polygon ([(83, 220), (65, 205),
         (88, 195), (83, 220)])

# cone
line(270, 160, 260, 260)
brushColor("yellow")
polygon([(270,160), (240, 115),
         (295, 115), (270,160)])
brushColor("red")
circle(270, 100, 15)
brushColor("white")
circle(255, 110, 15)
brushColor("brown")
circle(285, 110, 15)


# cone
line(438, 224, 434, 264)
brushColor("yellow")
polygon([(438,224), (426, 208),
         (450, 208), (438, 224)])
brushColor("red")
circle(438, 200, 8)
brushColor("white")
circle(430, 204, 8)
brushColor("brown")
circle(446, 204, 8)




run()
