from itertools import combinations

with open('17 (2)_7718.txt') as file:
    data = [int(i) for i in file if i]

ans = []

for a, b in combinations(data, 2):
    summ = a + b
    prod = a * b
    if (summ % 18 == 0) ^ (prod % 18 == 0):
        ans.append(summ)

print(len(ans), max(ans))