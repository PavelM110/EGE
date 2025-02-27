from itertools import product
from fnmatch import fnmatch

ans1_1 = []

for r1 in range(8):
    for r2 in range(8 - r1):
        for z1 in product('0123456789', repeat=r1):
            for z2 in product('0123456789', repeat=r2):
                num = int(f'4{''.join(z1)}5{''.join(z2)}6')
                if num % 1234 == 0 and num <= 10**10:
                    if fnmatch(str(num), '?74*68?'):
                        ans1_1.append(num)

for i in sorted(ans1_1)[::-1]:
    print(i, i // 1234)