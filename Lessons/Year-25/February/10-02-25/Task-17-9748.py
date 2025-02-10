with open('17_9748.txt') as file:
    data = [int(i) for i in file if i]

maxx = max([i for i in data if i%100 == 15])

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua4 = 1000 <= a <= 9999
    ub4 = 1000 <= b <= 9999
    uc4 = 1000 <= c <= 9999
    u1 = (ua4 + ub4 + uc4) == 1
    u2 = (a + b + c) >= maxx
    if u1 and u2:
        ans.append(a+b+c)

print(len(ans), max(ans))
