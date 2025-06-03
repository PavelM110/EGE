from itertools import product

cnt = 0

for i in product('гепард', repeat=5):
    if i[0] != 'а' and i[-1] != 'е' and i.count('г') == 1:
        cnt += 1

print(cnt)