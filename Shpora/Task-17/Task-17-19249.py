with open('17_19249 (1).txt') as file: data = [int(i) for i in file if i]

maxx = max(i for i in data if 10_000 <= abs(i) <= 99_999 and abs(i) % 100 == 43)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua = 10_000 <= abs(a) <= 99_999 and abs(a) % 100 == 43
    ub = 10_000 <= abs(b) <= 99_999 and abs(b) % 100 == 43
    uc = 10_000 <= abs(c) <= 99_999 and abs(c) % 100 == 43
    if ua or ub or uc:
        if a**2 + b**2 + c**2 <= maxx**2:
            ans.append(a**2 + b**2 + c**2)

print(len(ans), min(ans))