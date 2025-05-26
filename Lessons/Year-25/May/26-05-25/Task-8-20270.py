from itertools import product

cnt = 0

for i in product('0123456', repeat=5):
    if i[0] != '0':
        i = ''.join(i)
        for j in '35': i = i.replace(j, '1')
        for j in '246': i = i.replace(j, '0')
        i = i.replace('00', '@')
        if '@@' not in i and '0@' not in i and '@0' not in i and i.count('@') >= 2:
            cnt += 1

print(cnt)