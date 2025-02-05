from itertools import combinations

def f(x):
    p = 13 <= x <= 19
    q = 17 <= x <= 23
    a = a1 <= x <= a2
    u = (not((not p) <= q)) <= (a <= ((not q) <= p))
    return u

ans = []
line = [i / 10 for i in range(13 * 10, 23 * 10)]

for a1, a2 in combinations(line, 2):
    if all([f(x) for x in line]): ans.append(a2 - a1)

print(max(ans))