from turtle import *

tracer(0)
m = 10
screensize(10_000, 10_000)

rt(45)
for i in range(10):
    rt(45)
    fd(203 * m)
    rt(45)
up()
bk(40 * m)
rt(45)
down()
for i in range(5):
    fd(20 * m)
    lt(90)
up()

for x in range(-202, -160):
    for y in range(-240, -202):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()