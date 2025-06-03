from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()

fd(8 * m)
rt(90)
bk(3 * m)
lt(90)

down()

for i in range(8):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)

up()

for x in range(-10, 20):
    for y in range(-10, 20):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()