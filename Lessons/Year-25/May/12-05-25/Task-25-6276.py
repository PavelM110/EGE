from itertools import product
from fnmatch import fnmatch

ans1 = []
ans2 = []

for v1 in '0123456789':
    for v2 in '0123456789':
        for v3 in '0123456789':
            for r in range(3):
                for z in product('0123456789', repeat=r):
                    num = int(f'1{v1}1{v2}1{v3}1{''.join(z)}1')
                    if sum(map(int, str(num))) == 22:
                        if num % 2023 == 0:
                            ans1.append(num)

ans1 = sorted(ans1)
print(1)

for i in range(10101011 - 10101011 % 2023, 10 ** 10, 2023):
    i = str(i)
    if fnmatch(i, '1?1?1?1*1'):
        if sum(map(int, i)) == 22:
            ans2.append(int(i))

ans2 = sorted(ans2)

print(ans1 == ans2)

for i in ans2:
    print(i)
