from itertools import product, permutations

def f(x, y, z, w):
    return not(w <= (x == (y or y))) and (z <= x)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, 1, 1, a2), (0, a3, a4, 0), (a5, 0, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)