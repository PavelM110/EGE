with open('26_7456.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

def f(row):
    good = []
    row = sorted(row)
    if len(row) == 2: return []
    if len(row) == 3:
        return [row[1]] if row[1] - row[0] == 6 and row[2] - row[1] == 6 else []
    for i in range(1, len(row) - 1):
        if row[i] - row[i - 1] == 6 and row[i + 1] - row[i] == 6: good.append(row[i])
    return good

rows = [[] for i in range(max(i[0] for i in data) + 1)]

cnt = 0
ans1 = 0

for r, p in data:
    rows[r].append(p)


print(sorted(max(rows)))

print(f(max(rows)))

for i in range(len(rows))[::-1]:
    good = f(rows[i])
    cnt += len(good)
    if good:
        print(i)

print(cnt)