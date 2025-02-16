from itertools import product

alph = sorted('калейдосп')[::-1]

for pos, val in enumerate(product(alph, repeat=6), start=0):
    if pos % 2 == 0:
        val = ''.join(val)
        if val[0] == 'к':
            if val.count('й') >= 2:
                if 'с' not in val and 'е' not in val:
                    print(pos)
                    break