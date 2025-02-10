with open('17_9840.txt') as file:
    data = [int(i) for i in file if i]

max_39 = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 100 == 39)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    ua4 = 1000 <= abs(a) <= 9999
    ub4 = 1000 <= abs(b) <= 9999
    u1 = ua4 ^ ub4
    u2 = ((a + b) ** 2) <= max_39 ** 2
    if u1 and u2: ans.append(a + b)

print(len(ans), max(ans))