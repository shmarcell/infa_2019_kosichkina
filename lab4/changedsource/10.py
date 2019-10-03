from graph import *
import math as m
import random 

def ellipse(x, y, A, B):
	n=200
	tochki_ellipsa=[]
	for i in range(n):
		tochki_ellipsa.append((x+A*m.cos(2*m.pi*i/n), y+B*m.sin(2*m.pi*i/n)))
	polygon(tochki_ellipsa)

penColor('chartreuse')
brushColor('chartreuse')
rectangle(0 , 300 , 500, 600)

penColor('aqua')
brushColor('aqua')
rectangle(0 , 300 , 500, 0)

penColor('yellow')
brushColor('yellow')
circle(470 , 80,  100)

# дерево
penColor('lightgrey')
brushColor('lightgrey')
rectangle(40, 400, 60, 200)

penColor('green')
brushColor('green')
ellipse(50, 330, 40, 30)
ellipse(50, 280, 80, 40)
ellipse(50, 215, 40, 60)

penColor('lightpink')
brushColor('lightpink')
circle(72, 348, 10)
circle(103, 281, 10)
circle(3, 281, 10)
circle(69, 178, 10)



# единорог
penColor('white')
brushColor('white')
ellipse(345, 430, 90, 40)

polygon([(332, 417), (410, 417), (410, 326)])

ellipse(404, 340, 25, 15)
ellipse(424, 348, 25, 12)

penColor('mediumorchid')
brushColor('mediumorchid')
circle(410, 339, 8)

penColor('black')
brushColor('black')
circle(413, 339, 3)

penColor('white')
for i in range(7):
	point(413-i, 339-i)
for i in range(5):
	point(412-i, 337-i)
	point(411-i, 338-i)
point(410, 336)
point(411, 337)

penColor('PaleVioletRed')
brushColor('PaleVioletRed')
polygon([(407, 326), (407, 292), (393, 326)])

penColor('white')
brushColor('white')
rectangle(398, 450, 409, 501)
rectangle(368, 456, 384, 523)
rectangle(299, 457, 313, 508)
rectangle(269, 451, 280, 518)

for i in range(5):
	brushColor('PaleVioletRed')
	penColor('PaleVioletRed')
	ellipse(384 - 4*i, 327 + 15*i, 15 + 3*(-1)**i, 9+ 2*(-1)**i)

brushColor('PaleVioletRed')
penColor('PaleVioletRed')
ellipse(237, 426, 20, 10)
ellipse(257, 492, 17, 5)
ellipse(213, 483, 21, 9)
ellipse(235, 482, 11, 8)
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(245+t, 465+q, 15+w, 15-r)

brushColor('PaleTurquoise')
penColor('PaleTurquoise')
ellipse(375, 343, 19, 7)
ellipse(362, 366, 20, 8)
ellipse(355, 383, 15, 5)
ellipse(244, 467, 17, 6)
ellipse(210, 466, 15, 12)
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(250+t, 472+q, 15+w, 15-r)

brushColor('PaleGreen')
penColor('PaleGreen')
ellipse(345, 387, 17, 10)
ellipse(367, 353, 12, 5)
ellipse(233, 433, 15, 5)
ellipse(236, 500, 21, 12)
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(233+t, 470+q, 15+w, 15-r)

brushColor('khaki')
penColor('khaki')
ellipse(360, 376, 19, 7)
ellipse(377, 334, 13, 8)
ellipse(242, 414, 21, 10)
ellipse(235, 441, 22, 12)
ellipse(247, 510, 12, 5)
ellipse(247, 510, 13, 8)


run()
