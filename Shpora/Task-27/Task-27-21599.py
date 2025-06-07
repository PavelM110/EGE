from math import dist

with open('27_b_21599.txt') as file:
    cl1 =[]
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    cl6 = []
    for line in file:
        x, y = map(float, line.split())
        # if y < -5: cl3.append([x, y])
        # else:
        #     if y > x - 10: cl1.append([x, y])
        #     else: cl2.append([x, y])
        if y < -5: cl6.append([x, y])
        else:
            if y < .5 * x: cl5.append([x, y])
            else:
                if x < -10:
                    if y < -2.5 * x - 32.5: cl1.append([x, y])
                    else: cl2.append([x, y])
                else:
                    if y > (5 / 3) * x + (35 / 3): cl3.append([x, y])
                    else: cl4.append([x, y])

    clusters = [cl1, cl2, cl3, cl4, cl5, cl6]

def c(clust):
    dists = []
    for dot in clust:
        sum_d = 0
        for dot2 in clust:
            sum_d += dist(dot, dot2)
        dists.append([sum_d, dot])
    return min(dists)[1]

centers = [c(i) for i in clusters]

p_x = sum(i[0] for i in centers) / len(centers)
p_y = sum(i[1] for i in centers) / len(centers)

print(abs(int(p_x * 10_000)), int(abs(p_y * 10_000)))