from itertools import product

alph = '0123456789ab'
cnt = 0

for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] != '0':
        if i.count('7') == 1:
            if i.count('9') + i.count('a') + i.count('b') <= 3:
                cnt += 1

print(cnt)