from itertools import product, repeat

alph = 'котбус'

cnt = 0

for val in product(alph, repeat=8):
    val = ''.join(val)
    if val[0] not in 'оу' and 'кот' in val:
        cnt += 1

print(cnt)