from fnmatch import fnmatch
from itertools import product

pat = '1*28?64'

res = []

# for i in range(127544, 199999928964, 596):
#     if fnmatch(str(i), pat):
#         res.append(i)

for i in '0123456789':
    for j in range(0, 7):
        for k in product('0123456789', repeat=j):
            num = int('1' + ''.join(k) + '28' + i + '64')
            if num % 596 == 0:
                res.append(num)

print(len(res), sum(res) / len(res))