with open('26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x: (-sum(x[1:-1]), -x[-1], x[0]))

prohod = data[:s]

if sum(prohod[-1][1:-1]) == sum(data[s][1:-1]):
    polu_prohod = sum(data[s][1:-1])

for i in prohod.copy():
    if sum(i[1:-1]) <= polu_prohod: prohod.remove(i)

print(prohod[-1][0], sum([1 for i in data if sum(i[1:-1]) == polu_prohod]))