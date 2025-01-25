from itertools import product, permutations

def f(x, y, z, w):
    return ((not x) <= y) and ((not y) == z) and w

print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                u = f(x, y, z, w)
                if u:
                    print(x, y, z, w)


for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    table = [(0, a1, 0, a2), (0, a3, a4, a5), (a6, 0, a7, a8)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)