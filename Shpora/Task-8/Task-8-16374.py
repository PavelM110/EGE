from itertools import product

cnt = 0

for i in product('0123456', repeat=7):
    i = ''.join(i)
    if i[0] != '0':
        if (i.count('0') + i.count('2') + i.count('4') + i.count('6')) == 2:
            cnt += 1

print(cnt)