from itertools import product

alph = 'ясновидец'

cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[-1] in 'яоие' and val[0] not in 'яоие':
        if val.count(val[0]) == 1:
            if val.count(val[-1]) == 1: cnt += 1

print(cnt)