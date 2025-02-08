with open('26_8512.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)
cnt = 0
last = 0
cells = [0 for i in range(k)]

for start, end in data:
    for cell in range(len(cells)):
        if cells[cell] + 1 <= start:
            cells[cell] = end
            cnt += 1
            last = cell + 1
            break

print(cnt)
print(last)