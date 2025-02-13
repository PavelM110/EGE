from itertools import product

num = 3 * 15**1140 + 2 * 15**1025 + 15**923 - 3 * 15**85 + 2 * 15**74 + 3

alph = '0123456789abcdef'

res = ''
while num:
    res += str(alph[num % 15])
    num //= 15

res = res[::-1]

print(res)

for i in product(alph, repeat=2):
    i = ''.join(i)
    if i[0] != i[1]:
        res = res.replace(i, f'{i[0]} {i[1]}')

res = res.split()

print(res)

print(len(max(res, key=len)))