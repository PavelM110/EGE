with open('17_14952.txt') as file:
    data = [int(i) for i in file if i]

max_121 = max(i for i in data if abs(i) % 1000 == 121)

ans = []

l = range(1000, 9999, 2)

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua = abs(a) in l
    ub = abs(b) in l
    uc = abs(c) in l
    f1 = ua + ub + uc <= 1
    summ = a + b + c
    f2 = summ <= max_121
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))