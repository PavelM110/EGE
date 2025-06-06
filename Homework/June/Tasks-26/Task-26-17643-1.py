from itertools import groupby

with open('26_17643.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

sr = sum(i[1] for i in data) / len(data)

dorog = sorted([i for i in data if i[1] > sr])

leaders = {}

for i, c, s in dorog:
    if i in leaders:
        leaders[i][0] += 1 if s == 0 else 0
        leaders[i][2] += 1 if s == 1 else 0
    else:
        if s:
            leaders[i] = [0, c, 1]
        else: leaders[i] = [1, c, 0]

leader = max(leaders.values(), key=lambda x: [x[0], x[1], -x[2]])

print(leader[0] * leader[1], leader[-1])










