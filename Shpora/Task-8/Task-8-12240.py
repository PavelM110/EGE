from itertools import product

cnt = 0

for val in product('012345678', repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('5') == 1:
            if all(val[i] != val[i+1] for i in range(len(val) - 1)):
                cnt += 1

print(cnt)