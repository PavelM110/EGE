from itertools import product, permutations

def f(x, y, z, w):
    return(z and (not w)) or (z == x) or y

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, a2, 0, 1), (1, 0, a3, 1), (1, 1, 0, a4)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)