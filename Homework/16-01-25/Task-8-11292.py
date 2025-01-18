from itertools import product

cnt = 0

for val in product('0123456789abcdef', repeat=5):
    val = ''.join(val)
    if val.count('6') == 2 and val[0] != '0':
        for i in '02468ace':
            val = val.replace(i, '6')
        if '66' not in val:
            cnt += 1

print(cnt)