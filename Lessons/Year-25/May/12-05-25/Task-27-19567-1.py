from  math import dist

with open('27.13.B_19567.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []
    cluster6 = []
    for line in file:
        x, y = map(float, line.split())
        # if y > 0:
        #     cluster1.append([x, y])
        # else: cluster2.append([x, y])
        if y > x + 12: cluster1.append([x, y])
        else:
            if y > x + 4:
                if y > 7: cluster2.append([x, y])
                else: cluster3.append([x, y])
            else:
                if y < x - 2: cluster6.append([x, y])
                else:
                    if y > 4: cluster4.append([x, y])
                    else: cluster5.append([x, y])

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

center1 = centroid(cluster1)
center2 = centroid(cluster2)
center3 = centroid(cluster3)
center4 = centroid(cluster4)
center5 = centroid(cluster5)
center6 = centroid(cluster6)

p_x = (center1[0] + center2[0] + center3[0] + center4[0] + center5[0] + center6[0])/ 6
p_y = (center1[1] + center2[1] + center3[1] + center4[1] + center5[1] + center6[1])/ 6

print(abs(int(p_x * 10_000)), abs(int(p_y * 10_000)))