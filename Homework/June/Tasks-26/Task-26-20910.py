with open('26_20910.txt') as file:
    n, m, k = map(int, file.readline().split())
    places = [m] * (k + 1)
    for i in file:
        r, p = map(int, i.split())
        places[p] = min(places[p], r - 1)

ans = []

for i in range(1, len(places) - 1):
    a, b = places[i:i+2]
    ans.append([min(a, b), i])

ans = sorted(ans, key=lambda x: [-x[0], x[1]])

print(ans[0])