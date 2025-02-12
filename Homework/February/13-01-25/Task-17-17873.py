with open('17_17873.txt') as file:
    data = [int(i) for i in file if i]

minn = min(data)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    summ = a + b
    ua1 = a % 16 == minn
    ub1 = b % 16 == minn
    u1 = ua1 or ub1
    if u1: ans.append(summ)

print(len(ans), max(ans))