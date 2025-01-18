from itertools import product, permutations


def f(a, b, c, d, e):
    return (a or not b or not c or d or not e) and (not a or not b or c or d or e) and (a or not b or not c or not d or e)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(0, 1, 1, 0, a1), (0, 1, 1, 1, 0), (0, 1, a3, a4, 1), (0, 0, 0, 1, 0)]
    if len(table) == len(set(table)):
        for p in [('a', 'b', 'c', 'd', 'e')]:
            u = [f(**dict(zip(p, t))) for t in table] == [1, a2, 0, a5]
            if u:
                print(a1, a2, a3, a4, a5)