from itertools import combinations

def f(x):
    p = 5 <= x <= 40
    q = 41 <= x <= 54
    r = 6 <= x <= 53
    a = a1 <= x <= a2
    u = ((not p) <= q) and r and (not a)
    return u

ans = []
line = [i / 10 for i in range(5 * 10, 54 * 10)]

for a1, a2 in combinations(line, 2):
    if not(any([f(x) for x in line])): ans.append(a2 - a1)

print(min(ans))