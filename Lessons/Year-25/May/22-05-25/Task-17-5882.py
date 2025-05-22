with open('17_5882.txt') as file:
    data = [int(i) for i in file if i]

pairs = []

for i in range(len(data) - 1):
    a, b = data[i:i + 2]
    ua = abs(a) % 10 == 3
    ub = abs(b) % 10 == 3
    if ub != ua:
        pairs += [a, b]

min_3 = min(pairs)

summ = 0

for i in str(min_3).strip('-'):
    summ += int(i) ** 2

ans = []

for i in data:
    if i >= summ:
        if '3' in str(i):
            ans.append(i)

print(len(ans), min(ans))