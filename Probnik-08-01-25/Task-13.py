from itertools import product

cnt = 0

for p in product((0, 1), repeat=10):
    if 9 > (4 + sum(p)):
        cnt += 1

print(cnt)