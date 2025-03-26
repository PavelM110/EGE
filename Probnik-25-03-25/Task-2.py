from itertools import product, permutations

def f(x, y, z, w):
    return x and ((z <= y) == w)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, a1, 1, a2), (0, a3, 1, 1), (1, 1, 1, a4), (1, 1, 1, a5)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]
            if u:
                print(*p)

print('x y z wS')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w)