from itertools import product

for pos, val in list(enumerate(product(sorted('победа'), repeat=6), start=1))[::-1]:
    val = ''.join(val)
    if val[0] == 'о':
        if len(val) == len(set(val)):
            if pos % 2 == 0:
                print(pos)
                break