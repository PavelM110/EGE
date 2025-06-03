from itertools import product

cnt = 0

for i in product('ДГИАШЭ', repeat=5):
    if i[0] not in 'ИАЭ' and i[-1] not in 'ДГШ':
        cnt += 1

print(cnt)