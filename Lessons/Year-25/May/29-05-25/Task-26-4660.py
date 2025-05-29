with open('26_4660 (1).txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file if i]

data = sorted(data, reverse=True)

summ = 0

for i in range(len(data)):
    if (i + 1) % 4 == 0:
        summ += data[i] // 2
    else:
        summ += data[i]

print(summ)

data = sorted(data)

print((sum(data[:n//4]) // 2) + sum(data[n//4:]))

