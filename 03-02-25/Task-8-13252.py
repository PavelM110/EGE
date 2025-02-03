from itertools import permutations

alph = 'кидал'
cnt = 0

for i in permutations(alph):
    i = ''.join(i)
    if 'аа' not in i: cnt += 1

print(cnt)