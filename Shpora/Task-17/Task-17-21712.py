with open('17_21712.txt') as file:
    data = [int(i) for i in file if i]

minn = min(i for i in data if 1000 <= i <= 9999 and i % 10 == 6)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua1 = 1000 <= abs(a) <= 9999 and abs(a) % 10 == 6
    ub1 = 1000 <= abs(b) <= 9999 and abs(b) % 10 == 6
    uc1 = 1000 <= abs(c) <= 9999 and abs(c) % 10 == 6
    u1 = (ua1 + ub1 + uc1) == 1
    if u1 and (a + b + c) <= minn:
        ans.append(a + b + c)

print(len(ans), max(ans))