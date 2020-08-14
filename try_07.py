from vpython import *
import random
from math import sin

print(scene.camera.pos)
print(scene.camera.axis)

scene.camera.pos = vector(0, 0, 1.7)
scene.camera.axis = vector(0, 0, -1.7)

balls = [sphere(pos=vector(1-random.random(), 1-random.random(), 1-random.random()), radius=0.05)
         for i in range(100)]

time = 0
dt = 0.1
speed = 0.5

while True:
    rate(5)
    scene.camera.axis = vector(sin(time)/2, sin(time)/2, -1.7)
    time += dt


