from itertools import product, permutations


def f(x, y, z, w):
    return not(x <= w) or (y <= z) or not y

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, 1, a2, 0), (a3, 0, 1, a4), (a5, a6, 0, a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)