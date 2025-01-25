with open('26_17786.txt') as file:
    n, v = map(int, file.readline().split())
    data = [int(i) for i in file if i]

v *= 1000

data = sorted(data, reverse=True)

ans = []

for i in data:
    if i in range(7_000, 12_001):
        if sum(ans) + i <= v:
            ans.append(i)

print(len(ans), ans[-1])