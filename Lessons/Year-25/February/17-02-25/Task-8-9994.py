from itertools import product

alph = sorted('школа')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val == 'шалаш':
        print(pos)
        break