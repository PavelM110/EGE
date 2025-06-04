ans = []

for x in range(1, 3001):
    num = 4**210 + 4**110 - x
    cnt = 0
    while num:
        cnt += num % 4 == 0
        num //= 4
    ans.append([cnt, -x])

print(max(ans)[1])