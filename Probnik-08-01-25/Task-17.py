with open('17_11949.txt') as file:
    data = [int(i) for i in file if i]

maxi = 0
cnt = 0
ans = 0

for i in data:
    if i % 100 == 68:
        maxi = max(maxi, i)

for i in range(len(data) - 3):
    if sum(data[i:i+4]) >= maxi:
        lens = []
        for j in data[i:i+4]:
            lens.append(len(str(j).lstrip('-')))
        if lens.count(2) in (1, 4):
            cnt += 1
            ans = max(ans, sum(data[i:i+4]))

print(cnt, ans)