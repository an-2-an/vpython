from vpython import *
import itertools
import random

SIZE = 3

vertices = itertools.product(range(-SIZE, SIZE+1), range(-SIZE, SIZE+1), range(-SIZE, SIZE+1))
colors = [color.red, color.green, color.blue, color.white, color.yellow, color.orange,
          color.purple, color.cyan, color.magenta]


balls = [sphere(pos=vector(*v), color=random.choice(colors), radius=0.45) for v in vertices]

