from itertools import product

cnt = 0

for i in product('01234567', repeat=5):
    i = ''.join(i)
    if i.count('6') == 1 and i[0] != '0':
        for j in '137': i = i.replace(j, '5')
        if '56' not in i and '65' not in i:
            cnt += 1

print(cnt)