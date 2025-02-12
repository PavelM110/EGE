from itertools import combinations

def f(x):
    p = 10 <= x <= 25
    q = 15 <= x <= 30
    r = 25 <= x <= 40
    a = a1 <= x <= a2
    u = (q <= (not r)) and a and (not p)
    return u

line = [i / 10 for i in range(100, 400)]
ans = []

for a1, a2 in combinations(line, 2):
    if not(any(f(x) for x in line)): ans.append(a2 - a1)

print(max(ans))