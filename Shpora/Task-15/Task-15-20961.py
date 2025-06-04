from itertools import combinations

def f(x):
    p = 15 <= x <= 142
    q = 38 <= x <= 167
    a = a1 <= x <= a2
    u = not((q <= (not a and p)) <= (not q))
    return u

ans = []
line = [i + eps for i in range(15, 167) for eps in [0, .1, .9]]

for a1, a2 in combinations(line, 2):
    if all(not f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))