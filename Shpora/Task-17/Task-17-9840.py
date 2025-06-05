with open('17_9840.txt') as file: data = [int(i) for i in file if i]

maxx = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 100 == 39)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    ua = 1000 <= abs(a) <= 9999
    ub = 1000 <= abs(b) <= 9999
    if ua != ub:
        if (a + b)**2 <= maxx**2:
            ans.append(a + b)

print(len(ans), max(ans))