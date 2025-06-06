from math import dist

with open('27_B_21720.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for line in file:
        x, y = map(float, line.split())
        # if y > -1: cl1.append([x, y])
        # else: cl2.append([x, y])
        if y < 0: cl1.append([x, y])
        else:
            if x > -6: cl2.append([x, y])
            else: cl3.append([x, y])

def c(clust):
    dists = []
    for dot in clust:
        sum_d = 0
        for dot2 in clust:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

centers = [c(cl1), c(cl2), c(cl3)]

p_x = sum(i[0] for i in centers) / len(centers)

p_y = sum(i[1] for i in centers) / len(centers)

print(int(abs(p_x * 10_000)), int(abs(p_y * 10_000)))