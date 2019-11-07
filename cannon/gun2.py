from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
X = 800
Y = 600
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        print(self.x ** 2 + self.y ** 2)
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )
        print(self.vx ** 2 + self.vy ** 2)

    def move(self):
        dt = 3e-1
        g = 10
        g /= 2
        s = 0.7
        z = 0.9
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME

        if abs(self.x - X / 2) > X / 2 - self.r:
            if abs(self.vx) < 4:
                self.vx = 0
            else:
                self.vx = -self.vx * s
                self.vy = self.vy * z
        if self.y + self.r > 0.95 * Y:
            if self.vy < 4:
                self.vy = 0
                self.vx = 0
            else:
                self.vy = -self.vy * s
                self.vx = self.vx * z
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += g * dt
        self.set_coords()
        # FIXED 1/2

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME

        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        # self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )
        # canv.coords(self.id, 20, 450,
        # 20 + 20 * math.cos(self.an),
        # 450 + 20  * math.sin(self.an)
        # )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self, num):
        self.points = 0
        self.live = 1
        self.num = num
        if num == 1:
            self.px = 30
        else:
            self.px = 800 - 30
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(self.px, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = self.y0 = rnd(200, 600 - 200)
        r = self.r = rnd(5, 50)
        self.phi = 2 * math.pi * rnd(1, 100) / 100

        self.A1 = rnd(r, 60)
        self.A2 = rnd(r, 60)
        self.A3 = rnd(r, 60)
        self.A0 = rnd(190, 250) - self.A1 - self.A2 - self.A3
        if self.num == 1:
            self.color = 'orange'
        else:
            self.color = 'red'
        color = self.color
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        dphi = 3e-3 * rnd(1, 25)
        self.phi += dphi
        self.y = self.y0 + self.A0 * math.sin(self.phi) + self.A1 * math.cos(self.phi) + self.A2 * math.sin(
            2 * self.phi) + self.A3 * math.cos(2 * self.phi)
        x = self.x
        y = self.y
        r = self.r
        canv.coords(self.id, x - r, y - r, x + r, y + r)


t1 = target(0)
t2 = target(1)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    hits = 0
    z = 0.03 / 2
    t1.live = 1
    t2.live = 1
    # while t1.live or balls:
    while t1.live or t2.live or balls:
        for b in balls:
            # print('Good!')
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                ##canv.bind('<Button-1>', '')
                ##canv.bind('<ButtonRelease-1>', '')
                ##canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                ##canv.update()
                ##time.sleep(1.5)
                ##clear()
                # root.after(5000, clear())
                # time.sleep(z*100)
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if t1.live + t2.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                canv.update()
                time.sleep(1.5)
                clear()
        if t1.live:
            t1.move()
        if t2.live:
            t2.move()
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()


def clear():
    for b in balls:
        canv.delete(b.id)
    canv.delete(gun)
    canv.delete(t1)
    canv.delete(t2)
    canv.update()
    # canv.itemconfig(screen1, text='')
    root.after(2000, new_game())


new_game()

mainloop()