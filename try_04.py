from vpython import *
from math import sin, cos, asin, acos

sun = sphere(pos=vector(0, -1, 0), radius=0.2, color=color.yellow)
line = curve(pos=[vector(0, 0, 0), vector(0, -1, 0)], color=color.yellow)
# print(line.axis)
curve(vector(-1, 0, 0), vector(1, 0, 0))
box(pos=vector(0, -1, 0), size=(vector(0.03, 0.1, 0.03)))
box(pos=vector(0, -1, 0), size=(vector(0.1, 0.03, 0.03)))

time = 0
dt = 0.1
A = 0.8
L = 1

while True:
    rate(10)
    x = A * cos(time)
    y = -(L ** 2 - x ** 2)**0.5
    # print(x, y)
    sun.pos.x = x
    sun.pos.y = y
    line.axis = vector(-y, x, 0)
    time += dt


print('the end')