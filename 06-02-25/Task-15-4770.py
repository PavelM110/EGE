from itertools import combinations

def f(x):
    p = 35 <= x <= 55
    q = 45 <= x <= 65
    a = a1 <= x <= a2
    u = (p <= a) and ((not a) <= (not q))
    return u

ans = []
line = [i / 10 for i in range(33 * 10, 68 * 10)]

for a1, a2 in combinations(line, 2):
    if all([f(x) for x in line]): ans.append(a2 - a1)

print(min(ans))