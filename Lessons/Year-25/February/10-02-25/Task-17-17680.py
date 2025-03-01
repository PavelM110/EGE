with open('17_17680.txt') as file:
    data = [int(i) for i in file if i]

min_41 = min(i for i in data if i > 0 and i % 41 == 0)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    u1 = a != b
    u2 = abs(a - b) % min_41 == 0
    if u1 and u2: ans.append(a+b)

print(len(ans), max(ans))