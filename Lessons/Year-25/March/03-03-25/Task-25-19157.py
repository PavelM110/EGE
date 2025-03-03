from fnmatch import fnmatch
from itertools import product

ans = []
ans1 = []

for v in '0123456789':
    for r1 in range(4):
        for r2 in range(4 - r1):
            for z1 in product('0123456789', repeat=r1):
                for z2 in product('0123456789', repeat=r2):
                    num = int(f'1{v}3{''.join(z1)}5{''.join(z2)}954')
                    if num % 6437 == 0 and num <= 10**10:
                        ans.append((num, num // 6437))

ans = sorted(set(ans))

for num in range(1035954 - 1035954 % 6437, 10**10, 6437):
    if fnmatch(f'{num}', '1?3*5*954'):
        ans1.append((num, num // 6437))

ans1 = sorted(ans1)

for i in ans1: print(*i)

print(ans == ans1)

for i in ans:
    print(*i)