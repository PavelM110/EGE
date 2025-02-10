from itertools import permutations, product

def f(x, y, z):
    return x <= (y and z)

res = []

table = [(0, 1, 0), (1, 1, 0)]
for p in permutations('xyz'):
    u = [f(**dict(zip(p, t))) for t in table] == [0, 0]
    if u:
        res.append(p)

print(len(res))