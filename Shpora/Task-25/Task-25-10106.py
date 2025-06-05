from itertools import product
from fnmatch import fnmatch

ans1 = []
ans2 = []

for r in range(5):
    for z in product('0123456789', repeat=r):
        for v in '0123456789':
            num = int(f'1{v}2157{''.join(z)}4')
            if num <= 10**10 and num % 2024 == 0:
                ans1.append([num, num // 2024])

ans1 = sorted(ans1)

for i in range(1021574 - 1021574 % 2024, 10**10, 2024):
    if fnmatch(f'{i}', '1?2157*4'):
        ans2.append([i, i // 2024])

ans2 = sorted(ans2)

print(ans1 == ans2)

for i in ans1:
    print(*i)

print('-------------')

for i in ans2:
    print(*i)