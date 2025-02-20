from itertools import product, repeat

ans = []

for a in '02468':
    for r in range(5):
        for b in product('13579', repeat=r):
            num = int(f'1{a}2157{''.join(b)}4')
            if num % 133 == 0 and num < 10**10: ans.append((num, num // 133))

ans = sorted(ans)

for i in ans:
    print(*i)