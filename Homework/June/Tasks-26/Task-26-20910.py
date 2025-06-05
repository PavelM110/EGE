with open('26_20910.txt') as file:
    n, m, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

places = [m] * (k + 1)

for r, p in data:
    places[p] = min(r - 1, places[p])

ans_row = [0] * (k + 1)

for i in range(len(places) - 1):
    a, b = places[i:i+2]
    ans_row[i] = min(a, b)

ans = max(ans_row)

for i in range(len(places)):
    if places[i] == ans:
        print(ans, i)
        break
