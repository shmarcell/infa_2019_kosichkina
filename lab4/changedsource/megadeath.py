from graph import *
import math as m
import random

coordinats = []

def show_coordinats(event):
	coordinats.append((event.x, event.y))
	print(coordinats)

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

#Солнце
x=0
for i in range(24):
	penColor(0+5*x, 255-x//10, 255-x)
	brushColor(0+5*x, 255-x//10, 255-x)
	circle(362, 90, 70-(x-1))
	x+=2


#Деревья
penColor('LightGrey')
brushColor('LightGrey')
rectangle(36, 564, 48, 472)
rectangle(79, 450, 91, 401)
rectangle(28, 383, 40, 314)
rectangle(104, 340, 116, 304)
rectangle(88, 311, 100, 222)

penColor('chartreuse')
brushColor('green')
ellipse(94, 91, 50, 80)
ellipse(94, 168, 80, 40)
ellipse(94, 230, 50, 40)
brushColor('lightpink')
circle(117, 50, 10)
circle(148, 169, 10)
circle(44, 167, 10)
brushColor('green')
ellipse(110, 272, 40, 45)
ellipse(110, 315, 40, 20)
ellipse(110, 295, 50, 20)
brushColor('lightpink')
circle(124, 242, 10)
circle(149, 296, 9)
circle(127, 324, 8)
brushColor('green')
ellipse(33, 215, 25, 60)
ellipse(33, 262, 40, 38)
ellipse(33, 330, 30, 40)
brushColor('lightpink')
circle(50, 346, 9)
circle(60, 262, 9)
circle(35, 171, 9)
brushColor('green')
ellipse(83, 329, 38, 42)
ellipse(83, 380, 50, 28)
ellipse(83, 410, 38, 31)
brushColor('lightpink')
circle(102, 423, 9)
circle(118, 380, 9)
circle(46, 380, 9)
circle(98, 309, 9)
brushColor('green')
ellipse(42, 429, 31, 40)
ellipse(42, 459, 50, 25)
ellipse(42, 508, 35, 29)
brushColor('lightpink')
circle(58, 524, 9)
circle(78, 459, 9)
circle(2, 459, 9)
circle(49, 405, 9)





#ACT 1




#Единороги



#bodies
penColor('white')
brushColor('white')
ellipse(448, 308, 15, 8)
ellipse(317, 336, 25, 15)
ellipse(418, 426, 40, 29)
ellipse(294, 479, 55, 38)


#smallestlegs
rectangle(457, 312, 459, 322)
rectangle(452, 314, 454, 324)
rectangle(442, 314, 445, 326)
rectangle(436, 312, 437, 320)
#averagelegs
rectangle(332, 342, 336, 363)
rectangle(322, 346, 326, 365)
rectangle(304, 344, 309, 366)
rectangle(294, 341, 296, 365)
#biggerlegs
rectangle(385, 436, 388, 474)
rectangle(399, 447, 405, 486)
rectangle(429, 448, 437, 476)
rectangle(445, 443, 451, 480)
#biggestlegs
rectangle(330, 492, 337, 538)
rectangle(307, 503, 315, 552)
rectangle(264, 503, 272, 549)
rectangle(246, 495, 249, 556)


#neckies
#biggest
polygon([(347, 495), (381, 499), (298, 441)])
#bigger
polygon([(390, 434), (360, 434), (400, 399)])
#average
polygon([(340, 337), (362, 342), (324, 319)])
#smallest
polygon([(435, 315), (419, 317), (450, 298)])

#head
#mainheads
#additionalmouths
ellipse(439-20, 294+25, 5, 2)
ellipse(436-20, 297+25, 2, 1)

ellipse(331+25, 296+45, 10, 6)
ellipse(338+25, 300+45, 5, 2)

ellipse(391-35, 370+67, 12, 7)
ellipse(381-35, 373+67, 7, 4)

ellipse(329+40, 414+80, 15, 9)
ellipse(339+40, 417+80, 10, 6)





penColor('mediumorchid')
brushColor('mediumorchid')
circle(333+40, 414+80, 5)
circle(390-35, 371+67, 4)
circle(334+25, 297+45, 3)
circle(439-20, 295+25, 2)

penColor('black')
brushColor('black')
circle(333+40, 414+80, 2)
circle(390-35, 371+67, 2)
circle(334+25, 297+45, 1)
circle(439-20, 295+25, 1)

penColor('white')
brushColor('white')
point(333, 414)
point(332, 413)
point(331, 412)


point(390, 371)
point(391, 370)
point(392, 369)

point(334, 297)
point(333, 296)

point(439, 295)

penColor('PaleVioletRed')
brushColor('PaleVioletRed')
polygon([(329+40, 408+80), (329+40, 370+80), (321+40, 408+80)])
polygon([(389-35, 365+67), (389-35, 326+67), (396-35, 365+67)])
polygon([(333+25, 292+45), (333+25, 260+45), (327+25, 292+45)])
polygon([(439-20, 291+25), (439-20, 279+25), (441-20, 291+25)])




#ACT 2





#Грива и хвост самого большого единорога
brushColor('PaleTurquoise')
penColor('PaleTurquoise')
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(307+40+t, 433+80+q, 11+w, 11-r)
brushColor('PaleVioletRed')
penColor('PaleVioletRed')
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(307+40+t, 433+80+q, 11+w, 11-r)
brushColor('PaleGreen')
penColor('PaleGreen')
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(307+40+t, 433+80+q, 12+w, 12-r)

brushColor('PaleTurquoise')
penColor('PaleTurquoise')
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(218+t, 489+q, 12+w, 12-r)
brushColor('PaleVioletRed')
penColor('PaleVioletRed')
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(218+t, 497+q, 12+w, 12-r)
brushColor('PaleGreen')
penColor('PaleGreen')
ellipse(235, 472, 10, 13)
for i in range(2):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(218+t, 495+q, 12+w, 12-r)
brushColor('khaki')
penColor('khaki')
for i in range(2):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(218+t, 489+q, 12+w, 12-r)
brushColor('PaleVioletRed')
penColor('PaleVioletRed')
for i in range(3):
	t=random.randint(-15, 15)
	q=random.randint(-15, 15)
	w=random.randint(-7, 7)
	r=random.randint(-7, 7)
	ellipse(214+t, 535+q, 12+w, 12-r)

#Грива и хвост единорога, что чуть меньше самого большого
brushColor('PaleTurquoise')
penColor('PaleTurquoise')
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(413-35+t, 380+67+q, 10+w, 10-r)
brushColor('PaleVioletRed')
penColor('PaleVioletRed')
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(413-35+t, 380+67+q, 10+w, 10-r)
brushColor('PaleGreen')
penColor('PaleGreen')
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(413-35+t, 380+67+q, 10+w, 10-r)
brushColor('khaki')
penColor('khaki')
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(413-35+t, 380+67+q, 10+w, 10-r)
brushColor('khaki')
penColor('khaki')
ellipse(460, 426, 10, 7)
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(461+t, 428+q, 10+w, 10-r)
brushColor('PaleTurquoise')
penColor('PaleTurquoise')
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(461+t, 428+q, 10+w, 10-r)
brushColor('PaleVioletRed')
penColor('PaleVioletRed')
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(475+t, 458+q, 10+w, 10-r)
brushColor('PaleGreen')
penColor('PaleGreen')
for i in range(2):
	t=random.randint(-10, 10)
	q=random.randint(-10, 10)
	w=random.randint(-3, 3)
	r=random.randint(-3, 3)
	ellipse(461+t, 428+q, 10+w, 10-r)

#Грива и хвост единорога, что чуть больше самого маленького
brushColor('PaleTurquoise')
penColor('PaleTurquoise')
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(318+25+t, 307+45+q, 7+w, 7-r)
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(283+t, 339+q, 7+w, 7-r)
brushColor('PaleGreen')
penColor('PaleGreen')
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(318+25+t, 307+45+q, 7+w, 7-r)
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(283+t, 339+q, 7+w, 7-r)
brushColor('PaleVioletRed')
penColor('PaleVioletRed')
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(318+25+t, 307+45+q, 7+w, 7-r)
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(283+t, 339+q, 7+w, 7-r)
brushColor('PaleTurquoise')
penColor('PaleTurquoise')
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(318+25+t, 307+45+q, 7+w, 7-r)
for i in range(2):
	t=random.randint(-8, 8)
	q=random.randint(-8, 8)
	w=random.randint(-2, 2)
	r=random.randint(-2, 2)
	ellipse(283+t, 339+q, 7+w, 7-r)

#Грива и хвост самого маленького единорога
brushColor('PaleTurquoise')
penColor('PaleTurquoise')
ellipse(445-20, 298+25, 3, 2)
ellipse(466, 312, 3, 1)
ellipse(464, 320, 4, 3)
brushColor('PaleGreen')
penColor('PaleGreen')
ellipse(446-20, 300+25, 3, 2)
ellipse(465, 314, 3, 2)
ellipse(464, 321, 4, 2)
brushColor('PaleVioletRed')
penColor('PaleVioletRed')
ellipse(445-20, 299+25, 2, 1)
ellipse(464, 308, 4, 3)
ellipse(466, 321, 5, 2)
brushColor('PaleTurquoise')
penColor('PaleTurquoise')
ellipse(445-20, 298+25, 4, 1)
ellipse(468, 318, 3, 2)

onMouseDown(show_coordinats)

run()