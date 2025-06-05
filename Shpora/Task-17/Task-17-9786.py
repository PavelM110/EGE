with open('17_9786.txt') as file: data = [int(i) for i in file if i]

maxx = max(i for i in data if abs(i) % 100 == 25)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua = 1000 <= abs(a) <= 9999
    ub = 1000 <= abs(b) <= 9999
    uc = 1000 <= abs(c) <= 9999
    if (ua + ub + uc) <= 2:
        if a + b + c <= maxx:
            ans.append(a + b + c)

print(len(ans), max(ans))