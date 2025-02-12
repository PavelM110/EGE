with open('17_4705.txt') as file:
    data = [int(i) for i in file if i]

max_3 = max(i for i in data if abs(i) % 10 == 3)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    summ = a**2 + b**2
    ua1 = abs(a) % 10 == 3
    ub1 = abs(b) % 10 == 3
    u1 = ua1 ^ ub1
    u2 = summ >= max_3**2
    if u1 and u2: ans.append(summ)

print(len(ans), max(ans))