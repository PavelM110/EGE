from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

with open('27_B_21911.txt') as file:
    data = [list(map(float, i.split())) for i in file if i]

clusters = []
eps = 1

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

print([len(c) for c in clusters])

centers = [centroid(i) for i in clusters]

p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10_000), int(p_y * 10_000))