from string import digits, ascii_lowercase
from itertools import product

alph = digits + ascii_lowercase

cnt = 0

for val in product(alph[:20], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if alph.index(val[0]) + alph.index(val[-1]) == 26:
            for i in alph[::2]:
                val = val.replace(i, '0')
            for i in alph[1::2]:
                val = val.replace(i, '1')
            if '00' not in val and '11' not in val:
                cnt += 1

print(cnt)