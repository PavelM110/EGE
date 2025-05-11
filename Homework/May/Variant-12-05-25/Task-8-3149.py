from itertools import product

alph = '0123456789'

cnt = 0

for i in product(alph, repeat=5):
    if i[0] != '0':
        i = ''.join(i)
        if i[-1] not in '347':
            if all(j*3 not in i for j in alph):
                cnt += 1

print(cnt)