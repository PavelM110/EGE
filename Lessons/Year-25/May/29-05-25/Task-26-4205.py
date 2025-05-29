with open('26_4205.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

rows = [[] for i in range(max(data)[0] + 1)]

for r, p in data:
    rows[r].append(p)

for row in range(len(rows)):
    rows[row] = sorted(rows[row])

for row in range(len(rows))[::-1]:
    for i in range(len(rows[row]) - 1):
        if abs(rows[row][i] - rows[row][i+1]) == 14:
            print(row)
            print(rows[row][i] + 1)
            break