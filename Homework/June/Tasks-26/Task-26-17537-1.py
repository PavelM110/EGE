with open('26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

min_places = [m] * (k + 1)

for r, p in data:
    min_places[p] = min(r - 1, min_places[p])

ans_places = [0 for i in range(k + 1)]

for i in range(len(min_places) - 1):
    a, b = min_places[i:i+2]
    ans_places[i] = min(a, b)

maxx = max(ans_places)

for i in range(k + 1)[::-1]:
    if ans_places[i] == maxx:
        print(maxx, i + 1)
        break