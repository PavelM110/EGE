from itertools import product, permutations

def f(x, y, z, w):
    return all((x <= (not z), not(w <= z), not(not(x <= (not w)) and z)))
#(not((not(x <= (not w))) and z))
#(not(not(x <= (not w)) and z)) and (not(w <= z)) and (x <= (not z))
#(not((not(x <= (not w))) and z)) and (not(w <= z)) and (x <= (not z))
#all(x <= (not z), not(w <= z), not(not(x <= (not w)) and z))
cnt = 0

for a1, a2, a3, a4, a5 in product([1, 0], repeat=5):
    table = [(1, 0, a1, 0), (1, 0, a2, a3), (a4, 1, a5, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 0, 0]
            if u:
                cnt += 1
print(cnt)