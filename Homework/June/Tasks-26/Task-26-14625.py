with open('26_14625.txt') as file:
    n = int(file.readline())
    k, r, m = map(int, file.readline().split())
    m *= 2**20
    data = []
    for i in file:
        t, v, e = int(i.split()[0]), int(i.split()[1]), i.split()[2]
        if e == 'b': data.append([v, t])
        elif e == 'kb': data.append([v * 2**10, t])
        else: data.append([v * 2**20, t])

data = sorted(data, reverse=True)

type_cnts = [r for i in range(k + 1)]
deleted = []

for v, t in data:
    if type_cnts[t] > 0:
        type_cnts[t] -= 1
        deleted.append([v, t])
        m -= v
        if m <= 0:
            break

print(len(deleted))

m += deleted[-1][0]
type_cnts[deleted[-1][1]] += 1
deleted = deleted[:-1]

for v, t in sorted(data):
    if type_cnts[t] > 0:
        if m - v <= 0:
            print(v)
            break