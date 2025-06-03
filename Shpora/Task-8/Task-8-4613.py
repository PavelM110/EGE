from itertools import product

cnt = 0

for i in product('012345678', repeat=5):
    if i[0] not in '01357':
        i = ''.join(i)
        if i.count('3') <= 1:
            if i[-1] not in '18':
                cnt += 1

print(cnt)