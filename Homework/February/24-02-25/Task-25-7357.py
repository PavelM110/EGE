from itertools import product
from fnmatch import fnmatch

ans = []

for v in '2468':
    for r in range(7):
        for z in product('0123456789', repeat=r):
            if r and z[-1] in '13579':
                num = int(f'{v}136{''.join(z)}')
                if num < 10**10 and not num % 53191:
                    ans.append((num, num // 53191))

ans = sorted(ans)

ans1 = []

for num in range(53191, 10**10, 53191):
    if num % 2:
        if fnmatch(f'{num}', '[2468]136*'):
            ans1.append((num, num // 53191))

ans1 = sorted(ans1)

print(ans1 == ans)

for i in ans1[-5:]: print(*i)