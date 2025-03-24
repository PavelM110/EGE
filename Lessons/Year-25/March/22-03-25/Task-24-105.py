from itertools import groupby

with open('24_105.txt') as file:
    data = file.readline()

ans = 0

for k, g in groupby(data):
    ans = max(ans, len(list(g)))

print(ans)