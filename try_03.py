from vpython import *
from math import sin, cos

sun = sphere(pos=vector(0, 0, 0), radius=0.3, color=color.yellow)
mySphere = sphere(pos=vector(1, 0, 0), radius=0.2, color=color.green)
mySphere2 = sphere(pos=vector(0, 1, 0), radius=0.12, color=color.blue)

time = 0
dt = 0.1

while True:
    rate(10)
    mySphere.pos.x = cos(time)
    mySphere.pos.y = sin(time)
    mySphere2.pos.y = cos(time * 0.8)
    mySphere2.pos.z = sin(time * 0.8)
    time += dt

print('the end')