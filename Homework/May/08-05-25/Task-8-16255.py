from itertools import product

cnt = 0

for i in product('012345678', repeat=7):
    i = ''.join(i)
    if i[0] not in '01357':
        if int(i[-1]) % 3:
            if '6' in i:
                cnt += 1

print(cnt)