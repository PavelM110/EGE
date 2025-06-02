from itertools import product, permutations

def f(x, y, z, w):
    return (x <= (z == w)) or not(y <= w)

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, 1, a2, a3), (0, a4, 0, a5), (a6, 0, 0, a7)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)