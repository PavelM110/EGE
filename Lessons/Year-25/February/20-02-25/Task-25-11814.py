from itertools import product
from fnmatch import fnmatch

ans = []

for i in range(2100068079 - 2100068079 % 1777, 10**10, 1777):
    if fnmatch(str(i), '21???68?79'): ans.append((i, i // 1777))

ans = sorted(ans)

ans1 = []

for r in product('0123456789', repeat=3):
    for v in '0123456789':
        num = int(f'21{''.join(r)}68{v}79')
        if num % 1777 == 0 and num < 10**10: ans1.append((num, num // 1777))

ans1 = sorted(ans1)

if ans1 == ans:
    for i in ans: print(*i)
else: print('ERR')