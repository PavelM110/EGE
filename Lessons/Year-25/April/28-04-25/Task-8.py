from itertools import product

cnt = 0

for i in product('123456789abcde', repeat=5):
    # if i[0] != '0':
        i = ''.join(i)
        # if i.count('0') == 2:
        for j in 'bcde': i = i.replace(j, 'a')
        if i.count('a') <= 3:
            cnt += 1

print(cnt * (5 + 4 + 3 + 2 + 1))
# 10875000
# 7598610
# (5 + 4 + 3 + 2 + 1)