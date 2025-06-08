with open('26_20910.txt') as file:
    n, m, k = map(int, file.readline().split())
    places = [m] * (k + 1)
    for seat in file:
        r, p = map(int, seat.split())
        places[p] = min(places[p], r - 1)

ans = []

for i in range(1, len(places) - 1):
    ans.append([min(places[i], places[i + 1]), i])

print(sorted(ans, key=lambda x: [-x[0], x[1]])[0])