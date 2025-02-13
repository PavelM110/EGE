with open('17_19249.txt') as file:
    data = [int(i) for i in file if i]

max_5_43 = max(i for i in data if 10000 <= abs(i) <= 99999 and abs(i) % 100 == 43)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    summ = a**2 + b**2 + c**2
    ua_5_43 = 10000 <= abs(a) <= 99999 and abs(a) % 100 == 43
    ub_5_43 = 10000 <= abs(b) <= 99999 and abs(b) % 100 == 43
    uc_5_43 = 10000 <= abs(c) <= 99999 and abs(c) % 100 == 43
    u1 = any((ua_5_43, ub_5_43, uc_5_43))
    u2 = summ <= max_5_43**2
    if u1 and u2: ans.append(summ)

print(len(ans), min(ans))