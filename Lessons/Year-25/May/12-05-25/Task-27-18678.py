from math import dist
import turtle as t

m = 10
t.tracer(0)
t.screensize(10000, 10000)
t.up()


with open('27B_18678.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for line in file:
        x, y = map(float, line.split())
        if y < 2.5: cl1.append([x, y])
        else:
            if 1 <= x <= 6: cl2.append([x, y])

clusters = [cl1, cl2]

colors = ['red', 'blue', 'green']

for cl, col in zip(clusters, colors):
    for x, y in cl:
        t.goto(x * m, y * m)
        t.dot(3, col)

t.update()
t.done()

def centroid(cl):
    dists = []
    for dot in cl:
        sum_d = 0
        for dot2 in cl:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

centers = [centroid(i) for i in clusters]

p_x = sum(i[0] for i in centers) / len(clusters)
p_y = sum(i[1] for i in centers) / len(clusters)

print(int(p_x * 100_000), int(p_y * 100_000))