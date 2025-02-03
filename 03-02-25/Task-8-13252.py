from itertools import permutations

alph = 'кидала'
cnt = 0

for i in set(permutations(alph, 5)):
    i = ''.join(i)
    if 'аа' not in i: cnt += 1

print(cnt)