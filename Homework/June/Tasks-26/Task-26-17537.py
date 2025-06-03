with open('26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

max_places = [10 ** 10] * (k + 1)

for r, p in data:
    max_places[p] = min(max_places[p], r - 1)

ans_places = [0] * (k + 1)

for i in range(len(max_places) - 1):
    a, b = max_places[i:i+2]
    ans_places[i] = min(a, b)

ans_row = max(ans_places)

for i in range(len(ans_places))[::-1]:
    if ans_places[i] == ans_row:
        print(ans_row, i + 1)
        break