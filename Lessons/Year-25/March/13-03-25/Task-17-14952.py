with open('17_14952.txt') as file:
    data = [int(i) for i in file if i]

max_121 = max(i for i in data if abs(i) % 1000 == 121)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua4 = 1000 <= abs(a) <= 9999
    ub4 = 1000 <= abs(b) <= 9999
    uc4 = 1000 <= abs(c) <= 9999
    ua2 = abs(a) % 2 == 0
    ub2 = abs(b) % 2 == 0
    uc2 = abs(c) % 2 == 0
    ua = ua4 and ua2
    ub = ub4 and ub2
    uc = uc4 and uc2
    f1 = ua + ub + uc <= 1
    summ = a + b + c
    f2 = summ <= max_121
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))