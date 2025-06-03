from itertools import product

for pos, val in list(enumerate(product(sorted('фокус'), repeat=5), start=1))[::-1]:
    val = ''.join(val)
    if 'ф' not in val and val.count('у') == 2:
        print(pos)
        break