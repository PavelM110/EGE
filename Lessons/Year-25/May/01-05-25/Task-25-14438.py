from fnmatch import fnmatch
from itertools import product

ans1 = []
ans2 = []

for r in range(6):
    for z in product('0123456789', repeat=r):
        for v1 in '0123456789':
            for v2 in '0123456789':
                num = int(f'17{''.join(z)}46{v1}{v2}8')
                if num <= 10**12:
                    if num % 86513 == 0:
                        if (sum(map(int, str(num))) ** .5) % 1 == 0:
                            ans1.append((num, num // 86513))

ans1 = sorted(ans1)

for num in range(1746008 - 1746008 % 86513, 10**12, 86513):
    if fnmatch(str(num), '17*46??8'):
        if (sum(map(int, str(num))) ** .5) % 1 == 0:
            ans2.append((num, num // 86513))

ans2 = sorted(ans2)

print(ans1 == ans2)

for i in ans1:
    print(*i)