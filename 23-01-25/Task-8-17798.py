from itertools import product

alph = sorted('минус')

for pos, val in list(enumerate(product(alph, repeat=4), start=1))[::-1]:
    val = ''.join(val)
    if sum([val.count(i) for i in 'мнс']) >= sum([val.count(i) for i in 'уи']):
        print(pos)
        break