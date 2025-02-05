from itertools import combinations

def f(x):
    p = 43 <= x <= 49
    q = 44 <= x <= 53
    a = a1 <= x <= a2
    u = (a <= p) or q
    return u

ans = []
line = [i / 10 for i in range(20 * 10, 80 * 10)]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line): ans.append(a2 - a1)
    # for x in line:
    #     if not f(x): break
    # else: ans.append(a2 - a1)

print(max(ans))