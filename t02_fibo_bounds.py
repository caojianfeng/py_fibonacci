import math
from turtle import *
from fibos import fibos
from math_ex import gold_offset

WIN_SIZE = 500

setup (width=WIN_SIZE,height=WIN_SIZE)

def fly_home():
    offset = gold_offset(WIN_SIZE,'start')
    penup()
    home()
    forward(offset)
    right(90)
    forward(offset)
    left(270)
    pendown()

def draw_size(radius,fibo):
    if fibo < 2:
        return

    penup()

    text_pod = radius/2
    forward(text_pod)
    left(90)
    forward(text_pod)
    left(90)
    
    pendown()
    dot(3)
    write(fibo,align='center')
    penup()

    
    forward(text_pod)
    left(90)
    forward(text_pod)
    left(90)
    
    pendown()

def draw_bound(radius,fibo):
    for i in range(4):
        forward(radius)
        left(90)
    draw_size(radius,fibo)



def draw_fibo(radius):
    step = int(radius * math.pi/2)
    circle(radius, 90, step)

def draw_bounds(fibo_list,unit):
    fly_home()
    pencolor('#3399ff')
    width(1)
    
   
    for fibo in fibo_list:
        radius = fibo * unit
        draw_bound(radius,fibo)
        forward(radius)
        left(90)
        forward(radius)
    
def draw_fibos(fibo_list,unit):
    fly_home()
    pencolor('#ff9933')
    width(2)
    
    for fibo in fibo_list:
        radius = fibo * unit
        draw_fibo(radius)

if __name__ == "__main__":            
    hideturtle()
    speed(0)

    fibo_list = fibos(9)
    unit = 6
    draw_bounds(fibo_list,unit)
    draw_fibos(fibo_list,unit)

    
    done()
