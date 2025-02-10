from itertools import combinations

def f(x):
    p = 44 <= x <= 49
    q = 28 <= x <= 53
    a = a1 <= x <= a2
    u = (a <= p) or q
    return u

ans = []
line = [0, 44, 49, 28, 53, 60]

for a1, a2 in combinations(sorted(line), 2):
    if all([f(x) for x in range(0, 60)]): ans.append(a2 - a1)

print(max(ans))