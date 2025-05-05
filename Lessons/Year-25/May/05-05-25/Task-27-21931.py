from math import dist

with open('27_B_21931.txt') as file:
    data = [list(map(float, i.split())) for i in file if i]

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return max(dists)[1]

eps = 1
clusters = []

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

print([len(i) for i in clusters])

center_x = centroid(min(clusters, key=len))[0]
center_y = centroid(max(clusters, key=len))[1]

print(int(center_x * 10_000), int(center_y * 10_000))