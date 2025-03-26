with open('1706.txt') as file:
    data = [int(i) for i in file if i]

min_3_19_2 = min(i for i in data if abs(i) % 100 == 19 and 100 <= abs(i) <= 999) ** 2

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    summ = a + b + c
    ua = abs(a) % 100 == 19 and 10_000 <= abs(a) <= 99_999
    ub = abs(b) % 100 == 19 and 10_000 <= abs(b) <= 99_999
    uc = abs(c) % 100 == 19 and 10_000 <= abs(c) <= 99_999
    f1 = ua or ub or uc
    f2 = summ > min_3_19_2
    if f1 and f2:
        ans.append(summ)

print(len(ans), min(ans))