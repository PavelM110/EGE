from turtle import *

m = 10
tracer(0)
screensize(500 * m, 500 * m)
lt(90)

pencolor('black')
for i in range(9):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
up()
bk(10 * m)
rt(90)
down()
pencolor('blue')
for i in range(8):
    fd(15 * m)
    lt(90)
    fd(25 * m)
    lt(90)
up()
fd(6 * m)
lt(90)
down()
pencolor('red')
for i in range(7):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
up()

for x in range(-10, 50):
    for y in range(-10, 50):
        goto(x * m, y * m)
        dot(3, 'red')

done()