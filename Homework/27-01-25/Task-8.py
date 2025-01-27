from itertools import product, repeat

alph = '0123456789ab'

cnt = 0

for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('b') == 2:
        for i in '02468':
            val = val.replace(i, 'a')
        for i in '13579':
            val = val.replace(i, 'b')
        if 'aa' not in val and 'bb' not in val:
            cnt += 1

print(cnt)