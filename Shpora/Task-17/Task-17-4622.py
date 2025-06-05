with open('17_4622.txt') as file: data = [int(i) for i in file if i]

minn = min(i for i in data if i > 0 and abs(i) % 19 == 0)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    if a + b < minn:
        ans.append(a + b)

print(len(ans), abs(max(ans)))