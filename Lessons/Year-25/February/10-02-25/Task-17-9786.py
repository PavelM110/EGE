with open('17_9786.txt') as file:
    data = [int(i) for i in file if i]

max_25 = max([i for i in data if abs(i) % 100 == 25])

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua4 = 1000 <= abs(a) <= 9999
    ub4 = 1000 <= abs(b) <= 9999
    uc4 = 1000 <= abs(c) <= 9999
    u1 = (ua4 + ub4 + uc4) != 3
    u2 = a+b+c <= max_25
    if u1 and u2:
        ans.append(a+b+c)

print(len(ans), max(ans))