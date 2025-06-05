with open('17_17530.txt') as file: data = [int(i) for i in file if i]

minn = min(data)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    if a % 55 == minn or b % 55 == minn:
        ans.append(a + b)

print(len(ans), min(ans))