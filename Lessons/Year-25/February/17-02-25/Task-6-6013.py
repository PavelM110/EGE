from turtle import *

tracer(0)
m = 50
screensize(200 * m, 200 * m)
lt(90)

for i in range(2):
    rt(120)
    fd(7 * m)
rt(300)
for i in range(2):
    rt(120)
    fd(7 * m)
up()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(3, 'red')

done()