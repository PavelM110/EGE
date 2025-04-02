from itertools import product
from fnmatch import fnmatch
from re import fullmatch

ans2 = []
ans1 = []
ans = []

for r in range(6):
    for z in product('0123456789', repeat=r):
        n = int(f'20{''.join(z)}23')
        if n % 2023 == 0:
            if sum(map(int, str(n))) % 7 == 0 and sum(map(int, str(n))) < 20:
                ans.append(n)

for n in range(2023, 10**9, 2023):
    if fullmatch(r'20[0-9]*23', str(n)):
        s = sum(map(int, str(n)))
        if s % 7 == 0 and s < 20:
            ans1.append(n)

for n in range(2023, 10**9, 2023):
    if fnmatch(str(n), '20*23'):
        s = sum(map(int, str(n)))
        if s % 7 == 0 and s < 20:
            ans2.append(n)

print(sorted(ans) == sorted(ans1) == sorted(ans2) == sorted(ans))

for i in ans:
    print(i)