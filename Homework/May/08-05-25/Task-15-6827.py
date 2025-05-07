from itertools import combinations

def f(x):
    p = 257 <= x <= 1000
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = a1 <= x <= a2
    u = (a <= r) and ((not(a <= p)) <= q)
    return u

ans = 10**10
line = [i/4 for i in range(20, 4000)]

for a1, a2 in combinations(line, 2):
    if all([f(x) for x in line]):
        ans = min(ans, a2 - a1)

print(ans)