from itertools import combinations


def f(x):
    p = 12 <= x <= 26
    q = 30 <= x <= 53
    a = a1 <= x <= a2
    return (a <= p) or q


res = []
line = [x / 10 for x in range(0 * 10, 70 * 10)]

for a1, a2 in combinations(line, 2):
    for x in line:
        if not f(x): break
    else: res.append(a2 - a1)
print(max(res))