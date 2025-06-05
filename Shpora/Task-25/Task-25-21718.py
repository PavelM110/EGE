from fnmatch import fnmatch
from itertools import product

ans1 = []
ans2 = []

for r1 in range(5):
    for r2 in range(5 - r1):
        for z1 in product('0123456789', repeat=r1):
            for z2 in product('0123456789', repeat=r2):
                num = int(f'4{''.join(z1)}4736{''.join(z2)}1')
                if num % 7993 == 0:
                    ans1.append([num, num // 7993])

ans1 = sorted(ans1)

for i in range(447361 - 447361 % 7993, 10**10, 7993):
    if fnmatch(f'{i}', '4*4736*1'):
        ans2.append([i, i // 7993])

ans2 = sorted(ans2)

print(ans1 == ans2)

for i in ans1:
    print(*i)

print('-----------------')

for i in ans2: print(*i)