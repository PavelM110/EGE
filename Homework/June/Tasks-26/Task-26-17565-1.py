with open('26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x:[-sum(x[1:-1]), -x[-1], x[0]])

prohod = data[:s]

s = sum(data[s][1:-1])

if sum(prohod[-1][1:-1]) == s:
    for i in prohod.copy():
        if sum(i[1:-1]) == s: prohod.remove(i)

print(prohod[-1][0], len([i for i in data if sum(i[1:-1]) == s]))