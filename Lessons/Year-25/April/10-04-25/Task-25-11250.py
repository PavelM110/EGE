from itertools import product
from fnmatch import fnmatch

ans1 = []
ans2 = []

for r1 in range(4):
    for z1 in product('0123456789', repeat=r1):
        for v in '0123456789':
            for r2 in range(4):
                for z2 in product('0123456789', repeat=r2):
                    num = int(f'392{''.join(z1)}4{v}4{''.join(z2)}')
                    if num <= 10**8:
                        if num % 7058 == 0:
                            ans1.append((num, num // 7058))

for num in range(392404 - 392404 % 7058, 10**8, 7058):
    if fnmatch(str(num), '392*4?4*'):
        ans2.append((num, num // 7058))

ans1, ans2 = sorted(ans1), sorted(ans2)

print(ans1 == ans2)

for i in ans1:
    print(*i)

for i in ans2:
    print('2)', *i)