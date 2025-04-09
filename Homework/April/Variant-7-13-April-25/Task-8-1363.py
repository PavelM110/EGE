from itertools import product

cnt = 0

for i in product('01234', repeat=5):
    i = int('3'+''.join(i), 5)
    if not i % 2:
        cnt += 1

print(cnt)