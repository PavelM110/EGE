from itertools import product
from fnmatch import fnmatch

ans = []

for c1 in '2468':
    for v1 in '0123456789':
        for v2 in '0123456789':
            for r in range(3):
                for z in product('0123456789', repeat=r):
                    for n in '13579':
                        for c3 in '02468':
                            num = int(f'{c1}9{v1}23{v2}{''.join(z)}23{n}{c3}')
                            if num < 10**10 and num % 1984 == 0: ans.append((num, num // 1984))

ans = sorted(ans)

ans1 = []

for num in range(2902302310 - 2902302310 % 1984, 10**10, 1984):
    if fnmatch(str(num), '[2468]9?23?*23[13579][02468]'): ans1.append((num, num // 1984))

ans1 = sorted(ans1)

for i in ans: print(*i)

print('')

for i in ans1: print(*i)

print(ans == ans1)