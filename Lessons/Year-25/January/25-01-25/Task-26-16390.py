with open('26_16390.txt') as file:
    s, n = map(int, file.readline().split())
    data = [int(i) for i in file if i]

data = sorted(data)

ans_1 = 0
cnt_1 = 0

for i in data:
    if i + ans_1 <= s:
        ans_1 += i
        cnt_1 += 1

print(cnt_1)

for i in data[::-1]:
    if sum(data[:cnt_1 - 1]) + i <= s:
        print(i)
        break