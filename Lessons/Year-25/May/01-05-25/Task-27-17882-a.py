from math import dist

def centroid(cluster):
    distances = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distances.append([sum_dist, dot])
    return min(distances)[1]

with open('27_A_17882.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    for line in file:
        x, y = map(float, line.split())
        if y < 3:
            cluster_A1.append([x, y])
        else:
            cluster_A2.append([x, y])

center_A1 = centroid(cluster_A1)
center_A2 = centroid(cluster_A2)

ans_x = (center_A1[0] + center_A2[0]) / 2
ans_y = (center_A1[1] + center_A2[1]) / 2

print(int(ans_x * 10_000), int(ans_y * 10_000))