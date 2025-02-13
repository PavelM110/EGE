from itertools import product

alph = sorted('марксл')

for pos, val in list(enumerate(product(alph, repeat=6), start=1))[::-1]:
    val = ''.join(val)
    if 'ск' not in val and 'кс' not in val:
        cnt_3 = 0
        cnt_1 = 0
        for i in set(val):
            if val.count(i) == 3: cnt_3 += 1
            elif val.count(i) == 1: cnt_1 += 1
        if cnt_3 == 1 and cnt_1 == 3:
            print(pos, val)
            break