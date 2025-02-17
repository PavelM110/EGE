from itertools import product

for l in range(4):
    for i in product('0123456789', repeat=l):
        num = int(f'1234{''.join(i)}7')
        if num % 141 == 0: print(num, num // 141)