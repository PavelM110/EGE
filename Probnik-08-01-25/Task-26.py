with open('26_11956.txt') as file:
    n, k = list(map(int, file.readline().split()))
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)
cnt = 0

for i in data:
    if i[0] <= k:
        k += i[1]
        cnt += 1

print(cnt, k)