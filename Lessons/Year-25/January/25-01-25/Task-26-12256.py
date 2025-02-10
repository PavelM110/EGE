with open('26_12256.txt') as file:
    s, n = map(int, file.readline().split())
    data = [int(i) for i in file if i]

data = sorted(data)

ans_1, summ = 0, 0

for i in data:
    if summ + i <= s:
        summ += i
        ans_1 += 1

print(ans_1)

for i in data[::-1]:
    if i + sum(data[:ans_1 - 1]) <= s:
        print(i)
        break