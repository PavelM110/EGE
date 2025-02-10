from turtle import *

tracer(0)
lt(90)
up()
m = 10

for i in range(2):
    down()
    for j in range(2):
        fd(8 * m)
        rt(90)
        fd(8 * m)
        rt(90)
    up()
    fd(6 * m)
    rt(90)
    fd(6 * m)
    lt(90)
rt(180)
fd(4 * m)
down()
for i in range(4):
    fd(8 * m)
    rt(270)

up()

for x in range(-10, 30):
    for y in range(-10, 30):
        goto(x * m, y * m)
        dot(4, 'white')

done()