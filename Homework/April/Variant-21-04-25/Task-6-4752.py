from turtle import *

m = 30
screensize(10_000, 10_000)
tracer(0)
lt(90)

for i in range(15):
    fd(4 * m)
    rt(60)

up()

for x in range(1, 10):
    for y in range(1, 10):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()