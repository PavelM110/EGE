with open('17_14260.txt') as file:
    data = [int(i) for i in file if i]

min_p_4_2 = min(i for i in data if i > 0 and 1000 <= i <= 9999 and str(i)[-1] == str(i)[-2])

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i + 3]
    summ = a + b + c
    ua1 = 100 <= abs(a) <= 999
    ub1 = 100 <= abs(b) <= 999
    uc1 = 100 <= abs(c) <= 999
    u1 = ua1 and ub1 and uc1
    u2 = summ > min_p_4_2
    if u1 and u2:
        ans.append(summ)

print(len(ans), max(ans))