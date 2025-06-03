with open('26_17643.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

sr = sum(i[1] for i in data) / len(data)

expensive = {}

for a, c, s in data:
    if c >= sr:
        if f'{a}' in expensive:
            expensive[f'{a}'][0] += c
            expensive[f'{a}'][1] += 1
            expensive[f'{a}'][2] += not s
        else:
            b = int(not s)
            c *= b
            expensive |= {f'{a}':[c, 1, b]}

for key, val in expensive.copy().items():
    if val[2] == 0:
        del expensive[key]

leader = max(expensive.items(), key=lambda x: (x[1][2], x[1][0] / x[1][2], x[1][1] - x[1][2]))

print(leader[1][0], leader[1][1] - leader[1][2])

print(leader)