from itertools import combinations

def f(x):
    c = 48 <= x <= 94
    j = 83 <= x <= 100
    a = a1 <= x <= a2
    u = (not(c or j)) <= (not a)
    return u

ans = []
line = [i / 10 for i in range(45 * 10, 105 * 10)]

for a1, a2 in combinations(line, 2):
    if all([f(x) for x in line]):
        ans.append(a2 - a1)

print(max(ans))