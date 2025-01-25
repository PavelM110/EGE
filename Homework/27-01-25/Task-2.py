from itertools import product, permutations, repeat


def f(x, y, z, w):
    return (w and y) or ((x <= w) == (y <= z))


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(a1, a2, a3, 1), (1, a4, a5, 1), (1, a6, 1, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)