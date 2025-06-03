from itertools import product

for pos, val in list(enumerate(product(sorted('компьютер'), repeat=5), start=1))[::-1]:
    if pos % 2:
        if val[0] != 'ь':
            if val.count('к') == 2:
                print(pos)
                break