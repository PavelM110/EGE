from itertools import product

cnt = 0

for i in product('01234567', repeat=5):
    if i[0] != '0':
        i = ''.join(i)
        if i.count('6') == 1:
            for j in '024': i = i.replace(j, '6')
            if '66' not in i:
                cnt += 1

print(cnt)