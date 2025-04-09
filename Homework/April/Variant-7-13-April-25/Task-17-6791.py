with open('17_6791.txt') as file:
    data = [int(i) for i in file if i]

min_68 = min(i for i in data if abs(i) % 100 == 68)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    ua = abs(a) % 100 == 68
    ub = abs(b) % 100 == 68
    u1 = ua^ub
    u2 = a**2 + b**2 >= min_68**2
    if u1 and u2:
        ans.append(a**2 + b**2)

print(len(ans), max(ans))