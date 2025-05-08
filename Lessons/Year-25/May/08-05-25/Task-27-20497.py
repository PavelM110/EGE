from math import dist
import turtle as t

with open('27.19.B_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file if i]

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return max(dists)[1]

eps = 4
clusters = []

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 4:
        clusters.append(cluster)

print([len(i) for i in clusters])

centers = [centroid(i) for i in clusters if len(i) > 4]

t.tracer(0)
m = 50
t.up()

colors = ['red', 'green', 'blue', 'purple', 'black']

for cluster, color in zip(clusters, colors):
    for dot in cluster:
        t.goto(dot[0] * m, dot[1] * m)
        t.dot(3, color)

t.update()
t.done()

t_x = sum(i[0] for i in centers) / len(centers)
t_y = sum(i[1] for i in centers) / len(centers)

print(abs(int(t_x * 10_000)), abs(int(t_y * 10_000)))