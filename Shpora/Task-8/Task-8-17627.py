from itertools import product

cnt = 0

for val in product('0123456789ABCDE', repeat=5):
    if val[0] != '0':
        val = ''.join(val)
        if val.count('8') == 1:
            if sum(1 for i in val if i in 'ABCDE') >= 2:
                cnt += 1

print(cnt)