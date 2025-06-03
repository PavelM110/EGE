from itertools import product

for pos, val in list(enumerate(product(sorted('мангуст'), repeat=6), start=1))[::-1]:
    val = ''.join(val)
    if val[0] != 'у':
        if val.count('г') <= 1:
            if val.count('м') == 2:
                print(pos)
                break

print(int('566622', 7) + 1)