with open('17_17636.txt') as file:
    data = [int(i) for i in file if i]

max_3_3 = max(i for i in data if 100 <= abs(i) <= 999 and abs(i) % 10 == 3)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua = 100 <= abs(a) <= 999 and abs(a) % 10 == 3
    ub = 100 <= abs(b) <= 999 and abs(b) % 10 == 3
    uc = 100 <= abs(c) <= 999 and abs(c) % 10 == 3
    u1 = ua or ub or uc
    summ = a + b + c
    u2 = summ < max_3_3
    if u1 and u2: ans.append(summ)

print(len(ans), max(ans))