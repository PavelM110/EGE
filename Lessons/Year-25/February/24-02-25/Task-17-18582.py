with open('17_18582.txt') as file:
    data = [int(i) for i in file if i]

minn = abs(min(data)) % 10

ans = []

for i in range(len(data)  - 2):
    a, b, c = data[i:i+3]
    ua1 = 1 if a < 0 else 0
    ub1 = 1 if b < 0 else 0
    uc1 = 1 if c < 0 else 0
    u1 = ua1 + ub1 + uc1 >= 2
    summ = sum(data[i:i+3])
    u2 = abs(summ) % 10 == minn
    if u1 and u2:
        ans.append(abs(summ))

print(len(ans), max(ans))