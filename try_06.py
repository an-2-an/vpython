from vpython import *
from math import sin, cos, pi

# print(scene.camera.pos)
# print(scene.camera.axis)
scene.camera.pos = vector(1, -1, 2)
scene.camera.axis = vector(-0.3, 0.3, -1)

longHand = arrow(pos=vector(0, 0, 0), axis=vector(0, 0.8, 0), color=color.blue, radius=0.05)
shortHand = arrow(pos=vector(0, 0, 0), axis=vector(0, 0.6, 0), color=color.red, radius=0.08)

box(pos=vector(0, 1, 0), size=vector(0.02, 0.1, 0.02))
box(pos=vector(0, -1, 0), size=vector(0.02, 0.1, 0.02))
box(pos=vector(-1, 0, 0), size=vector(0.1, 0.02, 0.02))
box(pos=vector(1, 0, 0), size=vector(0.1, 0.02, 0.02))
box(pos=vector(0, 0, 0), size=vector(0.02, 0.02, 0.25), color=color.green)

n = 24
dots = [vector(cos(t * 2 * pi / n) * 1.1, sin(t * 2 * pi / n) * 1.1, 0) for t in range(n + 1)]
curve(pos=dots, radius=0.02)

time = 0
dt = 0.1
speed = -0.5

while True:
    rate(10)
    longHand.rotate(angle=speed, axis=vec(0, 0, 1))
    shortHand.rotate(angle=speed / 12, axis=vec(0, 0, 1))
    time += dt

