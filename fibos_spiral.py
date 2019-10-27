from turtle import *
from fibos import fibos
import sys
WIN_SIZE = 500
setup(width=WIN_SIZE, height=WIN_SIZE)
speed(0)


class FiboStyle(object):
    # angle 0-360
    # direction -1|1
    def __init__(self, width=2, phase=0, angle=90, direction=1, colors=['#3399ff']):
        self.width = width
        self.phase = phase
        self.angle = angle
        self.direction = direction
        self.colors = colors


def fibos_spiral(fibo_style=FiboStyle()):

    angle = fibo_style.angle * fibo_style.direction
    loop = 9
    init_step = 2
    colors = fibo_style.colors
    colors_count = len(colors)

    go_home()
    width(fibo_style.width)
    right(fibo_style.phase)

    for i in range(0, loop):
        pencolor(colors[i % colors_count])
        circle(init_step, angle, init_step)
        last_step = init_step
        init_step = init_step+last_step


def go_home():
    up()
    home()
    down()


def fibos_spirals(count, direction=1, angle=90, colors=['#3399ff']):

    for i in range(0, count):
        fibo_style = FiboStyle(
            phase=i*360/count, angle=angle, direction=direction, colors=colors)
        fibos_spiral(fibo_style)


def draw_style(style=0):

    angle_a = 90
    angle_b = 90

    if style == 1:
        bgcolor("#000000")
        colors_a = ['#ff9933']
        count_a = 21
        colors_b = ['#ffff00']
        count_b = 21
    elif style == 2:
        colors_a = ['#ff9933', '#33ff99', '#3399ff']
        colors_b = ['#99ff33', '#3399ff', '#ff9933']
        count_a = 13
        count_b = 13
        angle_a = 180
        angle_b = 180
    elif style == 3:
        bgcolor("#3399ff")
        colors_a = ['#3399ff']
        colors_b = ['#ffffff']
        count_a = 0
        count_b = 21

    else:
        print("STYLES:\n[1]sunflower\n[2]donut\n[3]vortex")
        colors_a = ['#ffffff']
        colors_b = ['#3399ff']
        count_a = 0
        count_b = 21

    fibos_spirals(count=count_a, angle=angle_a, colors=colors_a)
    fibos_spirals(count=count_b, angle=angle_b, direction=-1, colors=colors_b)


if __name__ == "__main__":
    style = 0
    if len(sys.argv) > 1:
        style = int(sys.argv[1])

    draw_style(style)

    done()
