with open('17_16383.txt') as file: data = [int(i) for i in file if i]

maxx = max(i for i in data if 10_000 <= abs(i) <= 99_999 and abs(i) % 100 == 21)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    ua = 10_000 <= abs(a) <= 99_999 and abs(a) % 100 == 21
    ub = 10_000 <= abs(b) <= 99_999 and abs(b) % 100 == 21
    if ua != ub:
        if a**2 + b**2 >= maxx**2:
            ans.append(a + b)

print(len(ans), max(ans))