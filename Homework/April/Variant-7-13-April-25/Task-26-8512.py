with open('26_8512.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)

cells = [0 for i in range(k)]

ans1 = 0
ans2 = 0

for s, e in data:
    for i in range(k):
        if s > cells[i]:
            cells[i] = e
            ans1 += 1
            ans2 = i + 1
            break

print(ans1, ans2)