from itertools import combinations

def f(x):
    p = 17 <= x <= 58
    q = 29 <= x <= 80
    a = a1 <= x <= a2
    u = p <= ((q and not a) <= (not p))
    return u

line = [i / 10 for i in range(170, 800)]
ans = []

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))