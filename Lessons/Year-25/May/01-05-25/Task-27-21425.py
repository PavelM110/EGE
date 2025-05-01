from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dists = 0
        for dot2 in cluster:
            sum_dists += dist(dot, dot2)
        dists.append([sum_dists, dot])
    return min(dists)[1]

with open('27_A_21425.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    for line in file:
        x, y = map(float, line.split())
        if x < 15:
            cluster_A1.append([x, y])
        else: cluster_A2.append([x, y])

center_A1 = centroid(cluster_A1)
center_A2 = centroid(cluster_A2)

ans_x = (center_A1[0] + center_A2[0]) / 2
ans_y = (center_A1[1] + center_A2[1]) / 2

print(int(ans_x * 10_000), int(ans_y * 10_000))

with open('27_B_21425.txt') as file:
    cluster_B1 = []
    cluster_B2 = []
    cluster_B3 = []
    for line in file:
        x, y = map(float, line.split())
        if x < 0: cluster_B1.append([x, y])
        else:
            if y > 10: cluster_B2.append([x, y])
            else: cluster_B3.append([x, y])

center_B1 = centroid(cluster_B1)
center_B2 = centroid(cluster_B2)
center_B3 = centroid(cluster_B3)

ans_x = (center_B1[0] + center_B2[0] + center_B3[0]) / 3
ans_y = (center_B1[1] + center_B2[1] + center_B3[1]) / 3

print(int(ans_x * 10_000), int(ans_y * 10_000))