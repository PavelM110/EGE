from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(13):
    fd(13 * m)
    rt(90)
    fd(5 * m)
up()
rt(90)
fd(7 * m)
lt(90)
fd(10 * m)
down()
for i in range(23):
    fd(8 * m)
    lt(90)
    fd(11 * m)
    lt(90)
up()

for x in range(-5, 30):
    for y in range(-5, 30):
        goto(x * m, y * m)
        dot(3, 'red')

done()