with open('17_21416.txt') as file:
    data = [int(i) for i in file if i]

summ = 0

for i in data:
    if i < 0: summ += i

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    prod = max(a, b, c) * min(a, b, c)
    if prod > summ:
        ans.append(a + b + c)

print(len(ans), abs(max(ans)))