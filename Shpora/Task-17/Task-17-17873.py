with open('17_17873.txt') as file:
    data = [int(i) for i in file if i]

minn = min(data)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    ua = a % 16 == minn
    ub = b % 16 == minn
    if ua or ub:
        ans.append(a + b)

print(len(ans), max(ans))