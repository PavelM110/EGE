from fnmatch import fnmatch
from itertools import product

def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    return divs

ans1 = []
ans2 = []

for v in '0123456789':
    for r in range(3):
        for z in product('0123456789', repeat=r):
            num = int(f'12{v}{''.join(z)}45')
            d = f(num)
            if len(d) == 18:
                ans1.append((num, max(d)))


for num in range(12045, 10**7):
    if fnmatch(str(num), '12?*45'):
        d = f(num)
        if len(d) == 18:
            ans2.append((num, max(d)))

ans1, ans2 = sorted(ans1), sorted(ans2)

print(ans1 == ans2)

for i in ans1:
    print(*i)