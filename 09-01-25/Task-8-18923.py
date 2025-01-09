from itertools import product

alph = 'вьюга'

cnt = 0

for i in product(alph, repeat=6):
    i = ''.join(i)
    if 'юг' in i:
        cnt += 1

print(cnt)