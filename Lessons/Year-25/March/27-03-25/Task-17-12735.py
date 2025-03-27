with open('17_12735.txt') as file:
    data = [int(i) for i in file if i]

max_09 = max(i for i in data if i % 100 == 9)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua = a % 7 == 0
    ub = b % 7 == 0
    uc = c % 7 == 0
    u1 = ua + ub + uc == 2
    summ = a + b + c
    if u1 and summ < max_09:
        ans.append(a*b*c)

print(len(ans), min(ans))
