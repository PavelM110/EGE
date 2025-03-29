with open('26_17687.txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file if i]

data = sorted(data)

summ = sum(data)

print(summ - sum(data[-int(n / 9):]))

cnt = int(n / 9)

ind = -9

while cnt:
    summ -= data[ind]
    ind -= 9
    cnt -= 1

print(summ)