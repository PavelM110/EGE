from itertools import groupby

with open('26_9847.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

timeline = [0 for i in range(1441)]

for s, e in data:
    print(s, e)
    for j in range(s, e):
        timeline[j] += 1

ans = 0
# 0 1 2 3 4 5 6 7 8
# 0 1 1 1 0 0 0 0 0
for k, g in groupby(timeline):
    print(k, *g)
    if k == max(timeline):
        ans += 1

print(ans, max(timeline))

print(*range(0, 1441))

print(*timeline)