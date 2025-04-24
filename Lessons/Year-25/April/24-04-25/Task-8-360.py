from itertools import product

cnt = 0

for p, i in enumerate([i for i in product(sorted('инставк'), repeat=4) if i[0] in 'нствк' and i[-1] in 'иа'], start=1):
    i = ''.join(i)
    if i == 'ника':
        print(p)
        break