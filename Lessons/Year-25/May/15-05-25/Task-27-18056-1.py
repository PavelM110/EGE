from math import dist

with open('27B_18056.txt') as file:
    data = [list(map(float, i.split())) for i in file if i]

clusters = []
eps = .3

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(i) for i in clusters])

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

centers = [centroid(i) for i in clusters]

p_x = sum(i[0] for i in centers) / len(centers)
p_y = sum(i[1] for i in centers) / len(centers)

print(abs(int(p_x * 100_000)), abs(int(p_y * 100_000)))