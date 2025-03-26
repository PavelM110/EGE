from itertools import product

alph = sorted('лунатик')

for pos, val in list(enumerate(product(alph, repeat=6), start=1))[::-1]:
    val = ''.join(val)
    if val[0] == 'н' and val.count('а') + val.count('у') + val.count('и') == 1:
        print(pos)
        break