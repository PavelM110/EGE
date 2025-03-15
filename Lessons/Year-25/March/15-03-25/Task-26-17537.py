with open('26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x: (x[1], x[0]))

min_seat = [m + 1 for i in range(k + 1)]

for i in data:
    min_seat[i[1]] = min(min_seat[i[1]], i[0])

ans = []

for i in range(1, k)[::-1]:
    a, b = min_seat[i:i+2]
    ans.append([min(a, b) - 1, i + 1])

print(max(ans))
