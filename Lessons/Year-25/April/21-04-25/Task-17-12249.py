with open('17_12249.txt') as file:
    data = [int(i) for i in file if i]

max_5_3 = max(i for i in data if 10000 <= abs(i) <= 99999 and abs(i) % 10 == 3)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    ua1 = abs(a) % 10 == 3
    ub1 = abs(b) % 10 == 3
    uc1 = abs(c) % 10 == 3
    u1 = ua1 or ub1 or uc1
    sum = a + b + c
    if u1 and sum <= max_5_3:
        ans.append(sum)

print(len(ans), max(ans))