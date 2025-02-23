from itertools import product
from fnmatch import fnmatch

ans = []

for r in range(6):
    for z in product('02468', repeat=r):
        if r != 0 and z[0] != '0':
            for v1 in '13579':
                for v2 in '13579':
                    num = int(f'{''.join(z)}12{v1}4{v2}')
                    if num < 10**10:
                        if not num % 9231:
                            ans.append((num, num // 9231))

ans = sorted(ans)

ans1 = []

for num in range(12040 - 12040 % 9231, 10**10, 9231):
    for r in range(6):
        if fnmatch(f'{num}', f'{'[2468]' * r}12?4?'):
            ans1.append((num, num // 9231))

ans1 = sorted(ans1)

print(ans == ans1)

for i in ans: print(*i)