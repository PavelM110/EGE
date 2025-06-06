from math import dist

with open('27_B_20911.txt') as file:
    data = [list(map(float, i.split())) for i in file if i]

def c(clust):
    dists = []
    for dot in clust:
        sum_d = 0
        for dot2 in clust:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

clusters = []
eps = 2

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

print([len(i) for i in clusters])

centers = [c(i) for i in clusters]

p_x = sum(i[0] for i in centers) / len(centers)

p_y = sum(i[1] for i in centers) / len(centers)

print(int(abs(p_x * 10_000)), int(abs(p_y * 10_000)))