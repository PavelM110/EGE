from itertools import permutations

cnt = 0

for val in permutations('0123456789ABCDEF', 3):
    val = ''.join(val)
    if val[0] != '0':
        for j in '3579BDF': val = val.replace(j, '1')
        for j in '2468ACE': val = val.replace(j, '0')
        if '11' not in val and '00' not in val:
            cnt += 1

print(cnt)