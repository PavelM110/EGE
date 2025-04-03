from itertools import product

alph = sorted('аргумент')

for pos, val in list(enumerate(product(alph, repeat=4), 1))[::-1]:
    val = ''.join(val)
    if len(val) == len(set(val)):
        if val == ''.join(sorted(val)):
            print(pos)
            break