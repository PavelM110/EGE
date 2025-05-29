with open('26_4629 (1).txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file if i]

data = sorted(data, reverse=True)

print(sum(data[:n//4]) // 2 + sum(data[n//4:]))

data = sorted(data)

print(sum(data[:n//4]) // 2 + sum(data[n//4:]))