from itertools import product

alph = sorted('привычка')

l1 = list(product(alph, repeat=5))

for i in range(4, len(l1), 5):
    l1[i] = 0

l = [i for i in l1 if i != 0]

for pos, val in enumerate(l, start=1):
    val = ''.join(val)
    if len(val) == len(set(val)):
        if all(i not in val for i in 'аиы'):
            print(pos)
            break