from math import dist

with open('27_B_18884.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for line in file:
        x, y = map(float, line.split())
        # if x > 40:
        #     cl1.append([x, y])
        # else: cl2.append([x, y])
        if y < x - 300: cl1.append([x, y])
        else:
            if y > -x - 400: cl2.append([x, y])
            else: cl3.append([x, y])


def f(clust):
    dists = []
    for dot in clust:
        sum_d = 0
        for dot2 in clust:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

centers = [f(cl1), f(cl2), f(cl3)]

p_x = sum(i[0] for i in centers) / len(centers)
p_y = sum(i[1] for i in centers) / len(centers)

print(abs(int(p_x)), abs(int(p_y)))