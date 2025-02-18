from fnmatch import fnmatch
from itertools import product

ans = []

for i in range(125670 - 125670%7777, 10**10, 7777):
    if fnmatch(str(i), '12*567?'): ans.append((i, i // 7777))

for i in sorted(ans): print(*i)

print('\n')

ans1 = []

for v in '0123456789':
    for l in range(6):
        for z in product('0123456789', repeat=l):
            num = int(f'12{''.join(z)}567{v}')
            if num <= 10**10:
                if num % 7777 == 0:
                    ans1.append((num, num // 7777))

for i in sorted(ans1):
    print(*i)

print('\n', sorted(ans)==sorted(ans1))