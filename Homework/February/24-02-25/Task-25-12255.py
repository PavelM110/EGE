from itertools import product
from fnmatch import fnmatch

ans = []

for v1 in '0123456789':
    for r in range(3):
        for z in product('0123456789', repeat=r):
            for v2 in '0123456789':
                for v3 in '0123456789':
                    num = int(f'12{v1}3{''.join(z)}456{v2}{v3}9')
                    if num % 98591 == 0:
                        ans.append((num, num // 98591))

ans = sorted(ans)

ans1 = []

for num in range(1203456009 - 1203456009 % 98591, 10**12, 98591):
    if fnmatch(f'{num}', '12?3*456??9'):
        ans1.append((num, num // 98591))

ans1 = sorted(ans1)

print(ans == ans1)

for i in ans: print(*i)