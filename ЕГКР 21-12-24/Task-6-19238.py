from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(8):
    fd(16 * m)
    rt(90)
    fd(22 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for i in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()

for x in range(-10, 100):
    for y in range(-10, 100):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()