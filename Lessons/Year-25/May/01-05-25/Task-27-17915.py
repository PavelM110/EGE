from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dists = 0
        for dot2 in cluster:
            sum_dists += dist(dot, dot2)
        dists.append([sum_dists, dot])
    return min(dists)[1]

with open('27_A_17915.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    cluster_A3 = []
    for line in file:
        x, y = map(float, line.split())
        if x < 6: cluster_A1.append([x, y])
        else:
            if y > 24: cluster_A2.append([x, y])
            else: cluster_A3.append([x, y])

center_A1 = centroid(cluster_A1)
center_A2 = centroid(cluster_A2)
center_A3 = centroid(cluster_A3)

ans_x = (center_A1[0] + center_A2[0] + center_A3[0]) / 3
ans_y = (center_A1[1] + center_A2[1] + center_A3[1]) / 3

print(int(ans_x * 10_000), int(ans_y * 10_000))