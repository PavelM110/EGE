with open('17_14952.txt') as file:
    data = [int(i) for i in file if i]

max_121 = max(i for i in data if abs(i) % 1000 == 121)

l = range(1000, 10000, 2)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    u1 = abs(a) in l
    u2 = abs(b) in l
    u3 = abs(c) in l
    f = u1 + u2 + u3 <= 1
    summ = a + b + c
    if f and summ <= max_121:
        ans.append(summ)

print(len(ans), max(ans))