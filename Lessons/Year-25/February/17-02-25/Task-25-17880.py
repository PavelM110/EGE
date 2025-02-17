from itertools import product

alph = '0123456789'

ans = []

for v1 in alph:
    for v2 in alph:
        for l in range(4):
            for z in product(alph, repeat=l):
                num = int(f'3{v1}12{v2}14{''.join(z)}5')
                if num <= 10**10:
                    if num % 1917 == 0: ans.append((num, num // 1917))

for i in sorted(ans):
    print(*i)