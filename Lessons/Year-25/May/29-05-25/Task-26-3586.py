from itertools import groupby

with open('26_3586 (1).txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

rows = []

for k, g in groupby(sorted(data), key=lambda x: x[0]):
    rows.append([k, sorted([i[1] for i in g])])

ans = []

for row in sorted(rows, reverse=True):
    pos, places = row[0], row[1]
    for i in range(len(places) - 1):
        ans.append([places[i+1] - places[i] - 1, pos])

print(max(ans))