from itertools import product
from fnmatch import fnmatch

ans = []

for v in '0123456789':
    for r in range(4):
        for z in product('0123456789', repeat=r):
            num = int(f'1{v}2139{''.join(z)}4')
            if num < 10**10 and num % 3052 == 0:
                ans.append((num, num // 3052))

ans = sorted(ans)

ans1 = []

for num in range(1021394 - 1021394 % 3052, 10**10, 3052):
    if fnmatch(str(num), '1?2139*4'):
        ans1.append((num, num // 3052))

ans1 = sorted(ans1)

print(ans1 == ans)

for i in ans: print(*i)