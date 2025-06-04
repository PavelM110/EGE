ans = []

for x in range(2030, 1, -1):
    num = 7**170 + 7**100 - x
    cnt = 0
    while num:
        cnt += num % 7 == 0
        num //= 7
    ans.append([cnt, x])

print(max(ans)[1])