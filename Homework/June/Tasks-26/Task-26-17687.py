with open('26_17687 (1).txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file if i]

data = sorted(data, reverse=True)

print(sum(data) - sum(data[:n//9]))

print(sum(data) - sum(data[8::9]))