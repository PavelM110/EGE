from math import dist

with open('27B_19747.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []
    for line in file:
        x, y = map(float, line.split())
        # if y < 5: cluster1.append([x, y])
        # else:
        #     if x < 5: cluster2.append([x, y])
        #     else: cluster3.append([x, y])
        if y < 10:
            if y > x:
                cluster1.append([x, y])
            else:
                if x < 10: cluster2.append([x, y])
                else: cluster3.append([x, y])
        else:
            if y > x: cluster4.append([x, y])
            else: cluster5.append([x, y])



def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

cent1 = centroid(cluster1)
cent2 = centroid(cluster2)
cent3 = centroid(cluster3)
cent4 = centroid(cluster4)
cent5 = centroid(cluster5)

p_x = (cent1[0] + cent2[0] + cent3[0] + cent4[0] + cent5[0]) / 5
p_y = (cent1[1] + cent2[1] + cent3[1] + cent4[1] + cent5[1]) / 5

print(int(p_x * 100_000), int(p_y * 100_000))