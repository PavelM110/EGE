from itertools import permutations

alph = 'макака'
cnt = 0

for i in set(permutations(alph)):
    i = ''.join(i)
    if 'аа' not in i and 'кк' not in i: cnt += 1

print(cnt)