with open('26_17881.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

sdal = [i for i in data if 2 not in i[1:]]
nesdal = [i for i in data if 2 in i[1:]]

sdal = sorted(sdal, key=lambda x: [-(sum(x[1:]) / 4), x[0]])

nesdal = sorted(nesdal, key=lambda x: [x[1:].count(2), x[0]])

data = sdal + nesdal

print(data[(len(data) // 4) - 1][0])

for i in data:
    if i[1:].count(2) > 2:
        print(i[0])
        break