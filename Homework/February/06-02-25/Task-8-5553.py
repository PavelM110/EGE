from itertools import permutations

alph = 'соточка'
cnt = 0

for i in set(permutations(alph)):
    i = ''.join(i)
    if 'оо' in i or 'оа' in i or 'ао' in i:
        cnt += 1

print(cnt)