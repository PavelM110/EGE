from turtle import *

m = 10
tracer(0)
lt(90)
screensize(200 * m, 200 * m)

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(m)
rt(90)
fd(5 * m)
lt(90)
down()
for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)
up()
for x in range(-10, 60):
    for y in range(-10, 60):
        goto(x * m,  y * m)
        dot(3, 'red')

done()