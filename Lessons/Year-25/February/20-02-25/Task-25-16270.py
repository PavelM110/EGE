from itertools import product
from fnmatch import fnmatch

ans = []

for v1 in '0123456789':
    for v2 in '0123456789':
        for v3 in '0123456789':
            num = int(f'12{v1}345{v2}67089{v3}')
            if num < 10**13 and num % 206 == 0: ans.append((num, num // 206))

ans = sorted(ans)

ans1 = []

for num in range(1203450670890 - 1203450670890 % 206, 10**13, 206):
    if fnmatch(str(num), '12?345?67089?'): ans1.append((num, num // 206))

ans1 = sorted(ans1)

if ans == ans1:
    for i in ans: print(*i)
else: print('ERR')