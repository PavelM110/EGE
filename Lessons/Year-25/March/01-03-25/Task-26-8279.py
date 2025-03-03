with open('26_8279.txt') as file:
    t, n, m = map(int, file.readline().split())
    data = enumerate(list(map(int, i.split())) for i in file if i)

data = sorted(data, key=lambda x: (x[1][-1], -x[1][1], x[1][0]))

ans = [0 for i in range(n)]

for time in range(t, 1441, t):
    for i in range(len(data)):
        num, s, e, M = data[i][0], data[i][1][0], data[i][1][1], data[i][1][2]
        if M < m:
            ans[num] += 1
            data[i][1][-1] += 1
            data = sorted(data, key=lambda x: (x[1][-1], -x[1][1], x[1][0]))

print(max(ans))
