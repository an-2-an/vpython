from vpython import *
from math import pi

g1 = shapes.gear(n=20)
gear1 = extrusion(path=[vector(0, 0, -0.3), vector(0, 0, 0.3)], shape=g1, color=color.blue)

gear2 = extrusion(path=[vector(2, 0, -0.6), vector(2, 0, 0.6)], shape=g1, color=color.green)
gear2.rotate(axis=vector(0, 0, 1), angle=pi / 20)

gear3 = extrusion(path=[vector(2, 2, -0.2), vector(2, 2, 0.2)], shape=g1, color=color.red)

dt = 0.1

while(True):
    rate(5)
    gear1.rotate(angle=dt, axis=vector(0, 0, 1))
    gear2.rotate(angle=-dt, axis=vector(0, 0, 1))
    gear3.rotate(angle=dt, axis=vector(0, 0, 1))
