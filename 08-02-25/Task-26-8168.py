with open('26_8168.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)
cells = [0] * k
time = ['' for i in range(1440)]
cnt = 0

for start, duration in data:
    for cell in range(len(cells)):
        if cells[cell] + 1 <= start:
            cells[cell] = start + duration
            cnt += 1
            for t in range(start + 1, start + duration):
                time[t] = time[t] + '1'
            break

print(n - cnt, time.count('1' * k))