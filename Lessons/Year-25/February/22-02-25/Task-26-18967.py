with open('26_18967.txt') as file:
    n, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x: (x[1], x[0], x[2]))

n_start = n

timeline = [0 for i in range(1441)]

cnt = 0

ids = []

angry = []

for i in data:
    if i[0] in angry: continue
    if i[0] not in ids:
        if i[-1] > n:
            cnt += i[-1]
            angry.append(i[0])
        else:
            n -= i[-1]
            ids.append(i[0])
            for t in range(i[1], len(timeline)):
                timeline[t] += i[-1]
    else:
        n += i[-1]
        for t in range(i[1], len(timeline))[::-1]:
            timeline[t] -= i[-1]

print(cnt)

print(sum(1 for i in timeline if i == n_start))