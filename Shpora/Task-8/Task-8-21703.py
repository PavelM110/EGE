from itertools import product

for pos, val in list(enumerate(product(sorted('победа'), repeat=6), start=1))[::-1]:
    if pos % 2 == 0:
        if val[0] == 'о':
            if len(val) == len(set(val)):
                print(pos)
                break