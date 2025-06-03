from itertools import product

for pos, val in list(enumerate(product(sorted('январь'), repeat=5), start=1))[::-1]:
    val = ''.join(val)
    if val[0] != 'я':
        if val.count('ь') <= 1:
            if 'яя' not in val:
                print(pos)
                break

print(int('45353', 6) + 1)