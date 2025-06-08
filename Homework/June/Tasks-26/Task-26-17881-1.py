with open('26_17881.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

sdali = sorted([i for i in data if 2 not in i[1:]], key=lambda x: [-sum(x[1:]) / 4, x[0]])

print(sdali[len(data) // 4 - 1][0])

ne_sdali = sorted([i for i in data if i[1:].count(2) > 2], key=lambda x: (x[1:].count(2), x[0]))

print(ne_sdali[0][0])