from itertools import product
from fnmatch import fnmatch

ans = []

for r1 in range(3):
    for r2 in range(3 - r1):
        for z1 in product('0123456789', repeat=r1):
            for z2 in product('0123456789', repeat=r2):
                num = f'124{''.join(z1)}5{''.join(z2)}79'
                summ_n = sum(int(i) for i in num if int(i) % 2 == 1)
                num = int(num)
                if num % summ_n == 0 and num < 10**8: ans.append((num, sum(int(i) for i in str(num))))

ans = sorted(ans)

# ans1 = []
#
# for num in range(124579, 10**8):
#     if fnmatch(str(num), '124*5*79'):
#         sum_n = sum(int(i) for i in str(num) if int(i) % 2 == 1)
#         if num % sum_n:
#             ans1.append((num, sum(int(i) for i in str(num))))
#
# ans1 = sorted(ans1)
#
# print(ans == ans1)

for i in ans: print(*i)