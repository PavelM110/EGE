with open('17_17636.txt') as file:
    data = [int(i) for i in file if i]

max_3_3 = max(i for i in data if 100 <= abs(i) <= 999 and abs(i) % 10 == 3)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua1 = abs(a) % 10 == 3 and 100 <= abs(a) <= 999
    ub1 = abs(b) % 10 == 3 and 100 <= abs(b) <= 999
    uc1 = abs(c) % 10 == 3 and 100 <= abs(c) <= 999
    u1 = ua1 or ub1 or uc1
    summ = a + b + c
    if u1 and summ < max_3_3:
        ans.append(summ)

print(len(ans), max(ans))