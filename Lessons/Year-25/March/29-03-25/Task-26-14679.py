from itertools import groupby

with open('26_14679.txt') as file:
    n = int(file.readline())
    k = int(file.readline())
    data = [list(map(lambda x: list(map(int, x.split('.'))), i.split())) for i in file]

for i in range(len(data)):
    s, e = data[i]
    s = s[3] + s[2] * 60 + s[0] * 24 * 60 + s[1] * 24 * 60 * 30
    e = e[3] + e[2] * 60 + e[0] * 24 * 60 + e[1] * 24 * 60 * 30
    data[i] = [s, e]

m = max([max(i) for i in data])

timeline = [0 for i in range(m + 1)]

for s, e in data:
    for i in range(s, e+1):
        timeline[i] += 1

ans1 = 0

for ky, g in groupby(timeline, key=lambda x: x >= k):
    if ky:
        ans1 += 1

print(ans1, max(timeline))