from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return max(dists)[1]

with open('27.19.B_20497.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []
    for line in file:
        x, y = map(float, line.split())
        # if 0 < y < 6:
        #     if x > -1: cluster1.append([x, y])
        # elif -5 < y < 0:
        #     if x < 0: cluster2.append([x, y])
        #     elif x > .5: cluster3.append([x, y])
        if y > 40:
            if -40 <= x <= -21: cluster1.append([x, y])
            elif -18 <= x:
                cluster2.append([x, y])
        else:
            if x < -37: cluster3.append([x, y])
            elif -26 <= x <= -7: cluster4.append([x, y])
            elif x > 0: cluster5.append([x, y])

center1 = centroid(cluster1)
center2 = centroid(cluster2)
center3 = centroid(cluster3)
center4 = centroid(cluster4)
center5 = centroid(cluster5)

t_x = (center1[0] + center2[0] + center3[0] + center4[0] + center5[0]) / 5
t_y = (center1[1] + center2[1] + center3[1] + center4[1] + center5[1]) / 5

print(abs(int(t_x * 10_000)), abs(int(t_y * 10_000)))