from math import dist
import turtle as t

t.tracer(0)
m = 1
colors = ['red', 'blue', 'green']
t.up()

with open('27B_18056.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for line in file:
        x, y = map(float, line.split())
        # if y > -1:
        #     if x < 1: cl1.append([x, y])
        # else:
        #     if x > 0: cl2.append([x, y])
        if y < .4 * x - .4:
            if x > 0:
                cl1.append([x, y])
        else:
            if y < -1 * x +4:
                if y < 4: cl2.append([x, y])
            else:
                if y < 6: cl3.append([x, y])
    clusters = [cl1, cl2, cl3]

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

for c, cl in zip(colors, clusters):
    for x, y in cl:
        t.goto(x * 10, y * 10)
        t.dot(3, c)

t.update()
t.done()

centers = [centroid(i) for i in clusters]

p_x = sum(i[0] for i in centers) / len(centers)
p_y = sum(i[1] for i in centers) / len(centers)

print(abs(int(p_x * 100_000)), abs(int(p_y * 100_000)))