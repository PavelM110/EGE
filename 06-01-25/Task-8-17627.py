from itertools import product

alph = '0123456789abcde'
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and sum([val.count(i) for i in val if i in 'abcde']) >= 2:
        cnt += 1

print(cnt)