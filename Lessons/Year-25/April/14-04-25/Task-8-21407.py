from itertools import product

cnt = 0

for i in product('ДГИАШЭ', repeat=5):
    if i[0] not in 'ИАЭ':
        if i[-1] not in 'ГДШ':
            cnt += 1

print(cnt)