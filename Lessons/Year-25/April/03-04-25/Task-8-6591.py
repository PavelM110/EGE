from itertools import product, repeat

alph = '0123456'
cnt = 0

for i in product(alph, repeat=5):
    val = ''.join(i)
    if val[0] != '0':
        if val.count('6') == 1:
            if sum(int(i) for i in val if i in '246') < sum(int(i) for i in val if i in '135'):
                cnt += 1

print(cnt)