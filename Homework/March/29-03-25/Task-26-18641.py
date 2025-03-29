from itertools import groupby

with open('26_18541.txt') as file:
    n, m = map(int, file.readline().split())
    weights = [int(file.readline()) for i in range(n)]
    guys = [int(i) for i in file]

weights = sorted(weights, reverse=True)

chosen = []

for g in guys:
    for w in weights:
        if w <= g:
            chosen.append(w)
            break

print(sum(chosen) // len(chosen))

cnt = []

for i in set(chosen):
    cnt.append([chosen.count(i), i])

print(max(cnt))