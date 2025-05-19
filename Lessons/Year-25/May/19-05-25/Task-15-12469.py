from itertools import combinations

def f(x):
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    a = a1 <= x <= a2
    u = d <= ((not c and not a) <= (not d))
    return u

line = [i / 10 for i in range(70, 1000)]
ans = []

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))