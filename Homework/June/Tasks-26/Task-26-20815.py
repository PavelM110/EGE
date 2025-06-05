with open('26_20815.txt') as file:
    n, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x: [-sum(x[1:]), -x[-1], x[0]])

prohod = data[:k]
s = sum(prohod[-1][1:])
if sum(data[k][1:]) == s:
    for i in prohod[::-1].copy():
        if sum(i[1:]) == s:
            prohod.remove(i)

print(prohod[-1][0], len([i for i in data if sum(i[1:]) == s]))