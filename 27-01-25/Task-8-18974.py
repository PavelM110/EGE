from string import digits, ascii_lowercase
from itertools import product

alph = digits + ascii_lowercase

cnt = 0

for val in product(alph[:25], repeat=4):
    val = ''.join(val)
    cnt_1 = 0
    for i in alph[1::2]:
        cnt_1 += val.count(i)
    if cnt_1 == 1 and val[0] != '0':
        cnt_2 = 0
        for i in alph[:6]:
            cnt_2 += val.count(i)
        if cnt_2 <= 2:
            cnt += 1

print(cnt)