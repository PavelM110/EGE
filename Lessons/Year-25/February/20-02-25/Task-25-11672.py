from fnmatch import fnmatch
from itertools import product

ans = []

for v in '0123456789':
    for r in range(6):
        for z in product('0123456789', repeat=r):
            num = f'12{''.join(z)}34{v}5'
            if int(num) < 10**10 and int(num) % 21025 == 0:
                chet = sum(num.count(i) for i in '02468')
                nech = len(num) - chet
                if chet == nech: ans.append((int(num), int(num) // 21025))

for i in sorted(ans):
    print(*i)

print('')

ans1 = []

for num in range(123405 - 123405 % 21025, 10**10, 21025):
    if fnmatch(str(num), '12*34?5'):
        chet = sum(str(num).count(i) for i in '02468')
        nech = len(str(num)) - chet
        if chet == nech: ans1.append((num, num // 21025))

for i in sorted(ans1): print(*i)

print(sorted(ans) == sorted(ans1))