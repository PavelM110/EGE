from itertools import permutations

cnt = 0

for i in permutations('0123456789', 4):
    if i[0] != '0':
        i = ''.join(i)
        u = ''.join([str(int(j) % 2) for j in i])
        if '11' not in u and '00' not in u:
            cnt += 1

print(cnt)