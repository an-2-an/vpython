from vpython import *
import itertools

# sphere(pos=vector(-1,0,0), color=color.green, radius=0.4)
# sphere(pos=vector(0,1,0), color=color.red, radius=0.5)

points = itertools.product((-1, 1), (-1, 1), (-1, 1))

# for x, y, z in points:
#     # print(x, y, z)
#     sphere(pos=vector(x, y, z), color=color.yellow, radius=0.1)

for p1, p2 in itertools.combinations(points, 2):
    # print(p1, p2)
    if sum(1 for c1, c2 in zip(p1, p2) if c1 == c2) in (0, 2):
        print(p1, p2)
        curve(pos=[p1, p2], color=color.red, radius=0.1)