from fnmatch import fnmatch
from itertools import product

ans = []

for v in '0123456789':
    for r in range(5):
        for z in product('0123456789', repeat=r):
            num = int(f'85{v}16{''.join(z)}4')
            if num % 2658 == 0 and num < 10**9: ans.append((num, num // 2658))

for i in sorted(ans):
    print(*i)

print('')

ans1 = []

for num in range(851604 - 851604 % 2658, 10**9, 2658):
    if fnmatch(str(num), '85?16*4'): ans1.append((num, num // 2658))

for i in sorted(ans1):
    print(*i)

print(sorted(ans) == sorted(ans1))