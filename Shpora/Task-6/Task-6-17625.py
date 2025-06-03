from turtle import *

lt(90)
m = 10
tracer(0)

for i in range(10):
    fd(22 * m)
    rt(90)
    fd(16 * m)
    rt(90)

up()
fd(m)
rt(90)
fd(m)
lt(90)
down()

for i in range(10):
    fd(72 * m)
    rt(90)
    fd(79 * m)
    rt(90)

up()

for x in range(-10, 20):
    for y in range(-10, 20):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()