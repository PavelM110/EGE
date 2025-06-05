from fnmatch import fnmatch
from itertools import product

ans1 = []
ans2 = []

for r in range(3):
    for z in product('0123456789', repeat=r):
        for v in '0123456789':
            num = int(f'12{''.join(z)}34{v}5')
            if num % 2025 == 0:
                ans1.append([num, num // 2025])

ans1 = sorted(ans1)

for i in range(123405 - 123405 % 2025, 10**8, 2025):
    if fnmatch(str(i), '12*34?5'):
        ans2.append([i, i // 2025])

ans2 = sorted(ans2)

print(ans1 == ans2)

for i in ans1:
    print(*i)

print('--------')

for i in ans2:
    print(*i)