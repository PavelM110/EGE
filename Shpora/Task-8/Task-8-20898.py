from itertools import product

cnt = 0

for val in product('012345678', repeat=5):
    if val[0] != '0':
        val = ''.join(val)
        for i in '357': val = val.replace(i, '1')
        if val.count('0') == 1 and '10' not in val and '01' not in val: cnt += 1

print(cnt)