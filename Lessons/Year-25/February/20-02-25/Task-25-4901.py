from itertools import product

def f(num):
    dell = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0: dell.append(i)
    return sum(dell)

ans = []

for r1 in range(5):
    for r2 in range(5):
         for z1 in product('0123456789', repeat=r1):
             for z2 in product('0123456789', repeat=r2):
                 for v1 in '123456789':
                     for v2 in '0123456789':
                         num = int(f'{v1}6{''.join(z1)}6{''.join(z2)}{v2}6')
                         if num % 6 == 0 and num % 7 == 0 and num % 8 == 0:
                            if len(ans) < 7:
                                ans.append((num, f(num)))
                            else: flag = True

ans = sorted(ans)

for i in ans: print(*i)