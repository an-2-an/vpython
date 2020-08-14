from vpython import *

mySphere = sphere(pos=vector(-3, 0, 0), radius=0.3, color=color.green)
brick1 = box(pos=vector(-4.5, 0, 0), size=vector(0.2, 0.2, 0.2), color=color.yellow)
brick2 = box(pos=vector(4.5, 0, 0), size=vector(0.2, 0.2, 0.2), color=color.yellow)

dx = 0.2

while True:
    rate(10)
    if -4 < mySphere.pos.x < 4:
        pass
    else:
        dx = dx * -1
    mySphere.pos.x = mySphere.pos.x + dx
    print(mySphere.pos)

print('the end')