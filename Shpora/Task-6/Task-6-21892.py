from turtle import *

m = 30
tracer(0)
lt(90)
screensize(1000, 1000)

rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)

up()

for x in range(-15, 10):
    for y in range(-17, 10):
        goto(x * m, y * m)
        dot(3, 'red')


update()
done()