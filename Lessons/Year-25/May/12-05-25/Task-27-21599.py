from math import dist
import turtle

turtle.tracer(0)
turtle.penup()
turtle.screensize(10_000, 10_000)
m = 10


with open('27_B_21599.txt')as file:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    cl6 = []
    for line in file:
        x, y = map(float, line.split())
        # if y < -7: cl1.append([x, y])
        # else:
        #     if y > x - 10: cl2.append([x, y])
        #     else: cl3.append([x, y])
        if y < -5: cl1.append([x, y])
        else:
            if y < .8 * x: cl2.append([x, y])
            else:
                if x > -9:
                    if y < 2 * x + 11: cl3.append([x, y])
                    else: cl4.append([x, y])
                else:
                    if y < -2 * x - 26: cl5.append([x, y])
                    else: cl6.append([x, y])

clusters = [cl1, cl2, cl3, cl4, cl5, cl6]
colors = ['red', 'blue', 'green', 'yellow', 'black', 'purple']

for cl, col in zip(clusters, colors):
    for x, y in cl:
        turtle.goto(x * m, y * m)
        turtle.dot(3, col)

turtle.update()
turtle.done()

def centroid(cl):
    dists = []
    for dot in cl:
        sum_d = 0
        for dot2 in cl:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

centers = [centroid(i) for i in clusters]

p_x = sum(i[0] for i in centers) / len(centers)
p_y = sum(i[1] for i in centers) / len(centers)

print(abs(int(p_x * 10_000)), abs(int(p_y * 10_000)))