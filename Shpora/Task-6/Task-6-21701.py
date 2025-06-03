from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()

for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()

for x in range(-2, 35):
    for y in range(-2, 35):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()