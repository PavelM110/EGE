with open('17_17530.txt') as file:
    data = [int(i) for i in file if i]

minn = min(data)
ans = []
for i in range(len(data) - 1):
    a, b = data[i:i+2]
    u1 = a % 55 == minn
    u2 = b % 55 == minn
    if u1 or u2: ans.append(a + b)

print(len(ans), min(ans))