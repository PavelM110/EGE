from itertools import product

alph = '0123456789'

ans = []

for j in '0123456789':
    for l in range(4):
        for i in product(alph, repeat=l):
            num = int(f'12{''.join(i)}4{j}65')
            if num <= 10 ** 8 and num % 161 == 0: ans.append((num, num // 161))

for i in sorted(ans):
    print(*i)