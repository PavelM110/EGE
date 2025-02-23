from itertools import product
from fnmatch import fnmatch

ans = []

for r1 in range(3):
    for r2 in range(3 - r1):
        for z1 in product('123456789', repeat=r1):
            for z2 in product('0123456789', repeat=r2):
                num = int(f'{''.join(z1)}15{''.join(z2)}7424')
                if num < 10**8:
                    if num % 111 == 0:
                        ans.append((num, num // 111))
                    elif num % 113 == 0:
                         ans.append((num, num // 113))
                    elif num % 127 == 0:
                        ans.append((num, num // 127))

ans = sorted(ans)

ans1 = []

for d in (111, 113, 127):
    for num in range(157424 - 157424 % d, 10**8, d):
        if fnmatch(f'{num}', '*15*7424'):
            ans1.append((num, num // d))

ans1 = sorted(ans1)

print(ans == ans1)

for i in ans: print(*i)