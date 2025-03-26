from fnmatch import fnmatch
from itertools import product

ans = []

for i in range(1203456009 - 1203456009 % 98591, 10**12, 98591):
    if fnmatch(str(i), '12?3*456??9'):
        ans.append((i, i // 98591))

ans1 = []

for v1 in '0123456789':
    for r in range(4):
        for z in product('0123456789', repeat=r):
            for v2 in '0123456789':
                for v3 in '0123456789':
                    num = int(f'12{v1}3{''.join(z)}456{v2}{v3}9')
                    if num <= 10**12 and num % 98591 == 0:
                        ans1.append((num, num // 98591))

ans1 = sorted(ans1)

print(ans == ans1)

for i in ans1:
    print(*i)