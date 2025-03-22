from itertools import groupby

with open('26_2480.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

road = [0 for i in range(0, 2_000_001)]

for s, e in data:
    for i in range(s, e):
        road[i] = 1

ans = []

for k, g in groupby(road):
    if k == 1:
        ans.append(len(list(g)))

print(len(ans), sum(ans))