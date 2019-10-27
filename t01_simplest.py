from turtle import *
import math
speed(0)

last_step = 0
this_step = 10
for i in range (8):
    circle(this_step,90,int(this_step*(math.pi)))
    this_step,last_step = this_step+last_step,this_step
    
done()
