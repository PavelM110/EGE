from itertools import product
from fnmatch import fnmatch

def f(num):
    res = ''
    while num:
        res += str(num % 7)
        num //= 7
    return res[::-1]

ans = []

flag = True

for v in '123456':
    if not flag: continue
    for r in range(10):
        for z in product('0123456', repeat=r):
            num_7 = f'{v}213{''.join(z)}5664'
            num = int(num_7, 7)
            if num > 10**9: flag = False
            if num <= 10**9 and num % 333 == 0:
                ans.append((num, num // 333))

ans = sorted(ans)

ans1 = []

for num in range(int('12135664', 7) - int('12135664', 7) % 333, 10**9, 333):
    if fnmatch(f(num), '?213*5664'):
        ans1.append((num, num // 333))

ans1 = sorted(ans1)

print(ans == ans1)

for i in ans1: print(*i)