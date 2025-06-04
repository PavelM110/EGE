from itertools import combinations

def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    u = p <= ((q and not a) <= (not p))
    return u

ans = []
line = [i / 10 for i in range(150, 630)]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))