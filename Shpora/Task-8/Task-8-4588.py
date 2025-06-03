from itertools import product

cnt = 0

for i in product('01234567', repeat=5):
    if i[0] != '0':
        i = ''.join(i)
        for j in '357': i = i.replace(j, '1')
        if i.count('6') == 1:
            if '16' not in i and '61' not in i:
                cnt += 1

print(cnt)