from itertools import product, repeat

cnt = 0

for p in product('abcdef', repeat=6):
    p = ''.join(p)
    if p[0] not in 'ae' and p[-1] not in 'ae':
        cnt += 1

print(cnt)