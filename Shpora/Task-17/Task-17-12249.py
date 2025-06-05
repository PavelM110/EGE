with open('17_12249.txt') as file: data = [int(i) for i in file if i]

maxx = max(i for i in data if 10_000 <= abs(i) <= 99_999 and abs(i) % 10 == 3)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    if abs(a) % 10 == 3 or abs(b) % 10 == 3 or abs(c) % 10 == 3:
        if a + b + c <= maxx:
            ans.append(a + b + c)

print(len(ans), max(ans))