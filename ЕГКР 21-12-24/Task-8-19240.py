from itertools import product

alph = sorted('январь')

for pos, val in list(enumerate(product(alph, repeat=5), start=1))[::-1]:
    val = ''.join(val)
    if val[0] != 'я' and 'яя' not in val and val.count('ь') <= 1:
        print(pos)
        break
